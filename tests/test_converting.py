import argparse

from unittest import TestCase
from profile.convert import run


class TestConverting(TestCase):
    def test_converting(self):
        """
        ./profile/convert.py -I simple -O dt tests/files/ec5859.yaml -o /tmp/ec5859.dt
        ./profile/convert.py -I simple -O dt tests/files/2b38a3.yaml -o /tmp/2b38a3.dt
        ./profile/convert.py -I simple -O dt tests/files/9874f6.yaml -o /tmp/9874f6.dt
        ./profile/convert.py -I dt -O simple tests/files/2b38a3.dt -o /tmp/2b38a3.yaml
        ./profile/convert.py -I dt -O simple tests/files/2b38a3.dt -o /tmp/2b38a3.yaml
        ./profile/convert.py -I dt -O simple tests/files/9874f6.dt -o /tmp/9874f6.yaml
        """
        parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter)
        parser.add_argument('-I', choices=['simple', 'dt'], required=True, help='input format of the profile')
        parser.add_argument('-O', choices=['simple', 'dt'], required=True, help='target format of the profile')
        parser.add_argument('input', metavar='path/to/profile')
        parser.add_argument('-o', metavar='path/to/target_profile')
        args = parser.parse_args(['-I', 'simple', '-O', 'dt', 'tests/files/ec5859.yaml', '-o', '/tmp/ec5859.dt'])
        run(args)
        args = parser.parse_args(['-I', 'simple', '-O', 'dt', 'tests/files/2b38a3.yaml', '-o', '/tmp/2b38a3.dt'])
        run(args)
        args = parser.parse_args(['-I', 'simple', '-O', 'dt', 'tests/files/9874f6.yaml', '-o', '/tmp/9874f6.dt'])
        run(args)
        args = parser.parse_args(['-O', 'simple', '-I', 'dt', 'tests/files/ec5859.dt', '-o', '/tmp/ec5859.yaml'])
        run(args)
        args = parser.parse_args(['-O', 'simple', '-I', 'dt', 'tests/files/2b38a3.dt', '-o', '/tmp/ec5859.yaml'])
        run(args)
        args = parser.parse_args(['-O', 'simple', '-I', 'dt', 'tests/files/9874f6.dt', '-o', '/tmp/ec5859.yaml'])
        run(args)
