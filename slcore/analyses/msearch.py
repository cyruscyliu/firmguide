import os

from slcore.database.dbf import get_database
from slcore.database.machine_id import find_machine_id
from slcore.database.board_dir import find_board_dir
from slcore.dt_parsers.compatible import find_compatible
from slcore.common import Common, setup_logging
from slcore.amanager import Analysis


MD_ATRRIBUTES = [
    'support_list', 'device_tree', 'targets']


class MD(Common):
    def __init__(self):
        super().__init__()
        self.set_attributes(MD_ATRRIBUTES)

    def __str__(self):
        a = 'DEVICE TREE: {}, TARGETS: {}'.format(
            self.device_tree, self.targets)
        if self.support_list is not None:
            a += '\n   PROFILES {}'.format(len(self.support_list))
            for k, v in self.support_list.items():
                a += '\n   {} {}'.format(k, v)
        return a

    def has_device_tree(self):
        return self.device_tree

    def find_profile_by_compatible(self, compatible):
        if self.support_list is None:
            return None
        for cmptb in compatible:
            if cmptb in self.support_list:
                return self.support_list[cmptb]
        return None

    def find_profile_by_id(self, machine_ids):
        if self.support_list is None:
            return None
        for machine_id in machine_ids:
            for k, v in self.support_list.items():
                if 'machine_ids' not in v:
                    continue
                if machine_id in v['machine_ids']:
                    return v
        return None

    def select_first_profile(self):
        if self.support_list is None:
            return None
        if len(self.support_list):
            for k, v in self.support_list.items():
                return v
        else:
            return None


class FindMachine(Analysis):
    def update_profile(self):
        # fix runtime
        self.firmware.set_stage(False, 'user_mode')
        self.firmware.profile['booting_command'] = None

        raw_name = self.firmware.get_components().get_raw_name()
        self.firmware.path_to_profile = os.path.join(
            self.analysis_manager.project.attrs['path'],
            '{}.profile.yaml'.format(raw_name))

    def update_log(self):
        raw_name = self.firmware.get_components().get_raw_name()
        setup_logging(self.analysis_manager.project.attrs['path'], raw_name)

    def update_trace(self):
        raw_name = self.firmware.get_components().get_raw_name()
        self.analysis_manager.arguments['path_to_trace'] = os.path.join(
            self.analysis_manager.project.attrs['path'],
            '{}.trace'.format(raw_name))

    def find_latest_board(self, url=None):
        support = get_database('support')
        revision, target, subtarget = [None] * 3

        brand = self.firmware.get_brand()
        assert brand is not None, 'brand must be clear'
        arch = self.firmware.get_arch()

        if url is not None and brand == 'openwrt':
            from slcore.brandsupkg.openwrt import parse_openwrt_url
            revision, target, subtarget = parse_openwrt_url(url)
        else:
            board = find_board_dir(
                self.firmware.get_components().get_path_to_kernel(), 
                self.firmware.get_arch())
            print(board)
            exit()

        board = support.select('board', arch=arch, brand=brand, target=target)
        if board is not None:
            md = MD()
            md.set_attributes(attrs=board)
            return md
        else:
            return None

    def run(self, **kwargs):
        components = self.firmware.get_components()

        if self.check_components_is_none():
            return False

        self.update_profile()
        self.update_log()
        self.update_trace()

        if not self.check_components():
            return False

        # T1: LATEST_BOARD_SIGNATURE
        # BOARD=TARGET>SUBTARGET>MACHINE=compatible=machine_id>PROFILE
        md = self.find_latest_board(url=kwargs.pop('url'))
        if md is None:
            # modeling 001
            self.error_info = '001 cannot find the board'
            return False
        self.info('find the board {}'.format(md), 1)

        # T2 DEVICE_TREE_DISTRIBUTION
        if md.has_device_tree():
            self.info('this board has device tree, we are tying the built-in device tree files', 1)
            # A3 BUILTIN DEVICE TREE
            if components.has_device_tree():
                compatible = find_compatible(components.get_path_to_dtb())
                # T5 WHETHER OR NOT WE ARE PREPARED
                profile = md.find_profile_by_compatible(compatible)
                if profile is None:
                    self.info('we will try our profiles one by one', 1)
                    profile = md.select_first_profile()
                if profile is None:
                    # modeling 002
                    self.error_info = \
                        '002 cannot find the compatible {} and nothing prepared'.format(compatible)
                    return False
                self.firmware.set_realdtb(os.path.join(
                    self.analysis_manager.project.attrs['base_dir'],
                    profile['realdtb']))
                self.info('we support {}'.format(compatible), 1)
                return True

        # T4 MACHINE_ID_SIGNATURE
        self.info('this board doesn\'t have device tree, we will be looking for its machine ids', 1)
        machine_ids = find_machine_id(components.get_path_to_kernel())
        if machine_ids is None:
            self.info('we will try our profiles one by one', 1)
            profile = md.select_first_profile()
        else:
            self.info('we support {}'.format(machine_ids), 1)
            profile = md.find_profile_by_id(machine_ids)

        # T5 WHETHER OR NOT WE ARE PREPARED
        if profile is None:
            # modeling 003
            self.error_info = \
                '003 cannot find any machine id or any built-in profile'
            return False

        self.firmware.set_realdtb(os.path.join(
            self.analysis_manager.project.attrs['base_dir'],
           profile['realdtb']))
        return True

    def __init__(self, analysis_manager):
        super().__init__(analysis_manager)
        self.name = 'msearch'
        self.description = 'Find a valid machine profile.'
        self.required = []
        self.critical = True
