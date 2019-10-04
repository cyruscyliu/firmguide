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

from analysis.common import search_most_possible_subtarget, search_most_possible_target, \
    search_most_possible_toh_record, search_most_possible_kernel_version, fit_parser, description_parser, get_candidates
from manager import finished, finish

logger = logging.getLogger()

__get_metadata = []


def by_file(firmware):
    image_type = firmware.get('image_type')
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
        logger.info('get metadata by file')
        info = os.popen('file -b {}'.format(firmware.image_path))
        metadata = info.readline().strip()
        items = metadata.split(', ')
        kernel_version = re.search(r'Linux-(\d+\.\d+\.\d+)', items[1]).groups()[0]
        _os = items[2].split('/')[0]
        arch = items[2].split('/')[1]
        kernel_created_time = time.strptime(items[5], "%a %b %d %H:%M:%S %Y")
        kernel_load_address = items[6]
        kernel_entry_point = items[7]

        firmware.set('kernel_version', value=kernel_version, confidence=1)
        firmware.set('os', value=_os, confidence=1)
        firmware.set('arch', value=arch, confidence=1)
        firmware.set('kernel_created_time', value=kernel_created_time, confidence=1)
        loading_address = re.search(r'.*(0x[0-9a-fA-F]+).*', kernel_load_address).groups()[0]
        firmware.set('kernel_load_address', value=loading_address, confidence=1)
        firmware.set('kernel_entry_point', value=kernel_entry_point, confidence=1)


def by_dumpimage(firmware):
    image_type = firmware.get('image_type')
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
        logger.info('get metadata by file')
        info = os.popen('dumpimage -l {}'.format(firmware.image_path))
        fit = fit_parser(info.readlines())
        config = fit['configurations']['default configuration']
        if 'description' in fit['properties']:
            description = fit['properties']['description']
            description_parser(firmware, description)
        firmware.metadata['created_time'].append({'value': fit['properties']['timestamp'], 'confidence': 1})
        if 'kernel' in fit['configurations'][config]:
            kernel_node = fit['images'][fit['configurations'][config]['kernel']]['properties']
            description = kernel_node['description']
            description_parser(firmware, description)
            if 'os' in kernel_node:
                firmware.set('os', value=kernel_node['os'], confidence=1)
            if 'arch' in kernel_node:
                firmware.set('arch', value=kernel_node['arch'], confidence=1)
            if 'load address' in kernel_node:
                loading_address = re.search(r'.*(0x[0-9a-fA-F]+).*', kernel_node['load address']).groups()[0]
                firmware.set('kernel_load_address', value=loading_address, confidence=1)
            if 'entry point' in kernel_node:
                firmware.set('kernel_entry_point', value=kernel_node['entry point'], confidence=1)


def by_kernel_version(firmware):
    kernel_version = firmware.get('kernel_version')
    if kernel_version is None:
        return
    logger.info('get metadata by kernel version')
    with open(os.path.join(os.getcwd(), 'database', 'openwrt.yaml')) as f:
        openwrt_release_info = yaml.safe_load(f)
    openwrt_revision = None
    for revision, info in openwrt_release_info.items():
        if info['kernel'] == kernel_version:
            openwrt_revision = str(revision)
            logger.info('\033[32mOpenWrt {} {} found\033[0m'.format(
                revision, openwrt_release_info[revision]['code name']))
    firmware.set('revision', value=openwrt_revision, confidence=1)
    if openwrt_revision is None:
        logger.info(
            'no available OpenWrt revision found for {}, '
            'please seek expertise for help'.format(kernel_version))


def by_device_tree(firmware):
    dtb = firmware.get('dtb')
    if dtb is None:
        return
    logger.info('search possible target(s) by device tree')
    # thanks to https://github.com/molejar/pyFDT, a flattened device tree parser in Python
    with open(dtb, 'rb') as f:
        dtb = f.read()
    dtc = fdt.parse_dtb(dtb)
    firmware.set('dtc', value=dtc)
    compatibles = dtc.get_property('compatible', '/').data
    # firmware.metadata['compatible'].append({'value': compatibles, 'confidence': 1})
    # logger.info('\033[32mget the platform {}, confidence: {}\033[0m'.format(compatibles, 1))
    models = dtc.get_property('model', '/').data
    # firmware.metadata['model'].append({'value': compatible, 'confidence': 1})
    # logger.info('\033[32mget the model {}, confidence: {}\033[0m'.format(model, 1))
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
    if firmware.get('toh') is not None:
        return
    logger.info('get metadata by strings')
    strings = get_strings(firmware)
    if strings is None:
        return None
    if firmware.get('revision') is None:
        search_most_possible_kernel_version(firmware, strings)
        by_kernel_version(firmware)
    search_most_possible_target(firmware, strings)
    search_most_possible_subtarget(firmware, strings)


def get_strings(firmware):
    """
    We get strings from uncompressed binary.

    :param firmware:
    :return: [strings] or None
    """
    strings = []
    # get candidate files which contain useful strings
    candidates = get_candidates(firmware)
    if candidates is None:
        return None
    for candidate in candidates:
        info = os.popen('strings {} -n 2 | grep -E "^[a-zA-Z]+[a-zA-Z0-9_-]{{1,20}}"'.format(candidate))
        strings += info.readlines()
    return strings


def register_get_metadata(func):
    __get_metadata.append(func)


register_get_metadata(by_file)
register_get_metadata(by_dumpimage)
register_get_metadata(by_kernel_version)
register_get_metadata(by_device_tree)
register_get_metadata(by_strings)


def get_metadata(firmware):
    for func in __get_metadata:
        if finished(firmware, 'get_metadata', func.__name__):
            continue
        func(firmware)
        finish(firmware, 'get_metadata', func.__name__)
