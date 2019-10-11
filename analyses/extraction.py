"""
Extract images, such as kernel image, dtb, from firmware blob.

Add your own extractor by register_extract_kernel_and_dtb(your_func).
"""

import os
import binwalk
import logging

from manager import finish, finished

logger = logging.getLogger()
TASK_DESCRIPTION = 'we are going to extract kernel, and dtb if any'

__extract_kernel_and_dtb = []


def by_binwalk(firmware):
    """
    The patched binwalk must be available.
    """
    LOG_SUFFIX = '[BINWALK]'
    for module in binwalk.scan(firmware.working_path, signature=True, extract=True,
                               quiet=True, block=firmware.size, directory=firmware.working_dir):
        count = 0
        for result in module.results:
            if str(result.description).find('flattened image tree') != -1:
                logger.info('\033[32mFIT uImage found, offset {}, {}\033[0m {}'.format(
                    result.offset, result.description, LOG_SUFFIX))
                image_type = 'fit uImage'
                image_path = module.extractor.output[result.file.path].carved[result.offset]
                firmware.set_format(image_type)
                firmware.set_path_to_image(image_path)
                count += 1
                break
            elif str(result.description).find('uImage') != -1:
                logger.info('\033[32mLegacy uImage found, offset {}, {}\033[0m {}'.format(
                    result.offset, result.description, LOG_SUFFIX))
                image_type = 'legacy uImage'
                image_path = module.extractor.output[result.file.path].carved[result.offset]
                firmware.set_format(image_type)
                firmware.set_path_to_image(image_path)
                count += 1
                break
            elif str(result.description).find('TRX') != -1:
                logger.info('\033[32mTRX image found, offset {}, {}\033[0m {}'.format(
                    result.offset, result.description, LOG_SUFFIX))
                image_type = 'trx kernel'
                # because *.trx will be overwrote by *.7z, we replace 7z with trx here
                image_path = module.extractor.output[result.file.path].carved[result.offset].replace('7z', 'trx')
                firmware.set_format(image_type)
                firmware.set_path_to_image(image_path)
                count += 1
                break
            else:
                image_type = 'unknown'
                firmware.set_format(image_type)
                logger.debug("\t%s    0x%.8X    %s [%s]" % (
                    result.file.name, result.offset, result.description, str(result.valid)))

        if not count:
            raise NotImplementedError('no support for other firmware header')


def by_uboot_tools(firmware):
    image_type = firmware.get_format()
    image_path = firmware.get_path_to_image()
    LOG_SUFFIX = '[UBOOT TOOLS]'
    if image_type not in ['fit uImage', 'legacy uImage']:
        return
    if image_type == 'legacy uImage':
        kernel = image_path.replace('uimage', 'kernel')
        os.system('dd if={} of={} bs=1 skip=64 >/dev/null 2>&1'.format(image_path, kernel))
        firmware.set_path_to_kernel(kernel)
        logger.info('\033[32mget kernel image {} at {}\033[0m {}'.format(os.path.basename(kernel), kernel, LOG_SUFFIX))
        firmware.set_path_to_dtb(None)
    elif image_type == 'fit uImage':
        kernel = image_path.replace('uimage.fit', 'kernel')
        dtb = image_path.replace('uimage.fit', 'dtb')
        os.system('dumpimage -T flat_dt -i {} -p 0 {} >/dev/null 2>&1'.format(image_path, kernel))
        firmware.set_path_to_kernel(kernel)
        logger.info('\033[32mget kernel image {} at {}\033[0m {}'.format(os.path.basename(kernel), kernel, LOG_SUFFIX))
        os.system('dumpimage -T flat_dt -i {} -p 1 {} >/dev/null 2>&1'.format(image_path, dtb))
        firmware.set_path_to_dtb(dtb)
        logger.info('\033[32mget device tree image {} at {}\033[0m {}'.format(
            os.path.basename(kernel), dtb, LOG_SUFFIX))


def by_lzma_tools(firmware):
    image_type = firmware.get_format()
    image_path = firmware.get_path_to_image()
    LOG_SUFFIX = '[LZMA TOOLS]'
    if image_type not in ['trx kernel']:
        return

    if image_type == 'trx kernel':
        kernel = image_path.replace('trx', 'kernel')
        os.system('lzma -d < {} > {} 2>/dev/null'.format(image_path, kernel))
        firmware.set_path_to_kernel(kernel)
        logger.info('\033[32mget kernel image {} at {}\033[0m {}'.format(os.path.basename(kernel), kernel, LOG_SUFFIX))
        firmware.set_path_to_dtb(None)


def register_extract_kernel_and_dtb(func):
    __extract_kernel_and_dtb.append(func)


register_extract_kernel_and_dtb(by_binwalk)
register_extract_kernel_and_dtb(by_uboot_tools)
register_extract_kernel_and_dtb(by_lzma_tools)


def extract_kernel_and_dtb(firmware):
    logging.info(TASK_DESCRIPTION)
    for func in __extract_kernel_and_dtb:
        if finished(firmware, 'extract_kernel_and_dtb', func.__name__):
            continue
        func(firmware)
        finish(firmware, 'extract_kernel_and_dtb', func.__name__)
