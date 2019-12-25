"""
The whole generator accepts the device profile which must be preprocessed.
"""
import hashlib


class PreProcessor(object):
    def __init__(self, firmware):
        self.firmware = firmware

    def preprocess_machine_name(self):
        if self.firmware.get_machine_name() is None:
            # it's ok if we cannot find a machine name
            tmp_machine_name = 'salamander@' + hashlib.md5(self.firmware.get_name().encode('utf-8')).hexdigest()
            self.firmware.set_machine_name(tmp_machine_name)

    def preprocess_machine_description(self):
        if self.firmware.get_machine_description() is None:
            # it's ok if we cannot find a machine description
            self.firmware.set_machine_description(self.firmware.get_machine_name())

    def preprocess_ram_priority(self):
        if self.firmware.get_ram_priority() is None:
            self.firmware.set_ram_priority("0")

    def preprocess(self):
        # handle non-critical things
        self.preprocess_machine_name()
        self.preprocess_machine_description()
        self.preprocess_ram_priority()
