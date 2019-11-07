import argparse
import logging
import multiprocessing

from database.dbf import get_database
from supervisor.error_handling import error_callback
from supervisor.save_and_restore import setup, check_and_restore, save_analysis
from supervisor.tasks import analysis, trace_diagnosis

logger = logging.getLogger()


def run(args):
    if args.trace:
        trace_diagnosis(args.trace, args.trace_format)
        return

    dbp = get_database('paused')
    if args.fix:
        args.uuid = dbp.select('uuid')
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
    try:
        analysis(firmware)
    except NotImplementedError as e:
        # e.args[0] = {'hint': 'the hint', 'input': 'what is the input'}
        logger.warning('\033[31mcan not support firmware {}, fix and rerun\033[0m'.format(firmware.uuid))
        dbp.add(uuid=firmware.uuid, name=firmware.name, hint=e.args[0]['hint'], input=e.args[0]['input'])
    save_analysis(firmware)


class INPUT(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        fixes = {}
        for value in values:
            k, v = value.split('=')
            fixes[k] = v
        setattr(namespace, self.dest, fixes)
