import os

from analyses.analysis import Analysis
from analyses.diag_tracing import LoadTrace


class Checking(Analysis):
    def scan_user_level_qemudebug(self, firmware, pql):
        user_level = 'usr32' if firmware.architecture == 'arm' else 'user'
        for k, cpurf in pql.cpurfs.items():
            if cpurf['mode'] == user_level:
                return True
        self.context['input'] = 'have not entered the user level'
        return False

    def scan_user_level_ktracer(self, firmware, pql):
        return False

    def run(self, firmware):
        self.info(firmware, 'scan user level indicators in {}'.format(firmware.path_to_trace), 1)

        trace = self.analysis_manager.get_analysis('load_trace')
        assert isinstance(trace, LoadTrace)
        pql = trace.pql

        if firmware.trace_format == 'qemudebug':
            result = self.scan_user_level_qemudebug(firmware, pql)
            if result:
                self.info(firmware, 'have entered the user level', 1)
                exit(-1)
            return result
        else:
            return self.scan_user_level_ktracer(firmware, pql)

    def __init__(self, analysis_manager):
        super().__init__(analysis_manager)
        self.name = 'check'
        self.description = 'check whether we have done our job'
        self.context['hint'] = 'bad bad bad trace'
        self.critical = False
        self.required = ['load_trace']
