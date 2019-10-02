"""
Extract images, such as kernel image, dtb, from firmware blob.

Add your own extractor by register_extract_kernel_and_dtb(your_func).
"""

import os
import binwalk
import logging

logger = logging.getLogger()

__extract_kernel_and_dtb = []


def by_binwalk(firmware):
    """
    The patched binwalk must be available.
    """
    logger.info('extract kernel and dtb by binwalk')
    for module in binwalk.scan(firmware.working_path, signature=True, extract=True,
                               quiet=True, block=firmware.size, directory=firmware.working_dir):
        count = 0
        for result in module.results:
            if str(result.description).find('flattened image tree') != -1:
                logger.info('\033[32mFIT uImage found\033[0m, offset {}, {}'.format(result.offset, result.description))
                firmware.image_type = 'fit uImage'
                firmware.image_path = module.extractor.output[result.file.path].carved[result.offset]
                count += 1
            elif str(result.description).find('uImage') != -1:
                logger.info(
                    '\033[32mLegacy uImage found\033[0m, offset {}, {}'.format(result.offset, result.description))
                firmware.image_type = 'legacy uImage'
                firmware.image_path = module.extractor.output[result.file.path].carved[result.offset]
                count += 1
            elif str(result.description).find('TRX') != -1:
                logger.info(
                    '\033[32mTRX image found\033[0m, offset {}, {}'.format(result.offset, result.description)
                )
                firmware.image_type = 'trx kernel'
                # because *.trx will be overwrote by *.7z, we replace 7z with trx here
                firmware.image_path = module.extractor.output[result.file.path].carved[result.offset].replace('7z',
                                                                                                              'trx')
                count += 1
            else:
                logger.debug("\t%s    0x%.8X    %s [%s]" % (
                    result.file.name, result.offset, result.description, str(result.valid)))

        if not count:
            logger.info('no support for other firmware header')


def by_uboot_tools(firmware):
    """
    firmware.image_type and firmware image_path must be assigned.
    """
    if firmware.image_type not in ['fit uImage', 'legacy uImage']:
        return
    if firmware.image_path is None:
        return
    logger.info('extract kernel and dtb by uboot_tools')

    if firmware.image_type == 'legacy uImage':
        kernel = firmware.image_path.replace('uimage', 'kernel')
        os.system('dd if={} of={} bs=1 skip=64 >/dev/null 2>&1'.format(firmware.image_path, kernel))
        firmware.kernel = kernel
        logger.info('\033[32mget kernel image {} at {}\033[0m'.format(os.path.basename(kernel), kernel))
        firmware.dtb = None
        return
    if firmware.image_type == 'fit uImage':
        kernel = firmware.image_path.replace('uimage.fit', 'kernel')
        dtb = firmware.image_path.replace('uimage.fit', 'dtb')
        os.system('dumpimage -T flat_dt -i {} -p 0 {} >/dev/null 2>&1'.format(firmware.image_path, kernel))
        logger.info('\033[32mget kernel image {} at {}\033[0m'.format(os.path.basename(kernel), kernel))
        firmware.kernel = kernel
        os.system('dumpimage -T flat_dt -i {} -p 1 {} >/dev/null 2>&1'.format(firmware.image_path, dtb))
        logger.info('\033[32mget device tree image {} at {}\033[0m'.format(os.path.basename(kernel), dtb))
        firmware.dtb = dtb
        return


def by_lzma_tools(firmware):
    if firmware.image_type not in ['trx kernel']:
        return
    if firmware.image_path is None:
        return
    logger.info('extract kernel and dtb by lzma')

    if firmware.image_type == 'trx kernel':
        kernel = firmware.image_path.replace('trx', 'kernel')
        os.system('lzma -d < {} > {} 2>/dev/null'.format(firmware.image_path, kernel))
        logger.info('\033[32mget kernel image {} at {}\033[0m'.format(os.path.basename(kernel), kernel))
        firmware.kernel = kernel
        firmware.dtb = None


def register_extract_kernel_and_dtb(func):
    __extract_kernel_and_dtb.append(func)


register_extract_kernel_and_dtb(by_binwalk)
register_extract_kernel_and_dtb(by_uboot_tools)
register_extract_kernel_and_dtb(by_lzma_tools)


def extract_kernel_and_dtb(firmware):
    for func in __extract_kernel_and_dtb:
        func(firmware)


def get_kernel_and_dtb(firmware):
    logger.info('\033[32mgot kernel image at {}\033[0m'.format(firmware.kernel))
    if firmware.dtb is not None:
        logger.info('\033[32mgot device tree at {}\033[0m'.format(firmware.dtb))
