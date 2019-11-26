#!/usr/bin/python

import argparse
import logging.config

from supervisor.scheduler import run
from supervisor.logging_setup import setup_logging

if __name__ == '__main__':
    parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter)
    # firmware source, device profile and working directory
    parser.add_argument('-dbt', '--database_type', choices=['text', 'firmadyne'], default='text',
                        type=str, help='assign the firmware db type')
    parser.add_argument('-p', '--profile', choices=['simple', 'dt', 'ipxact'], default='dt',
                        help='assign the device profile standard')
    parser.add_argument('-wd', '--working_directory',
                        help='assign the working directory for getting metadata, by default /tmp or %%TEMP%%')
    # precise control
    parser.add_argument('-l', '--limit', type=int, default=0,
                        help='limit the amount of firmware to test')
    parser.add_argument('-r', '--rerun', action='store_true', default=False,
                        help='ingore save and restore and rerun all analysis')
    parser.add_argument('-u', '--uuid', type=str, nargs='+',
                        help='assign a uuid to a firmware in the firmware db')
    # debug
    parser.add_argument('-d', '--debug', action='store_true', help='show verbose logs')
    # diagnosis group
    group = parser.add_argument_group('diagnosis')
    group.add_argument('-t', '--trace', type=str, help='assign a trace file')
    group.add_argument('-tf', '--trace_format', type=str, choices=['ktracer', 'qemudebug'], default='qemudebug',
                       help='assign a trace file format')
    args = parser.parse_args()
    if args.debug:
        setup_logging(default_level=logging.DEBUG)
    else:
        setup_logging(default_level=logging.INFO)
    logger = logging.getLogger()
    run(args)
