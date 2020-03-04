from slcore.database.dbf import get_database
from slcore.naive_parsers.machine_id import find_machine_id
from slcore.dt_parsers.compatible import find_compatible
from slcore.common import Common
from slcore.project import get_current_project


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


def find_latest_board(path_to_kenrel, arch, brand=None, url=None):
    support = get_database('support')
    revision, target, subtarget = [None] * 3

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


def project_find_profile(components, url=None):
    project = get_current_project()
    if project is None:
        return

    brand = project.attrs['brand']
    arch = project.attrs['arch']

    return find_profile(components, arch, brand=brand, url=url)


def find_profile(components, arch, brand=None, url=None):
    if components is None:
        return None

    # T1: LATEST_BOARD_SIGNATURE
    # BOARD=TARGET>SUBTARGET>MACHINE=compatible=machine_id>PROFILE
    md = find_latest_board(components.get_path_to_kernel(), arch, url=url, brand=brand)
    if md is None:
        # modeling 001
        print('cannot support this firmware(001 cannot find the board)')
        print('1) prepare the source code which can generate your firmware')
        print('2）see src.py -h for more details')
        return None

    # T2 DEVICE_TREE_DISTRIBUTION
    if md.has_device_tree():
        # A3 BUILTIN DEVICE TREE
        if components.has_device_tree():
            compatible = find_compatible(components.get_path_to_dtb())
            # T5 WHETHER OR NOT WE ARE PREPARED
            profile = md.find_profile_by_compatible(compatible)
            if profile is None:
                # modeling 002
                print('cannot support this firmware(002 cannot find the compatible {})'.format(compatible))
                print('1) prepare the source code which can generate your firmware')
                print('2）see src.py -h for more details')
                print('3) here is some reference: {}'.format(md))
            return profile

    # T4 MACHINE_ID_SIGNATURE
    machine_ids = find_machine_id(components.get_path_to_kernel())
    if machine_ids is None:
        profile = list(md.get_profiles().keys())
        if len(profile):
            profile = profile[0]
        else:
            profile = None
    else:
        profile = md.find_profile_by_id(machine_ids)

    # T5 WHETHER OR NOT WE ARE PREPARED
    if profile is None:
        # modeling 003
        print('cannot support this firmware(003 cannot find the machine id {})'.format(machine_ids))
        print('1) prepare the source code which can generate your firmware')
        print('2）see src.py -h for more details')
        print('3) here is some reference: {}'.format(md))
    return profile

