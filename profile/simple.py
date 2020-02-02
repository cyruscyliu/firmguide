"""
Our ugly solution.
"""
import os
import yaml
import shutil

from profile.firmware import Firmware


class Bamboo(object):
    def __init__(self):
        self.name = None
        self.mmio_base = None
        self.mmio_size = None
        self.id = None
        self.value = None

    def __str__(self):
        return '{} from 0x{:x} to 0x{:x} 0x{:x}'.format(
            self.name, self.mmio_base, self.mmio_base + self.mmio_size, self.value)


class SimpleFirmware(Firmware):
    def print_bamboo_devices(self, *args, **kwargs):
        for bamboo in self.bamboos:
            yield bamboo.__str__()

    def load_bamboo_devices(self, *args, **kwargs):
        self.bamboos = []  # clear otherwise dupicated mmio regions
        bamboo_devices = self.get_general('bamboo')
        if bamboo_devices is None:
            bamboo_devices = {}

        self.bamboo_mmio_count = 0
        for name, parameters in bamboo_devices.items():
            bamboo = Bamboo()
            bamboo.name = name
            bamboo.id = int(name[4:])
            bamboo.mmio_base = int(parameters['mmio_base'], 16)
            bamboo.mmio_size = int(parameters['mmio_size'], 16)
            bamboo.value = int(parameters['registers']['stub_reserved{}'.format(bamboo.id)]['value'], 16)
            self.bamboo_mmio_count += 1
            self.bamboos.append(bamboo)

    def update_bamboo_devices(self, *args, **kwargs):
        latest_bamboo_devices = {}
        for bamboo in self.bamboos:
            if bamboo.mmio_size == 4:
                offset = '0x0'
            else:
                offset = '0x0 ... 0x{:x}'.format(bamboo.mmio_size - 4)
            latest_bamboo_devices[bamboo.name] = {
                'mmio_base': hex(bamboo.mmio_base),
                'mmio_size': hex(bamboo.mmio_size),
                'registers': {'stub_reserved{}'.format(bamboo.id): {'offset': offset, 'value': hex(bamboo.value)}}
            }
        self.set_general('bamboo', value=latest_bamboo_devices)

    def get_bamboo_devices(self, *args, **kwargs):
        bamboo_devices = self.get_general('bamboo')
        if bamboo_devices is None:
            return {}
        return bamboo_devices

    def split_bamboo(self, bamboo, a, b, value):
        left = bamboo.mmio_base
        right = bamboo.mmio_base + bamboo.mmio_size

        split_bamboos = [bamboo]
        if left == a:
            # -----------------
            # ++++-------------
            bamboo.mmio_base = a + b
            bamboo.mmio_size = right - left - b
            split_bamboos.append(self.get_bamboo(a, b, value))
        elif right == a + b:
            # -----------------
            # -------------++++
            bamboo.mmio_size = a - left
            split_bamboos.append(self.get_bamboo(a, b, value))
        else:
            # -----------------
            # ------++++xxxxxxx
            bamboo.mmio_size = a - left
            split_bamboos.append(self.get_bamboo(a, b, value))
            split_bamboos.append(self.get_bamboo(a + b, right - a - b, bamboo.value))

        return split_bamboos

    def get_bamboo(self, mmio_base, mmio_size, value):
        bamboo = Bamboo()
        bamboo.mmio_base = mmio_base
        bamboo.mmio_size = mmio_size
        bamboo.name = 'stub{}'.format(self.bamboo_mmio_count)
        bamboo.value = value
        bamboo.id = self.bamboo_mmio_count
        self.bamboo_mmio_count += 1
        return bamboo

    def insert_bamboo_devices(self, *args, **kwargs):
        mmio_base, mmio_size = args
        value = kwargs.pop('value', 0)

        # at first, we must ensure the list to be inserted is in order
        new_bamboos = []
        bamboos = None
        for exist in sorted(self.bamboos, key=lambda x: x.mmio_base):
            if exist.mmio_base + exist.mmio_size <= mmio_base:
                new_bamboos.append(exist)
            elif exist.mmio_base >= mmio_base + mmio_size:
                new_bamboos.append(exist)
            else:
                if (exist.mmio_base <= mmio_base and
                    mmio_base + mmio_size < exist.mmio_base + exist.mmio_size) or \
                        (exist.mmio_base < mmio_base and
                         mmio_base + mmio_size <= exist.mmio_base + exist.mmio_size):
                    bamboos = self.split_bamboo(exist, mmio_base, mmio_size, value)
                else:
                    return False

        if bamboos is None:
            bamboos = self.get_bamboo(mmio_base, mmio_size, value)
            new_bamboos.append(bamboos)
        else:
            new_bamboos.extend(bamboos)
        self.bamboos = new_bamboos
        return True

    def stats(self):
        results = {}
        for key, properties in self.stat_reference.items():
            levels = properties['level'].split('/')
            node = self.get_general(*levels)
            if node is None:
                results[key] = False
                continue
            if properties['mode'] == 'count':
                # len(levels) must be 1
                results[key] = len(node)
            elif properties['mode'] == 'stats':
                results[key] = {}
                for expect in properties['expect']:
                    if expect in node:
                        results[key][expect] = True
                    else:
                        results[key][expect] = False
            elif properties['mode'] == 'value':
                results[key] = {}
                for expect in properties['expect']:
                    if expect in node:
                        results[key][expect] = node[expect]
                    else:
                        results[key][expect] = False

        self.stat_summary = results
        self.path_to_summary = os.path.join(self.target_dir, 'stats.yaml')
        with open(self.path_to_summary, 'w') as f:
            yaml.dump(self.stat_summary, f)

    def print_profile(self):
        path_to_profile = os.path.join(self.target_dir, 'profile.yaml')
        print(path_to_profile)
        os.system('cat {}'.format(path_to_profile))

    def get_uuid(self, *args, **kwargs):
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

    def set_path_to_rootfs(self, *args, **kwargs):
        self.set_general('components', 'path_to_rootfs', value=args[0])

    def get_path_to_rootfs(self, *args, **kwargs):
        return self.get_general('components', 'path_to_rootfs')

    def set_path_to_vmlinux(self, *args, **kwargs):
        self.set_general('components', 'path_to_vmlinux', value=args[0])

    def get_path_to_vmlinux(self, *args, **kwargs):
        return self.get_general('components', 'path_to_vmlinux')

    def set_path_to_gcc(self, *args, **kwargs):
        self.set_general('components', 'path_to_gcc', value=args[0])

    def get_path_to_gcc(self, *args, **kwargs):
        return self.get_general('components', 'path_to_gcc')

    def set_path_to_makeout(self, *args, **kwargs):
        self.set_general('components', 'path_to_makeout', value=args[0])

    def get_path_to_makeout(self, *args, **kwargs):
        return self.get_general('components', 'path_to_makeout')

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
        # args: name, offset, value
        self.set_general('interrupt_controller', 'registers', args[0], 'offset', value=args[1])
        self.set_general('interrupt_controller', 'registers', args[0], 'value', value=args[2])

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
        uart_num = self.get_general('uart', 'num')
        if uart_num is None:
            self.set_uart_num(0)
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
        shutil.copy(path_to_profile, os.path.join(self.target_dir, 'profile.yaml'))

    def is_empty_profile(self):
        with open(self.path_to_profile, 'r') as f:
            profile = yaml.safe_load(f)
        if profile == {}:
            return True
        return False

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

    def set_va_pa_mapping(self, *args, **kwargs):
        # va, pa, size
        va, pa, size = args
        self.set_general('mapping', va, 'va', value=va)
        self.set_general('mapping', va, 'pa', value=pa)
        self.set_general('mapping', va, 'size', value=size)

    def get_va_pa_mapping(self, *args, **kwargs):
        va_pa_mapping = self.get_general('mapping')
        if va_pa_mapping is None:
            return {}
        else:
            return va_pa_mapping

    def get_iteration(self, *args, **kwargs):
        return self.get_general('runtime', 'iteration')

    def set_iteration(self, *args, **kwargs):
        self.set_general('runtime', 'iteration', value=args[0])

    def get_stage(self, *args, **kwargs):
        # get_stage('user_mode')
        return self.get_general('runtime', args[0])

    def set_stage(self, *args, **kwargs):
        # set_state(True, 'user_mode')
        self.set_general('runtime', args[1], value=args[0])

    def __init__(self, *args, **kwargs):
        super(SimpleFirmware, self).__init__(*args, **kwargs)
        self.profile_ext = 'yaml'
        #
        self.bamboo_mmio_count = 0
        self.bamboos = []
