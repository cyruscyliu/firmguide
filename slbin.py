#!/usr/bin/python

import argparse
import logging.config

from slcore.environment import setup_target_dir
from slcore.compositor import unpack, migrate
from slcore.schedular import run_single_analysis
from slcore.naive_parsers.machine_id import find_machine_id
from slcore.naive_parsers.kernel_version import find_kernel_version
from slcore.database.machines import find_machine_by_id, find_machine_by_compatible
from slcore.logger import setup_logging, logger_info

def run(args):
    # mkdir working_dir/uuid
    setup_target_dir(args.uuid)

    # find prepared machine (abs/p/t/profile)
    components = unpack(args.firmware, arch=args.architecture, endian=args.endianness)
    if components.has_device_tree():
        compatible = components.get_compatible()
        machine = find_machine_by_compatible(compatble)
    else:
        machine_id = find_machine_id(components.get_kernel())
        machine = find_machine_by_id(machine_id)

    if machine is None:
        kernel_version = find_kernel_version(components.get_all())
        logger_info(args.uuid, 'slbin', args.firmware, 'no prepared machines avaiable', 0)
        return

    # run and diagnosis
    firmware = migrate(uuid, machine)
    run_single_analysis(firmware)


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
