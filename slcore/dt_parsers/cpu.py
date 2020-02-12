import fdt


def find_cpu_in_fdt(dts):
    path_to_cpu = '/cpus/cpu@0'
    compatible = self.dts.get_property('compatible', path_to_cpu).data[0]
    return compatible

def find_cpu(path_to_dtb):
    if path_to_dtb is None:
        return

    with open(path_to_dtb, 'rb') as f:
        dtb = f.read()
    dts = fdt.parse_dtb(dtb)

    return find_cpu_in_fdt(dts)

