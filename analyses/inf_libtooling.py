"""
Source Code Info Extraction.
"""
import os

from analyses.analysis import Analysis


class LibTooling(Analysis):
    def run(self, firmware):
        return True

    def __init__(self):
        super().__init__()
        self.name = 'libtooling'
        self.description = 'source code info extraction (libtooling)'
        self.required = ['srcode']
        self.context['hint'] = ''
        self.critical = False
