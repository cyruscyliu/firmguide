import argparse

from unittest import TestCase
from supervisor.scheduler import run


class TestGeneration(TestCase):
    def test_generation(self):
        """
        ./salamander.py -g tests/files/2b38a3.yaml -a arm -wd build/ -p simple
        ./salamander.py -g tests/files/ec5859.yaml -a arm -wd build/ -p simple
        ./salamander.py -g tests/files/9874f6.yaml -a mips -wd build/ -p simple
        """
        parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter)
        # general
        parser.add_argument('-p', '--profile', choices=['simple', 'dt', 'ipxact'], default='dt')
        parser.add_argument('-wd', '--working_directory')
        parser.add_argument('-r', '--rerun', action='store_true', default=False,
                            help='ingore save and restore and rerun all analysis')
        parser.add_argument('-d', '--debug', action='store_true', help='show verbose logs')
        # analysis
        group = parser.add_argument_group('analysis')
        group.add_argument('-f', '--firmware', type=str, metavar='path/to/firmware')
        group.add_argument('-u', '--uuid', type=str)
        group.add_argument('-a', '--architecture', type=str, choices=['arm', 'mips'])
        group.add_argument('-e', '--endian', type=str, choices=['b', 'l'])
        group.add_argument('-b', '--brand', type=str, choices=['openwrt'])
        group.add_argument('-q', '--quick', action='store_true', default=False, help='disable tracing and diagnosis')
        group.add_argument('-s', '--source_code', type=str, metavar='path/to/source_code')
        # generation
        group = parser.add_argument_group('code generation')
        group.add_argument('-g', '--generation', type=str, metavar='path/to/device_profile')
        # diagnosis
        group = parser.add_argument_group('diagnosis')
        group.add_argument('-t', '--trace', type=str, metavar='path/to/trace')
        group.add_argument('-tf', '--trace_format', type=str, choices=['ktracer', 'qemudebug'], default='qemudebug')

        args = parser.parse_args(['-g', 'tests/files/ec5859.yaml', '-a', 'arm', '-wd', 'build/', '-p', 'simple'])
        run(parser, args)
        args = parser.parse_args(['-g', 'tests/files/2b38a3.yaml', '-a', 'arm', '-wd', 'build/', '-p', 'simple'])
        run(parser, args)
        args = parser.parse_args(['-g', 'tests/files/9874f6.yaml', '-a', 'arm', '-wd', 'build/', '-p', 'simple'])
        run(parser, args)
