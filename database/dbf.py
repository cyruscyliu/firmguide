from database.db import DatabaseText


def get_database(dbtype, **kwargs):
    if dbtype == 'text':
        path = kwargs.pop('tdb', 'openwrt_arm_el')
        return DatabaseText(path)
    else:
        raise NotImplementedError('the dbtype {} is not support yet'.format(dbtype))