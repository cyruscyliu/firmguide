import os

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

def __find_interrupt_cells(dts, phandle):
    for pa, no, pros in dts.walk():
        if len(no):
            continue
        if dts.exist_property('interrupt-controller', pa) and \
                dts.exist_property('phandle', pa) and \
                phandle == dts.get_property('phandle', pa).data[0]:
            interrupt_cells = dts.get_property('#interrupt-cells', pa).data[0]
            return interrupt_cells
    return None


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
            raise NotImplementedError(
                'update COMPATIBLE_INTERRUPTS_INDEX for {}'.format(compatible))
    return None


def find_irqn_by_pphandle(dts, pphandle, cell):
    interrupts_index = __find_interrupts_index(dts, pphandle)
    if interrupts_index is None:
        return cell
    else:
        irqn = cell[interrupts_index]
        return irqn


def find_irqnc_by_pphandle(dts, pphandle, cell):
    """
    Precisely, we want to know how many entities we have
    beneath the same path. Say, we have <interrupt-parent> = <0x1>;
    <interrupts> = <0x3, 0x4>; <#interrtup-cells> = <0x1>;(of <0x1>),
    then we get two entities with irqn 0x3, 0x4 respectively.
    They may have the same reg, or they they may not,
    which really doesn't matter.
    """
    interrupts_index = __find_interrupts_index(dts, pphandle)
    interrupt_cells = __find_interrupt_cells(dts, pphandle)
    if interrupts_index is None or interrupt_cells is None:
        return cell

    irqn = []
    for i in range(len(cell) // interrupt_cells):
        irqn.append(cell[interrupts_index + i])
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
        if pnode is None:
            return None
        ppath = os.path.join(pnode.path, pnode.name)
        return find_pphandle_by_path(dts, ppath)
    else:
        return pphandle.data[0]


def find_interrupt_parent_by_path(dts, path):
    """
    Find interrupt-parent with a value, say
        interrupt-parent = <0x1>;
    . Sometimes, interrupt-parent with a value
    and interrupt-parent w/o a value together
    makes us confused. In order to distinguish them,
    we scan all properties in the given node.
    """
    ip = None

    cnode = dts.get_node(path)
    for prop in cnode.props:
        if prop.name == 'interrupt-parent' and \
                hasattr(prop,'data'):
            ip = prop.data[0]

    if ip is None:
        pnode = cnode.parent
        if pnode is None:
            return None
        ppath = os.path.join(pnode.path, pnode.name)
        return find_interrupt_parent_by_path(dts, ppath)
    else:
        return ip


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
                interrupt_parent = find_interrupt_parent_by_path(dts, pa)
                if interrupt_parent is None or \
                        (interrupt_parent is not None and interrupt_parent == phandle):
                    # here is the intc connecting to the cpu
                    flatten_intc_tree[pa] = {
                        'phandle': phandle, 'intc': True, 'master': True, 'slave': True,
                        'compatible': compatible, 'intcp': -1, 'irqn': -1}
                elif interrupt_parent is not None and interrupt_parent != phandle:
                    if not dts.exist_property('interrupts', pa):
                        continue
                    interrupts = dts.get_property('interrupts', pa).data
                    interrupts = find_irqn_by_pphandle(dts, interrupt_parent, interrupts)
                    flatten_intc_tree[pa] = {
                        'phandle': phandle, 'intc': True, 'master': True, 'slave': True,
                        'intcp': interrupt_parent, 'irqn': interrupts,
                        'compatible': compatible}
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
            print(mmio)
            if mmio is not None:
                # only you need is the base address
                flatten_intc_tree[pa]['reg'] = mmio['reg'][0]

    master = None
    flatten_intcs = []
    for k, v in flatten_intc_tree.items():
        v['path'] = k
        if 'intcp' in v and v['intcp'] == -1:
            master = v
        else:
            flatten_intcs.append(v)
    if master is not None:
        flatten_intcs.insert(0, master)

    return flatten_intcs

