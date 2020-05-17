"""
Unit test for slcore/aconfig, slcore/aregister.py, slcore/tools/lanalysis.py.
"""
from unittest import TestCase
from slcore.tools.lanalysis import list_analysis_and_group


class TestListAnalysis(TestCase):
    def test_list_analysis_and_group(self):
        self.assertTrue(list_analysis_and_group())
