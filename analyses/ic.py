"""
Handle IC.
"""
import os
import logging

from analyses.common import get_strings
from manager import finished

logger = logging.getLogger()
TASK_DESCRIPTION = 'we are inferring the interrupt controller'

__get_ic_info = []


def by_strings(firmware):
    LOG_SUFFIX = '[STRINGS]'
    ic_model = firmware.get_interrupt_controller_model()
    if ic_model is not None:
        return
    strings = get_strings(firmware)
    if strings is None:
        return None
    for string in strings:
        if string.find('ic') != -1:
            break


def register_get_ic_info(func):
    __get_ic_info.append(func)


register_get_ic_info(by_strings)


def get_ic_info(firmware):
    logger.info(TASK_DESCRIPTION)
    ic_model = firmware.get_interrupt_controller_model()
    if ic_model is not None:
        logger.info('\033[32mic model {} found\033[0m [DEVICE TREE]'.format(ic_model))
        return
    for func in __get_ic_info:
        if finished(firmware, 'get_interrupt_controller_info', func.__name__):
            continue
        func(firmware)
        finished(firmware, 'get_interrupt_controller_info', func.__name__)
