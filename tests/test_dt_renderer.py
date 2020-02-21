from unittest import TestCase

from settings import *
from slcore.profile.firmwaref import get_firmware
from slcore.generation.dt_renderer import DTRenderer
from slcore.environment import setup_target_dir

import os
import tempfile


class TestDTRenderer(TestCase):
    def test_machine(self):
        firmware = get_firmware('simple')

        target_dir = setup_target_dir('test_machine')
        firmware.set_target_dir(target_dir)
        path_to_profile = os.path.join(TESTS_DIR, 'profile.yaml')
        firmware.set_profile(path_to_profile=path_to_profile)
        firmware.set_dtb(os.path.join(TESTS_DIR, 'profile.dtb'))

        dt_renderer = DTRenderer(firmware)
        dt_renderer.load_template()
        a = dt_renderer.render()
        self.assertTrue(a)

