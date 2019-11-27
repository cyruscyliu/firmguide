"""
Handle all about source code.
"""
import os
import logging

from analyses.common.analysis import Analysis

logger = logging.getLogger()


class SRCode(Analysis):
    def run(self, firmware):
        brand = firmware.get_brand()
        if brand != 'openwrt':
            self.context['input'] = 'we can only support OpenWRT'
            return False
        # first, we tell openwrt-build-docker to build our machine
        # we need a openwrt_revision, a machine_name, and an openwrt .config
        revision = firmware.get_revision()  # 1
        machine_name = firmware.sget_machine_name()
        path_to_dot_config = firmware.get_path_to_dot_config()
        # TODO tell openwrt-build-docker and it should return the path to source code
        # and path to vmlinux
        path_to_source_code = None
        firmware.set_path_to_source_code(path_to_source_code)
        self.info('get path to source {}'.format(path_to_source_code))
        # then, we are supposed to tell llbic to compile the source code to bitcode
        # TODO tell llbic and it should returen the path to llvm bitcode
        path_to_llvm_bitcode = None
        firmware.set_path_to_llvm_bitcode(path_to_source_code)
        self.info('get path to llvm bitcode {}'.format(path_to_llvm_bitcode))
        return True

    def __init__(self):
        super().__init__()
        self.name = 'srcode'
        self.description = 'process source code'
        self.log_suffix = '[SRCODE]'
        self.required = ['strings', 'revision', 'url', 'toh']
        self.context['hint'] = ''
        self.critical = True
