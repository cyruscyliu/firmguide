'''
Source Code Info Extraction.
'''
import os

from analyses.analysis import Analysis


class LibTooling(Analysis):
    def run(self, firmware):
        """
        here is for 'uart/flash/bamboo devices'
        """
        return True

    def __init__(self, analysis_manager):
        super().__init__(analysis_manager)
        self.name = 'kerberos1'
        self.description = 'source code info extraction (libtooling)'
        self.required = ['srcode']
        self.context['hint'] = ''
        self.critical = False

