import os
import fdt

from analyses.analysis import Analysis
from slcore.profile.machine import Machine


class DeviceTree(Analysis):
    def compile_dts(self, path_to_dts):
        path_to_dtb = path_to_dts + '.dtb'
        os.system('dtc -I dts -O dtb -f {} -o {} >/dev/null 2>&1'.format(path_to_dts, path_to_dtb))
        return path_to_dtb

    def run(self, firmware):
        dir_to_dt_collection = firmware.get_dt_collection()

        if dir_to_dt_collection is None:
            return True
        for path_to_dts in os.listdir(dir_to_dt_collection):
            if path_to_dts.endswith('dtb'):
                continue
            if path_to_dts.endswith('dtsi'):
                continue
            # We must get dozen of device tree source files, to
            # handle them all, we propose a new data structure
            # named `machine` with CPU/RAM/INTC/TIMER/UART/BAMBOOS
            # detail in. For other situation, say CMDLINE diverging,
            # NVRAM diverging, we should duplicate the machine not
            # the firmware.
            path_to_dts = os.path.join(dir_to_dt_collection, path_to_dts)
            path_to_dtb = self.compile_dts(path_to_dts)
            with open(path_to_dtb, 'rb') as f:
                dtb = f.read()
            dts = fdt.parse_dtb(dtb)
            machine = Machine()
            machine.parse_dts(dts)
            firmware.machines.append(machine)
        self.info(firmware, 'get {} different dts'.format(len(firmware.machines)), 1)

        return True

    def __init__(self, analysis_manager):
        super().__init__(analysis_manager)
        self.name = 'device_tree'
        self.description = 'parse firmware\'s device tree'
        self.required = ['mfilter']
        self.context['hint'] = 'device tree is not available'
        self.critical = False
        self.settings = ['machines']

