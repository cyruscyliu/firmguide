"""
map kernel world to qemu world
"""
import os
import yaml

from slcore.database.db import Database


class DatabaseQEMUModels(Database):
    def select(self, *args, **kwargs):
        """
        Examples:
            select model where compatible=ns16550a
            select *
            select fix_parameters where compatible=ns16550a
        """
        # parse arguments
        action = args[0]
        compatible = kwargs.pop('compatible', None)

        # get the database
        database_dir = os.path.dirname(os.path.realpath(__file__))
        if action == 'fix_parameters':
            qemu_models = open(os.path.join(
                database_dir, 'fixparameters/qemu.{}.yaml'.format(self.t)))
        else:
            qemu_models = open(os.path.join(
                database_dir, 'bricktemplate/qemu.{}.yaml'.format(self.t)))
        database_qemu_models = yaml.safe_load(qemu_models)
        qemu_models.close()

        if action == 'model' and compatible is not None:
            if compatible in database_qemu_models:
                return database_qemu_models[compatible]
        elif action == '*':
            return database_qemu_models
        elif action == 'fix_parameters':
            if compatible in database_qemu_models:
                return database_qemu_models[compatible]
        return None

    def add(self, *args, **kwargs):
        """
        Examples:
            add compatible where pa=va, pb=vb
        """
        compatible = args[0]

        qdevices = self.select('*')
        if qdevices is None:
            qdevices = {compatible: kwargs}
        else:
            if compatible not in qdevices:
                qdevices[compatible] = kwargs

        database_dir = os.path.dirname(os.path.realpath(__file__))
        f = open(os.path.join(
            database_dir, 'bricktemplate/qemu.{}.yaml'.format(self.t)), 'w')
        yaml.safe_dump(qdevices, f)
        f.close()

    def delete(self, *args, **kwargs):
        raise NotImplementedError('you are not expected to modify this table')

    def update(self, *args, **kwargs):
        raise NotImplementedError('you are not expected to modify this table')

    def __init__(self, t):
        super().__init__()
        self.t = t
