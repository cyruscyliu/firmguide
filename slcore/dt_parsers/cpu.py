from slcore.dt_parsers.common import load_dtb
from slcore.dt_parsers.compatible import find_compatible_by_path
from slcore.dt_parsers.mmio import find_mmio_by_path


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
        compatible = compatible.data

    # TODO this is an ugly implementation
    gic_reg = None
    if 'arm,cortex-a9' in compatible:
        for path, _, _ in dts.walk():
            c = find_compatible_by_path(dts, path)
            if 'arm,cortex-a9-scu' in c:
                gic_regs = find_mmio_by_path(dts, path)['regs']
                break
    if gic_regs:
        return [{'path': path_to_cpu, 'compatible': compatible, 'regs': gic_regs}]
    else:
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

