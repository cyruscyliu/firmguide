import os
import yaml

from slcore.database.db import Database
from settings import *


class SupportMachines(Database):
    def select(self, *args, **kwargs):
        """
        select 'profile' where arch='arm32' and machine_id='0x661'
        select 'profile' where arch='arm32' and compatible='plxtech,nas7820'
        """
        arch = kwargs.pop('arch')
        assert arch in ['arm32', 'mips']
        machine_id = kwargs.pop('machine_id', None)
        compatible = kwargs.pop('compatible', None)

        table = open(os.path.join(BASE_DIR, 'slcore/database', 'support.{}.yaml'.format(arch)))
        info = yaml.safe_load(table)
        table.close()

        target = args[0]

        if target == 'profile' and machine_id is not None:
            for k, v in info['support'].items():
                if 'machine_ids' in v and machine_id in v['machine_ids']:
                    return os.path.join(BASE_DIR, v['profile'])
        elif target == 'profile' and compatible is not None:
            for k, v in info['support'].items():
                if 'compatible' in v and compatible in v['compatible']:
                    return os.path.join(BASE_DIR, v['profile'])

    def add(self, *args, **kwargs):
        raise NotImplementedError('you are not expected to modify this table')

    def delete(self, *args, **kwargs):
        raise NotImplementedError('you are not expected to modify this table')

    def update(self, *args, **kwargs):
        raise NotImplementedError('you are not expected to modify this table')
