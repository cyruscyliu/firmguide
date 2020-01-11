import os

from pyqemulog import PQLI

from analyses.analysis import Analysis
from analyses.diag_tracing import LoadTrace


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
            address, t, symbol = op.strip().split()
            if symbol == 'panic':
                address_to_panic = address

        if address_to_panic is None:
            self.context['input'] = 'no panic in this kernel'
            return False

        trace = self.analysis_manager.get_analysis('load_trace')
        assert isinstance(trace, LoadTrace)
        pql = trace.pql
        assert isinstance(pql, PQLI)

        for k, cpurf in pql.cpurfs.items():
            if k == address_to_panic:
                self.info(firmware, 'panic found at {}'.format(address_to_panic), 1)
                return True
        self.context['input'] = 'no panic found'
        return False

    def __init__(self, analysis_manager):
        super().__init__(analysis_manager)
        self.name = 'panic'
        self.description = 'find panic and show solutions'
        self.context['hint'] = 'there is no panic at all'
        self.critical = False
        self.required = ['check', 'data_abort']
        self.type = 'diag'
