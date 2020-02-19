from analyses.analysis import Analysis
from slcore.database.dbf import get_database
from slcore.profile.machine import Machine
from slcore.dt_parsers.common import *


class DeviceTree(Analysis):
    def run(self, firmware):
        path_to_dtb = firmware.get_components().get_path_to_dtb()
        if path_to_dtb is None:
            return True

        # 1. load the dtb
        dts = load_dtb(path_to_dtb)
        machine = Machine()
        machine.parse_dts(dts)
        firmware.machine = machine

        # 2. handle the cpu
        compatible = machine.cpus[0].get_compatible()
        for cmptb in compatible:
            qemu_devices = get_database('qemu.devices')
            cpu_model = qemu_devices.select('cpu', compatible=cmptb)
            if cpu_model is None:
                self.warning(firmware, 'please update qemu.devices for {}'.format(cmptb))
                continue
            firmware.set_cpu_model(cpu_model)
            self.info(firmware, 'get cpu {}'.format(cpu_model), 1)

        # 3. handle the intc
        # 3.1 handle intc one by one
        # 3.2 connect them

        # 4 handle the uart
        for uart in machine.uarts:
            uart.set_endian(firmware.get_endian())
        return True

    def __init__(self, analysis_manager):
        super().__init__(analysis_manager)
        self.name = 'device_tree'
        self.description = 'parse device tree source in the kernel'
        self.required = ['mfilter', 'ram']
        self.context['hint'] = 'something wrong'
        self.critical = False
        self.settings = ['machines']

