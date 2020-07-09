from slcore.amanager import Analysis


class CheckMissingCode(Analysis):
    def run(self, **kwargs):
        trace = self.analysis_manager.get_analysis('loadtrace')
        pql = trace.pql

        for k, cpurf in pql.get_cpurf():
            nop = 0

            bb = pql.get_bb(cpurf)
            for instruction in bb['instructions']:
                if instruction['opcode'] == 'nop':
                    nop += 1
            if nop == 512:
                last_cpurf = pql.get_last_cpurf(cpurf)
                self.error_info = \
                    '512 nop basic block, code is missing, last cpurf at line {}'.format(
                        last_cpurf['ln'])
                return False
        return True

    def __init__(self, analysis_manager):
        super().__init__(analysis_manager)
        self.name = 'codemissing'
        self.description = \
            'Check whether or not the executable is loaded normally.'
        self.critical = False
        self.required = ['userlevel', 'fastuserlevel', 'loadtrace']
        self.type = 'diag'
