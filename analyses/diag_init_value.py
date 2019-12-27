from analyses.analysis import Analysis


class InitValue(Analysis):
    def run(self, firmware):
        return True

    def __init__(self):
        super().__init__()
        self.name = 'init_value'
        self.description = 'solve the init value for a certain register'
        self.context['hint'] = 'very difficult program analysis'
        self.critical = False
        self.required = ['check']
