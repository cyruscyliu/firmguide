from slcore.amanager import Analysis


class CalcLoadAddr(Analysis):
    def run(self, **kwargs):
        if self.firmware.get_arch() == 'arm':
            self.firmware.set_kernel_load_address('0x00008000')
            self.info('set arm loading address 0x00008000 by default', 1)
            return True
        elif self.firmware.get_arch() == 'mips':
            self.firmware.set_kernel_load_address('0x80000000')
            self.info('set mips loading address 0x80000000 by default', 1)
            return True
        else:
            self.error_info(
                'cannot support arch {}'.format(self.firmware.get_arch()))
            return False

    def __init__(self, analysis_manager):
        super().__init__(analysis_manager)
        self.name = 'loaddr'
        self.description = 'Resolve image loading address.'
        self.required = []
