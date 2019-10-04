import os

from database.db import DatabaseText, DatabaseOpenWrt


def get_database(dbtype, **kwargs):
    if dbtype == 'text':
        return DatabaseText(os.path.join('database', 'firmware'), **kwargs)
    elif dbtype == 'openwrt':
        return DatabaseOpenWrt()
    else:
        raise NotImplementedError('the dbtype {} is not support yet'.format(dbtype))
