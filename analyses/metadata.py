"""
Get metadata from firmware blob.

Add your own function by register_get_metadata(your_func).
"""

import os
import re
import fdt
import time
import logging

import yaml
from prettytable import PrettyTable

from analyses.lib.common import search_most_possible_subtarget, search_most_possible_target, \
    search_most_possible_toh_record, search_most_possible_kernel_version, fit_parser, description_parser, \
    get_strings
from analyses.lib.display import print_table
from analyses.lib.openwrt_toh import find_openwrt_toh
from manager import finished, finish

logger = logging.getLogger()
TASK_DESCRIPTION = 'we are firstly getting critical metadata as much as possible'

__get_metadata = []


def by_file(firmware):
    LOG_SUFFIX = '[FILE]'
    image_type = firmware.get_format()
    image_path = firmware.get_path_to_image()
    if image_type == 'legacy uImage':
        """ 
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
        info = os.popen('file -b {}'.format(image_path))
        metadata = info.readline().strip()
        items = metadata.split(', ')
        kernel_version = re.search(r'Linux-(\d+\.\d+\.\d+)', items[1])
        if kernel_version is not None:
            kernel_version = kernel_version.groups()[0]
        else:
            kernel_version = re.search(r'.*\((\d+\.\d+\.\d+)\)', items[1])
        if not isinstance(kernel_version, str) and kernel_version is not None:
            kernel_version = kernel_version.groups()[0]
        _os = items[2].split('/')[0]
        arch = items[2].split('/')[1]
        kernel_created_time = items[5]  # time.strptime(items[5], "%a %b %d %H:%M:%S %Y")
        kernel_load_address = re.search(r'.*(0x[0-9a-fA-F]+).*', items[6]).groups()[0]
        kernel_entry_point = items[7]

        firmware.set_kernel_version(kernel_version)
        logger.info('\033[32mget the kernel version: {}\033[0m {}'.format(kernel_version, LOG_SUFFIX))
        firmware.set_kernel_created_time(kernel_created_time)
        logger.info('\033[32mget the kernel created time: {}\033[0m {}'.format(kernel_created_time, LOG_SUFFIX))
        firmware.set_kernel_load_address(kernel_load_address)
        firmware.set_kernel_entry_point(kernel_entry_point)


def by_dumpimage(firmware):
    image_type = firmware.get_format()
    image_path = firmware.get_path_to_image()
    LOG_SUFFIX = '[DUMPIMAGE]'
    if image_type == 'fit uImage':
        """
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
        info = os.popen('dumpimage -l {}'.format(image_path))
        fit = fit_parser(info.readlines())
        config = fit['configurations']['default configuration']
        if 'description' in fit['properties']:
            description = fit['properties']['description']
            description_parser(firmware, description)
        firmware.set_kernel_created_time(fit['properties']['timestamp'])
        if 'kernel' in fit['configurations'][config]:
            kernel_node = fit['images'][fit['configurations'][config]['kernel']]['properties']
            description = kernel_node['description']
            description_parser(firmware, description)
            # if 'os' in kernel_node:
            #     firmware.set('os', value=kernel_node['os'], confidence=1)
            # if 'arch' in kernel_node:
            #     firmware.set('arch', value=kernel_node['arch'], confidence=1)
            if 'load address' in kernel_node:
                loading_address = re.search(r'.*(0x[0-9a-fA-F]+).*', kernel_node['load address']).groups()[0]
                firmware.set_kernel_load_address(loading_address)
            if 'entry point' in kernel_node:
                firmware.set_kernel_entry_point(kernel_node['entry point'])


def by_kernel_version(firmware):
    kernel_version = firmware.get_kernel_version()
    if kernel_version is None:
        return
    LOG_SUFFIX = '[KERNEL VERSION]'
    with open(os.path.join(os.getcwd(), 'database', 'openwrt.yaml')) as f:
        openwrt_release_info = yaml.safe_load(f)
    openwrt_revision = None
    for revision, info in openwrt_release_info.items():
        if info['kernel'] == kernel_version:
            openwrt_revision = str(revision)
            logger.info('\033[32mOpenWrt {} {} found\033[0m {}'.format(
                revision, openwrt_release_info[revision]['code name'], LOG_SUFFIX))
    firmware.set_revision(openwrt_revision)
    if openwrt_revision is None:
        logger.info(
            'no available OpenWrt revision found for {}, '
            'please seek expertise for help'.format(kernel_version))


def by_device_tree(firmware):
    dtb = firmware.get_path_to_dtb()
    if dtb is None:
        return
    with open(dtb, 'rb') as f:
        dtb = f.read()
    dts = fdt.parse_dtb(dtb)
    firmware.set_dts(dts)
    compatibles = dts.get_property('compatible', '/').data
    models = dts.get_property('model', '/').data
    strings = []
    for compatible in compatibles:
        strings += compatible.split(',')
    for model in models:
        strings += model.split(' ')
    search_most_possible_toh_record(firmware, strings)


def by_strings(firmware):
    """
    If no dtb available, we can infer target platform and machine by strings.

    :param firmware: the firmware.
    :return: None
    """
    LOG_SUFFIX = '[STRINGS]'
    strings = get_strings(firmware)
    if strings is None:
        return None
    if firmware.get_revision() is None:
        search_most_possible_kernel_version(firmware, strings)
        by_kernel_version(firmware)
    search_most_possible_target(firmware, strings)
    search_most_possible_subtarget(firmware, strings)


def by_url(firmware):
    """
    Example:
        http://archive.openwrt.org/chaos_calmer/15.05/ar71xx/generic/openwrt-15.05-ar71xx-generic-bxu2000n-2-a1-kernel.bin
                                                  ^     ^       ^
                                              revision      subtarget
                                                      target
        http://archive.openwrt.org/backfire/10.03/orion/openwrt-wrt350nv2-squashfs-recovery.bin
                                              ^     ^
                                            revision
                                                  target
    """
    LOG_SUFFIX = '[URL]'
    if firmware.get_brand() == 'openwrt':
        homepage = os.path.dirname(firmware.get_url())
        firmware.set_homepage(homepage)
        logger.info('\033[32mdownload page found {}\033[0m {}'.format(homepage, LOG_SUFFIX))
        items = homepage.split('/')
        revision = items[4]
        target = items[5]
        subtarget = None
        if len(items) == 7:
            subtarget = items[6]
        firmware.set_target(target)
        logger.info('\033[32mget the most possible target {}\033[0m {}'.format(target, LOG_SUFFIX))
        firmware.set_subtarget(subtarget)
        logger.info('\033[32mget the most possible subtarget {}\033[0m {}'.format(subtarget, LOG_SUFFIX))
        firmware.set_revision(revision)
        logger.info('\033[32mget the revision {}\033[0m {}'.format(revision, LOG_SUFFIX))
        toh, header = find_openwrt_toh(revision, target, subtarget)
        if toh:
            firmware.set_toh(toh, header=header)
            logger.info('\033[32mget the toh {}\033[0m {}'.format(toh, LOG_SUFFIX))
            print_table(header, toh)


def by_description(firmware):
    pass


def register_get_metadata(func):
    __get_metadata.append(func)


register_get_metadata(by_file)
register_get_metadata(by_dumpimage)
register_get_metadata(by_kernel_version)
register_get_metadata(by_device_tree)
register_get_metadata(by_strings)
register_get_metadata(by_description)
register_get_metadata(by_url)


def get_metadata(firmware):
    logger.info(TASK_DESCRIPTION)
    for func in __get_metadata:
        if finished(firmware, 'get_metadata', func.__name__):
            continue
        func(firmware)
        finish(firmware, 'get_metadata', func.__name__)
