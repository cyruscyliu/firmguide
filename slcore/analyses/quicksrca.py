from slcore.analysis import Analysis


generic_fcbs = {
    'plat_irq_dispatch': {'ignored': True},
    'of_irq_init': {'ignored': False},
    'irq_set_chip_and_handler_name': {'ignored': False},
    'irq_set_chained_handler_and_data': {'ignored': False},
    'irq_domain_add_legacy': {'ignored': False},
    '__irq_domain_add': {'ignored': False},
    'panic': {'ignored': True},
    'r4k_clockevent_init': {'ignored': True},
    'init_r4k_clocksource': {'ignored': True},
    'mips_cpu_irq_init': {'ignored': True},
    '__irq_set_handler': {'ignored': False},
    'irq_domain_add_simple': {'ignored': False},
    'of_clk_init': {'ignored': True},
    'set_handle_irq': {'ignored': False},
}


class QuickSrcA(Analysis):
    def __init__(self, analysis_manager):
        super().__init__(analysis_manager)

        self.name = 'quicksrca'
        self.description = 'Quick source code analysis.'

    def run(self, firmware, **kwargs):
        ep = kwargs.pop('ep', None)
        caller = kwargs.pop('caller', 'unknown')
        cfcfg = kwargs.pop('cgcfg', False)

        # We simply preprocess the c file containing
        # the entry point if no other arguments assigned.
        srcodec = firmware.srcodec

        # 1 symbol2file
        path_to_entry_point = srcodec.symbol2file(ep)
        if path_to_entry_point is None:
            path_to_entry_point = srcodec.symbol2fileg(ep)
            if path_to_entry_point is None:
                self.info(firmware, 'cannot find {}'.format(ep), 0)
                return False
        self.info(
            firmware, 'find {} in {}'.format(ep, path_to_entry_point), 1)
        cmdline = srcodec.get_cmdline(path_to_entry_point)
        path_to_pentry_point = \
            srcodec.preprocess(path_to_entry_point, cmdline=cmdline)
        self.info(firmware,  'preprocess and save as {}/{}'.format(
            srcodec.get_path_to_source_code(), path_to_pentry_point))

        if cfcfg:
            srcodec.traverse_funccalls2([ep], caller=caller, fcbs=generic_fcbs)
        return True
