from analyses.analysis import Analysis
from slcore.profile.machine import Machine
from slcore.dt_parsers.common import *


class DeviceTree(Analysis):
    def run(self, firmware):
        dir_to_dt_collection = firmware.get_dt_collection()
        if dir_to_dt_collection is None:
            return True

        # for path_to_dtb in compile_dts_in_dtcg(dir_to_dt_collection):
            # We must get dozen of device tree source files, to
            # handle them all, we propose a new data structure
            # named `machine` with CPU/RAM/INTC/TIMER/UART/BAMBOOS
            # detail in. For other situation, say CMDLINE diverging,
            # NVRAM diverging, we should duplicate the machine not
            # the firmware.
            # dts = load_dtb(path_to_dtb)
            # machine = Machine()
            # machine.parse_dts(dts)
            # firmware.machines.append(machine)

            # for line in machine.__str__().strip().split('\n'):
            #     self.debug(firmware, '{}'.format(line), 1)

        return True

    def __init__(self, analysis_manager):
        super().__init__(analysis_manager)
        self.name = 'device_tree'
        self.description = 'parse device tree source in the kernel'
        self.required = ['mfilter', 'ram']
        self.context['hint'] = 'something wrong'
        self.critical = False
        self.settings = ['machines']

