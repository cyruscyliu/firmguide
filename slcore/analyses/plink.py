from slcore.amanager import Analysis


class PartiallyLink(Analysis):
    def __init__(self, analysis_manager):
        super().__init__(analysis_manager)

        self.name = 'plink'
        self.description = 'Link LLVM bitcode selectively.'
        self.required = ['ctollvm']

    def run(self, **kwargs):
        return True
