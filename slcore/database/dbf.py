import os

from database.qemu import DatabaseQEMUDevices, DatabaseQEMUAPIS
from database.openwrt import DatabaseOpenWRTMapping, DatabaseOpenWRTToH
from database.support import SupportMachines


def get_database(dbtype, **kwargs):
    if dbtype == 'openwrt':
        return DatabaseOpenWRTToH()
    elif dbtype == 'openwrt.yaml':
        return DatabaseOpenWRTMapping()
    elif dbtype == 'qemu.devices':
        return DatabaseQEMUDevices()
    elif dbtype == 'qemu.apis':
        return DatabaseQEMUAPIS()
    elif dbtype == 'support':
        return SupportMachines()
    else:
        raise NotImplementedError('the dbtype {} is not support yet'.format(dbtype))
