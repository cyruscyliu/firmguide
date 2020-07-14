from slcore.analyses.ofinitsrc import search_cb
from slcore.dt_parsers.common import load_dtb
from slcore.dt_parsers.intc import find_flatten_intc_in_fdt


def __of_irq_init_handler(self, caller, extend=[]):
    # This is an indirect-call-like function that calls 
    # callbacks of registerd interrupt controllers.
    srcodec = self.analysis_manager.srcodec
    if not srcodec.supported:
        self.error_info = 'please set the source code'
        return False
    path_to_source = srcodec.get_path_to_source_code()

    path_to_dtb = self.firmware.get_realdtb()
    if path_to_dtb is None:
        self.error_info = 'there is no real dtb available.'
        return False

    dts = load_dtb(path_to_dtb)
    intcs = find_flatten_intc_in_fdt(dts)

    for intc in intcs:
        for cmptb in intc['compatible']:
            for triple, path in search_cb(cmptb, path_to_source):
                if triple[2] not in extend:
                    extend.append(triple[2])
    return True


generic_fcbs = {
    'plat_irq_dispatch': {'ignored': True},
    'of_irq_init': {'handler': __of_irq_init_handler},
    'irq_set_chip_and_handler_name': {},
    'irq_set_chained_handler_and_data': {},
    'irq_domain_add_legacy': {},
    '__irq_domain_add': {},
    'panic': {'ignored': True},
    'r4k_clockevent_init': {'ignored': True},
    'init_r4k_clocksource': {'ignored': True},
    'mips_cpu_irq_init': {'ignored': True},
    '__irq_set_handler': {},
    'irq_domain_add_simple': {},
    'of_clk_init': {},
    'set_handle_irq': {},
    'setup_arch': {'intermediate': True},
    'init_IRQ': {'intermediate': True},
    'time_init': {'intermediate': True},
    'rest_init': {'intermediate': True},
    'irqchip_init': {'intermediate': True}
}
