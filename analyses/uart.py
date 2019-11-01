"""
Handle UART.
"""
import os
import logging

from analyses.lib.strings import get_strings
from manager import finished, finish

logger = logging.getLogger()
TASK_DESCRIPTION = 'we are inferring the uart'

__get_uart_info = []


def by_strings(firmware):
    LOG_SUFFIX = '[STRINGS]'
    strings = get_strings(firmware)
    if strings is None:
        return None
    for string in strings:
        if string.find('8250') != -1 or string.find('16550') != -1:
            firmware.set_uart_model('ns16550A')
            logger.info('\033[32muart model {} found\033[0m {}'.format('ns16550A', LOG_SUFFIX))
            break
        else:
            pass
    for string in strings:
        if string.find('root=') != -1:
            # root=/dev/mtdblock1 rootfstype=squashfs,jffs2 noinitrd console=ttyS0,115200\n
            a, _, b = string.partition('console=')
            if _ is '':
                continue
            else:
                uart_baud = b.split(',')[1].strip()
                firmware.set_uart_baud(uart_baud)
                logger.info('\033[32muart baud {} found\033[0m {}'.format(uart_baud, LOG_SUFFIX))
                break


def register_get_uart_info(func):
    __get_uart_info.append(func)


register_get_uart_info(by_strings)


def get_uart_info(firmware):
    logger.info(TASK_DESCRIPTION)
    for func in __get_uart_info:
        if finished(firmware, 'get_uart_info', func.__name__):
            continue
        func(firmware)
        finish(firmware, 'get_uart_info', func.__name__)
