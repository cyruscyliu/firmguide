import os
from slcore.dt_parsers.common import load_dtb
from slcore.dt_parsers.compatible import find_compatible_by_path


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


def find_parent_offset(dts, path, x, fx, debug=False):
    """Find the offset of the parent node.

    Args:
        dts(dts) : The dts from load_dtb.
        path(str): The path to current node.
        x(int)   : The base value to be corrected.
        fx(dict) : Address mapping. Must be None when called from the external.

    Returns:
        int: The offset of the parent node.
    """
    node = dts.get_node(path)
    parent = node.parent

    if parent is None:
        if fx is None:
            return 0
        for k, v in fx.items():
            if k <= x < k + v[1]:
                if debug:
                    print('[+] {} {:x}: {:x} {:x} {:x}'.format(path, x, k, v[0], v[1]))
                return (v[0] - k)
        # Then the bus has no mapping for x.
        return None

    path = os.path.join(parent.path, parent.name)
    if dts.exist_property('ranges', path):
        local_address_cells = dts.get_property('#address-cells', path).data[0]
        parent_address_cells = __find_parent_address_sells(dts, path)
        local_size_cells = dts.get_property('#size-cells', path).data[0]
        ranges = dts.get_property('ranges', path)
        if not hasattr(ranges, 'data'):
            return find_parent_offset(dts, path, x, fx, debug=debug)
        ranges = ranges.data
        if debug:
            print('[+] {} range cells: {:x} {:x} {:x}'.format(
                path, local_address_cells, parent_address_cells, local_size_cells))
        bank_size = \
            (local_address_cells + parent_address_cells + local_size_cells)
        fx_parent = {}
        for i in range(0, len(ranges) // bank_size):
            if debug:
                print('[+] {} bank {} {}'.format(
                    path, i, ranges[i * bank_size: (i + 1) * bank_size]))
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
            if debug:
                print('[+] {} bank {} => {:x} {:x} {:x}'.format(
                    path, i, local_address, parent_address, local_size))
        if fx is not None:
            for ok, ov in fx.items():
                for nk, nv in fx_parent.items():
                    if nk <= ov[0] < nk + nv[1]:
                        ov[0] = ov[0] - nk + nv[0]
        else:
            fx = fx_parent
    return find_parent_offset(dts, path, x, fx, debug=debug)


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


def find_mmio_by_path(dts, path, memory=False):
    """Find mmio regions by path."""
    flatten_mmio = find_flatten_mmio_in_fdt(dts, memory=memory)
    for mmio in flatten_mmio:
        if mmio['path'] == path:
            return mmio


def find_flatten_mmio_in_fdt(dts, memory=False):
    """Find mmio regions in a machine.

    Args:
        dts(dts): The dts from the load_dtb.

    Returns:
        list: A list of mmio regions in the machine. For example:
        [{'compatible': ['example,mmio'], 'path': /example/mmio,
        'regs': [{'base': 0xFFFF0000, 'size': 0x10000, 'priority': 0}]}]
    """
    top_address_cells = dts.get_property('#address-cells', '/').data[0]
    top_size_cells = dts.get_property('#size-cells', '/').data[0]

    mmio = {}
    for pa, no, pros in dts.walk():
        if pa.find('partition') != -1:
            continue
        compatible = find_compatible_by_path(dts, pa)
        if 'palmbus' in compatible:
            continue

        size_cells = __find_parent_size_cells(dts, pa)
        if size_cells is None:
            size_cells = top_size_cells
        if size_cells == 0:
            continue
        pcie_io = False
        if not dts.exist_property('reg', pa):
            if not dts.exist_property('pcie-io-aperture', pa):
                continue
            else:
                pcie_io = True
        if not memory and pa.startswith('/memory'):
            continue
        address_cells = __find_parent_address_sells(dts, pa)
        if address_cells is None:
            address_cells = top_address_cells
        if not pcie_io:
            mmios = dts.get_property('reg', pa).data
        if dts.exist_property('assigned-addresses', pa):
            mmios = dts.get_property('assigned-addresses', pa).data
            mmios[0] &= 0xffff0000
        if dts.exist_property('pcie-io-aperture', pa):
            # pcie-io-aperture = <0xF2000000 0x100000>;
            mmios = dts.get_property('pcie-io-aperture', pa).data

        mmio[pa] =  {'regs': [], 'compatible': compatible}
        for i in range(len(mmios) // (size_cells + address_cells)):
            base = 0
            for j in range(address_cells):
                base += mmios[i * (size_cells + address_cells) + j]
            size = 0
            for j in range(size_cells):
                size += mmios[i * (size_cells + address_cells) + address_cells + j]
            offset = find_parent_offset(dts, pa, base, None)
            if offset is None:
                continue
            if size == 0:
                continue
            base = base + offset
            # sometimes we get a size 0xffffffff...
            if base + size > (1 << 32):
                size = (1 << 32) - base
            mmio[pa]['regs'].append(
                {'base': base, 'size': size, 'priority': 0})

    flatten_mmio = []
    for k, v in mmio.items():
        v['path'] = k
        flatten_mmio.append(v)

    return flatten_mmio


def merge_flatten_mmio(flatten_mmio):
    """Merge flatten mmio regions with same compatible."""
    merged_flatten_mmio = []

    compatibles = []
    for mmio in flatten_mmio:
        if 'simple-bus' in mmio['compatible']:
            mmio['compatible'].remove('simple-bus')
        if mmio['compatible'] not in compatibles:
            compatibles.append(mmio['compatible'])
            merged_flatten_mmio.append(mmio)
        else:
            index = compatibles.index(mmio['compatible'])
            merged_flatten_mmio[index]['regs'].extend(mmio['regs'])
            merged_flatten_mmio[index]['regs'] = \
                sorted(merged_flatten_mmio[index]['regs'],
                       key=lambda x: x['base'])
    return merged_flatten_mmio


def find_flatten_mmio(path_to_dtb):
    """Find the mmio regions in a machine.

    Args:
        path_to_dtb(str): The path to the device tree blob.

    Returns:
        list: A list of mmio regions..
    """
    dts = load_dtb(path_to_dtb)
    return find_flatten_mmio_in_fdt(dts)
