import fdt

def find_compatible_in_fdt(dts):
    compatible = dts.get_property('compatible', '/').data
    return compatible

def find_compatible(path_to_dtb):
    if path_to_dtb is None:
        return

    with open(path_to_dtb, 'rb') as f:
        dtb = f.read()
    dts = fdt.parse_dtb(dtb)

    return find_compatible_in_fdt(dts)

