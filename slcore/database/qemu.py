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


class DatabaseQEMUModels(Database):
    def select(self, *args, **kwargs):
        """
        select model where compatible=ns16550a
        """
        # parse arguments
        action = args[0]
        compatible = kwargs.pop('compatible', None)

        # get the database
        qemu_models = open(os.path.join(DATABASE_DIR, 'qemu.{}.yaml'.format(self.t)))
        database_qemu_models = yaml.safe_load(qemu_models)
        qemu_models.close()

        if action == 'model' and compatible is not None:
            if compatible in database_qemu_models:
                return database_qemu_models[compatible]

    def add(self, *args, **kwargs):
        raise NotImplementedError('you are not expected to modify this table')

    def delete(self, *args, **kwargs):
        raise NotImplementedError('you are not expected to modify this table')

    def update(self, *args, **kwargs):
        raise NotImplementedError('you are not expected to modify this table')

    def __init__(self, t):
        super().__init__()
        self.t = t


class DatabaseQEMUDevices(Database):
    def select(self, *args, **kwargs):
        """
        select cpu where compatible=arm,arm11mpcore
        """
        # parse arguments
        device = args[0]
        compatible = kwargs.pop('compatible', None)

        # get the database
        qemu_devices = open(os.path.join(DATABASE_DIR, 'qemu.devices.yaml'))
        database_qemu_devices = yaml.safe_load(qemu_devices)
        qemu_devices.close()

        # get choices
        choices = database_qemu_devices[device]

        result = None
        if device == 'cpu' and compatible is not None:
            if compatible in choices:
                result = choices[compatible][0]
        return result

    def add(self, *args, **kwargs):
        raise NotImplementedError('you are not expected to modify this table')

    def delete(self, *args, **kwargs):
        raise NotImplementedError('you are not expected to modify this table')

    def update(self, *args, **kwargs):
        raise NotImplementedError('you are not expected to modify this table')

