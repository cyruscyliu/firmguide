"""
Handle RAM
"""
import logging

from database.dbf import get_database
from manager import finished, finish

logger = logging.getLogger()
TASK_DESCRIPTION = 'let us infer the suitable size of ram'

__get_ram_info = []


def by_toh(firmware):
    LOG_SUFFIX = '[ToH]'
    [ram] = firmware.get_toh('rammb')
    if ram is not None and ram != '':
        firmware.set_ram(0, ram, unit='MiB')
        logger.info('\033[32mget memory info, base: {}, size: {}MB\033[0m {}'.format(0, ram, LOG_SUFFIX))


def by_default(firmware):
    LOG_SUFFIX = 'DEFAULT'
    ram_base, ram_size = firmware.get_ram()
    if ram_size != 0:
        return
    firmware.set_ram(0, 1024, unit='MiB')
    logger.info('\033[32mget memory info, base: {}, size: {}MB\033[0m {}'.format(0, 1024, LOG_SUFFIX))


def register_get_ram_info(func):
    __get_ram_info.append(func)


register_get_ram_info(by_toh)
register_get_ram_info(by_default)


def get_ram_info(firmware):
    logger.info(TASK_DESCRIPTION)
    ram_base, ram_size = firmware.get_ram()
    if ram_size != 0:
        logger.info('\033[32mhave got memory info, base: {}, size: {}MB\033[0m [DEVICE TREE]'.format(
            0, ram_size))
        return
    for func in __get_ram_info:
        if finished(firmware, 'get_ram_info', func.__name__):
            continue
        func(firmware)
        finish(firmware, 'get_ram_info', func.__name__)
