import qmp
import subprocess

from analyses.abelia import AbeliaRAM
from analyses.check import Checking
from analyses.analysis import AnalysesManager
from analyses.device_tree import DeviceTree
from analyses.dot_config import DotConfig
from analyses.extraction import Extraction
from analyses.format import Format
from analyses.init_value import InitValue
from analyses.dead_loop import DeadLoop
from analyses.kernel import Kernel
from analyses.openwrt import OpenWRTRevision, OpenWRTURL, OpenWRTToH
from analyses.srcode import SRCode
from analyses.strings import Strings
from generation.compilerf import get_compiler
from profile.firmwaref import get_firmware_in_profile
from supervisor.logging_setup import logger_info, logger_warning
from supervisor.save_and_restore import check_and_restore, save_analysis, setup_diagnosis, setup_code_generation, \
    setup_single_analysis


def run_diagnosis(firmware):
    analyses_manager = AnalysesManager(firmware)
    analyses_manager.register_analysis(DeadLoop(), no_chained=True)
    analyses_manager.run_analysis(firmware, 'dead_loop')


def run_single_analysis(firmware):
    analysis_wrapper(firmware)


def run_code_generation(firmware):
    analysis_wrapper(firmware)


def run(parser, args):
    firmware = get_firmware_in_profile(args.profile)
    if args.trace:
        setup_diagnosis(args, firmware)
        run_diagnosis(firmware)
    elif args.generation:
        setup_code_generation(args, firmware)
        run_code_generation(firmware)
    elif args.uuid:
        setup_single_analysis(args, firmware)
        run_single_analysis(firmware)
    else:
        parser.print_help()


def register_analysis(firmware, no_inference=False):
    analyses_manager = AnalysesManager(firmware)
    # format <- extraction
    analyses_manager.register_analysis(Format(), no_chained=no_inference)
    analyses_manager.register_analysis(Extraction(), no_chained=no_inference)
    # extraction <- kernel
    analyses_manager.register_analysis(Kernel(), no_chained=no_inference)
    # extraction <- dt
    analyses_manager.register_analysis(DeviceTree(), no_chained=no_inference)
    # extraction, revision <- strings
    analyses_manager.register_analysis(Strings(), no_chained=no_inference)
    # kernel <- revision
    analyses_manager.register_analysis(OpenWRTRevision(), no_chained=no_inference)
    # revision, url <- toh
    analyses_manager.register_analysis(OpenWRTURL(), no_chained=no_inference)
    analyses_manager.register_analysis(OpenWRTToH(), no_chained=no_inference)
    # toh <- ram by default
    analyses_manager.register_analysis(AbeliaRAM(), no_chained=no_inference)
    # srcode <- .config
    # analyses_manager.register_analysis(SRCode(), no_chained=no_inference)
    # analyses_manager.register_analysis(DotConfig(), no_chained=no_inference)
    # other analysis
    analyses_manager.register_analysis(Checking(), no_chained=True)
    analyses_manager.register_analysis(DeadLoop(), no_chained=True)
    analyses_manager.register_analysis(InitValue(), no_chained=True)
    return analyses_manager


def analysis_wrapper(firmware):
    check_and_restore(firmware)

    analyses_manager = register_analysis(firmware, no_inference=firmware.no_inference)

    try:
        # run them all
        analyses_manager.run()
        save_analysis(firmware)

        while not firmware.do_not_diagnosis:  # exit early
            # perform code generation
            machine_compiler = get_compiler(firmware)
            machine_compiler.solve()
            machine_compiler.link_and_install()
            running_command = machine_compiler.make()
            # perform dynamic checking
            if trace_collection(firmware, running_command):
                raise SystemError('bugs in tracing or before')
            analyses_manager.run_analysis(firmware, 'check')
            if analyses_manager.last_analysis_status:
                logger_info(
                    firmware.get_uuid(), 'analysis', 'checking analysis', 'GOOD! Have entered the user level!', 1)
                break
            logger_info(
                firmware.get_uuid(), 'analysis', 'checking analysis', 'BAAD! Have not entered the user level!', 0)
            analyses_manager.run_analysis(firmware, 'dead_loop')
            analyses_manager.run_analysis(firmware, 'init_value')
            break
    except NotImplementedError as e:
        exception = e.args[0]
        if isinstance(exception, str):
            logger_warning(firmware.get_uuid(), 'scheduler', 'exception', '{}, fix and rerun'.format(exception), 0)
        else:
            logger_warning(firmware.get_uuid(), 'scheduler', 'exception', 'can not support firmware, fix and rerun', 0)
    except SystemError as e:
        logger_warning(firmware.get_uuid(), 'scheduler', 'exception', e.__str__(), 0)


def trace_collection(firmware, running_command):
    # nochain is too too slow
    trace_flags = '-d in_asm,int,cpu -D {}'.format(firmware.path_to_trace)
    qmp_flags = '-qmp tcp:localhost:4444,server,nowait'
    full_command = ' '.join([running_command, trace_flags, qmp_flags])
    try:
        logger_info(firmware.get_uuid(), 'tracing', 'qemudebug', full_command, 0)
        status = subprocess.run(full_command, timeout=60, shell=True).returncode
    except subprocess.TimeoutExpired:
        status = 0
        qemu = qmp.QEMUMonitorProtocol(('localhost', 4444))
        qemu.connect()
        qemu.cmd('quit')
        qemu.close()
    return status
