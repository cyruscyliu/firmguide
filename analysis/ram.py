"""
Handle RAM
"""
import os
import logging

from analysis.common import vote
from database.dbf import get_database

logger = logging.getLogger()

__get_ram_info = []


def by_device_tree(firmware):
    if firmware.dtb is None:
        return
    logger.info('get ram info by device tree')
    reg = firmware.dtc.get_property('reg', '/memory').data
    [start, end] = reg
    if not start and not end:
        logger.info('get default memory node reg: {}'.format(reg))
        return
    firmware.ram_start = start
    firmware.ram_size = end - start
    logger.info('\033[32get memory info, base: {}, size: \033[0m'.format(start, end - start))


def by_toh(firmware):
    if firmware.openwrt is None:
        return
    logger.info('get ram info by table of hardware')
    pid = firmware.openwrt[0]
    openwrt = get_database('openwrt')
    result = openwrt.select(*['pid', 'flashmb', 'rammb'], pid=pid, row=True)
    ram = result[pid][openwrt.header_last_selected.index('rammb')]
    if ram != '':
        firmware.ram_start = 0
        firmware.ram_size = ram
        logger.info('\033[32mget memory info, base: {}, size: {}MB\033[0m'.format(0, ram))
    openwrt.table.close()


def by_loading_address(firmware):
    if not (firmware.metadata['kernel_load_address']):
        return
    if firmware.ram_size is not None:
        return
    logger.info('get ram info by loading address')
    loading_address = vote(firmware.metadata['kernel_load_address'], 'kernel load address')
    firmware.ram_start = 0
    firmware.ram_size = (int(loading_address, 16) + 512 * 1024 * 1024) // 1024 // 1024
    logger.info('\033[32mget memory info, base: {}, size: {}MB\033[0m'.format(0, firmware.ram_size))
    if firmware.ram_size > 4 * 1024 * 1024 * 1024:
        logger.warning('the memory size {} seems too large'.format(firmware.ram_size))


def by_default(firmware):
    if firmware.ram_size is not None:
        return
    logger.info('set ram info by default')
    firmware.ram_size = 0
    firmware.ram_start = 1 * 1024
    logger.info('\033[32mget memory info, base: {}, size: {}MB\033[0m'.format(0, firmware.ram_size))


def register_get_ram_info(func):
    __get_ram_info.append(func)


register_get_ram_info(by_device_tree)
register_get_ram_info(by_toh)
register_get_ram_info(by_loading_address)
register_get_ram_info(by_default)


def get_ram_info(firmware):
    for func in __get_ram_info:
        func(firmware)


def make_ram(firmware):
    pass
