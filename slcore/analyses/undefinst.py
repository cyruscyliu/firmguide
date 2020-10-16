from slcore.amanager import Analysis


class CheckUndefInst(Analysis):
    def handle_arm_undef_inst(self, pql):
        uis = []
        for k, cpurf in pql.get_cpurf():
            if 'exception' in cpurf and 'type' in cpurf['exception'] and \
                    cpurf['exception']['type'] == 'ui':
                uis.append(cpurf)

        if not len(uis):
            self.debug('there is no undefined instruction', 1)
            return True

        for cpurf in uis[:10]:
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
        unkinsns = []
        for k, cpurf in pql.get_cpurf():
            if 'exception' in cpurf and 'type' in cpurf['exception'] and \
                    cpurf['exception']['type'] == 'ri':
                unkinsns.append(cpurf)

        if not len(unkinsns):
            self.debug('there is no unknown instruction', 1)
            return True

        for cpurf in unkinsns[:10]:
            ret = pql.get_exception_return_cpurf(cpurf)
            if ret is None:
                self.info('line {}:0x{} has a {} exception, return abnormally'.format(
                    cpurf['ln'], cpurf['register_files']['pc'], cpurf['exception']['type']), 1)
            else:
                self.info('line {}:0x{} has a {} exception, return normally'.format(
                    cpurf['ln'], cpurf['register_files']['pc'], cpurf['exception']['type']), 1)
            self.info('maybe data is treated as instruction, change the entrypoint', 1)
        return True

    def run(self, **kwargs):
        trace = self.analysis_manager.get_analysis('loadtrace')
        pql = trace.pql

        arch = self.analysis_manager.firmware.get_arch()
        if arch == 'arm':
            return self.handle_arm_undef_inst(pql)
        elif arch == 'mips':
            return self.handle_mips_undef_inst(pql)
        else:
            self.error_info = 'unsupported arch {}'.format(arch)
            return False

    def __init__(self, analysis_manager):
        super().__init__(analysis_manager)
        self.name = 'undefinst'
        self.description = 'Find data abort info.'
        self.critical = False
        self.required = ['userlevel', 'fastuserlevel', 'loadtrace']
