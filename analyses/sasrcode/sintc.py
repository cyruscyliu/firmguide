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
        cmdline = firmware.srcodec.get_cmdline(path_to_entry_point)
        path_to_pentry_point = firmware.srcodec.preprocess(path_to_entry_point, cmdline=cmdline)
        funccalls = firmware.srcodec.get_funccalls(path_to_pentry_point, entry_point, mode='sparse')
        self.debug(firmware, '{} -> {}'.format(entry_point, funccalls), 1)

        has_device_tree = False
        for funccall in funccalls:
            if funccall.startswith('of_'):
                has_device_tree = True

        if has_device_tree:
            self.info(firmware, 'has device tree', 1)
        else:
            self.debug(firmware, 'has no device tree', 0)

        has_internal_intc = False
        if arch == 'mips':
            # path = os.path.join(firmware.srcodec.srcode, path_to_entry_point)
            # output = os.popen('grep -nir mips_cpu_irq_init {}'.format(path)).readlines()
            # almost all mips cpus define 8 interrupt sources
            if 'mips_cpu_irq_init' in funccalls:
                has_internal_intc = True
            # if len(output):
                # has_internal_intc = True

        if has_internal_intc:
            self.info(firmware, 'get mips internal intc', 1)
        else:
            self.debug(firmware, 'no mips internal intc', 0)

        return True

    def __init__(self, analysis_manager):
        super().__init__(analysis_manager)
        self.name = 'sintc'
        self.description = 'source code info analysis (llvm)'
        self.required = ['ram']
        self.context['hint'] = ''
        self.critical = False

