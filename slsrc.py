#!/usr/bin/python

import os
import shutil
import argparse
import logging.config

from logger import setup_logging
from slcore.environment import setup_target_dir # srcode
from slcore.profile.firmwaref import get_firmware
from slcore.environment import snapshot, archive # firmware
from slcore.scheduler import run_static_analysis, run_dynamic_analysis # firmware
from slcore.srcodec import SRCodeController
from slcore.compositor import unpack

logger = logging.getLogger()

def run(args):
    # 1. setup a working dir
    target_dir = setup_target_dir(args.uuid)

    # 2. prepare a firmware
    firmware = get_firmware('simple')
    firmware.uuid = args.uuid
    firmware.target_dir = target_dir

    firmware.set_profile(target_dir=target_dir, first=args.rerun)
    if args.rerun:
        firmware.set_uuid(args.uuid)
        firmware.set_architecture(args.arch)
        firmware.set_machine_name(args.uuid)

        components = unpack(args.firmware, target_dir=target_dir)
        firmware.set_components(components)
        firmware.set_working_path(
                    os.path.join(firmware.get_target_dir(), components.get_raw_name())
        )
        # copy the firmware to working path
        if not os.path.exists(firmware.working_path):
            shutil.copy(
                os.path.join(os.getcwd(), components.get_path_to_raw()),
                os.path.join(firmware.working_path)
            )
    path_to_source_code = args.source_code
    path_to_vmlinux = os.path.join(path_to_source_code, 'vmlinux')
    path_to_dot_config = os.path.join(path_to_source_code, '.config')
    firmware.set_path_to_source_code(path_to_source_code)
    firmware.set_path_to_vmlinux(path_to_vmlinux)
    firmware.set_path_to_dot_config(path_to_dot_config)
    firmware.set_path_to_gcc(args.gcc)
    firmware.rerun = args.rerun

    firmware.srcodec = SRCodeController(path_to_source_code, args.arch, args.gcc)
    if args.endian:
        firmware.set_endian(args.endian)
    if args.makeout:
        firmware.set_path_to_makeout(args.makeout)
        firmware.srcodec.set_makeout(args.makeout)

    # 3. analyze the source code
    status = run_static_analysis(firmware)

    # 4. take snapshots to save results
    status = snapshot(firmware)

    # 5. invoke dynamic analysis
    firmware.trace_format = 'qemudebug'
    firmware.path_to_trace = 'log/{}-{}-{}.trace'.format(
        firmware.get_uuid(), firmware.get_architecture(), firmware.get_endian()
    )
    firmware.max_iteration = 1
    status = run_dynamic_analysis(firmware, check_only=True)

    # 6. take snapshots to save results
    status = snapshot(firmware)

    return archive(firmware)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter)
    # general
    parser.add_argument('-r', '--rerun', action='store_true', default=False,
                        help='ingore save and restore and rerun all analysis')
    parser.add_argument('-d', '--debug', action='store_true', help='show verbose logs')

    # analysis
    group = parser.add_argument_group('analysis')
    group.add_argument('-a', '--arch', choices=['arm', 'arm64', 'mips'], required=True)
    group.add_argument('-e', '--endian', choices=['b', 'l'], required=True)
    group.add_argument('-b', '--brand', choices=['openwrt'], required=False)
    group.add_argument('-f', '--firmware', required=True)
    group.add_argument('-s', '--source_code', metavar='path/to/source_code', required=True)
    group.add_argument('-gcc', '--gcc', metavar='path/to/prefix', required=True)
    group.add_argument('-u', '--uuid', type=str, required=True)
    group.add_argument('-mkout', '--makeout', metavar='path/to/makeout', required=True)

    args = parser.parse_args()
    if args.debug:
        setup_logging(default_level=logging.DEBUG, uuid=args.uuid)
    else:
        setup_logging(default_level=logging.INFO, uuid=args.uuid)

    run(args)

