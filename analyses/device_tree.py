import fdt

from analyses.common.analysis import Analysis


class DeviceTree(Analysis):
    def run(self, firmware):
        dtb = firmware.get_path_to_dtb()
        if dtb is None:
            self.context['input'] = 'assign the path to the device tree blob'
            return False
        with open(dtb, 'rb') as f:
            dtb = f.read()
        dts = fdt.parse_dtb(dtb)
        firmware.set_dts(dts)
        return True

    def __init__(self):
        super().__init__()
        self.name = 'dt'
        self.description = 'parse firmware\'s device tree'
        self.log_suffix = '[DEVICE TREE]'
        self.required = ['extraction']
        self.context['hint'] = 'device tree is not available'
        self.critical = False
