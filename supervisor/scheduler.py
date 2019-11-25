import argparse
import logging
import multiprocessing

from analyses.trace.collection import trace_collection
from analyses.trace.format import QEMUDebug, KTracer
from database.dbf import get_database
from generation.compiler import CompilerToQEMUMachine
from supervisor.error_handling import error_callback
from supervisor.save_and_restore import setup, check_and_restore, save_analysis
from supervisor.tasks import static_analysis, trace_diagnosis

logger = logging.getLogger()


def run(args):
    if args.trace_format == 'qemudebug':
        trace = QEMUDebug(args.trace)
    else:  # 'ktracer'
        trace = KTracer(args.trace)

    # handle diagnosis early
    if args.trace:
        trace_diagnosis(trace)
        return

    # normal routine
    dbp = get_database('paused')
    dbi = get_database(args.database_type, profile=args.profile)
    analysis_pool = multiprocessing.Pool(4)
    for firmware in dbi.get_firmware():
        if args.uuid is not None and firmware.uuid not in args.uuid:
            continue
        if args.limit and firmware.id > args.limit:
            continue
        analysis_pool.apply_async(
            analysis_wrapper, (firmware, args, dbp), error_callback=error_callback)
    analysis_pool.close()
    analysis_pool.join()


def analysis_wrapper(firmware, args, dbp):
    setup(args, firmware)
    check_and_restore(firmware, rerun=args.rerun)
    # perform static analysis
    try:
        static_analysis(firmware)
    except NotImplementedError as e:
        firmware, analysis = e.args
        logger.warning('\033[31mcan not support firmware {}, fix and rerun\033[0m'.format(firmware.uuid))
        dbp.add(uuid=firmware.uuid, name=firmware.name, hint=analysis.context['hint'], input=analysis.context['input'])
    save_analysis(firmware)

    # the following code are not tested, so we return here
    return
    # perform code generation
    machine_compiler = CompilerToQEMUMachine()
    machine_compiler.solve(firmware)
    machine_compiler.link(firmware)
    machine_compiler.install(firmware)

    # perform dynamic inference
    trace_format = args.trace_format
    path_to_trace = 'log/{}.trace'.format(firmware.uuid)
    if trace_format == 'qemudebug':
        trace = QEMUDebug(path_to_trace)
    else:  # 'ktracer'
        trace = KTracer(path_to_trace)
    while trace.scan_user_level():
        logger.info('GOOD! Have entered the user level!')
        trace_collection(firmware)
        trace_diagnosis(trace)
