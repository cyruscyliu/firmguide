import os

from database.db import DatabaseText, DatabaseOpenWrt, DatabaseFirmadyne, DatabasePaused


def get_database(**kwargs):
    dbtype = kwargs.pop('dbtype', None)
    uuid = kwargs.pop('uuid', None)
    if dbtype == 'text':
        return DatabaseText(os.path.join('database', 'firmware.text'), **kwargs)
    elif dbtype == 'firmadyne':
        return DatabaseFirmadyne(os.path.join('database', 'firmware.firmadyne'), **kwargs)
    elif dbtype == 'openwrt':
        return DatabaseOpenWrt()
    elif dbtype is None and uuid is not None:
        return DatabasePaused(os.path.join('database', 'firmware.paused'), **kwargs)
    else:
        raise NotImplementedError('the dbtype {} is not support yet'.format(dbtype))
