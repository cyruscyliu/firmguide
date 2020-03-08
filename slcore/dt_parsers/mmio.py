import os
from slcore.dt_parsers.common import load_dtb


def __find_parent_address(dts, path):
    print('{}.{} is deprecated'.format(__name__, __find_parent_address.__name__))
    # at most 2 levels
    node = dts.get_node(path)
    parent = node.parent

    if parent is None:
        return 0

    path = os.path.join(parent.path, parent.name)
    # there must be one start address
    if dts.exist_property('reg', path):
        return dts.get_property('reg', path).data[0]
    else:
        return 0


def __find_parent_offset(dts, path, x, fx):
    node = dts.get_node(path)
    parent = node.parent

    if parent is None:
        if fx is None:
            return 0
        for k, v in fx.items():
            if k <= x < k + v[1]:
                return (v[0] - k)
        return 0

    path = os.path.join(parent.path, parent.name)
    if dts.exist_property('ranges', path):
        local_address_cells = dts.get_property('#address-cells', path).data[0]
        parent_address_cells = __find_parent_address_sells(dts, path)
        local_size_cells = dts.get_property('#size-cells', path).data[0]
        ranges = dts.get_property('ranges', path)
        if not hasattr(ranges, 'data'):
            return __find_parent_offset(dts, path, x, fx)
        ranges = ranges.data
        bank_size = (local_address_cells + parent_address_cells + local_size_cells )
        fx_parent = {}
        for i in range(0, len(ranges) // bank_size):
            local_address = 0
            for j in range(0, local_address_cells):
                local_address += ranges[i * bank_size + j]
            parent_address = 0
            for j in range(0, parent_address_cells):
                parent_address += ranges[i * bank_size + local_address_cells + j]
            local_size = 0
            for j in range(0, local_size_cells):
                local_size += ranges[i * bank_size + local_address_cells + parent_address_cells + j]
            fx_parent[local_address] = [parent_address, local_size]
        if fx is not None:
            for k, v in fx.items():
                if v[0] in fx_parent:
                    fx[k] = fx_parent[v[0]]
        else:
            fx = fx_parent
    return __find_parent_offset(dts, path, x, fx)


def __find_parent_address_sells(dts, path):
    node = dts.get_node(path)
    parent = node.parent

    if parent is None:
        return None

    path = os.path.join(parent.path, parent.name)
    if dts.exist_property('#address-cells', path):
        return dts.get_property('#address-cells', path).data[0]
    else:
        return __find_parent_address_sells(dts, os.path.join(parent.path, parent.name))


def __find_parent_size_cells(dts, path):
    node = dts.get_node(path)
    parent = node.parent

    if parent is None:
        return None

    path = os.path.join(parent.path, parent.name)
    if dts.exist_property('#size-cells', path):
        return dts.get_property('#size-cells', path).data[0]
    else:
        return __find_parent_size_cells(dts, path)


def find_mmio_by_path(dts, path):
    flatten_mmio = find_flatten_mmio_in_fdt(dts)
    for mmio in flatten_mmio:
        if mmio['path'] == path:
            return mmio


def find_flatten_mmio_in_fdt(dts):
    """Find mmio regions in a machine.

    Args:
        dts(dts): The dts from the load_dtb.

    Returns:
        list: A list of mmio regions in the machine. For example:

        [
            {
                'compatible': ['example,mmio'],
                'path': /example/mmio,
                'regs': [{'base': 0xFFFF0000, 'size': 0x10000}]
            }
        ]
    """
    top_address_cells = dts.get_property('#address-cells', '/').data[0]
    top_size_cells = dts.get_property('#size-cells', '/').data[0]

    mmio = {}
    for pa, no, pros in dts.walk():
        if not dts.exist_property('compatible', pa):
            continue
        if pa.find('partitions') != -1:
            continue
        compatible = dts.get_property('compatible', pa).data
        if 'palmbus' in compatible:
            continue

        size_cells = __find_parent_size_cells(dts, pa)
        if size_cells is None:
            size_cells = top_size_cells
        if size_cells == 0:
            continue
        if not dts.exist_property('reg', pa):
            continue
        if pa == '/memory':
            continue
        address_cells = __find_parent_address_sells(dts, pa)
        if address_cells is None:
            address_cells = top_address_cells
        mmios = dts.get_property('reg', pa).data

        mmio[pa] =  {'regs': [], 'compatible': compatible}
        for i in range(len(mmios) // (size_cells + address_cells)):
            base = 0
            for j in range(address_cells):
                base += mmios[i * (size_cells + address_cells) + j]
            size = 0
            for j in range(size_cells):
                size += mmios[i * (size_cells + address_cells) + address_cells + j]
            offset = __find_parent_offset(dts, pa, base, None)
            if size == 0:
                continue
            mmio[pa]['regs'].append({'base': base + offset, 'size': size})

    flatten_mmio = []
    for k, v in mmio.items():
        v['path'] = k
        flatten_mmio.append(v)

    return flatten_mmio


def find_flatten_mmio(path_to_dtb):
    """Find the mmio regions in a machine.

    Args:
        path_to_dtb(str): The path to the device tree blob.

    Returns:
        list: A list of mmio regions..
    """
    dts = load_dtb(path_to_dtb)
    return find_flatten_mmio_in_fdt(dts)

