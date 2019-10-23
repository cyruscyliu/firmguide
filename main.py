import argparse
import logging.config
import multiprocessing

from analyses.cpu import get_cpu_model_info
from analyses.extraction import extract_kernel_and_dtb
from analyses.flash import get_flash_info
from analyses.ic import get_ic_info
from analyses.metadata import get_metadata
from analyses.ram import get_ram_info
from analyses.srcode import get_source_code
from analyses.timer import get_timer_info
from analyses.uart import get_uart_info

from database.dbf import get_database
from manager import setup_logging, setup, check_and_restore, save_analysis


def error_callback(e):
    try:
        raise e
    except Exception as e:
        logger.exception(e)


def run(args):
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
            analysis_wrapper, (firmware, dbp, args.rerun), error_callback=error_callback)
    analysis_pool.close()
    analysis_pool.join()


def analysis(firmware):
    # let's start
    extract_kernel_and_dtb(firmware)
    get_metadata(firmware)
    get_source_code(firmware)
    get_cpu_model_info(firmware)
    get_ram_info(firmware)
    get_flash_info(firmware)
    get_uart_info(firmware)
    get_ic_info(firmware)
    get_timer_info(firmware)


def analysis_wrapper(firmware, dbp, rerun):
    setup(args, firmware)
    check_and_restore(firmware, rerun=rerun)
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


if __name__ == '__main__':
    parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument('-dbt', '--database_type', required=True, choices=['text', 'firmadyne'],
                        type=str, help='assign the firmware db type')
    parser.add_argument('-d', '--debug', action='store_true', help='show verbose logs')
    parser.add_argument('-i', '--input', type=str, nargs='+', action=INPUT,
                        metavar='k1=v1 k2=v2',
                        help='fix paused analyses')
    parser.add_argument('-l', '--limit', type=int, default=0,
                        help='limit the amount of firmware we test')
    parser.add_argument('-r', '--rerun', action='store_true', default=False,
                        help='rerun all analysis')
    parser.add_argument('-p', '--profile', choices=['simple', 'dt', 'ipxact'], default='dt',
                        help='assign the device profile standard')
    group = parser.add_mutually_exclusive_group()
    group.add_argument('-u', '--uuid', type=str, nargs='+',
                       help='assign a uuid to an paused analysis')
    group.add_argument('-f', '--fix', type=str, choices=['all'],
                       help='assign a file to paused analyses')
    parser.add_argument('-wd', '--working_directory',
                        help='assign the working directory for getting metadata, '
                             'save and store mechanism is on except by default /tmp or %%TEMP%%')
    args = parser.parse_args()
    if args.debug:
        setup_logging(default_level=logging.DEBUG)
    else:
        setup_logging(default_level=logging.INFO)
    logger = logging.getLogger()
    run(args)
