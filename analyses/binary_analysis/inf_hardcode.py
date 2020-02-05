from analyses.analysis import Analysis


class HardCode(Analysis):
    def run(self, firmware):
        if firmware.get_uuid() == "13882":
            firmware.load_bamboo_devices()
            firmware.insert_bamboo_devices(0x44e001f0, 0x4, value=3 << 8 | 3 << 4)
            firmware.insert_bamboo_devices(0x44e001f4, 0x4, value=32768)
            firmware.insert_bamboo_devices(0x44e001f8, 0x8, value=0)
            firmware.update_bamboo_devices()
            self.info(firmware, 'update plla initvalue at 0x44e001f0/0x44e001f4/0x44e001f8', 1)
            for bamboo_device in firmware.print_bamboo_devices():
                self.info(firmware, bamboo_device, 1)
        return True

    def __init__(self, analysis_manager):
        super().__init__(analysis_manager)
        self.name = 'hardcode'
        self.description = 'sometimes, we need hardcode some properties which cannot be infered'
        self.required = []
        self.context = 'no errors at all'
        self.critical = False

