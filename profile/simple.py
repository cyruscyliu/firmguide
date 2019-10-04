"""
Our ugly solution.
"""
from profile.firmware import Firmware


class SimpleFirmware(Firmware):
    def set(self, *args, **kwargs):
        pass

    def get(self, *args, **kwargs):
        pass

    def __init__(self, *args, **kwargs):
        super(SimpleFirmware, self).__init__(*args, **kwargs)
