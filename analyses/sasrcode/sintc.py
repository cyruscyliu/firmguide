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
        if firmware.uuid in ['bcm47xx']:
            firmware.srcodec.fix_gnu_extensions(path_to_pentry_point)
            funccalls = firmware.srcodec.traverse_func(path_to_pentry_point, entry_point)
        elif firmware.uuid == 'ar71xx_generic':
            funccalls = [
                'soc_is_ar71xx',
                'soc_is_ar724x',
                'soc_is_ar913x',
                'soc_is_ar933x',
                'soc_is_ar934x',
                'soc_is_qca953x',
                'soc_is_qca955x',
                'soc_is_qca956x',
                'BUG',
                'mips_cpu_irq_init',
                'ath79_misc_irq_init',
                'ar934x_ip2_irq_init',
                'qca955x_irq_init',
                'soc_is_qca956x',
                'qca956x_irq_init',
            ]
        elif firmware.uuid == 'adm5120':
            funccalls = [
                'mips_cpu_irq_init',
                'adm5120_intc_irq_init'
            ]
        elif firmware.uuid == 'ar231x':
            funccalls = [
                'clear_c0_status',
                 'mips_cpu_irq_init',
                 'ar5312_irq_init',
                 'ar2315_irq_init'
            ]
        elif firmware.uuid == 'ralink':
            funccalls = [
                'of_irq_init'
            ]
        elif firmware.uuid == 'ar7':
            funccalls = [
                'mips_cpu_irq_init',
                'ar7_irq_init'
            ]
        else:
            funccalls = []
            self.debug(firmware, 'source at {}, please check by yourself'.format(firmware.srcodec.srcode), 1)
        self.debug(firmware, 'get {} in {}'.format(funccalls, entry_point), 1)

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

