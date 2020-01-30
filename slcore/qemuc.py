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
from settings import *
from supervisor.logging_setup import logger_info

import os
import qmp
import subprocess



class QEMUController(object):
    def __init__(self):
        self.modified = []

    def patch(self, *args, **kwargs):
        """
        patch(abs/p/t/src, abs/p/t/dst, bak=True) or
        patch(abs/p/t/new, abs/p/t/old, bak=True)
        """
        src, dst = args
        os.system('cp {}{{,.bak}}'.format(dst))
        os.system('cp {} {}'.format(src, dst))
        self.modified.append(dst)

    def recover(self, *args, **kwargs):
        """
        recover()
        """
        for dst in self.modified:
            os.system('mv {}{{.bak,}}'.format(dst))

    def compile(self, *args, **kwargs):
        """
        compile(cpu=4)
        """
        cpu = kwargs.pop('cpu', 4)
        os.system('cd {}/{} && make -j{} && cd ~-'.format(
            WORKING_DIR, QEMU_DIR_NAME, cpu))

    def run(self, *args, **kwargs):
        """
        run(command) w/ abs/p/t/qemu
        """
        for command in *args:
            os.system('{}'.format(command))

    def trace(self, *args, **kwargs):
        """
        trace(command, uuid=0, arch='arm', endian='l')
        """
        uuid = kwargs.pop('uuid', 'unknown')
        arch = kwargs.pop('arch', 'arm')
        endian = kwargs.pop('endian', 'l')
        trace_to = '{}-{}-{}.trace'.format(uuid, arch, endian)
        trace_flags = '-d in_asm,int,cpu -D {}'.format(trace_to)

        qmp_flags = '-qmp tcp:localhost:4444,server,nowait'

        for command in *args:
            try:
                logger_info(uuid, 'tracing', 'qemudebug', full_command, 0)
                subprocess.run(full_command, timeout=20, shell=True)
            except subprocess.TimeoutExpired:
                qemu = qmp.QEMUMonitorProtocol(('localhost', 4444))
                qemu.connect()
                qemu.cmd('quit')
                qemu.close()
                logger_info(firmware.get_uuid(), 'tracing', 'qemudebug', 'done', 0)

