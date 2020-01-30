import os
import re

from slcore.compositor import UNKNOWN, TRX_KERNEL, LEGACY_UIMAGE, FIT_UIMAGE
from slcore.naive_parsers.kernel_version import *
from analyses.analysis import Analysis


class Kernel(Analysis):
    def run(self, firmware):
        image_type = firmware.get_format()
        image_path = firmware.get_path_to_image()

        kernel_load_address = None  # not critical, to avoid referenced before assignment
        kernel_entry_point = None  # not critical, to avoid referenced before assignment
        if image_type == LEGACY_UIMAGE:
            kernel_version = find_kernel_version_in_legacy_uimage(image_path)
        elif image_type == FIT_UIMAGE:
            kernel_version = find_kernel_version_in_fit_uimage(image_path)
        else:
            self.context['input'] = 'this image type {} is not supported'.format(image_type)
            return False
        firmware.set_kernel_version(kernel_version)
        self.info(firmware, 'get kernel version: {}'.format(kernel_version), 1)
        return True

    def __init__(self, analysis_manager):
        super().__init__(analysis_manager)
        self.name = 'kernel'
        self.description = 'extract kernel related information from the given firmware'
        self.context['hint'] = 'you must add strings parsers'
        self.required = []
        self.critical = False
        self.settings = ['kernel_version']
