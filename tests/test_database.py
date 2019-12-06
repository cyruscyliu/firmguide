from unittest import TestCase

from database.dbf import get_database


class TestDatabase(TestCase):
    def test_select(self):
        database_qemu_device = get_database('qemu.devices')
        cpu = database_qemu_device.select('cpu', like='arm,arm11mpcore')
        self.assertEqual('arm11mpcore', cpu)
