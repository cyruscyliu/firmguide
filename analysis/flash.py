"""
Handle flash.
"""

import os
import yaml
import logging

from database.dbf import get_database
from manager import finished, finish

logger = logging.getLogger()

__get_flash_info = []


def by_device_tree(firmware):
    dtb = firmware.get('dtb')
    if dtb is None:
        return
    logger.info('get flash info by device tree')
    dtc = firmware.get('dtc')
    flash_type, flash_path = None, None
    for path, nodes, props in dtc.walk():
        if path.find('partition') != -1:
            node = dtc.get_node(path)
            flash_node = node.parent
            if flash_node.name.find('nand') != -1:
                flash_type = 'nand'
            else:
                flash_type = 'nor'
            flash_path = os.path.join(flash_node.path, flash_node.name)
    if flash_path is not None:
        flash_compatible = dtc.get_property('compatible', flash_path).data[0]
        firmware.set('flash', key='type', value=flash_type, confidence=1)
        firmware.set('flash', key='model', value=flash_compatible, confidence=1)


def by_toh(firmware):
    toh = firmware.get('toh')
    if toh is None:
        return
    flash = firmware.get('flash', key='type')
    if flash is not None:
        return
    logger.info('get ram info by table of hardware')
    pid = toh[0]
    openwrt = get_database('openwrt')
    result = openwrt.select(*['pid', 'flashmb'], pid=pid, row=True)
    flash = result[pid][openwrt.header_last_selected.index('flashmb')]
    if flash != '' and flash != '?':
        # microSD, NAND, CF card, microSDXC, SDHC, eMMC
        if flash.find('NAND') != -1:
            firmware.set('flash', key='type', value='nand', confidence=1)
        else:
            firmware.set('flash', key='type', value='nor', confidence=1)


def by_source_code(firmware):
    pass


def by_strings(firmware):
    pass


def register_get_flash_info(func):
    __get_flash_info.append(func)


register_get_flash_info(by_device_tree)
register_get_flash_info(by_toh)
register_get_flash_info(by_source_code)
register_get_flash_info(by_strings)


def get_flash_info(firmware):
    for func in __get_flash_info:
        if finished(firmware, 'get_flash_info', func.__name__):
            continue
        func(firmware)
        finish(firmware, 'get_flash_info', func.__name__)


__check_qemu_support_for_flash = []


def by_qemu_support_list(firmware):
    flash_type = firmware.get('flash', key='type')
    if flash_type is None:
        return
    qemu = yaml.safe_load(open(os.path.join(os.getcwd(), 'database', 'flash.yaml')))
    support_list = qemu[flash_type]


def reigster_check_qemu_support_for_flash(func):
    __check_qemu_support_for_flash.append(func)


def check_qemu_support_for_flash(firmware):
    for func in __check_qemu_support_for_flash:
        if finished(firmware, 'check_qemu_support_for_flash', func.__name__):
            continue
        func(firmware)
        finish(firmware, 'check_qemu_support_for_flash', func.__name__)
