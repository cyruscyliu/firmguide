'''
Source Code Info Analysis.
'''
import os

from analyses.analysis import Analysis


class SINTC(Analysis):
    def run(self, firmware):
        """
        here is for 'simple interrupt controller solution'
        """
        # mask register
        # timer irqn and proper mmio init values to trigger timer's callback
        # proper mmio init values to pass multi-level of intc checkings
        # address to pull down intc signal
        return True

    def __init__(self, analysis_manager):
        super().__init__(analysis_manager)
        self.name = 'kerberos2'
        self.description = 'source code info analysis (llvm)'
        self.required = ['mfilter']
        self.context['hint'] = ''
        self.critical = False

