import abc
import os


class DatabaseInterface(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def get_count(self, *args, **kwargs):
        pass

    @abc.abstractmethod
    def get_firmware(self, *args, **kwargs):
        pass


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
            'model': []
        }
        self.brand = kwargs.pop('brand', None)
        self.most_possible_target = None
        self.most_possible_subtarget = None
        self.openwrt = None
        self.openwrt_revision = None
