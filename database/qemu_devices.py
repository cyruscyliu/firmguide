"""
map kernel world to qemu world
"""
from database.db import Database


class DatabaseQEMUDevices(Database):
    def select(self, *args, **kwargs):
        """
        select cpu where name like arm,arm11mpcore
        """
        pass

    def add(self, *args, **kwargs):
        raise NotImplementedError('you are not expected to modify this table')

    def delete(self, *args, **kwargs):
        raise NotImplementedError('you are not expected to modify this table')

    def update(self, *args, **kwargs):
        raise NotImplementedError('you are not expected to modify this table')
