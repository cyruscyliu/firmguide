import os
import fdt

from slcore.dt_parsers.mmio import *
from slcore.dt_parsers.compatible import *


COMPATIBLE_INTERRUPTS_INDEX = {
    'arm,gic-400': 1,
    'arm,cortex-a15-gic': 1,
    'arm,cortex-a9-gic': 1,
    'arm,cortex-a7-gic': 1,
    'arm,arm11mp-gic': 1,
    'brcm,brahma-b15-gic': 1,
}

def __find_interrupts_index(dts, phandle):
    for pa, no, pros in dts.walk():
        if len(no):
            continue
        if dts.exist_property('interrupt-controller', pa) and \
                dts.exist_property('phandle', pa) and \
                phandle == dts.get_property('phandle', pa).data[0]:
            interrupt_cells = dts.get_property('#interrupt-cells', pa).data[0]
            if interrupt_cells == 1:
                return 0
            # we should find the index in the table
            compatible = dts.get_property('compatible', pa).data
            for cmptb in compatible:
                if cmptb in COMPATIBLE_INTERRUPTS_INDEX:
                    return COMPATIBLE_INTERRUPTS_INDEX[cmptb]
    return None


def find_irqn_by_pphandle(dts, pphandle, cell):
    interrupts_index = __find_interrupts_index(dts, pphandle)
    if interrupts_index is None:
        return cell
    else:
        irqn = cell[interrupts_index]
        return irqn


def find_intc_by_phandle(dts, phandle):
    flatten_intcs = find_flatten_intc_in_fdt(dts)
    for intc in flatten_intcs:
        if intc['phandle'] == phandle:
            return intc

def find_pphandle_by_path(dts, path):
    pphandle = dts.get_property('interrupt-parent', path)
    if pphandle is None:
        pnode = dts.get_node(path).parent
        ppath = os.path.join(pnode.path, pnode.name)
        return find_pphandle_by_path(dts, ppath)
    else:
        return pphandle.data[0]


def find_flatten_intc_in_fdt(dts):
    """
    intc:      always, whether is an interrupt controller or not
    phandle:   always, a number identifies an interrupt controller
    master:    always, whether is a master interrupt controller or not
    slave:     always, whether is a slave interrupt controller or not
    intcp:     condit, the phandle of the parent interrupt controller, if the slave is true
    irqn:      condit, the irq number to which the slave device connect, if the slave is true
    compatible always, the compatible of the node
    path:      always, the path of the node
    reg:       always, see find_mmio_by_path for details
    """
    flatten_intc_tree = {}
    for pa, no, pros in dts.walk():
        if len(no):
            continue
        if dts.exist_property('interrupt-controller', pa):
            compatible = find_compatible_by_path(dts, pa)
            if dts.exist_property('phandle', pa):
                phandle = dts.get_property('phandle', pa).data[0]
                if dts.exist_property('interrupt-parent', pa) and \
                        hasattr(dts.get_property('interrupt-parent', pa),'data'):
                    interrupt_parent = find_pphandle_by_path(dts, pa)
                    if not dts.exist_property('interrupts', pa):
                        continue
                    interrupts = dts.get_property('interrupts', pa).data
                    interrupts = find_irqn_by_pphandle(dts, interrupt_parent, interrupts)
                    flatten_intc_tree[pa] = {
                        'phandle': phandle, 'intc': True, 'master': True, 'slave': True,
                        'intcp': interrupt_parent, 'irqn': interrupts,
                        'compatible': compatible}
                else:
                    # here is the intc connecting to the cpu
                    flatten_intc_tree[pa] = {
                        'phandle': phandle, 'intc': True, 'master': True, 'slave': True,
                        'compatible': compatible, 'intcp': -1, 'irqn': -1}
                if dts.exist_property('#address-cells', pa):
                    flatten_intc_tree[pa]['address-cells'] = \
                        dts.get_property('#address-cells', pa).data[0]
                if dts.exist_property('#interrupt-cells', pa):
                    flatten_intc_tree[pa]['interrupt-cells'] = \
                        dts.get_property('#interrupt-cells', pa).data[0]
            else:
                # here is the intc which will probably not being used
                flatten_intc_tree[pa] = {
                    'intc': True, 'master': False, 'slave': False,
                    'compatible': compatible}
            mmio = find_mmio_by_path(dts, pa)
            if mmio is not None:
                # only you need is the base address
                flatten_intc_tree[pa]['reg'] = mmio['reg'][0]

    flatten_intcs = []
    for k, v in flatten_intc_tree.items():
        v['path'] = k
        flatten_intcs.append(v)

    return flatten_intcs

