from unittest import TestCase

from slcore.dt_parsers.common import load_dtb, compile_dts
from slcore.dt_parsers.mmio import find_mmio_by_path, \
    find_parent_offset
import os


class TestDTParsersMMIO(TestCase):
    def compile_dts(self, name):
        path_to_dts = os.path.join(
            os.path.dirname(os.path.realpath(__file__)),
            name)
        return compile_dts(path_to_dts)

    def test_mmio_complex_ranges(self):
        path_to_dtb = self.compile_dts(
            'dts/mmio_complex_ranges.dts')
        dts = load_dtb(path_to_dtb)
        offset = find_parent_offset(dts, '/soc/spi@10600', 0xF0010000, None, debug=True)
        self.assertEqual(0xf1000000, offset + 0xF0010000)

        offset = find_parent_offset(dts, '/soc/spi@10600', 0x011E0000, None, debug=True)
        self.assertEqual(0xfff10000, offset + 0x011E0000)

        offset = find_parent_offset(dts, '/soc/spi@10600', 0x015E0000, None, debug=True)
        self.assertIsNone(offset)

        offset = find_parent_offset(dts, '/soc/spi@10600', 0x019E0000, None, debug=True)
        self.assertIsNone(offset)

        offset = find_parent_offset(dts, '/soc/spi@10600', 0x01DE0000, None, debug=True)
        self.assertIsNone(offset)

        offset = find_parent_offset(dts, '/soc/spi@10600', 0x011F0000, None, debug=True)
        self.assertEqual(0xfff20000, offset + 0x011F0000)

        offset = find_parent_offset(dts, '/soc/spi@10600', 0x015E0000, None, debug=True)
        self.assertIsNone(offset)

        offset = find_parent_offset(dts, '/soc/spi@10600', 0x019F0000, None, debug=True)
        self.assertIsNone(offset)

        offset = find_parent_offset(dts, '/soc/spi@10600', 0x01DF0000, None, debug=True)
        self.assertIsNone(offset)

    def test_mmio_multilevel_ranges(self):
        path_to_dtb = self.compile_dts(
            'dts/mmio_multilevel_ranges.dts')
        dts = load_dtb(path_to_dtb)
        offset = find_parent_offset(dts, '/soc/internal-regs/interrupt-controller@20a00', 0x20A00, None, debug=True)
        self.assertEqual(0xf1020a00, offset + 0x20a00)

