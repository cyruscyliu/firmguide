from analyses.analysis import Analysis


class MIPSCPU(Analysis):
    def run(self, firmware):
        return True

    def __init__(self, analysis_manager):
        super().__init__(analysis_manager)
        self.name = 'mips_cpu'
        self.description = 'infer supported mips cpus'
        self.context['hint'] = 'no srcode available'
        self.critical = True
        self.required = ['srcode']
