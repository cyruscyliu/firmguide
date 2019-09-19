"""
Handle all about source code.
"""
import os
import yaml
import logging

from analysis.common import vote

logger = logging.getLogger()

__process_source_code = []


def register_process_source_code(func):
    __process_source_code.append(func)


def process_source_code(firmware):
    for func in __process_source_code:
        func(firmware)


def get_source_code(firmware):
    # vote for the brand
    if firmware.brand is None:
        brand = vote(firmware.metadata['brand'], 'brand')
    else:
        brand = firmware.brand

    if brand == 'OpenWrt':
        logger.info('get source by kernel version')
        with open(os.path.join(os.getcwd(), 'database', 'openwrt.yaml')) as f:
            openwrt_release_info = yaml.safe_load(f)
        # vote for the kernel version, all should be of Linux-x.x.x format.
        kernel_version = vote(firmware.metadata['kernel_version'], 'kernel version')
        simple_kernel_version = kernel_version.split('-')[1]
        openwrt_revision = None
        for revision, info in openwrt_release_info.items():
            if info['kernel'] == simple_kernel_version:
                openwrt_revision = revision
                logger.info('\033[32mOpenWrt {} {} found\033[0m'.format(
                    revision, openwrt_release_info[revision]['code name']))
        if openwrt_revision is None:
            raise ValueError(
                'no available OpenWrt revision found for {}, '
                'please seek expertise for help'.format(kernel_version))

