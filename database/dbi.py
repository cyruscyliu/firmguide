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
        # directory where the firmware are put
        self.storage = os.getcwd()
        # absolute or relative path for the firmware
        self.path = kwargs.pop('path')
        self.relative = True
        self.arch = kwargs.pop('arch')
        self.endian = kwargs.pop('endian')
