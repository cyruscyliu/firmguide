"""
Handle UART.
"""
import os
import yaml
import logging

from analysis.metadata import get_strings
from manager import finished, finish

logger = logging.getLogger()

__get_uart_info = []


def by_device_tree(firmware):
    dtc = firmware.get('dtc')
    if dtc is None:
        return
    logger.info('get uart info by device tree')
    uart_type, uart_path = None, None
    for path, nodes, props in dtc.walk():
        if path.find('uart@') != -1:
            uart_node = dtc.get_node(path)
            uart_path = os.path.join(uart_node.path, uart_node.name)
    if uart_path is not None:
        uart_compatible = dtc.get_property('compatible', uart_path).data[0]
        firmware.set('uart', key='model', value=uart_compatible, confidence=1)


def by_strings(firmware):
    uart_model = firmware.get('uart', key='model')
    if uart_model is not None:
        return
    logger.info('get uart info by strings')
    strings = get_strings(firmware)
    if strings is None:
        return None
    for string in strings:
        if string.find('uart') != -1:
            if string.find('8250') != -1:
                firmware.set('uart', key='model', value='8250', confidence=1)
                break
            elif string.find('16550') != -1:
                firmware.set('uart', key='model', value='16550', confidence=1)
                break
            else:
                pass


def register_get_uart_info(func):
    __get_uart_info.append(func)


register_get_uart_info(by_device_tree)
register_get_uart_info(by_strings)


def get_uart_info(firmware):
    for func in __get_uart_info:
        if finished(firmware, 'get_uart_info', func.__name__):
            continue
        func(firmware)
        finish(firmware, 'get_uart_info', func.__name__)


def check_qemu_support_for_uart(firmware):
    uart_model = firmware.get('uart', key='model')
    if uart_model is None:
        return
    qemu = yaml.safe_load(open(os.path.join(os.getcwd(), 'database', 'uart.yaml')))
    for k, v in qemu.items():
        if v is None:
            continue
        conditions = v['condition_or']
        __flag = 0
        for key in conditions:
            if uart_model.find(key) != -1:
                __flag = 1
                firmware.set('uart', key='qemu', value=k, confidence=1)
                break
        if __flag:
            break
