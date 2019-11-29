"""
A tiny implementation for testing.
"""
from profile.firmware import Firmware


class TinyForTestFirmware(Firmware):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
