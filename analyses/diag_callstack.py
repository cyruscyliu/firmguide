from analyses.analysis import Analysis
from pyqemulog import *


class CallStack(Analysis):
    def run(self, firmware):
        pass

    def __init__(self):
        super().__init__()
        self.name = 'callstack'
        self.description = 'show callstack in the trace'
        self.context['hint'] = 'bad bad bad trace'
        self.critical = False
        self.required = ['check']
