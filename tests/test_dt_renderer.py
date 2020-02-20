from unittest import TestCase

from settings import *
from slcore.profile.firmwaref import get_firmware
from slcore.generation.dt_renderer import DTRenderer

import os
import tempfile


class TestDTRenderer(TestCase):
    def test_machine(self):
        firmware = get_firmware('simple')
        path_to_profile = os.path.join(TESTS_DIR, 'profile.yaml')
        firmware.set_profile(path_to_profile=path_to_profile)
        firmware.set_dtb(os.path.join(TESTS_DIR, 'profile.dtb'))

        dt_renderer = DTRenderer(firmware)
        a = dt_renderer.render()
        print(a)

