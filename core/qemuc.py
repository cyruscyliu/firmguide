"""
QEMU controller

after several experiments, I conclude
    1) QEMU is likely to be supported on Windows with extra compilation efforts
    https://stackoverflow.com/questions/53084815/compile-qemu-under-windows-10-64-bit-for-windows-10-64-bit
    which is not elegant and not easy. I hope QEMU will be officially supported on Windows in the future.
    2) Multi-processing introduces more complexity than speed increment. Once you'd like to
    analyze more than one firmware at the same time, you must consider QEMU pollution(synchronization) problem.
    Modifying QEMU source code at the same time makes everything messy and embarrassing. JIT solution is one of
    the ideal ways to solve this problem. BTW, running in different directories looks quick and dirty but is
    really helpful.

finite state machine
                |<-----> RECOVER
    START --> PATCH <--> COMPILE
      |---------<----------|
      |---<----RUN----<----|
      |---<-- TRACE---<----|
"""
from core.externalc import ExternalPackage
from settings import *

import os

START, PATCH, RECOVER, COMPILE, RUN, TRACE = 0, 1, 2, 3, 4, 5


class QEMUController(ExternalPackage):
    def install(self):
        os.system(
            'wget -nc {0} -O {1}/{2} || true &&'
            'tar --skip-old-files -Jxf {1}/{2} -C {1} &&'
            'cp -r {3}/* {1}/{4}'.format(
                QEMU_PACKAGE_URL, WORKING_DIR, QEMU_PACKAGE_NAME,
                QEMU_PATCH_DIR, QEMU_DIR_NAME))

    def clean(self):
        os.system('rm -rf {}/{}'.format(WORKING_DIR, QEMU_DIR_NAME))

    def clear(self):
        os.system('rm -rf {0}/{1} {0}/{2}'.format(
            WORKING_DIR, QEMU_DIR_NAME, QEMU_PACKAGE_NAME))

    def __init__(self):
        self.state = START

    def patch(self, *args, **kwargs):
        pass

    def recover(self, *args, **kwargs):
        pass

    def compile(self, *args, **kwargs):
        pass

    def run(self, *args, **kwargs):
        pass

    def trace(self, *args, **kwargs):
        pass

