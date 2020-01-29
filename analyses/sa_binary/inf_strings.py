from analyses.analysis import Analysis
from slcore.parser import get_candidates, get_all_strings
from slcore.naive_parsers.cpu import find_cpu_in_strings, find_cpu_private_peripheral
from slcore.naive_parsers.uart import find_uart
from slcore.naive_parsers.flash import find_flash
from slcore.naive_parsers.cmdline import find_cmdline_in_strings
from slcore.naive_parsers.kernel_version import find_kernel_version_in_strings

import os


class Strings(Analysis):
    def run(self, firmware):
        path_to_kernel = firmware.get_path_to_kernel()

        candidates = get_candidates(path_to_kernel)
        strings = get_all_strings(candidates)

        if strings is None:
            self.context['input'] = 'no strings at all'
            return False

        self.info(firmware, 'get {} strings'.format(len(strings)), 1)

        # kernel version is very critical
        kernel_version = find_kernel_version_in_strings(strings)
        self.info(firmware, 'get kernel version: {}'.format(kernel_version), 1)

        cpu = find_cpu_in_strings(strings)
        self.info(firmware, 'get cpu: {}'.format(cpu), 1)
        # cpu_pp = find_cpu_private_peripheral(cpu)
        # self.info(firmware, 'get cpu_pp: {}'.format(cpu_pp), 1)
        # self.find_uart(firmware)
        # self.find_flash(firmware)
        cmdline = find_cmdline_in_strings(strings)
        self.info(firmware, 'get cmdline: {}'.format(cmdline), 1)

        return True

    def __init__(self, analysis_manager):
        super().__init__(analysis_manager)
        self.name = 'strings'
        self.description = 'handle strings'
        self.required = ['revision']
        self.context['hint'] = 'no strings'
        self.critical = False
        self.settings = ['toh', 'target', 'subtarget', 'cpu', 'uart', 'flash', 'kernel_version']

