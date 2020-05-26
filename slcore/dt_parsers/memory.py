from slcore.dt_parsers.common import load_dtb
from slcore.dt_parsers.mmio import find_mmio_by_path


def __get_ram_generic():
    return [{'regs': [{'base': 0, 'size': 256 * 1024 * 1024, 'priority': 0}],
            'compatible': ['ram,generic'], 'path': '/memory'}]


def __validate_ram_size(memory):
    for reg in memory[0]['regs']:
        reg['priority'] = 0

    if len(memory[0]['regs']) == 1 and \
            memory[0]['regs'][0]['size'] == 0:
        memory[0]['regs']['size'] = 256 * 1024 * 1024

    return memory


def __find_memory_path(dts):
    """/memory or /memory@0"""
    for path, nodes, props in dts.walk():
        # the memory node is just in the root node
        if path.strip('/').find('/') != -1:
            continue
        # there is one and only one memory block
        if path.strip('/').startswith('memory'):
            return path
    return None


def find_memory_in_fdt(dts):
    """Find the memory configuration in a machine.

    Args:
        dts(dts): The dts from load_dtb.

    Returns:
        dict: A list of the memory node in the machine. For example:
        [{'regs': [{'base': 0, 'size': 8192}], 'compatible':
        ['test,compatible'], 'path': '/memory'}]
    """
    path_to_memory = __find_memory_path(dts)

    if path_to_memory is None:
        return __get_ram_generic()

    memory = [find_mmio_by_path(dts, path_to_memory, memory=True)]
    assert memory[0] is not None, 'bugs in find_mmio_by_path'

    if len(memory[0]['regs']) == 0:
        memory = __get_ram_generic()

    __validate_ram_size(memory)

    memory[0]['regs'] = \
        sorted(memory[0]['regs'], key=lambda x: x['base'])

    return memory


def find_memory(path_to_dtb):
    """Find the first cpu in a machine.

    Args:
        path_to_dtb(str): The path to the device tree blob.

    Returns:
        dict: A list of the memory node in the machine. For example:
        [{'regs': [{'base': 0, 'size': 8192}], 'compatible':
        ['test,compatible'], 'path': '/memory'}]
    """
    dts = load_dtb(path_to_dtb)
    memory = find_memory_in_fdt(dts)

    if memory is None:
        return __get_ram_generic()

    __validate_ram_size(memory)
    return memory


find_flatten_ram_in_fdt = find_memory_in_fdt
