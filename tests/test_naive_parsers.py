from unittest import TestCase

from slcore.naive_parsers.symbols import parse_system_map, addr2file
from settings import *
import os

class TestNaiveParsers(TestCase):
    def test_parse_system_map(self):
        test_system_map = os.path.join(TESTS_DIR, 'test_system_map')
        with open(test_system_map, 'w') as f:
            f.write('0xFFFFFFFF01234567 T hello_world')

        system_map = parse_system_map(test_system_map)
        self.assertEqual(system_map['hello_world']['type'], 'T')
        self.assertEqual(system_map['hello_world']['addr'], 0x01234567)

        system_map = parse_system_map(test_system_map, bits=48)
        self.assertEqual(system_map['hello_world']['addr'], 0xFFFF01234567)

    def test_addr2line(self):
        test_binary = os.path.join(TESTS_DIR, 'vmlinux')

        f = addr2file(test_binary, 0x803db1e8)
        self.assertTrue(f.endswith('.h'))

        f = addr2file(test_binary, 0x01234567)
        self.assertIsNone(f)

