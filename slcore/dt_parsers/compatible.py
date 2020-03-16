from slcore.dt_parsers.common import load_dtb
import os


def find_compatible_in_fdt(dts):
    """Find the compatible of a machine.

    Args:
        dts(dts): The dts from load_dtb.

    Returns:
        list: The compatible of the machine.
    """
    compatible = dts.get_property('compatible', '/').data
    return compatible


def find_compatible(path_to_dtb):
    """Find the compatible of a machine.

    Args:
        dtb(str): The path to the device tree blob.

    Returns:
        list: The compatible of the machine.
    """
    if path_to_dtb is None:
        return

    dts = load_dtb(path_to_dtb)
    return find_compatible_in_fdt(dts)


def find_compatible_by_path(dts, path):
    """Find compatible by a path in a recursive manner.

    Args:
        dts(dts): The dts from load_dtb.

    Returns:
        list: The compatible of the path.
    """
    compatible = dts.get_property('compatible', path)
    if compatible is None:
        pnode = dts.get_node(path).parent
        ppath = os.path.join(pnode.path, pnode.name)
        return find_compatible_by_path(dts, ppath)
    else:
        return compatible.data

