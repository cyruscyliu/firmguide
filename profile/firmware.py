import os
import abc

from profile.kernel import KernelForFirmware
from profile.openwrt import OpenWRTForFirmware


class Firmware(KernelForFirmware, OpenWRTForFirmware):
    def __init__(self, *args, **kwargs):
        self.uuid = None
        self.size = None
        self.working_directory = None
        self.working_path = None

        self.analysis_progress = None  # file
        self.profile = None  # dict

        self.trace_format = None
        self.path_to_trace = None
        self.do_not_diagnosis = False  # flag
        self.no_inference = False

        self.rerun = False
        self.running_command = None

    def init_profile(self):
        self.set_uart_num(0)

    @abc.abstractmethod
    def load_uuid(self, *args, **kwargs):
        pass

    def get_uuid(self, *args, **kwargs):
        if self.uuid is None:
            return self.load_uuid()
        else:
            return self.uuid

    @abc.abstractmethod
    def set_uuid(self, *args, **kwargs):
        pass

    @abc.abstractmethod
    def get_name(self, *args, **kwargs):
        pass

    @abc.abstractmethod
    def set_name(self, *args, **kwargs):
        pass

    @abc.abstractmethod
    def get_path(self, *args, **kwargs):
        pass

    @abc.abstractmethod
    def set_path(self, *args, **kwargs):
        pass

    def get_working_dir(self):
        return self.working_directory

    def set_working_dir(self, working_dir):
        self.working_directory = working_dir

    def get_working_path(self):
        return self.working_path

    def set_working_path(self, working_path):
        self.working_path = working_path

    def get_trace_format(self):
        return self.trace_format

    def set_trace_format(self, trace_format):
        self.trace_format = trace_format

    def get_path_to_trace(self):
        return self.path_to_trace

    def set_path_to_trace(self, path_to_trace):
        self.path_to_trace = path_to_trace

    @abc.abstractmethod
    def set_architecture(self, *args, **kwargs):
        pass

    @abc.abstractmethod
    def get_architecture(self, *args, **kwargs):
        pass

    @abc.abstractmethod
    def get_endian(self, *args, **kwargs):
        pass

    @abc.abstractmethod
    def set_endian(self, *args, **kwargs):
        pass

    @abc.abstractmethod
    def get_brand(self, *args, **kwargs):
        pass

    @abc.abstractmethod
    def set_brand(self, *args, **kwargs):
        pass

    def set_profile(self, *args, **kwargs):
        """
        set_profile(profile)
        set_profile(working_dir=working_dir, first=True)
            load from file after create it
        set_profile(working_dir=working_dir) *
            load from file by default
        set_profile(working_dir=working_dir, first=False) *
            load from file by default
        set_profile(path_to_profile=path_to_profile) **
            load from the file assigned
        set_profile(path_to_profile=path_to_profile, first=False) **
            load from the file assigned
        NOTE: * are same and ** are same.
        """
        first = kwargs.pop('first', False)
        working_dir = kwargs.pop('working_dir', None)
        path_to_profile = kwargs.pop('path_to_profile', None)

        if len(args):
            profile = args[0]
        else:
            profile = None

        if profile is not None:
            self.profile = profile
            return

        if working_dir is None:
            self.path_to_profile = path_to_profile
        else:
            self.path_to_profile = os.path.join(working_dir, 'profile.dt')

        if first:
            self.create_empty_profile()
        self.load_from_profile()
        self.init_profile()

    @abc.abstractmethod
    def create_empty_profile(self):
        pass

    @abc.abstractmethod
    def load_from_profile(self):
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
            self.get_uuid(), self.get_name(), self.get_brand(), self.get_architecture(),
            self.working_directory, self.get_endian()
        )
        return brief_introduction

    def summary(self, *args, **kwargs):
        brief_summary = 'uuid: {}, name:{}, profile at {}'.format(self.get_uuid(), self.get_name(),
                                                                  self.path_to_profile)
        return brief_summary

    # components
    @abc.abstractmethod
    def set_format(self, *args, **kwargs):
        pass

    @abc.abstractmethod
    def get_format(self, *args, **kwargs):
        pass

    @abc.abstractmethod
    def set_path_to_vmlinux(self, *args, **kwargs):
        pass

    @abc.abstractmethod
    def get_path_to_vmlinux(self, *args, **kwargs):
        pass

    @abc.abstractmethod
    def set_path_to_source_code(self, *args, **kwargs):
        pass

    @abc.abstractmethod
    def get_path_to_source_code(self, *args, **kwargs):
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
    def set_timer_irq(self, *args, **kwargs):
        pass

    @abc.abstractmethod
    def get_timer_irq(self, *args, **kwargs):
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
        return int(self.get_uart_num()) > 0

    @abc.abstractmethod
    def set_uart_num(self, *args, **kwargs):
        pass

    @abc.abstractmethod
    def get_uart_num(self, *args, **kwargs):
        pass

    @abc.abstractmethod
    def get_uart_name(self, *args, **kwargs):
        pass

    @abc.abstractmethod
    def set_uart_name(self, *args, **kwargs):
        pass

    @abc.abstractmethod
    def get_uart_mmio_size(self, *args, **kwargs):
        pass

    @abc.abstractmethod
    def set_uart_mmio_size(self, *args, **kwargs):
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

    # ==== mapping ====
    @abc.abstractmethod
    def set_va_pa_mapping(self, *args, **kwargs):
        # va, pa, size
        pass

    @abc.abstractmethod
    def get_va_pa_mapping(self, *args, **kwargs):
        pass
