import os
import fdt

from slcore.dt_parsers.mmio import *
from slcore.dt_parsers.intc import *


def __find_path_to_serial(dts):
    supported_serials = ['ns16550a', 'ns8250']
    path_to_serials = []
    for pa, no, pros in dts.walk():
        compatible = dts.get_property('compatible', pa)
        if compatible is None:
            continue
        for cmptb in compatible.data:
            if cmptb in supported_serials:
                path_to_serials.append(pa)

    if len(path_to_serials) == 0:
        return None
    return path_to_serials


def find_flatten_serial_in_fdt(dts):
    """
    baud_rate:   always, the baud rate of a uart, by default 0x1c200
    reg:         always, see find_mmio_by_path for details
    reg_shift:   always, the reg shift of a uart
    path:        always, the path of the node
    compatilble: always, the compatible of the node
    intcp:       always, the phandle of the parent interrupt controller
    irqn:        always, the irq number to which the slave device connect
    id:          always, the nth serial device
    """
    path_to_serials = __find_path_to_serial(dts)
    if path_to_serials is None:
        return None

    flatten_serial = []
    for i, path_to_serial in enumerate(path_to_serials):
        compatible = dts.get_property('compatible', path_to_serial).data

        mmio = find_mmio_by_path(dts, path_to_serial)
        # we only need the base address
        reg = mmio['reg'][0]

        try:
            baud_rate = dts.get_property('current-speed', path_to_serial).data[0]
        except AttributeError as e:
            baud_rate = 0x1c200
        reg_shift = dts.get_property('reg-shift', path_to_serial).data[0]

        interrupt_parent = dts.get_property('interrupt-parent', path_to_serial).data[0]
        interrupts = dts.get_property('interrupts', path_to_serial).data
        irqn = find_irqn_by_pphandle(dts, interrupt_parent, interrupts)

        flatten_serial.append({
            'path': path_to_serial, 'compatible': compatible,
            'reg': reg, 'irqn': irqn, 'intcp': interrupt_parent,
            'baud_rate': baud_rate, 'reg_shift': reg_shift, 'id': i
        })

    return flatten_serial

