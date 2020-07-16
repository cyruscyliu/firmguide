from slcore.database.dbf import get_database
from slcore.dt_parsers.mmio import find_mmio_by_path
from slcore.dt_parsers.intc import \
    find_interrupt_parent_by_path, find_irqnc_by_pphandle
from slcore.dt_parsers.compatible import find_compatible_by_path
from slcore.dt_parsers.common import load_dtb

# so we don't need to update builtin miscs manually
builtin_miscs = list(get_database('qemu.misc').select('*').keys())


def __is_misc(dts, path):
    if dts.exist_property('compatible', path):
        for cmptbl in dts.get_property('compatible', path).data:
            if cmptbl in builtin_miscs:
                # yes, this is a misc
                return True
    return False


def find_flatten_misc_in_fdt(dts):
    """Find miscs in a machine.

    Args:
        dts(dts): The dts from load_dtb.
        intc(bool): Whether or not returns the miscs which are free running. Default is False.

    Returns:
        list: A list of miscs in the machine. For example:
        [{'compatible': ['example,misc'], 'path': /example/misc,
        'regs': [{'base': 0xFFFF0000, 'size': 0x10000}],
        'intcp': -1, 'irqns': [0]}]
    """
    flatten_miscs = {}
    for pa, no, pros in dts.walk():
        if not __is_misc(dts, pa):
            continue
        compatible = find_compatible_by_path(dts, pa)
        flatten_miscs[pa] = {'compatible': compatible}

        mmio = find_mmio_by_path(dts, pa)
        if mmio is not None:
            flatten_miscs[pa]['regs'] = mmio['regs']

        if dts.exist_property('interrupts', pa):
            interrupt_parent = find_interrupt_parent_by_path(dts, pa)
            interrupts = dts.get_property('interrupts', pa).data
            irqns = find_irqnc_by_pphandle(dts, interrupt_parent, interrupts)
            flatten_miscs[pa]['intcp'] = interrupt_parent
            flatten_miscs[pa]['irqns'] = irqns

    ft = []
    for k, v in flatten_miscs.items():
        v['path'] = k
        ft.append(v)

    return ft


def find_flatten_misc(path_to_dtb):
    """Find the miscs in a machine.

    Args:
        path_to_dtb(str): The path to the device tree blob.

    Returns:
        list: A list of misc chips.
    """
    dts = load_dtb(path_to_dtb)
    return find_flatten_misc_in_fdt(dts)
