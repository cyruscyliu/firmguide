from slcore.project import project_get_srcodec

generic_fcbs = {
    'plat_irq_dispatch':{ 'ignored': True },
    'of_irq_init': { 'ignored': False, },
    'irq_set_chip_and_handler_name': { 'ignored': False },
    'irq_set_chained_handler_and_data': { 'ignored': False },
    'irq_domain_add_legacy': { 'ignored': False },
    '__irq_domain_add': { 'ignored': False },
    'panic': { 'ignored': True },
    'of_clk_init': { 'ignored': True },
    'r4k_clockevent_init': { 'ignored': True },
    'init_r4k_clocksource': { 'ignored': True },
    'mips_cpu_irq_init': { 'ignored': True },
    '__irq_set_handler': { 'ignored': False },
    'irq_domain_add_simple': { 'ignored': False },
    'of_clk_init': { 'ignored': True }
}

def project_source_analysis(ep, **kwargs):
    """
    We simply preprocess the c file containing the entry point
    if no other arguments assigned.
    """
    srcodec = project_get_srcodec()

    # 1 symbol2file
    path_to_entry_point = srcodec.symbol2file(ep)
    if path_to_entry_point is None:
        path_to_entry_point = srcodec.symbol2fileg(ep)
        if path_to_entry_point is None:
            print('[-] cannot find {}'.format(ep))
            return
    print('[+] find {} in {}'.format(ep, path_to_entry_point))
    cmdline = srcodec.get_cmdline(path_to_entry_point)
    path_to_pentry_point = srcodec.preprocess(path_to_entry_point, cmdline=cmdline)
    print('[+] preprocess and save as {}/{}'.format(srcodec.get_path_to_source_code(), path_to_pentry_point))

    caller = kwargs.pop('caller', 'unknown')

    # ===== intc subsystem =====
    # 1. get_irqnr_and_base/plat_irq_dispatch(not neccesory)
    # For ARM, we have get_irqnr_preamble, get irqnr_and_base
    # which together are also named arch_irq_handler_default after ?(at least >2.16)
    # and handler_arch_irq which is a global function pointer which is
    # defined by set_handle_irq separately.
    # For MIPS, you can skip plat_irq_dispatch because it is very general.
    # Mostly, timer interrupt is IRQ7 and you won't be worry about it.
    # 2 intc initilization
    # ep = 'init_IRQ'
    # srcodec.traverse_funccalls2([ep], caller='start_kernel', fcbs=fcbs)
    # fcbs = ath79_fcbs
    # fcbs = bcm63xx_fcbs
    cfcfg = kwargs.pop('cgcfg', False)
    if cfcfg:
        srcodec.traverse_funccalls2([ep], caller=caller, fcbs=generic_fcbs)


