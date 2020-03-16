from slcore.parser import fit_parser

import os
import re


def find_kernel_version_in_string(string):
    """Find which Linux kernel version the image belongs to.

    Args:
        string(str): String from the image.

    Returns:
        str: The Linux kernel version the image may belongs to.
    """
    patterns = [r'Linux-(\d+\.\d+\.\d+)', r'.*\((\d+\.\d+\.\d+)\)', r'[lL]inux version ([1-5]+\.\d+\.\d+).*']

    kernel_version = None
    for pattern in patterns:
        kernel_version = re.search(pattern, string)
        if kernel_version is not None:
            kernel_version = kernel_version.groups()[0]
            break

    return kernel_version


def find_kernel_version_in_strings(strings):
    """Find which Linux kernel version the image belongs to.

    Args:
        strings(list): Strings from the image.

    Returns:
        str: The Linux kernel version the image may belongs to.
    """
    for string in strings:
        kernel_version = find_kernel_version_in_string(string)
        if kernel_version is not None:
            return kernel_version


def find_kernel_version_in_legacy_uimage(path_to_image):
    """Find which Linux kernel version the image belongs to.

    Args:
        path_to_kernel(str): Path to the image. We will get strings from it.

    Returns:
        str: The Linux kernel version the image may belongs to.

    Example:
        file uImage: delimiter=', '
            [0] u-boot legacy uImage,
            [1] Linux-3.3.8,
            [2] Linux/ARM,
            [3] OS Kernel Image (Not compressed),
            [4] 960520 bytes,
            [5] Sun Mar 24 03:00:11 2013,
            [6] Load Address: 0x00008000,
            [7] Entry Point: 0x00008000,
            [8] Header CRC: 0xCC8FC8A7,
            [9] Data CRC: 0x90F6B42F
    """
    info = os.popen('file -b {}'.format(path_to_image))
    metadata = info.readline().strip()
    items = metadata.split(', ')
    kernel_version = find_kernel_version_in_string(items[1])
    # _os = items[2].split('/')[0]
    # arch = items[2].split('/')[1]
    kernel_created_time = items[5]  # time.strptime(items[5], "%a %b %d %H:%M:%S %Y")
    kernel_load_address = re.search(r'.*(0x[0-9a-fA-F]+).*', items[6]).groups()[0]
    kernel_entry_point = items[7]
    return kernel_version


def find_kernel_version_in_fit_uiamge(path_to_image):
    """Find which Linux kernel version the image belongs to.

    Args:
        path_to_kernel(str): Path to the image. We will get strings from it.

    Returns:
        str: The Linux kernel version the image may belongs to.

    Example:
        FIT description: ARM OpenWrt FIT (Flattened Image Tree)
        Created:         Sat Sep 12 01:13:52 2015
        Image 0 (kernel@1)
        Description:  ARM OpenWrt Linux-3.18.20
        Created:      Sat Sep 12 01:13:52 2015
        Type:         Kernel Image
        Compression:  uncompressed
        Data Size:    2988352 Bytes = 2918.31 kB = 2.85 MB
        Architecture: ARM
        OS:           Linux
        Load Address: 0x60008000
        Entry Point:  0x60008000
        Hash algo:    crc32
        Hash value:   bb7fe659
        Hash algo:    sha1
        Hash value:   8b1986ad81f17b94f355b1724a482496877f877a
        Image 1 (fdt@1)
        Description:  ARM OpenWrt kd20 device tree blob
        Created:      Sat Sep 12 01:13:52 2015
        Type:         Flat Device Tree
        Compression:  uncompressed
        Data Size:    8091 Bytes = 7.90 kB = 0.01 MB
        Architecture: ARM
        Hash algo:    crc32
        Hash value:   c2f4f5a9
        Hash algo:    sha1
        Hash value:   13de26cd9ac3e38c4073f010be71eac4f1915640
        Default Configuration: 'config@1'
        Configuration 0 (config@1)
        Description:  OpenWrt
        Kernel:       kernel@1
        FDT:          fdt@1
    """
    info = os.popen('dumpimage -l {}'.format(path_to_image))
    fit = fit_parser(info.readlines())
    config = fit['configurations']['default configuration']
    if 'description' in fit['properties']:
        description = fit['properties']['description']
        kernel_version = find_kernel_version_in_string(description)
    kernel_created_time = fit['properties']['timestamp']
    if 'kernel' in fit['configurations'][config]:
        kernel_node = fit['images'][fit['configurations'][config]['kernel']]['properties']
        description = kernel_node['description']
        kernel_version = find_kernel_version_in_string(description)
        # if 'os' in kernel_node:
        #     firmware.set('os', value=kernel_node['os'], confidence=1)
        # if 'arch' in kernel_node:
        #     firmware.set('arch', value=kernel_node['arch'], confidence=1)
        if 'load address' in kernel_node:
            kernel_load_address = re.search(r'.*(0x[0-9a-fA-F]+).*', kernel_node['load address']).groups()[0]
        if 'entry point' in kernel_node:
            kernel_entry_point = kernel_node['entry point']
    return kernel_version

# print(find_kernel_version_in_string('[1] Linux-3.3.8,'))
# print(find_kernel_version_in_string('Description:  ARM OpenWrt Linux-3.18.20'))
# print(find_kernel_version_in_string('linux version 3.18.20'))
# print(find_kernel_version_in_string('Linux version 3.18.20'))
