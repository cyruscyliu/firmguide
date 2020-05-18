import os

from slcore.amanager import Analysis
from slcore.dt_parsers.common import load_dtb
from slcore.dt_parsers.cpu import find_flatten_cpu_in_fdt
from slcore.dt_parsers.serial import find_flatten_serial_in_fdt
from slcore.dt_parsers.intc import find_flatten_intc_in_fdt
from slcore.dt_parsers.timer import find_flatten_timer_in_fdt
from slcore.dt_parsers.flash import find_flatten_flash_in_fdt
from slcore.dt_parsers.misc import find_flatten_misc_in_fdt
from slcore.dt_parsers.memory import find_flatten_ram_in_fdt
from slcore.dt_parsers.mmio import find_flatten_mmio_in_fdt
from slcore.brick import Brick


class UpdateHardwareDT(Analysis):
    def __init__(self, analysis_manager):
        super().__init__(analysis_manager)

        self.name = 'scanhwdt'
        self.description = \
            'Scan hardware in the OS source by device tree blobs.'
        self.required = []
        self.scan_handlers = {
            'cpu': find_flatten_cpu_in_fdt,
            'ram': find_flatten_ram_in_fdt,
            'intc': find_flatten_intc_in_fdt,
            'serial': find_flatten_serial_in_fdt,
            'timer': find_flatten_timer_in_fdt,
            'flash': find_flatten_flash_in_fdt,
            'misc': find_flatten_misc_in_fdt,
            'mmio': find_flatten_mmio_in_fdt,
        }
        self.skipped_bdevices = []

    def is_gpio_intc(self, t, compatible):
        if t != 'intc':
            return False

        for cmptb in compatible:
            if cmptb.find('gpio') != -1:
                return True

    def __skip(self, compatible):
        for cmptb in compatible:
            if cmptb in self.skipped_bdevices:
                return True

    def scan_and_update(self, dts):
        for k, v in self.scan_handlers.items():
            flatten_ks = v(dts)
            for context in flatten_ks:
                if self.__skip(context['compatible']):
                    self.debug('skip {}'.format(context['compatible']), 0)
                    continue
                b = Brick(k, context['compatible'])
                if not b.supported and \
                        not self.is_gpio_intc(k, context['compatible']):
                    b.update_model()
                    self.info('update {} {}'.format(
                        k, context['compatible']), 1)
                self.skipped_bdevices.append(b.effic_compatible)
                self.skipped_bdevices.extend(b.buddy_compatible)

    def run(self, **kwargs):
        srcodec = self.analysis_manager.srcodec
        if not srcodec.supported:
            self.error_info('please set the source code')
            return False

        # search *.dtb in the source
        path_to_source = srcodec.get_path_to_source_code()
        with os.popen('find {} -name *.dtb'.format(path_to_source)) as f:
            for dtb in f:
                dts = load_dtb(dtb.strip())
                self.scan_and_update(dts)
        return True
