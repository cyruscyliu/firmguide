import os
import yaml

from slcore.database.db import Database


class SupportMachines(Database):
    def select(self, *args, **kwargs):
        """
        Examples:
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

        database_dir = os.path.dirname(os.path.realpath(__file__))
        base_dir = os.path.dirname(os.path.dirname(database_dir))
        table = open(os.path.join(database_dir, 'support.{}.yaml'.format(arch)))
        info = yaml.safe_load(table)
        table.close()

        action = args[0]

        if action == 'profile' and machine_id is not None:
            for k, v in info.items():
                if 'machine_ids' in v and machine_id in v['machine_ids']:
                    return os.path.join(base_dir, v['machine_ids'][machine_id])
        elif action == 'profile' and compatible is not None:
            for k, v in info.items():
                if 'compatible' in v and compatible in v['compatible']:
                    return os.path.join(base_dir, v['compatible'][compatible])
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
        """
        update mach-oxnas where arch='arm' and board=board
        """
        arch = kwargs.pop('arch')
        assert arch in ['arm', 'arm64', 'mips']

        database_dir = os.path.dirname(os.path.realpath(__file__))
        table = open(os.path.join(database_dir, 'support.{}.yaml'.format(arch)))
        info = yaml.safe_load(table)
        table.close()

        info[args[0]] = kwargs.pop('board', None)

        table = open(os.path.join(database_dir, 'support.{}.yaml'.format(arch)), 'w')
        yaml.safe_dump(info, table)
        table.close()

