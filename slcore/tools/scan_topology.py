#!/usr/bin/python
import sys
sys.path.extend(['.', '..', '../..'])

from slcore.dt_parsers.intc import *
from slcore.dt_parsers.common import load_dtb
from graphviz import Digraph
from slcore.project import get_current_project


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
            if d['irqns'] == [-1]:
                g.edge(f, t)
            else:
                for i in d['irqns']:
                    g.edge(f, t, str(i))
    g.graph_attr['rankdir'] = 'LR'
    print(g.source)
    print('FYI: ONLINE GRAPHIVZ VIEWER: https://edotor.net')


def project_scan_topology(path_to_dtb):
    project = get_current_project()
    if project is None:
        return

    if path_to_dtb is None:
        if project.attrs['dtbs'] is None:
            print('please assign -dtb/--dtb or add a device tree blob to current project')
            return
        elif len(project.attrs['dtbs']) == 0:
            print('please assign -dtb/--dtb or add a device tree blob to current project')
            return
        else:
            path_to_dtb = project.attrs['dtbs'][0]

    scan_topology(path_to_dtb)

if __name__ == '__main__':
    if len(sys.argv) == 2:
        path_to_dtb = sys.argv[1]
        scan_topology(path_to_dtb)
    else:
        print('usage: ./scan_topology.py path/to/dtb')

