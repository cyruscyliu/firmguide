"""
map kernel world to qemu world
"""
import os
import yaml

from fuzzywuzzy import process
from settings import *
from slcore.database.db import Database


class DatabaseQEMUAPIS(Database):
    def select(self, *args, **kwargs):
        """
        select cpu where name like arm,arm11mpcore
        """
        # parse arguments
        device, wanted_property = args[0], args[1]

        # get the database
        qemu_apis = open(os.path.join(BASE_DIR, 'slcore/database', 'qemu.apis.yaml'))
        database_qemu_apis = yaml.safe_load(qemu_apis)
        qemu_apis.close()

        # get choices
        choices = database_qemu_apis[device]
        if wanted_property in choices:
            return choices[wanted_property]
        else:
            return None

    def add(self, *args, **kwargs):
        raise NotImplementedError('you are not expected to modify this table')

    def delete(self, *args, **kwargs):
        raise NotImplementedError('you are not expected to modify this table')

    def update(self, *args, **kwargs):
        raise NotImplementedError('you are not expected to modify this table')


class DatabaseQEMUDevices(Database):
    def select(self, *args, **kwargs):
        """
        select cpu where name like arm,arm11mpcore
        """
        # parse arguments
        device = args[0]
        like = kwargs.pop('like')

        # get the database
        qemu_devcies = open(os.path.join(BASE_DIR, 'slcore/database', 'qemu.devices.yaml'))
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
