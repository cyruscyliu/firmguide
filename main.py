import argparse
import logging.config
import multiprocessing

from database.dbf import get_database
from manager import analysis_wrapper, setup_logging


def run(args):
    dbi = get_database(dbtype=args.dbt, uuid=args.uuid, profile=args.profile)
    analysis_pool = multiprocessing.Pool(4)
    for firmware in dbi.get_firmware():
        analysis_pool.apply_async(analysis_wrapper, (firmware,))
    analysis_pool.close()
    analysis_pool.join()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group()
    group.add_argument('-dbt', '--database_type', choices=['text', 'firmadyne'], type=str,
                       help='assign the firmware db type')
    group.add_argument('-u', '--uuid', type=int, nargs='+',
                       help='assign a uuid to an paused analysis')
    parser.add_argument('-d', '--debug', action='store_true', help='show verbose logs')
    parser.add_argument('-p', '--profile', choices=['simple', 'dt', 'ipxact'], default='dt',
                        help='assign the device profile standard')
    parser.add_argument('-wd', '--working_directory',
                        help='assign the working directory for getting metadata, '
                             'save and store mechanism is on except by default /tmp or %%TEMP%%')
    args = parser.parse_args()
    if args.debug:
        setup_logging(default_level=logging.DEBUG)
    else:
        setup_logging(default_level=logging.INFO)
    run(args)
