import abc
import os

from profile.pff import get_firmware_in_profile


class DatabaseInterface(object):
    def __init__(self, *args, **kwargs):
        self.dbtype = None
        self.path = os.path.join(os.getcwd(), args[0])
        self.profile = kwargs.pop('profile')
        self.records = []
        self.count = 1
        self.header = None
        self.items = None  # for current line

    @abc.abstractmethod
    def parse_pre(self, line, **kwargs):
        pass

    @abc.abstractmethod
    def handle_post(self, firmware, **kwargs):
        pass

    def load(self, *args, **kwargs):
        with open(self.path) as f:
            for line in f:
                context = self.parse_pre(line.strip())
                # uuid, name, path, size
                if context is None:
                    continue
                firmware = get_firmware_in_profile(self.profile, **context)
                firmware.id = self.count
                self.handle_post(firmware)
                yield firmware
                self.count += 1

    def get_count(self, *args, **kwargs):
        return self.count

    def get_firmware(self, *args, **kwargs):
        for firmware in self.load(*args, **kwargs):
            yield firmware


class Firmware(object):
    def __init__(self, *args, **kwargs):
        self.uuid = kwargs.pop('uuid')

        self.relative = True
        # directory where the firmware are put
        self.storage = os.getcwd()
        # absolute or relative path for the firmware
        self.path = kwargs.pop('path')
        self.working_dir = None
        self.working_path = None
        self.size = None

        self.arch = kwargs.pop('arch')
        self.endian = kwargs.pop('endian')

        self.image_type = None
        self.image_path = None
        self.kernel = None
        self.dtb = None
        self.dtc = None
        self.metadata = {
            'brand': [],
            'os': [],
            'arch': [],
            'created_time': [],
            'kernel_version': [],
            'kernel_created_time': [],
            'kernel_load_address': [],
            'kernel_entry_point': [],
            'possible_targets': [],
            'possible_subtargets': [],
            'compatible': [],
            'model': [],
            'cpu': [],
            'soc': [],
        }
        self.brand = kwargs.pop('brand', None)
        self.most_possible_target = None
        self.most_possible_subtarget = None
        self.openwrt = None
        self.openwrt_revision = None
        self.src = None
        self.cpu = None
        self.cpu_priv = None
        self.ram_start = None
        self.ram_size = None
        self.flash = None
        self.flash_model = None
        self.uart_model = None
        self.ic_model = None
