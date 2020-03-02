#!/usr/bin/python

import os
import shutil
import argparse
import logging.config

from logger import setup_logging
from slcore.environment import setup_target_dir, migrate
from slcore.environment import snapshot, archive
from slcore.scheduler import run_static_analysis, run_diagnosis
from slcore.srcodec import SRCodeController
from slcore.qemuc import QEMUController
from slcore.compositor import unpack

logger = logging.getLogger()

def run(args):
    # 1. setup analysis environment
    target_dir = setup_target_dir(args.uuid)

    path_to_profile = os.path.join(target_dir, 'profile.yaml')
    if not os.path.exists(path_to_profile):
        args.rerun = True
        path_to_profile = None

    if args.rerun:
        # rewrite existing profile(including the first attemp)
        components = unpack(args.firmware, target_dir=target_dir)
        path_to_profile = None
    else:
        components = None

    firmware = migrate(args.uuid, path_to_profile=path_to_profile, components=components)
    firmware.set_arch(args.arch)
    firmware.set_endian(args.endian)
    firmware.set_machine_name(args.uuid)
    firmware.rerun = args.rerun

    if args.dtb:
        firmware.set_dtb(args.dtb)
    elif firmware.get_components().get_path_to_dtb():
        firmware.set_dtb(firmware.get_components().get_path_to_dtb())
    else:
        print('neither dtb was found in tested firmware nor -dtb was assigned')
        return

    # 2.1 low level source code controller
    srcodec = SRCodeController()
    path_to_source_code = args.source_code
    srcodec.set_path_to_source_code(path_to_source_code)
    srcodec.set_path_to_vmlinux(os.path.join(path_to_source_code, 'vmlinux'))
    srcodec.set_path_to_dot_config(os.path.join(path_to_source_code, '.config'))
    srcodec.set_path_to_cross_compile(args.gcc)
    srcodec.set_endian(args.endian)
    srcodec.set_arch(args.arch)
    if args.makeout:
        srcodec.set_path_to_makeout(args.makeout)
    firmware.srcodec = srcodec
    # 2.2 low level qemu controller
    qemuc = QEMUController()
    firmware.qemuc = qemuc

    # 3. analyze the source code
    status = run_static_analysis(firmware)

    # 4. take snapshots to save results
    status = snapshot(firmware)

    # 5. invoke diagnosis
    firmware.max_iteration = 1
    firmware.trace_format = 'qemudebug'
    firmware.path_to_trace = 'log/{}-{}-{}.trace'.format(
        firmware.get_uuid(), firmware.get_arch(), firmware.get_endian()
    )
    firmware.debug = args.debug
    status = run_diagnosis(firmware)

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
    group.add_argument('-dtb', '--dtb', metavar='path/to/dtb', required=False)
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

