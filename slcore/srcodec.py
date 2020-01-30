"""
source code controller
"""
from settings import *
from supervisor.logging_setup import logger_info

import os
import qmp
import subprocess

BACKUP, PATCH, COMPILE, LINK = 0, 1, 2, 3

class SRCodeController(object):
    def __init__(self):
        self.gcc = None
        self.makeout = None
        self.srcode = None
        self.clang = None
        self.opt = None
        self.llvm_link = None
        self.llvm_status = [False] * 4

    def get_makeout(self, *args, **kwargs):
        pass

    def __backup(compress=True, copy=False):
        if
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

    def preprocess(self, *args, **kwargs):
        """
        target a file
        """
        pass
