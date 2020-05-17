import os

from slcore.database.dbf import get_database
from slcore.naive_parsers.machine_id import find_machine_id
from slcore.dt_parsers.compatible import find_compatible
from slcore.common import Common
from slcore.amanager import Analysis


MD_ATRRIBUTES = [
    'machine_ids', 'compatible', 'profiles', 'device_tree', 'targets']


class MD(Common):
    def __init__(self):
        super().__init__()
        self.set_attributes(MD_ATRRIBUTES)

    def __str__(self):
        a = 'DEVICE TREE: {}, TARGETS: {}'.format(
            self.device_tree, self.targets)
        if self.profiles is not None and len(self.profiles):
            a += '\n   PROFILES {}'.format(len(self.profiles))
            for k, v in self.profiles.items():
                a += '\n   {} {}'.format(k, v)
        return a

    def has_device_tree(self):
        return self.device_tree

    def find_profile_by_compatible(self, compatible):
        if self.compatible is None:
            return None
        for cmptb in compatible:
            if cmptb in self.compatible:
                return self.compatible[cmptb]

    def find_profile_by_id(self, machine_ids):
        if self.machine_ids is None:
            return None
        for machine_id in machine_ids:
            if machine_id in self.machine_ids:
                return self.machine_ids[machine_id]


class FindMachine(Analysis):
    def select_first_profile(self, md):
        profile = list(md.get_profiles().keys())
        if len(profile):
            profile = profile[0]
        else:
            profile = None
        return profile

    def update_profile(self):
        raw_name = self.firmware.get_components().get_raw_name()
        self.firmware.path_to_profile = os.path.join(
            self.analysis_manager.project.attrs['path'],
            '{}.profile.yaml'.format(raw_name))

    def clear_runtime(self):
        if 'runtime' in self.firmware.profile:
            self.firmware.profile.pop('runtime')

    def update_trace(self):
        raw_name = self.firmware.get_components().get_raw_name()
        self.analysis_manager.arguments['path_to_trace'] = os.path.join(
            self.analysis_manager.project.attrs['path'],
            '{}.trace'.format(raw_name))

    def find_latest_board(self, url=None):
        support = get_database('support')
        revision, target, subtarget = [None] * 3

        brand = self.firmware.get_brand()
        arch = self.firmware.get_arch()

        if brand is None:
            print('maybe brand is missing?')
        if url is not None and brand == 'openwrt':
            from slcore.naive_parsers.openwrt import parse_openwrt_url
            revision, target, subtarget = parse_openwrt_url(url)

        board = support.select('board', arch=arch, brand=brand, target=target)
        if board is not None:
            md = MD()
            md.set_attributes(attrs=board)
            return md
        else:
            return None

    def run(self, **kwargs):
        components = self.firmware.get_components()

        if components is None:
            self.error_info = 'components is missing'
            return False

        # L1 every case needs a custom profile
        self.update_profile()

        if not components.supported:
            self.clear_runtime()
            self.error_info = 'cannot unpack this image'
            return False

        if not components.has_kernel():
            self.clear_runtime()
            self.error_info = 'have no kernel, maybe a rootfs image'
            return False

        # T1: LATEST_BOARD_SIGNATURE
        # BOARD=TARGET>SUBTARGET>MACHINE=compatible=machine_id>PROFILE
        md = self.find_latest_board(url=self.firmware.get_url())
        if md is None:
            # modeling 001
            self.clear_runtime()
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
                    profile = self.select_first_profile(md)
                if profile is None:
                    # modeling 002
                    self.clear_runtime()
                    self.error_info = \
                        '002 cannot find the compatible {} and nothing prepared'.format(compatible)
                    return False
                self.info('we support {}'.format(compatible), 1)
                # update profile and change save-to-path to
                # avoid modifying our well-defined profile
                self.firmware.load_from_profile(path_to_profile=profile)
                self.firmware.set_components(components)
                self.update_profile()
                self.update_trace()
                components.set_path_to_dtb(self.firmware.get_realdtb())
                return True
        self.info('this board doesn\'t have device tree, we will be looking for its machine ids', 1)

        # T4 MACHINE_ID_SIGNATURE
        machine_ids = find_machine_id(components.get_path_to_kernel())
        if machine_ids is None:
            self.info('we will try our profiles one by one', 1)
            profile = self.select_first_profile(md)
        else:
            self.info('we support {}'.format(machine_ids), 1)
            profile = md.find_profile_by_id(machine_ids)

        # T5 WHETHER OR NOT WE ARE PREPARED
        if profile is None:
            # modeling 003
            self.clear_runtime()
            self.error_info = \
                '003 cannot find any machine id or any built-in profile'
            return False

        # update profile and change save-to-path to
        # avoid modifing our well-defined profile
        self.firmware.load_from_profile(path_to_profile=profile)
        self.firmware.set_components(components)
        self.update_profile()
        self.update_trace()
        components.set_path_to_dtb(self.firmware.get_realdtb())

        return True

    def __init__(self, analysis_manager):
        super().__init__(analysis_manager)
        self.name = 'msearch'
        self.description = 'Find a valid machine profile.'
        self.required = []
        self.critical = True
