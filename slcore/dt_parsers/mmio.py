import os
import fdt


def find_parent_address(dts, path):
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


def find_flatten_mmio_in_fdt(dts):
    top_address_cells = dts.get_property('#address-cells', '/').data[0]
    top_size_cells = dts.get_property('#size-cells', '/').data[0]

    flatten_mmio = {}
    for pa, no, pros in dts.walk():
        if pa.find('pinctrl') != -1:
            continue
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

        # if it has offsets
        offset = find_parent_address(dts, pa)
        for i in range(len(mmios) // (size_cells + address_cells)):
            base = 0
            for j in range(address_cells):
                base += mmios[i * (size_cells + address_cells) + j]
            size = 0
            for j in range(size_cells):
                size += mmios[i * (size_cells + address_cells) + address_cells + j]
            flatten_mmio[pa] = {'base': base + offset, 'size': size}
    return flatten_mmio

