#!/usr/bin/python3.7
import os
import argparse
import logging.config

from logger import setup_logging, logger_info
from slcore.compositor import unpack
from slcore.machines import find_machine
from slcore.environment import migrate, snapshot
from slcore.environment import setup_target_dir
from slcore.scheduler import run_binary_analysis, run_diagnosis
from slcore.qemuc import QEMUController


def run(args):
    # 1. find a prepared machine
    target_dir = setup_target_dir(args.uuid)
    components = unpack(args.firmware, target_dir=target_dir)
    if not components.supported:
        return
    machine = find_machine(components, args.arch)
    if machine is None:
        return

    # 2. setup analysis environment
    firmware = migrate(args.uuid, path_to_profile=machine, components=components)
    firmware.set_arch(args.arch)
    firmware.set_endian(args.endian)

    # 3. lauch it if supported
    firmware.max_iteration = 1
    firmware.trace_format = args.trace_format
    firmware.path_to_trace = 'log/{}-{}-{}.trace'.format(
        firmware.get_uuid(), firmware.get_arch(), firmware.get_endian()
    )
    firmware.qemuc = QEMUController()
    status = run_diagnosis(firmware, check_only=True)

    # 4 run your own analysis
    # at here, the firmware has been launched,
    # then you can run your own dynamic analysis
    # import it from slcore.schedular and call it here
    # please have a look at run_binary_analysis/run_diagnosis

    # 5. take snapshots to save results
    return snapshot(firmware)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument('-d', '--debug', action='store_true', help='show verbose logs')

    # analysis
    group = parser.add_argument_group('analysis')
    group.add_argument('-a', '--arch', choices=['arm', 'arm64', 'mips'], required=True)
    group.add_argument('-b', '--brand', choices=['openwrt'], required=False)
    group.add_argument('-e', '--endian', choices=['b', 'l'], required=True)
    group.add_argument('-f', '--firmware', metavar='path/to/firmware', required=True)
    group.add_argument('-u', '--uuid', type=str, required=True)
    group.add_argument('-l', '--url', required=False )

    # diagnosis
    group = parser.add_argument_group('diagnosis')
    group.add_argument('-t', '--trace', metavar='path/to/uuid-arch-endian.trace')
    group.add_argument('-tf', '--trace_format', choices=['qemudebug'], default='qemudebug')
    group.add_argument('-m', '--max', type=int, help='max times of iteration', default=1)

    args = parser.parse_args()
    if args.debug:
        setup_logging(default_level=logging.DEBUG, uuid=args.uuid)
    else:
        setup_logging(default_level=logging.INFO, uuid=args.uuid)

    run(args)

