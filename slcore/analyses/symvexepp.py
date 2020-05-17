from slcore.amanager import Analysis


class SVEPostProcess(Analysis):
    def __init__(self, analysis_manager):
        super().__init__(analysis_manager)

        self.name = 'svepp'
        self.description = 'Post process the results of SVE.'
        self.required = ['symvexe']

    def run(self, **kwargs):
        self.info(self.firmware.running_command, 1)
        return True
