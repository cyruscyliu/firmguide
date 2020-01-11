'''
Source Code Info Extraction.
'''
import os

from analyses.analysis import Analysis


class LibTooling(Analysis):
    def run(self, firmware):
        if firmware.get_uuid() == '15007':
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
            firmware.set_interrupt_controller_name('sintc')
            firmware.set_interrupt_controller_mmio_base('0xf1020100')
            firmware.set_interrupt_controller_mmio_size('0x200')
            firmware.set_interrupt_controller_registers('interrupt_cause_register', '0x100', '0x0')
            firmware.set_interrupt_controller_registers('interrupt_mask_register', '0x104', '0x0')
            firmware.set_interrupt_controller_registers('interrupt_clear_register', '0x010', '0x0')
            firmware.set_timer_irq('0x0')
            self.info(firmware, 'set interrupt controller manually, waiting for libtooling ...', 1)
            firmware.set_va_pa_mapping('0xfdd00000', '0xf1000000', '0x100000')
            firmware.set_va_pa_mapping('0xfde00000', '0xf2000000', '0x100000')
            firmware.set_va_pa_mapping('0xfdf00000', '0xf2100000', '0x100000')
            firmware.set_va_pa_mapping('0xfe000000', '0xf0000000', '0x1000000')
            self.info(firmware, 'set va/pa mapping manually, waiting for libtooling ...', 1)
        elif firmware.get_uuid() == '13882':
            firmware.set_va_pa_mapping('0xf0002000', '0x47000000', '0x2000')
            firmware.set_va_pa_mapping('0xf0004000', '0x44e00000', '0x1000')
            firmware.set_va_pa_mapping('0xf0005000', '0x44f00000', '0x1000')
            firmware.set_va_pa_mapping('0xf0006000', '0x44400000', '0x1000')
            firmware.set_va_pa_mapping('0xfdd07000', '0x44500000', '0x1000')
            self.info(firmware, 'set va/pa mapping manually, waiting for libtooling ...', 1)
        elif firmware.get_uuid() == '14567':
            firmware.set_uart_num(1)
            firmware.set_uart_name('serial8250', 0)
            firmware.set_uart_mmio_base('0x18020000', 0)
            firmware.set_uart_mmio_size('0x100', 0)
            firmware.set_uart_baud_rate('115200', 0)
            firmware.set_uart_reg_shift('0', 0)
            firmware.set_uart_irq('3', 0)  # 11
            self.info(firmware, 'set uart manually, waiting for libtooling ...', 1)
            firmware.set_va_pa_mapping('0x80000000', '0x00000000', '0x20000000')
            firmware.set_va_pa_mapping('0xa0000000', '0x00000000', '0x20000000')
            self.info(firmware, 'set mips va/pa mapping manually (kseg0/1)', 1)
            firmware.set_flash_base('0x1f000000')
            firmware.set_flash_size('32 * MiB')
            self.info(firmware, 'set flash manually, waiting for libtooling ...', 1)
        elif firmware.get_uuid() == '14235':
            firmware.set_uart_num(1)
            firmware.set_uart_name('serial8250', 0)
            firmware.set_uart_mmio_base('0x18000000', 0)
            firmware.set_uart_mmio_size('0x100', 0)
            firmware.set_uart_baud_rate('115200', 0)
            firmware.set_uart_reg_shift('0', 0)
            firmware.set_uart_irq('3', 0)  # unknown    
            self.info(firmware, 'set uart manually, waiting for libtooling ...', 1)
        return True

    def __init__(self, analysis_manager):
        super().__init__(analysis_manager)
        self.name = 'kerberos'
        self.description = 'source code info extraction (libtooling)'
        self.required = ['srcode']
        self.context['hint'] = ''
        self.critical = False
        #
        # according to usage of analysis bamboo
        # put str(start_address) in bamboo_address is ok
        self.bamboo_address = []
