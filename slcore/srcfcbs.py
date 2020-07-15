from slcore.analyses.ofinitsrc import search_cb
from slcore.dt_parsers.common import load_dtb
from slcore.dt_parsers.intc import find_flatten_intc_in_fdt
from slcore.dt_parsers.timer import find_flatten_timer_in_fdt
from slcore.srcodecontroller import load_system_map


def __of_irq_init_handler(self, caller, extend=[]):
    """
    This is an indirect-call-like function that calls 
    callbacks of registerd interrupt controllers.
    """
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


def __clocksource_of_init_handler(self, caller, extend=[]):
    """
    This is an indirect-call-like function that calls 
    callbacks of registerd timers.
    """
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
    timers = find_flatten_timer_in_fdt(dts)

    for timer in timers:
        for cmptb in timer['compatible']:
            for triple, path in search_cb(cmptb, path_to_source):
                if triple[2] not in extend:
                    extend.append(triple[2])
    return True


def __kernel_thread_handler(self, caller, extend=[]):
    """
    Ugly implementation because we cannot get meaningful arguments of
    functions due to the IR level parser(not AST level).
    """
    if caller == 'rest_init':
        if not hasattr(self, 'kernel_thread'):
            self.kernel_thread = 1
            extend.append('kernel_init')
        else:
            if self.kernel_thread == 1:
                extend.append('kthreadd')
        return True
    return False


def __do_one_initcall_handler(self, caller, extend=[]):
    """
    Linux kernel has several initcall prefixs, "early",
    "core", "postcore", "arch", "subsys", "fs", "device", "late".
    """
    srcodec = self.analysis_manager.srcodec
    if not srcodec.supported:
        self.error_info = 'please set the source code'
        return False

    if srcodec.system_map is None:
        srcodec.system_map = load_system_map(srcodec.path_to_source_code)
    system_map = srcodec.system_map

    funccalls = []
    for symbol, v in system_map.items():
        ep = None
        if symbol.startswith('__initcall') and \
                symbol.find('start') == -1 and \
                symbol.find('end') == -1:
            # example1: __initcall_ath79_setup3
            ep = symbol[11:]
            if ep[-1] in ['0', '1', '2', '3', '4', '5', '6', '7']:
                ep = ep[:-1]
            if ep[-2:] in ['1s', '2s', '3s', '4s', '5s', '6s', '7s']:
                ep = ep[:-2]
            # example2: populate_rootfsrootfs
            if ep.endswith('rootfs'):
                ep = ep[:-6]
            # example3: spawn_ksoftirqdearly
            if ep.endswith('early'):
                ep = ep[:-5]
            extend.append(ep)
    return True


generic_fcbs = {
    'plat_irq_dispatch': {'ignored': True},
    'of_irq_init': {'handler': __of_irq_init_handler},
    'clocksource_of_init': {'handler': __clocksource_of_init_handler},
    'kernel_thread': {'handler': __kernel_thread_handler},
    'irq_set_chip_and_handler_name': {},
    'irq_set_chained_handler_and_data': {},
    'irq_domain_add_legacy': {},
    '__irq_domain_add': {},
    'r4k_clockevent_init': {'ignored': True},
    'init_r4k_clocksource': {'ignored': True},
    'mips_cpu_irq_init': {'ignored': True},
    '__irq_set_handler': {},
    'irq_domain_add_simple': {},
    'of_clk_init': {},
    'set_handle_irq': {},
    'setup_arch': {'intermediate': True},
    'init_IRQ': {'intermediate': True},
    'irqchip_init': {'intermediate': True},
    'time_init': {'intermediate': True},
    'rest_init': {'intermediate': True},
    'kernel_init': {'intermediate': True},
    'kernel_init_freeable': {'intermediate': True},
    'do_basic_setup': {'intermediate': True},
    'do_initcalls': {'intermediate': True},
    'do_initcall_level': {'intermediate': True},
    'do_one_initcall': {'handler': __do_one_initcall_handler},
}
