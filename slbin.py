#!/usr/bin/python3.7
import os
import argparse
import shutil
import logging.config

from logger import setup_logging, logger_info
from slcore.compositor import unpack
from slcore.machines import find_machine
from slcore.environment import migrate, snapshot
from slcore.environment import setup_target_dir
from slcore.scheduler import run_binary_analysis, run_diagnosis


def run(args):
    # 1. find a prepared machine
    target_dir = setup_target_dir(args.uuid)
    components = unpack(args.firmware, target_dir=target_dir)
    if not components.supported:
        return
    machine = find_machine(components, args.arch)

    # 3. migrate the machine to or create the working dir
    firmware = migrate(args.uuid, path_to_profile=machine)
    firmware.set_working_path(
        os.path.join(firmware.get_target_dir(), components.get_raw_name()))
    firmware.set_components(components)
    firmware.set_architecture(args.arch)
    firmware.set_endian(args.endian)
    firmware.trace_format = args.trace_format
    firmware.path_to_trace = 'log/{}-{}-{}.trace'.format(
        firmware.get_uuid(), firmware.get_architecture(), firmware.get_endian()
    )
    firmware.max_iteration = 1
    # copy the firmware to working path
    if not os.path.exists(firmware.working_path):
        shutil.copy(
            os.path.join(os.getcwd(), components.get_path_to_raw()),
            os.path.join(firmware.working_path)
    )

    # 4. lauch it if supported, otherwise analyze it simply
    status = True
    if machine is not None:
        status = run_diagnosis(firmware, check_only=True)

    if machine is None or not status:
        if args.brand:
            firmware.set_brand(args.brand)
        if args.url:
            firmware.set_url(args.url)
        status = run_binary_analysis(firmware)
        if not status:
            return snapshot(firmware)

    # 5 run your own analysis
    # at here, the firmware has been launched,
    # then you can run your own dynamic analysis
    # import it from slcore.schedular and call it here
    # please have a look at run_binary_analysis/run_diagnosis

    # 6. take snapshots to save results
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

