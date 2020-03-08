from slcore.dt_parsers.mmio import find_mmio_by_path
from slcore.dt_parsers.compatible import find_compatible_by_path
from slcore.dt_parsers.intc import \
    find_interrupt_parent_by_path, find_irqnc_by_pphandle
from slcore.dt_parsers.common import load_dtb


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
    """Find flatten serials in a machine.

    Args:
        dts(dts): The dts from load_dtb.

    Returns:
        list: A list of serials in a machine. For example:

        [
            {
                'compatible': ['example,serial'],
                'path': /example/serial,
                'regs': [{'base': 0xFFFF0000, 'size': 0x10000}],
                'baud_rate': 115200,
                'reg_shift': 0, # or 2
                'intcp': -1, # optional
                'irqns': [0] # optional
            }
        ]
    """
    path_to_serials = __find_path_to_serial(dts)
    if path_to_serials is None:
        return None

    flatten_serial = []
    for i, path_to_serial in enumerate(path_to_serials):
        compatible = find_compatible_by_path(dts, path_to_serial)

        mmio = find_mmio_by_path(dts, path_to_serial)
        # we only need the base address
        reg = mmio['regs']

        try:
            baud_rate = dts.get_property('current-speed', path_to_serial).data[0]
        except AttributeError as e:
            baud_rate = 0x1c200
        reg_shift = dts.get_property('reg-shift', path_to_serial)
        if reg_shift is not None:
            reg_shift = reg_shift.data[0]
        else:
            continue


        interrupt_parent = find_interrupt_parent_by_path(dts, path_to_serial)
        interrupts = dts.get_property('interrupts', path_to_serial).data
        irqns = find_irqnc_by_pphandle(dts, interrupt_parent, interrupts)

        flatten_serial.append({
            'path': path_to_serial, 'compatible': compatible,
            'regs': reg, 'irqn': irqns[0], 'intcp': interrupt_parent,
            'baud_rate': baud_rate, 'reg_shift': reg_shift, 'id': i
        })

    return flatten_serial


def find_flatten_serial(path_to_dtb):
    """Find the timers in a machine.

    Args:
        path_to_dtb(str): The path to the device tree blob.

    Returns:
        list: A list of serial chips.
    """
    dts = load_dtb(path_to_dtb)
    return find_flatten_serial_in_fdt(dts)


