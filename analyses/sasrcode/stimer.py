'''
Source Code Info Analysis.
'''
import os

from analyses.analysis import Analysis
from pycparser import c_parser, c_ast, parse_file


class STimer(Analysis):
    def run(self, firmware):
        """
        here is for 'simple timer solution'
        """
        arch = firmware.get_architecture()
        if arch == 'arm':
            entry_point = ''
        elif arch == 'mips':
            entry_point = 'plat_time_init'

        address = firmware.srcodec.symbol2address(entry_point)
        path_to_entry_point = firmware.srcodec.addr2file(address)
        cmdline = firmware.srcodec.get_cmdline(path_to_entry_point)
        path_to_pentry_point = firmware.srcodec.preprocess(path_to_entry_point, cmdline=cmdline)
        funccalls = firmware.srcodec.get_funccalls(path_to_pentry_point, entry_point, mode='sparse')
        self.debug(firmware, '{} -> {}'.format(entry_point, funccalls), 1)

        has_device_tree = False
        for funccall in funccalls:
            if funccall.startswith('of_'):
                has_device_tree = True
            if funccall.find('of_remap') != -1:
                has_device_tree = True

        if has_device_tree:
            self.info(firmware, 'has device tree', 1)
        else:
            self.debug(firmware, 'has no device tree', 1)

        if arch == 'mips':
            # problem:
            # it's not possible to see the two functions below
            # 1) they are defined by inline assembly
            # 2) inline assembly will be ignored by far
            # write_c0_count(0);
            # write_c0_compare(0xffff);
            # so, we search write_c0_count before preprocessing
            path = os.path.join(firmware.srcodec.srcode, path_to_entry_point)
            output = os.popen('grep -nir write_c0_count {}'.format(path)).readlines()
            if len(output):
                self.info(firmware, 'get mips internel timer', 1)

        return True

    def __init__(self, analysis_manager):
        super().__init__(analysis_manager)
        self.name = 'stimer'
        self.description = 'source code info analysis (llvm)'
        self.required = ['sintc']
        self.context['hint'] = ''
        self.critical = False

