from unittest import TestCase

from analyses.trace.format import QEMUDebug
from profile.tinyft import TinyForTestFirmware
from analyses.trace.collection import trace_collection

import math


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
        trace.detect_dead_loop()
        self.assertEqual(trace.loops.__len__(), 77)
        trace.load_in_asm()
        self.assertEqual(trace.bbs.__len__(), 5016)
        for uuid, loop in trace.loops.items():
            reg_offset = trace.cpus[uuid]['offset']
            c = math.floor(math.log(reg_offset, 10)) + 1
            length = loop['length']
            iteration = loop['iteration']
            print('This loop starts at line {}, repeated {} times!'.format(reg_offset, iteration))
            for i in range(uuid, uuid + length + 1):
                pc = trace.cpus[i]['pc']
                bb_offset = trace.bbs[pc]['offset']
                for j, line in enumerate(trace.bbs[pc]['content']):
                    print('{} {}'.format('-' * c, line))
                for j, line in enumerate(trace.cpus[i]['content']):
                    reg_offset = trace.cpus[i]['offset']
                    print('{} {}'.format(reg_offset, line))
                print()
            break