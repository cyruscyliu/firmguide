from pyqemulog import PQLI

from analyses.analysis import Analysis
from analyses.diag_tracing import LoadTrace


class InitValue(Analysis):
    def run(self, firmware):
        trace = self.analysis_manager.get_analysis('load_trace')
        assert isinstance(trace, LoadTrace)
        pql = trace.pql
        assert isinstance(pql, PQLI)

        panic_cpurf = self.analysis_manager.get_analysis('panic').panic_cpurf
        if panic_cpurf is None:
            self.context['input'] = 'there is no panic'
            return False

        cpurf = panic_cpurf
        while cpurf:
            bb = pql.get_bb(cpurf)
            print(bb)
            cpurf = pql.get_last_cpurf(panic_cpurf)

        return True

    def __init__(self, analysis_manager):
        super().__init__(analysis_manager)
        self.name = 'init_value'
        self.description = 'solve the init value for a certain register'
        self.context['hint'] = 'very difficult program analysis'
        self.critical = False
        self.required = ['panic']
        self.type = 'diag'
