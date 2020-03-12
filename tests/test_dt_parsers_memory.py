from unittest import TestCase
from slcore.dt_parsers.common import load_dtb, compile_dts
from slcore.dt_parsers.memory import find_memory, \
    find_memory_in_fdt
import os


class TestNaiveParsers(TestCase):
    def compile_dts(self, name):
        path_to_dts = os.path.join(
            os.path.dirname(os.path.realpath(__file__)),
            name)
        return compile_dts(path_to_dts)

    def test_memory_generic_case(self):
        path_to_dtb = self.compile_dts(
            'dts/memory_generic_case.dts')
        dts = load_dtb(path_to_dtb)
        a = find_memory_in_fdt(dts)
        self.assertEqual(1, len(a['regs']))
        self.assertEqual(0x0, a['regs'][0]['base'])
        self.assertEqual(0x2000, a['regs'][0]['size'])
        a = find_memory(path_to_dtb)
        self.assertEqual(1, len(a['regs']))
        self.assertEqual(0x0, a['regs'][0]['base'])
        self.assertEqual(0x2000, a['regs'][0]['size'])

    def test_memory_dual_rams(self):
        path_to_dtb = self.compile_dts(
            'dts/memory_dual_rams.dts')
        dts = load_dtb(path_to_dtb)
        a = find_memory_in_fdt(dts)
        self.assertEqual(2, len(a['regs']))

    def test_memory_no_memory_node(self):
        path_to_dtb = self.compile_dts(
            'dts/memory_no_memory_node.dts')
        dts = load_dtb(path_to_dtb)
        a = find_memory_in_fdt(dts)
        self.assertIsNone(a)

    def test_memory_zero_regs(self):
        path_to_dtb = self.compile_dts(
            'dts/memory_zero_regs.dts')
        dts = load_dtb(path_to_dtb)
        a = find_memory_in_fdt(dts)
        self.assertEqual(0, len(a['regs']))

    def test_memory_path_with_act(self):
        path_to_dtb = self.compile_dts(
            'dts/memory_path_with_act.dts')
        dts = load_dtb(path_to_dtb)
        a = find_memory_in_fdt(dts)
        self.assertEqual(1, len(a['regs']))
        self.assertEqual(0x0, a['regs'][0]['base'])
        self.assertEqual(0x2000, a['regs'][0]['size'])
        a = find_memory(path_to_dtb)
        self.assertEqual(1, len(a['regs']))
        self.assertEqual(0x0, a['regs'][0]['base'])
        self.assertEqual(0x2000, a['regs'][0]['size'])

