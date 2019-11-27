import os
import logging
import multiprocessing
import subprocess
import qmp

from analyses.check import Checking
from analyses.common.analysis import AnalysesManager
from analyses.device_tree import DeviceTree
from analyses.dot_config import DotConfig
from analyses.extraction import Extraction
from analyses.format import Format
from analyses.kernel import Kernel
from analyses.openwrt import OpenWRTRevision, OpenWRTURL, OpenWRTToH
from analyses.srcode import SRCode
from analyses.strings import Strings
from analyses.dead_loop import DeadLoop
from database.dbf import get_database
from generation.compiler import CompilerToQEMUMachine
from profile.pff import get_firmware_in_profile
from supervisor.error_handling import error_callback
from supervisor.save_and_restore import setup, check_and_restore, save_analysis

logger = logging.getLogger()


def run_diagnosis(args):
    trace_format = args.trace_format
    path_to_trace = args.trace
    analyses_manager = AnalysesManager()
    analyses_manager.register_analysis(DeadLoop(), no_chained=True)
    analyses_manager.run_analysis(None, 'dead_loop', trace_format, path_to_trace)


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
    analysis_wrapper(firmware, args)


def run_massive_analyses(args):
    # normal routine
    dbi = get_database(args.database_type, profile=args.profile)
    analysis_pool = multiprocessing.Pool(1)
    for firmware in dbi.get_firmware():
        if args.uuid is not None and firmware.uuid not in args.uuid:
            continue
        if args.limit and firmware.id > args.limit:
            continue
        analysis_pool.apply_async(
            analysis_wrapper, (firmware, args), error_callback=error_callback)
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


def analysis_wrapper(firmware, args):
    setup(args, firmware)
    check_and_restore(firmware, rerun=args.rerun)

    trace_format = args.trace_format
    path_to_trace = 'log/{}.trace'.format(firmware.uuid)

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
    try:
        while 1:
            # perform code generation
            machine_compiler = CompilerToQEMUMachine()
            machine_compiler.solve(firmware)
            machine_compiler.link(firmware)
            machine_compiler.install(firmware)
            machine_compiler.run(firmware)
            # perform dynamic checking
            trace_collection(firmware)
            if analyses_manager.run_analysis(firmware, 'check', trace_format, path_to_trace):
                break
            logger.info('BAAD! Have not entered the user level!')
            analyses_manager.run_analysis(firmware, 'dead_loop', trace_format, path_to_trace)
            # analysis, args = trace.diagnosis()
            # analyses_manager.run_analysis(firmware, analysis, args)
    except NotImplementedError as e:
        firmware, analysis = e.args
        logger.warning('\033[31mcan not support firmware {}, fix and rerun\033[0m'.format(firmware.uuid))
        # dbp.add(uuid=firmware.uuid, name=firmware.name, hint=analysis.context['hint'],
        #         input=analysis.context['input'])

    logger.info('GOOD! Have entered the user level!')
    save_analysis(firmware)


def trace_collection(firmware):
    running_command = firmware.get_running_command()
    # nochain is too too slow
    trace_flags = '-d in_asm,cpu -D log/{}.trace'.format(firmware.uuid)
    qmp_flags = '-qmp tcp:localhost:4444,server,nowait'
    full_command = ' '.join([running_command, trace_flags, qmp_flags])
    try:
        logger.info('tracing ...')
        subprocess.run(full_command, timeout=30, shell=True)
    except subprocess.TimeoutExpired:
        qemu = qmp.QEMUMonitorProtocol(('localhost', 4444))
        qemu.connect()
        qemu.cmd('quit')
        qemu.close()
    logger.info('trace at log/{}.trace'.format(firmware.uuid))
