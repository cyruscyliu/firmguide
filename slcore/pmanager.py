import os
import yaml


class Project(object):
    def __init__(self, *args, **kwargs):
        self.attrs = {
            'path': kwargs.pop('path'),
            'base_dir': kwargs.pop('base_dir'),
            'rootfs_dir': kwargs.pop('rootfs_dir'),
            'qemu_dir': kwargs.pop('qemu_dir'),
            'logname': kwargs.pop('logname'),
            # TODO
            # 'llvm_dir': kwargs.pop('llvm_dir'),
            'sparse_dir': kwargs.pop('sparse_dir'),
        }
