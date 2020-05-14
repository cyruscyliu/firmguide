from slcore.analysis import Analysis


class PluginPBtngCMD(Analysis):
    def __init__(self, analysis_manager):
        super().__init__(analysis_manager)

        self.name = 'pbtngcmd'
        self.description = 'Plugin - Print booting cmdline for given image.'

    def run(self, firwmare, **kwargs):
        pass
