import os
import yaml

from database.db import Database


class SupportMachines(Database):
    def select(self, *args, **kwargs):
        """
        select target where arch='arm32' returns True or False
        select target where arch='mips' returns True or False
        """
        target = args[0]
        arch = kwargs.pop('arch')
        assert arch in ['arm32', 'mips']

        table = open(os.path.join(os.getcwd(), 'database', 'support.{}.yaml'.format(arch)))
        info = yaml.safe_load(table)

        status = False
        if target in info['support']:
            status = True

        table.close()
        return status

    def add(self, *args, **kwargs):
        raise NotImplementedError('you are not expected to modify this table')

    def delete(self, *args, **kwargs):
        raise NotImplementedError('you are not expected to modify this table')

    def update(self, *args, **kwargs):
        raise NotImplementedError('you are not expected to modify this table')
