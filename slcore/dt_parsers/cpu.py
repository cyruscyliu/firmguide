import fdt


def find_flatten_cpu_in_fdt(dts):
    """
    Return the first one, because they are all same.
    """
    path_to_cpu = '/cpus/cpu@0'
    compatible = dts.get_property('compatible', path_to_cpu).data
    return [{'path': path_to_cpu, 'compatible': compatible}]

