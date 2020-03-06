import os


def parse_system_map(path, bits=32):
    """Parse system map, get the address, the type, and the symbol in the lines.

    Example: ffffffff803687e8 T arch_init_irq

    :param path: The path to the System.map.
    :type  path: str
    :param bit : How many bits of an address, default is 32.
    :type  bit : int
    :returns   : The dict with symbols as keys, like {__start: {'addr': 0x00000000, 'type': T}}
    :rtype     : dict
    """
    system_map = {}

    if bits == 32:
        mask = 0xffffffff
    else:
        mask = 0xffffffffffffffff >> (64 - bits)

    with open(path) as f:
        for line in f:
            addr, type_, sym = line.strip().split()
            system_map[sym] = {'addr': int(addr, 16) & mask, 'type': type_}
    return system_map


def addr2file(path, address):
    """Find the file according to the address.

    A wrapper of addr2line.

    :param path   : The path to the binary.
    :type  path   : str
    :param address: The address you want to watch.
    :type  address: str
    :returns      : The path w.s.t the address.
    :rtype        : str
    """
    # /abs/path/to/x.c:69
    with os.popen('addr2line -e {} {}'.format(path, hex(address))) as o:
        output = o.readlines()
    if not len(output):
        return None
    assert len(output) == 1

    if output[0].startswith('??'):
        return None

    f, l = output[0].split(':')
    f = os.path.realpath(f)

    return f

