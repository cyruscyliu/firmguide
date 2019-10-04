"""
Extract images, such as kernel image, dtb, from firmware blob.

Add your own extractor by register_extract_kernel_and_dtb(your_func).
"""

import os
import binwalk
import logging

from manager import finish, finished

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
                image_type = 'fit uImage'
                image_path = module.extractor.output[result.file.path].carved[result.offset]
                firmware.set('image_type', value=image_type)
                firmware.set('image_path', value=image_path)
                count += 1
            elif str(result.description).find('uImage') != -1:
                logger.info(
                    '\033[32mLegacy uImage found\033[0m, offset {}, {}'.format(result.offset, result.description))
                image_type = 'legacy uImage'
                image_path = module.extractor.output[result.file.path].carved[result.offset]
                firmware.set('image_type', value=image_type)
                firmware.set('image_path', value=image_path)
                count += 1
            elif str(result.description).find('TRX') != -1:
                logger.info(
                    '\033[32mTRX image found\033[0m, offset {}, {}'.format(result.offset, result.description)
                )
                image_type = 'trx kernel'
                # because *.trx will be overwrote by *.7z, we replace 7z with trx here
                image_path = module.extractor.output[result.file.path].carved[result.offset].replace('7z', 'trx')
                firmware.set('image_type', value=image_type)
                firmware.set('image_path', value=image_path)
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
    image_type = firmware.get('image_type')
    image_path = firmware.get('image_path')
    if image_type not in ['fit uImage', 'legacy uImage']:
        return
    if image_path is None:
        return
    logger.info('extract kernel and dtb by uboot_tools')

    if image_type == 'legacy uImage':
        kernel = image_path.replace('uimage', 'kernel')
        os.system('dd if={} of={} bs=1 skip=64 >/dev/null 2>&1'.format(image_path, kernel))
        firmware.set('kernel', value=kernel)
        firmware.set('dtb', value=None)
        return
    if firmware.image_type == 'fit uImage':
        kernel = firmware.image_path.replace('uimage.fit', 'kernel')
        dtb = firmware.image_path.replace('uimage.fit', 'dtb')
        os.system('dumpimage -T flat_dt -i {} -p 0 {} >/dev/null 2>&1'.format(firmware.image_path, kernel))
        firmware.set('kernel', value=kernel)
        os.system('dumpimage -T flat_dt -i {} -p 1 {} >/dev/null 2>&1'.format(firmware.image_path, dtb))
        firmware.set('dtb', value=dtb)
        return


def by_lzma_tools(firmware):
    image_type = firmware.get('image_type')
    image_path = firmware.get('image_path')
    if image_type not in ['trx kernel']:
        return
    if image_path is None:
        return
    logger.info('extract kernel and dtb by lzma')

    if image_type == 'trx kernel':
        kernel = image_path.replace('trx', 'kernel')
        os.system('lzma -d < {} > {} 2>/dev/null'.format(image_path, kernel))
        firmware.set('kernel', value=kernel)
        firmware.set('dtb', value=None)


def register_extract_kernel_and_dtb(func):
    __extract_kernel_and_dtb.append(func)


register_extract_kernel_and_dtb(by_binwalk)
register_extract_kernel_and_dtb(by_uboot_tools)
register_extract_kernel_and_dtb(by_lzma_tools)


def extract_kernel_and_dtb(firmware):
    for func in __extract_kernel_and_dtb:
        if finished(firmware, 'extract_kernel_and_dtb', func.__name__):
            continue
        func(firmware)
        finish(firmware, 'extract_kernel_and_dtb', func.__name__)
