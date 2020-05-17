import os
import yaml

from slcore.common import Common
from slcore.compositor import Components
from slcore.profile.kernel import KernelForFirmware
from slcore.profile.openwrt import OpenWRTForFirmware


class Firmware(KernelForFirmware, OpenWRTForFirmware, Common):
    def __init__(self, *args, **kwargs):
        self.analysis_progress = None  # /tmp/uuid/analyses

        self.profile = None
        self.components = None
        self.running_command = None

        self.path_to_profile = None  # path
        self.realdtb = None  # path
        self.realdts = None  # path

    # ######## components ########
    def get_components(self):
        return self.components

    def set_components(self, components):
        self.components = components

    def get_realdtb(self):
        return self.realdtb

    def set_realdtb(self, dtb):
        self.realdtb = dtb

    def get_realdts(self):
        return self.realdts

    def set_realdts(self, dts):
        self.realdts = dts

    # ######### profile ##########
    def set_profile(self, profile):
        self.profile = profile

    def get_profile(self, *args, **kwargs):
        return self.profile

    def create_empty_profile(self, path):
        self.path_to_profile = os.path.join(path, 'profile.yaml')
        with open(self.path_to_profile, 'w') as f:
            yaml.safe_dump({}, f)
        self.set_profile({})

    def load_from_profile(self, path_to_profile):
        self.path_to_profile = path_to_profile
        with open(self.path_to_profile, 'r') as f:
            profile = yaml.safe_load(f)

        if 'components' in profile:
            self.components = Components()
            self.components.set_attributes(profile['components'])
        # if 'path_to_dtb' in profile:
        #     self.dtb = os.path.join(BASE_DIR, profile['path_to_dtb'])
        self.set_profile(profile)

    def save_profile(self):
        if self.components:
            self.profile['components'] = self.components.get_attributes()
        if self.realdtb:
            self.profile['path_to_dtb'] = \
                os.path.join('examples/profiles',
                             self.get_machine_name(), 'profile.dtb')
        if self.running_command:
            self.profile['booting_command'] = self.running_command

        with open(self.path_to_profile, 'w') as f:
            yaml.safe_dump(self.profile, f)

    # ######## setter and getter ########
    def set_general(self, *levels, value=None):
        # for loop not recursion
        profile = self.profile
        for level in levels[:-1]:
            if level not in profile:
                profile[level] = {}
            profile = profile[level]
        profile[levels[-1]] = value

    def get_general(self, *levels):
        # for loop not recursion
        profile = self.profile
        for level in levels:
            if level in profile:
                profile = profile[level]
            else:
                profile = None
                break
        return profile

    # ######## basics ########
    def get_board(self, *args, **kwargs):
        return self.get_general('basics', 'board')

    def set_board(self, *args, **kwargs):
        self.set_general('basics', 'board', value=args[0])

    def set_arch(self, *args, **kwargs):
        self.set_general('basics', 'architecture', value=args[0])

    def get_arch(self, *args, **kwargs):
        return self.get_general('basics', 'architecture')

    def get_endian(self, *args, **kwargs):
        return self.get_general('basics', 'endian')

    def set_endian(self, *args, **kwargs):
        self.set_general('basics', 'endian', value=args[0])

    def get_brand(self, *args, **kwargs):
        return self.get_general('basics', 'brand')

    def set_brand(self, *args, **kwargs):
        self.set_general('basics', 'brand', value=args[0])

    def get_machine_description(self, *args, **kwargs):
        return self.get_general('basics', 'machine_description')

    def set_machine_description(self, *args, **kwargs):
        self.set_general('basics', 'machine_description', value=args[0])

    def get_machine_name(self, *args, **kwargs):
        return self.get_general('basics', 'machine_name')

    def set_machine_name(self, *args, **kwargs):
        self.set_general('basics', 'machine_name', value=args[0])

    def get_board_id(self, *args, **kwargs):
        return self.get_general('basics', 'board_id')

    def set_board_id(self, *args, **kwargs):
        self.set_general('basics', 'board_id', value=args[0])

    def set_description(self, *args, **kwargs):
        self.set_general('basics', 'description', value=args[0])

    def get_description(self, *args, **kwargs):
        return self.get_general('basics', 'description')

    # ######## OpenWRT ########
    def set_url(self, *args, **kwargs):
        self.set_general('brand', 'url', value=args[0])

    def get_url(self, *args, **kwargs):
        return self.get_general('brand', 'url')

    def set_homepage(self, *args, **kwargs):
        self.set_general('brand', 'homepage', value=args[0])

    def get_homepage(self, *args, **kwargs):
        return self.get_general('brand', 'homepage')

    def set_toh(self, *args, **kwargs):
        toh = args[0]
        assert isinstance(toh, list)
        header = kwargs.pop('header', None)
        if header is None:
            return
        for k, v in zip(header, toh):
            self.set_general('brand', 'toh', k, value=v)

    def get_toh(self, *args, **kwargs):
        toh = []
        for arg in args:
            toh.append(self.get_general('brand', 'toh', arg))
        return toh

    def get_revision(self, *args, **kwargs):
        return self.get_general('brand', 'revision')

    def set_revision(self, *args, **kwargs):
        self.set_general('brand', 'revision', value=args[0])

    def get_target(self, *args, **kwargs):
        return self.get_general('brand', 'target')

    def set_target(self, *args, **kwargs):
        self.set_general('brand', 'target', value=args[0])

    def get_subtarget(self, *args, **kwargs):
        return self.get_general('brand', 'subtarget')

    def set_subtarget(self, *args, **kwargs):
        self.set_general('brand', 'subtarget', value=args[0])

    # ######## Linux Kernel ########
    def get_kernel_load_address(self, *args, **kwargs):
        return self.get_general('kernel', 'kernel_load_address')

    def set_kernel_load_address(self, *args, **kwargs):
        self.set_general('kernel', 'kernel_load_address', value=args[0])

    def get_kernel_version(self, *args, **kwargs):
        return self.get_general('kernel', 'kernel_version')

    def set_kernel_version(self, *args, **kwargs):
        self.set_general('kernel', 'kernel_version', value=args[0])

    def get_kernel_created_time(self, *args, **kwargs):
        return self.get_general('kernel', 'kernel_created_time')

    def set_kernel_created_time(self, *args, **kwargs):
        self.set_general('kernel', 'kernel_created_time', value=args[0])

    def get_kernel_entry_point(self, *args, **kwargs):
        return self.get_general('kernel', 'kernel_entry_point')

    def set_kernel_entry_point(self, *args, **kwargs):
        self.set_general('kernel', 'kernel_entry_point', value=args[0])

    # ######## runtime ########
    def get_iteration(self, *args, **kwargs):
        return self.get_general('runtime', 'iteration')

    def set_iteration(self, *args, **kwargs):
        self.set_general('runtime', 'iteration', value=args[0])

    def get_stage(self, *args, **kwargs):
        # get_stage('user_mode')
        return self.get_general('runtime', args[0])

    def set_stage(self, *args, **kwargs):
        # set_state(True, 'user_mode')
        self.set_general('runtime', args[1], value=args[0])

    # ######## statistics ########
    def set_uart_num(self, *args, **kwargs):
        self.set_general('uart', 'num', value=args[0])

    def get_uart_num(self, *args, **kwargs):
        uart_num = self.get_general('uart', 'num')
        if uart_num is None:
            self.set_uart_num(0)
        return self.get_general('uart', 'num')
