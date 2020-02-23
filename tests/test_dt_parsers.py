from unittest import TestCase

from slcore.dt_parsers.mmio import *
from settings import *
import os

class TestNaiveParsers(TestCase):
    def test_mmio_fix_address(self):
        mmio = find_mmio_in_fla

