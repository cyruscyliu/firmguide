#!/usr/bin/python
import sys
sys.path.extend(['.', '..', '../..'])

from slcore.dt_parsers.intc import *
from slcore.dt_parsers.common import load_dtb
from graphviz import Digraph


def scan_topology(path_to_dtb):
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
            if d['irqn'] == -1:
                g.edge(f, t)
            else:
                g.edge(f, t, str(d['irqn']))
    g.graph_attr['rankdir'] = 'LR'
    print(g.source)
    print('FYI: ONLINE GRAPHIVZ VIEWER: https://edotor.net')


def project_scan_topology(path_to_dtb):
    scan_topology(path_to_dtb)

if __name__ == '__main__':
    if len(sys.argv) == 2:
        path_to_dtb = sys.argv[1]
        scan_topology(path_to_dtb)
    else:
        print('usage: ./scan_topology.py path/to/dtb')

