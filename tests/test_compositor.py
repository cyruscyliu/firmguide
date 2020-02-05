from unittest import TestCase

from slcore.compositor import unpack
from slcore.compositor import Components
from settings import *

import os
import tempfile

class TestCompositor(TestCase):
    def test_dynamic_attrs(self):
        components = Components()

        self.assertEqual(None, components.get_path_to_kernel())

    def test_unpack1(self):
        components = unpack(
            os.path.join(TESTS_DIR, '9874f62ffd1d5d1ccdfa919cc29794f03d1f08db.bin'),
            target_dir=tempfile.gettempdir(), extract=False)

        self.assertIsNotNone(components.get_path_to_uimage())
        self.assertIsNotNone(components.get_path_to_kernel())
        self.assertIsNotNone(components.get_path_to_rootfs())
        self.assertTrue(components.supported)

    def test_unpack2(self):
        components = unpack(
            os.path.join(TESTS_DIR, '2b38a390ba53209a1fa4c6aed8489c14774db4c9.bin'),
            target_dir=tempfile.gettempdir(), extract=False)

        self.assertIsNotNone(components.get_path_to_uimage())
        self.assertIsNotNone(components.get_path_to_kernel())
        self.assertIsNone(components.get_path_to_rootfs())
        self.assertTrue(components.supported)
        self.assertTrue(components.has_device_tree())

    def test_unpack3(self):
        components = unpack(
            os.path.join(TESTS_DIR, 'ec5859077831e078987ebb05461d4ec834896f3e.bin'),
            target_dir=tempfile.gettempdir(), extract=False)

        self.assertIsNotNone(components.get_path_to_uimage())
        self.assertIsNotNone(components.get_path_to_kernel())
        self.assertIsNotNone(components.get_path_to_rootfs())
        self.assertTrue(components.supported)

    def test_unpack4(self):
        components = unpack(
            os.path.join(TESTS_DIR, '00107b9211802ca6923ab9bdcdc891266562db70.bin'),
            target_dir=tempfile.gettempdir(), extract=False)

        self.assertFalse(components.supported)


