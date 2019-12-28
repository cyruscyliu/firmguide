"""
Our ugly solution.
"""
import os
import yaml
import shutil

from profile.firmware import Firmware


class SimpleFirmware(Firmware):
    def load_uuid(self, *args, **kwargs):
        return self.get_general('basics', 'uuid')

    def set_uuid(self, *args, **kwargs):
        self.set_general('basics', 'uuid', value=args[0])

    def get_name(self, *args, **kwargs):
        return self.get_general('basics', 'name')

    def set_name(self, *args, **kwargs):
        self.set_general('basics', 'name', value=args[0])

    def get_path(self, *args, **kwargs):
        return self.get_general('basics', 'path')

    def set_path(self, *args, **kwargs):
        self.set_general('basics', 'path', value=args[0])

    def set_architecture(self, *args, **kwargs):
        self.set_general('basics', 'architecture', value=args[0])

    def get_architecture(self, *args, **kwargs):
        return self.get_general('basics', 'architecture')

    def get_endian(self, *args, **kwargs):
        return self.get_general('basics', 'endian')

    def set_endian(self, *args, **kwargs):
        self.set_general('basics', 'endian', value=args[0])

    def get_brand(self, *args, **kwargs):
        return self.get_general('basics', 'brand')

    def set_brand(self, *args, **kwargs):
        self.set_general('basics', 'brand', value=args[0])

    def set_general(self, *levels, value=None):
        # for loop not recursion
        profile = self.profile
        for level in levels[:-1]:
            if level not in profile:
                profile[level] = {}
            profile = profile[level]
        profile[levels[-1]] = value

    def get_general(self, *levels):
        # for loop not recursion
        profile = self.profile
        for level in levels:
            if level in profile:
                profile = profile[level]
            else:
                profile = None
                break
        return profile

    def set_path_to_vmlinux(self, *args, **kwargs):
        self.set_general('components', 'path_to_vmlinux', value=args[0])

    def get_path_to_vmlinux(self, *args, **kwargs):
        return self.get_general('components', 'path_to_vmlinux')

    def set_path_to_source_code(self, *args, **kwargs):
        self.set_general('components', 'path_to_source_code', value=args[0])

    def get_path_to_source_code(self, *args, **kwargs):
        return self.get_general('components', 'path_to_source_code')

    def set_path_to_llvm_bitcode(self, *args, **kwargs):
        self.set_general('components', 'path_to_llvm_bitcode', value=args[0])

    def get_path_to_llvm_bitcode(self, *args, **kwargs):
        return self.get_general('components', 'path_to_llvm_bitcode')

    def set_path_to_dot_config(self, *args, **kwargs):
        self.set_general('components', 'path_to_dot_config', value=args[0])

    def get_path_to_dot_config(self, *args, **kwargs):
        return self.get_general('components', 'path_to_dot_config')

    def set_path_to_uimage(self, *args, **kwargs):
        self.set_general('components', 'path_to_uimage', value=args[0])

    def get_path_to_uimage(self, *args, **kwargs):
        return self.get_general('components', 'path_to_uimage')

    def get_machine_description(self, *args, **kwargs):
        return self.get_general('basics', 'machine_description')

    def set_machine_description(self, *args, **kwargs):
        self.set_general('basics', 'machine_description', value=args[0])

    def get_machine_name(self, *args, **kwargs):
        return self.get_general('basics', 'machine_name')

    def set_machine_name(self, *args, **kwargs):
        self.set_general('basics', 'machine_name', value=args[0])

    def get_board_id(self, *args, **kwargs):
        return self.get_general('basics', 'board_id')

    def set_board_id(self, *args, **kwargs):
        self.set_general('basics', 'board_id', value=args[0])

    def get_cpu_pp_name(self, *args, **kwargs):
        return self.get_general('cpu_pp', 'name')

    def set_cpu_pp_name(self, *args, **kwargs):
        self.set_general('cpu_pp', 'name', value=args[0])

    def get_cpu_pp_mmio_base(self, *args, **kwargs):
        return self.get_general('cpu_pp', 'mmio_base')

    def set_cpu_pp_mmio_base(self, *args, **kwargs):
        self.set_general('cpu_pp', 'mmio_base', value=args[0])

    def get_ram_priority(self, *args, **kwargs):
        return self.get_general('ram', 'priority')

    def set_ram_priority(self, *args, **kwargs):
        self.set_general('ram', 'priority', value=args[0])

    def set_ram_base(self, *args, **kwargs):
        self.set_general('ram', 'base', value=args[0])

    def get_ram_base(self, *args, **kwargs):
        return self.get_general('ram', 'base')

    def get_ram_size(self, *args, **kwargs):
        return self.get_general('ram', 'size')

    def set_ram_size(self, *args, **kwargs):
        self.set_general('ram', 'size', value=args[0])

    def get_interrupt_controller_name(self, *args, **kwargs):
        return self.get_general('interrupt_controller', 'name')

    def set_interrupt_controller_name(self, *args, **kwargs):
        self.set_general('interrupt_controller', 'name', value=args[0])

    def get_interrupt_controller_registers(self, *args, **kwargs):
        return self.get_general('interrupt_controller', 'registers')

    def set_interrupt_controller_registers(self, *args, **kwargs):
        # args: name, address, value
        self.set_general('interrupt_controller', 'registers', args[0], 'offset', value=args[0])
        self.set_general('interrupt_controller', 'registers', args[0], 'value', value=args[0])

    def get_interrupt_controller_mmio_size(self, *args, **kwargs):
        return self.get_general('interrupt_controller', 'mmio_size')

    def set_interrupt_controller_mmio_size(self, *args, **kwargs):
        self.set_general('interrupt_controller', 'mmio_size', value=args[0])

    def get_interrupt_controller_mmio_base(self, *args, **kwargs):
        return self.get_general('interrupt_controller', 'mmio_base')

    def set_interrupt_controller_mmio_base(self, *args, **kwargs):
        self.set_general('interrupt_controller', 'mmio_base', value=args[0])

    def set_timer_irq(self, *args, **kwargs):
        self.set_general('interrupt_controller', 'timer_irq', value=args[0])

    def get_timer_irq(self, *args, **kwargs):
        return self.get_general('interrupt_controller', 'timer_irq')

    def get_timer_name(self, *args, **kwargs):
        return self.get_general('timer', 'name')

    def set_timer_name(self, *args, **kwargs):
        self.set_general('timer', 'name', value=args[0])

    def get_timer_registers(self, *args, **kwargs):
        return self.get_general('timer', 'registers')

    def set_timer_register(self, *args, **kwargs):
        pass

    def get_timer_mmio_size(self, *args, **kwargs):
        return self.get_general('timer', 'mmio_size')

    def set_timer_mmio_size(self, *args, **kwargs):
        self.set_general('timer', 'mmio_size', value=args[0])

    def get_timer_mmio_base(self, *args, **kwargs):
        return self.get_general('timer', 'mmio_base')

    def set_timer_mmio_base(self, *args, **kwargs):
        self.set_general('timer', 'mmio_base', value=args[0])

    def set_uart_num(self, *args, **kwargs):
        self.set_general('uart', 'num', value=args[0])

    def get_uart_num(self, *args, **kwargs):
        return self.get_general('uart', 'num')

    def get_uart_name(self, *args, **kwargs):
        uart_index = args[0]
        return self.get_general('uart', 'uart@{}'.format(uart_index), 'name')

    def set_uart_name(self, *args, **kwargs):
        uart_index = args[1]
        self.set_general('uart', 'uart@{}'.format(uart_index), 'name', value=args[0])

    def get_uart_mmio_size(self, *args, **kwargs):
        uart_index = args[0]
        return self.get_general('uart', 'uart@{}'.format(uart_index), 'mmio_size')

    def set_uart_mmio_size(self, *args, **kwargs):
        uart_index = args[1]
        self.set_general('uart', 'uart@{}'.format(uart_index), 'mmio_size', value=args[0])

    def get_uart_mmio_base(self, *args, **kwargs):
        uart_index = args[0]
        return self.get_general('uart', 'uart@{}'.format(uart_index), 'mmio_base')

    def set_uart_mmio_base(self, *args, **kwargs):
        uart_index = args[1]
        self.set_general('uart', 'uart@{}'.format(uart_index), 'mmio_base', value=args[0])

    def get_uart_baud_rate(self, *args, **kwargs):
        uart_index = args[0]
        return self.get_general('uart', 'uart@{}'.format(uart_index), 'baud_rate')

    def set_uart_baud_rate(self, *args, **kwargs):
        uart_index = args[1]
        self.set_general('uart', 'uart@{}'.format(uart_index), 'baud_rate', value=args[0])

    def get_uart_reg_shift(self, *args, **kwargs):
        uart_index = args[0]
        return self.get_general('uart', 'uart@{}'.format(uart_index), 'reg_shift')

    def set_uart_reg_shift(self, *args, **kwargs):
        uart_index = args[1]
        self.set_general('uart', 'uart@{}'.format(uart_index), 'reg_shift', value=args[0])

    def get_uart_irq(self, *args, **kwargs):
        uart_index = args[0]
        return self.get_general('uart', 'uart@{}'.format(uart_index), 'irq')

    def set_uart_irq(self, *args, **kwargs):
        uart_index = args[1]
        self.set_general('uart', 'uart@{}'.format(uart_index), 'irq', value=args[0])

    def get_flash_base(self, *args, **kwargs):
        return self.get_general('flash', 'base')

    def set_flash_base(self, *args, **kwargs):
        self.set_general('flash', 'base', value=args[0])

    def get_flash_section_size(self, *args, **kwargs):
        return self.get_general('flash', 'section_size')

    def set_flash_section_size(self, *args, **kwargs):
        self.set_general('flash', 'section_size', value=args[0])
        pass

    def get_bamboo_devices(self, *args, **kwargs):
        bamboo = self.get_general('bamboo', None)
        if bamboo is None:
            return []
        else:
            return bamboo

    def probe_bridge(self):
        return 'bridge' in self.profile

    def set_url(self, *args, **kwargs):
        self.set_general('brand', 'url', value=args[0])

    def get_url(self, *args, **kwargs):
        return self.get_general('brand', 'url')

    def set_format(self, *args, **kwargs):
        self.set_general('components', 'format', value=args[0])

    def get_format(self, *args, **kwargs):
        return self.get_general('components', 'format')

    def set_homepage(self, *args, **kwargs):
        self.set_general('brand', 'homepage', value=args[0])

    def get_homepage(self, *args, **kwargs):
        return self.get_general('brand', 'homepage')

    def set_description(self, *args, **kwargs):
        self.set_general('basics', 'description', value=args[0])

    def get_description(self, *args, **kwargs):
        return self.get_general('basics', 'description')

    def set_path_to_image(self, *args, **kwargs):
        self.set_general('components', 'path_to_image', value=args[0])

    def get_path_to_image(self, *args, **kwargs):
        return self.get_general('components', 'path_to_image')

    def set_path_to_kernel(self, *args, **kwargs):
        self.set_general('components', 'path_to_kernel', value=args[0])

    def get_path_to_kernel(self, *args, **kwargs):
        return self.get_general('components', 'path_to_kernel')

    def set_path_to_dtb(self, *args, **kwargs):
        self.set_general('components', 'path_to_dtb', value=args[0])

    def get_path_to_dtb(self, *args, **kwargs):
        return self.get_general('components', 'path_to_dtb')

    def set_toh(self, *args, **kwargs):
        toh = args[0]
        assert isinstance(toh, list)
        header = kwargs.pop('header', None)
        if header is None:
            return
        for k, v in zip(header, toh):
            self.set_general('brand', 'toh', k, value=v)

    def get_toh(self, *args, **kwargs):
        toh = []
        for arg in args:
            toh.append(self.get_general('brand', 'toh', arg))
        return toh

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
        self.set_general('flash', 'size', value=args[0])

    def set_flash_type(self, *args, **kwargs):
        self.set_general('flash', 'type', value=args[0])

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
        self.set_general('brand', 'revision', value=args[0])

    def get_target(self, *args, **kwargs):
        return self.get_general('brand', 'target')

    def set_target(self, *args, **kwargs):
        self.set_general('brand', 'target', value=args[0])

    def get_subtarget(self, *args, **kwargs):
        return self.get_general('brand', 'subtarget')

    def set_subtarget(self, *args, **kwargs):
        self.set_general('brand', 'subtarget', value=args[0])

    def get_kernel_load_address(self, *args, **kwargs):
        return self.get_general('kernel', 'kernel_load_address')

    def set_kernel_load_address(self, *args, **kwargs):
        self.set_general('kernel', 'kernel_load_address', value=args[0])

    def get_kernel_version(self, *args, **kwargs):
        return self.get_general('kernel', 'kernel_version')

    def set_kernel_version(self, *args, **kwargs):
        self.set_general('kernel', 'kernel_version', value=args[0])

    def get_kernel_created_time(self, *args, **kwargs):
        return self.get_general('kernel', 'kernel_created_time')

    def set_kernel_created_time(self, *args, **kwargs):
        self.set_general('kernel', 'kernel_created_time', value=args[0])

    def get_kernel_entry_point(self, *args, **kwargs):
        return self.get_general('kernel', 'kernel_entry_point')

    def set_kernel_entry_point(self, *args, **kwargs):
        self.set_general('kernel', 'kernel_entry_point', value=args[0])

    def get_cpu_model(self, *args, **kwargs):
        return self.get_general('cpu', 'model')

    def set_cpu_model(self, *args, **kwargs):
        self.set_general('cpu', 'model', value=args[0])

    def __init__(self, *args, **kwargs):
        super(SimpleFirmware, self).__init__(*args, **kwargs)
