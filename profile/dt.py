"""
Device tree solution.
"""
import shutil
import os
import fdt

from profile.firmware import Firmware


class DTFirmware(Firmware):
    """
    nodes: basics, components, openwrt, kernel, cpus, memory, flash
    """

    def set_node_property(self, path_to_node, property_, *values):
        for value in values:
            if value is None:
                return
        node = self.profile.get_node(path_to_node, create=True)
        if node.exist_property(property_):
            node.remove_property(property_)
        node.append(fdt.PropStrings(property_, *values))

    def get_node_property(self, path_to_node, property_, end=1):
        if not self.profile.exist_node(path_to_node):
            return
        node = self.profile.get_node(path_to_node)
        if not node.exist_property(property_):
            return
        value = node.get_property(property_)
        if value is None:
            return
        else:
            if end == 1:
                return value.data[0]
            else:
                return value.data[0: end]

    def copy_profile(self, *args, **kwargs):
        path_to_profile = args[0]
        shutil.copy(path_to_profile, os.path.join(self.working_directory, 'profile.dt'))

    def create_empty_profile(self):
        with open(self.path_to_profile, 'w') as f:
            f.write('/dts-v1/;\n\n/ {\n};\n')

    def load_from_profile(self):
        with open(self.path_to_profile, 'r') as f:
            profile = f.read()
        self.profile = fdt.parse_dts(profile)

    def save_profile(self, *args, **kwargs):
        with open(self.path_to_profile, 'w') as f:
            f.write(self.profile.to_dts())

    def get_dts(self, *args, **kwargs):
        return self.get_profile()

    def set_dts(self, *args, **kwargs):
        dt = args[0]
        self.profile.merge(dt)

    def set_format(self, *args, **kwargs):
        format_ = args[0]
        self.set_node_property('/components', 'format', format_)

    def get_format(self, *args, **kwargs):
        return self.get_node_property('/components', 'format')

    def set_path_to_llvm_bitcode(self, *args, **kwargs):
        path_to_llvm_bitcode = args[0]
        self.set_node_property('/components', 'path_to_llvm_bitcode', path_to_llvm_bitcode)

    def get_path_to_llvm_bitcode(self, *args, **kwargs):
        return self.get_node_property('/components', 'path_to_llvm_bitcode')

    def set_path_to_dot_config(self, *args, **kwargs):
        path_to_dot_image = args[0]
        self.set_node_property('/components', 'path_to_dot_config', path_to_dot_image)

    def get_path_to_dot_config(self, *args, **kwargs):
        return self.get_node_property('/components', 'path_to_dot_config')

    def set_path_to_image(self, *args, **kwargs):
        path_to_image = args[0]
        self.set_node_property('/components', 'path_to_image', path_to_image)

    def get_path_to_image(self, *args, **kwargs):
        return self.get_node_property('/components', 'path_to_image')

    def get_path_to_uimage(self, *args, **kwargs):
        return self.get_node_property('/components', 'path_to_uimage')

    def set_path_to_uimage(self, *args, **kwargs):
        path_to_uimage = args[0]
        self.set_node_property('/components', 'path_to_uimage', path_to_uimage)

    def set_path_to_kernel(self, *args, **kwargs):
        path_to_kernel = args[0]
        self.set_node_property('/components', 'path_to_kernel', path_to_kernel)

    def get_path_to_kernel(self, *args, **kwargs):
        return self.get_node_property('/components', 'path_to_kernel')

    def set_path_to_dtb(self, *args, **kwargs):
        path_to_dtb = args[0]
        self.set_node_property('/components', 'path_to_dtb', path_to_dtb)

    def get_path_to_dtb(self, *args, **kwargs):
        return self.get_node_property('/components', 'path_to_dtb')

    def set_machine_description(self, *args, **kwargs):
        description = args[0]
        self.set_node_property('/basics', 'description', description)

    def get_machine_description(self, *args, **kwargs):
        return self.get_node_property('/basics', 'description')

    def set_machine_name(self, *args, **kwargs):
        machine_name = args[0]
        return self.set_node_property('/basics', 'machine_name', machine_name)

    def get_machine_name(self, *args, **kwargs):
        return self.get_node_property('/basics', 'machine_name')

    def set_board_id(self, *args, **kwargs):
        board_id = args[0]
        return self.set_node_property('/basics', 'board_id', board_id)

    def get_board_id(self, *args, **kwargs):
        # return self.get_node_property('/basics', 'board_id')
        return "0x661"

    def get_cpu_model(self, *args, **kwargs):
        return self.get_node_property('cpu', 'model')

    def set_cpu_model(self, *args, **kwargs):
        cpu_model = args[0]
        self.set_node_property('cpu', 'model', cpu_model)

    def set_cpu_pp_name(self, *args, **kwargs):
        cpu_pp_name = args[0]
        self.set_node_property('cpu_pp', 'name', cpu_pp_name)

    def get_cpu_pp_name(self, *args, **kwargs):
        return self.get_node_property('cpu_pp', 'name')

    def get_cpu_pp_mmio_base(self, *args, **kwargs):
        return self.get_node_property('cpu_pp', 'mmio_base')

    def set_cpu_pp_mmio_base(self, *args, **kwargs):
        cpu_pp_mmio_base = args[0]
        self.set_node_property('cpu_pp', 'mmio_base', cpu_pp_mmio_base)

    def get_ram_priority(self, *args, **kwargs):
        return '0'

    def get_ram_size(self, *args, **kwargs):
        return self.get_node_property('ram', 'size')

    def set_ram_size(self, *args, **kwargs):
        ram_size = args[0]
        self.set_node_property('ram', 'size', ram_size)

    def get_ram_base(self, *args, **kwargs):
        return self.get_node_property('ram', 'base')

    def set_ram_base(self, *args, **kwargs):
        ram_base = args[0]
        self.set_node_property('ram', 'base', ram_base)

    def get_bridge_name(self, *args, **kwargs):
        pass

    def get_bridge_mmio_base(self, *args, **kwargs):
        pass

    def get_bridge_mmio_size(self, *args, **kwargs):
        pass

    def get_bridge_registers(self, *args, **kwargs):
        pass

    def get_interrupt_controller_name(self, *args, **kwargs):
        return self.get_node_property('interrupt_controller', 'name')

    def set_interrupt_controller_name(self, *args, **kwargs):
        ic_name = args[0]
        self.set_node_property('interrupt_controller', 'name', ic_name)

    def get_interrupt_controller_registers(self, *args, **kwargs):
        pass

    def get_interrupt_controller_mmio_size(self, *args, **kwargs):
        return self.get_node_property('interrupt_controller', 'mmio_size', *args)

    def set_interrupt_controller_mmio_size(self, *args, **kwargs):
        self.set_node_property('interrupt_controller', 'mmio_size', *args)

    def get_interrupt_controller_mmio_base(self, *args, **kwargs):
        return self.get_node_property('interrupt_controller', 'mmio_base')

    def set_interrupt_controller_mmio_base(self, *args, **kwargs):
        self.set_node_property('interrupt_controller', 'mmio_base', *args)

    def get_n_irqs(self, *args, **kwargs):
        pass

    def get_timer_name(self, *args, **kwargs):
        pass

    def set_timer_name(self, *args, **kwargs):
        pass

    def get_timer_registers(self, *args, **kwargs):
        pass

    def set_timer_register(self, *args, **kwargs):
        pass

    def get_timer_mmio_size(self, *args, **kwargs):
        pass

    def set_timer_mmio_size(self, *args, **kwargs):
        pass

    def get_timer_mmio_base(self, *args, **kwargs):
        pass

    def set_timer_mmio_base(self, *args, **kwargs):
        pass

    def get_uart_name(self, *args, **kwargs):
        return self.get_node_property('/uart', 'name')

    def set_uart_name(self, *args, **kwargs):
        uart_name = args[0]
        self.set_node_property('/uart', 'name', uart_name)

    def get_uart_mmio_base(self, *args, **kwargs):
        return self.get_node_property('/uart', 'mmio_base')

    def set_uart_mmio_base(self, *args, **kwargs):
        uart_mmio_base = args[0]
        self.set_node_property('/uart', 'mmio_base', uart_mmio_base)

    def get_uart_baud_rate(self, *args, **kwargs):
        return self.get_node_property('/uart', 'baud_rate')

    def set_uart_baud_rate(self, *args, **kwargs):
        uart_baud_rate = args[0]
        self.set_node_property('/uart', 'baud_rate', uart_baud_rate)

    def get_uart_reg_shift(self, *args, **kwargs):
        return self.get_node_property('/uart', 'reg_shift')

    def set_uart_reg_shift(self, *args, **kwargs):
        uart_reg_shift = args[0]
        self.set_node_property('/uart', 'reg_shift', uart_reg_shift)

    def get_uart_irq(self, *args, **kwargs):
        return self.get_node_property('/uart', 'irq')

    def set_uart_irq(self, *args, **kwargs):
        uart_irq = args[0]
        self.set_node_property('/uart', 'irq', uart_irq)

    def get_flash_base(self, *args, **kwargs):
        self.get_node_property('/flash', 'base')

    def set_flash_base(self, *args, **kwargs):
        flash_base = args[0]
        self.set_node_property('/flash', 'base', flash_base)

    def set_flash_type(self, *args, **kwargs):
        flash_type = args[0]
        self.set_node_property('/flash', 'type', flash_type)

    def get_flash_type(self, *args, **kwargs):
        return self.get_node_property('/flash', 'type')

    def get_flash_size(self, *args, **kwargs):
        return self.get_node_property('/flash', 'size')

    def set_flash_size(self, *args, **kwargs):
        flash_size = args[0]
        return self.set_node_property('/flash', 'size', flash_size)

    def get_flash_section_size(self, *args, **kwargs):
        return self.get_node_property('/flash', 'section_size')

    def set_flash_section_size(self, *args, **kwargs):
        flash_section_size = args[0]
        return self.set_node_property('/flash', 'section_size', flash_section_size)

    def get_bamboo_devices(self, *args, **kwargs):
        return []

    def get_kernel_load_address(self, *args, **kwargs):
        return self.get_node_property('kernel', 'kernel_load_address')

    def set_kernel_load_address(self, *args, **kwargs):
        kernel_load_address = args[0]
        self.set_node_property('/kernel', 'kernel_load_address', kernel_load_address)

    def get_kernel_version(self, *args, **kwargs):
        return self.get_node_property('/kernel', 'kernel_version')

    def set_kernel_version(self, *args, **kwargs):
        kernel_version = args[0]
        self.set_node_property('/kernel', 'kernel_version', kernel_version)

    def get_kernel_created_time(self, *args, **kwargs):
        return self.get_node_property('/kernel', 'kernel_created_time')

    def set_kernel_created_time(self, *args, **kwargs):
        kernel_created_time = args[0]
        self.set_node_property('/kernel', 'kernel_created_time', kernel_created_time)

    def get_kernel_entry_point(self, *args, **kwargs):
        return self.get_node_property('/kernel', 'kernel_entry_point')

    def set_kernel_entry_point(self, *args, **kwargs):
        kernel_entry_point = args[0]
        self.set_node_property('/kernel', 'kernel_entry_point', kernel_entry_point)

    def set_url(self, *args, **kwargs):
        url = args[0]
        self.set_node_property('/brand', 'url', url)

    def get_url(self, *args, **kwargs):
        return self.get_node_property('/brand', 'url')

    def set_homepage(self, *args, **kwargs):
        homepage = args[0]
        self.set_node_property('/brand', 'homepage', homepage)

    def get_homepage(self, *args, **kwargs):
        return self.get_node_property('/brand', 'homepage')

    def get_target(self, *args, **kwargs):
        return self.get_node_property('/brand', 'target')

    def set_target(self, *args, **kwargs):
        target = args[0]
        self.set_node_property('/brand', 'target', target)

    def get_subtarget(self, *args, **kwargs):
        return self.get_node_property('/brand', 'subtarget')

    def set_subtarget(self, *args, **kwargs):
        subtarget = args[0]
        self.set_node_property('/brand', 'subtarget', subtarget)

    def get_revision(self, *args, **kwargs):
        return self.get_node_property('/brand', 'revision')

    def set_revision(self, *args, **kwargs):
        revision = args[0]
        self.set_node_property('/brand', 'revision', revision)

    def set_toh(self, *args, **kwargs):
        toh = args[0]
        assert isinstance(toh, list)
        header = kwargs.pop('header', None)
        if header is None:
            return
        brand_node = self.profile.get_node('/brand/toh', create=True)
        for k, v in zip(header, toh):
            if brand_node.exist_property(k):
                brand_node.remove_property(k)
            if not len(v):
                continue
            brand_node.append(fdt.PropStrings(k, v))

    def get_toh(self, *args, **kwargs):
        if not len(args):
            return None
        toh = []
        brand_node = self.profile.get_node('/brand/toh')
        assert brand_node is not None
        for property_ in args:
            value = brand_node.get_property(property_)
            if value is None:
                toh.append(value)
            else:
                toh.append(value.data[0])
        return toh
