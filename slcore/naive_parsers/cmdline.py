from slcore.parser import get_candidates, get_all_strings


def parse_cmdfile(path):
    """Linux kernel will write compilation command w.s.t to the object
    to .xxx.o.cmd in the same directory. The format is xxx.o := command
    in the first line.

    :param strings: Path to .xxx.o.cmd.
    :type  strings: str
    :returns      : The real command.
    :rtype        : str
    """
    with open(path) as f:
        cmdline = f.readline().strip().split(':=')[1]
    return cmdline


def __split_cmdline(valid_cmdline):
    kv_pairs = {}

    for cmd in valid_cmdline.strip().split(' '):
        k, _, v = cmd.partition('=')
        if len(_):
            kv_pairs[k] = v
        else:
            kv_pairs[k] = True

    return kv_pairs


def find_cmdline_in_string(string, split=False):
    """Find the default kernel command line in the image.

    :param string: The string from the image.
    :type  string: str
    :param split : Whether or not we split the command line by =
    :type  split : bool
    :returns     : Return the command line if split is False, otherwise, return the key pairs.
    :rtype       : str or dict
    """
    cmdline = None
    kv_pairs = None

    if string.find('root=/') != -1:
        # root=/dev/mtdblock1 rootfstype=squashfs,jffs2 noinitrd console=ttyS0,115200
        cmdline = string.strip()
        valid_cmdline = cmdline
        kv_pairs = __split_cmdline(valid_cmdline)
    elif string.find('CMDLINE') != -1:
        # CMDLINE:board=AP135-020 console=ttyS0,115200 mtdparts=spi0.0:256k(u-boot)ro,
        # 64k(u-boot-env)ro,14528k(rootfs),1472k(kernel),64k(art)ro,16000k@0x50000(firmware)
        cmdline = string.strip()
        valid_cmdline = cmdline[8:]
        kv_pairs = __split_cmdline(valid_cmdline)

    if split:
        return kv_pairs
    else:
        return cmdline


def find_cmdline_in_strings(strings, split=False):
    """Find the default kernel command line in the image.

    :param strings: The strings from the image.
    :type  strings: list
    :param split  : Whether or not we split the command line by =
    :type  split  : bool
    :returns      : Return the command line if split is False, otherwise, return the key pairs.
    :rtype        : str or dict
    """
    cmdline_or_kv_pairs = None

    for string in strings:
        cmdline_or_kv_pairs = find_cmdline_in_string(string, split=split)
        if cmdline_or_kv_pairs is not None:
            break

    return cmdline_or_kv_pairs


def find_cmdline(path_to_kernel, split=False):
    """Find the default kernel command line in the image.

    :param path_to_kernel: The path to the image.
    :type  path_to_kernel: list
    :param split         : Whether or not we split the command line by =
    :type  split         : bool
    :returns             : Return the command line if split is False, otherwise, return the key pairs.
    :rtype               : str or dict
    """
    candidates = get_candidates(path_to_kernel)
    strings = get_all_strings(candidates)
    return find_cmdline_in_strings(strings, split=split)

# print(find_cmdline_in_string('root=/dev/mtdblock1 rootfstype=squashfs,jffs2 noinitrd console=ttyS0,115200'))
# print(find_cmdline_in_string('CMDLINE:board=AP135-020 console=ttyS0,115200 mtdparts=spi0.0:256k(u-boot)ro,64k(u-boot-env)ro,14528k(rootfs),1472k(kernel),64k(art)ro,16000k@0x50000(firmware)'))
# print(find_cmdline_in_string('root=/dev/mtdblock1 rootfstype=squashfs,jffs2 noinitrd console=ttyS0,115200', split=True))
# print(find_cmdline_in_string('CMDLINE:board=AP135-020 console=ttyS0,115200 mtdparts=spi0.0:256k(u-boot)ro,64k(u-boot-env)ro,14528k(rootfs),1472k(kernel),64k(art)ro,16000k@0x50000(firmware)', split=True))
