import fdt


def find_flatten_cpu_in_fdt(dts):
    """
    Return the first one, because they are all same.
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

