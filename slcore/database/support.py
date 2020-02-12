import os
import yaml

from slcore.database.db import Database
from settings import *


class SupportMachines(Database):
    def select(self, *args, **kwargs):
        """
        select 'profile' where arch='arm' and machine_id='0x661'
        select 'profile' where arch='arm' and compatible='plxtech,nas7820'
        """
        arch = kwargs.pop('arch')
        assert arch in ['arm', 'arm64', 'mips']
        machine_id = kwargs.pop('machine_id', None)
        compatible = kwargs.pop('compatible', None)
        target = kwargs.pop('target', None)

        table = open(os.path.join(BASE_DIR, 'slcore/database', 'support.{}.yaml'.format(arch)))
        info = yaml.safe_load(table)
        table.close()

        action = args[0]

        if action == 'profile' and machine_id is not None:
            for k, v in info.items():
                if 'machine_ids' in v and machine_id in v['machine_ids']:
                    return os.path.join(BASE_DIR, v['profile'])
        elif action == 'profile' and compatible is not None:
            for k, v in info.items():
                if 'compatible' in v and compatible in v['compatible']:
                    return os.path.join(BASE_DIR, v['profile'])
        elif action == 'support':
            assert target is not None
            return target in info

    def add(self, *args, **kwargs):
        raise NotImplementedError('you are not expected to modify this table')

    def delete(self, *args, **kwargs):
        raise NotImplementedError('you are not expected to modify this table')

    def update(self, *args, **kwargs):
        raise NotImplementedError('you are not expected to modify this table')
