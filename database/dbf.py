import os

from database.db import DatabaseOpenWRTToH, DatabasePaused
from database.firmware import DatabaseFirmadyne, DatabaseText


def get_database(dbtype, **kwargs):
    if dbtype == 'text':
        return DatabaseText(os.path.join('database', 'firmware.text'), **kwargs)
    elif dbtype == 'firmadyne':
        return DatabaseFirmadyne(os.path.join('database', 'firmware.firmadyne'), **kwargs)
    elif dbtype == 'openwrt':
        return DatabaseOpenWRTToH()
    elif dbtype == 'paused':
        return DatabasePaused()
    else:
        raise NotImplementedError('the dbtype {} is not support yet'.format(dbtype))
