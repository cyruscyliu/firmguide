from unittest import TestCase

from profile.tinyft import TinyForTestFirmware
from supervisor.tasks import trace_collection


class SupervisorTest(TestCase):
    def test_trace_collection(self):
        firmware = TinyForTestFirmware(**{'uuid': 123456789, 'name': None, 'path': None, 'size': None})
        running_command = 'build/qemu-4.0.0/arm-softmmu/qemu-system-arm ' \
                          '-M nas7820 -kernel tests/files/nas7820.uImage -dtb tests/files/nas7820.dtb ' \
                          '-nographic'
        firmware.set_running_command(running_command)
        trace_collection(firmware)
