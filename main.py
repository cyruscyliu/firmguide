import argparse
import logging.config

from supervisor.scheduler import run, INPUT
from supervisor.logging_setup import setup_logging

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
