import os

from slcore.database.dbf import get_database
from slcore.naive_parsers.machine_id import find_machine_id
from slcore.dt_parsers.compatible import find_compatible
from slcore.common import Common
from slcore.analyses.analysis import Analysis


MD_ATRRIBUTES = ['machine_ids', 'compatible', 'profiles', 'device_tree', 'targets']


class MD(Common):
    def __init__(self):
        super().__init__()
        self.set_attributes(MD_ATRRIBUTES)

    def __str__(self):
        a = 'DEVICE TREE: {}, TARGETS: {}'.format(self.device_tree, self.targets)
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


class Machines(Analysis):
    def select_first_profile(self, md):
        profile = list(md.get_profiles().keys())
        if len(profile):
            profile = profile[0]
        else:
            profile = None
        return profile

    def update_profile(self, firmware):
        raw_name = firmware.get_components().get_raw_name()
        firmware.path_to_profile = os.path.join(
            firmware.get_target_dir(), '{}.profile.yaml'.format(raw_name))

    def clear_runtime(self, firmware):
        if 'runtime' in firmware.profile:
            firmware.profile.pop('runtime')

    def update_stats(self, firmware):
        raw_name = firmware.get_components().get_raw_name()
        firmware.path_to_summary = os.path.join(
            firmware.get_target_dir(), '{}.stats.yaml'.format(raw_name))

    def update_trace(self, firmware):
        raw_name = firmware.get_components().get_raw_name()
        firmware.path_to_trace = os.path.join(
            firmware.get_target_dir(), '{}.trace'.format(raw_name))

    def find_latest_board(self, firmware, url=None):
        support = get_database('support')
        revision, target, subtarget = [None] * 3

        brand = firmware.get_brand()
        arch = firmware.get_arch()

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

    def run(self, firmware):
        components = firmware.get_components()

        if components is None:
            self.context['input'] = 'components is missing'
            return False

        # L1 every case needs a custom profile
        self.update_profile(firmware)

        if not components.supported:
            self.clear_runtime(firmware)
            self.context['input'] = 'cannot unpack this image'
            return False

        # L2 format supported cases need statistics
        self.update_stats(firmware)

        if not components.has_kernel():
            self.clear_runtime(firmware)
            self.context['input'] = 'have no kernel, maybe a rootfs image'
            return False

        # T1: LATEST_BOARD_SIGNATURE
        # BOARD=TARGET>SUBTARGET>MACHINE=compatible=machine_id>PROFILE
        md = self.find_latest_board(firmware, url=firmware.get_url())
        if md is None:
            # modeling 001
            self.clear_runtime(firmware)
            self.context['input'] = '001 cannot find the board'
            return False
        self.info(firmware, 'find the board {}'.format(md), 1)

        # T2 DEVICE_TREE_DISTRIBUTION
        if md.has_device_tree():
            self.info(firmware, 'this board has device tree, we are tying the built-in device tree files', 1)
            # A3 BUILTIN DEVICE TREE
            if components.has_device_tree():
                compatible = find_compatible(components.get_path_to_dtb())
                # T5 WHETHER OR NOT WE ARE PREPARED
                profile = md.find_profile_by_compatible(compatible)
                if profile is None:
                    profile = self.select_first_profile(md)
                if profile is None:
                    # modeling 002
                    self.clear_runtime(firmware)
                    self.context['input'] = '002 cannot find the compatible {} and nothing prepared'.format(compatible)
                    return False
                self.info(firmware, 'we support {}'.format(compatible), 1)
                # update profile and change save-to-path to avoid modifying our well-defined profile
                firmware.set_profile(path_to_profile=profile)
                firmware.set_components(components)
                self.update_profile(firmware)
                self.update_trace(firmware)
                components.set_path_to_dtb(firmware.dtb)
                return True
        self.info(firmware, 'this board doesn\'t have device tree, we will be looking for its machine ids', 1)

        # T4 MACHINE_ID_SIGNATURE
        machine_ids = find_machine_id(components.get_path_to_kernel())
        if machine_ids is None:
            self.info(firmware, 'we will try our profiles one by one', 1)
            profile = self.select_first_profile(md)
        else:
            self.info(firmware, 'we support {}'.format(machine_ids), 1)
            profile = md.find_profile_by_id(machine_ids)

        # T5 WHETHER OR NOT WE ARE PREPARED
        if profile is None:
            # modeling 003
            self.clear_runtime(firmware)
            self.context['input'] = '003 cannot find any machine id or any built-in profile'
            return False

        # update profile and change save-to-path to avoid modifing our well-defined profile
        firmware.set_profile(path_to_profile=profile)
        firmware.set_components(components)
        self.update_profile(firmware)
        self.update_trace(firmware)
        components.set_path_to_dtb(firmware.dtb)

        return True

    def __init__(self, analysis_manager):
        super().__init__(analysis_manager)
        self.name = 'machines'
        self.description = 'find a valid profile'
        self.context['hint'] = 'oops'
        self.required = []
        self.critical = True

