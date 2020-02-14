from slcore.database.dbf import get_database
from slcore.naive_parsers.machine_id import find_machine_id
from slcore.dt_parsers.compatible import find_compatible
from slcore.compositor import Common


MD_ATRRIBUTES = ['machine_ids', 'compatible', 'profiles', 'device_tree']


class MD(Common):
    def __init__(self):
        super().__init__()
        self.set_attributes(MD_ATRRIBUTES)

    def __str__(self):
        pass

    def has_device_tree(self):
        return self.device_tree

    def find_profile_by_compatible(self, compatible):
        for cmptb in compatible:
            if cmptb in self.compatible:
                return self.compatible[cmptb]

    def find_profile_by_id(self, machine_ids):
        for machine_id in machine_ids:
            if machine_id in self.machine_ids:
                return self.machine_ids[machine_id]


def find_latest_board(path_to_kenrel, arch, brand=None, url=None):
    support = get_database('support')
    revision, target, subtarget = [None] * 3

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


def find_profile(components, arch, brand=None, url=None):
    if components is None:
        return None

    # T1: LATEST_BOARD_SIGNATURE
    # BOARD=TARGET>SUBTARGET>MACHINE=compatible=machine_id>PROFILE
    md = find_latest_board(components.get_path_to_kernel(), arch, url=url, brand=brand)
    if md is None:
        # modeling 001
        print('cannot support this firmware(001)')
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
                # modeling 003
                print('cannot support this firmware(003)')
                print('1) prepare the source code which can generate your firmware')
                print('2）see src.py -h for more details')
                print('3) here is some reference: {}'.format(md.description()))
            return profile

    # T4 MACHINE_ID_SIGNATURE
    machine_ids = find_machine_id(components.get_path_to_kernel())
    if machine_ids is None:
        # modeling 002
        print('cannot support this firmware(002)')
        print('1) prepare the source code which can generate your firmware')
        print('2）see src.py -h for more details')
        print('3) here is some reference: {}'.format(md.description()))
        return None
    # T5 WHETHER OR NOT WE ARE PREPARED
    profile = md.find_profile_by_id(machine_ids)
    if profile is None:
        # modeling 003
        print('cannot support this firmware(003)')
        print('1) prepare the source code which can generate your firmware')
        print('2）see src.py -h for more details')
        print('3) here is some reference: {}'.format(md.description()))
    return profile

