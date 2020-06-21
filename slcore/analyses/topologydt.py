from graphviz import Digraph
from slcore.dt_parsers.intc import find_flatten_intc_in_fdt
from slcore.dt_parsers.common import load_dtb
from slcore.amanager import Analysis


class TopologyDT(Analysis):
    def __init__(self, analysis_manager):
        super().__init__(analysis_manager)

        self.name = 'tolologydt'
        self.description = \
            'Display the interrupt topology in given device tree blob.'

    def run(self, **kwargs):
        path_to_dtb = self.firmware.get_realdtb()
        if path_to_dtb is None:
            self.error_info = 'there is no real dtb available.'
            return False

        dts = load_dtb(path_to_dtb)

        flatten_intc_all = find_flatten_intc_in_fdt(dts, nonintc_slave=True)

        def label_intc(intc):
            return intc['compatible'][-1]

        def get_intc(flatten_intc_all, intcp):
            if intcp == -1:
                return {'compatible': ['cpu']}
            for intc in flatten_intc_all:
                if intc['intc'] and intc['phandle'] == intcp:
                    return intc

        g = Digraph()
        for d in flatten_intc_all:
            if d['slave']:
                f = label_intc(d)
                t = label_intc(get_intc(flatten_intc_all, d['intcp']))
                if d['irqns'] == [-1]:
                    g.edge(f, t)
                else:
                    for i in d['irqns']:
                        g.edge(f, t, str(i))
        g.graph_attr['rankdir'] = 'LR'
        print(g.source)
        self.info('ONLINE GRAPHIVZ VIEWER: https://edotor.net', 1)
        return True
