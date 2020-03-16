from unittest import TestCase

from slcore.qemuc import QEMUController
from settings import *

import os

class TestQEMUController(TestCase):
    def test_get_command(self):
        qemuc = QEMUController(os.path.join(WORKING_DIR, QEMU_DIR_NAME))
        path_to_vmlinux = os.path.join(TESTS_DIR, 'vmlinux')
        running_command = qemuc.get_command('arm', 'l', 'wrt350n_v2', path_to_vmlinux)
        # qemu-system-arm -M wrt350n_v2 -kernel /root/esv/tests/vmlinux -nographic -append "console=ttyS0"
        self.assertEqual(
            running_command.split('-M')[1].strip(),
            'wrt350n_v2 -kernel /root/esv/tests/vmlinux -nographic -append "console=ttyS0"')

    def test_patch_recover(self):
        qemuc = QEMUController(os.path.join(WORKING_DIR, QEMU_DIR_NAME))

        # patch(abs/p/t/old, rel/p/t/new, bak=True)
        old = os.path.join(BASE_DIR, 'examples/machines/wrt350n_v2.c')
        new = 'hw/arm/wrt350n_v2.c'

        # 1 patch a file which doesn't exist
        qemuc.patch(old, new)
        qemuc.recover()
        self.assertFalse(os.path.exists(new))

        # 2 patch a file which exists
        abs_new = os.path.join(WORKING_DIR, QEMU_DIR_NAME, new)
        os.system('cp {} {}'.format(old, abs_new))
        qemuc.patch(old, new)
        self.assertTrue(os.path.exists(abs_new + '.bak'))
        qemuc.recover()
        self.assertTrue(os.path.exists(abs_new))
        os.system('rm {}'.format(abs_new))

    def test_install_recover(self):
        qemuc = QEMUController(os.path.join(WORKING_DIR, QEMU_DIR_NAME))

        # install(prefix)
        prefix = os.path.join(TESTS_DIR, 'qemu_install')
        qemuc.install(prefix)
        abs_new = os.path.join(WORKING_DIR, QEMU_DIR_NAME, 'wrt350n_v2.c')
        self.assertTrue(os.path.exists(abs_new))
        qemuc.recover()
        self.assertFalse(os.path.exists(abs_new))

    def test_compile(self):
        qemuc = QEMUController(os.path.join(WORKING_DIR, QEMU_DIR_NAME))
        qemuc.compile()

    def test_debug(self):
        qemuc = QEMUController(os.path.join(WORKING_DIR, QEMU_DIR_NAME))
        path_to_vmlinux = os.path.join(TESTS_DIR, 'vmlinux')
        running_command = qemuc.get_command('arm', 'l', 'versatilepb', path_to_vmlinux)
        qemuc.debug(running_command, path_to_vmlinux)

    def test_trace(self):
        pass

    def test_add_target(self):
        # add_target('hwname', 'hwname', type_='hw', arch='arm', endian='l')
        qemuc = QEMUController(os.path.join(WORKING_DIR, QEMU_DIR_NAME))
        qemuc.add_target('hwname', 'hwname', t='hw', arch='arm', endian='l')
        qemuc.recover()

        # add_target('hwname', 'fname', type_='intc')
        qemuc.add_target('hwname', 'fname', t='intc')
        abs_new = os.path.join(WORKING_DIR, QEMU_DIR_NAME, 'hw/intc/Makefile.objs')
        self.assertTrue(os.path.exists(abs_new + '.bak'))
        qemuc.recover()
        self.assertTrue(os.path.exists(abs_new))
        self.assertFalse(os.path.exists(abs_new + '.bak'))


