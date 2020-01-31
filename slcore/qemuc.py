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
import os
import qmp
import subprocess

from settings import *


class QEMUController(object):
    def __init__(self):
        self.modified = []
        self.new = []
        self.qemu_root = os.path.join(WORKING_DIR, QEMU_DIR_NAME)

    def get_file_path(self, path):
        return os.path.join(self.qemu_root, path)

    def get_binary(self, arch, endian):
        if arch == 'arm':
            return '{}/arm-softmmu/qemu-system-arm'.format(self.qemu_root)
        elif arch == 'mips':
            if endian == 'l':
                return '{}/mipsel-softmmu/qemu-system-mipsel'.format(self.qemu_root)
            else:
                return '{}/mips-softmmu/qemu-system-mips'.format(self.qemu_root)

    def get_command(self, arch, endian, machine, kernel, flash=None, image=None, flash_size=None, dtb=None):
        running_command = self.get_binary(arch, endian)
        if running_command is None:
            return None
        running_command += ' -M {}'.format(machine)
        running_command += ' -kernel {}'.format(kernel)
        if dtb:
            running_command += ' -dtb {}'.format(dtb)
        if flash == 'nor':
            running_command += ' -drive file={},if=pflash,format=raw'.format(image)
        elif flash == 'nand':
            running_command += ' -drive file={},if=mtd,format=raw'.format(image)
        running_command += ' -nographic'
        return running_command

    def patch(self, *args, **kwargs):
        """
        this function is not thread safety, combining with
        recover, it can only guarentee the patch is valid

        patch(abs/p/t/src, abs/p/t/dst, bak=True) or
        patch(abs/p/t/new, abs/p/t/old, bak=True)
        """
        src, dst = args
        dst = self.get_file_path(dst)
        if os.path.exists(dst):
            os.system('cp {0} {0}.bak'.format(dst))
            self.modified.append(dst)
        else:
            self.new.append(dst)
        os.system('cp {} {}'.format(src, dst))
        return dst

    def recover(self, *args, **kwargs):
        """
        recover()
        """
        for dst in self.modified:
            os.system('mv {0}.bak {0}'.format(dst))
        for dst in self.new:
            os.system('rm {}'.format(dst))

    def compile(self, cflags=None, cpu=4):
        if cflags:
            os.system('cd {}/{} && make -j{} CFLAGS={} && cd $OLDPWD'.format(WORKING_DIR, QEMU_DIR_NAME, cpu, cflags))
        else:
            os.system('cd {}/{} && make -j{} && cd $OLDPWD'.format(WORKING_DIR, QEMU_DIR_NAME, cpu))

    def run(self, *args, **kwargs):
        """
        run(command) w/ abs/p/t/qemu
        """
        for command in args:
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

        for command in args:
            try:
                subprocess.run(full_command, timeout=20, shell=True)
            except subprocess.TimeoutExpired:
                qemu = qmp.QEMUMonitorProtocol(('localhost', 4444))
                qemu.connect()
                qemu.cmd('quit')
                qemu.close()

