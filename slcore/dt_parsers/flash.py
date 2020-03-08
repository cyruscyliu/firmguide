from slcore.database.dbf import get_database
from slcore.dt_parsers.common import load_dtb
from slcore.dt_parsers.mmio import find_mmio_by_path
from slcore.dt_parsers.compatible import find_compatible_by_path


# so we don't need to update builtin_flashes manually
builtin_flashes = list(get_database('qemu.flash').select('*').keys())


def __is_flash(dts, path):
    if dts.exist_property('compatible', path):
        for cmptbl in dts.get_property('compatible', path).data:
            if cmptbl in builtin_flashes:
                # yes, this is a flash
                return True
            if cmptbl.find('flash') != -1:
                # yes, this is a flash
                return True
    return False


def find_flatten_flash_in_fdt(dts):
    """Find the flashes in a machine.

    Args:
        dts(dts): The dts from load_dtb.

    Returns:
        list: A list of flash chips. For example:
        [{'compatible': ['example,compatible'], path: /example/flash,
        regs: [{'base': 0xFFFF0000, 'size': 0x10000}]},]
    """
    flatten_flashs = {}
    for pa, no, pros in dts.walk():
        if not __is_flash(dts, pa):
            continue
        compatible = find_compatible_by_path(dts, pa)
        flatten_flashs[pa] = {'compatible': compatible}

        mmio = find_mmio_by_path(dts, pa)
        if mmio is not None:
            flatten_flashs['regs'] = mmio['regs']
        else:
            continue

    ft = []
    for k, v in flatten_flashs.items():
        v['path'] = k
        ft.append(v)

    return ft


def find_flatten_flash(path_to_dtb):
    """Find the flashes in a machine.

    Args:
        path_to_dtb(str): The path to the device tree blob.

    Returns:
        list: A list of flash chips.
    """
    dts = load_dtb(path_to_dtb)
    return find_flatten_flash_in_fdt(dts)

