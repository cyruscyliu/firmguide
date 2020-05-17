from slcore.amanager import Analysis


class SymVExe(Analysis):
    def __init__(self, analysis_manager):
        super().__init__(analysis_manager)

        self.name = 'symvexe'
        self.description = 'Symbolic virtual execution of start_kernel().'
        self.required = ['plink']

    def run(self, **kwargs):
        return True
