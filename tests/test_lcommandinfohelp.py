"""
Unit test for slcore/cmdcocnfig, slcore/cgenerator.py,
    slcore/tools/lcommandhelpinfo.py.
"""
from unittest import TestCase
from slcore.tools.lcommandhelpinfo import list_cmd_args, \
    list_cmd_argsf

import os


class TestListCommandHelpInfo(TestCase):
    def test_list_cmd_args(self):
        try:
            list_cmd_args()
        except SystemExit:
            pass

    def test_list_subcommand_args(self):
        try:
            list_cmd_args('create')
        except SystemExit:
            pass

    def test_list_cmd_argsf(self):
        try:
            list_cmd_argsf(os.path.join(
                os.path.dirname(__file__),
                'test.cmd.yaml'
            ))
        except SystemExit:
            pass
