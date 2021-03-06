import os

from slcore.amanager import Analysis
from slcore.dt_parsers.common import load_dtb
from slcore.dt_parsers.compatible import find_compatible_in_fdt
from slcore.dt_parsers.serial import find_flatten_serial_in_fdt
from slcore.dt_parsers.cpu import find_flatten_cpu_in_fdt
from slcore.dt_parsers.compatible import query_arch_by_compatible, \
        query_board_id_by_compatible


class DTPreprocessing(Analysis):
    def run(self, **kwargs):
        # Data should not be obtained from kwargs.
        path_to_dtb = self.analysis_manager.firmware.get_realdtb()
        if path_to_dtb is None:
            self.error_info = 'there is no device tree blob available.'
            return False

        dts = load_dtb(path_to_dtb)
        path_to_dts = os.path.join(
            self.analysis_manager.project.attrs['path'],
            '{}.dts'.format(os.path.basename(path_to_dtb)))
        with open(path_to_dts, 'w') as f:
            f.write(dts.to_dts())
        self.info('dtb at {}'.format(path_to_dtb), 1)
        self.info('dts at {}'.format(path_to_dts), 1)

        # machine name: must exist
        compatible = find_compatible_in_fdt(dts)
        self.analysis_manager.firmware.set_machine_name('fg_' + '_'.join([
            comptb.replace(',', '_').replace('-', '_') for comptb in compatible]))
        # TODO update board_id
        board_id = query_board_id_by_compatible(compatible)
        self.analysis_manager.firmware.set_board_id(board_id)
        self.info('board id {} is chosen automatically'.format(board_id), 1)

        # arch
        cpu = find_flatten_cpu_in_fdt(dts)
        if cpu is None:
            self.error_info = 'invalid dtb, no processor is available'
            return False
        arch = query_arch_by_compatible(cpu[0]['compatible'])
        self.analysis_manager.firmware.set_arch(arch)
        self.info('arch {} is chosen automatically'.format(arch), 1)
        if arch == 'arm':
            self.analysis_manager.firmware.set_endian('l')
            self.info('endian l is chosen automatically', 1)
            self.analysis_manager.firmware.set_kernel_load_address('0x00008000')
            self.info('load address 0x00008000 is chosen automatically', 1)
        else:
            # mips
            endian = kwargs.pop('endian')
            load = kwargs.pop('load')
            if not (endian and load):
                self.error_info = 'please set -e for endian and -ld for load address'
                return False
            self.analysis_manager.firmware.set_endian(endian)
            self.analysis_manager.firmware.set_kernel_load_address(load)

        # uart count
        self.analysis_manager.firmware.set_uart_num(len(find_flatten_serial_in_fdt(dts) or []))
        return True

    def __init__(self, analysis_manager):
        super().__init__(analysis_manager)
        self.name = 'preprocdt'
        self.description = 'Preprocess the device tree blob.'
        self.required = ['bfilter', 'msearch', 'unpack']
        self.critical = True
