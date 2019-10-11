"""
Handle UART.
"""
import os
import logging

from analyses.common import get_strings
from manager import finished, finish

logger = logging.getLogger()
TASK_DESCRIPTION = 'we are inferring the uart'

__get_uart_info = []


def by_strings(firmware):
    LOG_SUFFIX = '[STRINGS]'
    uart_model = firmware.get_uart_model()
    if uart_model is not None:
        return
    strings = get_strings(firmware)
    if strings is None:
        return None
    for string in strings:
        if string.find('uart') != -1:
            if string.find('8250') != -1:
                firmware.set_uart_model('8250')
                logger.info('\033[32muart model {} found\033[0m {}'.format(uart_model, LOG_SUFFIX))
                break
            elif string.find('16550') != -1:
                firmware.set_uart_model('16550A')
                logger.info('\033[32muart model {} found\033[0m {}'.format(uart_model, LOG_SUFFIX))
                break
            else:
                pass


def register_get_uart_info(func):
    __get_uart_info.append(func)


register_get_uart_info(by_strings)


def get_uart_info(firmware):
    logger.info(TASK_DESCRIPTION)
    uart_model = firmware.get_uart_model()
    if uart_model is not None:
        logger.info('\033[32muart model {} found\033[0m [DEVICE TREE]'.format(uart_model))
        return
    for func in __get_uart_info:
        if finished(firmware, 'get_uart_info', func.__name__):
            continue
        func(firmware)
        finish(firmware, 'get_uart_info', func.__name__)
