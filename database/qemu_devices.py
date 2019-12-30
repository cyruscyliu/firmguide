"""
map kernel world to qemu world
"""
import os
import yaml

from fuzzywuzzy import process

from database.db import Database


class DatabaseQEMUDevices(Database):
    def select(self, *args, **kwargs):
        """
        select cpu where name like arm,arm11mpcore
        """
        # parse arguments
        device = args[0]
        like = kwargs.pop('like')

        # get the database
        qemu_devcies = open(os.path.join(os.getcwd(), 'database', 'qemu_devices.yaml'))
        database_qemu_devices = yaml.safe_load(qemu_devcies)

        # get choices
        choices = database_qemu_devices[device]

        result = None
        if device == 'cpu':
            if like in choices:
                result = choices[like][0]
        elif device == 'cpu_private':
            if like in choices:
                result = choices[like]
        qemu_devcies.close()
        return result

    def add(self, *args, **kwargs):
        raise NotImplementedError('you are not expected to modify this table')

    def delete(self, *args, **kwargs):
        raise NotImplementedError('you are not expected to modify this table')

    def update(self, *args, **kwargs):
        raise NotImplementedError('you are not expected to modify this table')
