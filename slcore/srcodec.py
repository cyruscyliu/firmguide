"""
source code controller
"""
from settings import *
from logger import logger_info

import os
import qmp
import subprocess

BACKUP, PATCH, COMPILE, LINK = 0, 1, 2, 3

class SRCodeController(object):
    def __init__(self, srcode, arch, prefix, cpu=4):
        self.srcode = srcode
        self.arch = arch
        self.prefix = prefix

        self.makeout = None
        self.cpu = cpu

    def run(self, command):
        cwd = os.getcwd()
        os.chdir(self.srcode)
        status = os.system(command)
        os.chdir(cwd)
        return status

    def set_makeout(self, makeout):
        self.makeout = makeout

    def get_makeout(self):
        if self.makeout is not None:
            return self.makeout

        self.makeout = os.path.join(self.srcode, 'makeout.txt')
        self.run('make -j{} ARCH={} CROSS_COMPILE={}'.format(self.cpu, self.arch, self.prefix))

        return self.makeout

    def __backup(compress=True, copy=False):
        pass

    def __patch():
        if self.patch:
            return
        self.patch = True

    def __build():
        if self.build:
            return
        self.build = True
        pass

    def __link():
        pass

    def apply_to_llvm(self, backup=True, patch=True, build=True, link=True):
        self.__backup()
        self.__patch()
        if build:
            self.__build()
        if link:
            self.__link()

    def __has_gcc(self, line):
        gcc = [os.path.basename(self.prefix) + 'gcc', 'ccache_cc']
        for i in gcc:
            if line.split()[0].endswith(i):# or line.split()[1].endswith(gcc):
                return True
        return False

    def __correct_gcc(self, command):
        items = command.split()
        items[0] = self.prefix + 'gcc'
        return ' '.join(items)

    def preprocess(self, path, cmdline=None):
        """
        preprocess('arch/arm/mm/proc-xxx.c')
        """
        if self.makeout is None:
            return

        command = None
        target = os.path.basename(path)
        with open(self.makeout) as f:
            for line in f:
                if not self.__has_gcc(line):
                    continue
                if line.strip().endswith(target):
                    command = line
                    break
        if command is None:
            if cmdline is not None:
                command = cmdline
            else:
                return None

        command = self.__correct_gcc(command)
        command = command.replace('-c', '-E').replace('.o', '.i')
        status = self.run(command)
        if status == 0:
            return os.path.join(self.srcode, path.replace('.c', '.i'))
        else:
            return None

