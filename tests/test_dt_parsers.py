from unittest import TestCase

from slcore.dt_parsers.mmio import *
from slcore.dt_parsers.flash import *
from slcore.dt_parsers.common import load_dtb
from settings import *
import os

class TestNaiveParsers(TestCase):
    def test_mmio_fix_address(self):
        path_to_dtb = os.path.join(TESTS_DIR, 'orion5x-netgear-wnr854t.dtb')
        dts = load_dtb(path_to_dtb)

        mmio = find_flatten_mmio_in_fdt(dts)
        # print(mmio)

    def test_get_flatten_flash(self):
        path_to_dtb = os.path.join(TESTS_DIR, 'orion5x-netgear-wnr854t.dtb')
        dts = load_dtb(path_to_dtb)

        flashes = find_flatten_flash_in_fdt(dts)
        print(flashes)

