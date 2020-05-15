from slcore.amanager import Analysis


class CheckTLBExcep(Analysis):
    def handle_mips_tlb_exception(self, firmware, pql):
        tlb = []
        tlbl = 0
        tlbs = 0
        for k, cpurf in pql.cpurfs.items():
            if 'exception' in cpurf and 'type' in cpurf['exception'] and \
                    cpurf['exception']['type'] == 'tlbl' and tlbl < 10:
                tlb.append(cpurf)
                tlbl += 1
            if 'exception' in cpurf and 'type' in cpurf['exception'] and \
                    cpurf['exception']['type'] == 'tlbs' and tlbs < 10:
                tlb.append(cpurf)
                tlbs += 1

        if not len(tlb):
            self.context['input'] = 'no tlb exception'
            return True

        for cpurf in tlb:
            ret = pql.get_exception_return_cpurf(cpurf)
            if ret is None:
                self.info(firmware, 'line {}:0x{} has a {} exception, return abnormally'.format(
                    cpurf['ln'], cpurf['exception']['type'], cpurf['register_files']['pc']), 1)
            else:
                self.info(firmware, 'line {}:0x{} has a {} exception, return normally'.format(
                    cpurf['ln'], cpurf['exception']['type'], cpurf['register_files']['pc']), 1)
                self.info(firmware, 'the program re-entry {}'.format(ret['exception']['pc']), 1)
        return True

    def handle_arm_tlb_exception(self, firmware, pql):
        return True

    def run(self, firmware):
        trace = self.analysis_manager.get_analysis('loadtrace')
        pql = trace.pql

        if firmware.get_arch() == 'arm':
            return self.handle_arm_tlb_exception(firmware, pql)
        else:
            return self.handle_mips_tlb_exception(firmware, pql)

    def __init__(self, analysis_manager):
        super().__init__(analysis_manager)
        self.name = 'tlbexcep'
        self.description = 'Find tlb load exception info.'
        self.context['hint'] = 'bad bad bad trace'
        self.critical = False
        self.required = ['checkuserlevel', 'checkuserlevelf']
        self.type = 'diag'
