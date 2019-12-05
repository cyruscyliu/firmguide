"""
Device tree solution.
"""
from profile.firmware import Firmware
import os
import fdt


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

    def set_profile(self, *args, **kwargs):
        if len(args):
            profile = args[0]
        else:
            profile = None
        first = kwargs.pop('first', False)
        working_dir = kwargs.pop('working_dir', None)

        if profile is not None:
            self.profile = profile
            return
        if working_dir is None:
            raise ValueError('please assign the working directory if no profile available')
        path_to_profile = os.path.join(working_dir, 'profile.dt')
        if first:
            with open(path_to_profile, 'w') as f:
                f.write('/dts-v1/;\n\n/ {\n};\n')
        with open(path_to_profile, 'r') as f:
            profile = f.read()
        self.profile = fdt.parse_dts(profile)

    def save_profile(self, *args, **kwargs):
        working_dir = kwargs.pop('working_dir', None)
        path_to_profile = os.path.join(working_dir, 'profile.dt')
        with open(path_to_profile, 'w') as f:
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
        return self.get_node_property('/basics', 'board_id')

    def get_cpu_model(self, *args, **kwargs):
        pass

    def set_cpu_model(self, *args, **kwargs):
        pass

    def get_cpu_pp_mmio_base(self, *args, **kwargs):
        pass

    def get_ram_priority(self, *args, **kwargs):
        pass

    def get_ram_size(self, *args, **kwargs):
        pass

    def probe_bridge(self, *args, **kwargs):
        pass

    def get_bridge_name(self, *args, **kwargs):
        pass

    def get_bridge_mmio_base(self, *args, **kwargs):
        pass

    def get_bridge_mmio_size(self, *args, **kwargs):
        pass

    def get_bridge_registers(self, *args, **kwargs):
        pass

    def probe_interrupt_controller(self, *args, **kwargs):
        pass

    def get_interrupt_controller_name(self, *args, **kwargs):
        pass

    def get_interrupt_controller_registers(self, *args, **kwargs):
        pass

    def get_interrupt_controller_mmio_size(self, *args, **kwargs):
        pass

    def get_interrupt_controller_mmio_base(self, *args, **kwargs):
        pass

    def get_n_irqs(self, *args, **kwargs):
        pass

    def probe_timer(self, *args, **kwargs):
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

    def probe_uart(self, *args, **kwargs):
        pass

    def get_uart_name(self, *args, **kwargs):
        pass

    def set_uart_name(self, *args, **kwargs):
        pass

    def get_uart_mmio_base(self, *args, **kwargs):
        pass

    def set_uart_mmio_base(self, *args, **kwargs):
        pass

    def get_uart_baud_rate(self, *args, **kwargs):
        pass

    def set_uart_baud_rate(self, *args, **kwargs):
        pass

    def get_uart_reg_shift(self, *args, **kwargs):
        pass

    def set_uart_reg_shift(self, *args, **kwargs):
        pass

    def get_uart_irq(self, *args, **kwargs):
        pass

    def set_uart_irq(self, *args, **kwargs):
        pass

    def get_flash_base(self, *args, **kwargs):
        pass

    def set_flash_base(self, *args, **kwargs):
        pass

    def get_flash_type(self, *args, **kwargs):
        pass

    def set_flash_type(self, *args, **kwargs):
        pass

    def get_flash_size(self, *args, **kwargs):
        pass

    def set_flash_size(self, *args, **kwargs):
        pass

    def get_flash_section_size(self, *args, **kwargs):
        pass

    def set_flash_section_size(self, *args, **kwargs):
        pass

    def get_bamboo_devices(self, *args, **kwargs):
        pass

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
        self.set_node_property('/openwrt', 'url', url)

    def get_url(self, *args, **kwargs):
        return self.get_node_property('/openwrt', 'url')

    def set_homepage(self, *args, **kwargs):
        homepage = args[0]
        self.set_node_property('/openwrt', 'homepage', homepage)

    def get_homepage(self, *args, **kwargs):
        return self.get_node_property('/openwrt', 'homepage')

    def get_target(self, *args, **kwargs):
        return self.get_node_property('/openwrt', 'target')

    def set_target(self, *args, **kwargs):
        target = args[0]
        self.set_node_property('/openwrt', 'target', target)

    def get_subtarget(self, *args, **kwargs):
        return self.get_node_property('/openwrt', 'subtarget')

    def set_subtarget(self, *args, **kwargs):
        subtarget = args[0]
        self.set_node_property('/openwrt', 'subtarget', subtarget)

    def get_revision(self, *args, **kwargs):
        return self.get_node_property('/openwrt', 'revision')

    def set_revision(self, *args, **kwargs):
        revision = args[0]
        self.set_node_property('/openwrt', 'revision', revision)

    def set_toh(self, *args, **kwargs):
        toh = args[0]
        assert isinstance(toh, list)
        header = kwargs.pop('header', None)
        if header is None:
            return
        brand_node = self.profile.get_node('/openwrt/toh', create=True)
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
        brand_node = self.profile.get_node('/openwrt/toh')
        assert brand_node is not None
        for property_ in args:
            value = brand_node.get_property(property_)
            if value is None:
                toh.append(value)
            else:
                toh.append(value.data[0])
        return toh
