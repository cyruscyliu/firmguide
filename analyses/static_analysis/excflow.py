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

        if not path_to_entry_point.startswith('arch'):
            self.debug(firmware, '{} -> {}(built-in function in {})'.format(caller, ep, path_to_entry_point), 1)
            return None, path_to_entry_point, [], {}

        dirs = path_to_entry_point.split('/')
        if dirs[2] == 'include':
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
        for g, ops in gs.items():
            if 'store' in ops:
                self.debug(firmware, '{} -> {}(global defined)'.format(caller, g), 1)

    def parse_funcalls(self, firmware, caller, funccalls):
        funccalls = list(set(funccalls))

        # remove functions we donot want to analyze
        for da in UNMODELED_SKIP_LIST:
            if da in funccalls:
                self.debug(firmware, '{} -> {}(built-in function)'.format(caller, da), 1)
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

        # [FUNCTION] int platform_device_register(struct platform_device *);
        # [STRUCT] platform_devcie, resource, plat_serial8250_port
        if 'platform_device_register' in funccalls:
            funccalls.remove('platform_device_register')
            if firmware.uuid == 'ar71xx_generic':
                if caller == 'ath79_register_uart':
                    # ath79_setup -> ath79_register_uart(arch/mips/ath79/dev-common.c)
                    # [CONDITIONAL] platform_device_register(&ath79_uart_device);
                    # static struct resource ath79_uart_resources[] = {
                    #   {
                    #     .start = (0x18000000 + 0x00020000),
                    #     .end = (0x18000000 + 0x00020000) + 0x100 - 1,
                    #     .flags = 0x00000200,
                    #   },
                    # };
                    # static struct plat_serial8250_port ath79_uart_data[] = {
                    #   {
                    #     .mapbase = (0x18000000 + 0x00020000),
                    #     .irq = (8 + (3)),
                    #     .flags = ((( upf_t ) (1 << 28)) | (( upf_t ) (1 << 6)) | (( upf_t ) (1 << 31))),
                    #     .iotype = (3),
                    #     .regshift = 2,
                    #   }, {
                    #   }
                    # };
                    # static struct platform_device ath79_uart_device = {
                    #   .name = "serial8250",
                    #   .id = PLAT8250_DEV_PLATFORM,
                    #   .resource = ath79_uart_resources,
                    #   .num_resources = ...,
                    #   .dev = { .platform_data = ath79_uart_data },
                    # };
                    uart_name = 'serial8250'
                    uart_mmio_base = eval('(0x18000000 + 0x00020000)')
                    uart_mmio_size = eval('(0x18000000 + 0x00020000) + 0x100 - 1') + 1 - uart_mmio_base
                    # uart_irqn = eval('(8 + (3))')
                    uart_irqn = 6
                    uart_reg_shift = eval('2')
                    firmware.set_uart('0', uart_name, uart_mmio_base, uart_irqn, uart_reg_shift, uart_mmio_size)
                    self.info(firmware, 'get uart name {}'.format(uart_name), 1)
                    self.info(firmware, 'get uart mmio base {} size {}'.format(hex(uart_mmio_base), hex(uart_mmio_size)), 1)
                    self.info(firmware, 'get uart irq {}'.format(uart_irqn), 1)
                    self.info(firmware, 'get uart reg shift {}'.format(uart_reg_shift), 1)
                    # [CONDITIONAL] platform_device_register(&ar933x_uart_device);
                    # static struct resource ar933x_uart_resources[] = {
                    #   {
                    #     .start = (0x18000000 + 0x00020000),
                    #     .end = (0x18000000 + 0x00020000) + 0x100 - 1,
                    #     .flags = 0x00000200,
                    #   }, {
                    #     .start = (8 + (3)),
                    #     .end = (8 + (3)),
                    #     .flags = 0x00000400,
                    #   },
                    # };
                    # static struct platform_device ar933x_uart_device = {
                    #   .name = "ar933x-uart",
                    #   .id = -1,
                    #   .resource = ar933x_uart_resources,
                    #   .num_resources = .
                    # };
                    # cannot support ar933x-uart, but the start address of the ar933x-uart is equal to the serial8250
                    # either is ok, the conditions are ignored
                elif caller == 'ath79_register_eth':
                    # [DIRECT] platform_device_register(pdev)
                    # [CONDITIONAL] pdev = &ath79_eth0_device # 1st
                    # [CONDITIONAL] pdev = &ath79_eth1_device # 2nd
                    #  static struct resource ath79_eth0_resources[] = {
                    #   {
                    #     .name = "mac_base",
                    #     .flags = 0x00000200,
                    #     .start = 0x19000000,
                    #     .end = 0x19000000 + 0x200 - 1,
                    #   }, {
                    #     .name = "mac_irq",
                    #     .flags = 0x00000400,
                    #     .start = (0 + (4)),
                    #     .end = (0 + (4)),
                    #  },
                    # };
                    # struct ag71xx_platform_data ath79_eth0_data = {
                    #   .reset_bit = (1UL << (9)),
                    # };
                    # struct platform_device ath79_eth0_device = {
                    #   .name = "ag71xx",
                    #   .id = 0,
                    #   .resource = ath79_eth0_resources,
                    #   .num_resources = ...
                    #   .dev = { .platform_data = &ath79_eth0_data, },
                    # };
                    mmio_name = 'ag71xx' # duplicated
                    mmio_base = 0x19000000
                    mmio_size = 0x200
                    firmware.insert_bamboo_devices(mmio_base, mmio_size, value=0)
                    self.info(firmware, 'get mmio base {} size {}'.format(hex(mmio_base), hex(mmio_size)), 1)
                    # static struct resource ath79_eth1_resources[] = {
                    #   {
                    #     .name = "mac_base",
                    #     .flags = 0x00000200,
                    #     .start = 0x1a000000,
                    #     .end = 0x1a000000 + 0x200 - 1,
                    #   }, {
                    #     .name = "mac_irq",
                    #     .flags = 0x00000400,
                    #     .start = (0 + (5)),
                    #     .end = (0 + (5)),
                    #   },
                    # };
                    # struct ag71xx_platform_data ath79_eth1_data = {
                    #   .reset_bit = (1UL << (13)),
                    # };
                    # struct platform_device ath79_eth1_device = {
                    #   .name = "ag71xx",
                    #   .id = 1,
                    #   .resource = ath79_eth1_resources,
                    #   .num_resources =  ...
                    #   .dev = { .platform_data = &ath79_eth1_data, },
                    # };
                    mmio_name = 'ag71xx' # duplicated
                    mmio_base = 0x1a000000
                    mmio_size = 0x200
                    firmware.insert_bamboo_devices(mmio_base, mmio_size, value=0)
                    self.info(firmware, 'get mmio base {} size {}'.format(hex(mmio_base), hex(mmio_size)), 1)
                elif caller ==  'ath79_register_mdio':
                    # [DIRECT] platform_device_register(mdio_dev);
                    # [CONDITIONAL] mdio_dev = &ath79_mdio1_device; # 2nd
                    # [CONDITIONAL] mdio_dev = &ath79_mdio0_device; # 1st
                    # [CONDITIONAL] mdio_dev = &ath79_mdio1_device; # duplicated
                    # [CONDITIONAL] mdio_dev = &ath79_mdio0_device; # duplicated
                    # static struct resource ath79_mdio1_resources[] = {
                    #   {
                    #     .name = "mdio_base",
                    #     .flags = 0x00000200,
                    #     .start = 0x1a000000,
                    #     .end = 0x1a000000 + 0x200 - 1,
                    #   }
                    # };
                    # struct ag71xx_mdio_platform_data ath79_mdio1_data;
                    # struct platform_device ath79_mdio1_device = {
                    #   .name = "ag71xx-mdio",
                    #   .id = 1,
                    #   .resource = ath79_mdio1_resources,
                    #   .num_resources = ...,
                    #   .dev = { .platform_data = &ath79_mdio1_data, },
                    # };
                    mmio_name = 'ag71xx-mdio'
                    mmio_base = 0x1a000000
                    mmio_size = 0x200
                    firmware.insert_bamboo_devices(mmio_base, mmio_size, value=0)
                    self.info(firmware, 'get mmio base {} size {}'.format(hex(mmio_base), hex(mmio_size)), 1)
                    # static struct resource ath79_mdio0_resources[] = {
                    #   {
                    #     .name = "mdio_base",
                    #     .flags = 0x00000200,
                    #     .start = 0x19000000,
                    #     .end = 0x19000000 + 0x200 - 1,
                    #   }
                    # };
                    # struct ag71xx_mdio_platform_data ath79_mdio0_data;
                    # struct platform_device ath79_mdio0_device = {
                    #   .name = "ag71xx-mdio",
                    #   .id = 0,
                    #   .resource = ath79_mdio0_resources,
                    #   .num_resources = ...,
                    #   .dev = { .platform_data = &ath79_mdio0_data, },
                    # }
                    mmio_name = 'ag71xx-mdio'
                    mmio_base = 0x19000000
                    mmio_size = 0x200
                    firmware.insert_bamboo_devices(mmio_base, mmio_size, value=0)
                    self.info(firmware, 'get mmio base {} size {}'.format(hex(mmio_base), hex(mmio_size)), 1)
                elif caller == 'ath79_register_spi':
                    # [DIRECT] platform_device_register(&ath79_spi_device);
                    # static struct resource ath79_spi_resources[] = {
                    #   {
                    #     .start = 0x1f000000,
                    #     .end = 0x1f000000 + 0x01000000 - 1,
                    #     .flags = 0x00000200,
                    #   },
                    # };
                    # static struct platform_device ath79_spi_device = {
                    #   .name = "ath79-spi",
                    #   .id = -1,
                    #   .resource = ath79_spi_resources,
                    #   .num_resources = ...
                    # };
                    flash_base = eval('0x1f000000')
                    flash_size = 0x01000000
                    self.info(firmware, 'get flash base {} size {}'.format(hex(flash_base), hex(flash_size)), 1)
                    firmware.insert_bamboo_devices(flash_base, flash_size, value=0)
                elif caller == 'ath79_register_wmac':
                    # static struct ath9k_platform_data ath79_wmac_data = {
                    #   .led_pin = -1,
                    # };
                    # static struct resource ath79_wmac_resources[] = {
                    #   {
                    #     .flags = 0x00000200,
                    #   }, {
                    #     .flags = 0x00000400,
                    #   },
                    # };
                    # static struct platform_device ath79_wmac_device = {
                    #   .name = "ath9k",
                    #   .id = -1,
                    #   .resource = ath79_wmac_resources,
                    #   .num_resources =
                    #   .dev = { .platform_data = &ath79_wmac_data, },
                    # };
                    mmio_name = 'ath9k'
                    # [CONDITIONAL] ar913x_wmac_setup
                    # ath79_wmac_resources[0].start = (0x18000000 + 0x000C0000);
                    # ath79_wmac_resources[0].end = (0x18000000 + 0x000C0000) + 0x30000 - 1;
                    # ath79_wmac_resources[1].start = (0 + (2));
                    # ath79_wmac_resources[1].end = (0 + (2));
                    mmio_base = eval('(0x18000000 + 0x000C0000)')
                    mmio_size = 0x30000
                    firmware.insert_bamboo_devices(mmio_base, mmio_size, value=0)
                    self.info(firmware, 'get mmio base {} size {}'.format(hex(mmio_base), hex(mmio_size)), 1)
                    # [CONDITIONAL] ar933x_wmac
                    # ath79_wmac_device.name = "ar933x_wmac";
                    # ath79_wmac_resources[0].start = (0x18000000 + 0x00100000);
                    # ath79_wmac_resources[0].end = (0x18000000 + 0x00100000) + 0x20000 - 1;
                    # ath79_wmac_resources[1].start = (0 + (2));
                    # ath79_wmac_resources[1].end = (0 + (2));
                    mmio_name = 'ar933x_wmac'
                    mmio_base = eval('(0x18000000 + 0x00100000)')
                    mmio_size = 0x20000
                    firmware.insert_bamboo_devices(mmio_base, mmio_size, value=0)
                    self.info(firmware, 'get mmio base {} size {}'.format(hex(mmio_base), hex(mmio_size)), 1)
                    # [CONDITIONAL] ar934x_wmac_setup
                    # ath79_wmac_device.name = "ar934x_wmac"; # duplicated
                    # ath79_wmac_resources[0].start = (0x18000000 + 0x00100000);
                    # ath79_wmac_resources[0].end = (0x18000000 + 0x00100000) + 0x20000 - 1;
                    # ath79_wmac_resources[1].start = (((8 + 32) + 6) + (1));
                    # ath79_wmac_resources[1].end = (((8 + 32) + 6) + (1));
                    mmio_name = 'ar934x_wmac'
                    mmio_base = eval('(0x18000000 + 0x00100000)')
                    mmio_size = 0x20000
                    firmware.insert_bamboo_devices(mmio_base, mmio_size, value=0)
                    self.info(firmware, 'get mmio base {} size {}'.format(hex(mmio_base), hex(mmio_size)), 1)
                    # [CONDITIONAL] qca953x_wmac_setup
                    # ath79_wmac_device.name = "qca953x_wmac";
                    # ath79_wmac_resources[0].start = (0x18000000 + 0x00100000);
                    # ath79_wmac_resources[0].end = (0x18000000 + 0x00100000) + 0x20000 - 1;
                    # ath79_wmac_resources[1].start = (0 + (2));
                    # ath79_wmac_resources[1].end = (0 + (2));
                    mmio_name = 'qca953x_wmac' #duplicated, share the same mmio space but have different functionality
                    mmio_base = eval('(0x18000000 + 0x00100000)')
                    mmio_size = 0x20000
                    firmware.insert_bamboo_devices(mmio_base, mmio_size, value=0)
                    self.info(firmware, 'get mmio base {} size {}'.format(hex(mmio_base), hex(mmio_size)), 1)
                    # [CONDITIONAL] qca955x_wmac_setup
                    # ath79_wmac_device.name = "qca953x_wmac";
                    # ath79_wmac_resources[0].start = (0x18000000 + 0x00100000);
                    # ath79_wmac_resources[0].end = (0x18000000 + 0x00100000) + 0x20000 - 1;
                    # ath79_wmac_resources[1].start = (0 + (2));
                    # ath79_wmac_resources[1].end = (0 + (2));
                    mmio_name = 'qca955x_wmac' #duplicated
                    mmio_base = eval('(0x18000000 + 0x00100000)')
                    mmio_size = 0x20000
                    firmware.insert_bamboo_devices(mmio_base, mmio_size, value=0)
                    self.info(firmware, 'get mmio base {} size {}'.format(hex(mmio_base), hex(mmio_size)), 1)
                    # [CONDITIONAL] qca956x_wmac_setup
                    # ath79_wmac_device.name = "qca956x_wmac";
                    # ath79_wmac_resources[0].start = (0x18000000 + 0x00100000);
                    # ath79_wmac_resources[0].end = (0x18000000 + 0x00100000) + 0x20000 - 1;
                    # ath79_wmac_resources[1].start = (((8 + 32) + 6) + (1));
                    # ath79_wmac_resources[1].end = (((8 + 32) + 6) + (1));
                    mmio_name = 'qca956x_wmac' #duplicated
                    mmio_base = eval('(0x18000000 + 0x00100000)')
                    mmio_size = 0x20000
                    firmware.insert_bamboo_devices(mmio_base, mmio_size, value=0)
                    self.info(firmware, 'get mmio base {} size {}'.format(hex(mmio_base), hex(mmio_size)), 1)
                else:
                    self.warning(firmware, 'platform_device_register found but no handlers', 0)
            else:
                self.warning(firmware, 'platform_device_register found but no handlers', 0)

        # [FUNCTION] platform_device_register_full
        if 'platform_device_register_full' in funccalls:
            funccalls.remove('platform_device_register_full')
            if firmware.uuid == 'ar71xx_generic':
                if caller == 'ath79_register_wdt':
                    # ath79_setup -> ath79_register_wdt(arch/mips/ath79/dev-common.c)
                    # [DIRECT] platform_device_register_simple("ath79-wdt", -1, &res, 1);
                    # res.flags = 0x00000200;
                    # res.start = (0x18000000 + 0x00060000) + 0x08;
                    # res.end = res.start + 0x8 - 1;
                    mmio_name = 'ar933x-uart'
                    mmio_base = eval('(0x18000000 + 0x00060000) + 0x08')
                    mmio_size = eval('(0x18000000 + 0x00060000) + 0x08 + 0x8 - 1') + 1 - mmio_base
                    firmware.insert_bamboo_devices(mmio_base, mmio_size, value=0)
                    self.info(firmware, 'get mmio base {} size {}'.format(hex(mmio_base), hex(mmio_size)), 1)
                else:
                    self.warning(firmware, 'platform_device_register_full found but no handlers', 0)
            else:
                self.warning(firmware, 'platform_device_register_full found but no handlers', 0)

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

        # [FUNCIIONS] platform_device_alloc, platform_device_add_data, platform_device_add(pdev);
        if 'platform_device_alloc' in funccalls:
            funccalls.remove('platform_device_alloc')
            if 'platform_device_add_data' in funccalls:
                funccalls.remove('platform_device_add_data')
            if 'platform_device_add' in funccalls:
                funccalls.remove('platform_device_add')
            if 'platform_device_put' in funccalls:
                funccalls.remove('platform_device_put')
            if firmware.uuid == 'ar71xx_generic':
                if caller == 'ath79_register_leds_gpio':
                    # bhu_bxu2000n2_a1_setup -> ath79_register_leds_gpio(arch/mips/ath79/dev-leds-gpio.c)
                    # [DIRECT] no resouces found
                    # pdev = platform_device_alloc("leds-gpio", id);
                    # err = platform_device_add_data(pdev, &pdata, sizeof(pdata));
                    # err = platform_device_add(pdev);
                    pass
                elif caller == 'ath79_register_gpio_keys_polled':
                    # bhu_bxu2000n2_a1_setup -> ath79_register_gpio_keys_polled(arch/mips/ath79/dev-gpio-buttons.c)
                    # [DIRECT] no reources found
                    # pdev = platform_device_alloc("gpio-keys-polled", id);
                    # err = platform_device_add_data(pdev, &pdata, sizeof(pdata));
                    # err = platform_device_add(pdev);
                    pass
                else:
                    self.warning(firmware, 'platform_device_register_full found but no handlers', 0)
            else:
                self.warning(firmware, 'platform_device_register_full found but no handlers', 0)

        # [FUNCTION] __iounmap() -> ()__ioremap_mode() -> ()__ioremap()
        if '__iounmap' in funccalls:
            funccalls.remove('__iounmap')
            if firmware.uuid == 'ar71xx_generic':
                if caller == 'ath79_mii_ctrl_set_if':
                    # ath79_mii_ctrl_set_if(no address)
                    # [DIRECT] base = __ioremap_mode(((0x18000000 + 0x00070000)), (0x100), ...)
                    mmio_name = 'reserved0'
                    mmio_base = eval('(0x18000000 + 0x00070000)')
                    mmio_size = 0x100
                    firmware.insert_bamboo_devices(mmio_base, mmio_size, value=0)
                    self.info(firmware, 'get mmio base {} size {}'.format(hex(mmio_base), hex(mmio_size)), 1)
                elif caller == 'ath79_set_pll':
                    # ath79_set_pll(no address)
                    # [DIRECT] base = __ioremap_mode(((0x18000000 + 0x00050000)), (0x100), ...)
                    mmio_name = 'reserved1'
                    mmio_base = eval('(0x18000000 + 0x00050000)')
                    mmio_size = 0x100
                    firmware.insert_bamboo_devices(mmio_base, mmio_size, value=0)
                    self.info(firmware, 'get mmio base {} size {}'.format(hex(mmio_base), hex(mmio_size)), 1)
                else:
                    self.warning(firmware, '__ioremap_mode found but no handlers', 0)
            else:
                self.warning(firmware, '__ioremap_mode found but no handlers', 0)

        # [FUNCTION] spi_register_board_info && flash_platform_data
        if 'spi_register_board_info' in funccalls:
            funccalls.remove('spi_register_board_info')
            if firmware.uuid == 'ar71xx_generic':
                if caller == 'ath79_register_spi':
                    # static struct ath79_spi_controller_data ath79_spi0_cdata =
                    # { .cs_type = ATH79_SPI_CS_TYPE_INTERNAL, .cs_line = 0, };
                    # static struct ath79_spi_controller_data ath79_spi1_cdata =
                    # { .cs_type = ATH79_SPI_CS_TYPE_INTERNAL, .cs_line = 1, };
                    # static struct spi_board_info ath79_spi_info[] = {
                    #   {
                    #     .bus_num    = 0,
                    #     .chip_select    = 0,
                    #     .max_speed_hz   = 25000000,
                    #     .modalias   = "m25p80",
                    #     .controller_data = &ath79_spi0_cdata,
                    #   },{
                    #     .bus_num    = 0,
                    #     .chip_select    = 1,
                    #     .max_speed_hz   = 25000000,
                    #     .modalias   = "m25p80",
                    #     .controller_data = &ath79_spi1_cdata,
                    #   }
                    # };
                    # ath79_spi0_cdata.is_flash = true;
                    # ath79_spi_info[0].platform_data = pdata;
                    # spi_register_board_info(ath79_spi_info, 1);
                    # flash:
                    #  num:
                    #   flash@1:
                    #     type = 'nor'
                    #     interface = 'spi'
                    #     name = 'm25p80'
                    flash_type = 'nor'
                    flash_interface = 'spi'
                    flash_name = 'm25p80'
                    # flash is not going to be set any more
                    # firmware.set_flash('0', flash_name, flash_type, flash_interface, flash_base, flash_size)
                    self.info(firmware, 'get {} {} flash {}'.format(flash_interface, flash_type, flash_name), 1)
                else:
                    self.warning(firmware, 'spi_register_board_info found but no handlers', 0)
            else:
                self.warning(firmware, 'spi_register_board_info found but no handlers', 0)

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

        # ==== setup ====
        ep = 'setup_arch'
        # mips
        #   setup_arch->cpu_probe
        #   setup_arch->prom_init
        #   setup_arch->setup_early_printk -> FP -> prom_putchar
        #       note: ingore FP here, because uarts will be determined in do_initcalls
        #   setup_arch->arch_mem_init->plat_mem_setup
        self.traverse_funccalls(firmware, [ep], caller='start_kernel')
        if firmware.uuid == 'ar71xx_generic':
            # __ioremap_mode will be ignored
            # ath79_reset_base = __ioremap_mode(((0x18000000 + 0x00060000)), (0x100), ...);
            mmio_name = 'ath79_reset'; mmio_base = eval('((0x18000000 + 0x00060000))'); mmio_size = 0x100
            firmware.insert_bamboo_devices(mmio_base, mmio_size, value=0)
            self.info(firmware, 'get mmio base {} size {}'.format(hex(mmio_base), hex(mmio_size)), 1)
            ## =========== from stinc.py =============
            firmware.insert_bamboo_devices(0x18060010, 0x4, value=0x10000000)
            firmware.insert_bamboo_devices(0x18060014, 0x4, value=0x10000000)
            ## =======================================
            # ath79_pll_base = __ioremap_mode(((0x18000000 + 0x00050000)), (0x100), ...);
            mmio_name = 'ath79_pll'; mmio_base = eval('((0x18000000 + 0x00050000))'); mmio_size = 0x100
            firmware.insert_bamboo_devices(mmio_base, mmio_size, value=0)
            self.info(firmware, 'get mmio base {} size {}'.format(hex(mmio_base), hex(mmio_size)), 1)
            ## =========== from stimer.py ==============
            firmware.insert_bamboo_devices(0x18050000, 0x4, value=0x10)
            ## =========================================
            # ath79_ddr_base = __ioremap_mode(((0x18000000 + 0x00000000)), (0x100), ...);
            mmio_name = 'ath79_ddr'; mmio_base = eval('((0x18000000 + 0x00000000))'); mmio_size = 0x100
            firmware.insert_bamboo_devices(mmio_base, mmio_size, value=0)
            self.info(firmware, 'get mmio base {} size {}'.format(hex(mmio_base), hex(mmio_size)), 1)

        # ===== intc subsystem =====
        # 1 intc initilization
        ep = 'init_IRQ'
        self.traverse_funccalls(firmware, [ep], caller='start_kernel')
        # ralink_rt3883: arch_init_irq -> [of_irq_init']
        if firmware.uuid == 'ar71xx_generic':
            # arch_init_irq -> ath79_misc_irq_init(no address)
            self.traverse_no_address_funccall(firmware, 'ath79_misc_irq_init', 'arch/mips/ath79/irq.c')
        # 2. do_asm_IRQ/plat_irq_dispatch
        if firmware.get_arch() == 'arm':
            ep = 'do_asm_IRQ'
            self.traverse_funccalls(firmware, [ep], caller='start_kernel')
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
        self.traverse_funccalls(firmware, [ep], caller='start_kernel')

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
                    funccalls.append(ep)

        funccalls = self.parse_funcalls(firmware, 'do_initcall', funccalls)
        self.traverse_funccalls(firmware, funccalls, caller='do_initcall')

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
        self.description = 'source code info analysis (llvm)'
        self.required = ['stimer']
        self.context['hint'] = ''
        self.critical = False

