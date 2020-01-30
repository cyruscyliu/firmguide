#!/usr/bin/python

import argparse
import logging.config

from logger import setup_logging
from slcore.environment import setup_target_dir # srcode
from profile.firmwaref import get_firmware
from slcore.environment import snapshot, archive # firmware
from slcore.environment import run_statis_analysis # firmware

logger = logging.getLogger()

def run(args):
    # 1. setup a working dir
    target_dir = setup_target_dir('srcode')

    # 2. prepare a firmware
    firmware = get_firmware('simple')
    firmware.uuid = 'srcode'
    firmware.target_dir = target_dir
    firmware.set_profile(target_dir=target_dir, first=True)
    firmware.set_uuid('srcode')
    firmware.set_path_to_srcode = args.source_code
    firmware.set_path_to_gcc = args.gcc
    if args.arch:
        firmware.set_architecture(args.arch)
    if args.endian:
        firmware.set_endian(args.endian)
    if args.makeout:
        firmware.set_path_to_mkout(args.makeout)

    # 3. analyze the source code
    status = run_static_analysis(firmware, binary=False)

    # 4. take snapshots to save results
    status = snapshot(firmware)

    # 5. archive
    return archive(firmware)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter)
    # general
    parser.add_argument('-r', '--rerun', action='store_true', default=False,
                        help='ingore save and restore and rerun all analysis')
    parser.add_argument('-d', '--debug', action='store_true', help='show verbose logs')

    # analysis
    group = parser.add_argument_group('analysis')
    group.add_argument('-a', '--arch', type=str, choices=['arm32', 'arm64', 'mips'], required=False)
    group.add_argument('-e', '--endian', type=str, choices=['b', 'l'], required=False)
    group.add_argument('-b', '--brand', type=str, choices=['openwrt'], required=False)
    group.add_argument('-s', '--source_code', type=str, metavar='path/to/source_code', required=True)
    group.add_argument('-gcc', '--gcc', type=str, metavar='path/to/gcc', required=True)
    group.add_argument('-mkout', '--makeout', type=str, metavar='path/to/makeout', required=False)

    args = parser.parse_args()
    if args.debug:
        setup_logging(default_level=logging.DEBUG)
    else:
        setup_logging(default_level=logging.INFO)

    run(args)
