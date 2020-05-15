from slcore.dt_parsers.flash import find_flatten_flash_in_fdt
from slcore.dt_parsers.mmio import find_flatten_mmio_in_fdt
from slcore.dt_parsers.common import load_dtb
from slcore.amanager import Analysis


class DiscloseDT(Analysis):
    def __init__(self, analysis_manager):
        super().__init__(analysis_manager)

        self.name = 'disclosedt'
        self.description = 'Disclose device tree blob.'

    def run(self, firmware, **kwargs):
        path_to_dtb = kwargs.pop(
            'dtb', firmware.get_components().get_path_to_dtb())
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
            for mmio in sorted(
                    mmios, key=lambda x: x['regs'][0]['base']):
                for reg in mmio['regs']:
                    message =  \
                        '[MMIO] base 0x{:08x} size 0x{:08x} of {}/{}'.format(
                            reg['base'], reg['size'],
                            mmio['path'], mmio['compatible'])
                    self.info(firmware, message, 1)
        if flash:
            for flash in find_flatten_flash_in_fdt(dts):
                for reg in flash['regs']:
                    message = \
                        '[FLASH] base 0x{:08x} size 0x{:08x} of {}/{}'.format(
                            reg['base'], reg['size'],
                            flash['path'], flash['compatible'])
                    self.info(firmware, message, 1)

        self.info(firmware, 'save dts at {}'.format(path_to_dts), 1)
        return True
