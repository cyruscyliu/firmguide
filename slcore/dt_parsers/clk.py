from slcore.database.dbf import get_database
from slcore.dt_parsers.mmio import find_mmio_by_path
from slcore.dt_parsers.intc import \
    find_interrupt_parent_by_path, find_irqnc_by_pphandle
from slcore.dt_parsers.compatible import find_compatible_by_path
from slcore.dt_parsers.common import load_dtb

# so we don't need to update builtin clks manually
builtin_clks = list(get_database('qemu.clk').select('*').keys())


def __is_clk(dts, path):
    if dts.exist_property('compatible', path):
        for cmptbl in dts.get_property('compatible', path).data:
            if cmptbl in builtin_clks:
                # yes, this is a clk
                return True
            if cmptbl.find('clk') != -1:
                # yes, this is a clk
                return True
    return False


def find_flatten_clk_in_fdt(dts):
    """Find clks in a machine.

    Args:
        dts(dts): The dts from load_dtb.

    Returns:
        list: A list of clks in the machine. For example:
        [{'compatible': ['example,clk'], 'path': /example/clk}]
    """
    flatten_clks = {}
    for pa, no, pros in dts.walk():
        if not __is_clk(dts, pa):
            continue
        compatible = find_compatible_by_path(dts, pa)
        flatten_clks[pa] = {'compatible': compatible}

    ft = []
    for k, v in flatten_clks.items():
        v['path'] = k
        ft.append(v)

    return ft


def find_flatten_clk(path_to_dtb):
    """Find the clks in a machine.

    Args:
        path_to_dtb(str): The path to the device tree blob.

    Returns:
        list: A list of clk chips.
    """
    dts = load_dtb(path_to_dtb)
    return find_flatten_clk_in_fdt(dts)
