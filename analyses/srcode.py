"""
Handle all about source code.
"""
import os
import yaml
import logging

logger = logging.getLogger()

__process_source_code = []


def register_process_source_code(func):
    __process_source_code.append(func)


def process_source_code(firmware):
    for func in __process_source_code:
        func(firmware)


def get_source_code(firmware):
    brand = firmware.get('brand')
    if brand == 'openwrt':
        logger.info('get source code by openwrt table of hardware')
        if firmware.get('toh') is None:
            if firmware.get('target') is None or \
                    firmware.get('subtarget') is None:
                raise ValueError('incomplete information for finding source code')
        with open(os.path.join(os.getcwd(), 'database', 'openwrt.yaml')) as f:
            openwrt_release_info = yaml.safe_load(f)
        try:
            url = openwrt_release_info[firmware.get('revision')]['url']
        except KeyError:
            logger.info('no available url for this version {}'.format(firmware.get('revision')))
            return
        possible_package = os.path.join(
            url,
            firmware.get('target'),  # target
            firmware.get('subtarget'),  # subtarget
        )
        logger.info(
            '\033[32mdownload page found for OpenWrt project {}\033[0m'.format(possible_package))
