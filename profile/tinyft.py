"""
A tiny implementation for testing.
"""
from profile.firmware import Firmware


class TinyForTestFirmware(Firmware):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.properties = {}

    def set_running_command(self, *args, **kwargs):
        running_command = args[0]
        self.properties['running_command'] = running_command

    def get_running_command(self, *args, **kwargs):
        return self.properties['running_command']
