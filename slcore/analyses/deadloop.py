from slcore.amanager import Analysis


class ShowDeadLoop(Analysis):
    def address2symbol(self, address):
        srcodec = self.analysis_manager.srcodec
        if not srcodec.supported:
            return None
        return srcodec.address2symbol(address)

    def run(self, **kwargs):
        trace = self.analysis_manager.get_analysis('loadtrace')
        pql = trace.pql

        cpurfs = pql.cpurfs
        kmax = (len(cpurfs) - 1)
        b = int(pql.get_pc(cpurfs[kmax]), 16)
        a = int(pql.get_ra(cpurfs[kmax]), 16)

        if b >= a:
            b_sym = self.address2symbol(b)
            a_sym = self.address2symbol(a)
            if b_sym is None or a_sym is None:
                self.info('deap loop from 0x{:x} to 0x{:x}'.format(b, a), 1)
            else:
                self.info('deap loop from 0x{:x}({}) to 0x{:x}({})'.format(
                    b, b_sym, a, a_sym), 1)
        return True

    def __init__(self, analysis_manager):
        super().__init__(analysis_manager)
        self.name = 'deadloop'
        self.description = 'Find dead loop in given trace.'
        self.critical = False
        self.required = ['callstack']
        self.type = 'diag'
