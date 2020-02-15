'''
Source Code Info Analysis.
'''
import os
import re

from analyses.analysis import Analysis
from pycparser import c_parser, c_ast, parse_file
from analyses.static_analysis.builtin import UNMODELED_SKIP_LIST, MODELED_SKIP_TABLE


class ExecutionFlow(Analysis):
    def traverse_struct(self, firmware, path_to_st):
        # because we cannot use pycparser now, simply we can get the setup function
        # from source code using regular expression
        # MIPS_MACHINE(ATH79_MACH_CARAMBOLA2, "CARAMBOLA2", "8devices Carambola2 board", carambola2_setup);
        string = ''
        with open(os.path.join(firmware.srcodec.get_path_to_source_code(), path_to_st)) as f:
            for line in f:
                string += line.strip()
        match = re.search(r'MIPS_MACHINE\(\s*[_A-Z0-9]+\s*,\s*".*?"\s*,\s*".*?"\s*,\s*([_a-zA-Z0-9]+)\s*\)', string)
        setup = match.group(1)
        return setup

    def get_funccalls(self, firmware, ep, caller='do_initcall'):
        path_to_entry_point = firmware.srcodec.symbol2file(ep)
        if path_to_entry_point is None:
            path_to_entry_point = firmware.srcodec.symbol2fileg(ep)
        if path_to_entry_point is None:
            self.warning(firmware, '{} -> {}(no address)'.format(caller, ep), 1)
            return None, None, [], {}

        if path_to_entry_point.startswith('fs'):
            self.debug(firmware, '{} -> {}(built-in function in {})'.format(caller, ep, path_to_entry_point), 1)
            return None, path_to_entry_point, [], {}

        if path_to_entry_point.endswith('.h'):
            path_to_entry_point = firmware.srcodec.symbol2fileg(ep)
            if path_to_entry_point is None:
                self.warning(firmware, '{} -> {}(inline in header)'.format(caller, ep, path_to_entry_point), 1)
                return None, path_to_entry_point, [], {}
        self.debug(firmware, '{} -> {}({})'.format(caller, ep, path_to_entry_point), 1)

        cmdline = firmware.srcodec.get_cmdline(path_to_entry_point)
        path_to_pentry_point = firmware.srcodec.preprocess(path_to_entry_point, cmdline=cmdline)
        if path_to_pentry_point is None:
            self.debug(firmware, '{} -> {}(error in preprocessing)'.format(caller, ep, path_to_entry_point), 1)
            return None, None, [], {}

        funccalls = firmware.srcodec.get_funccalls(path_to_pentry_point, ep, mode='sparse')
        gs = firmware.srcodec.get_globals(path_to_pentry_point, ep, mode='sparse')

        return None, path_to_entry_point, funccalls, gs

    def parse_globals(self, firmware, caller, gs):
        """
        Globals will not trigger analysis but serve for debugging.
        Global data/function pointer both will influence execution flow.
        Global data is interesting when
        1) it is defined by the value from nvram
        2) it is defined by the value from ioremap().
        Global data is interesting when
        1) it is defined conditionally
        2) it is defined according to CMDLINE
        """
        for g, ops in gs.items():
            if 'store' in ops:
                self.globals.append(g)
                # self.debug(firmware, '{} -> {}(global defined)'.format(caller, g), 1)
            if 'load' in ops and g not in self.globals:
                # self.warning(firmware, '{} -> {}(global used before defined)'.format(caller, g), 1)
                pass


    def parse_funcalls(self, firmware, caller, funccalls):
        def remove_duplicated(seq):
                seen = set()
                seen_add = seen.add
                return [x for x in seq if not (x in seen or seen_add(x))]
        funccalls = remove_duplicated(funccalls)

        # remove functions we donot want to analyze
        for da in UNMODELED_SKIP_LIST:
            if da in funccalls:
                # self.debug(firmware, '{} -> {}(built-in function)'.format(caller, da), 1)
                funccalls.remove(da)

        # remove functions we have already analyzed
        for da in MODELED_SKIP_TABLE:
            if da in funccalls:
                funccalls.remove(da)
                MODELED_SKIP_TABLE[da]['handle'](self, firmware, caller=caller)

        # remove funcations addr2line cannot handle correct
        for da in ['ath79_gpio_init', 'ath79_gpio_function_setup']:
            if da in funccalls:
                self.debug(firmware, '{} -> {}(addr2line)'.format(caller, da), 1)
                funccalls.remove(da)

        # remove funcations sparse cannot handle correct
        for da in ['ath79_register_gpio_keys_polled']:
            if da in funccalls:
                self.debug(firmware, '{} -> {}(sparse)'.format(caller, da), 1)
                funccalls.remove(da)

        if '__platform_driver_register' in funccalls:
            funccalls.remove('__platform_driver_register')


        # [FUNCTION] void mips_machine_setup(void);
        # this function decides which machine->setup to be called according to a kernel boot args
        if firmware.get_arch() == 'mips' and 'mips_machine_setup' in funccalls:
            funccalls.remove('mips_machine_setup')
            # according to arch/mips/include/asm/mips_machine.h, we have
            # system_map = firmware.srcodec.parse_system_map()
            # for symbol, v in system_map.items():
                # machine_id_##_type
                # if symbol.startswith('machine_id'):
                    # addr2line not work for data
                    # machine_type = symbol[11:]
                    # output = os.popen('grep -nir "MIPS_MACHINE({}" {}/arch/{}'.format(
                        # machine_type, firmware.srcodec.srcode, firmware.get_arch())).readlines()
                    # assert len(output), 'where is the symbol {}'.format(machine_type)
                    # output = output[0].split(':')[0][len(firmware.srcodec.srcode)+1:]
                    # machine_setup = self.traverse_struct(firmware, output)
                    # self.debug(firmware, 'get mips machine type {} -> {}'.format(machine_type, machine_setup), 1)
                    # funccalls.append(machine_setup)
            funccalls.append('bhu_bxu2000n2_a1_setup')


        # [FUNCTION]  struct irq_domain *irq_domain_add_legacy(struct device_node *of_node, unsigned int size,
        # unsigned int first_irq, irq_hw_number_t first_hwirq, const struct irq_domain_ops *ops, void *host_data);
        if 'irq_domain_add_legacy' in funccalls:
            funccalls.remove('irq_domain_add_legacy')
            if firmware.uuid == 'rampis_rt3883':
                if caller == 'mips_cpu_intc_init':
                    # domain = irq_domain_add_legacy(of_node, 8, 0, 0, &mips_cpu_intc_irq_domain_ops, ((void *)0));
                    # for i in range(0, 8):
                    #     analysis.debug(firmware, '{0} {0} direct mips_cpu_intc_irq_domain_ops None'.format(i), 1)
                    # it not only tells us hw0-7 -> irqn0-7, but also shows irqchip in xxx_ops
                    self.debug(firmware, '{} -> {}(FP -> [mips_cpu_intc_map])'.format(caller, 'irq_domain_add_legacy'), 1)
                    funccalls.extend(['mips_cpu_intc_map'])
                elif caller == 'intc_of_init':
                    # domain = irq_domain_add_legacy(node, 32, 8, 0, &irq_domain_ops, ((void *)0));
                    # for i in range(0, 32):
                    #     analysis.debug(firmware, '{0} {1} direct mips_cpu_intc_irq_domain_ops None'.format(i, i+8), 1)
                    # it not only tells us hw0-31 -> irqn8-39, but also shows irqchip in xxx_ops
                    self.debug(firmware, '{} -> {}(FP -> [intc_map])'.format(caller, 'irq_domain_add_legacy'), 1)
                    funccalls.extend(['intc_map'])
                else:
                    analysis.warning(firmware, '{} -> irq_domain_add_legacy(w/o handler)'.format(caller), 0)
            else:
                analysis.warning(firmware, '{} -> irq_domain_add_legacy(w/o handler)'.format(caller), 0)

        # [FUNCTION] void __init of_irq_init(const struct of_device_id *matches)
        if 'of_irq_init' in funccalls:
            funccalls.remove('of_irq_init')
            if firmware.uuid == 'rampis_rt3883':
                if caller == 'arch_init_irq':
                    # you have to analyze its parameter
                    # static struct of_device_id __attribute__ ((__section__(".init.data"))) of_irq_ids[] = {
                    #   { .compatible = "mti,cpu-interrupt-controller", .data = mips_cpu_intc_init  },
                    #   { .compatible = "ralink,rt2880-intc", .data = intc_of_init  },
                    #   {},
                    # };
                    # of_irq_init(of_irq_ids);
                    funccalls.extend(['mips_cpu_intc_init', 'intc_of_init'])
                    self.debug(firmware, '{} -> {}(FP -> [mips_cpu_intc_init, intc_of_init])'.format(caller, 'of_irq_init'), 1)
                else:
                    self.warning(firmware, 'of_irq_init found w/o handler', 0)
            else:
                self.warning(firmware, 'of_irq_init found w/o handler', 0)

        return funccalls

    def traverse_funccalls(self, firmware, entry_point, caller=None, depth=0):
        if depth == 4:
            return
        for ep in entry_point:
            address, path_to_ep, funccalls, gs = self.get_funccalls(firmware, ep, caller=caller)
            funccalls = self.parse_funcalls(firmware, ep, funccalls)
            self.parse_globals(firmware, ep, gs)
            self.traverse_funccalls(firmware, funccalls, caller=ep, depth=depth+1)

    def traverse_no_address_funccall(self, firmware, ep, path_to_entry_point):
        cmdline = firmware.srcodec.get_cmdline(path_to_entry_point)
        path_to_pentry_point = firmware.srcodec.preprocess(path_to_entry_point, cmdline=cmdline)
        funccalls = firmware.srcodec.get_funccalls(path_to_pentry_point, ep, mode='sparse')
        self.info(firmware, '{} -> {}'.format(ep, funccalls), 1)
        gs = firmware.srcodec.get_globals(path_to_pentry_point, ep, mode='sparse')
        funccalls = self.parse_funcalls(firmware, ep, funccalls)
        self.parse_globals(firmware, ep, gs)
        self.traverse_funccalls(firmware, funccalls, caller=ep)

    def traverse_indirect_funccall(self, firmware, ep, caller):
        self.traverse_funccalls(firmware, [ep], caller=caller)

    def run(self, firmware):
        srcodec = firmware.get_srcodec()

        if firmware.uuid == 'ar71xx_generic':
            ## =========== from stinc.py =============
            firmware.insert_bamboo_devices(0x18060010, 0x4, value=0x10000000)
            firmware.insert_bamboo_devices(0x18060014, 0x4, value=0x10000000)
            ## =======================================
            ## =========== from stimer.py ==============
            firmware.insert_bamboo_devices(0x18050000, 0x4, value=0x10)
            ## =========================================

        # ===== intc subsystem =====
        # 1 intc initilization
        ep = 'init_IRQ'
        # self.traverse_funccalls(firmware, [ep], caller='start_kernel')
        if firmware.uuid == 'ar71xx_generic':
            # arch_init_irq -> ath79_misc_irq_init(no address)
            self.traverse_no_address_funccall(firmware, 'ath79_misc_irq_init', 'arch/mips/ath79/irq.c')
        # 2. do_asm_IRQ/plat_irq_dispatch(not neccesory)
        if firmware.get_arch() == 'arm':
            ep = 'do_asm_IRQ'
            self.traverse_funccalls(firmware, [ep], caller='start_kernel')
        elif firmware.get_arch() == 'mips':
            self.info(firmware, 'interrupt -> plat_irq_dispatch(found, level1 intc mmio->irqn mapping)', 1)

        # for mips, you could skip plat_irq_dispatch because it is very general
        # mostly, timer interrupt is IRQ7 and you won't worry about it

        # ==== timer subsystem ====
        ep = 'time_init'
        # this is a simple implementation
        # For mips, time_init includes plat_time_init and
        # mips_clockevent_init, cpu_has_mfc0_count_bug, init_mips_clocksource.
        # Recursively, if time_init has r4k_clockevent_init, r4k_clockevent_init
        # this machine can use the r4k compatile counter as interrupt source
        # and clock source. At the same time, mips_hpt_frequency must be defined
        # to not zero in plat_time_init. Other cases can be discussed seperately.
        # self.traverse_funccalls(firmware, [ep], caller='start_kernel')

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
            self.warning(firmware, 'you need analyze plat_time_init to guarentee mips_hpt_frequency not 0', 0)

        # do_initcall analysis
        # "early", "core", "postcore", "arch", "subsys", "fs", "device", "late",
        path_to_entry_point = firmware.srcodec.symbol2file('remove_me_later')
        system_map = firmware.srcodec.system_map
        funccalls = []
        for symbol, v in system_map.items():
            ep = None
            if symbol.startswith('__initcall') and \
                    symbol.find('start') == -1 and \
                    symbol.find('end') == -1:
                # __initcall_ath79_setup3
                ep = symbol[11:]
                if ep[-1] in ['0', '1', '2', '3', '4', '5', '6', '7']:
                    ep = ep[:-1]
                if ep[-2:] in ['1s', '2s', '3s', '4s', '5s', '6s', '7s']:
                    ep = ep[:-2]
                # populate_rootfsrootfs
                if ep.endswith('rootfs'):
                    ep = ep[:-6]
                # spawn_ksoftirqdearly
                if ep.endswith('early'):
                    ep = ep[:-5]
                path_to_entry_point = firmware.srcodec.symbol2file(ep)
                if path_to_entry_point is None:
                    path_to_entry_point = firmware.srcodec.symbol2fileg(ep)
                if path_to_entry_point is None:
                    self.warning(firmware, '{} -> {}(no address)'.format('do_initcall', ep), 1)
                    continue
                if path_to_entry_point.endswith('.h'):
                    path_to_entry_point = firmware.srcodec.symbol2fileg(ep)
                    if path_to_entry_point is None:
                        self.warning(firmware, '{} -> {}(inline in header)'.format('do_initcall', ep, path_to_entry_point), 1)
                        continue
                if not path_to_entry_point.startswith('arch'):
                    continue
                funccalls.append(ep)

        funccalls = self.parse_funcalls(firmware, 'do_initcall', funccalls)
        self.traverse_funccalls(firmware, funccalls, caller='do_initcall')
        exit(1)

        # because symbols/addr2line sometimes don't work well, so we manullay set the value
        if firmware.uuid == 'ar71xx_generic':
            # [checked] ath79_setup(arch/mips/ath79/setup.c)
            # [][checked] ath79_gpio_init(arch/mips/include/asm/mach-ath79/ath79.h)
            path_to_entry_point = 'arch/mips/ath79/gpio.c'
            cmdline = firmware.srcodec.get_cmdline(path_to_entry_point)
            path_to_pentry_point = firmware.srcodec.preprocess(path_to_entry_point, cmdline=cmdline)
            funccalls = firmware.srcodec.get_funccalls(path_to_pentry_point, 'ath79_gpio_init', mode='sparse')
            self.info(firmware, '{} -> {}'.format('ath79_gpio_init', funccalls), 1)
            funccalls.append('__ioremap') # __ioremap is missing
            funccalls = self.parse_funcalls(firmware, 'ath79_gpio_init', funccalls)
            self.traverse_funccalls(firmware, funccalls, caller='ath79_gpio_init')
            # [][checked] ath79_register_uart(arch/mips/ath79/dev-common.c)
            # [][checked] ath79_register_wdt(arch/mips/ath79/dev-common.c)
            # [][checked] mips_machine_setup(arch/mips/kernel/mips_machine.c)
            # [][][checked] bhu_bxu2000n2_a1_setup(arch/mips/ath79/mach-bhu-bxu2000n2-a.c)
            # [][][][checked] bhu_ap123_setup
            # vmlinux has no symbol of bhu_ap123_setup, unbelievable!
            path_to_entry_point = 'arch/mips/ath79/mach-bhu-bxu2000n2-a.c'
            cmdline = firmware.srcodec.get_cmdline(path_to_entry_point)
            path_to_pentry_point = firmware.srcodec.preprocess(path_to_entry_point, cmdline=cmdline)
            entry_point = [
                'ath79_register_m25p80', 'ath79_register_mdio', 'ath79_init_mac',
                'ath79_register_eth', 'ath79_register_wmac']
            funccalls = firmware.srcodec.get_funccalls(path_to_pentry_point, 'bhu_ap123_setup', mode='sparse')
            self.info(firmware, '{} -> {}'.format('bhu_ap123_setup', funccalls), 1)
            funccalls = self.parse_funcalls(firmware, 'bhu_ap123_setup', entry_point)
            self.traverse_funccalls(firmware, funccalls, caller='bhu_ap123_setup')
            # [][][][][checked] ath79_register_m25p80(arch/mips/ath79/dev-m25p80.c)
            # [][][][][][checked] ath79_register_spi(arch/mips/ath79/dev-spi.c)
            # [][][][][][][DIRECT] spi_register_board_info(info, n);
            # [][][][][][][DIRECT] platform_device_register(&ath79_spi_device);
            # [][][][][][done]
            # [][][][]done]
            # [][][][][checked] ath79_register_mdio(arch/mips/ath79/dev-eth.c)
            # [][][][][][checked] ath79_set_pll(no address)
            path_to_entry_point = 'arch/mips/ath79/dev-eth.c'
            cmdline = firmware.srcodec.get_cmdline(path_to_entry_point)
            path_to_pentry_point = firmware.srcodec.preprocess(path_to_entry_point, cmdline=cmdline)
            funccalls = firmware.srcodec.get_funccalls(path_to_pentry_point, 'ath79_set_pll', mode='sparse')
            self.info(firmware, '{} -> {}'.format('ath79_set_pll', funccalls), 1)
            funccalls = self.parse_funcalls(firmware, 'ath79_set_pll', funccalls)
            self.traverse_funccalls(firmware, funccalls, caller='ath79_set_pll')
            # [][][][][][unchecked] ar934x_get_mdio_ref_clock(no address)
            # [][][][][][DIRECT] platform_device_register(mdio_dev);
            # [][][][][done]
            # [][][][][checked] ath79_init_mac(arch/mips/ath79/dev-eth.c)
            # [][][][][checked] ath79_register_eth(arch/mips/ath79/dev-eth.c)
            # [][][][][][unchecked] ath79_init_eth_pll_data(no address)
            # [][][][][][checked] ath79_setup_phy_if_mode(no address)
            path_to_entry_point = 'arch/mips/ath79/dev-eth.c'
            cmdline = firmware.srcodec.get_cmdline(path_to_entry_point)
            path_to_pentry_point = firmware.srcodec.preprocess(path_to_entry_point, cmdline=cmdline)
            funccalls = firmware.srcodec.get_funccalls(path_to_pentry_point, 'ath79_setup_phy_if_mode', mode='sparse')
            self.info(firmware, '{} -> {}'.format('ath79_setup_phy_if_mode', funccalls), 1)
            funccalls = self.parse_funcalls(firmware, 'ath79_setup_phy_if_mode', funccalls)
            self.traverse_funccalls(firmware, funccalls, caller='ath79_setup_phy_if_mode')
            # [][][][][][][checked] ath79_mii_ctrl_set_if(no address)
            path_to_entry_point = 'arch/mips/ath79/dev-eth.c'
            cmdline = firmware.srcodec.get_cmdline(path_to_entry_point)
            path_to_pentry_point = firmware.srcodec.preprocess(path_to_entry_point, cmdline=cmdline)
            funccalls = firmware.srcodec.get_funccalls(path_to_pentry_point, 'ath79_mii_ctrl_set_if', mode='sparse')
            self.info(firmware, '{} -> {}'.format('ath79_mii_ctrl_set_if', funccalls), 1)
            funccalls = self.parse_funcalls(firmware, 'ath79_mii_ctrl_set_if', funccalls)
            self.traverse_funccalls(firmware, funccalls, caller='ath79_mii_ctrl_set_if')
            # [][][][][][checked] get_random_bytes(drivers/char/random.c)
            # [][][][][][unchecked] ath79_device_reset_set(inline in header)
            # [][][][][][unchecked] ath79_device_reset_clear(inline in header)
            # [][][][][][DIRECT] platform_device_register(pdev)
            # [][][][][done]
            # [][][][][checked] ath79_register_wmac(arch/mips/include/asm/mach-ath79/ath79.h)
            # inline function in header but addr2line is wrong
            path_to_entry_point = 'arch/mips/ath79/dev-wmac.c'
            cmdline = firmware.srcodec.get_cmdline(path_to_entry_point)
            path_to_pentry_point = firmware.srcodec.preprocess(path_to_entry_point, cmdline=cmdline)
            funccalls = firmware.srcodec.get_funccalls(path_to_pentry_point, 'ath79_register_wmac', mode='sparse')
            self.info(firmware, '{} -> {}'.format('ath79_register_wmac', funccalls), 1)
            funccalls = self.parse_funcalls(firmware, 'ath79_register_wmac', funccalls)
            self.traverse_funccalls(firmware, funccalls, caller='ath79_register_wmac')
            # [][][][][][DIRECT] platform_device_register(&ath79_wmac_device);
            # [][][][][done]
            # [][][][done]
            # [][][][checked] ath79_register_leds_gpio(arch/mips/ath79/dev-leds-gpio.c)
            # [][][][checked] ath79_register_gpio_keys_polled(arch/mips/ath79/dev-gpio-buttons.c)
            # [][][done]
            # [][done]
            # [done]

        if firmware.uuid == 'bcm47xx':
            # [skip] arch/mips/bcm47xx/buttons.c
            # bcm47xx_buttons_gpio_keys.dev is dependent on the value
            # of bcm47xx_board_get with no mem/irq resouces
            path_to_entry_point = 'arch/mips/bcm47xx/buttons.c'
            cmdline = firmware.srcodec.get_cmdline(path_to_entry_point)
            path_to_pentry_point = firmware.srcodec.preprocess(path_to_entry_point, cmdline=cmdline)
            # [skip] arch/mips/bcm47xx/serial.c
            # this board is using ssb rather than bcma
            # whichever bus the bcm47xx use, its uart is configured by nvram
            # we have to seek a symbolic excution engine for a help
            # or a tool which can resolve the values of the nvram by code snippets
            path_to_entry_point = 'arch/mips/bcm47xx/serial.c'
            cmdline = firmware.srcodec.get_cmdline(path_to_entry_point)
            path_to_pentry_point = firmware.srcodec.preprocess(path_to_entry_point, cmdline=cmdline)
            # [skip] arch/mips/bcm47xx/setup.c
            path_to_entry_point = 'arch/mips/bcm47xx/setup.c'
            cmdline = firmware.srcodec.get_cmdline(path_to_entry_point)
            path_to_pentry_point = firmware.srcodec.preprocess(path_to_entry_point, cmdline=cmdline)
            # gpio_wdt_device.dev is dependent on the value
            # of bcm47xx_board_get with no mem/irq resouces
        elif firmware.uuid == 'ar71xx_generic':
            pass

        firmware.update_bamboo_devices()
        return True

    def __init__(self, analysis_manager):
        super().__init__(analysis_manager)
        self.name = 'excflow'
        self.description = 'source code info analysis (sparse)'
        self.required = ['mfilter', 'device_tree']
        self.context['hint'] = ''
        self.critical = False
        #
        self.globals = []

