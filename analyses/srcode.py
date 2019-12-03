"""
Handle all about source code.
"""
import os

from analyses.common.analysis import Analysis


class SRCode(Analysis):
    def run(self, firmware):
        brand = firmware.get_brand()
        if brand != 'openwrt':
            self.context['input'] = 'we can only support OpenWRT'
            return False
        # first, get the source code the vmlinux only by its uuid
        path_to_source_code, path_to_vmlinux = firmware.get_path_to_source_code(), None
        if path_to_source_code is None:
            self.context['input'] = 'no source code available'
            return False
        path_to_vmlinux = os.path.join(path_to_source_code, 'vmlinux')
        path_to_dot_config = os.path.join(path_to_source_code, '.config')
        firmware.set_path_to_source_code(path_to_source_code)
        self.info(firmware, 'get path to source code {}'.format(path_to_source_code), 1)
        firmware.set_path_to_vmlinux(path_to_vmlinux)
        self.info(firmware, 'get path to vmlinux {}'.format(path_to_vmlinux), 1)
        firmware.set_path_to_dot_config(path_to_dot_config)
        self.info(firmware, 'get path to .config {}'.format(path_to_dot_config), 1)
        # then, we are supposed to tell llbic to compile the source code to bitcode
        # TODO tell llbic and it should returen the path to llvm bitcode
        path_to_llvm_bitcode = None
        firmware.set_path_to_llvm_bitcode(path_to_source_code)
        self.info(firmware, 'get path to llvm bitcode {}'.format(path_to_llvm_bitcode), 1)
        return True

    def __init__(self):
        super().__init__()
        self.name = 'srcode'
        self.description = 'process source code'
        self.required = ['strings', 'revision', 'url', 'toh']
        self.context['hint'] = ''
        self.critical = False
