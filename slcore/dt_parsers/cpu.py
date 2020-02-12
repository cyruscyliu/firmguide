import fdt


def find_cpu_in_fdt(dts):
    """
    Return the first one, because they are all same.
    """
    path_to_cpu = '/cpus/cpu@0'
    compatible = dts.get_property('compatible', path_to_cpu).data
    return {path_to_cpu: {'compatible': compatible}}


def find_cpun_in_fdt(dts):
    pass


def find_cpu(path_to_dtb):
    pass


def find_cpun_in_fdt(dts):
    pass

