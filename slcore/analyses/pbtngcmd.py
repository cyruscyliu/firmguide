from slcore.amanager import Analysis


class PBtngCMD(Analysis):
    def __init__(self, analysis_manager):
        super().__init__(analysis_manager)

        self.name = 'pbtngcmd'
        self.description = 'Print booting cmdline for given image.'

    def run(self, firwmare, **kwargs):
        return True
