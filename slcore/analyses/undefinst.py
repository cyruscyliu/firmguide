from slcore.amanager import Analysis


class CheckUndefInst(Analysis):
    def handle_arm_undef_inst(self, pql):
        uis = []
        for k, cpurf in pql.cpurfs.items():
            if 'exception' in cpurf and 'type' in cpurf['exception'] and \
                    cpurf['exception']['type'] == 'ui':
                uis.append(cpurf)

        if not len(uis):
            self.error_info = 'no undefined instruction'
            return True

        for cpurf in uis:
            ret = pql.get_exception_return_cpurf(cpurf)
            if ret is None:
                self.info('line {}:0x{} has an undef inst, return abnormally'.format(
                    cpurf['ln'], cpurf['register_files']['R15']), 1)
            else:
                self.info('line {}:0x{} has an undef inst, return normally'.format(
                    cpurf['ln'], cpurf['register_files']['R15']), 1)
                self.info('the program re-entry {}'.format(ret['exception']['pc']), 1)
        return True

    def handle_mips_undef_inst(self, pql):
        return True

    def run(self, **kwargs):
        self.dead_addresses = []

        trace = self.analysis_manager.get_analysis('loadtrace')
        pql = trace.pql

        if self.firmware.get_arch() == 'arm':
            return self.handle_arm_undef_inst(pql)
        else:
            return self.handle_mips_undef_inst(pql)

    def __init__(self, analysis_manager):
        super().__init__(analysis_manager)
        self.name = 'undefinst'
        self.description = 'Find data abort info.'
        self.critical = False
        self.required = ['userlevel', 'fastuserlevel']
        self.type = 'diag'
        #
        self.dead_addresses = []
