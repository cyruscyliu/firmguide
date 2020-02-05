from analyses.analysis import Analysis


class RAM(Analysis):
    def run(self, firmware):
        ram_size = firmware.get_ram_size()
        if ram_size is not None:
            self.info(firmware, 'get memory size {}'.format(ram_size), 1)
            return True
        arch = firmware.get_architecture()
        if arch == 'arm':
            rs = 32
        elif arch == 'mips':
            rs = 128
            firmware.set_va_pa_mapping('0x80000000', '0x00000000', '0x20000000')
            firmware.set_va_pa_mapping('0xa0000000', '0x00000000', '0x20000000')
            self.info(firmware, 'set mips va/pa mapping manually (kseg0/1)', 1)
        else:
            self.context['input'] = 'do not support new arch {}'.format(arch)
            return False

        firmware.set_ram_size('{} * MiB'.format(rs))
        firmware.set_ram_base('0x0')
        self.info(firmware, 'get memory info, base: {}, size: {}MB'.format(0, rs), 1)
        return True

    def __init__(self, analysis_manager):
        super().__init__(analysis_manager)
        self.name = 'ram'
        self.description = 'allocate 32M(ARM)/128M(MIPS) ram by default'
        self.required = ['cpu']
        self.critical = False

