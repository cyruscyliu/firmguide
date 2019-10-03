"""
Handle flash.
"""

import os
import yaml
import logging

from database.dbf import get_database

logger = logging.getLogger()

__get_flash_info = []


def by_device_tree(firmware):
    if firmware.dtb is None:
        return
    logger.info('get flash infor by device tree')
    flash_type, flash_path = None, None
    for path, nodes, props in firmware.dtc.walk():
        if path.find('partition') != -1:
            node = firmware.dtc.get_node(path)
            flash_node = node.parent
            if flash_node.name.find('nand') != -1:
                flash_type = 'nand'
            else:
                flash_type = 'nor'
            flash_path = os.path.join(flash_node.path, flash_node.name)
    if flash_path is not None:
        flash_compatible = firmware.dtc.get_property('compatible', flash_path).data[0]
        logger.info('\033[32mget the flash type: {}\033[0m'.format(flash_type))
        logger.info('\033[32mget the flash model: {}\033[0m'.format(flash_compatible))
        firmware.flash = flash_type
        firmware.flash_model = flash_compatible


def by_toh(firmware):
    if firmware.openwrt is None:
        return
    if firmware.flash is not None:
        return
    logger.info('get ram info by table of hardware')
    pid = firmware.openwrt[0]
    openwrt = get_database('openwrt')
    result = openwrt.select(*['pid', 'flashmb'], pid=pid, row=True)
    flash = result[pid][openwrt.header_last_selected.index('flashmb')]
    if flash != '' and flash != '?':
        # microSD, NAND, CF card, microSDXC, SDHC, eMMC
        if flash.find('NAND') != -1:
            firmware.flash = 'nand'
        else:
            firmware.flash = 'nor'
        logger.info('\033[32mget the flash type: {}\033[0m'.format(firmware.flash))


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
        func(firmware)


__check_qemu_support_for_flash = []


def by_qemu_support_list(firmware):
    if firmware.flash is None:
        return
    qemu = yaml.safe_load(open(os.path.join(os.getcwd(), 'database', 'flash.yaml')))
    support_list = qemu[firmware.flash]
    

def reigster_check_qemu_support_for_flash(func):
    __check_qemu_support_for_flash.append(func)


def check_qemu_support_for_flash(firmware):
    for func in __check_qemu_support_for_flash:
        func(firmware)


def make_flash(firmware):
    pass
