''')
Source Code Info Analysis.
'''
import os
import re

from analyses.analysis import Analysis
from pycparser import c_parser, c_ast, parse_file


class PlatformDevices(Analysis):
    def traverse_struct(self, firmware, path_to_st):
        # because we cannot use pycparser now, simply we can get the setup function
        # from source code using regular expression
        # MIPS_MACHINE(ATH79_MACH_CARAMBOLA2, "CARAMBOLA2", "8devices Carambola2 board", carambola2_setup);
        string = ''
        with open(os.path.join(firmware.srcodec.srcode, path_to_st)) as f:
            for line in f:
                string += line.strip()
        match = re.search(r'MIPS_MACHINE\(\s*[_A-Z0-9]+\s*,\s*".*?"\s*,\s*".*?"\s*,\s*([_a-zA-Z0-9]+)\s*\)', string)
        setup = match.group(1)
        return setup

    def traverse_func(self, firmware, entry_point, caller='do_initcall'):
        for ep in entry_point:
            address = firmware.srcodec.symbol2address(ep)
            if address is None:
                continue
            path_to_entry_point = firmware.srcodec.addr2file(address)
            if not path_to_entry_point.startswith('arch'):
                continue
            # arch/arm/kernel -> ['arch', 'arm', 'kernel']
            dirs = path_to_entry_point.split('/')
            if dirs[2] in ['mm', 'pci']:
                continue
            self.info(firmware, 'backbone {} -> {}({})'.format(caller, ep, path_to_entry_point), 1)

            cmdline = firmware.srcodec.get_cmdline(path_to_entry_point)
            path_to_pentry_point = firmware.srcodec.preprocess(path_to_entry_point, cmdline=cmdline)
            # firmware.srcodec.fix_gnu_extensions(path_to_pentry_point)
            # funccalls = firmware.srcodec.traverse_func(path_to_pentry_point, entry_point)

    def run(self, firmware):
        """
        here is for platform_devices
        """
        entry_point = [
            'platform_device_register',
        ]
        # do_initcall analysis
        # "early", "core", "postcore", "arch", "subsys", "fs", "device", "late",
        system_map = firmware.srcodec.get_system_map()
        for symbol, v in system_map.items():
            if symbol.startswith('__initcall') and \
                    symbol.find('start') == -1 and \
                    symbol.find('end') == -1:
                # __initcall_ath79_setup3
                ep = symbol[11:]
                if ep[-1] in ['0', '1', '2', '3', '4', '5', '6', '7']:
                    ep = ep[:-1]
                    entry_point.append(ep)
        self.traverse_func(firmware, entry_point)

        # because the parser always doesn't work, so we manullay set the value
        if firmware.uuid == 'ar71xx_generic':
            # [checked] init_ramfs_fs(arch/mips/include/asm/bitops.h)
            # inline function in header but addr2line is wrong
            entry_point = 'fs/ramfs/inode.c' # which is out of our scopejjj
            # [checked] ath79_setup(arch/mips/ath79/setup.c)
            entry_point = ['ath79_gpio_init', 'ath79_register_uart', 'ath79_register_wdt', 'mips_machine_setup']
            self.traverse_func(firmware, entry_point, caller='ath79_setup')
            # [][checked] ath79_gpio_init(arch/mips/include/asm/mach-ath79/ath79.h)
            # inline function in header but addr2line is wrong
            path_to_entry_point = 'arch/mips/ath79/gpio.c'
            cmdline = firmware.srcodec.get_cmdline(path_to_entry_point)
            path_to_pentry_point = firmware.srcodec.preprocess(path_to_entry_point, cmdline=cmdline)
            # [FUNCTION] void __iomem * __ioremap(phys_t offset, phys_t size, unsigned long flags);
            # [DIRECT] ath79_gpio_base = __ioremap_mode(((0x18000000 + 0x00040000)), (0x100), ...)
            mmio_name = 'ath79_gpio'
            mmio_base = eval('((0x18000000 + 0x00040000))')
            mmio_size = eval('(0x100)')
            self.info(firmware, 'get mmio base {} size {}'.format(hex(mmio_base), hex(mmio_size)), 1)
            # [][checked] ath79_register_uart(arch/mips/ath79/dev-common.c)
            # [FUNCTION] int platform_device_register(struct platform_device *);
            # [STRUCT] platform_devcie, resource, plat_serial8250_port
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
            uart_mmio_size = eval('(0x18000000 + 0x00020000) + 0x100 - 1') + 1 - mmio_base
            uart_irq = eval('(8 + (3))')
            uart_reg_shift = eval('2')
            self.info(firmware, 'get uart name {}'.format(uart_name), 1)
            self.info(firmware, 'get uart mmio base {} size {}'.format(hex(uart_mmio_base), hex(uart_mmio_size)), 1)
            self.info(firmware, 'get uart irq {}'.format(uart_irq), 1)
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
            # [][checked] ath79_register_wdt(arch/mips/ath79/dev-common.c)
            # [DIRECT] platform_device_register_simple("ath79-wdt", -1, &res, 1);
            # res.flags = 0x00000200;
            # res.start = (0x18000000 + 0x00060000) + 0x08;
            # res.end = res.start + 0x8 - 1;
            mmio_name = 'ar933x-uart'
            mmio_base = eval('(0x18000000 + 0x00060000) + 0x08')
            mmio_size = eval('(0x18000000 + 0x00060000) + 0x08 + 0x8 - 1') + 1 - mmio_base
            self.info(firmware, 'get mmio base {} size {}'.format(hex(mmio_base), hex(mmio_size)), 1)
            # [][checked] mips_machine_setup(arch/mips/kernel/mips_machine.c)
            # [FUNCTION] void mips_machine_setup(void);
            # this function decides which machine->setup to be called according to a kernel boot args
            # according to arch/mips/include/asm/mips_machine.h, we have
            for symbol, v in system_map.items():
                # machine_id_##_type
                if symbol.startswith('machine_id'):
                    # addr2line not work for data
                    machine_type = symbol[11:]
                    output = os.popen('grep -nir "MIPS_MACHINE({}" {}/arch/{}'.format(
                        machine_type, firmware.srcodec.srcode, firmware.get_architecture())).readlines()
                    assert len(output), 'where is the symbol {}'.format(machine_type)
                    output = output[0].split(':')[0][len(firmware.srcodec.srcode)+1:]
                    # self.debug(firmware, 'get machine type {}'.format(machine_type), 1)
                    machine_setup = self.traverse_struct(firmware, output)
                    self.traverse_func(firmware, [machine_setup], caller='mips_machine_setup')
                    # time consuming, skip
                    break
            # [][unchecked] ath79_generic_init(arch/mips/ath79/setup.c)
            # [][checked] alfa_ap96_init(arch/mips/ath79/mach-alfa-ap96.c)
            # [][checked] alfa_nx_setup(arch/mips/ath79/mach-alfa-nx.c)
            # [][checked] all0258n_setup(arch/mips/ath79/mach-all0258n.c)
            # [][checked] all0315n_setup(arch/mips/ath79/mach-all0315n.c)
            # [][checked] antminer_s1_setup(arch/mips/ath79/mach-antminer-s1.c)
            # [][checked] antminer_s3_setup(arch/mips/ath79/mach-antminer-s3.c)
            # [][checked] ap113_setup(arch/mips/ath79/mach-ap113.c)
            # [][checked] ap121_setup(arch/mips/ath79/mach-ap121.c)
            # [][checked] ap121_setup(arch/mips/ath79/mach-ap121.c)
            # [][checked] ap132_setup(arch/mips/ath79/mach-ap132.c)
            # [][checked] ap136_010_setup(arch/mips/ath79/mach-ap136.c)
            # [][checked] ap136_010_setup(arch/mips/ath79/mach-ap136.c)
            # [][checked] ap136_010_setup(arch/mips/ath79/mach-ap136.c)
            # [][checked] ap81_setup(arch/mips/ath79/mach-ap81.c)
            # [][checked] ap83_setup(arch/mips/ath79/mach-ap83.c)
            # [][checked] ap96_setup(arch/mips/ath79/mach-ap96.c)
            # [][checked] archer_c5_setup(arch/mips/ath79/mach-archer-c7.c)
            # [][checked] archer_c5_setup(arch/mips/ath79/mach-archer-c7.c)
            # [][checked] archer_c5_setup(arch/mips/ath79/mach-archer-c7.c)
            # [][checked] aw_nr580_setup(arch/mips/ath79/mach-aw-nr580.c)
            # [][unchecked] bhu_bxu2000n2_a1_setup(arch/mips/ath79/mach-bhu-bxu2000n2-a.c)
            # this setup function will be called r.s.t the tested firmware
            entry_point = ['bhu_ap123_setup', 'ath79_register_leds_gpio', 'ath79_register_gpio_keys_polled']
            self.traverse_func(firmware, entry_point, caller='bhu_bxu2000n2_a1_setup')
            # [][][checked] bhu_ap123_setup
            # vmlinux has no symbol of bhu_ap123_setup, unbelievable!
            entry_point = [ 'ath79_register_m25p80', 'ath79_register_mdio', 'ath79_init_mac', 'ath79_register_eth',
                'ath79_register_wmac']
            self.traverse_func(firmware, entry_point, caller='bhu_ap123_setup')
            # [][][][checked] ath79_register_m25p80(arch/mips/ath79/dev-m25p80.c)
            # ############## flash ################
            self.traverse_func(firmware, ['ath79_register_spi'], caller='ath79_register_m25p80')
            # [][][][][checked] ath79_register_spi(arch/mips/ath79/dev-spi.c)
            # [FUNCTION] spi_register_board_info && flash_platform_data
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
            self.info(firmware, 'get {} {} flash {} base {} size {}'.format(
                flash_interface, flash_type, flash_name, hex(flash_base), hex(flash_size)), 1)
            # [][][][checked] ath79_register_mdio(arch/mips/ath79/dev-eth.c)
            entry_point = ['ath79_set_pll', 'ar934x_get_mdio_ref_clock']
            self.traverse_func(firmware, entry_point, caller='ath79_register_mdio') # which is out of our scope
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
            self.info(firmware, 'get mmio base {} size {}'.format(hex(mmio_base), hex(mmio_size)), 1)
            # [][][][checked] ath79_init_mac(arch/mips/ath79/dev-eth.c)
            # [DIRECT] is_valid_ether_addr(mac) which is out of our scope by its name
            # [][][][checked] ath79_register_eth(arch/mips/ath79/dev-eth.c)
            # [DIRECT] ath79_init_eth_pll_data which is out of our scope by its name
            # [DIRECT] ath79_setup_phy_if_mode which is out of our scope by its name
            # [DIRECT] is_valid_ether_addr which is out of our scope by its name
            # [DIRECT] eth_random_addr which is out of our scope by its name
            # [DIRECT] ath79_device_reset_set which is out of our scope by its name
            # [DIRECT] ath79_device_reset_clear which is out of our scope by its name
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
            self.info(firmware, 'get mmio base {} size {}'.format(hex(mmio_base), hex(mmio_size)), 1)
            # [][][][checked] ath79_register_wmac(arch/mips/include/asm/mach-ath79/ath79.h)
            # inline function in header but addr2line is wrong
            path_to_entry_point = 'arch/mips/ath79/dev-wmac.c'
            cmdline = firmware.srcodec.get_cmdline(path_to_entry_point)
            path_to_pentry_point = firmware.srcodec.preprocess(path_to_entry_point, cmdline=cmdline)
            entry_point = ['ar913x_wmac_setup', 'ar933x_wmac_setup', 'ar934x_wmac_setup', 'qca953x_wmac_setup',
                           'qca955x_wmac_setup', 'qca956x_wmac_setup']
            # resource infomation is in funcations above
            # [DIRECT] platform_device_register(&ath79_wmac_device);
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
            self.info(firmware, 'get mmio base {} size {}'.format(hex(mmio_base), hex(mmio_size)), 1)
            # [][][checked] ath79_register_leds_gpio(arch/mips/ath79/dev-leds-gpio.c)
            # [FUNCIIONS] platform_device_alloc, platform_device_add_data, platform_device_add(pdev);
            # [DIRECT] no resouces found
            # pdev = platform_device_alloc("leds-gpio", id);
            # err = platform_device_add_data(pdev, &pdata, sizeof(pdata));
            # err = platform_device_add(pdev);
            # [][][checked] ath79_register_gpio_keys_polled(arch/mips/ath79/dev-gpio-buttons.c)
            # [DIRECT] no reources found
            # pdev = platform_device_alloc("gpio-keys-polled", id);
            # err = platform_device_add_data(pdev, &pdata, sizeof(pdata));
            # err = platform_device_add(pdev);
            # [][unchecked] bsb_setup(arch/mips/ath79/mach-bsb.c)
            # [][checked] cap4200ag_setup(arch/mips/ath79/mach-cap4200ag.c)
            # [][checked] cpe510_setup(arch/mips/ath79/mach-cpe510.c)
            # [][checked] db120_setup(arch/mips/ath79/mach-db120.c)
            # [][checked] dlan_pro_500_wp_setup(arch/mips/ath79/mach-dlan-pro-500-wp.c)
            # [][checked] dlan_pro_1200_ac_setup(arch/mips/ath79/mach-dlan-pro-1200-ac.c)
            # [][checked] dgl_5500_a1_setup(arch/mips/ath79/mach-dgl-5500-a1.c)
            # [][checked] dhp1565a1_setup(arch/mips/ath79/mach-dhp-1565-a1.c)
            # [][checked] dir_505_a1_setup(arch/mips/ath79/mach-dir-505-a1.c)
            # [][checked] dir_600_a1_setup(arch/mips/ath79/mach-dir-600-a1.c)
            # [][checked] dir_600_a1_setup(arch/mips/ath79/mach-dir-600-a1.c)
            # [][checked] dir_600_a1_setup(arch/mips/ath79/mach-dir-600-a1.c)
            # [][checked] dir_615c1_setup(arch/mips/ath79/mach-dir-615-c1.c)
            # [][checked] dir825b1_setup(arch/mips/ath79/mach-dir-825-b1.c)
            # [][checked] dir825c1_setup(arch/mips/ath79/mach-dir-825-c1.c)
            # [][checked] dir825c1_setup(arch/mips/ath79/mach-dir-825-c1.c)
            # [][checked] dragino2_setup(arch/mips/ath79/mach-dragino2.c)
            # [][checked] esr900_setup(arch/mips/ath79/mach-esr900.c)
            # [][checked] ew_dorin_setup(arch/mips/ath79/mach-ew-dorin.c)
            # [][checked] ew_dorin_setup(arch/mips/ath79/mach-ew-dorin.c)
            # [][checked] eap300v2_setup(arch/mips/ath79/mach-eap300v2.c)
            # [][checked] eap7660d_setup(arch/mips/ath79/mach-eap7660d.c)
            # [][checked] eap7660d_setup(arch/mips/ath79/mach-eap7660d.c)
            # [][checked] el_m150_setup(arch/mips/ath79/mach-el-m150.c)
            # [][checked] el_mini_setup(arch/mips/ath79/mach-el-mini.c)
            # [][checked] epg5000_setup(arch/mips/ath79/mach-epg5000.c)
            # [][checked] esr1750_setup(arch/mips/ath79/mach-esr1750.c)
            # [][checked] f9k1115v2_setup(arch/mips/ath79/mach-f9k1115v2.c)
            # [][checked] gl_inet_setup(arch/mips/ath79/mach-gl-inet.c)
            # [][checked] gs_oolite_setup(arch/mips/ath79/mach-gs-oolite.c)
            # [][checked] hiwifi_hc6361_setup(arch/mips/ath79/mach-hiwifi-hc6361.c)
            # [][checked] ja76pf_init(arch/mips/ath79/mach-ja76pf.c)
            # [][checked] ja76pf_init(arch/mips/ath79/mach-ja76pf.c)
            # [][checked] jwap003_init(arch/mips/ath79/mach-jwap003.c)
            # [][checked] hornet_ub_setup(arch/mips/ath79/mach-hornet-ub.c)
            # [][checked] mac1200r_setup(arch/mips/ath79/mach-mc-mac1200r.c)
            # [][checked] MR12_setup(arch/mips/ath79/mach-mr12.c)
            # [][checked] MR16_setup(arch/mips/ath79/mach-mr16.c)
            # [][checked] mr600_setup(arch/mips/ath79/mach-mr600.c)
            # [][checked] mr600_setup(arch/mips/ath79/mach-mr600.c)
            # [][checked] mr900_setup(arch/mips/ath79/mach-mr900.c)
            # [][checked] mr900_setup(arch/mips/ath79/mach-mr900.c)
            # [][checked] mynet_n600_setup(arch/mips/ath79/mach-mynet-n600.c)
            # [][checked] mynet_n750_setup(arch/mips/ath79/mach-mynet-n750.c)
            # [][checked] mynet_rext_setup(arch/mips/ath79/mach-mynet-rext.c)
            # [][checked] mzk_w04nu_setup(arch/mips/ath79/mach-mzk-w04nu.c)
            # [][checked] mzk_w300nh_setup(arch/mips/ath79/mach-mzk-w300nh.c)
            # [][checked] nbg460n_setup(arch/mips/ath79/mach-nbg460n.c)
            # [][checked] om2p_setup(arch/mips/ath79/mach-om2p.c)
            # [][checked] om2p_setup(arch/mips/ath79/mach-om2p.c)
            # [][checked] om2p_setup(arch/mips/ath79/mach-om2p.c)
            # [][checked] om2p_setup(arch/mips/ath79/mach-om2p.c)
            # [][checked] om2p_setup(arch/mips/ath79/mach-om2p.c)
            # [][checked] om5p_setup(arch/mips/ath79/mach-om5p.c)
            # [][checked] om5p_setup(arch/mips/ath79/mach-om5p.c)
            # [][checked] onion_omega_setup(arch/mips/ath79/mach-onion-omega.c)
            # [][checked] pb42_init(arch/mips/ath79/mach-pb42.c)
            # [][checked] pb44_init(arch/mips/ath79/mach-pb44.c)
            # [][checked] pb92_init(arch/mips/ath79/mach-pb92.c)
            # [][checked] qihoo_c301_setup(arch/mips/ath79/mach-qihoo-c301.c)
            # [][checked] r6100_setup(arch/mips/ath79/mach-r6100.c)
            # [][checked] rw2458n_setup(arch/mips/ath79/mach-rw2458n.c)
            # [][checked] smart_300_setup(arch/mips/ath79/mach-smart-300.c)
            # [][checked] tew_632brp_setup(arch/mips/ath79/mach-tew-632brp.c)
            # [][checked] tew673gru_setup(arch/mips/ath79/mach-tew-673gru.c)
            # [][checked] tew_712br_setup(arch/mips/ath79/mach-tew-712br.c)
            # [][checked] tew_732br_setup(arch/mips/ath79/mach-tew-732br.c)
            # [][checked] tl_mr11u_setup(arch/mips/ath79/mach-tl-mr11u.c)
            # [][checked] tl_mr11u_setup(arch/mips/ath79/mach-tl-mr11u.c)
            # [][checked] tl_mr11u_setup(arch/mips/ath79/mach-tl-mr11u.c)
            # [][checked] tl_mr13u_setup(arch/mips/ath79/mach-tl-mr13u.c)
            # [][checked] tl_mr3020_setup(arch/mips/ath79/mach-tl-mr3020.c)
            # [][checked] tl_mr3220_setup(arch/mips/ath79/mach-tl-mr3x20.c)
            # [][checked] tl_mr3220_setup(arch/mips/ath79/mach-tl-mr3x20.c)
            # [][checked] tl_mr3220_setup(arch/mips/ath79/mach-tl-mr3x20.c)
            # [][checked] tl_wa750re_setup(arch/mips/ath79/mach-tl-wax50re.c)
            # [][checked] tl_wa750re_setup(arch/mips/ath79/mach-tl-wax50re.c)
            # [][checked] tl_wa750re_setup(arch/mips/ath79/mach-tl-wax50re.c)
            # [][checked] tl_wa750re_setup(arch/mips/ath79/mach-tl-wax50re.c)
            # [][checked] tl_wa750re_setup(arch/mips/ath79/mach-tl-wax50re.c)
            # [][checked] tl_wa701ndv2_setup(arch/mips/ath79/mach-tl-wa701nd-v2.c)
            # [][checked] tl_wa7210n_v2_setup(arch/mips/ath79/mach-tl-wa7210n-v2.c)
            # [][checked] tl_wa830re_v2_setup(arch/mips/ath79/mach-tl-wa830re-v2.c)
            # [][checked] tl_wa901nd_setup(arch/mips/ath79/mach-tl-wa901nd.c)
            # [][checked] tl_wa901nd_v2_setup(arch/mips/ath79/mach-tl-wa901nd-v2.c)
            # [][checked] tl_wa901nd_v2_setup(arch/mips/ath79/mach-tl-wa901nd-v2.c)
            # [][checked] wdr3500_setup(arch/mips/ath79/mach-tl-wdr3500.c)
            # [][checked] wdr4300_setup(arch/mips/ath79/mach-tl-wdr4300.c)
            # [][checked] tl_wr741nd_setup(arch/mips/ath79/mach-tl-wr741nd.c)
            # [][checked] tl_wr741ndv4_setup(arch/mips/ath79/mach-tl-wr741nd-v4.c)
            # [][checked] tl_wr741ndv4_setup(arch/mips/ath79/mach-tl-wr741nd-v4.c)
            # [][checked] tl_wr841n_v1_setup(arch/mips/ath79/mach-tl-wr841n.c)
            # [][checked] tl_wr841n_v8_setup(arch/mips/ath79/mach-tl-wr841n-v8.c)
            # [][checked] tl_wr841n_v8_setup(arch/mips/ath79/mach-tl-wr841n-v8.c)
            # [][checked] tl_wr841n_v8_setup(arch/mips/ath79/mach-tl-wr841n-v8.c)
            # [][checked] tl_wr841n_v8_setup(arch/mips/ath79/mach-tl-wr841n-v8.c)
            # [][checked] tl_wr841n_v9_setup(arch/mips/ath79/mach-tl-wr841n-v9.c)
            # [][checked] tl_wr941nd_setup(arch/mips/ath79/mach-tl-wr941nd.c)
            # [][checked] tl_wr1041nv2_setup(arch/mips/ath79/mach-tl-wr1041n-v2.c)
            # [][checked] tl_wr1043nd_v2_setup(arch/mips/ath79/mach-tl-wr1043nd-v2.c)
            # [][checked] tl_wr1043nd_v2_setup(arch/mips/ath79/mach-tl-wr1043nd-v2.c)
            # [][checked] tl_wr2543n_setup(arch/mips/ath79/mach-tl-wr2543n.c)
            # [][checked] tl_mr10u_setup(arch/mips/ath79/mach-tl-wr703n.c)
            # [][checked] tl_mr10u_setup(arch/mips/ath79/mach-tl-wr703n.c)
            # [][checked] tl_mr10u_setup(arch/mips/ath79/mach-tl-wr703n.c)
            # [][checked] tl_wr720n_v3_setup(arch/mips/ath79/mach-tl-wr720n-v3.c)
            # [][checked] tube2h_setup(arch/mips/ath79/mach-tube2h.c)
            # [][checked] ubnt_rs_setup(arch/mips/ath79/mach-ubnt.c)
            # [][checked] ubnt_rs_setup(arch/mips/ath79/mach-ubnt.c)
            # [][checked] ubnt_rs_setup(arch/mips/ath79/mach-ubnt.c)
            # [][checked] ubnt_rs_setup(arch/mips/ath79/mach-ubnt.c)
            # [][checked] ubnt_xm_init(arch/mips/ath79/mach-ubnt-xm.c)
            # [][checked] ubnt_xm_init(arch/mips/ath79/mach-ubnt-xm.c)
            # [][checked] ubnt_xm_init(arch/mips/ath79/mach-ubnt-xm.c)
            # [][checked] ubnt_xm_init(arch/mips/ath79/mach-ubnt-xm.c)
            # [][checked] ubnt_xm_init(arch/mips/ath79/mach-ubnt-xm.c)
            # [][checked] ubnt_xm_init(arch/mips/ath79/mach-ubnt-xm.c)
            # [][checked] ubnt_xm_init(arch/mips/ath79/mach-ubnt-xm.c)
            # [][checked] ubnt_xm_init(arch/mips/ath79/mach-ubnt-xm.c)
            # [][checked] ubnt_xm_init(arch/mips/ath79/mach-ubnt-xm.c)
            # [][checked] ubnt_xm_init(arch/mips/ath79/mach-ubnt-xm.c)
            # [][checked] ubnt_xm_init(arch/mips/ath79/mach-ubnt-xm.c)
            # [][checked] ubnt_xm_init(arch/mips/ath79/mach-ubnt-xm.c)
            # [][checked] ubnt_xm_init(arch/mips/ath79/mach-ubnt-xm.c)
            # [][checked] whrhpg300n_setup(arch/mips/ath79/mach-whr-hp-g300n.c)
            # [][checked] whrhpg300n_setup(arch/mips/ath79/mach-whr-hp-g300n.c)
            # [][checked] whrhpg300n_setup(arch/mips/ath79/mach-whr-hp-g300n.c)
            # [][checked] wlaeag300n_setup(arch/mips/ath79/mach-wlae-ag300n.c)
            # [][checked] wlr8100_010_setup(arch/mips/ath79/mach-wlr8100.c)
            # [][checked] wndap360_setup(arch/mips/ath79/mach-wndap360.c)
            # [][checked] wndr4300_setup(arch/mips/ath79/mach-wndr4300.c)
            # [][checked] wndr4300_setup(arch/mips/ath79/mach-wndr4300.c)
            # [][checked] wndr4300_setup(arch/mips/ath79/mach-wndr4300.c)
            # [][checked] wnr2000_setup(arch/mips/ath79/mach-wnr2000.c)
            # [][checked] wnr2000v3_setup(arch/mips/ath79/mach-wnr2000-v3.c)
            # [][checked] wnr2000v3_setup(arch/mips/ath79/mach-wnr2000-v3.c)
            # [][checked] wnr2000v3_setup(arch/mips/ath79/mach-wnr2000-v3.c)
            # [][checked] wnr2000v4_setup(arch/mips/ath79/mach-wnr2000-v4.c)
            # [][checked] wnr2200_setup(arch/mips/ath79/mach-wnr2200.c)
            # [][checked] wp543_setup(arch/mips/ath79/mach-wp543.c)
            # [][checked] wpe72_setup(arch/mips/ath79/mach-wpe72.c)
            # [][checked] wpj344_setup(arch/mips/ath79/mach-wpj344.c)
            # [][checked] wpj531_setup(arch/mips/ath79/mach-wpj531.c)
            # [][checked] wpj558_setup(arch/mips/ath79/mach-wpj558.c)
            # [][checked] wrt160nl_setup(arch/mips/ath79/mach-wrt160nl.c)
            # [][checked] wrt400n_setup(arch/mips/ath79/mach-wrt400n.c)
            # [][checked] wzrhpg300nh2_setup(arch/mips/ath79/mach-wzr-hp-g300nh2.c)
            # [][checked] wzrhpg300nh2_setup(arch/mips/ath79/mach-wzr-hp-g300nh2.c)
            # [][checked] wzrhpag300h_setup(arch/mips/ath79/mach-wzr-hp-ag300h.c)
            # [][checked] wzrhpg450h_init(arch/mips/ath79/mach-wzr-hp-g450h.c)
            # [][checked] wzr_450hp2_setup(arch/mips/ath79/mach-wzr-450hp2.c)
            # [][checked] zcn_1523h_2_setup(arch/mips/ath79/mach-zcn-1523h.c)
            # [][checked] zcn_1523h_2_setup(arch/mips/ath79/mach-zcn-1523h.c)
            # [][checked] carambola2_setup(arch/mips/ath79/mach-carambola2.c)
            # [][unchecked] nbg6716_010_setup(arch/mips/ath79/mach-nbg6716.c)


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

        return True

    def __init__(self, analysis_manager):
        super().__init__(analysis_manager)
        self.name = 'platform_devices'
        self.description = 'source code info analysis (llvm)'
        self.required = ['stimer']
        self.context['hint'] = ''
        self.critical = False

