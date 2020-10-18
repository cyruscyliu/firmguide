#!/usr/bin/python
import os
import sys
import tempfile
import argparse

sys.path.extend(['.', '..', '../..'])

from slcore.compositor import unpack
from slcore.dt_parsers.compatible import find_compatible
from slcore.database.machineid import find_machine_id
from slcore.database.board_dir import find_board_dir


def foreigner(args):
    firmware = args.firmware
    if not os.path.exists(firmware):
        print('[-] {} doesnot exist'.format(firmware))
        return False

    try:
        components = unpack(firmware, tempfile.gettempdir())
    except FileNotFoundError:
        print('[-] {} not found'.format(firmware))
        return False
    if not components.supported:
        print('[-] {} format not supported'.format(firmware))
        return False

    if components.has_device_tree():
        compatible = find_compatible(components.get_path_to_dtb())
        print('[+] compatible {}'.format(compatible))

    machine_id = find_machine_id(components.get_path_to_kernel())
    print('[+] machine id {}'.format(machine_id))

    board = find_board_dir(components.get_path_to_kernel(), args.arch)
    print('[+] board {}'.format(board))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('-f', '--firmware', required=True, help='foreign firmware')
    parser.add_argument('-a', '--arch', required=True, help='arch of firmware')
    args = parser.parse_args()

    foreigner(args)
