from slcore.analyses.ofinitsrc import search_cb
from slcore.dt_parsers.common import load_dtb
from slcore.dt_parsers.intc import find_flatten_intc_in_fdt
from slcore.dt_parsers.timer import find_flatten_timer_in_fdt
from slcore.dt_parsers.clk import find_flatten_clk_in_fdt
from slcore.srcodecontroller import load_system_map


temp_of_init_table = {
    'mti,cpu-interrupt-controller': 'mips_cpu_intc_init',
    'ralink,rt2880-intc': 'intc_of_init',
    # 'ralink,rt2880-timer': 'rt_timer_probe', # in do_initcall
}


def __generic_of_init_handler(self, find, extend=[]):
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
    periphs = find(dts)

    for periph in periphs:
        for cmptb in periph['compatible']:
            for triple, path in search_cb(cmptb, path_to_source):
                if triple[2] not in extend:
                    extend.append(triple[2])

    for periph in periphs:
        for cmptb in periph['compatible']:
            if cmptb in temp_of_init_table:
                extend.append(temp_of_init_table[cmptb])
    return True


def __of_irq_init_handler(self, func, caller, extend=[], pos={}):
    return __generic_of_init_handler(self, find_flatten_intc_in_fdt, extend=extend)


def __clocksource_of_init_handler(self, func, caller, extend=[], pos={}):
    return __generic_of_init_handler(self, find_flatten_timer_in_fdt, extend=extend)


def __of_clk_init_handler(self, func, caller, extend=[], pos={}):
    return __generic_of_init_handler(self, find_flatten_clk_in_fdt, extend=extend)


def __kernel_thread_handler(self, func, caller, extend=[], pos={}):
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


def __do_one_initcall_handler(self, func, caller, extend=[], pos={}):
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


def __generic_slicing_handler(self, func, caller, extend=[], pos={}):
    if func not in self.slicing:
        self.slicing[func] = {}

    import copy
    self.slicing[func][len(self.slicing[func])] = copy.copy(pos)

    return True


generic_fcbs = {
    # interrupt controller
    'of_irq_init': {'handler': __of_irq_init_handler},  # indirect call
    'irq_domain_add_simple': {'handler': __generic_slicing_handler},  # args::ops->map
    'irq_domain_add_legacy': {'handler': __generic_slicing_handler},  # args::ops->map
    'irq_domain_add_linear': {'handler': __generic_slicing_handler},  # args::ops->map
    '__irq_domain_add': {'handler': __generic_slicing_handler},  # args::ops->map
    '__irq_set_handler': {'handler': __generic_slicing_handler},  # args::handle
    'irq_set_chained_handler': {'handler': __generic_slicing_handler}, # args::handle
    'irq_set_chip_and_handler_name': {'handler': __generic_slicing_handler},  # args::handle
    'irq_set_chained_handler_and_data': {'handler': __generic_slicing_handler},  # args::handle
    'l2x0_of_init': {'handler': __generic_slicing_handler},
    'mips_cpu_irq_init': {},
    # FOR ARM, we have get_irqnr_preamble, get irqnr_and_base that together are also
    # named arch_irq_handler_default after ?(at least >2.16). As for handler_arch_irq,
    # a global function pointer, it is defined by set_handle_irq somewhere..
    'set_handle_irq': {'handler': __generic_slicing_handler}, # args::(*handle_irq) 
    # FOR MIPS, you could skip plat_irq_dispatch because it is very general
    'plat_irq_dispatch': {'ignored': True},
    # clock and timer
    'of_clk_init': {'handler': __of_clk_init_handler}, # indirect call
    'clocksource_of_init': {'handler': __clocksource_of_init_handler},  # indirect call
    'timer_probe': {'handler': __clocksource_of_init_handler},  # indirect call
    'request_percpu_irq': {'handler': __generic_slicing_handler},
    'setup_irq': {'handler': __generic_slicing_handler},
    'clocksource_register_hz': {'handler': __generic_slicing_handler},
    'clocksource_mmio_init': {'handler': __generic_slicing_handler},
    'clocksource_register': {'handler': __generic_slicing_handler},
    '__clocksource_register_scale': {'handler': __generic_slicing_handler},
    'sched_clock_register': {'handler': __generic_slicing_handler},
    'clockevents_config_and_register': {'handler': __generic_slicing_handler},
    'clockevents_register_device': {'handler': __generic_slicing_handler},
    'clk_register': {'handler': __generic_slicing_handler},
    'clk_hw_register': {'handler': __generic_slicing_handler},
    'clk_get_sys': {'handler': __generic_slicing_handler},
    'clkdev_add': {'handler': __generic_slicing_handler},
    'register_current_timer_delay': {'handler': __generic_slicing_handler},
    # initcalls
    'kernel_thread': {'handler': __kernel_thread_handler},  # indirect call
    'do_one_initcall': {'handler': __do_one_initcall_handler},  # indirect call
    # intermediate function
    'setup_arch': {'intermediate': True},
    'init_IRQ': {'intermediate': True},
    'irqchip_init': {'intermediate': True},
    'time_init': {'intermediate': True},
    'mips_clockevent_init': {'intermediate': True},
    'r4k_clockevent_init': {'intermediate': True},
    'init_r4k_clocksource': {'intermediate': True},
    # ignore rest_init until we can handle it
    'rest_init': {'ignored': True, 'intermediate': True},
    'kernel_init': {'intermediate': True},
    'kernel_init_freeable': {'intermediate': True},
    'do_basic_setup': {'intermediate': True},
    'do_initcalls': {'intermediate': True},
    'do_initcall_level': {'intermediate': True},
}
