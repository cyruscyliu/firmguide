"""
Our ugly solution.
"""
import os
import yaml
import shutil

from profile.firmware import Firmware


class SimpleFirmware(Firmware):
    def set_uuid(self, *args, **kwargs):
        self.set_general('basics', 'uuid', *args)

    def get_name(self, *args, **kwargs):
        return self.get_general('basics', 'name')

    def set_name(self, *args, **kwargs):
        self.set_general('basics', 'name', *args)

    def get_path(self, *args, **kwargs):
        return self.get_general('basics', 'path')

    def set_path(self, *args, **kwargs):
        self.set_general('basics', 'path', *args)

    def set_architecture(self, *args, **kwargs):
        self.set_general('basics', 'architecture', *args)

    def get_architecture(self, *args, **kwargs):
        return self.get_general('basics', 'architecture')

    def get_endian(self, *args, **kwargs):
        return self.get_general('basics', 'endian')

    def set_endian(self, *args, **kwargs):
        self.set_general('basics', 'endian', *args)

    def get_brand(self, *args, **kwargs):
        return self.get_general('basics', 'brand')

    def set_brand(self, *args, **kwargs):
        self.set_general('basics', 'brand', *args)

    def set_general(self, l1, l2, *args):
        value = args[0]
        if l2 is not None:
            if l1 not in self.profile:
                self.profile[l1] = {}
            self.profile[l1][l2] = value
        else:
            self.profile[l1] = value

    def get_general(self, l1, l2):
        try:
            if l2 is not None:
                return self.profile[l1][l2]
            else:
                return self.profile[l1]
        except KeyError:
            return None

    def set_path_to_llvm_bitcode(self, *args, **kwargs):
        self.set_general('components', 'path_to_llvm_bitcode', *args)

    def get_path_to_llvm_bitcode(self, *args, **kwargs):
        return self.get_general('components', 'path_to_llvm_bitcode')

    def set_path_to_dot_config(self, *args, **kwargs):
        self.set_general('components', 'path_to_dot_config', *args)

    def get_path_to_dot_config(self, *args, **kwargs):
        return self.get_general('components', 'path_to_dot_config')

    def set_path_to_uimage(self, *args, **kwargs):
        self.set_general('components', 'path_to_uimage', *args)

    def get_path_to_uimage(self, *args, **kwargs):
        return self.get_general('components', 'path_to_uimage')

    def get_machine_description(self, *args, **kwargs):
        return self.get_general('basics', 'machine_description')

    def set_machine_description(self, *args, **kwargs):
        self.set_general('basics', 'machine_description', *args)

    def get_machine_name(self, *args, **kwargs):
        return self.get_general('basics', 'machine_name')

    def set_machine_name(self, *args, **kwargs):
        self.set_general('basics', 'machine_name', *args)

    def get_board_id(self, *args, **kwargs):
        return self.get_general('basics', 'board_id')

    def set_board_id(self, *args, **kwargs):
        self.set_general('basics', 'board_id', *args)

    def get_cpu_pp_name(self, *args, **kwargs):
        return self.get_general('cpu_pp', 'name')

    def set_cpu_pp_name(self, *args, **kwargs):
        self.set_general('cpu_pp', 'name', *args)

    def get_cpu_pp_mmio_base(self, *args, **kwargs):
        return self.get_general('cpu_pp', 'mmio_base')

    def set_cpu_pp_mmio_base(self, *args, **kwargs):
        self.set_general('cpu_pp', 'mmio_base', *args)

    def get_ram_priority(self, *args, **kwargs):
        return self.get_general('ram', 'priority')

    def set_ram_priority(self, *args, **kwargs):
        self.set_general('ram', 'priority', *args)

    def set_ram_base(self, *args, **kwargs):
        self.set_general('ram', 'base', *args)

    def get_ram_base(self, *args, **kwargs):
        return self.get_general('ram', 'base')

    def get_ram_size(self, *args, **kwargs):
        return self.get_general('ram', 'size')

    def set_ram_size(self, *args, **kwargs):
        self.set_general('ram', 'size', *args)

    def get_bridge_name(self, *args, **kwargs):
        return self.get_general('bridge', 'name')

    def set_bridge_name(self, *args, **kwargs):
        self.set_general('bridge', 'name', *args)

    def get_bridge_mmio_base(self, *args, **kwargs):
        return self.get_general('bridge', 'mmio_base')

    def set_bridge_mmio_base(self, *args, **kwargs):
        self.set_general('bridge', 'mmio_base', *args)

    def get_bridge_mmio_size(self, *args, **kwargs):
        return self.get_general('bridge', 'mmio_size')

    def set_bridge_mmio_size(self, *args, **kwargs):
        self.set_general('bridge', 'mmio_size', *args)

    def get_bridge_registers(self, *args, **kwargs):
        return self.get_general('bridge', 'registers')

    def get_interrupt_controller_name(self, *args, **kwargs):
        return self.get_general('interrupt_controller', 'name')

    def set_interrupt_controller_name(self, *args, **kwargs):
        self.set_general('interrupt_controller', 'name', *args)

    def get_interrupt_controller_registers(self, *args, **kwargs):
        return self.get_general('interrupt_controller', 'registers')

    def set_interrupt_controller_registers(self, *args, **kwargs):
        self.set_general('interrupt_controller', 'registers', *args)

    def get_interrupt_controller_mmio_size(self, *args, **kwargs):
        return self.get_general('interrupt_controller', 'mmio_size')

    def set_interrupt_controller_mmio_size(self, *args, **kwargs):
        self.set_general('interrupt_controller', 'mmio_size', *args)

    def get_interrupt_controller_mmio_base(self, *args, **kwargs):
        return self.get_general('interrupt_controller', 'mmio_base')

    def set_interrupt_controller_mmio_base(self, *args, **kwargs):
        self.set_general('interrupt_controller', 'mmio_base', *args)

    def get_n_irqs(self, *args, **kwargs):
        return self.get_general('interrupt_controller', 'n_irqs')

    def set_n_irqs(self, *args, **kwargs):
        self.set_general('interrupt_controller', 'n_irqs', *args)

    def get_timer_name(self, *args, **kwargs):
        return self.get_general('timer', 'name')

    def set_timer_name(self, *args, **kwargs):
        self.set_general('timer', 'name', *args)

    def get_timer_registers(self, *args, **kwargs):
        return self.get_general('timer', 'registers')

    def set_timer_register(self, *args, **kwargs):
        pass

    def get_timer_mmio_size(self, *args, **kwargs):
        return self.get_general('timer', 'mmio_size')

    def set_timer_mmio_size(self, *args, **kwargs):
        self.set_general('timer', 'mmio_size', *args)

    def get_timer_mmio_base(self, *args, **kwargs):
        return self.get_general('timer', 'mmio_base')

    def set_timer_mmio_base(self, *args, **kwargs):
        self.set_general('timer', 'mmio_base', *args)

    def get_uart_name(self, *args, **kwargs):
        return self.get_general('uart', 'name')

    def set_uart_name(self, *args, **kwargs):
        self.set_general('uart', 'name', *args)

    def get_uart_mmio_base(self, *args, **kwargs):
        return self.get_general('uart', 'mmio_base')

    def set_uart_mmio_base(self, *args, **kwargs):
        self.set_general('uart', 'mmio_base', *args)

    def get_uart_baud_rate(self, *args, **kwargs):
        return self.get_general('uart', 'baud_rate')

    def set_uart_baud_rate(self, *args, **kwargs):
        self.set_general('uart', 'baud_rate', *args)

    def get_uart_reg_shift(self, *args, **kwargs):
        return self.get_general('uart', 'reg_shift')

    def set_uart_reg_shift(self, *args, **kwargs):
        self.set_general('uart', 'reg_shift', *args)

    def get_uart_irq(self, *args, **kwargs):
        return self.get_general('uart', 'irq')

    def set_uart_irq(self, *args, **kwargs):
        self.set_general('uart', 'irq', *args)

    def get_flash_base(self, *args, **kwargs):
        return self.get_general('flash', 'base')

    def set_flash_base(self, *args, **kwargs):
        self.set_general('flash', 'base', *args)

    def get_flash_section_size(self, *args, **kwargs):
        return self.get_general('flash', 'section_size')

    def set_flash_section_size(self, *args, **kwargs):
        self.set_general('flash', 'section_size', *args)
        pass

    def get_bamboo_devices(self, *args, **kwargs):
        return self.get_general('bamboo', None)

    def probe_bridge(self):
        return 'bridge' in self.profile

    def set_url(self, *args, **kwargs):
        self.set_general('brand', 'url', *args)

    def get_url(self, *args, **kwargs):
        return self.get_general('brand', 'url')

    def set_format(self, *args, **kwargs):
        self.set_general('components', 'format', *args)

    def get_format(self, *args, **kwargs):
        return self.get_general('components', 'format')

    def set_homepage(self, *args, **kwargs):
        self.set_general('brand', 'homepage', *args)

    def get_homepage(self, *args, **kwargs):
        return self.get_general('brand', 'homepage')

    def set_description(self, *args, **kwargs):
        self.set_general('basics', 'description', *args)

    def get_description(self, *args, **kwargs):
        return self.get_general('basics', 'description')

    def set_path_to_image(self, *args, **kwargs):
        self.set_general('components', 'path_to_image', *args)

    def get_path_to_image(self, *args, **kwargs):
        return self.get_general('components', 'path_to_image')

    def set_path_to_kernel(self, *args, **kwargs):
        self.set_general('components', 'path_to_kernel', *args)

    def get_path_to_kernel(self, *args, **kwargs):
        return self.get_description('components', 'path_to_kernel')

    def set_path_to_dtb(self, *args, **kwargs):
        self.set_general('components', 'path_to_dtb', *args)

    def get_path_to_dtb(self, *args, **kwargs):
        return self.get_general('components', 'path_to_dtb')

    def set_toh(self, *args, **kwargs):
        pass

    def get_toh(self, *args, **kwargs):
        pass

    def save_profile(self, *args, **kwargs):
        with open(self.path_to_profile, 'w') as f:
            yaml.safe_dump(self.profile, f)

    def get_dts(self, *args, **kwargs):
        pass

    def set_dts(self, *args, **kwargs):
        pass

    def get_flash_size(self, *args, **kwargs):
        return self.get_general('flash', 'size')

    def set_flash_size(self, *args, **kwargs):
        self.set_general('flash', 'size', *args)

    def set_flash_type(self, *args, **kwargs):
        self.set_general('flash', 'type', *args)

    def get_flash_type(self, *args, **kwargs):
        return self.get_general('flash', 'type')

    def copy_profile(self, *args, **kwargs):
        path_to_profile = args[0]
        shutil.copy(path_to_profile, os.path.join(self.working_directory, 'profile.yaml'))

    def create_empty_profile(self):
        with open(self.path_to_profile, 'w') as f:
            yaml.safe_dump({}, f)

    def load_from_profile(self):
        with open(self.path_to_profile, 'r') as f:
            profile = yaml.safe_load(f)
        self.profile = profile

    def get_profile(self, *args, **kwargs):
        return self.get_profile()

    def get_revision(self, *args, **kwargs):
        return self.get_general('brand', 'revision')

    def set_revision(self, *args, **kwargs):
        self.set_general('brand', 'revision', *args)

    def get_target(self, *args, **kwargs):
        return self.get_general('brand', 'target')

    def set_target(self, *args, **kwargs):
        self.set_general('brand', 'target', *args)

    def get_subtarget(self, *args, **kwargs):
        return self.get_general('brand', 'subtarget')

    def set_subtarget(self, *args, **kwargs):
        self.set_general('brand', 'subtarget', *args)

    def get_kernel_load_address(self, *args, **kwargs):
        return self.get_general('kernel', 'kernel_load_address')

    def set_kernel_load_address(self, *args, **kwargs):
        self.set_general('kernel', 'kernel_load_address', *args)

    def get_kernel_version(self, *args, **kwargs):
        return self.get_general('kernel', 'kernel_version')

    def set_kernel_version(self, *args, **kwargs):
        self.set_general('kernel', 'kernel_version', *args)

    def get_kernel_created_time(self, *args, **kwargs):
        return self.get_general('kernel', 'kernel_created_time')

    def set_kernel_created_time(self, *args, **kwargs):
        self.set_general('kernel', 'kernel_created_time', *args)

    def get_kernel_entry_point(self, *args, **kwargs):
        return self.get_general('kernel', 'kernel_entry_point')

    def set_kernel_entry_point(self, *args, **kwargs):
        self.set_general('kernel', 'kernel_entry_point', *args)

    def get_cpu_model(self, *args, **kwargs):
        return self.get_general('cpu', 'model')

    def set_cpu_model(self, *args, **kwargs):
        self.set_general('cpu', 'model', *args)

    def __init__(self, *args, **kwargs):
        super(SimpleFirmware, self).__init__(*args, **kwargs)
