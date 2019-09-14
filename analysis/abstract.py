import os
import tempfile
import shutil


def extract_kernel_and_dtb(firmware):
    """
    The patched binwalk must be available.
    """
    if firmware.relative:
        full_path = os.path.join(firmware.storage, firmware.path)
    else:
        full_path = firmware.path
    working_dir = tempfile.gettempdir()
    os.mkdir(os.path.join(working_dir, firmware.uuid))
    target_full_path = shutil.copy(full_path, working_dir)
    print(target_full_path)


def get_kernel_and_dtb(firmware):
    pass
