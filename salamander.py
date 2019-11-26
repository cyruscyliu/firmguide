#!/usr/bin/python

import argparse
import logging.config

from supervisor.scheduler import run
from supervisor.logging_setup import setup_logging

if __name__ == '__main__':
    parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter)
    # general
    parser.add_argument('-p', '--profile', choices=['simple', 'dt', 'ipxact'], default='dt',
                        help='assign the device profile standard')
    parser.add_argument('-wd', '--working_directory',
                        help='assign the working directory for getting metadata, by default /tmp or %%TEMP%%')
    parser.add_argument('-r', '--rerun', action='store_true', default=False,
                        help='ingore save and restore and rerun all analysis')
    parser.add_argument('-d', '--debug', action='store_true', help='show verbose logs')
    # single analysis
    group = parser.add_argument_group('single analysis')
    group.add_argument('-f', '--firmware', type=str, help='path to firmware')
    group.add_argument('-i', '--id', type=int, help='assign a id to the firmware')
    group.add_argument('-a' '--architecture', type=str, help='assign the architecture', choices=['arm', 'mips'])
    group.add_argument('-e', '--endian', type=str, help='assign the endian', choices=['b', 'l'])
    group.add_argument('-b', '--brand', type=str, help='assign the brand of this firmware', choices=['openwrt'])
    # massive analyses
    group = parser.add_argument_group('massive analyses')
    group.add_argument('-dbt', '--database_type', choices=['text', 'firmadyne'], default='text',
                        type=str, help='assign the firmware db type')
    group.add_argument('-l', '--limit', type=int, default=0,
                        help='limit the amount of firmware to test')
    group.add_argument('-u', '--uuid', type=str, nargs='+',
                        help='assign a uuid to a firmware in the firmware db')
    # diagnosis
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
    run(parser, args)
