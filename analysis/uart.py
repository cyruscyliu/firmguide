"""
Handle UART.
"""
import os
import yaml
import logging

from analysis.metadata import get_strings

logger = logging.getLogger()

__get_uart_info = []


def by_device_tree(firmware):
    if firmware.dtb is None:
        return
    logger.info('get uart info by device tree')
    uart_type, uart_path = None, None
    for path, nodes, props in firmware.dtc.walk():
        if path.find('uart@') != -1:
            uart_node = firmware.dtc.get_node(path)
            uart_path = os.path.join(uart_node.path, uart_node.name)
    if uart_path is not None:
        uart_compatible = firmware.dtc.get_property('compatible', uart_path).data[0]
        logger.info('\033[32mget the uart model: {}\033[0m'.format(uart_compatible))
        firmware.uart_model = uart_compatible


def by_strings(firmware):
    if firmware.uart_model is not None:
        return
    logger.info('get uart info by strings')
    strings = get_strings(firmware)
    for string in strings:
        if string.find('uart') != -1:
            if string.find('8250') != -1:
                firmware.uart_model = '8250'
                logger.info('\033[32mget the uart model: {}\033[0m'.format('uart8250'))
                break
            elif string.find('16550') != -1:
                firmware.uart_model = '16550'
                logger.info('\033[32mget the uart model: {}\033[0m'.format('uart16550'))
                break
            else:
                pass


def register_get_uart_info(func):
    __get_uart_info.append(func)


register_get_uart_info(by_device_tree)
register_get_uart_info(by_strings)


def get_uart_info(firmware):
    for func in __get_uart_info:
        func(firmware)


def check_qemu_support_for_uart(firmware):
    if firmware.uart_model is None:
        return
    qemu = yaml.safe_load(open(os.path.join(os.getcwd(), 'database', 'uart.yaml')))
    for k, v in qemu.items():
        if v is None:
            continue
        conditions = v['condition_or']
        __flag = 0
        for key in conditions:
            if firmware.uart_model.find(key) != -1:
                logger.info('\033[32mQEMU {} supports {}\033[0m'.format(k, firmware.uart_model))
                __flag = 1
                firmware.uart_model = k
                break
        if __flag:
            break
