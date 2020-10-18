import os

from slcore.amanager import Analysis
from slcore.dt_parsers.common import load_dtb
from slcore.dt_parsers.serial import find_flatten_serial_in_fdt
from slcore.dt_parsers.intc import find_flatten_intc_in_fdt
from slcore.dt_parsers.cpu import find_flatten_cpu_in_fdt
from slcore.brick import Brick


class TestUSN(Analysis):
    def run(self, **kwargs):
        path_to_dtb = self.analysis_manager.firmware.get_realdtb()
        if path_to_dtb is None:
            self.error_info = 'there is no real dtb available.'
            return False

        dts = load_dtb(path_to_dtb)

        # test serial model
        serials = find_flatten_serial_in_fdt(dts) or []
        for serial in serials:
            b = Brick('serial', serial['compatible'])
            if not b.supported:
                self.warning('cannot support serial {}'.format(
                    serial['compatible']), 0)
            else:
                self.info('support serial {}'.format(
                    serial['compatible']), 0)

        # test smp
        cpus = find_flatten_cpu_in_fdt(dts) or []
        if len(cpus) == 1:
            self.info('there is only 1 processor.', 1)
            return True
        else:
            self.warning('there are {} processors.'.format(len(cpus)), 0)

        # test intc model
        intcs = find_flatten_intc_in_fdt(dts) or []
        for intc in intcs:
            b = Brick('intc', intc['compatible'])
            if not b.supported:
                self.warning('cannot support intc {}'.format(
                    intc['compatible']), 0)
            else:
                self.info('support intc {}'.format(
                    intc['compatible']), 0)

        return True

    def __init__(self, analysis_manager):
        super().__init__(analysis_manager)
        self.name = 'usntest'
        self.description = 'Test serials and SMP configs.'
        self.critical = False
        self.required = []
