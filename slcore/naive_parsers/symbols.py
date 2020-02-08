import os

def parse_system_map(path, bits=32):
    """
    ffffffff803687e8 T arch_init_irq
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
    """
    addr2file -e path/to/binary address
    """
    dir_of_binary = os.path.realpath(os.path.dirname(path))

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

