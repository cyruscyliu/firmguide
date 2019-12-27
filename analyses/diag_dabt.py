from analyses.analysis import Analysis
from pyqemulog import *


class DataAbort(Analysis):
    def run(self, firmware):
        pass

    def __init__(self):
        super().__init__()
        self.name = 'data_abort'
        self.description = 'find data abort info'
        self.context['hint'] = 'bad bad bad trace'
        self.critical = False
        self.required = ['check']
