from slcore.analyses.analysis import Analysis
from slcore.dt_parsers.common import load_dtb
from slcore.dt_parsers.mmio import find_flatten_mmio_in_fdt
from slcore.dt_parsers.memory import find_memory_in_fdt

import os


class DTPreprocessing(Analysis):
    def run(self, firmware):
        path_to_dtb = firmware.get_dtb()
        if path_to_dtb is None:
            return True

        # 1. load the dtb
        dts = load_dtb(path_to_dtb)
        path_to_dts = os.path.join(firmware.get_target_dir(), '{}.dts'.format(os.path.basename(path_to_dtb)))
        with open(path_to_dts, 'w') as f:
            f.write(dts.to_dts())
        self.info(firmware, 'dtb at {}'.format(path_to_dtb), 1)
        self.info(firmware, 'dts at {}'.format(path_to_dts), 1)

        firmware.set_machine_name(firmware.get_uuid())

        # 2. create bdevices
        mmios = []
        mmio_c = 0
        for mmio in find_flatten_mmio_in_fdt(dts):
            for reg in mmio['regs']:
                mmio_c += 1
                mmios.append({'base': reg['base'], 'size': reg['size'], 'value': 0, 'compatible': mmio['compatible']})

        mmios = sorted(mmios, key=lambda k: k['base'])
        for reg in mmios:
            # TODO
            if reg['compatible'] == ['marvell,orion-mdio']:
                continue
            status = firmware.insert_bamboo_devices(
                reg['base'], reg['size'],
                value=0, compatible=reg['compatible'])
            self.debug(firmware, 'update base 0x{:08x} size 0x{:04x} of {} {}'.format(
                reg['base'], reg['size'], reg['compatible'], status), 1)
        firmware.update_bamboo_devices()
        self.debug(firmware, 'recognize {} mmio regions'.format(mmio_c), 1)

        # 3. assign board_id
        firmware.set_board_id('0xFFFFFFFF')

        # 4. check the memory size
        memory = find_memory_in_fdt(dts)
        if memory is not None and len(memory['regs']) > 0:
            ram_size = memory['regs'][0]['size']
            if ram_size > 0:
                firmware.set_ram_size(hex(ram_size))
                self.info(firmware, 'update ram size to {} MiB'.format(ram_size // 0x100000), 1)

        return True

    def __init__(self, analysis_manager):
        super().__init__(analysis_manager)
        self.name = 'preprocdt'
        self.description = 'preprocess the device tree file'
        self.required = ['mfilter']
        self.critical = False

