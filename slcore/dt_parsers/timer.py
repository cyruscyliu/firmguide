from slcore.database.dbf import get_database
from slcore.dt_parsers.mmio import find_mmio_by_path
from slcore.dt_parsers.intc import \
    find_interrupt_parent_by_path, find_irqnc_by_pphandle
from slcore.dt_parsers.compatible import find_compatible_by_path
from slcore.dt_parsers.common import load_dtb

# so we don't need to update builtin timers manually
builtin_timers = list(get_database('qemu.timer').select('*').keys())


def __is_timer(dts, path):
    if dts.exist_property('compatible', path):
        for cmptbl in dts.get_property('compatible', path).data:
            if cmptbl in builtin_timers:
                # yes, this is a timer
                return True
            if cmptbl.find('timer') != -1:
                # yes, this is a timer
                return True
    return False


def find_flatten_timer_in_fdt(dts, intc=True):
    """Find timers in a machine.

    Args:
        dts(dts): The dts from load_dtb.
        intc(bool): Whether or not returns the timers which are free running. Default is False.

    Returns:
        list: A list of timers in the machine. For example:
        [{'compatible': ['example,timer'], 'path': /example/timer,
        'regs': [{'base': 0xFFFF0000, 'size': 0x10000}],
        'intcp': -1, 'irqns': [0]}]
    """
    flatten_timers = {}
    for pa, no, pros in dts.walk():
        if not __is_timer(dts, pa):
            continue
        compatible = find_compatible_by_path(dts, pa)
        flatten_timers[pa] = {'compatible': compatible}

        mmio = find_mmio_by_path(dts, pa)
        if mmio is not None:
            flatten_timers[pa]['regs'] = mmio['regs']

        if dts.exist_property('interrupts', pa):
            interrupt_parent = find_interrupt_parent_by_path(dts, pa)
            interrupts = dts.get_property('interrupts', pa).data
            irqns = find_irqnc_by_pphandle(dts, interrupt_parent, interrupts)
            flatten_timers[pa]['intcp'] = interrupt_parent
            flatten_timers[pa]['irqns'] = irqns

        if not intc and 'intcp' not in flatten_timers[pa]:
            # by default we don't return the timers which are free running
            flatten_timers.pop(pa)

    ft = []
    for k, v in flatten_timers.items():
        v['path'] = k
        ft.append(v)

    return ft


def find_flatten_timer(path_to_dtb):
    """Find the timers in a machine.

    Args:
        path_to_dtb(str): The path to the device tree blob.

    Returns:
        list: A list of timer chips.
    """
    dts = load_dtb(path_to_dtb)
    return find_flatten_timer_in_fdt(dts)
