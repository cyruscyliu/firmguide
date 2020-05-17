from unittest import TestCase
from slcore.qemucontroller import QEMUController

import os

QEMU_DIR = os.path.join(os.path.dirname(__file__), 'qemu-4.0.0')


class TestQEMUController(TestCase):
    def test_get_command(self):
        qemuc = QEMUController(QEMU_DIR)
        path_to_vmlinux = os.path.join(os.path.dirname(__file__), 'vmlinux')
        running_command = \
            qemuc.get_command('arm', 'l', 'wrt350n_v2', path_to_vmlinux)
        # qemu-system-arm -M wrt350n_v2
        # -kernel /root/esv/tests/vmlinux -nographic -append "console=ttyS0"
        print(running_command)
        self.assertEqual(
            running_command.split('-M')[1].strip(),
            'wrt350n_v2 -kernel {} -nographic -append "console=ttyS0 nowatchdog nokaslr"'.format(
                path_to_vmlinux))

    def test_patch_recover(self):
        qemuc = QEMUController(QEMU_DIR)

        # patch(abs/p/t/old, rel/p/t/new, bak=True)
        old = os.path.join(os.path.dirname(__file__), 'wrt350n_v2.c')
        new = 'hw/arm/wrt350n_v2.c'

        # 1 patch a file which doesn't exist
        qemuc.patch(old, new)
        qemuc.recover()
        self.assertFalse(os.path.exists(new))

        # 2 patch a file which exists
        abs_new = os.path.join(QEMU_DIR, new)
        os.system('cp {} {}'.format(old, abs_new))
        qemuc.patch(old, new)
        self.assertTrue(os.path.exists(abs_new + '.bak'))
        qemuc.recover()
        self.assertTrue(os.path.exists(abs_new))
        os.system('rm {}'.format(abs_new))

    def test_install_recover(self):
        qemuc = QEMUController(QEMU_DIR)

        # install(prefix)
        prefix = \
            os.path.join(os.path.dirname(__file__), 'qemu-install')
        qemuc.install(prefix)
        abs_new = os.path.join(QEMU_DIR, 'wrt350n_v2.c')
        self.assertTrue(os.path.exists(abs_new))
        qemuc.recover()
        self.assertFalse(os.path.exists(abs_new))

    def test_compile(self):
        qemuc = QEMUController(QEMU_DIR)
        qemuc.compile()

    def test_debug(self):
        qemuc = QEMUController(QEMU_DIR)
        path_to_vmlinux = os.path.join(os.path.dirname(__file__), 'vmlinux')
        running_command = \
            qemuc.get_command('arm', 'l', 'versatilepb', path_to_vmlinux)
        qemuc.debug(running_command, path_to_vmlinux)

    def test_trace(self):
        pass

    def test_add_target(self):
        # add_target('hwname', 'hwname', type_='hw', arch='arm', endian='l')
        qemuc = QEMUController(QEMU_DIR)
        qemuc.add_target('hwname', 'hwname', t='hw', arch='arm', endian='l')
        qemuc.recover()

        # add_target('hwname', 'fname', type_='intc')
        qemuc.add_target('hwname', 'fname', t='intc')
        abs_new = os.path.join(QEMU_DIR, 'hw/intc/Makefile.objs')
        self.assertTrue(os.path.exists(abs_new + '.bak'))
        qemuc.recover()
        self.assertTrue(os.path.exists(abs_new))
        self.assertFalse(os.path.exists(abs_new + '.bak'))
