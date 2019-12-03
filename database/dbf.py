import os

from database.db import DatabaseOpenWRTToH


def get_database(dbtype, **kwargs):
    if dbtype == 'openwrt':
        return DatabaseOpenWRTToH()
    else:
        raise NotImplementedError('the dbtype {} is not support yet'.format(dbtype))
