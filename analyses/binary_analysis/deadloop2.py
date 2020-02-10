from pyqemulog import PQLI

from analyses.analysis import Analysis
from analyses.callstack import CallStack, CallRecord
from analyses.trace import LoadTrace


class DeadLoop2(Analysis):
    def run(self, firmware):
        callstack = self.analysis_manager.get_analysis('callstack')
        assert isinstance(callstack, CallStack)
        funcs = callstack.callstack

        trace = self.analysis_manager.get_analysis('load_trace')
        assert isinstance(trace, LoadTrace)
        pql = trace.pql
        assert isinstance(pql, PQLI)

        # find final func which does not return normally
        target_func = None
        for func in reversed(funcs):
            assert isinstance(func, CallRecord)
            if not func.returned:
                target_func = func
                break

        if target_func is None:
            self.context['input'] = 'every func returns normally'
            return False

        cpurf = target_func.cpurf
        last_cpurfs = []

        while cpurf:
            last_cpurfs.append(cpurf)
            cpurf = pql.get_next_cpurf(cpurf)

        b = int(pql.get_pc(last_cpurfs[-2]), 16)
        a = int(pql.get_pc(last_cpurfs[-1]), 16)

        if b > a:
            self.info(firmware, 'there is deap loop from 0x{:x} to 0x{:x}'.format(b, a), 1)

        return True

    def __init__(self, analysis_manager):
        super().__init__(analysis_manager)
        self.name = 'deadloop2'
        self.description = 'new algo to find dead loop in the given trace'
        self.context['hint'] = 'bad bad bad trace'
        self.critical = False
        self.required = ['callstack']
        self.type = 'diag'

