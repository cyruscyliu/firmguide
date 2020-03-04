import os

from pyqemulog import PQLI

from slcore.analyses.analysis import Analysis
from slcore.analyses.trace import LoadTrace


class Panic(Analysis):
    def run(self, firmware):
        path_to_vmlinux = firmware.get_path_to_vmlinux()
        if path_to_vmlinux is None:
            self.context['input'] = 'no vmlinux'
            return False

        # 80023a48 T panic
        output = os.popen('nm {}'.format(path_to_vmlinux)).readlines()

        address_to_panic = None
        for op in output:
            things = op.strip().split()
            if len(things) < 3:
                continue
            address, t, symbol = things
            if symbol == 'panic':
                address_to_panic = address
                break

        if address_to_panic is None:
            self.context['input'] = 'no panic in this kernel'
            return False

        trace = self.analysis_manager.get_analysis('load_trace')
        assert isinstance(trace, LoadTrace)
        pql = trace.pql
        assert isinstance(pql, PQLI)

        for k, cpurf in pql.cpurfs.items():
            if pql.get_pc(cpurf) == address_to_panic:
                self.info(firmware, 'panic found at {}'.format(address_to_panic), 1)
                self.panic_cpurf = cpurf
                return True
        self.context['input'] = 'no panic found'
        return False

    def __init__(self, analysis_manager):
        super().__init__(analysis_manager)
        self.name = 'panic'
        self.description = 'find panic and show solutions'
        self.context['hint'] = 'there is no panic at all'
        self.critical = False
        self.required = ['check']
        self.type = 'diag'
        #
        self.panic_cpurf = None
