from analyses.common.analysis import AnalysisGroup, Analysis


class AbeliaCPU(Analysis):
    def run(self, firmware):
        pass

    def __init__(self):
        super().__init__()
        # basic
        self.description = 'we\'re gonna infer what CPU model the firmware use'
        self.name = 'cpu'
        # exception
        self.context['hint'] = ''
        # requirement
        self.required = []


class AbeliaRAM(Analysis):
    def run(self, firmware):
        ram_base, ram_size = firmware.get_ram()
        if ram_size is not None:
            return
        firmware.set_ram(0, 1024, unit='MiB')
        self.info(firmware, 'get memory info, base: {}, size: {}MB'.format(0, 1024), 1)


class AbeliaUART(Analysis):
    pass


class AbeliaIC(Analysis):
    pass


class AbeliaFLASH(Analysis):
    pass


class AbeliaTimer(Analysis):
    pass
