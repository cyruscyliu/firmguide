import os
import tempfile
import shutil
import binwalk
import logging

logger = logging.getLogger()

def extract_kernel_and_dtb(firmware):
    """
    The patched binwalk must be available.
    """
    if firmware.relative:
        full_path = os.path.join(firmware.storage, firmware.path)
    else:
        full_path = firmware.path
    working_dir = tempfile.gettempdir()
    target_dir = os.path.join(working_dir, firmware.uuid)
    if not os.path.exists(target_dir):
        os.mkdir(os.path.join(working_dir, firmware.uuid))
    target_full_path = shutil.copy(full_path, target_dir)
    logger.info('firmware {} at {}'.format(firmware.uuid, target_full_path))
    for module in binwalk.scan(target_full_path, signature=True, quiet=True):
        for result in module.results:
            print("\t%s    0x%.8X    %s" % (firmware.uuid, result.offset, result.description))


def get_kernel_and_dtb(firmware):
    pass
