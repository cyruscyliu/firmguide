import os
import yaml

from slcore.database.db import Database
from settings import *


class SupportMachines(Database):
    def select(self, *args, **kwargs):
        """
        select 'profile' where arch='arm' and machine_id='0x661'
        select 'profile' where arch='arm' and compatible='plxtech,nas7820'
        select 'board'   where arch='arm' and board='mach-orion5x'
        select 'board'   where arch='arm' and brand='openwrt' and target='orion'
        """
        arch = kwargs.pop('arch')
        assert arch in ['arm', 'arm64', 'mips']

        brand = kwargs.pop('brand', None)
        board = kwargs.pop('board', None)
        compatible = kwargs.pop('compatible', None)
        machine_id = kwargs.pop('machine_id', None)
        target = kwargs.pop('target', None)

        table = open(os.path.join(BASE_DIR, 'slcore/database', 'support.{}.yaml'.format(arch)))
        info = yaml.safe_load(table)
        table.close()

        action = args[0]

        if action == 'profile' and machine_id is not None:
            for k, v in info.items():
                if 'machine_ids' in v and machine_id in v['machine_ids']:
                    return os.path.join(BASE_DIR, v['machine_ids'][machine_id])
        elif action == 'profile' and compatible is not None:
            for k, v in info.items():
                if 'compatible' in v and compatible in v['compatible']:
                    return os.path.join(BASE_DIR, v['compatible'][compatible])
        elif action == 'board' and board is not None:
            if board in info:
                return info[board]
        elif action == 'board' and brand is not None and target is not None:
            for k, v in info.items():
                if 'targets' in v and brand in v['targets'] and target in v['targets'][brand]:
                    return v

    def add(self, *args, **kwargs):
        raise NotImplementedError('you are not expected to modify this table')

    def delete(self, *args, **kwargs):
        raise NotImplementedError('you are not expected to modify this table')

    def update(self, *args, **kwargs):
        raise NotImplementedError('you are not expected to modify this table')

