def to_irq(name):
    return '{}_IRQ'.format(name.upper())


def concat(x):
    return ''.join(x.split('_'))


def to_cpu_pp_type(name):
    if name == 'arm11mpcore':
        return 'TYPE_ARM11MPCORE_PRIV'


def to_cpu_pp_state(name):
    if name == 'arm11mpcore':
        return 'ARM11MPCorePriveState'


def to_state(name):
    return '{}State'.format(name.upper())


def to_mmio(name):
    return '{}_mmio'.format(name)


def to_ops(name):
    return '{}_ops'.format(name)


def indent(line, level=1):
    return ' ' * level * 4 + line


def to_type(name):
    return 'TYPE_{}'.format(name.upper())


def to_read(name):
    return '{}_read'.format(name)


def to_write(name):
    return '{}_write'.format(name)


def to_update(name):
    return '{}_update'.format(name)


def to_header(name):
    return '{}_H'.format(name.upper())


def to_upper(name):
    return name.upper()
