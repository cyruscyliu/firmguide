from unittest import TestCase

from analyses.trace.format import QEMUDebug
from profile.tinyft import TinyForTestFirmware
from analyses.trace.collection import trace_collection


class TraceAnalysisTest(TestCase):
    def test_trace_collection(self):
        firmware = TinyForTestFirmware(**{'uuid': 123456789, 'name': None, 'path': None, 'size': None})
        running_command = 'build/qemu-4.0.0/arm-softmmu/qemu-system-arm ' \
                          '-M nas7820 -kernel tests/files/nas7820.uImage -dtb tests/files/nas7820.dtb ' \
                          '-nographic'
        firmware.set_running_command(running_command)
        trace_collection(firmware)

    def test_scan_user_level(self):
        path_to_trace = 'tests/files/trace.qemudebug'
        trace = QEMUDebug(path_to_trace)
        self.assertFalse(trace.scan_user_level())

    def test_trace_all(self):
        path_to_trace = 'tests/files/trace.qemudebug'
        trace = QEMUDebug(path_to_trace)
        trace.load_cpu()
        trace.cycle_detection_all()
        self.assertEqual(trace.loops.__len__(), 77)
