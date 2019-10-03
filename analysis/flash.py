"""
Handle flash.
"""

import os
import yaml
import logging

logger = logging.getLogger()

__get_flash_info = []


def by_device_tree(firmware):
    pass


def by_source_code(firmware):
    pass


def by_strings(firmware):
    pass


def register_get_flash_info(func):
    __get_flash_info.append(func)


register_get_flash_info(by_device_tree)
register_get_flash_info(by_source_code)
register_get_flash_info(by_strings)


def get_flash_info(firmware):
    for func in __get_flash_info:
        func(firmware)


def make_flash(firmware):
    pass
