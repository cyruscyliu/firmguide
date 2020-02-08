from slcore.parser import get_candidates, get_all_strings

import os

def parse_cmdfile(path):
    """
    Linux kernel will write compilation commands w.s.t to relavent objects
    to .xxx.o.cmd in the same directories.

    the format is xxx.o := command for the first line
    """
    with open(path) as f:
        cmdline = f.readline().strip().split(':=')[1]
    return cmdline


def split_cmdline(valid_cmdline):
    kv_pairs = {}

    for cmd in valid_cmdline.strip().split(' '):
        k, _, v = cmd.partition('=')
        if len(_):
            kv_pairs[k] = v
        else:
            kv_pairs[k] = True

    return kv_pairs


def find_cmdline_in_string(string, split=False):
    cmdline = None
    kv_pairs = None

    if string.find('root=/') != -1:
        # root=/dev/mtdblock1 rootfstype=squashfs,jffs2 noinitrd console=ttyS0,115200
        cmdline = string.strip()
        valid_cmdline = cmdline
        kv_pairs = split_cmdline(valid_cmdline)
    elif string.find('CMDLINE') != -1:
        # CMDLINE:board=AP135-020 console=ttyS0,115200 mtdparts=spi0.0:256k(u-boot)ro,
        # 64k(u-boot-env)ro,14528k(rootfs),1472k(kernel),64k(art)ro,16000k@0x50000(firmware)
        cmdline = string.strip()
        valid_cmdline = cmdline[8:]
        kv_pairs = split_cmdline(valid_cmdline)

    if split:
        return kv_pairs
    else:
        return cmdline


def find_cmdline_in_strings(strings, split=False):
    cmdline_or_kv_pairs = None

    for string in strings:
        cmdline_or_kv_pairs = find_cmdline_in_string(string, split=split)
        if cmdline_or_kv_pairs is not None:
            break

    return cmdline_or_kv_pairs


def find_cmdline(path_to_kernel, split=False):
    candidates = get_candidates(path_to_kernel)
    strings = get_all_strings(candidates)
    return find_cmdline_in_strings(strings, split=split)

# print(find_cmdline_in_string('root=/dev/mtdblock1 rootfstype=squashfs,jffs2 noinitrd console=ttyS0,115200'))
# print(find_cmdline_in_string('CMDLINE:board=AP135-020 console=ttyS0,115200 mtdparts=spi0.0:256k(u-boot)ro,64k(u-boot-env)ro,14528k(rootfs),1472k(kernel),64k(art)ro,16000k@0x50000(firmware)'))
# print(find_cmdline_in_string('root=/dev/mtdblock1 rootfstype=squashfs,jffs2 noinitrd console=ttyS0,115200', split=True))
# print(find_cmdline_in_string('CMDLINE:board=AP135-020 console=ttyS0,115200 mtdparts=spi0.0:256k(u-boot)ro,64k(u-boot-env)ro,14528k(rootfs),1472k(kernel),64k(art)ro,16000k@0x50000(firmware)', split=True))

