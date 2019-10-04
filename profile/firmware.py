import abc
import os


class Firmware(object):
    def __init__(self, *args, **kwargs):
        self.uuid = kwargs.pop('uuid')
        self.name = kwargs.pop('name')
        self.path = kwargs.pop('path')
        self.size = kwargs.pop('size')
        self.working_dir = None
        self.working_path = None

    def set_working_env(self, dir, path):
        self.working_dir = dir
        self.working_path = path

    @abc.abstractmethod
    def set(self, *args, **kwargs):
        pass

    @abc.abstractmethod
    def get(self, *args, **kwargs):
        pass
