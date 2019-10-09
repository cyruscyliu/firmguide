"""
Handle IC.
"""
import os
import yaml
import logging

from analysis.common import get_strings

logger = logging.getLogger()

__get_ic_info = []


def by_device_tree(firmware):
    dtb = firmware.get('dtb')
    if dtb is None:
        return
    logger.info('get ic info by device tree')
    dtc = firmware.get('dtc')
    ic_type, ic_path = None, None
    for path, nodes, props in dtc.walk():
        if path.find('ic@') != -1:
            ic_node = dtc.get_node(path)
            ic_path = os.path.join(ic_node.path, ic_node.name)
    if ic_path is not None:
        ic_compatible = dtc.get_property('compatible', ic_path).data[0]
        logger.info('\033[32mget the ic model: {}\033[0m'.format(ic_compatible))
        firmware.set('ic', key='model', value=ic_compatible, confidence=1)


def by_strings(firmware):
    ic_model = firmware.get('ic', key='model')
    if ic_model is not None:
        return
    logger.info('get ic info by strings')
    strings = get_strings(firmware)
    if strings is None:
        return None
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
    ic_model = firmware.get('ic', key='model')
    if ic_model is None:
        return
    qemu = yaml.safe_load(open(os.path.join(os.getcwd(), 'database', 'ic.yaml')))
    for k, v in qemu.items():
        if v is None:
            continue
        conditions = v['condition_or']
        __flag = 0
        for key in conditions:
            if ic_model.find(key) != -1:
                __flag = 1
                firmware.set('ic', key='qemu', value=k, confidenc=1)
                break
        if __flag:
            break
