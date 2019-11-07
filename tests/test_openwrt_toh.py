from unittest import TestCase

from database.dbf import get_database


class TestOpenwrtToh(TestCase):
    def test_find_openwrt_toh(self):
        openwrt = get_database('openwrt')
        results = openwrt.select('*', supportedcurrentrel='10.03', target='orion', subtarget='')
        self.assertEqual(1, len(results))
        self.assertLess(len(results[0]), 60)
        results = openwrt.select('target', transpose=True)
        self.assertEqual(1, len(results))
        l = len(results[0])
        results = openwrt.select('target', 'subtarget', transpose=True, deduplicated=True)
        self.assertEqual(2, len(results))
        self.assertLess(len(results[0]), l)
