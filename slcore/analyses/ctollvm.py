from slcore.amanager import Analysis


class CToLLVM(Analysis):
    def __init__(self, analysis_manager):
        super().__init__(analysis_manager)

        self.name = 'ctollvm'
        self.description = 'Compile the source to llvm bitcode.'
        self.required = []

    def run(self, **kwargs):
        return True
