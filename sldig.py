#!/usr/bin/python

import argparse
import logging.config

from supervisor.scheduler import run
from supervisor.logging_setup import setup_logging

logger = logging.getLogger()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument('-d', '--debug', action='store_true', help='show verbose logs')

    # diagnosis
    group = parser.add_argument_group('diagnosis')
    group.add_argument('-t', '--trace', type=str, metavar='path/to/uuid-arch.endian.trace')
    group.add_argument('-tf', '--trace_format', type=str, choices=['ktracer', 'qemudebug'], default='qemudebug')
    group.add_argument('-m', '--max', type=int, help='max iteration', default=20)

    args = parser.parse_args()
    if args.debug:
        setup_logging(default_level=logging.DEBUG)
    else:
        setup_logging(default_level=logging.INFO)

    run(parser, args)
