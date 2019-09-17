import os
import tempfile
import shutil
import binwalk
import logging

logger = logging.getLogger()

__extract_kernel_and_dtb = []


def by_binwalk(firmware):
    """
    The patched binwalk must be available.
    """
    pass


def register_extract_kernel_and_dtb(func):
    __extract_kernel_and_dtb.append(func)


def extract_kernel_and_dtb(firmware):
    register_extract_kernel_and_dtb(by_binwalk)



def get_kernel_and_dtb(firmware):
    pass
