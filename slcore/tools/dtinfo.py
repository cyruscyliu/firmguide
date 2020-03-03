from slcore.dt_parsers.mmio import find_flatten_mmio_in_fdt
from slcore.dt_parsers.common import load_dtb


def project_show_dtinfo(path_to_dtb, **kwargs):
    mmio = kwargs.pop('mmio', False)

    dts = load_dtb(path_to_dtb)

    if mmio:
        for mmio in find_flatten_mmio_in_fdt(dts):
            for reg in mmio['reg']:
                print('[+] [MMIO] base 0x{:08x} size 0x{:08x} of {}/{}'.format(reg['base'], reg['size'], mmio['path'], mmio['compatible']))
