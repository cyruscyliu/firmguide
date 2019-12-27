from analyses.analysis import Analysis
from pyqemulog import *


class CallStack(Analysis):
    def run(self, firmware):
        pass

    def __init__(self, analysis_manager):
        super().__init__(analysis_manager)
        self.name = 'callstack'
        self.description = 'show callstack in the trace'
        self.context['hint'] = 'bad bad bad trace'
        self.critical = False
        self.required = ['check']
