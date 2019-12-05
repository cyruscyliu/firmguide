from analyses.common.analysis import AnalysisGroup, Analysis


class AbeliaRAM(Analysis):
    def run(self, firmware):
        ram_size = firmware.get_ram_size()
        if ram_size is not None:
            self.info(firmware, 'get memory size {}'.format(ram_size), 1)
            return True
        firmware.set_ram_size(0, 1024, unit='MiB')
        self.info(firmware, 'get memory info, base: {}, size: {}MB'.format(0, 1024), 1)

    def __init__(self):
        super().__init__()
        self.name = 'ram'
        self.description = 'assign 1G ram by default'
        self.required = ['toh']
        self.critical = False
