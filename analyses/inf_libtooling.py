"""
Source Code Info Extraction.
"""
import os

from analyses.analysis import Analysis


class LibTooling(Analysis):
    def run(self, firmware):
        # uarts
        firmware.set_uart_num(2)
        firmware.set_uart_name('serial8250', 0)
        firmware.set_uart_mmio_base('0xf1012000', 0)
        firmware.set_uart_mmio_size('0x100', 0)
        firmware.set_uart_baud_rate('115200', 0)
        firmware.set_uart_reg_shift('2', 0)
        firmware.set_uart_irq('3', 0)
        firmware.set_uart_name('serial8250', 1)
        firmware.set_uart_mmio_base('0xf1012100', 1)
        firmware.set_uart_mmio_size('0x100', 1)
        firmware.set_uart_baud_rate('115200', 1)
        firmware.set_uart_reg_shift('2', 1)
        firmware.set_uart_irq('4', 1)
        self.info(firmware, 'set uart manually, waiting for libtooling ...', 1)
        firmware.set_flash_base('0xf4000000')
        firmware.set_flash_size('8 * MiB')
        self.info(firmware, 'set flash manually, waiting for libtooling ...', 1)
        return True

    def __init__(self, analysis_manager):
        super().__init__(analysis_manager)
        self.name = 'kerberos'
        self.description = 'source code info extraction (libtooling)'
        self.required = ['srcode']
        self.context['hint'] = ''
        self.critical = False
