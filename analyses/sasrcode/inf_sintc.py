'''
Source Code Info Analysis.
'''
import os

from analyses.analysis import Analysis
from pycparser import c_parser, c_ast, parse_file


class SINTC(Analysis):
    def run(self, firmware):
        """
        here is for 'simple interrupt controller solution'
        """
        # mask register
        # timer irqn and proper mmio init values to trigger timer's callback
        # proper mmio init values to pass multi-level of intc checkings
        # address to pull down intc signal
        arch = firmware.get_architecture()
        if arch == 'arm':
            entry_point = ''
        elif arch == 'mips':
            entry_point = 'arch_init_irq'

        address = firmware.srcodec.symbol2address(entry_point)
        path_to_entry_point = firmware.srcodec.addr2file(address)
        self.info(firmware, 'backbone start_kernel -> init_IRQ {}({})'.format(entry_point, path_to_entry_point), 1)
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
            if 'mips_cpu_irq_init' in funccalls:
                # almost all mips cpus define 8 interrupt sources
                self.info(firmware, 'get mips internal intc', 1)

        return True

    def __init__(self, analysis_manager):
        super().__init__(analysis_manager)
        self.name = 'sintc'
        self.description = 'source code info analysis (llvm)'
        self.required = ['cpu']
        self.context['hint'] = ''
        self.critical = False

