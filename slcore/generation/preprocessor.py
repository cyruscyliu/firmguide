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

    def preprocess_machine_description(self):
        if self.firmware.get_machine_description() is None:
            # it's ok if we cannot find a machine description
            self.firmware.set_machine_description(self.firmware.get_machine_name())
            self.debug('machine description not exists, refer to {}'.format(self.firmware.get_machine_name()))

    def preprocess_ram_priority(self):
        if self.firmware.get_ram_priority() is None:
            self.firmware.set_ram_priority("0")
            self.debug('ram prioirty not exists, refer to "0"')

    def preprocess_uart_baud_rate(self):
        for i in range(0, self.firmware.get_uart_num()):
            if self.firmware.get_uart_baud_rate(i) is None:
                baud_rate = "115200"
                self.firmware.set_uart_baud_rate(baud_rate, i)
                self.debug('uart baud rate not exist, refre to {}'.format(baud_rate))

    def preprocess_flash_section_size(self):
        for i in range(0, self.firmware.get_flash_num()):
            if self.firmware.get_flash_type(i) == 'nor' and self.firmware.get_flash_section_size(i) is None:
                section_size = '64 * KiB'
                self.firmware.set_flash_section_size(section_size, i)
                self.debug('nor flash section size not exists, refer to {}'.format(section_size))

    def preprocess(self):
        # handle non-critical things
        self.preprocess_machine_description()
        self.preprocess_ram_priority()
        self.preprocess_uart_baud_rate()
        self.preprocess_flash_section_size()

