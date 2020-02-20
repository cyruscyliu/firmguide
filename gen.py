#!/usr/bin/python

import argparse
import logging.config

from logger import setup_logging
from slcore.environment import snapshot, migrate
from slcore.generation.dt_renderer import run_dt_renderer
from slcore.qemuc import QEMUController

logger = logging.getLogger()

def run(args):
    # 1. compile device tree source
    # Usually, you can compile the dts file directly with dtc
    #     dtc -I dts -O dtc path/to/dts -o target/to/dtb
    # If you'd like to compile the dts files in the Linux kernel,
    # you have to preprocess these dts files with cpp on your host.
    #     cpp -nostdinc -I include -I arch  -undef -x assembler-with-cpp path/to/dts target/to/dts.i
    # Then compile it.
    #     dtc -I dts -O dtc path/to/dts.i target/to/dtb

    # 2. let's begin
    firmware = migrate(args.uuid)
    firmware.set_dtb(args.dtb)
    firmware.set_arch(args.arch)
    firmware.set_endian(args.endian)
    firmware.set_machine_name(args.uuid)
    # low level qemu controller
    qemuc = QEMUController()
    firmware.qemuc = qemuc

    # 3. generate the machine.c etc.
    status = run_dt_renderer(firmware)

    # 4. take snapshots to save results
    status = snapshot(firmware)
    return status


if __name__ == '__main__':
    parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter)
    # general
    parser.add_argument('-d', '--debug', action='store_true', help='show verbose logs')

    # analysis
    group = parser.add_argument_group('generation')
    group.add_argument('-a', '--arch', choices=['arm', 'arm64', 'mips'], required=True)
    group.add_argument('-e', '--endian', choices=['b', 'l'], required=True)
    group.add_argument('-u', '--uuid', metavar='board', required=True)
    group.add_argument('-dtb', '--dtb', metavar='path/to/dtb', required=True)

    args = parser.parse_args()
    if args.debug:
        setup_logging(default_level=logging.DEBUG, uuid=args.uuid)
    else:
        setup_logging(default_level=logging.INFO, uuid=args.uuid)

    run(args)

