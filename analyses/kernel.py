import os
import re

from analyses.common.analysis import Analysis
from analyses.common.fit import fit_parser


def find_kernel_version(strings_to_kernel_version):
    kernel_version = re.search(r'Linux-(\d+\.\d+\.\d+)', strings_to_kernel_version)
    if kernel_version is not None:
        kernel_version = kernel_version.groups()[0]
    else:
        kernel_version = re.search(r'.*\((\d+\.\d+\.\d+)\)', strings_to_kernel_version)
    if not isinstance(kernel_version, str) and kernel_version is not None:
        kernel_version = kernel_version.groups()[0]
    return kernel_version


class Kernel(Analysis):
    def run(self, firmware):
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
            #
            kernel_version = find_kernel_version(items[1])
            _os = items[2].split('/')[0]
            arch = items[2].split('/')[1]
            #
            kernel_created_time = items[5]  # time.strptime(items[5], "%a %b %d %H:%M:%S %Y")
            #
            kernel_load_address = re.search(r'.*(0x[0-9a-fA-F]+).*', items[6]).groups()[0]
            #
            kernel_entry_point = items[7]
        elif image_type == 'fit uImage':
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
                kernel_version = find_kernel_version(description)
            kernel_created_time = fit['properties']['timestamp']
            if 'kernel' in fit['configurations'][config]:
                kernel_node = fit['images'][fit['configurations'][config]['kernel']]['properties']
                description = kernel_node['description']
                kernel_version = find_kernel_version(description)
                # if 'os' in kernel_node:
                #     firmware.set('os', value=kernel_node['os'], confidence=1)
                # if 'arch' in kernel_node:
                #     firmware.set('arch', value=kernel_node['arch'], confidence=1)
                if 'load address' in kernel_node:
                    kernel_load_address = re.search(r'.*(0x[0-9a-fA-F]+).*', kernel_node['load address']).groups()[0]
                if 'entry point' in kernel_node:
                    kernel_entry_point = kernel_node['entry point']
        else:
            return False
        firmware.set_kernel_version(kernel_version)
        self.info('\033[32mget the kernel version: {}\033[0m'.format(kernel_version))
        firmware.set_kernel_created_time(kernel_created_time)
        firmware.set_kernel_load_address(kernel_load_address)
        firmware.set_kernel_entry_point(kernel_entry_point)
        return True

    def __init__(self):
        super().__init__()
        # basic
        self.description = 'extract kernel related information from mthe given firmware'
        self.name = 'kernel'
        # logging
        self.log_suffix = '[KERNEL]'
        # exception
        self.context['hint'] = 'you must add strings parsers'
        # requirement
        self.required = ['extraction']
