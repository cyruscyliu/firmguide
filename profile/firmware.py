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

        self.analysis_progress = None
        self.profile = None
        self.preset_cache = []

        self.trace_format = None
        self.path_to_trace = None
        self.do_not_diagnosis = False

        self.path_to_source_code = None
        self.architecture = None
        self.endian = None
        self.brand = None

        # basics
        # brand, homepage, description, format, architecture, endian, url
        # components
        # path_to_image, path_to_kernel, path_to_dtb

    # core
    def set_working_env(self, dir, path):
        self.working_dir = dir
        self.working_path = path

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

    @abc.abstractmethod
    def get_profile(self, *args, **kwargs):
        pass

    @abc.abstractmethod
    def save_profile(self, *args, **kwargs):
        pass

    @abc.abstractmethod
    def get_dts(self, *args, **kwargs):
        pass

    @abc.abstractmethod
    def set_dts(self, *args, **kwargs):
        pass

    def brief(self):
        brief_introduction = "uuid: {}, name: {}, brand: {}, architecture: {}, working_dir: {}, endian: {}".format(
            self.uuid, self.name, self.brand, self.architecture, self.working_dir, self.endian
        )
        return brief_introduction

    def summary(self):
        return self.brief()
   
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

    # basics
    @abc.abstractmethod
    def get_machine_description(self):
        pass

    @abc.abstractmethod
    def get_machine_name(self):
        pass

    @abc.abstractmethod
    def get_board_id(self):
        pass

    # ==== cpu ====
    @abc.abstractmethod
    def get_cpu_model(self):
        pass

    @abc.abstractmethod
    def set_cpu_model(self, *args, **kwargs):
        pass

    @abc.abstractmethod
    def get_cpu_pp_mmio_base(self):
        pass

    # ==== ram ====
    @abc.abstractmethod
    def get_ram_priority(self):
        pass

    @abc.abstractmethod
    def get_ram_size(self):
        pass

    # ===== bridge ====
    @abc.abstractmethod
    def probe_bridge(self):
        return False

    @abc.abstractmethod
    def get_bridge_name(self):
        pass

    @abc.abstractmethod
    def get_bridge_mmio_base(self):
        pass

    @abc.abstractmethod
    def get_bridge_mmio_size(self):
        pass

    @abc.abstractmethod
    def get_bridge_registers(self):
        pass

    # ===== interrupt controller ====
    @abc.abstractmethod
    def probe_interrupt_controller(self):
        pass

    @abc.abstractmethod
    def get_interrupt_controller_name(self):
        pass

    @abc.abstractmethod
    def get_interrupt_controller_registers(self):
        pass

    @abc.abstractmethod
    def get_interrupt_controller_mmio_size(self):
        pass

    @abc.abstractmethod
    def get_interrupt_controller_mmio_base(self):
        pass

    @abc.abstractmethod
    def get_n_irqs(self):
        pass

    # ==== timer ====
    @abc.abstractmethod
    def probe_timer(self):
        pass

    @abc.abstractmethod
    def get_timer_name(self):
        pass

    @abc.abstractmethod
    def set_timer_name(self):
        pass

    @abc.abstractmethod
    def get_timer_registers(self):
        pass

    @abc.abstractmethod
    def set_timer_register(self):
        pass

    @abc.abstractmethod
    def get_timer_mmio_size(self):
        pass

    @abc.abstractmethod
    def set_timer_mmio_size(self):
        pass

    @abc.abstractmethod
    def get_timer_mmio_base(self):
        pass

    @abc.abstractmethod
    def set_timer_mmio_base(self):
        pass

    # ==== uart ====
    @abc.abstractmethod
    def probe_uart(self):
        pass

    @abc.abstractmethod
    def get_uart_name(self):
        pass

    @abc.abstractmethod
    def set_uart_name(self):
        pass

    @abc.abstractmethod
    def get_uart_mmio_base(self):
        pass

    @abc.abstractmethod
    def set_uart_mmio_base(self):
        pass

    @abc.abstractmethod
    def get_uart_baud_rate(self):
        pass

    @abc.abstractmethod
    def set_uart_baud_rate(self):
        pass

    @abc.abstractmethod
    def get_uart_reg_shift(self):
        pass

    @abc.abstractmethod
    def set_uart_reg_shift(self):
        pass

    @abc.abstractmethod
    def get_uart_irq(self):
        pass

    @abc.abstractmethod
    def set_uart_irq(self):
        pass

    # ==== flash ====
    @abc.abstractmethod
    def get_flash_base(self):
        pass

    @abc.abstractmethod
    def set_flash_base(self):
        pass

    @abc.abstractmethod
    def get_flash_type(self):
        pass

    @abc.abstractmethod
    def set_flash_type(self):
        pass

    @abc.abstractmethod
    def get_flash_size(self):
        pass

    @abc.abstractmethod
    def set_flash_size(self):
        pass

    @abc.abstractmethod
    def get_flash_section_size(self):
        pass

    @abc.abstractmethod
    def set_flash_section_size(self):
        pass

    # ==== bamboo devices ====
    @abc.abstractmethod
    def get_bamboo_devices(self):
        pass
