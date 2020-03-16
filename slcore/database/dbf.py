from slcore.database.qemu import DatabaseQEMUDevices,\
    DatabaseQEMUModels, DatabaseQEMUAPIS
from slcore.database.support import SupportMachines
from slcore.database.iv import InitValue


def get_database(dbtype, **kwargs):
    """Database factory."""
    if dbtype == 'qemu.devices':
        return DatabaseQEMUDevices()
    elif dbtype == 'qemu.cpu':
        return DatabaseQEMUModels('cpu')
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
    elif dbtype == 'qemu.apis':
        return DatabaseQEMUAPIS()
    elif dbtype == 'support':
        return SupportMachines()
    elif dbtype == 'iv':
        return InitValue()
    else:
        raise NotImplementedError('the dbtype {} is not support yet'.format(dbtype))
