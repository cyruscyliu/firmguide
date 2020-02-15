import os
import fdt


COMPATIBLE_INTERRUPTS_INDEX = {
    'arm,gic-400': 1,
    'arm,cortex-a15-gic': 1,
    'arm,cortex-a9-gic': 1,
    'arm,cortex-a7-gic': 1,
    'arm,arm11mp-gic': 1,
    'brcm,brahma-b15-gic': 1,
}

def find_interrupts_index(dts, phandle):
    for pa, no, pros in dts.walk():
        if len(no):
            continue
        if dts.exist_property('interrupt-controller', pa) and \
                dts.exist_property('phandle', pa) and \
                phandle == dts.get_property('phandle', pa).data[0]:
            interrupt_cells = dts.get_property('#interrupt-cells', pa).data[0]
            if interrupt_cells == 1:
                return 0
            # in this situation, we should find the index in the table
            compatible = dts.get_property('compatible', pa).data
            for cmptb in compatible:
                if cmptb in COMPATIBLE_INTERRUPTS_INDEX:
                    return COMPATIBLE_INTERRUPTS_INDEX[cmptb]
    return None


def find_flatten_intc_tree_in_fdt(dts):
    flatten_intc_tree = {}
    for pa, no, pros in dts.walk():
        if len(no):
            continue
        if dts.exist_property('interrupt-controller', pa):
            compatible = dts.get_property('compatible', pa)
            if compatible is None:
                compatible = dts.get_property('compatible', os.path.dirname(pa))
            else:
                compatible = compatible.data
            if dts.exist_property('phandle', pa):
                phandle = dts.get_property('phandle', pa).data[0]
                if dts.exist_property('interrupt-parent', pa):
                    interrupt_parent = dts.get_property('interrupt-parent', pa).data[0]
                    interrupts = dts.get_property('interrupts', pa).data
                    # ==== get real irqn ====
                    interrupts_index = find_interrupts_index(dts, interrupt_parent)
                    if interrupts_index is None:
                        print('update COMPATIBLE_INTERRUPTS_INDEX for {}'.format(compatible))
                    else:
                        interrupts = interrupts[interrupts_index]
                    # ====     done      ====
                    flatten_intc_tree[pa] = {
                        'phandle': phandle, 'intc': True, 'master': True, 'slave': True,
                        'interrupt_parent': interrupt_parent, 'interrupts': interrupts,
                        'compatible': compatible}
                else:
                    flatten_intc_tree[pa] = {
                        'phandle': phandle, 'intc': True, 'master': True, 'slave': False,
                        'compatible': compatible}
                if dts.exist_property('#address-cells', pa):
                    flatten_intc_tree[pa]['address-cells'] = \
                        dts.get_property('#address-cells', pa).data[0]
                if dts.exist_property('#interrupt-cells', pa):
                    flatten_intc_tree[pa]['interrupt-cells'] = \
                        dts.get_property('#interrupt-cells', pa).data[0]
            else:
                flatten_intc_tree[pa] = {
                    'intc': True, 'master': False, 'slave': False,
                    'compatible': compatible}
        elif dts.exist_property('interrupt-parent', pa):
            compatible = dts.get_property('compatible', pa).data
            interrupt_parent = dts.get_property('interrupt-parent', pa).data[0]
            interrupts = dts.get_property('interrupts', pa).data
            # ==== get real irqn ====
            interrupts_index = find_interrupts_index(dts, interrupt_parent)
            if interrupts_index is None:
                print('update COMPATIBLE_INTERRUPTS_INDEX for {}'.format(compatible))
            else:
                interrupts = interrupts[interrupts_index]
            # ====     done      ====
            flatten_intc_tree[pa] = {
                'intc': False, 'slave': True,
                'interrupt_parent': interrupt_parent, 'interrupts': interrupts,
                'compatible': compatible}

    return flatten_intc_tree

