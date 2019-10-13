"""
Handle flash.
"""

import logging

from database.dbf import get_database
from manager import finished, finish

logger = logging.getLogger()
TASK_DESCRIPTION = 'let us infer the flash'

__get_flash_info = []


def by_toh(firmware):
    LOG_SUFFIX = '[ToH]'
    [flash] = firmware.get_toh('flashmb')
    if flash is not None and flash != '' and flash != '?':
        # microSD, NAND, CF card, microSDXC, SDHC, eMMC
        if flash.find('NAND') != -1:
            firmware.set_flash_type('nand')
        else:
            firmware.set_flash_type('nor')


def by_source_code(firmware):
    pass


def by_strings(firmware):
    pass


def register_get_flash_info(func):
    __get_flash_info.append(func)


register_get_flash_info(by_toh)
register_get_flash_info(by_source_code)
register_get_flash_info(by_strings)


def get_flash_info(firmware):
    logger.info(TASK_DESCRIPTION)
    flash_model = firmware.get_flash_model()
    if flash_model is not None:
        logger.info('\033[32mflash model {} found\033[0m [DEVICE TREE]'.format(flash_model))
        return
    for func in __get_flash_info:
        if finished(firmware, 'get_flash_info', func.__name__):
            continue
        func(firmware)
        finish(firmware, 'get_flash_info', func.__name__)
