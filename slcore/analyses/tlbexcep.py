from slcore.amanager import Analysis


class CheckTLBExcep(Analysis):
    def handle_mips_tlb_exception(self, pql):
        tlb = []
        tlbl = 0
        tlbs = 0
        for k, cpurf in pql.get_cpurf():
            if 'exception' in cpurf and 'type' in cpurf['exception'] and \
                    cpurf['exception']['type'] == 'tlbl' and tlbl < 10:
                tlb.append(cpurf)
                tlbl += 1
            if 'exception' in cpurf and 'type' in cpurf['exception'] and \
                    cpurf['exception']['type'] == 'tlbs' and tlbs < 10:
                tlb.append(cpurf)
                tlbs += 1

        if not len(tlb):
            self.debug('there is no tlb exception', 1)
            return True

        for cpurf in tlb[:10]:
            ret = pql.get_exception_return_cpurf(cpurf)
            if ret is None:
                self.info('line {}:0x{} has a {} exception, return abnormally'.format(
                    cpurf['ln'], cpurf['register_files']['pc'], cpurf['exception']['type']), 1)
            else:
                self.info('line {}:0x{} has a {} exception, return normally'.format(
                    cpurf['ln'], cpurf['register_files']['pc'], cpurf['exception']['type']), 1)
                self.info('the program re-entry {}'.format(ret['exception']['pc']), 1)
        return True

    def handle_arm_tlb_exception(self, pql):
        return True

    def run(self, **kwargs):
        trace = self.analysis_manager.get_analysis('loadtrace')
        pql = trace.pql

        arch = self.analysis_manager.firmware.get_arch()
        if arch == 'arm':
            return self.handle_arm_tlb_exception(pql)
        elif arch == 'mips':
            return self.handle_mips_tlb_exception(pql)
        else:
            self.error_info = 'unsupported arch {}'.foramt(arch)
            return False

    def __init__(self, analysis_manager):
        super().__init__(analysis_manager)
        self.name = 'tlbexcep'
        self.description = 'Find tlb load exception info.'
        self.critical = False
        self.required = ['userlevel', 'fastuserlevel', 'loadtrace']
