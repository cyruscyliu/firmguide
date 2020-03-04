import os
import yaml

from slcore.database.db import Database
from settings import *


class InitValue(Database):
    def select(self, *args, **kwargs):
        """
        select 'iv' where arch='arm' and board='ath79'
        """
        arch = kwargs.pop('arch')
        assert arch in ['arm', 'arm64', 'mips']

        board = kwargs.pop('board', None)

        table = open(os.path.join(BASE_DIR, 'slcore/database', 'iv.{}.yaml'.format(arch)))
        info = yaml.safe_load(table)
        table.close()

        action = args[0]

        if action == 'iv' and board is not None:
            if board in info:
                return info[board]
        return None

    def add(self, *args, **kwargs):
        raise NotImplementedError('you are not expected to modify this table')

    def delete(self, *args, **kwargs):
        raise NotImplementedError('you are not expected to modify this table')

    def update(self, *args, **kwargs):
        raise NotImplementedError('you are not expected to modify this table')

