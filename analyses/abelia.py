from analyses.common.analysis import AnalysisGroup, Analysis

class AbeliaCPU(Analysis):
    def run(self, firmware):
        pass

    def __init__(self):
        super().__init__()
        # basic
        self.description = 'we\'re gonna infer what CPU model the firmware use'
        self.name = 'cpu'
        # logging
        self.log_suffix = '[CPU]'
        # exception
        self.context['hint'] = ''
        # requirement
        self.required = []


class AbeliaRAM(Analysis):
    def run(self, firmware):
        LOG_SUFFIX = 'DEFAULT'
        ram_base, ram_size = firmware.get_ram()
        if ram_size is not None:
            return
        firmware.set_ram(0, 1024, unit='MiB')
        self.info('\033[32mget memory info, base: {}, size: {}MB\033[0m {}'.format(0, 1024, LOG_SUFFIX))



class AbeliaUART(Analysis):
    pass


class AbeliaIC(Analysis):
    pass


class AbeliaFLASH(Analysis):
    pass


class AbeliaTimer(Analysis):
    pass


class Abelia(AnalysisGroup):
    def run(self, firmware):
        pass

    def __init__(self):
        super().__init__()
        self.name = 'abelia'
        self.description = 'abelia devices which must be functional accurate'
        self.members = [AbeliaCPU(), AbeliaRAM(), AbeliaIC(), AbeliaTimer(), AbeliaUART(), AbeliaFLASH()]
