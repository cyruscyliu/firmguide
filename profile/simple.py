"""
Our ugly solution.
"""
from generation.generatori import CodeGenerationInterface
from profile.firmware import Firmware


class SimpleFirmware(Firmware, CodeGenerationInterface):
    def sget_ram_priority(self):
        if 'ram_priority' in self.profile['ram']:
            return self.profile['ram']['ram_priority']
        else:
            return '-1'

    def sget_interrupt_controller_name(self):
        return self.profile['interrupt_controller']['ic_name']

    def lget_interrupt_controller_registers(self):
        return self.profile['interrupt_controller']['ic_registers']

    def sget_interrupt_controller_mmio_size(self):
        return self.profile['interrupt_controller']['ic_mmio_size']

    def sget_interrupt_controller_mmio_base(self):
        return self.profile['interrupt_controller']['ic_mmio_base']

    def sget_n_irqs(self):
        return self.profile['interrupt_controller']['ic_n_irqs']

    def sget_timer_name(self):
        return self.profile['timer']['timer_name']

    def lget_timer_registers(self):
        return self.profile['timer']['timer_registers']

    def sget_timer_mmio_size(self):
        return self.profile['timer']['timer_mmio_size']

    def sget_timer_mmio_base(self):
        return self.profile['timer']['timer_mmio_base']

    def sget_uart_baud_rate(self):
        return self.profile['uart']['uart_baud_rate']

    def sget_uart_reg_shift(self):
        return self.profile['uart']['uart_reg_shift']

    def sget_uart_irq(self):
        return self.profile['uart']['uart_irq']

    def sget_flash_base(self):
        return self.profile['flash']['flash_base']

    def sget_uart_mmio_base(self):
        return self.profile['uart']['uart_mmio_base']

    def sget_cpu_pp_mmio_base(self):
        return self.profile['cpu_pp']['cpu_pp_mmio_base']

    def probe_cpu_pp_model(self):
        return 'cpu_pp' in self.profile

    def sget_flash_type(self):
        return self.profile['flash']['flash_type']

    def sget_flash_size(self):
        return self.profile['flash']['flash_size']

    def sget_flash_section_size(self):
        return self.profile['flash']['flash_section_size']

    def sget_path_to_kernel(self):
        return ''
        # return self.get_path_to_kernel()

    def sget_board_id(self):
        return self.profile['board_id']

    def lget_bamboo_devices(self):
        if 'bamboo' in self.profile:
            return self.profile['bamboo']
        else:
            return []

    def sget_machine_description(self):
        return self.profile['machine_desc']

    def sget_machine_name(self):
        return self.profile['machine_name']

    def sget_architecture(self):
        return self.profile['architecture']

    def sget_ram_size(self):
        return self.profile['ram']['ram_size']

    def sget_cpu_model(self):
        return self.profile['cpu']['cpu_type']

    def set_url(self, *args, **kwargs):
        pass

    def get_url(self, *args, **kwargs):
        pass

    def set_format(self, *args, **kwargs):
        pass

    def get_format(self, *args, **kwargs):
        pass

    def set_homepage(self, *args, **kwargs):
        pass

    def get_homepage(self, *args, **kwargs):
        pass

    def set_description(self, *args, **kwargs):
        pass

    def get_description(self, *args, **kwargs):
        pass

    def set_path_to_image(self, *args, **kwargs):
        pass

    def get_path_to_image(self, *args, **kwargs):
        pass

    def set_path_to_kernel(self, *args, **kwargs):
        pass

    def get_path_to_kernel(self, *args, **kwargs):
        pass

    def set_path_to_dtb(self, *args, **kwargs):
        pass

    def get_path_to_dtb(self, *args, **kwargs):
        pass

    def set_path_to_source_code(self, *args, **kwargs):
        pass

    def get_path_to_source_code(self, *args, **kwargs):
        pass

    def set_toh(self, *args, **kwargs):
        pass

    def get_toh(self, *args, **kwargs):
        pass

    def save_profile(self, *args, **kwargs):
        pass

    def get_endian(self, *args, **kwargs):
        pass

    def set_endian(self, *args, **kwargs):
        pass

    def get_dts(self, *args, **kwargs):
        pass

    def set_dts(self, *args, **kwargs):
        pass

    def get_soc_model(self, *args, **kwargs):
        pass

    def set_soc_model(self, *args, **kwargs):
        pass

    def get_interrupt_controller_model(self, *args, **kwargs):
        pass

    def set_interrupt_controller_model(self, *args, **kwargs):
        pass

    def get_flash_model(self, *args, **kwargs):
        pass

    def set_flash_model(self, *args, **kwargs):
        pass

    def get_flash_size(self, *args, **kwargs):
        pass

    def set_flash_size(self, *args, **kwargs):
        pass

    def set_flash_type(self, *args, **kwargs):
        pass

    def get_flash_type(self, *args, **kwargs):
        pass

    def get_uart_model(self, *args, **kwargs):
        pass

    def set_uart_model(self, *args, **kwargs):
        pass

    def get_timer_model(self, *args, **kwargs):
        pass

    def set_timer_model(self, *args, **kwargs):
        pass

    def set_profile(self, *args, **kwargs):
        pass

    def get_profile(self, *args, **kwargs):
        pass

    def get_brand(self, *args, **kwargs):
        pass

    def set_brand(self, *args, **kwargs):
        pass

    def get_revision(self, *args, **kwargs):
        pass

    def set_revision(self, *args, **kwargs):
        pass

    def get_target(self, *args, **kwargs):
        pass

    def set_target(self, *args, **kwargs):
        pass

    def get_subtarget(self, *args, **kwargs):
        pass

    def set_subtarget(self, *args, **kwargs):
        pass

    def get_kernel_load_address(self, *args, **kwargs):
        pass

    def set_kernel_load_address(self, *args, **kwargs):
        pass

    def get_kernel_version(self, *args, **kwargs):
        pass

    def set_kernel_version(self, *args, **kwargs):
        pass

    def get_kernel_created_time(self, *args, **kwargs):
        pass

    def set_kernel_created_time(self, *args, **kwargs):
        pass

    def get_kernel_entry_point(self, *args, **kwargs):
        pass

    def set_kernel_entry_point(self, *args, **kwargs):
        pass

    def get_cpu_model(self, *args, **kwargs):
        pass

    def set_cpu_model(self, *args, **kwargs):
        pass

    def get_ram(self, *args, **kwargs):
        pass

    def set_ram(self, *args, **kwargs):
        pass

    def get_interrupt_controller(self, *args, **kwargs):
        pass

    def set_interrupt_controller(self, *args, **kwargs):
        pass

    def get_flash(self, *args, **kwargs):
        pass

    def set_flash(self, *args, **kwargs):
        pass

    def get_uart(self, *args, **kwargs):
        pass

    def get_architecture(self, *args, **kwargs):
        pass

    def set_architecture(self, *args, **kwargs):
        pass

    def __init__(self, *args, **kwargs):
        super(SimpleFirmware, self).__init__(*args, **kwargs)
