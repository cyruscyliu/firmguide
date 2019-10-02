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

    if brand == 'openwrt':
        logger.info('get source code by openwrt table of hardware')
        if firmware.openwrt is None:
            if firmware.most_possible_target is None or firmware.most_possible_subtarget is None:
                raise ValueError('incomplete information for finding source code')
        with open(os.path.join(os.getcwd(), 'database', 'openwrt.yaml')) as f:
            openwrt_release_info = yaml.safe_load(f)
        try:
            url = openwrt_release_info[firmware.openwrt_revision]['url']
        except KeyError:
            logger.info('no available url for this version {}'.format(firmware.openwrt_revision))
            return
        possible_package = os.path.join(
            url,
            firmware.most_possible_target,  # target
            firmware.most_possible_subtarget,  # subtarget
        )
        logger.info(
            '\033[32mdownload page found for OpenWrt project {}\033[0m'.format(possible_package))
