import os
from slcore.dt_parsers.mmio import find_mmio_by_path
from slcore.dt_parsers.compatible import find_compatible_by_path
from slcore.dt_parsers.common import load_dtb


COMPATIBLE_INTERRUPTS_INDEX = {
    'arm,gic-400': 1,
    'arm,cortex-a15-gic': 1,
    'arm,cortex-a9-gic': 1,
    'arm,cortex-a7-gic': 1,
    'arm,arm11mp-gic': 1,
    'brcm,brahma-b15-gic': 1,
    'atmel,at91rm9200-aic': 0,
    'atmel,sama5d2-aic': 0,
    'atmel,sama5d3-aic': 0,
    'atmel,sama5d4-aic': 0,
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


def find_irqnc_by_pphandle(dts, pphandle, cell):
    """Find all irq numbers.

    Precisely, we want to know how many entities we have
    beneath the same path. Say, we have <interrupt-parent> = <0x1>;
    <interrupts> = <0x3, 0x4>; <#interrtup-cells> = <0x1>;(of <0x1>),
    then we get two entities with irqn 0x3, 0x4 respectively.
    """
    interrupts_index = __find_interrupts_index(dts, pphandle)
    interrupt_cells = __find_interrupt_cells(dts, pphandle)
    if interrupts_index is None or interrupt_cells is None:
        return []

    irqn = []
    for i in range(len(cell) // interrupt_cells):
        irqn.append(cell[interrupts_index + i])
    return irqn


def find_intc_by_phandle(dts, phandle):
    """Find the interrupt controller by phandle."""
    flatten_intcs = find_flatten_intc_in_fdt(dts)
    for intc in flatten_intcs:
        if intc['phandle'] == phandle:
            return intc


def find_pphandle_by_path(dts, path):
    """Find the phandle of a interrupt controller by path."""
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
    """Find the interrupt parent phandle by path.

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


def __construct_nointc_slave(dts, pa):
    nointc_slave = {}

    compatible = find_compatible_by_path(dts, pa)
    if dts.exist_property('interrupts', pa):
        interrupts = dts.get_property('interrupts', pa).data
        interrupt_parent = find_interrupt_parent_by_path(dts, pa)
        interrupts = find_irqnc_by_pphandle(dts, interrupt_parent, interrupts)
        nointc_slave = {
            'compatible': compatible, 'irqns': interrupts, 'intcp': interrupt_parent,
            'intc': False, 'master': False, 'slave': True
        }
        return nointc_slave
    return None


def __construct_intc(dts, pa):
    intc = {}

    compatible = find_compatible_by_path(dts, pa)
    if dts.exist_property('phandle', pa):
        phandle = dts.get_property('phandle', pa).data[0]
        interrupt_parent = find_interrupt_parent_by_path(dts, pa)
        if interrupt_parent is None or \
                (interrupt_parent is not None and interrupt_parent == phandle):
            # here is the intc connecting to the cpu
            intc = {
                'phandle': phandle, 'intc': True, 'master': True, 'slave': True,
                'compatible': compatible, 'intcp': -1, 'irqns': [-1]}
        elif interrupt_parent is not None and interrupt_parent != phandle:
            if not dts.exist_property('interrupts', pa):
                return None
            interrupts = dts.get_property('interrupts', pa).data
            interrupts = find_irqnc_by_pphandle(dts, interrupt_parent, interrupts)
            intc = {
                'phandle': phandle, 'intc': True, 'master': True, 'slave': True,
                'intcp': interrupt_parent, 'irqns': interrupts,
                'compatible': compatible}
        if dts.exist_property('#address-cells', pa):
            intc['address-cells'] = \
                dts.get_property('#address-cells', pa).data[0]
        if dts.exist_property('#interrupt-cells', pa):
            intc['interrupt-cells'] = \
                dts.get_property('#interrupt-cells', pa).data[0]
    else:
        # here is the intc which will probably not being used
        intc = {
            'intc': True, 'master': False, 'slave': False,
            'compatible': compatible}
    mmio = find_mmio_by_path(dts, pa)
    if mmio is not None:
        intc['regs'] = mmio['reg']
    return intc


def find_flatten_intc_in_fdt(dts, nonintc_slave=False):
    """Find interrupt controller in the machine.

    Args:
        dts(dts)           : The dts from load_dtb.
        nonintc_slave(bool): Whether or not return slaves which are not interrupt controllers.

    Return:
        list: A list of interrupt controllers. For example:

        [
            {
                'compatible': ['example,intc'],
                'path': /example/intc,
                'regs': [{'base': 0xFFFF0000, 'size': 0x10000}],
                'intc': True,
                'phandle': 1,
                'master': True,
                'slave': True,
                'intcp': -1,
                'irqns': [0],
            }
        ]
    """
    flatten_intc_tree = {}
    for pa, no, pros in dts.walk():
        if len(no):
            continue
        if dts.exist_property('interrupt-controller', pa):
            intc = __construct_intc(dts, pa)
            if intc is None:
                continue
            flatten_intc_tree[pa] = intc
        elif nonintc_slave:
            nointc_slave = __construct_nointc_slave(dts, pa)
            if nointc_slave is None:
                continue
            flatten_intc_tree[pa] = nointc_slave

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


def find_flatten_intc(path_to_dtb):
    """Find the interrupt controllers in a machine.

    Args:
        path_to_dtb(str): The path to the device tree blob.

    Returns:
        list: A list of interrupt controller chips.
    """
    dts = load_dtb(path_to_dtb)
    return find_flatten_intc_in_fdt(dts)

