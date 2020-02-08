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
        srcodec = firmware.get_srcodec()

        # analysis along the intc subsystem flow
        # 1. init_IRQ
        entry_point = 'init_IRQ'
        path_to_entry_point = srcodec.symbol2file(entry_point)
        cmdline = srcodec.get_cmdline(path_to_entry_point)
        path_to_pentry_point = srcodec.preprocess(path_to_entry_point, cmdline=cmdline)
        funccalls = srcodec.get_funccalls(path_to_pentry_point, entry_point, mode='sparse')
        self.debug(firmware, '{} -> {}'.format(entry_point, funccalls), 1)
        # init_IRQ -> ['irq_modify_status', 'arch_init_irq']
        entry_point = 'arch_init_irq'
        path_to_entry_point = srcodec.symbol2file(entry_point)
        cmdline = srcodec.get_cmdline(path_to_entry_point)
        path_to_pentry_point = srcodec.preprocess(path_to_entry_point, cmdline=cmdline)
        funccalls = srcodec.get_funccalls(path_to_pentry_point, entry_point, mode='sparse')
        self.debug(firmware, '{} -> {}'.format(entry_point, funccalls), 1)
        # arch_init_irq -> [
        #     '__builtin_unreachable', => BUG_ON ath79_soc => ar913x(see platform_devices.py)
        #     'mips_cpu_irq_init'      => @001
        #     'ath79_misc_irq_init', 'ar934x_ip2_irq_init', 'qca955x_irq_init', 'qca956x_irq_init',
        # ]
        # almost all mips cpus define 8 interrupt sources
        has_internal_intc = False
        if 'mips_cpu_irq_init' in funccalls:
           has_internal_intc = True
        entry_point = 'ath79_misc_irq_init'
        funccalls = srcodec.get_funccalls(path_to_pentry_point, entry_point, mode='sparse')
        self.debug(firmware, '{} -> {}'.format(entry_point, funccalls), 1)
        # ath79_misc_irq_init -> [
        #     '__builtin_unreachable',          => SAME AS ABOVE
        #     'irq_set_chip_and_handler_name',  @002
        #     '__irq_set_handler'               @003
        # ]
        # and we have two gloable variable set
        # ath79_ip2_handler = ar913x_ip2_handler;
        # ath79_ip3_handler = ar913x_ip3_handler;
        # the other 3 functions will not be called at this time due to ath79_soc
        # ar934x_ip2_irq_init -> ['irq_set_chip_and_handler_name', '__irq_set_handler']
        # qca955x_irq_init -> ['irq_set_chip_and_handler_name', '__irq_set_handler', 'irq_set_chip_and_handler_name', '__irq_set_handler']
        # qca956x_irq_init -> ['irq_set_chip_and_handler_name', '__irq_set_handler', 'irq_set_chip_and_handler_name', '__irq_set_handler']

        # 2. do_asm_IRQ/plat_irq_dispatch
        entry_point = 'plat_irq_dispatch'
        funccalls = srcodec.get_funccalls(path_to_pentry_point, entry_point, mode='sparse')
        self.debug(firmware, '{} -> {}'.format(entry_point, funccalls), 1)
        # plat_irq_dispatch -> ['do_IRQ', 'do_IRQ', 'do_IRQ', 'do_IRQ', 'spurious_interrupt']
        # this function is very special
        # first, it will call read_c0_status and read_c0_cause calculating pending irqn(0-7)
        # at this time, in this function
        # if (pending & STATUSF_IP7) do_IRQ(ATH79_CPU_IRQ(7));
        # else if (pending & STATUSF_IP6) do_IRQ(ATH79_CPU_IRQ(6));
        # else if (pending & STATUSF_IP5) do_IRQ(ATH79_CPU_IRQ(5));
        # else if (pending & STATUSF_IP4) do_IRQ(ATH79_CPU_IRQ(4));
        # else if (pending & STATUSF_IP3) ath79_ip3_handler();
        # else if (pending & STATUSF_IP2) ath79_ip2_handler();
        # else spurious_interrupt();
        # mostly, timer interrupt is IRQ7 and you won't worry about it
        # in this case, UART irqn is 8 + 3 = 11 in [8,40] so UART irqn can be set to 6

        # the flow of the second level handler
        entry_point = 'ath79_misc_irq_handler'
        funccalls = srcodec.get_funccalls(path_to_pentry_point, entry_point, mode='sparse')
        self.debug(firmware, '{} -> {}'.format(entry_point, funccalls), 1)
        # ath79_misc_irq_handler -> ['generic_handle_irq', 'spurious_interrupt']
        # in this function, we know
        # void *base = ath79_reset_base;
        # u32 pending = __raw_readl(base + 0x10) & __raw_readl(base + 0x14);
        # if (!pending) { spurious_interrupt(); return; }
        # while (pending) { int bit = __ffs(pending); generic_handle_irq((8 + (bit))); pending &= ~(1UL << (bit)); }
        # a = (*(base + 0x10)) & (*(base + 0x14))
        # bit = clz(a & -a) (couting the leading zero)
        # obviously bit should be 3, => 0001 0000 0000 0000 == (a & -a) (of low zeros)
        # => a at least xxx1 0000 0000 0000 (prioirty)
        # => base + 0x10 => 0x10000000
        # => base + 0x14 => 0x10000000
        mmio_base = 0x18060010
        mmio_size = 0x4
        mmio_value = 0x10000000
        # firmware.insert_bamboo_devices(mmio_base, mmio_size, value=0) # see platform_devices.py
        self.info(firmware, 'get mmio base {} size {}'.format(hex(mmio_base), hex(mmio_size)), 1)
        mmio_base = 0x18060014
        mmio_size = 0x4
        mmio_value = 0x10000000
        # firmware.insert_bamboo_devices(mmio_base, mmio_size, value=0) # see platform_devices.py
        self.info(firmware, 'get mmio base {} size {}'.format(hex(mmio_base), hex(mmio_size)), 1)
        # IRQ    TYPE         HANDLER                    CHIP            WHERE_BE_SET
        #
        #  6   chained  ath79_misc_irq_handler                              @003
        #  7
        #  8
        #  ...  direct    handle_level_irq       ath79_misc_irq_chip        @002
        #  39
        has_device_tree = False
        for funccall in funccalls:
            if funccall.startswith('of_'):
                has_device_tree = True

        if has_device_tree:
            self.info(firmware, 'has device tree', 1)
        else:
            self.debug(firmware, 'has no device tree', 0)

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

