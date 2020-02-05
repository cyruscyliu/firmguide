from unittest import TestCase

from slcore.compositor import Common
from settings import *

import os
import tempfile

class TestCompositor(TestCase):
    def test_set_attributes(self):
        common = Common()

        TEST_ATTRIBUTS = ['test', 'attrs']
        common.set_attributes(TEST_ATTRIBUTS)

        self.assertEqual(None, common.get_test())
        self.assertEqual(None, common.get_attrs())

        TEST_ATTRIBUTS = {'test': 'A', 'attrs': 'B'}
        common.set_attributes(TEST_ATTRIBUTS)

        attrs = common.get_attributes()
        self.assertEqual({'test': 'A', 'attrs': 'B'}, attrs)


    def test_get_attributes(self):
        common = Common()

        TEST_ATTRIBUTS = ['test', 'attrs']
        common.set_attributes(TEST_ATTRIBUTS)

        attrs = common.get_attributes()
        self.assertEqual({'test': None, 'attrs': None}, attrs)

