from slcore.dt_parsers.common import load_dtb


def find_flatten_cpu_in_fdt(dts):
    """Find the first cpu in a machine.

    Return the first one, because they are all same.

    Args:
        dts(dts): The dts from load_dtb.

    Returns:
        list: A list of cpus in the machine. For example:
        [{compatible': ['example,cpu'], 'path': /cpus/cpu@0,}]
    """
    path_to_cpu = None
    for p, ns, pros in dts.walk():
        if not p.startswith('/cpus/cpu@'):
            continue
        path_to_cpu = p

    if path_to_cpu is None:
        return None
    compatible = dts.get_property('compatible', path_to_cpu)
    if compatible is None:
        return None
    else:
        compatible == compatible.data
    return [{'path': path_to_cpu, 'compatible': compatible}]


def find_flatten_cpu(path_to_dtb):
    """Find the first cpu in a machine.

    Args:
        path_to_dtb(str): The path to the device tree blob.

    Returns:
        list: A list of cpus in the machine.
    """
    dts = load_dtb(dtb)
    return find_flatten_cpu_in_fdt(dts)

