from slcore.database.qemu import DatabaseQEMUModels
from slcore.database.machines import SupportMachines


def get_database(dbtype, **kwargs):
    """Database factory."""
    if dbtype == 'qemu.cpu':
        return DatabaseQEMUModels('cpu')
    elif dbtype == 'qemu.ram':
        return DatabaseQEMUModels('ram')
    elif dbtype == 'qemu.serial':
        return DatabaseQEMUModels('serial')
    elif dbtype == 'qemu.intc':
        return DatabaseQEMUModels('intc')
    elif dbtype == 'qemu.timer':
        return DatabaseQEMUModels('timer')
    elif dbtype == 'qemu.clk':
        return DatabaseQEMUModels('clk')
    elif dbtype == 'qemu.flash':
        return DatabaseQEMUModels('flash')
    elif dbtype == 'qemu.misc':
        return DatabaseQEMUModels('misc')
    elif dbtype == 'qemu.mmio':
        return DatabaseQEMUModels('mmio')
    elif dbtype == 'support':
        return SupportMachines()
    else:
        raise NotImplementedError(
            'the dbtype {} is not support yet'.format(dbtype))
