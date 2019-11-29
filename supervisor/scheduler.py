import os
import multiprocessing
import subprocess
import qmp

from analyses.check import Checking
from analyses.common.analysis import AnalysesManager
from analyses.device_tree import DeviceTree
from analyses.dot_config import DotConfig
from analyses.extraction import Extraction
from analyses.format import Format
from analyses.init_value import InitValue
from analyses.kernel import Kernel
from analyses.openwrt import OpenWRTRevision, OpenWRTURL, OpenWRTToH
from analyses.srcode import SRCode
from analyses.strings import Strings
from analyses.dead_loop import DeadLoop
from database.dbf import get_database
from generation.compiler import CompilerToQEMUMachine
from profile.pff import get_firmware_in_profile
from profile.tinyft import TinyForTestFirmware
from supervisor.logging_setup import logger_info, logger_warning
from supervisor.save_and_restore import setup, check_and_restore, save_analysis


def error_callback(e):
    # keep this
    pass


def run_diagnosis(args):
    firmware = TinyForTestFirmware(**{'uuid': '0', 'path': 'no/path', 'size': 0, 'name': 'TinyForTestFirmware'})
    setup(args, firmware)
    analyses_manager = AnalysesManager()
    analyses_manager.register_analysis(DeadLoop(), no_chained=True)
    analyses_manager.run_analysis(firmware, 'dead_loop')


def run_single_analysis(args):
    firmware = get_firmware_in_profile(args.profile, **{
        'uuid': args.id,
        'name': os.path.basename(args.firmware),
        'path': args.firmware,
        'size': os.path.getsize(args.firmware)
    })
    firmware.preset_cache = [
        (firmware.set_brand, args.brand),
        (firmware.set_architecture, args.arch),
        (firmware.set_endian, args.endian)
    ]
    setup(args, firmware)
    analysis_wrapper(firmware)


def run_massive_analyses(args):
    # normal routine
    dbi = get_database(args.database_type, profile=args.profile)
    analysis_pool = multiprocessing.Pool(1)
    for firmware in dbi.get_firmware():
        if args.uuid is not None and firmware.uuid not in args.uuid:
            continue
        if args.limit and firmware.id > args.limit:
            continue
        setup(args, firmware)
        # analysis_pool.apply_async(
        #     analysis_wrapper, (firmware), error_callback=error_callback)
        analysis_wrapper(firmware)
    analysis_pool.close()
    analysis_pool.join()


def run(parser, args):
    if args.trace:
        run_diagnosis(args)
    elif args.firmware:
        run_single_analysis(args)
    elif args.database_type:
        run_massive_analyses(args)
    else:
        parser.print_help()


def analysis_wrapper(firmware):
    check_and_restore(firmware)

    analyses_manager = AnalysesManager()
    # format <- extraction
    analyses_manager.register_analysis(Format())
    analyses_manager.register_analysis(Extraction())
    # extraction <- kernel
    analyses_manager.register_analysis(Kernel())
    # extraction <- dt
    analyses_manager.register_analysis(DeviceTree())
    # extraction, revision <- strings
    analyses_manager.register_analysis(Strings())
    # kernel <- revision
    analyses_manager.register_analysis(OpenWRTRevision())
    # revision, url <- toh
    analyses_manager.register_analysis(OpenWRTURL())
    analyses_manager.register_analysis(OpenWRTToH())
    # srcode <- .config
    analyses_manager.register_analysis(SRCode())
    analyses_manager.register_analysis(DotConfig())
    # run them all
    analyses_manager.run(firmware)

    # other analysis
    analyses_manager.register_analysis(Checking(), no_chained=True)
    analyses_manager.register_analysis(DeadLoop(), no_chained=True)
    analyses_manager.register_analysis(InitValue(), no_chained=True)
    try:
        while 1:
            # perform code generation
            machine_compiler = CompilerToQEMUMachine()
            machine_compiler.solve(firmware)
            machine_compiler.link(firmware)
            machine_compiler.install(firmware)
            machine_compiler.run(firmware)
            if firmware.do_not_diagnosis:  # exit early
                break
            # perform dynamic checking
            trace_collection(firmware)
            analyses_manager.run_analysis(firmware, 'check')
            if analyses_manager.last_analysis_status:
                break
            logger_info(firmware.uuid, 'analysis', 'checking analysis', 'BAAD! Have not entered the user level!', 0)
            analyses_manager.run_analysis(firmware, 'dead_loop')
            analyses_manager.run_analysis(firmware, 'init_value')
            break
    except NotImplementedError as e:
        firmware, analysis = e.args
        logger_warning(firmware.uuid, 'scheduler', 'exception', 'can not support this firmware, fix and rerun', 0)

    logger_info(firmware.uuid, 'analysis', 'checking analysis', 'GOOD! Have entered the user level!', 1)
    save_analysis(firmware)


def trace_collection(firmware):
    running_command = firmware.get_running_command()
    # nochain is too too slow
    trace_flags = '-d in_asm,cpu -D log/{}.trace'.format(firmware.uuid)
    qmp_flags = '-qmp tcp:localhost:4444,server,nowait'
    full_command = ' '.join([running_command, trace_flags, qmp_flags])
    try:
        logger_info(firmware.uuid, 'tracing', 'qemudebug', full_command, 0)
        subprocess.run(full_command, timeout=60, shell=True)
    except subprocess.TimeoutExpired:
        qemu = qmp.QEMUMonitorProtocol(('localhost', 4444))
        qemu.connect()
        qemu.cmd('quit')
        qemu.close()
