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
    else:
         analysis.warning(firmware, '{} -> BUG()/BUG_ON() found but no handlers'.format(caller), 0)


def _platform_device_register(analysis, firmware, **kwargs):
    # [FUNCTION] int platform_device_register(struct platform_de:vice *);
    # [STRUCT] platform_devcie, resource, plat_serial8250_port
    caller = kwargs.pop('caller')
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
            analysis.info(firmware, 'get uart name {}'.format(uart_name), 1)
            analysis.info(firmware, 'get uart mmio base {} size {}'.format(hex(uart_mmio_base), hex(uart_mmio_size)), 1)
            analysis.info(firmware, 'get uart irq {}'.format(uart_irqn), 1)
            analysis.info(firmware, 'get uart reg shift {}'.format(uart_reg_shift), 1)
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
            analysis.info(firmware, 'get mmio base {} size {}'.format(hex(mmio_base), hex(mmio_size)), 1)
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
            analysis.info(firmware, 'get mmio base {} size {}'.format(hex(mmio_base), hex(mmio_size)), 1)
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
            analysis.info(firmware, 'get mmio base {} size {}'.format(hex(mmio_base), hex(mmio_size)), 1)
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
            analysis.info(firmware, 'get mmio base {} size {}'.format(hex(mmio_base), hex(mmio_size)), 1)
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
            analysis.info(firmware, 'get flash base {} size {}'.format(hex(flash_base), hex(flash_size)), 1)
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
            analysis.info(firmware, 'get mmio base {} size {}'.format(hex(mmio_base), hex(mmio_size)), 1)
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
            analysis.info(firmware, 'get mmio base {} size {}'.format(hex(mmio_base), hex(mmio_size)), 1)
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
            analysis.info(firmware, 'get mmio base {} size {}'.format(hex(mmio_base), hex(mmio_size)), 1)
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
            analysis.info(firmware, 'get mmio base {} size {}'.format(hex(mmio_base), hex(mmio_size)), 1)
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
            analysis.info(firmware, 'get mmio base {} size {}'.format(hex(mmio_base), hex(mmio_size)), 1)
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
            analysis.info(firmware, 'get mmio base {} size {}'.format(hex(mmio_base), hex(mmio_size)), 1)
        else:
            analysis.warning(firmware, 'platform_device_register found but no handlers', 0)
    else:
        analysis.warning(firmware, 'platform_device_register found but no handlers', 0)


def _platform_device_register_full(analysis, firmware, **kwargs):
    # [FUNCTION] platform_device_register_full
    caller = kwargs.pop('caller')
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
            analysis.info(firmware, 'get mmio base {} size {}'.format(hex(mmio_base), hex(mmio_size)), 1)
        else:
            analysis.warning(firmware, 'platform_device_register_full found but no handlers', 0)
    else:
        analysis.warning(firmware, 'platform_device_register_full found but no handlers', 0)


def _platform_device_alloc(analysis, firmware, **kwargs):
    # [FUNCIIONS] platform_device_alloc, platform_device_add_data, platform_device_add(pdev);
    caller = kwargs.pop('caller')
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
            analysis.warning(firmware, 'platform_device_register_full found but no handlers', 0)
    else:
        analysis.warning(firmware, 'platform_device_register_full found but no handlers', 0)



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
    'paging_init', 'device_tree_init', 'strlcat', 'set_isa', 'decode_configs', 'spram_config',
    # some functions we think are not neccessory to be analyzed
    'prom_init', 'setup_early_printk', 'cpu_probe'
]


MODELED_SKIP_TABLE = {
    'irq_modify_status': {'handle': _default},
    'irq_set_chip_and_handler_name': {'handle': _irq_set_chip_and_handler_name},
    '__irq_set_handler': {'handle': ___irq_set_handler},
    'irq_domain_add_legacy': {'handle': _irq_domain_add_legacy},
    '__ioremap': {'handle': ___ioremap},
    'panic': {'handle': _panic},
    'r4k_clockevent_init': {'handle': _r4k_clockevent_init},
    'init_r4k_clocksource': {'handle': _init_r4k_clocksource},
    '__builtin_unreachable': {'handle': ___builtin_unreachable},
    'platform_device_register': {'handle': _platform_device_register},
    'platform_devcie_register_full': {'handle': _platform_device_register_full},
    'platform_device_alloc': {'handle': _platform_device_alloc},
    'platform_device_add_data': {'handle': _default},
    'platform_device_add': {'handle': _default},
}


