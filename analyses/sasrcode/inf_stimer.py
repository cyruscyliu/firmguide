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
        # mask register
        # timer irqn and proper mmio init values to trigger timer's callback
        # proper mmio init values to pass multi-level of intc checkings
        # address to pull down intc signal
        arch = firmware.get_architecture()
        if arch == 'arm':
            entry_point = ''
        elif arch == 'mips':
            entry_point = 'plat_time_init'

        address = firmware.srcodec.symbol2address(entry_point)
        path_to_entry_point = firmware.srcodec.addr2file(address)
        self.info(firmware, 'backbone start_kernel -> init_time -> {}({})'.format(entry_point, path_to_entry_point), 1)
        cmdline = firmware.srcodec.get_cmdline(path_to_entry_point)
        path_to_pentry_point = firmware.srcodec.preprocess(path_to_entry_point, cmdline=cmdline)
        self.debug(firmware, 'get {}'.format(path_to_pentry_point), 1)
        firmware.srcodec.fix_gnu_extensions(path_to_pentry_point)

        funccalls = firmware.srcodec.traverse_func(path_to_pentry_point, entry_point)
        self.debug(firmware, 'get {} in {}'.format(funccalls, entry_point), 1)

        has_device_tree = False
        for funccall in funccalls:
            if funccall.startswith('of_'):
                has_device_tree = True

        if has_device_tree:
            self.info(firmware, 'has device tree', 1)
        else:
            self.info(firmware, 'has no device tree', 1)

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

