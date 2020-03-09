import os

from slcore.dt_parsers.flash import find_flatten_flash_in_fdt
from slcore.dt_parsers.mmio import find_flatten_mmio_in_fdt
from slcore.dt_parsers.common import load_dtb


def project_show_dtinfo(path_to_dtb, **kwargs):
    mmio = kwargs.pop('mmio', False)
    flash = kwargs.pop('flash', False)

    dts = load_dtb(path_to_dtb)
    path_to_dts = path_to_dtb + '.dts'
    with open(path_to_dts, 'w') as f:
        f.write(dts.to_dts())

    if mmio:
        mmios = []
        for mmio in find_flatten_mmio_in_fdt(dts):
            if len(mmio['regs']):
                mmios.append(mmio)
        for mmio in sorted(mmios, key=lambda x: x['regs'][0]['base']):
            for reg in mmio['regs']:
                print('[+] [MMIO] base 0x{:08x} size 0x{:08x} of {}/{}'.format(reg['base'], reg['size'], mmio['path'], mmio['compatible']))

    if flash:
        for flash in find_flatten_flash_in_fdt(dts):
            for reg in flash['regs']:
                print('[+] [FLASH] base 0x{:08x} size 0x{:08x} of {}/{}'.format(reg['base'], reg['size'], flash['path'], flash['compatible']))

    print('[+] save dts at {}'.format(path_to_dts))
