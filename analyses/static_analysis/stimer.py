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
            entry_point = 'time_init'

        # this is a simple implementation
        # For mips, time_init includes plat_time_init and
        # mips_clockevent_init, cpu_has_mfc0_count_bug, init_mips_clocksource.
        # Recursively, if time_init has r4k_clockevent_init, r4k_clockevent_init
        # this machine can use the r4k compatile counter as interrupt source
        # and clock source. At the same time, mips_hpt_frequency must be defined
        # to not zero in plat_time_init. Other cases can be discussed seperately.
        address = firmware.srcodec.symbol2address(entry_point)
        path_to_entry_point = firmware.srcodec.addr2file(address)
        cmdline = firmware.srcodec.get_cmdline(path_to_entry_point)
        path_to_pentry_point = firmware.srcodec.preprocess(path_to_entry_point, cmdline=cmdline)
        funccalls = firmware.srcodec.get_funccalls(path_to_pentry_point, entry_point, mode='sparse')
        self.debug(firmware, '{} -> {}'.format(entry_point, funccalls), 1)

        all_funccalls = []
        all_funccalls.extend(funccalls)

        for funccall in funccalls:
            if 'r4k_clockevent_init' == funccall or 'init_r4k_clocksource' == funccall:
                continue
            address = firmware.srcodec.symbol2address(funccall)
            if address is None:
                self.warning(firmware, '{} -> {}(no address)'.format(entry_point, funccall), 1)
                continue
            path_to_entry_point = firmware.srcodec.addr2file(address)
            self.debug(firmware, '{} -> {}({})'.format(entry_point, funccall, path_to_entry_point), 1)
            cmdline = firmware.srcodec.get_cmdline(path_to_entry_point)
            path_to_pentry_point = firmware.srcodec.preprocess(path_to_entry_point, cmdline=cmdline)
            if path_to_pentry_point is None:
                continue
            funccalls2 = firmware.srcodec.get_funccalls(path_to_pentry_point, funccall, mode='sparse')
            self.debug(firmware, '{} -> {}'.format(funccall, funccalls2), 1)
            all_funccalls.extend(funccalls2)

        if arch == 'mips':
            if 'r4k_clockevent_init' in all_funccalls:
                self.info(firmware, 'get mips internel timer as interrupt source', 1)
            if 'init_r4k_clocksource' in all_funccalls:
                self.info(firmware, 'get mips internel timer as clock source', 1)

        if firmware.uuid == 'ar71xx_generic':
            entry_point = ['ath79_clocks_init', 'ath79_get_sys_clk_rate']
            # by manually analysis, to guarentee mips_hpt_frequency not zero
            # ath79_clocks_init has BUG_ON() and is related to ath79_soc set to ar9130,
            # so ar913x_clocks_init will be called and we have
            # ref_rate = 5000000;
            # pll = ath79_pll_rr(0x00);             pll      = *(ath79_pll_rr+0x00)
            # div = ((pll >> 0) & 0x3ff);           div      = (pll >> 0) & 0x3ff
            # freq = div * ref_rate;                freq     = ((pll >> 0) & 0x3ff) * 5000000
            # cpu_rate = freq;                      cpu_rate = ((pll >> 0) & 0x3ff) * 5000000
            # div = ((pll >> 22) & 0x3) + 1;        div      = (pll >> 22) & 0x3) + 1
            # ddr_rate = freq / div;                ddr_rate = (((pll >> 0) & 0x3ff) * 5000000) / ((pll >> 22) & 0x3) + 1)
            # div = (((pll >> 19) & 0x1) + 1) * 2;  div      = (((pll >> 19) & 0x1) + 1) * 2
            # ahb_rate = cpu_rate / div;            ahb_rate = ((pll >> 0) & 0x3ff) * 5000000 / (((pll >> 19) & 0x1) + 1) * 2
            # [FUNCTION] clk_register_clkdev(clk, id, ((void *)0));
            # this function is used to register a clock device with a rate
            # [FUNCTION] clk_get, clk_get_rate
            # these two functions can be used together get the rate of a clkdev by its id
            # ath79_add_sys_clkdev("ref", ref_rate); # an id is a string, a rate is a int
            # ath79_add_sys_clkdev("cpu", cpu_rate);
            # ath79_add_sys_clkdev("ddr", ddr_rate);
            # ath79_add_sys_clkdev("ahb", ahb_rate);
            # [FUNCTION] clk_add_alias is obviously to add a new clock alias
            # clk_add_alias("wdt", ((void *)0), "ahb", ((void *)0));
            # clk_add_alias("uart", ((void *)0), "ahb", ((void *)0));
            # at last, we have 6 clocks with differate rates, they are ref, cpu, ddr, ahb, wdt(=ahb), uart(=ahb)
            # in plat_time_init, we know mips_hpt_frequency = cpu_clk_rate / 2 = cpu_rate = ((pll >> 0) & 0x3ff) * 5000000
            # so the constraint is ((pll >> 0) & 0x3ff) * 5000000 / 2 != 0
            # such that ((pll >> 0) & 0x3ff) * 5000000 > 2
            # such that ((pll >> 0) & 0x3ff) > 1
            # such that the low 10 bits of pll should be large than 0, the first reasonable value is 1 -> 2.5M
            mmio_name = 'ath79_pll_rr'
            mmio_base = eval('(0x18050000 + 0x00)')
            mmio_size = 0x4
            mmio_value = 0x10
            # will be updated in platform_devices.py
            # firmware.insert_bamboo_devices(mmio_base, mmio_size, value=mmio_value)
            self.info(firmware, 'get mmio base {} size {}'.format(hex(mmio_base), hex(mmio_size)), 1)
        else:
            self.warning(firmware, 'you need analyze plat_time_init to guarentee mips_hpt_frequency not 0')

        has_device_tree = False
        for funccall in all_funccalls:
            if funccall.startswith('of_'):
                has_device_tree = True
            if funccall.find('of_remap') != -1:
                has_device_tree = True

        if has_device_tree:
            self.info(firmware, 'has device tree', 1)
        else:
            self.debug(firmware, 'has no device tree', 1)

        return True

    def __init__(self, analysis_manager):
        super().__init__(analysis_manager)
        self.name = 'stimer'
        self.description = 'source code info analysis (llvm)'
        self.required = ['sintc']
        self.context['hint'] = ''
        self.critical = False

