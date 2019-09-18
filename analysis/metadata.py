"""
Get metadata from firmware blob.

Add your own function by register_get_metadata(your_func).
"""

import os
import re
import time
import logging

logger = logging.getLogger()

__get_metadata = []


def by_file(firmware):
    if firmware.image_type == 'legacy uImage':
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
        kernel_version = items[1]
        _os = items[2].split('/')[0]
        arch = items[2].split('/')[1]
        kernel_created_time = time.strptime(items[5], "%a %b %d %H:%M:%S %Y")
        kernel_load_address = items[6]
        kernel_entry_point = items[7]
        firmware.metadata['kernel_version'].append({'value': kernel_version, 'confidence': 1})
        logger.info('\033[32mget the kernel version: {}, confidence: {}\033[0m'.format(kernel_version, 1))
        firmware.metadata['os'].append({'value': _os, 'confidence': 1})
        logger.info('\033[32mget the operating system: {}, confidence: {}\033[0m'.format(_os, 1))
        firmware.metadata['arch'].append({'value': arch, 'confidence': 1})
        logger.info('\033[32mget the architecture: {}, confidence: {}\033[0m'.format(arch, 1))
        firmware.metadata['kernel_created_time'].append({'value': kernel_created_time, 'confidence': 1})
        firmware.metadata['kernel_load_address'].append({'value': kernel_load_address, 'confidence': 1})
        firmware.metadata['kernel_entry_point'].append({'value': kernel_entry_point, 'confidence': 1})


def fit_parser(dumpimage_lines):
    fit = {
        'properties': {
            'timestamp': None
        }, 'images': {
        }, 'configurations': {
            'default configuration': None,
        }
    }
    level = 0
    image_node = ''
    conf_node = ''
    config = False
    for line in dumpimage_lines:
        if not len(line):
            continue
        if line.startswith('  '):
            level = 2
        elif line.startswith(' '):
            level = 1
        else:
            pass
        items = line.strip().split(': ')
        if level == 0 and line.startswith('FIT description'):
            fit['properties']['description'] = items[1].strip()
        elif level == 0 and line.startswith('Created'):
            fit['properties']['timestamp'] = time.strptime(items[1].strip(), "%a %b %d %H:%M:%S %Y")
        elif level == 1 and line.startswith(' Image'):
            assert len(items) == 1
            image_node = line.strip().split('(')[1].split(')')[0]
            if image_node not in fit['images']:
                fit['images'][image_node] = {'properties': {}, 'hash': {}}
        elif level == 2 and line.startswith('  Description'):
            fit['images'][image_node]['properties']['description'] = items[1].strip()
        elif level == 2 and line.startswith('  Created'):
            fit['images'][image_node]['properties']['timestamp'] = \
                time.strptime(items[1].strip(), "%a %b %d %H:%M:%S %Y")
        elif level == 2 and line.startswith('  Type'):
            fit['images'][image_node]['properties']['type'] = items[1].strip()
        elif level == 2 and line.startswith('  Compression'):
            fit['images'][image_node]['properties']['compression'] = items[1].strip()
        elif level == 2 and line.startswith('  Architecture'):
            fit['images'][image_node]['properties']['arch'] = items[1].strip()
        elif level == 2 and line.startswith('  OS'):
            fit['images'][image_node]['properties']['os'] = items[1].strip()
        elif level == 2 and line.startswith('  Load Address'):
            fit['images'][image_node]['properties']['load address'] = items[1].strip()
        elif level == 2 and line.startswith('  entry point'):
            fit['images'][image_node]['properties']['entry point'] = items[1].strip()
        elif level == 1 and line.startswith(' Default Configuration'):
            fit['configurations']['default configuration'] = items[1].strip('\'')
        elif level == 1 and line.startswith(' Configuration'):
            assert len(items) == 1
            conf_node = line.strip().split('(')[1].split(')')[0]
            if conf_node not in fit['configurations']:
                fit['configurations'][conf_node] = {}
            config = True
        elif level == 2 and config and line.startswith('  Kernel'):
            fit['configurations'][conf_node]['kernel'] = items[1].strip()
        elif level == 2 and config and line.startswith('  FDT'):
            fit['configurations'][conf_node]['fdt'] = items[1].strip()
        else:
            logging.debug('not support line {}'.format(dumpimage_lines))
    return fit


def description_parser(firmware, description):
    if description.find('OpenWrt') != -1:
        firmware.metadata['brand'].append({'value': 'OpenWrt', 'confidence': 1})
    kernel_version = re.search(r'Linux-\d+.\d+.\d+', description)
    if kernel_version:
        firmware.metadata['kernel_version'].append({'value': kernel_version.group(), 'confidence': 1})
        logger.info(
            '\033[32mget the kernel version: {}, confidence: {}\033[0m'.format(kernel_version.group(), 1))
    # search for board name and target platform


def by_dumpimage(firmware):
    if firmware.image_type == 'legacy uImage':
        # provide no more information than file command
        return
    if firmware.image_type == 'fit uImage':
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
                firmware.metadata['os'].append({'value': kernel_node['os'], 'confidence': 1})
                logger.info('\033[32mget the operating system: {}, confidence: {}\033[0m'.format(kernel_node['os'], 1))
            if 'arch' in kernel_node:
                firmware.metadata['arch'].append({'value': kernel_node['arch'], 'confidence': 1})
                logger.info('\033[32mget the architecture: {}, confidence: {}\033[0m'.format(kernel_node['arch'], 1))
            if 'load address' in kernel_node:
                firmware.metadata['kernel_load_address'].append({'value': kernel_node['load address'], 'confidence': 1})
            if 'entry point' in kernel_node:
                firmware.metadata['kernel_entry_point'].append({'value': kernel_node['entry point'], 'confidence': 1})


def by_strings(firmware):
    pass


def by_binwalk(firmware):
    pass


def register_get_metadata(func):
    __get_metadata.append(func)


register_get_metadata(by_file)
register_get_metadata(by_dumpimage)
register_get_metadata(by_strings)
register_get_metadata(by_binwalk)


def get_metadata(firmware):
    for func in __get_metadata:
        func(firmware)
