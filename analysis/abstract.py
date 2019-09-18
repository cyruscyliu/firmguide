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
    logger.info('extract kernel and dtb by binwalk')
    for module in binwalk.scan(firmware.working_path, signature=True, quiet=True, block=firmware.size):
        for result in module.results:
            print("\t%s    0x%.8X    %s [%s]" % (
                result.file.name, result.offset, result.description, str(result.valid)))


def register_extract_kernel_and_dtb(func):
    __extract_kernel_and_dtb.append(func)


register_extract_kernel_and_dtb(by_binwalk)


def extract_kernel_and_dtb(firmware):
    for func in __extract_kernel_and_dtb:
        func(firmware)


def get_kernel_and_dtb(firmware):
    pass
