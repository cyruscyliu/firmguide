"""
The whole generator accepts the device profile which must be preprocessed.
"""
import hashlib

from logger import logger_info, logger_debug


class PreProcessor(object):
    def __init__(self, firmware):
        self.firmware = firmware

    def info(self, message):
        logger_info(self.firmware.get_uuid(), 'code_generation', 'preprocessing', message, 0)

    def debug(self, message):
        logger_debug(self.firmware.get_uuid(), 'code_generation', 'proprocessing', message, 0)

    def preprocess_machine_name(self):
        if self.firmware.get_machine_name() is None:
            # it's ok if we cannot find a machine name
            tmp_machine_name = 'salamander' + hashlib.md5(self.firmware.get_name().encode('utf-8')).hexdigest()
            self.firmware.set_machine_name(tmp_machine_name)
            self.info('machine name not exists, refer to {}'.format(tmp_machine_name))

    def preprocess_machine_description(self):
        if self.firmware.get_machine_description() is None:
            # it's ok if we cannot find a machine description
            self.firmware.set_machine_description(self.firmware.get_machine_name())
            self.info('machine description not exists, refer to {}'.format(self.firmware.get_machine_name()))

    def preprocess_ram_priority(self):
        if self.firmware.get_ram_priority() is None:
            self.firmware.set_ram_priority("0")
            self.info('ram prioirty not exists, refer to "0"')

    def preprocess_flash_section_size(self):
        if self.firmware.get_flash_type() == 'nor' and self.firmware.get_flash_section_size() is None:
            section_size = '64 * KiB'
            self.firmware.set_flash_section_size(section_size)
            self.info('nor flash section size not exists, refer to {}'.format(section_size))

    def preprocess(self):
        # handle non-critical things
        self.preprocess_machine_name()
        self.preprocess_machine_description()
        self.preprocess_ram_priority()
        self.preprocess_flash_section_size()
