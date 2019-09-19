"""
Handle all about source code.
"""
import os
import yaml
import logging

from analysis.common import vote
from database.dbf import get_database

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
                openwrt_revision = str(revision)
                logger.info('\033[32mOpenWrt {} {} found\033[0m'.format(
                    revision, openwrt_release_info[revision]['code name']))
        if openwrt_revision is None:
            raise ValueError(
                'no available OpenWrt revision found for {}, '
                'please seek expertise for help'.format(kernel_version))
        if firmware.most_possible_target is None:
            return
        openwrt = get_database('openwrt')
        by_target = openwrt.select(
            'devicetype', 'brand', 'model', 'supportedsincerel',
            'supportedcurrentrel', 'target', 'subtarget',
            target=firmware.most_possible_target)
        supported_current_rels = by_target[openwrt.header.index('supportedcurrentrel')]
        targets = by_target[openwrt.header.index('target')]
        sub_targets = by_target[openwrt.header.index('subtarget')]
        possible_packages = {}
        for i, supported_current_rel in enumerate(supported_current_rels):
            if supported_current_rel == openwrt_revision:
                possible_packages[i] = {'value': os.path.join(
                    openwrt_release_info[openwrt_revision]['url'], openwrt_revision,
                    targets[i], sub_targets[i])}
        if len(possible_packages) > 0:
            for possible_package in possible_packages.values():
                logger.info('>> {}'.format(possible_package['value']))

