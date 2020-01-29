#!/usr/bin/python3.7

import os
import argparse
import logging.config

from logger import setup_logging, logger_info
from slcore.environment import setup_target_dir # uuid
from slcore.compositor import unpack # components
from slcore.machines import find_machine # components
from slcore.environment import migrate, snapshot # components + firmware
from slcore.scheduler import run_static_analysis, run_dynamic_analysis # firmware

def run(args):
    # 1. setup a working dir
    target_dir = setup_target_dir(args.uuid)

    # 2. find a prepared machine
    components = unpack(args.firmware, uuid=args.uuid, arch=args.architecture, endian=args.endianness, target_dir=target_dir)
    machine = find_machine(components)

    # 3. migrate the machine to the working dir
    firmware = migrate(components, machine)

    # 4. analyze this new firmware or lauch it
    status = run_static_analysis(firmware)
    # if machine is None:
        # status = run_static_analysis(firmware)
    # else:
        # status = run_dynamic_analysis(firmware)

    # 5. take snapshots to save results
    return snapshot(firmware)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument('-d', '--debug', action='store_true', help='show verbose logs')

    # analysis
    group = parser.add_argument_group('analysis')
    group.add_argument('-a', '--architecture', choices=['arm32', 'arm64', 'mips'], required=True)
    group.add_argument('-b', '--brand', choices=['openwrt'], required=False)
    group.add_argument('-e', '--endianness', choices=['b', 'l'], required=True)
    group.add_argument('-f', '--firmware', metavar='path/to/firmware', required=True)
    group.add_argument('-u', '--uuid', type=str, required=True)

    # diagnosis
    group = parser.add_argument_group('diagnosis')
    group.add_argument('-t', '--trace', metavar='path/to/uuid-arch-endian.trace')
    group.add_argument('-tf', '--trace_format', choices=['qemudebug'], default='qemudebug')
    group.add_argument('-m', '--max', type=int, help='max times of iteration', default=20)

    args = parser.parse_args()
    if args.debug:
        setup_logging(default_level=logging.DEBUG)
    else:
        setup_logging(default_level=logging.INFO)

    run(args)

