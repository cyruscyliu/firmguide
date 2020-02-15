import os
import fdt

from slcore.dt_parsers.mmio import find_parent_address
from slcore.dt_parsers.intc import find_interrupts_index


def __find_path_to_uart(dts):
    supported_uarts = ['ns16550a', 'ns8250']
    path_to_uarts = []
    for pa, no, pros in dts.walk():
        compatible = dts.get_property('compatible', pa)
        if compatible is None:
            continue
        for cmptb in compatible.data:
            if cmptb in supported_uarts:
                path_to_uarts.append(pa)

    if len(path_to_uarts) == 0:
        return None
    return path_to_uarts


def find_flatten_uart_in_fdt(dts, flatten_intc_tree=None, flatten_mmio=None, flatten_pinctrl=None):
    path_to_uarts = __find_path_to_uart(dts)
    if path_to_uarts is None:
        return None

    flatten_uart = {}
    for i, path_to_uart in enumerate(path_to_uarts):
        compatible = dts.get_property('compatible', path_to_uart).data

        if flatten_mmio:
            base = flatten_mmio[path_to_uart]['base']
            size = flatten_mmio[path_to_uart]['size']
        else:
            # top
            top_address_cells = dts.get_property('#address-cells', '/').data[0]
            top_size_cells = dts.get_property('#size-cells', '/').data[0]
            # offset
            offset = get_parent_address(dts, path_to_uart)
            # parent
            size_cells = __find_parent_size_cells(dts, pa)
            if size_cells is None:
                size_cells = top_size_cells
            address_cells = __find_parent_address_sells(dts, pa)
            if address_cells is None:
                address_cells = top_address_cells
            # itself
            mmios = dts.get_property('reg', pa).data
            for i in range(len(mmios) // (size_cells + address_cells)):
                base = 0
                for j in range(address_cells):
                    base += mmios[i * (size_cells + address_cells) + j]
                size = 0
                for j in range(size_cells):
                    size += mmios[i * (size_cells + address_cells) + address_cells + j]
        try:
            baud_rate = dts.get_property('current-speed', path_to_uart).data[0]
        except AttributeError as e:
            baud_rate = 0x1c200
        reg_shift = dts.get_property('reg-shift', path_to_uart).data[0]

        interrupt_parent = dts.get_property('interrupt-parent', path_to_uart).data[0]
        if flatten_intc_tree:
            irqn = flatten_intc_tree[path_to_uart]['interrupts']
        else:
            interrupts = dts.get_property('interrupts', path_to_uart).data
            # ==== get real irqn ====
            interrupts_index = find_interrupts_index(dts, phandle)
            if interrupts_index is None:
                irqn = interrupts
                print('update COMPATIBLE_INTERRUPTS_INDEX for {}'.format(compatible))
            else:
                irqn = interrupts[interrupts_index]
            # ====     done      ====
        flatten_uart[path_to_uart] = {
            'compatible': compatible,
            'base': base, 'size': size, 'irqn': irqn,
            'baud_rate': baud_rate, 'reg_shift': reg_shift,
        }

    return flatten_uart



