'''
Source Code Info Analysis.
'''
import os
import re

from analyses.analysis import Analysis
from pycparser import c_parser, c_ast, parse_file

DONOT_ANALYSIS = [
    'kmemdup', 'kfree', 'msleep',
    '__builtin_unreachable', 'clk_get', 'panic', 'clk_get_rate', 'clk_put',
    '__builtin_memset', 'pcibios_init', 'ipc_ns_init', 'init_mmap_min_addr', 'net_ns_init',
    'wq_sysfs_init', 'ksysfs_init', 'init_jiffies_clocksource', 'init_zero_pfn', 'fsnotify_init',
    'filelock_init', 'init_script_binfmt', 'init_elf_binfmt', 'debugfs_init', 'prandom_init',
    'sock_init', 'netlink_proto_init', 'bdi_class_init', 'mm_sysfs_init', 'kobject_uevent_init',
    'gpiolib_sysfs_init', 'pcibus_class_init', 'pci_driver_init', 'tty_class_init', 'pi_init',
    'i2c_init', 'frame_info_init', 'debugfs_mips', 'signal_setup', 'trap_pm_init', 'r4k_cache_init_pm',
    'r4k_tlb_init_pm', 'topology_init', 'init_vdso', 'uid_cache_init', 'param_sysfs_init', 'pm_sysrq_init',
    'default_bdi_init', 'percpu_enable_async', 'init_reserve_notifier', 'init_admin_reserve',
    'init_user_reserve', 'cryptomgr_init', 'init_bio', 'blk_settings_init', 'blk_ioc_init',
    'blk_softirq_init', 'blk_iopoll_setup', 'blk_mq_init', 'genhd_device_init', 'gpiolib_debugfs_init',
    'nxp_74hc153_init', 'pcf857x_init', 'pci_slot_init', 'misc_init', 'dma_buf_init', 'mtdsplit_seama_init',
    'mtdsplit_squashfs_init', 'mtdsplit_lzma_init', 'phy_init', 'i2c_gpio_init', 'watchdog_init', 'leds_init',
    'proto_init', 'net_dev_init', 'neigh_init', 'fib_rules_init', 'pktsched_init', 'tc_filter_init',
    'tc_action_init', 'genl_init', 'wireless_nlevent_init', 'mips_dma_init', 'clocksource_done_booting',
    'init_pipe_fs', 'eventpoll_init', 'anon_inode_init', 'proc_cmdline_init', 'proc_consoles_init',
    'proc_cpuinfo_init', 'proc_devices_init', 'proc_interrupts_init', 'proc_loadavg_init', 'proc_meminfo_init',
    'proc_stat_init', 'proc_uptime_init', 'proc_version_init', 'proc_softirqs_init', 'proc_kmsg_init',
    'init_ramfs_fs', 'blk_scsi_ioctl_init', 'chr_dev_init', 'firmware_class_init', 'sysctl_core_init',
    'inet_init', 'ipv4_offload_init', 'af_unix_init', 'ipv6_offload_init', 'debugfs_unaligned', 'segments_info',
    'proc_execdomains_init', 'ioresources_init', 'init_posix_timers', 'init_posix_cpu_timers',
    'timekeeping_init_ops', 'init_clocksource_sysfs', 'init_timer_list_procfs', 'alarmtimer_init',
    'clockevents_init_sysfs', 'init_tstats_procfs', 'futex_init', 'proc_modules_init', 'kallsyms_init',
    'utsname_sysctl_init', 'crashlog_init_fs', 'init_per_zone_wmark_min', 'kswapd_init', 'setup_vmstat',
    'workingset_init', 'proc_vmalloc_init', 'procswaps_init', 'slab_sysfs_init', 'fcntl_init',
    'proc_filesystems_init', 'dio_init', 'fsnotify_mark_init', 'inotify_user_setup', 'proc_locks_init',
    'init_devpts_fs', 'init_squashfs_fs', 'init_jffs2_fs', 'ovl_init', 'ipc_init', 'ipc_sysctl_init',
    'key_proc_init', 'crypto_algapi_init', 'aes_init', 'proc_genhd_init', 'noop_init', 'deadline_init',
    'phy_core_init', 'pci_proc_init', 'pty_init', 'sysrq_init', 'serial8250_init', 'topology_sysfs_init',
    'init_mtd', 'mtdsplit_uimage_init', 'redboot_parser_init', 'cmdline_parser_init', 'myloader_mtd_parser_init',
    'tplink_parser_init', 'cybertan_parser_init', 'init_mtdblock', 'cfi_probe_init', 'physmap_init', 'm25p80_driver_init',
    'net_olddevs_init', 'swconfig_init', 'marvell_init', 'rtl_init', 'ksphy_init', 'gpio_led_driver_init',
    'timer_trig_init', 'defon_trig_init', 'netdev_trig_init', 'staging_init', 'llc_init', 'snap_init',
    'blackhole_module_init', 'fq_codel_module_init', 'gre_offload_init', 'sysctl_ipv4_init', 'ipv4_netfilter_init',
    'cubictcp_register', 'packet_init', 'br_init', 'br_netfilter_init', 'dsa_init_module', 'vlan_proto_init',
    'init_oops_id', 'pm_qos_power_init', 'printk_late_init', 'tk_debug_sleep_time_init', 'fault_around_debugfs',
    'init_root_keyring', 'prandom_reseed', 'pci_resource_alignment_sysfs_init', 'pci_sysfs_init',
    'deferred_probe_initcall', 'tcp_congestion_default', 'ar933x_uart_init', 'ap83_spi_init', 'ath79_spi_driver_init',
    'ip17xx_init', 'ar8xxx_init', 'rtl8366s_module_init', 'rtl8366rb_module_init', 'rtl8367_module_init', 'atheros_init',
    'mv88e6060_init', 'mv88e6063_init', 'ag71xx_module_init', 'ath79_wdt_driver_init', 'strlcpy', 'printk'
]

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

    def get_funccalls(self, firmware, ep, caller='do_initcall'):
        address = firmware.srcodec.symbol2address(ep)
        if address is None:
            self.warning(firmware, '{} -> {}(no address)'.format(caller, ep), 1)
            return None, None, []

        path_to_entry_point = firmware.srcodec.addr2file(address)
        if not path_to_entry_point.startswith('arch'):
            self.debug(firmware, '{} -> {}({})'.format(caller, ep, path_to_entry_point), 1)
            return address, path_to_entry_point, []

        dirs = path_to_entry_point.split('/')
        # self.debug(firmware, '{} -> {}({})'.format(caller, ep, path_to_entry_point), 1)
        if dirs[2] == 'include':
            self.warning(firmware, '{} -> {}(inline in header)'.format(caller, ep, path_to_entry_point), 1)
            return address, path_to_entry_point, []

        cmdline = firmware.srcodec.get_cmdline(path_to_entry_point)
        path_to_pentry_point = firmware.srcodec.preprocess(path_to_entry_point, cmdline=cmdline)
        if path_to_pentry_point is None:
            self.debug(firmware, '{} -> {}(error in preprocessing)'.format(caller, ep, path_to_entry_point), 1)
            return address, None, []

        funccalls = firmware.srcodec.get_funccalls(path_to_pentry_point, ep, mode='sparse')
        self.debug(firmware, '{} -> {}'.format(ep, funccalls), 1)

        return address, path_to_entry_point, funccalls

    def parse_funcalls(self, firmware, caller, funccalls):
        # remove duplicated functions
        funccalls = list(set(funccalls))

        # remove functions we donot want to analysis
        for da in DONOT_ANALYSIS:
            if da in funccalls:
                self.debug(firmware, '{} -> {}(built-in function)'.format(caller, da), 1)
                funccalls.remove(da)

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
                    uart_irqn = eval('(8 + (3))')
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
        if firmware.get_architecture() == 'mips' and 'mips_machine_setup' in funccalls:
            funccalls.remove('mips_machine_setup')
            # according to arch/mips/include/asm/mips_machine.h, we have
            # system_map = firmware.srcodec.get_system_map()
            # for symbol, v in system_map.items():
                # machine_id_##_type
                # if symbol.startswith('machine_id'):
                    # addr2line not work for data
                    # machine_type = symbol[11:]
                    # output = os.popen('grep -nir "MIPS_MACHINE({}" {}/arch/{}'.format(
                        # machine_type, firmware.srcodec.srcode, firmware.get_architecture())).readlines()
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

        # [FUNCTION] void __iomem * __ioremap(phys_t offset, phys_t size, unsigned long flags);
        if '__ioremap' in funccalls:
            funccalls.remove('__ioremap')
            if firmware.uuid == 'ar71xx_generic':
                if caller == 'ath79_gpio_init':
                    # ath79_gpio_init(arch/mips/include/asm/mach-ath79/ath79.h)
                    # [DIRECT] ath79_gpio_base = __ioremap_mode(((0x18000000 + 0x00040000)), (0x100), ...)
                    mmio_name = 'ath79_gpio'
                    mmio_base = eval('((0x18000000 + 0x00040000))')
                    mmio_size = eval('(0x100)')
                    firmware.insert_bamboo_devices(mmio_base, mmio_size, value=0)
                    self.info(firmware, 'get mmio base {} size {}'.format(hex(mmio_base), hex(mmio_size)), 1)
                else:
                    self.warning(firmware, 'platform_device_register_full found but no handlers', 0)
            else:
                self.warning(firmware, 'platform_device_register_full found but no handlers', 0)

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
                    firmware.set_flash('0', flash_name, flash_type, flash_interface, flash_base, flash_size)
                    self.info(firmware, 'get {} {} flash {}'.format(flash_interface, flash_type, flash_name), 1)
                else:
                    self.warning(firmware, 'spi_register_board_info found but no handlers', 0)
            else:
                self.warning(firmware, 'spi_register_board_info found but no handlers', 0)

        if len(funccalls):
            self.debug(firmware, '{} -> {}(unhandled)'.format(caller, funccalls), 1)
        return funccalls

    def traverse_funccalls(self, firmware, entry_point, caller=None, depth=0):
        if depth == 4:
            return
        for ep in entry_point:
            address, path_to_ep, funccalls = self.get_funccalls(firmware, ep, caller=caller)
            funccalls = self.parse_funcalls(firmware, ep, funccalls)
            self.traverse_funccalls(firmware, funccalls, caller=ep, depth=depth+1)

    def run(self, firmware):
        """
        here is for platform_devices
        """
        # do_initcall analysis
        # "early", "core", "postcore", "arch", "subsys", "fs", "device", "late",
        system_map = firmware.srcodec.get_system_map()
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
            self.parse_funcalls(firmware, 'ath79_gpio_init', ['__ioremap'])
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
            # [][][][][][checked] ar934x_get_mdio_ref_clock(no address)
            # [][][][][][DIRECT] platform_device_register(mdio_dev);
            # [][][][][done]
            # [][][][][checked] ath79_init_mac(arch/mips/ath79/dev-eth.c)
            # [][][][][checked] ath79_register_eth(arch/mips/ath79/dev-eth.c)
            # [][][][][][checked] ath79_init_eth_pll_data(no address)
            # [][][][][][checked] ath79_setup_phy_if_mode(no address)
            # [][][][][][checked] get_random_bytes(drivers/char/random.c)
            # [][][][][][checked] ath79_device_reset_set which is out of our scope by its name
            # [][][][][][checked] ath79_device_reset_clear which is out of our scope by its name
            # [][][][][][DIRECT] platform_device_register(pdev)
            # [][][][][done]
            # [][][][][checked] ath79_register_wmac(arch/mips/include/asm/mach-ath79/ath79.h)
            # inline function in header but addr2line is wrong
            path_to_entry_point = 'arch/mips/ath79/dev-wmac.c'
            cmdline = firmware.srcodec.get_cmdline(path_to_entry_point)
            path_to_pentry_point = firmware.srcodec.preprocess(path_to_entry_point, cmdline=cmdline)
            entry_point = [
                'ar913x_wmac_setup', 'ar933x_wmac_setup', 'ar934x_wmac_setup',
                'qca953x_wmac_setup','qca955x_wmac_setup', 'qca956x_wmac_setup', 'platform_device_register']
            funccalls = firmware.srcodec.get_funccalls(path_to_pentry_point, 'ath79_register_wmac', mode='sparse')
            self.info(firmware, '{} -> {}'.format('ath79_register_wmac', funccalls), 1)
            funccalls = self.parse_funcalls(firmware, 'ath79_register_wmac', entry_point)
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
        self.name = 'platform_devices'
        self.description = 'source code info analysis (llvm)'
        self.required = ['stimer']
        self.context['hint'] = ''
        self.critical = False

