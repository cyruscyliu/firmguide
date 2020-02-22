from analyses.analysis import Analysis
from slcore.dt_parsers.common import load_dtb
from slcore.dt_parsers.mmio import find_flatten_mmio_in_fdt

import os


class DTPreprocessing(Analysis):
    def run(self, firmware):
        path_to_dtb = firmware.get_dtb()
        if path_to_dtb is None:
            return True

        # 1. load the dtb
        dts = load_dtb(path_to_dtb)
        with open(os.path.join(
                firmware.get_target_dir(),
                '{}.dts'.format(os.path.basename(path_to_dtb))), 'w') as f:
            f.write(dts.to_dts())

        # 2. create bdevices
        for mmio in find_flatten_mmio_in_fdt(dts):
            for reg in mmio['reg']:
                firmware.insert_bamboo_devices(
                    reg['base'], reg['size'],
                    value=0, compatible=mmio['compatible'])
                self.info(firmware, 'update base 0x{:08x} size 0x{:04x} of {}'.format(
                    reg['base'], reg['size'], mmio['compatible']), 1)
        firmware.update_bamboo_devices()

        # 3. assign board_id
        firmware.set_board_id('0xFFFFFFFF')
        return True

    def __init__(self, analysis_manager):
        super().__init__(analysis_manager)
        self.name = 'preprocdt'
        self.description = 'preprocess the device tree file'
        self.required = ['mfilter']
        self.critical = False

