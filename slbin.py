#!/usr/bin/python3.7

import argparse
import logging.config

# components
from slcore.compositor import unpack
from slcore.database.machines import find_machine
from slcore.parser import parse

# uuid
from slcore.environment import setup_target_dir, migrate

# firmware
from slcore.scheduler import run_single_analysis

from slcore.logger import setup_logging, logger_info

def run(args):
    # mkdir working_dir/uuid
    setup_target_dir(args.uuid)

    # find prepared machine (abs/p/t/profile)
    components = unpack(args.firmware, arch=args.architecture, endian=args.endianness)
    machine = find_machine(components)

    if machine is not None:
        # run and diagnosis
        firmware = migrate(uuid, machine)
        run_single_analysis(firmware)
        return

    info = parse(components)
    logger_info(args.uuid, 'slbin', args.firmware, 'no prepared machines avaiable', 0)
    logger_info(args.uuid, 'slbin', args.firmware, info, 0)
    return



if __name__ == '__main__':
    parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter)
    # general
    parser.add_argument('-r', '--rerun', action='store_true', default=False,
                        help='ingore save and restore and rerun all analysis')
    parser.add_argument('-d', '--debug', action='store_true', help='show verbose logs')

    # analysis
    group = parser.add_argument_group('analysis')
    group.add_argument('-u', '--uuid', type=str, required=True)
    group.add_argument('-f', '--firmware', type=str, metavar='path/to/firmware', required=True)
    group.add_argument('-a', '--architecture', type=str, choices=['arm', 'mips'], required=True)
    group.add_argument('-e', '--endianness', type=str, choices=['b', 'l'], required=True)
    group.add_argument('-q', '--quick', action='store_true', default=False, help='skip analysis')

    args = parser.parse_args()
    if args.debug:
        setup_logging(default_level=logging.DEBUG)
    else:
        setup_logging(default_level=logging.INFO)

    if args.uuid is None:
        parser.print_help()
    else:
        run(args)
