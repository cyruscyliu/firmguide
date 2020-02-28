import os
import fdt


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
    """
    path:       the pathe of the node
    compatible: the compatible of the node
    reg:        the absolute address, size paris,
                e.g. reg: [{base: 0, size: 1}, {base: 1, size: 1}]
    """
    top_address_cells = dts.get_property('#address-cells', '/').data[0]
    top_size_cells = dts.get_property('#size-cells', '/').data[0]

    mmio = {}
    for pa, no, pros in dts.walk():
        if not dts.exist_property('compatible', pa):
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

        mmio[pa] =  {'reg': [], 'compatible': dts.get_property('compatible', pa).data}
        for i in range(len(mmios) // (size_cells + address_cells)):
            base = 0
            for j in range(address_cells):
                base += mmios[i * (size_cells + address_cells) + j]
            size = 0
            for j in range(size_cells):
                size += mmios[i * (size_cells + address_cells) + address_cells + j]
            offset = __find_parent_offset(dts, pa, base, None)
            mmio[pa]['reg'].append({'base': base + offset, 'size': size})

    flatten_mmio = []
    for k, v in mmio.items():
        v['path'] = k
        flatten_mmio.append(v)

    return flatten_mmio

