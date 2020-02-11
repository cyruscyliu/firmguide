"""
UNMODELED_SKIP_LIST:  WE DON'T ANALYZE THEM
  MODELED_SKIP_TABLE: WE DON'T ANALYZE THEM ANY MORE
"""

def _default(analysis, firmware, **kwargs):
    pass


def _irq_set_chip_and_handler_name(analysis, firmware, **kwargs):
    # [FUNCTION] extern void irq_set_chip_and_handler_name(
    # unsigned int irq, struct irq_chip *chip, irq_flow_handler_t handle, const char *name);
    caller = kwargs.pop('caller')
    if firmware.uuid == 'ar71xx_generic':
        if caller == 'ath79_misc_irq_init':
            # for (i = 8; i < 8 + 32; i++) { irq_set_chip_and_handler(i, &ath79_misc_irq_chip, handle_level_irq); }
            for i in range(8, 40):
                analysis.info(firmware, '? {} direct handle_level_irq ath79_misc_irq_chip'.format(i), 1)
        elif caller == 'mips_cpu_irq_init':
            for i in range(0, 8):
                analysis.debug(firmware, '{0} {0} direct handle_percpu_irq  mips_cpu_irq_controller'.format(i), 1)
        else:
            analysis.warning(firmware, '{} -> irq_set_chip_and_handler_name(w/o handler)'.format(caller), 0)
    else:
        analysis.warning(firmware, '{} -> irq_set_chip_and_handler_name(w/o handler)'.format(caller), 0)


def ___irq_set_handler(analysis, firmware, **kwargs):
    # [FUNCTION] extern void __irq_set_handler(
    # unsigned int irq, irq_flow_handler_t handle, int is_chained, const char *name);
    caller = kwargs.pop('caller')
    if firmware.uuid == 'ar71xx_generic':
        # irq_set_chained_handler((0 + (6)), ath79_misc_irq_handler);
        # When we meet chained handler, we must go deeply. What's the
        # mapping between hwirqn and irqn? Usually, hwirqn comes from
        # mmio or mmios, say hwirqn = F(m1, m2). Perform the reachability
        # analysis to the function 'generic_handler_irq(irqn)' and we
        # get the formula: irqn = f(hwirqn) = f(F(m1, m2)) (f-1).
        # Now, we may get several irqns no hwirqns, according to f-1,
        # Let irqn = 8, then we can get its hwirqns, and mmios with proper
        # init values.
        if caller == 'ath79_misc_irq_init':
            analysis.debug(firmware, 'to reach generic_handler_irq, (readl(base + 0x10) & readl(base + 0x14)) != 0', 1)
            analysis.info(firmware, '6 6 chained ath79_misc_irq_handler None ', 1)
            analysis.info(firmware, '6 6 irqn = 8 + __ffs(readl(base+0x10)&readl(base+0x14))', 1)
        else:
            analysis.warning(firmware, '{} -> __irq_set_handler(w/o handler)', 0)
    elif firmware.uuid == 'rampis_rt3883':
        if caller == 'intc_of_init':
            # irq_set_chained_handler(irq, ralink_intc_irq_handler);
            analysis.debug(firmware, 'to reach generic_handler_irq, readl(rt_intc_membase+0x00) != 0', 1)
            analysis.info(firmware, '? ? chained ralink_intc_irq_handler None ', 1)
            analysis.info(firmware, '? ? irqn = remap(__ffs(readl(rt_intc_membase+0x00))', 1)
        else:
            analysis.warning(firmware, '{} -> __irq_set_handler(w/o handler)', 0)
    else:
        analysis.warning(firmware, '{} -> __irq_set_handler(w/o handler)', 0)


def _irq_domain_add_legacy(analysis, firmware, **kwargs):
    # [FUNCTION]  struct irq_domain *irq_domain_add_legacy(struct device_node *of_node, unsigned int size,
    # unsigned int first_irq, irq_hw_number_t first_hwirq, const struct irq_domain_ops *ops, void *host_data);
    caller = kwargs.pop('caller')
    if firmware.uuid == 'rampis_rt3883':
        if caller == 'mips_cpu_intc_init':
            # domain = irq_domain_add_legacy(of_node, 8, 0, 0, &mips_cpu_intc_irq_domain_ops, ((void *)0));
            for i in range(0, 8):
                analysis.debug(firmware, '{0} {0} direct mips_cpu_intc_irq_domain_ops None'.format(i), 1)
        elif caller == 'intc_of_init':
            # domain = irq_domain_add_legacy(node, 32, 8, 0, &irq_domain_ops, ((void *)0));
            for i in range(0, 32):
                analysis.debug(firmware, '{0} {1} direct mips_cpu_intc_irq_domain_ops None'.format(i, i+8), 1)
        else:
            analysis.warning(firmware, '{} -> irq_domain_add_legacy(w/o handler)'.format(caller), 0)
    else:
        analysis.warning(firmware, '{} -> irq_domain_add_legacy(w/o handler)'.format(caller), 0)


def ___ioremap(analysis, firmware, **kwargs):
    # [FUNCTION] void __iomem * __ioremap(phys_t offset, phys_t size, unsigned long flags);
    caller = kwargs.pop('caller')
    if firmware.uuid == 'ar71xx_generic':
        if caller == 'ath79_gpio_init':
            # ath79_gpio_base = __ioremap_mode(((0x18000000 + 0x00040000)), (0x100), ...)
            mmio_name = 'ath79_gpio'
            mmio_base = eval('((0x18000000 + 0x00040000))')
            mmio_size = eval('(0x100)')
            firmware.insert_bamboo_devices(mmio_base, mmio_size, value=0)
            analysis.info(firmware, 'get mmio base {} size {}'.format(hex(mmio_base), hex(mmio_size)), 1)
        else:
            analysis.warning(firmware, '{} -> __ioremap(w/o handler)'.format(caller), 0)
    elif firmware.uuid == 'rampis_rt3883':
        if caller == 'intc_of_init':
            # rt_intc_membase = __ioremap_mode((res.start), (resource_size(&res)), ...)
            mmio_name = '?'
            mmio_base = 0xFFFFFFFF
            mmio_size = 0xFFFFFFFF
            analysis.info(firmware, 'get mmio base {} size {}'.format(hex(mmio_base), hex(mmio_size)), 1)
        else:
            analysis.warning(firmware, '{} -> __ioremap(w/o handler)'.format(caller), 0)
    else:
        analysis.warning(firmware, '{} -> __ioremap(w/o handler)'.format(caller), 0)


def _panic(analysis, firmware, **kwargs):
    # [FUNCTION] panic()
    # panic() is a very strong mark of exceptional path
    caller = kwargs.pop('caller')
    if firmware.uuid == 'ar71xx_generic':
        if caller == 'ath79_detect_sys_type':
            # by manually analysis, we know
            # ath79_reset_rr(0x90)
            # (*(0x18060000 + 0x90)) & 0xfff0 == 0x00a0 or
            # (*(0x18060000 + 0x90)) & 0xfff0 == 0x00c0 or
            # (*(0x18060000 + 0x90)) & 0xfff0 == 0x0100 or
            # (*(0x18060000 + 0x90)) & 0xfff0 == 0x1100 or
            # (*(0x18060000 + 0x90)) & 0xfff0 == 0x00b0 or
            # (*(0x18060000 + 0x90)) & 0xfff0 == 0x0110 or
            # (*(0x18060000 + 0x90)) & 0xfff0 == 0x0120 or
            # (*(0x18060000 + 0x90)) & 0xfff0 == 0x1120 or
            # (*(0x18060000 + 0x90)) & 0xfff0 == 0x2120 or
            # (*(0x18060000 + 0x90)) & 0xfff0 == 0x0160 or
            # (*(0x18060000 + 0x90)) & 0xfff0 == 0x0140 or
            # (*(0x18060000 + 0x90)) & 0xfff0 == 0x0130 or
            # (*(0x18060000 + 0x90)) & 0xfff0 == 0x1130 or
            # (*(0x18060000 + 0x90)) & 0xfff0 == 0x0150 or
            # (*(0x18060000 + 0x90)) & 0xfff0 == 0x1150
            mmio_name = 'ath79_reset_rr'
            mmio_base = eval('(0x18060000 + 0x90)')
            mmio_size = 0x4
            mmio_value = 0x00b0
            # firmware.insert_bamboo_devices(mmio_base, mmio_size, value=mmio_value)
        else:
            analysis.warning(firmware, '{} -> panic(w/o handler)'.format(caller), 0)
    elif firmware.uuid == 'rampis_rt3883':
        if caller == 'mips_cpu_intc_init':
            # return from any function in MODELED_SKIP_TABLE
            pass
        elif caller == 'intc_of_init':
            # return from any function in UNMODELED_SKIP_LIST
            pass
    else:
        analysis.warning(firmware, '{} -> panic(w/o handler)'.format(caller), 0)


def _r4k_clockevent_init(analysis, firmware, **kwargs):
    analysis.info(firmware, 'get mips internel timer as interrupt source', 1)


def _init_r4k_clocksource(analysis, firmware, **kwargs):
     analysis.info(firmware, 'get mips internel timer as clock source', 1)


def ___builtin_unreachable(analysis, firmware, **kwargs):
     # BUG()/BUG_ON() is a very strong mark of exceptional path
     caller = kwargs.pop('caller')
     if firmware.uuid == 'ar71xx_generic':
         if caller == 'ath79_register_wmac':
             # if (soc_is_ar913x()) ar913x_wmac_setup();
             # else if (soc_is_ar933x()) ar933x_wmac_setup();
             # else if (soc_is_ar934x()) ar934x_wmac_setup();
             # else if (soc_is_qca953x()) qca953x_wmac_setup();
             # else if (soc_is_qca955x()) qca955x_wmac_setup();
             # else if (soc_is_qca956x()) qca956x_wmac_setup();
             # else BUG();
             # by manually analysis, we know
             # (ath79_soc == ATH79_SOC_AR9130 || ath79_soc == ATH79_SOC_AR9132);
             # (ath79_soc == ATH79_SOC_AR9330 || ath79_soc == ATH79_SOC_AR9331);
             # (ath79_soc == ATH79_SOC_AR9341) || (ath79_soc == ATH79_SOC_AR9342) || (ath79_soc == ATH79_SOC_AR9344);
             # (ath79_soc == ATH79_SOC_QCA9533);
             # (ath79_soc == ATH79_SOC_QCA9556) || (ath79_soc == ATH79_SOC_QCA9558);
             # (ath79_soc == ATH79_SOC_TP9343) || (ath79_soc == ATH79_SOC_QCA9561);
             # we need a ud analysis, manually we know
             # ath79_soc is defined in ath79_detect_sys_type which is analyzed just above
             # ath79_soc is used in ath79_register_wmac and has several reasonable values
             # so ath79_reset_rr's value could be 0x00b0, so ath79_soc is ATH79_SOC_AR9130
             mmio_name = 'ath79_reset_rr'
             mmio_base = eval('(0x18060000 + 0x90)')
             mmio_size = 0x4
             mmio_value = 0x00b0
             firmware.insert_bamboo_devices(mmio_base, mmio_size, value=mmio_value)
         analysis.warning(firmware, '{} -> BUG()/BUG_ON() found but no handlers'.format(caller), 0)
     else:
         analysis.warning(firmware, '{} -> BUG()/BUG_ON() found but no handlers'.format(caller), 0)


UNMODELED_SKIP_LIST = [
    'early_init_dt_scan', 'of_flat_dt_get_machine_name', 'of_scan_flat_dt',
    'kmemdup', 'kfree', 'msleep', '__builtin_memcmp', 'add_memory_region', 'detect_memory_region',
    'clk_get', 'clk_get_rate', 'clk_put', 'sprintf',  '__udelay',
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
    'mv88e6060_init', 'mv88e6063_init', 'ag71xx_module_init', 'ath79_wdt_driver_init', 'strlcpy', 'printk',
    'irq_create_mapping', 'of_address_to_resource', 'of_property_read_u32_array', 'irq_of_parse_and_map',
    'irq_set_handler_data', 'arch_mem_addpart', 'print_memory_map', 'mips_parse_crashkernel', 'bootmem_init',
    'cpu_report', 'check_bugs_early', 'resource_init', 'plat_smp_setup', 'prefill_possible_map', 'cpu_cache_init',
    'paging_init',
    # for performance consideration
    'set_isa'
]


MODELED_SKIP_TABLE= {
    'irq_modify_status': {'handle': _default},
    'irq_set_chip_and_handler_name': {'handle': _irq_set_chip_and_handler_name},
    '__irq_set_handler': {'handle': ___irq_set_handler},
    'irq_domain_add_legacy': {'handle': _irq_domain_add_legacy},
    '__ioremap': {'handle': ___ioremap},
    'panic': {'handle': _panic},
    'r4k_clockevent_init': {'handle': _r4k_clockevent_init},
    'init_r4k_clocksource': {'handle': _init_r4k_clocksource},
    '__builtin_unreachable': {'handle': ___builtin_unreachable},
}


