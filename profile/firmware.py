import abc

from profile.kernel import KernelForFirmware
from profile.openwrt import OpenWRTForFirmware


class Firmware(KernelForFirmware, OpenWRTForFirmware):
    def __init__(self, *args, **kwargs):
        self.uuid = None
        self.name = None
        self.path = None
        self.size = None
        self.working_dir = None
        self.working_path = None

        self.analysis_progress = None  # file
        self.profile = None  # dict
        self.path_to_profile = None

        self.trace_format = None
        self.path_to_trace = None
        self.do_not_diagnosis = False  # flag

        self.path_to_source_code = None
        self.path_to_vmlinux = None

        self.architecture = None
        self.endian = None
        self.brand = None

    # general getters and setters
    def get_uuid(self):
        return self.uuid

    def set_uuid(self, uuid):
        self.uuid = uuid

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_path(self):
        return self.path

    def set_path(self, path):
        self.path = path

    def get_working_path(self):
        return self.working_path

    def set_working_path(self, working_path):
        self.working_path = working_path

    def get_working_dir(self):
        return self.working_dir

    def set_working_dir(self, working_dir):
        self.working_dir = working_dir

    def get_trace_format(self):
        return self.trace_format

    def set_trace_format(self, trace_format):
        self.trace_format = trace_format

    def get_path_to_trace(self):
        return self.path_to_trace

    def set_path_to_trace(self, path_to_trace):
        self.path_to_trace = path_to_trace

    def get_architecture(self):
        return self.architecture

    def get_endian(self):
        return self.endian

    def set_endian(self, endian):
        self.endian = endian

    def get_brand(self):
        return self.brand

    def set_brand(self, brand):
        self.brand = brand

    def get_path_to_vmlinux(self):
        return self.path_to_vmlinux

    def set_path_to_vmlinux(self, path_to_vmlinux):
        self.path_to_vmlinux = path_to_vmlinux

    def get_path_to_source_code(self):
        return self.path_to_source_code

    def set_path_to_source_code(self, path_to_source_code):
        self.path_to_source_code = path_to_source_code

    # core
    def set_working_env(self, dir, path):
        self.working_dir = dir
        self.working_path = path

    @abc.abstractmethod
    def copy_profile(self, *args, **kwargs):
        pass

    @abc.abstractmethod
    def set_profile(self, *args, **kwargs):
        """
        set_profile(profile)
        set_profile(working_dir=working_dir, first=True)
            load from file after create it
        set_profile(working_dir=working_dir) *
            load from file
        set_profile(working_dir=working_dir, first=False) *
            load from file
        NOTE: * are some.

        :param args: profile.
        :param kwargs: working_dir, first.
        :return: None
        """
        pass

    def get_profile(self, *args, **kwargs):
        return self.profile

    @abc.abstractmethod
    def save_profile(self, *args, **kwargs):
        pass

    @abc.abstractmethod
    def get_dts(self, *args, **kwargs):
        pass

    @abc.abstractmethod
    def set_dts(self, *args, **kwargs):
        pass

    def brief(self, *args, **kwargs):
        brief_introduction = 'uuid: {}, name: {}, brand: {}, architecture: {}, working_dir: {}, endian: {}'.format(
            self.uuid, self.name, self.brand, self.architecture, self.working_dir, self.endian
        )
        return brief_introduction

    def summary(self, *args, **kwargs):
        brief_summary = 'uuid: {}, name:{}, profile at {}'.format(self.uuid, self.name, self.path_to_profile)
        return brief_summary

    # components
    @abc.abstractmethod
    def set_format(self, *args, **kwargs):
        pass

    @abc.abstractmethod
    def get_format(self, *args, **kwargs):
        pass

    @abc.abstractmethod
    def set_path_to_llvm_bitcode(self, *args, **kwargs):
        pass

    @abc.abstractmethod
    def get_path_to_llvm_bitcode(self, *args, **kwargs):
        pass

    @abc.abstractmethod
    def set_path_to_dot_config(self, *args, **kwargs):
        pass

    @abc.abstractmethod
    def get_path_to_dot_config(self, *args, **kwargs):
        pass

    @abc.abstractmethod
    def set_path_to_image(self, *args, **kwargs):
        pass

    @abc.abstractmethod
    def get_path_to_image(self, *args, **kwargs):
        pass

    @abc.abstractmethod
    def set_path_to_uimage(self, *args, **kwargs):
        pass

    @abc.abstractmethod
    def get_path_to_uimage(self, *args, **kwargs):
        pass

    @abc.abstractmethod
    def set_path_to_kernel(self, *args, **kwargs):
        pass

    @abc.abstractmethod
    def get_path_to_kernel(self, *args, **kwargs):
        pass

    @abc.abstractmethod
    def set_path_to_dtb(self, *args, **kwargs):
        pass

    @abc.abstractmethod
    def get_path_to_dtb(self, *args, **kwargs):
        pass

    # basics
    @abc.abstractmethod
    def get_machine_description(self, *args, **kwargs):
        pass

    @abc.abstractmethod
    def set_machine_description(self, *args, **kwargs):
        pass

    @abc.abstractmethod
    def get_machine_name(self, *args, **kwargs):
        pass

    @abc.abstractmethod
    def set_machine_name(self, *args, **kwargs):
        pass

    @abc.abstractmethod
    def get_board_id(self, *args, **kwargs):
        pass

    @abc.abstractmethod
    def set_board_id(self, *args, **kwargs):
        pass

    # ==== cpu ====
    @abc.abstractmethod
    def get_cpu_model(self, *args, **kwargs):
        pass

    @abc.abstractmethod
    def set_cpu_model(self, *args, **kwargs):
        pass

    def probe_cpu_pp_model(self, *args, **kwargs):
        return self.get_cpu_pp_name() is not None

    @abc.abstractmethod
    def get_cpu_pp_name(self, *args, **kwargs):
        pass

    @abc.abstractmethod
    def set_cpu_pp_name(self, *args, **kwargs):
        pass

    @abc.abstractmethod
    def get_cpu_pp_mmio_base(self, *args, **kwargs):
        pass

    @abc.abstractmethod
    def set_cpu_pp_mmio_base(self, *args, **kwargs):
        pass

    # ==== ram ====
    @abc.abstractmethod
    def get_ram_priority(self, *args, **kwargs):
        pass

    @abc.abstractmethod
    def set_ram_priority(self, *args, **kwargs):
        pass

    @abc.abstractmethod
    def get_ram_base(self, *args, **kwargs):
        pass

    @abc.abstractmethod
    def set_ram_base(self, *args, **kwargs):
        pass

    @abc.abstractmethod
    def get_ram_size(self, *args, **kwargs):
        pass

    @abc.abstractmethod
    def set_ram_size(self, *args, **kwargs):
        pass

    # ===== bridge ====
    def probe_bridge(self, *args, **kwargs):
        return self.get_bridge_name() is not None

    @abc.abstractmethod
    def get_bridge_name(self, *args, **kwargs):
        pass

    @abc.abstractmethod
    def set_bridge_name(self, *args, **kwargs):
        pass

    @abc.abstractmethod
    def get_bridge_mmio_base(self, *args, **kwargs):
        pass

    @abc.abstractmethod
    def set_bridge_mmio_base(self, *args, **kwargs):
        pass

    @abc.abstractmethod
    def get_bridge_mmio_size(self, *args, **kwargs):
        pass

    @abc.abstractmethod
    def set_bridge_mmio_size(self, *args, **kwargs):
        pass

    @abc.abstractmethod
    def get_bridge_registers(self, *args, **kwargs):
        pass

    # ===== interrupt controller ====
    def probe_interrupt_controller(self, *args, **kwargs):
        return self.get_interrupt_controller_name() is not None

    @abc.abstractmethod
    def get_interrupt_controller_name(self, *args, **kwargs):
        pass

    @abc.abstractmethod
    def set_interrupt_controller_name(self, *args, **kwargs):
        pass

    @abc.abstractmethod
    def get_interrupt_controller_registers(self, *args, **kwargs):
        pass

    @abc.abstractmethod
    def set_interrupt_controller_registers(self, *args, **kwargs):
        pass

    @abc.abstractmethod
    def get_interrupt_controller_mmio_size(self, *args, **kwargs):
        pass

    @abc.abstractmethod
    def set_interrupt_controller_mmio_size(self, *args, **kwargs):
        pass

    @abc.abstractmethod
    def get_interrupt_controller_mmio_base(self, *args, **kwargs):
        pass

    @abc.abstractmethod
    def set_interrupt_controller_mmio_base(self, *args, **kwargs):
        pass

    @abc.abstractmethod
    def get_n_irqs(self, *args, **kwargs):
        pass

    @abc.abstractmethod
    def set_n_irqs(self, *args, **kwargs):
        pass

    # ==== timer ====
    def probe_timer(self, *args, **kwargs):
        return self.get_timer_name() is not None

    @abc.abstractmethod
    def get_timer_name(self, *args, **kwargs):
        pass

    @abc.abstractmethod
    def set_timer_name(self, *args, **kwargs):
        pass

    @abc.abstractmethod
    def get_timer_registers(self, *args, **kwargs):
        pass

    @abc.abstractmethod
    def set_timer_register(self, *args, **kwargs):
        pass

    @abc.abstractmethod
    def get_timer_mmio_size(self, *args, **kwargs):
        pass

    @abc.abstractmethod
    def set_timer_mmio_size(self, *args, **kwargs):
        pass

    @abc.abstractmethod
    def get_timer_mmio_base(self, *args, **kwargs):
        pass

    @abc.abstractmethod
    def set_timer_mmio_base(self, *args, **kwargs):
        pass

    # ==== uart ====
    def probe_uart(self, *args, **kwargs):
        return self.get_uart_name() is not None

    @abc.abstractmethod
    def get_uart_name(self, *args, **kwargs):
        pass

    @abc.abstractmethod
    def set_uart_name(self, *args, **kwargs):
        pass

    @abc.abstractmethod
    def get_uart_mmio_base(self, *args, **kwargs):
        pass

    @abc.abstractmethod
    def set_uart_mmio_base(self, *args, **kwargs):
        pass

    @abc.abstractmethod
    def get_uart_baud_rate(self, *args, **kwargs):
        pass

    @abc.abstractmethod
    def set_uart_baud_rate(self, *args, **kwargs):
        pass

    @abc.abstractmethod
    def get_uart_reg_shift(self, *args, **kwargs):
        pass

    @abc.abstractmethod
    def set_uart_reg_shift(self, *args, **kwargs):
        pass

    @abc.abstractmethod
    def get_uart_irq(self, *args, **kwargs):
        pass

    @abc.abstractmethod
    def set_uart_irq(self, *args, **kwargs):
        pass

    # ==== flash ====
    def probe_flash(self, *args, **kwargs):
        return self.get_flash_type() is not None

    @abc.abstractmethod
    def get_flash_base(self, *args, **kwargs):
        pass

    @abc.abstractmethod
    def set_flash_base(self, *args, **kwargs):
        pass

    @abc.abstractmethod
    def get_flash_type(self, *args, **kwargs):
        pass

    @abc.abstractmethod
    def set_flash_type(self, *args, **kwargs):
        pass

    @abc.abstractmethod
    def get_flash_size(self, *args, **kwargs):
        pass

    @abc.abstractmethod
    def set_flash_size(self, *args, **kwargs):
        pass

    @abc.abstractmethod
    def get_flash_section_size(self, *args, **kwargs):
        pass

    @abc.abstractmethod
    def set_flash_section_size(self, *args, **kwargs):
        pass

    # ==== bamboo devices ====
    @abc.abstractmethod
    def get_bamboo_devices(self, *args, **kwargs):
        pass
