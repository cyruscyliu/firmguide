"""
Device tree solution.
"""
from generation.generatori import CodeGenerationInterface
from profile.firmware import Firmware
import os
import fdt


class DTFirmware(Firmware, CodeGenerationInterface):
    def probe_flash(self):
        return False

    def probe_uart(self):
        return False

    def probe_timer(self):
        return False

    def probe_interrupt_controller(self):
        return False

    def probe_bridge(self):
        return False

    def sget_bridge_name(self):
        pass

    def sget_bridge_mmio_base(self):
        pass

    def sget_bridge_mmio_size(self):
        pass

    def lget_bridge_registers(self):
        pass

    def sget_ram_priority(self):
        return '0'

    def sget_interrupt_controller_name(self):
        pass

    def lget_interrupt_controller_registers(self):
        pass

    def sget_interrupt_controller_mmio_size(self):
        pass

    def sget_interrupt_controller_mmio_base(self):
        pass

    def sget_n_irqs(self):
        pass

    def sget_timer_name(self):
        pass

    def lget_timer_registers(self):
        pass

    def sget_timer_mmio_size(self):
        pass

    def sget_timer_mmio_base(self):
        pass

    def sget_flash_base(self):
        pass

    def sget_machine_description(self):
        return self.get_node_property('/basics', 'description')

    def sget_machine_name(self):
        return self.get_node_property('/brand', 'model')

    def sget_architecture(self):
        return self.get_node_property('/basics', 'architecture')

    def sget_ram_size(self):
        _, ram_size = self.get_ram()
        return '{} MiB'.format(ram_size)

    def sget_cpu_model(self):
        # TODO solve this
        return 'arm926'

    def probe_cpu_pp_model(self):
        return False

    def sget_cpu_pp_mmio_base(self):
        pass

    def sget_uart_mmio_base(self):
        pass

    def sget_uart_baud_rate(self):
        pass

    def sget_uart_reg_shift(self):
        pass

    def sget_uart_irq(self):
        pass

    def lget_bamboo_devices(self):
        return []

    def sget_board_id(self):
        # TODO fix this
        return '0x661'

    def sget_path_to_kernel(self):
        pass

    def sget_flash_type(self):
        pass

    def sget_flash_size(self):
        pass

    def sget_flash_section_size(self):
        pass

    def get_running_command(self, *args, **kwargs):
        return self.get_node_property('/basics', 'running_command')

    def set_running_command(self, *args, **kwargs):
        running_command = args[0]
        self.set_node_property('/basics', running_command)

    def set_uart_baud(self, *args, **kwargs):
        uart_baud = args[0]
        self.set_node_property('uart', 'baud', uart_baud)

    def get_uart_baud(self, *args, **kwargs):
        return self.get_node_property('uart', 'baud')

    def set_url(self, *args, **kwargs):
        url = args[0]
        self.set_node_property('/basics', 'url', url)

    def get_url(self, *args, **kwargs):
        return self.get_node_property('/basics', 'url')

    def set_format(self, *args, **kwargs):
        format_ = args[0]
        self.set_node_property('/basics', 'format', format_)

    def get_format(self, *args, **kwargs):
        return self.get_node_property('/basics', 'format')

    def set_homepage(self, *args, **kwargs):
        homepage = args[0]
        self.set_node_property('/basics', 'homepage', homepage)

    def get_homepage(self, *args, **kwargs):
        return self.get_node_property('/basics', 'homepage')

    def set_description(self, *args, **kwargs):
        description = args[0]
        self.set_node_property('/basics', 'description', description)

    def get_description(self, *args, **kwargs):
        return self.get_node_property('/basics', 'description')

    def set_path_to_image(self, *args, **kwargs):
        path_to_image = args[0]
        self.set_node_property('/components', 'path_to_image', path_to_image)

    def get_path_to_image(self, *args, **kwargs):
        return self.get_node_property('/components', 'path_to_image')

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

    def set_path_to_source_code(self, *args, **kwargs):
        path_to_source_code = args[0]
        self.set_node_property('/components', 'path_to_source_code', path_to_source_code)

    def get_path_to_source_code(self, *args, **kwargs):
        return self.get_node_property('/components', 'path_to_source_code')

    def get_brand(self, *args, **kwargs):
        return self.get_node_property('/basics', 'brand')

    def set_brand(self, *args, **kwargs):
        brand = args[0]
        self.set_node_property('/basics', 'brand', brand)

    def get_endian(self, *args, **kwargs):
        return self.get_node_property('/basics', 'endian')

    def set_endian(self, *args, **kwargs):
        endian = args[0]
        self.set_node_property('/basics', 'endian', endian)

    def get_architecture(self, *args, **kwargs):
        return self.get_node_property('/basics', 'architecture')

    def set_architecture(self, *args, **kwargs):
        architecture = args[0]
        self.set_node_property('/basics', 'architecture', architecture)

    def get_timer_model(self, *args, **kwargs):
        return self.get_node_property('timer', 'compatible')

    def set_timer_model(self, *args, **kwargs):
        timer_model = args[0]
        self.set_node_property('timer', 'compatible', timer_model)

    def get_interrupt_controller_model(self, *args, **kwargs):
        return self.get_node_property('ic', 'compatible')

    def set_interrupt_controller_model(self, *args, **kwargs):
        ic_model = args[0]
        self.set_node_property('ic', 'compatible', ic_model)

    def get_uart_model(self, *args, **kwargs):
        return self.get_node_property('uart', 'compatible')

    def set_uart_model(self, *args, **kwargs):
        uart_model = args[0]
        self.set_node_property('uart', 'compatible', uart_model)

    def set_flash_type(self, *args, **kwargs):
        flash_type = args[0]
        self.set_node_property('flash', 'type', flash_type)

    def get_flash_type(self, *args, **kwargs):
        self.get_node_property('flash', 'type')

    def get_flash_model(self, *args, **kwargs):
        return self.get_node_property('flash', 'compatible')

    def find_flash_node(self):
        path_to_flash = None
        for path, nodes, props in self.profile.walk():
            if path.find('nand@') != -1 and path.find('partition@') == -1:
                path_to_flash = path
        if path_to_flash is None:
            path_to_flash = '/flash@0'
        return path_to_flash

    def find_cpu_nodes(self, new=False):
        # cpu nodes must follow the path convention below
        # /cpus/cpu@0, /cpus/cpu@1, ..., /cpus/@cpu@n
        # and this is the only api to create new cpu node
        # call this api before your call set_node_property
        path = []
        cpus = self.profile.get_node('/cpus', create=True)
        nodes = cpus.nodes
        for node in nodes:
            path.append(os.path.join(node.path, node.name))
        if not new:
            return path
        else:
            return os.path.join('/cpus', 'cpu@{}'.format(len(path)))

    def find_memory_node(self):
        # there should be one and only one memory node
        # and this is the only api to create new memory node
        memory = self.profile.get_node('/memory', create=True)
        self.set_node_property('/memory', 'device_type', 'memory')
        return '/memory'

    def set_node_property(self, path_to_node, property_, *values):
        for value in values:
            if value is None:
                return
        if path_to_node == 'flash':
            path_to_node = self.find_flash_node()
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

    def set_flash_model(self, *args, **kwargs):
        model = args[0]
        self.set_node_property('flash', 'compatible', model)

    def get_flash_size(self, *args, **kwargs):
        pass

    def set_flash_size(self, *args, **kwargs):
        pass

    def get_soc_model(self, *args, **kwargs):
        return self.get_node_property('/', 'model')

    def set_soc_model(self, *args, **kwargs):
        soc = args[0]
        self.set_node_property('/', 'model', soc)

    def get_toh(self, *args, **kwargs):
        if not len(args):
            return None
        toh = []
        brand_node = self.profile.get_node('/brand')
        assert brand_node is not None
        for property_ in args:
            value = brand_node.get_property(property_)
            if value is None:
                toh.append(value)
            else:
                toh.append(value.data[0])
        return toh

    def set_toh(self, *args, **kwargs):
        toh = args[0]
        assert isinstance(toh, list)
        header = kwargs.pop('header', None)
        if header is None:
            return
        brand_node = self.profile.get_node('/brand', create=True)
        for k, v in zip(header, toh):
            if brand_node.exist_property(k):
                brand_node.remove_property(k)
            if not len(v):
                continue
            brand_node.append(fdt.PropStrings(k, v))

    def get_revision(self, *args, **kwargs):
        return self.get_node_property('/brand', 'revision')

    def set_revision(self, *args, **kwargs):
        revision = args[0]
        self.set_node_property('/brand', 'revision', revision)

    def get_dts(self, *args, **kwargs):
        return None

    def set_dts(self, *args, **kwargs):
        dt = args[0]
        self.profile.merge(dt)

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

    def get_profile(self, *args, **kwargs):
        return self.profile

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

    def get_cpu_model(self, *args, **kwargs):
        return self.get_node_property('cpu', 'compatible')

    def set_cpu_model(self, *args, **kwargs):
        cpu_model = args[0]
        path_to_cpu = self.find_cpu_nodes(new=True)
        self.set_node_property(path_to_cpu, 'reg', '0x0')
        self.set_node_property(path_to_cpu, 'device_type', 'cpu')
        self.set_node_property(path_to_cpu, 'compatible', cpu_model)

    def get_ram(self, *args, **kwargs):
        path_to_ram = self.find_memory_node()
        ram = self.get_node_property(path_to_ram, 'reg', end=2)
        if ram is None:
            return None, None
        ram_base, ram_size = ram
        return ram_base, int(ram_size) / 1024  # to MiB

    def set_ram(self, *args, **kwargs):
        ram_base, ram_size = args
        unit = kwargs.pop('unit', 'MiB')
        factor = 1024
        self.set_node_property('/memory', 'reg', str(int(ram_base) * factor), str(int(ram_size) * factor))

    def __init__(self, *args, **kwargs):
        super(DTFirmware, self).__init__(*args, **kwargs)
