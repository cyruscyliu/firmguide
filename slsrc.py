#!/usr/bin/python

import os
import argparse
import logging.config

from logger import setup_logging
from slcore.environment import setup_target_dir # srcode
from profile.firmwaref import get_firmware
from slcore.environment import snapshot, archive # firmware
from slcore.scheduler import run_static_analysis # firmware
from slcore.srcodec import SRCodeController

logger = logging.getLogger()

def run(args):
    # 1. setup a working dir
    target_dir = setup_target_dir(args.uuid)

    # 2. prepare a firmware
    firmware = get_firmware('simple')
    firmware.uuid = args.uuid
    firmware.target_dir = target_dir
    firmware.set_profile(target_dir=target_dir, first=True)
    firmware.set_uuid(args.uuid)
    firmware.set_architecture(args.arch)

    path_to_source_code = args.source_code
    path_to_vmlinux = os.path.join(path_to_source_code, 'vmlinux')
    path_to_dot_config = os.path.join(path_to_source_code, '.config')
    firmware.set_path_to_source_code(path_to_source_code)
    firmware.set_path_to_vmlinux(path_to_vmlinux)
    firmware.set_path_to_dot_config(path_to_dot_config)
    firmware.set_path_to_gcc(args.gcc)
    firmware.srcodec = SRCodeController(path_to_source_code, args.arch, args.gcc)

    if args.endian:
        firmware.set_endian(args.endian)
    if args.makeout:
        firmware.set_path_to_makeout(args.makeout)
        firmware.srcodec.set_makeout(args.makeout)

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
    group.add_argument('-a', '--arch', type=str, choices=['arm', 'arm64', 'mips'], required=True)
    group.add_argument('-e', '--endian', type=str, choices=['b', 'l'], required=False)
    group.add_argument('-b', '--brand', type=str, choices=['openwrt'], required=False)
    group.add_argument('-s', '--source_code', type=str, metavar='path/to/source_code', required=True)
    group.add_argument('-gcc', '--gcc', type=str, metavar='path/to/prefix', required=True)
    group.add_argument('-u', '--uuid', type=str, required=True)
    group.add_argument('-mkout', '--makeout', type=str, metavar='path/to/makeout', required=False)

    args = parser.parse_args()
    if args.debug:
        setup_logging(default_level=logging.DEBUG)
    else:
        setup_logging(default_level=logging.INFO)

    run(args)

