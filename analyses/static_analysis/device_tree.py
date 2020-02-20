from analyses.analysis import Analysis
from slcore.dt_parsers.common import *
from slcore.generation.dt_renderer import Model
from slcore.dt_parsers.intc import *
from slcore.dt_parsers.serial import *
from slcore.dt_parsers.mmio import *


class DeviceTree(Analysis):
    def contain(self, aa, b):
        """
        aa contains b
        """
        for a in aa:
            if a['path'] == b['path']:
                return True
        return False

    def run(self, firmware):
        path_to_dtb = firmware.get_components().get_path_to_dtb()
        if path_to_dtb is None:
            return True

        # 1. load the dtb
        dts = load_dtb(path_to_dtb)

        # 2. create bdevices
        # 2.1 get the intc/serail/mmio list
        flatten_intc = find_flatten_intc_in_fdt(dts)
        flatten_serial = find_flatten_serial_in_fdt(dts)
        flatten_mmio = find_flatten_mmio_in_fdt(dts)
        # 2.2 create bamboo devices
        for mmio in flatten_mmio:
            if self.contain(flatten_intc, mmio):
                continue
            if self.contain(flatten_serial, mmio):
                continue
            for reg in mmio['reg']:
                firmware.insert_bamboo_devices(
                    reg['base'], reg['size'], value=0)
        firmware.update_bamboo_devices()

        return True

    def __init__(self, analysis_manager):
        super().__init__(analysis_manager)
        self.name = 'device_tree'
        self.description = 'parse device tree source in the kernel'
        self.required = ['mfilter', 'ram']
        self.context['hint'] = ''
        self.critical = False
        self.settings = ['bamboo_devices']

