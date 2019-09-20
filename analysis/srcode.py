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
        logger.info('get source code by openwrt table of hardware')
        if firmware.openwrt is None:
            raise ValueError('no record found in toh of openwrt')
        with open(os.path.join(os.getcwd(), 'database', 'openwrt.yaml')) as f:
            openwrt_release_info = yaml.safe_load(f)
        possible_package = os.path.join(
            openwrt_release_info[firmware.openwrt_revision]['url'],
            firmware.openwrt[5],  # supportedcurrentrel
            firmware.openwrt[6],  # target
            firmware.openwrt[7],  # subtarget
        )
        logger.info(
            '\033[32mdownload page found for OpenWrt project {}\033[0m'.format(possible_package))
