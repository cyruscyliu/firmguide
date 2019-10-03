"""
Handle IC.
"""
import os
import yaml
import logging

from analysis.metadata import get_strings

logger = logging.getLogger()

__get_ic_info = []


def by_device_tree(firmware):
    if firmware.dtb is None:
        return
    logger.info('get ic info by device tree')
    ic_type, ic_path = None, None
    for path, nodes, props in firmware.dtc.walk():
        if path.find('ic@') != -1:
            ic_node = firmware.dtc.get_node(path)
            ic_path = os.path.join(ic_node.path, ic_node.name)
    if ic_path is not None:
        ic_compatible = firmware.dtc.get_property('compatible', ic_path).data[0]
        logger.info('\033[32mget the ic model: {}\033[0m'.format(ic_compatible))
        firmware.ic_model = ic_compatible


def by_strings(firmware):
    if firmware.ic_model is not None:
        return
    logger.info('get ic info by strings')
    strings = get_strings(firmware)
    for string in strings:
        if string.find('ic') != -1:
            break


def register_get_ic_info(func):
    __get_ic_info.append(func)


register_get_ic_info(by_device_tree)
register_get_ic_info(by_strings)


def get_ic_info(firmware):
    for func in __get_ic_info:
        func(firmware)


def check_qemu_support_for_ic(firmware):
    if firmware.ic_model is None:
        return
    qemu = yaml.safe_load(open(os.path.join(os.getcwd(), 'database', 'ic.yaml')))
    for k, v in qemu.items():
        if v is None:
            continue
        conditions = v['condition_or']
        __flag = 0
        for key in conditions:
            if firmware.ic_model.find(key) != -1:
                logger.info('\033[32mQEMU {} supports {}\033[0m'.format(k, firmware.ic_model))
                __flag = 1
                firmware.ic_model = k
                break
        if __flag:
            break
