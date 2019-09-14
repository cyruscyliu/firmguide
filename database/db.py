from db_text import DatabaseText
import abc
import os


class Firmware(object):
    def __init__(self, *args, **kwargs):
        self.uuid = kwargs.pop('uuid')
        # directory where the firmware are put
        self.storage = os.path.realpath(os.path.join(os.getcwd(), '..'))
        # absolute or relative path for the firmware
        self.path = kwargs.pop('path')
        self.relative = True
        self.arch = kwargs.pop('arch')
        self.endian = kwargs.pop('endian')


class Database(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def select(self, *args, **kwargs):
        pass

    @abc.abstractmethod
    def add(self, *args, **kwargs):
        pass

    @abc.abstractmethod
    def delete(self, *args, **kwargs):
        pass

    @abc.abstractmethod
    def update(self, *args, **kwargs):
        pass


def get_database(dbtype, **kwargs):
    if dbtype == 'text':
        path = kwargs.pop('tdb', 'openwrt_arm_el')
        return DatabaseText(path)
    else:
        raise NotImplementedError('the dbtype {} is not support yet'.format(dbtype))


class DatabaseInterface(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def get_count(self, *args, **kwargs):
        pass

    @abc.abstractmethod
    def get_firmware(self, *args, **kwargs):
        pass
