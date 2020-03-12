from slcore.analyses.analysis import Analysis
from slcore.analyses.trace import LoadTrace


class UndefInst(Analysis):
    def handle_arm_undef_inst(self, firmware, pql):
        uis = []
        for k, cpurf in pql.cpurfs.items():
            if 'exception' in cpurf and 'type' in cpurf['exception'] and \
                    cpurf['exception']['type'] == 'ui':
                uis.append(cpurf)

        if not len(uis):
            self.context['input'] = 'no undefined instruction'
            return True

        for cpurf in uis:
            ret = pql.get_exception_return_cpurf(cpurf)
            if ret is None:
                self.info(firmware, 'line {}:0x{} has an undef inst, return abnormally'.format(
                    cpurf['ln'], cpurf['register_files']['R15']), 1)
            else:
                self.info(firmware, 'line {}:0x{} has an undef inst, return normally'.format(
                    cpurf['ln'], cpurf['register_files']['R15']), 1)
                self.info(firmware, 'the program re-entry {}'.format(ret['exception']['pc']), 1)
        return True

    def handle_mips_undef_inst(self, firmware, pql):
        return True

    def run(self, firmware):
        self.dead_addresses = []

        trace = self.analysis_manager.get_analysis('load_trace')
        assert isinstance(trace, LoadTrace)
        pql = trace.pql

        if firmware.get_arch() == 'arm':
            return self.handle_arm_undef_inst(firmware, pql)
        else:
            return self.handle_mips_undef_inst(firmware, pql)

    def __init__(self, analysis_manager):
        super().__init__(analysis_manager)
        self.name = 'undef_inst'
        self.description = 'find data abort info'
        self.context['hint'] = 'bad bad bad trace'
        self.critical = False
        self.required = ['check']
        self.type = 'diag'
        #
        self.dead_addresses = []
