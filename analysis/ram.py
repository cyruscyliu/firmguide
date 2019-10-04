"""
Handle RAM
"""
import logging

from database.dbf import get_database
from manager import finished, finish

logger = logging.getLogger()

__get_ram_info = []


def by_device_tree(firmware):
    dtb = firmware.get('dtb')
    if dtb is None:
        return
    logger.info('get ram info by device tree')
    dtc = firmware.get('dtc')
    reg = dtc.get_property('reg', '/memory').data
    [start, end] = reg
    if not start and not end:
        logger.info('get default memory node reg: {}'.format(reg))
        return
    firmware.set('ram', key='start', value=start, confidence=1)
    size = end - start
    firmware.set('ram', key='size', value=size, confidence=1)


def by_toh(firmware):
    toh = firmware.get('toh')
    if toh is None:
        return
    logger.info('get ram info by table of hardware')
    pid = toh[0]
    openwrt = get_database('openwrt')
    result = openwrt.select(*['pid', 'flashmb', 'rammb'], pid=pid, row=True)
    ram = result[pid][openwrt.header_last_selected.index('rammb')]
    if ram != '':
        firmware.set('ram', key='start', value=0, confidence=1)
        firmware.set('ram', key='size', value=ram, confidence=1)
    openwrt.table.close()


def by_loading_address(firmware):
    if not firmware.get('kernel_load_address'):
        return
    if firmware.get('ram', key='size') is not None:
        return
    logger.info('get ram info by loading address')
    loading_address = firmware.get('kernel_load_address')
    firmware.set('ram', key='start', value=0, confidence=1)
    size = (int(loading_address, 16) + 512 * 1024 * 1024) // 1024 // 1024
    firmware.set('ram', key='size', value=size, confidence=1)
    if size > 4 * 1024 * 1024 * 1024:
        logger.warning('the memory size {} seems too large'.format(size))


def by_default(firmware):
    if firmware.get('ram', 'size') is not None:
        return
    logger.info('set ram info by default')
    firmware.set('ram', 'start', value=0, confidence=1)
    firmware.set('ram', 'size', value=1024, confidence=1)


def register_get_ram_info(func):
    __get_ram_info.append(func)


register_get_ram_info(by_device_tree)
register_get_ram_info(by_toh)
register_get_ram_info(by_loading_address)
register_get_ram_info(by_default)


def get_ram_info(firmware):
    for func in __get_ram_info:
        if finished(firmware, 'get_ram_info', func.__name__):
            continue
        func(firmware)
        finish(firmware, 'get_ram_info', func.__name__)
