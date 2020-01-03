from analyses.analysis import Analysis


class RAMDefault(Analysis):
    def run(self, firmware):
        ram_size = firmware.get_ram_size()
        if ram_size is not None:
            self.info(firmware, 'get memory size {}'.format(ram_size), 1)
            return True
        firmware.set_ram_size('32 * MiB')
        firmware.set_ram_base('0x0')
        self.info(firmware, 'get memory info, base: {}, size: {}MB'.format(0, 32), 1)

    def __init__(self, analysis_manager):
        super().__init__(analysis_manager)
        self.name = 'ram'
        self.description = 'assign 1G ram by default'
        self.required = ['toh']
        self.critical = False
