"""
UNMODELED_SKIP_LIST:  WE DON'T ANALYZE THEM
  MODELED_SKIP_TABLE: WE DON'T ANALYZE THEM ANY MORE
"""

def _default(analysis, firmware, **kwargs):
    pass


def _clkdev_add(analysis, firmware, **kwargs):
    # [FUNCTION] void clkdev_add(struct clk_loopup *cl);
    caller = kwargs.pop('caller')
    if firmware.uuid == 'ramips_rt3883':
        if caller == 'ralink_clk_add':
            # from ralink_clk_init we known
            # syscfg0 = rt_sysc_r32(0x10);
            # clksel = ((syscfg0 >> 8) & 0x3);
            # ddr2 = syscfg0 & (1UL << (17));
            # switch (clksel) {
                # case 0x0: cpu_rate = 250000000; sys_rate = (ddr2) ? 125000000 : 83000000; break;
                # case 0x1: cpu_rate = 384000000; sys_rate = (ddr2) ? 128000000 : 96000000; break;
                # case 0x2: cpu_rate = 480000000; sys_rate = (ddr2) ? 160000000 : 120000000; break;
                # case 0x3: cpu_rate = 500000000; sys_rate = (ddr2) ? 166000000 : 125000000; break;
            # }
            # ralink_clk_add("cpu", cpu_rate); # cpu_rate has no relationship to mmio init value
            # ralink_clk_add("10000100.timer", sys_rate);
            # ralink_clk_add("10000120.watchdog", sys_rate);
            # ralink_clk_add("10000500.uart", 40000000);
            # ralink_clk_add("10000b00.spi", sys_rate);
            # ralink_clk_add("10000c00.uartlite", 40000000);
            # ralink_clk_add("10100000.ethernet", sys_rate);
            # ralink_clk_add("10180000.wmac", 40000000);
            analysis.info(firmware, 'set clk cpu with rate {}'.format(250000000), 1)
        else:
            analysis.warning(firmware, '{} -> clkdev_add(w/o handler)'.format(caller), 0)
    else:
        analysis.warning(firmware, '{} -> clkdev_add(w/o handler)'.format(caller), 0)


def _clk_get_sys(analysis, firmware, **kwargs):
    # [FUNCTION] struct clk *clk_get_sys(const char *dev_id, const char *con_id);
    caller = kwargs.pop('caller')
    if firmware.uuid == 'ramips_rt3883':
        if caller == 'plat_time_init':
            # ralink_clk_add("cpu", cpu_rate); # cpu_rate has no relationship to mmio init value
            analysis.info(firmware, 'get clk cpu with rate {}'.format(250000000), 1)
        else:
            analysis.warning(firmware, '{} -> clk_get_sys(w/o handler)'.format(caller), 0)
    else:
        analysis.warning(firmware, '{} -> clk_get_sys(w/o handler)'.format(caller), 0)


def _clockevents_register_device(analysis, firmware, **kwargs):
    # [FUNCTION] extern void clockevents_register_device(struct clock_event_device *dev);
    caller = kwargs.pop('caller')
    if firmware.uuid == 'ramips_rt3883':
        if caller == 'r4k_clockevent_init':
            # cd->event_handler = mips_event_handler;
            # clockevents_register_device(cd);
            analysis.info(firmware, 'irqn07 -> hw07, clockevent device, event_handler=mips_event_handler', 1)
        else:
            analysis.warning(firmware, '{} -> clockevents_register_device(w/o handler)'.format(caller), 0)
    else:
        analysis.warning(firmware, '{} -> clockevents_register_device(w/o handler)'.format(caller), 0)


def _setup_irq(analysis, firmware, **kwargs):
    # [FUNCTION] extern int setup_irq(unsigned int irq, struct irqaction *new);
    caller = kwargs.pop('caller')
    if firmware.uuid == 'ramips_rt3883':
        if caller == 'r4k_clockevent_init':
            # setup_irq(irq, &c0_compare_irqaction);
            # -> write_c0_compare(read_c0_compare()); cd->event_handler(cd);
            analysis.info(firmware, 'irqn07 -> hw07, timer interrupt, handler=c0_compare_interrupt', 1)
        else:
            analysis.warning(firmware, '{} -> setup_irq(w/o handler)'.format(caller), 0)
    else:
        analysis.warning(firmware, '{} -> setup_irq(w/o handler)'.format(caller), 0)


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
    elif firmware.uuid == 'ramips_rt3883':
        if caller == 'mips_cpu_intc_map':
            # irq_set_chip_and_handler(irq, chip, handle_percpu_irq);
            analysis.info(firmware, 'irqn00-07 -> hw00->07, handle_percpu_irq, mips_cpu_irq_controller', 1)
            get_registers = "[{rname: c0, offset: -1, unmask_action: (set_c0_status(0x100 << (d->irq - 0))), unmask: True, mask_action: (clear_c0_status(0x100 << (d->irq - 0))), mask: True, ack_action: (clear_c0_status(0x100 << (d->irq - 0))), ack: True}]"
            analysis.info(firmware, 'get_register: {}'.format(get_registers), 1)
        elif caller == 'intc_map':
            # irq_set_chip_and_handler(irq, &ralink_intc_irq_chip, handle_level_irq);
            analysis.info(firmware, 'irqn08->39 -> hw00-31, handle_level_irq, ralink_intc_irq_chip', 1)
            get_registers = "[{rname: r1, offset: '0x34', unmask_action: (1 << irqn), mask_ack: False, mask: False, unmask: True, ack: False}, {rname: r2, offset: '0x38', mask_ack_action: (1 << irqn), mask_ack: True, mask_action: (1 << irqn), mask: False, unmask: False, ack: False}]"
            analysis.info(firmware, 'get_register: {}'.format(get_registers), 1)
        else:
            analysis.warning(firmware, '{} -> irq_set_chip_and_handler_name(w/o handler)'.format(caller), 0)
    elif firmware.uuid == 'oxnas_generic':
        if caller == 'rps_irq_domain_map':
            # irq_set_chip_and_handler(irq, &rps_chip, handle_level_irq);
            analysis.info(firmware, 'irqn??->?? -> hw00-31, handle_level_irq, rps_chip', 1)
            # RPS_UNMASK = 8, RPS_MASK = 0xc,
            # u32 mask = (1UL << (d->hwirq));
            # __raw_writel(( __u32)(( __le32)(__u32)(mask)), chip_data->base + RPS_MASK); });
            get_registers = "[{rname: r1, offset: '0x8', unmask_action: (1 << irqn), mask_ack: False, mask: False, unmask: True, ack: False}, {rname: r2, offset: '0xc', mask_ack: False, mask_action: (1 << irqn), mask: False, unmask: False, ack: False}]"
            analysis.info(firmware, 'get_register: {}'.format(get_registers), 1)
    else:
        analysis.warning(firmware, '{} -> irq_set_chip_and_handler_name(w/o handler)'.format(caller), 0)


def ___irq_set_handler(analysis, firmware, **kwargs):
    # [FUNCTION] extern void __irq_set_handler(
    # unsigned int irq, irq_flow_handler_t handle, int is_chained, const char *name);
    caller = kwargs.pop('caller')
    analysis.info(firmware, '{} -> __irq_set_handler(found, level2 intc mmio->irqn mapping)'.format(caller), 0)
    if firmware.uuid == 'ar71xx_generic':
        # When we meet chained handler, we must go deeply. What's the
        # mapping between hwirqn and irqn? Usually, hwirqn comes from
        # mmio or mmios, say hwirqn = F(m1, m2). Perform the reachability
        # analysis to the function 'generic_handler_irq(irqn)' and we
        # get the formula: irqn = f(hwirqn) = f(F(m1, m2)) (f-1).
        # Now, we may get several irqns no hwirqns, according to f-1,
        # Let irqn = 8, then we can get its hwirqns, and mmios with proper
        # init values.
        if caller == 'ath79_misc_irq_init':
            # irq_set_chained_handler((0 + (6)), ath79_misc_irq_handler);
            analysis.debug(firmware, 'to reach generic_handler_irq, (readl(base + 0x10) & readl(base + 0x14)) != 0', 1)
            analysis.info(firmware, 'irqn = 8 + __ffs(readl(base+0x10)&readl(base+0x14))', 1)
        else:
            analysis.warning(firmware, '{} -> __irq_set_handler(w/o handler)', 0)
    elif firmware.uuid == 'ramips_rt3883':
        if caller == 'intc_of_init':
            # irq_set_chained_handler(irq, ralink_intc_irq_handler);
            analysis.debug(firmware, 'to reach generic_handler_irq, readl(rt_intc_membase+0x00) != 0', 1)
            # irqn = remap(__ffs(readl(rt_intc_membase+0x00))
            # __ffs find the first set bit in the word
            # 0b00000001 -> 0; 0b00100000 -> 5;
            irqn_to_reg = "{irqn: i, set_body: ['s->r0 |= (1 << i);'], clear_body: ['s->r0 &= ~(1 << i);']}"
            analysis.info(firmware, 'irqn_to_reg: {}'.format(irqn_to_reg), 1)
        else:
            analysis.warning(firmware, '{} -> __irq_set_handler(w/o handler)'.format(caller), 0)
    elif firmware.uuid == 'oxnas_generic':
        if caller == 'gic_cascade_irq':
            # irq_set_chained_handler(irq, gic_handle_cascade_irq)
            analysis.debug(firmware, 'to reach generic_handler_irq, 32 <= readl(cpu_base.common_base+0x00) <= 1020', 1)
            # irqn = readl(cpu_base.common_base+0x0c) & 0x3ff
            irqn_to_reg = "{irqn: i, set_body: ['s->r0 = (i);'], clear_body: ['s->r0 = 1023);']}"
            analysis.info(firmware, 'irqn_to_reg: {}'.format(irqn_to_reg), 1)
        elif caller == 'rps_of_init':
            # irq_set_chip_and_handler(irq, rps_handle_cascade_irq)
            analysis.debug(firmware, 'to reach generic_handler_irq, __ffs(readl(base+0x00)) < 32', 1)
            # status = __raw_readl(chip_data->base + RPS_STATUS)
            # rps_irq = __ffs(status)
            irqn_to_reg = "{irqn: i, set_body: ['s->r0 |= (1 << i);'], clear_body: ['s->r0 &= ~(1 << i);']}"
        else:
            analysis.warning(firmware, '{} -> __irq_set_handler(w/o handler)'.format(caller), 0)
    else:
        analysis.warning(firmware, '{} -> __irq_set_handler(w/o handler)'.format(caller), 0)


def _panic(analysis, firmware, **kwargs):
    # [FUNCTION] panic()
    # panic() is a very strong mark of exceptional path
    caller = kwargs.pop('caller')
    if firmware.uuid == 'ath79_generic':
        if caller == 'ath79_detect_sys_type':
            # by manually analysis, we know
            # ath79_reset_rr(0x90)
            # (*(0x18060000 + 0x90)) & 0xfff0 == 0x00a0 or (*(0x18060000 + 0x90)) & 0xfff0 == 0x00c0 or
            # (*(0x18060000 + 0x90)) & 0xfff0 == 0x0100 or (*(0x18060000 + 0x90)) & 0xfff0 == 0x1100 or
            # (*(0x18060000 + 0x90)) & 0xfff0 == 0x00b0 or (*(0x18060000 + 0x90)) & 0xfff0 == 0x0110 or
            # (*(0x18060000 + 0x90)) & 0xfff0 == 0x0120 or (*(0x18060000 + 0x90)) & 0xfff0 == 0x1120 or
            # (*(0x18060000 + 0x90)) & 0xfff0 == 0x2120 or (*(0x18060000 + 0x90)) & 0xfff0 == 0x0160 or
            # (*(0x18060000 + 0x90)) & 0xfff0 == 0x0140 or (*(0x18060000 + 0x90)) & 0xfff0 == 0x0130 or
            # (*(0x18060000 + 0x90)) & 0xfff0 == 0x1130 or (*(0x18060000 + 0x90)) & 0xfff0 == 0x0150 or
            # (*(0x18060000 + 0x90)) & 0xfff0 == 0x1150
            mmio_name = 'ath79_reset_rr'
            mmio_base = eval('(0x18060000 + 0x90)')
            firmware.insert_bamboo_devices(mmio_base, 0x4, value=0x00b0) # ar9130
        elif caller == '__mips_cpu_irq_init':
            # domain = irq_domain_add_legacy(of_node, 8, 0, 0, &mips_cpu_intc_irq_domain_ops, ((void *)0))
            # from builtin function will never be panic
            pass
        else:
            analysis.warning(firmware, '{} -> panic(w/o handler)'.format(caller), 0)
    elif firmware.uuid == 'ramips_rt3883':
        if caller == 'mips_cpu_intc_init':
            # domain = irq_domain_add_legacy(of_node, 8, 0, 0, &mips_cpu_intc_irq_domain_ops, ((void *)0))
            # from builtin function will never be panic
            pass
        elif caller == 'prom_soc_init':
            # void *sysc = (void *) ((((int)(int)(0x10000000)) & 0x1fffffff) | 0xa0000000);
            # n0 = __raw_readl(sysc + 0x00); n1 = __raw_readl(sysc + 0x04); id = __raw_readl(sysc + 0x0c);
            # if (n0 == 0x38335452 && n1 == 0x20203338) { ... } else { panic("..."); }
            mmio_base = 0x10000000
            firmware.insert_bamboo_devices(mmio_base + 0x00, 0x4, value=0x38335452, compatible=['prom_soc_init1'])
            firmware.insert_bamboo_devices(mmio_base + 0x04, 0x4, value=0x20203338, compatible=['prom_soc_init2'])
        elif caller == 'intc_of_init':
            # irq = irq_of_parse_and_map(node, 0); if (!irq) panic("Failed to get INTC IRQ");
            # from builtin function will never be panic
            # if (of_address_to_resource(node, 0, &res)) panic("Failed to get intc memory range");
            # from builtin function will never be panic
            pass
        elif caller == 'plat_time_init':
            # clk = clk_get_sys("cpu", ((void *)0)); if (IS_ERR(clk)) panic("unable to get CPU clock, err=%ld", PTR_ERR(clk));
            # from builtin function will never be panic
            pass
        elif caller == 'ralink_of_remap':
            # rt_sysc_membase = plat_of_remap_node("ralink,rt3883-sysc");
            # rt_memc_membase = plat_of_remap_node("ralink,rt3883-memc");
            # if (!rt_sysc_membase || !rt_memc_membase) panic("Failed to remap core resources");
            # go into plat_of_remap_node, we found return __ioremap_mode((res.start), (resource_size(&res)), ...)
            # from builtin function will never be panic
            pass
        elif caller == 'plat_of_remap_node':
            # np = of_find_compatible_node(((void *)0), ((void *)0), node); if (!np) panic("Failed to find %s node", node);
            # if (of_address_to_resource(np, 0, &res)) panic("Failed to get resource for %s", node);'
            # from builtin function will never be panic
            pass
        elif caller == 'ralink_clk_add':
            # struct clk *clk = kzalloc(sizeof(struct clk), ((( gfp_t )0x10u) | (( gfp_t )0x40u) | (( gfp_t )0x80u)));
            # if (!clk) panic("failed to add clock");
            # from builtin function will never be panic
            pass
        elif caller == 'plat_of_setup':
            # if (!of_have_populated_dt()) panic("device tree not present");
            # from builtin function will never be panic
            # if (of_platform_populate(((void *)0), of_ids, ((void *)0), ((void *)0))) panic("failed to populate DT");
            # from builtin function will never be panic
            pass
        else:
            analysis.warning(firmware, '{} -> panic(w/o handler)'.format(caller), 0)
    else:
        analysis.warning(firmware, '{} -> panic(w/o handler)'.format(caller), 0)


def _init_r4k_clocksource(analysis, firmware, **kwargs):
    caller = kwargs.pop('caller')
    analysis.info(firmware, '{} -> init_r4k_clocksource(mips internal timer as clock source)'.format(caller), 1)


def ___builtin_unreachable(analysis, firmware, **kwargs):
    # BUG()/BUG_ON() is a very strong mark of exceptional path
    caller = kwargs.pop('caller')
    if caller == 'cpu_probe':
        # __BUG_ON((unsigned long)(!__cpu_name[cpu]));
        # => __cpu_name[cpu] != 0 => c->processor_id & 0xff0000 must be in [...]
        # __BUG_ON((unsigned long)(c->cputype == CPU_UNKNOWN));
        # => c->cputype != CPU_UNKNOWN => c->processor_id & 0xff0000 must be in [...]
        # __BUG_ON((unsigned long)(current_cpu_type() != c->cputype));
        # => c->cputype == __get_cpu_type(cpu_data[0].cputype) => c->processor_id & 0xff0000 must be in [...]
        # => c->processor_id = `inline assembly` = read_cpu_id()
        # NOTE: inline assembly will be replaced in advance
        # I guess this is way too much difficult to analyze so we have to simpify
        # it in advance. From past experiences, we know 1) the situation itself is
        # way too complicated 2) not all kernel source have same pattern 3) suppose
        # we have source, we can obtain CPU/arch/endian from the vmlinux. So, we decide
        # to give it up.
        pass

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
    elif firmware.uuid == 'oxnas_generic':
        if caller == 'cpu_architecture':
            # do {} while(0);
            pass
        elif caller == 'cpu_init':
            # do {} while(0);
            pass
        elif caller == 'gic_cascade_irq':
            # do {} while(0);
            pass
        elif caller == 'rps_of_init':
            # do {} while(0);
            pass
        else:
            analysis.warning(firmware, '{} -> BUG()/BUG_ON() found but no handlers'.format(caller), 0)
    else:
         analysis.warning(firmware, '{} -> BUG()/BUG_ON() found but no handlers'.format(caller), 0)


UNMODELED_SKIP_LIST = [
    'early_init_dt_scan', 'of_flat_dt_get_machine_name', 'of_scan_flat_dt',
    'kmemdup', 'kfree', 'msleep', '__builtin_memcmp', 'add_memory_region', 'detect_memory_region',
    'clk_get_rate', 'clk_put', 'sprintf',  '__udelay',
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
    'paging_init', 'device_tree_init', 'strlcat', 'set_isa', 'decode_configs', 'spram_config',
    'setup_early_printk', 'cpu_probe', 'cp0_compare_irq', 'c0_compare_int_usable',
    'clockevent_delta2ns', 'clocks_calc_mult_shift', 'get_c0_compare_int', 'irq_modify_status',
    'cpu_has_mfc0_count_bug', 'debugfs_create_file', 'of_find_compatible_node', 'of_platform_populate',
    'reset_controller_register', 'early_init_dt_verify', 'of_flat_dt_match_machine', 'sanity_check_meminfo',
    'setup_processor', 'request_standard_resources', 'smp_build_mpidr_hash', 'setup_machine_fdt', 'parse_early_param',
    'sanity_check_meminfo', 'arm_memblock_init', 'unflatten_device_tree', 'arm_dt_init_cpu_maps',
    'init_static_idmap', 'ptrace_break_init', 'twd_clk_init', 'atomic_pool_init', 'exceptions_init', 'proc_cpu_init', 'alignment_init',
    'early_init_fdt_scan_reserved_mem', 'early_init_fdt_scan_reserved_mem', 'of_count_phandle_with_args',
    'of_property_read_u32_index', 'of_parse_phandle_with_args', 'mips_set_machine_name'
    'early_init_fdt_reserve_self', 'of_property_count_elems_of_size', 'of_find_property', 'of_property_read_variable_u32_array',
    'warn_slowpath_null', 'vprintk', 'mutex_lock', 'of_get_cpu_node', 'mips_sysrq_init', 'pcibios_set_cache_line_size'
]


MODELED_SKIP_TABLE = {
    'irq_set_chip_and_handler_name': {'handle': _irq_set_chip_and_handler_name},
    '__irq_set_handler': {'handle': ___irq_set_handler},
    'panic': {'handle': _panic},
    'init_r4k_clocksource': {'handle': _init_r4k_clocksource},
    '__builtin_unreachable': {'handle': ___builtin_unreachable},
    'clockevents_register_device': {'handle': _clockevents_register_device},
    'setup_irq': {'handle': _setup_irq},
    'clk_get_sys': {'handle': _clk_get_sys},
    'clkdev_add': {'handle': _clkdev_add},
}
