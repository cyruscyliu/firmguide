import os

from slcore.amanager import Analysis
from slcore.dt_parsers.common import load_dtb
from slcore.dt_parsers.compatible import find_compatible_in_fdt
from slcore.dt_parsers.serial import find_flatten_serial_in_fdt


class DTPreprocessing(Analysis):
    def run(self, **kwargs):
        path_to_dtb = self.firmware.get_realdtb()
        dts = load_dtb(path_to_dtb)

        path_to_dts = os.path.join(
            self.analysis_manager.project.attrs['path'],
            '{}.dts'.format(os.path.basename(path_to_dtb)))
        with open(path_to_dts, 'w') as f:
            f.write(dts.to_dts())
        self.info('dtb at {}'.format(path_to_dtb), 1)
        self.info('dts at {}'.format(path_to_dts), 1)

        # machine name
        compatible = find_compatible_in_fdt(dts)
        self.firmware.set_machine_name(
            compatible[-1].replace(',', '_').replace('-', '_'))

        # board_id
        self.firmware.set_board_id('0xFFFFFFFF')

        # uart count
        self.firmware.set_uart_num(len(find_flatten_serial_in_fdt(dts)))

        return True

    def __init__(self, analysis_manager):
        super().__init__(analysis_manager)
        self.name = 'preprocdt'
        self.description = 'Preprocess the device tree blob.'
        self.required = ['bfilter', 'msearch']
        self.critical = True
