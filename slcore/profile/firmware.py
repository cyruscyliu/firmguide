import os
import abc
import yaml

from slcore.profile.kernel import KernelForFirmware
from slcore.profile.openwrt import OpenWRTForFirmware


class Firmware(KernelForFirmware, OpenWRTForFirmware):
    def __init__(self, *args, **kwargs):
        # at beginning, you must uuid because your profile
        # is not ready, after your profile is ready, you
        # are suppose to use get_uuid()/set_uuid()
        # firmware is created/loaded/clean before an analysis
        # firmware is held in an analysis
        # firmware should be serialized after an analysis
        self.uuid = None

        # the following arguments will not go to your profile
        # because they are dynamically resolved
        self.size = None
        self.working_dir = None  # /tmp
        self.target_dir = None  # /tmp/uuid
        self.working_path = None  # /tmp/uuid/xxx.bin

        self.analysis_progress = None  # /tmp/uuid/analyses
        self.profile = None  # /tmp/uuid/profile.ext, dickt
        self.profile_ext = 'yaml'
        self.machine = None

        self.stat_reference = \
            yaml.safe_load(open(os.path.join(os.getcwd(), 'slcore/profile', 'stats.yaml')))
        self.stat_summary = {}
        self.path_to_summary = None  # /tmp/uuid/stats.yaml

        self.components = None
        self.dt_collection = None
        self.srcodec = None
        self.qemuc = None

        self.running_command = None
        self.trace_format = None
        self.path_to_trace = None
        self.cancle_compilation = False

        # flags
        self.do_not_diagnosis = False  # will stop early
        self.max_iteration = 20  # stop at 20 iteration
        self.rerun = False  # rerun inference analysis

    @abc.abstractmethod
    def stats(self):
        pass

    def init_profile(self):
        pass

    @abc.abstractmethod
    def print_profile(self):
        pass

    @abc.abstractmethod
    def get_uuid(self, *args, **kwargs):
        pass

    @abc.abstractmethod
    def set_uuid(self, *args, **kwargs):
        pass

    def get_target_dir(self):
        return self.target_dir

    def set_target_dir(self, target_dir):
        self.target_dir = target_dir

    def get_working_dir(self):
        return self.working_dir

    def set_working_dir(self, working_dir):
        self.working_dir = working_dir

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

    def get_components(self):
        return self.components

    def set_components(self, components):
        self.components = components

    def get_qemuc(self):
        return self.qemuc

    def set_qemuc(self, qemuc):
        self.qemuc = qemuc

    def get_srcodec(self):
        return self.srcodec

    def set_qemuc(self, srcodec):
        self.srcodec = srcodec

    def get_dt_collection(self):
        return self.dt_collection

    def set_dt_collection(self, dtc):
        self.dt_collection = dtc

    @abc.abstractmethod
    def set_arch(self, *args, **kwargs):
        pass

    @abc.abstractmethod
    def get_arch(self, *args, **kwargs):
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
        set_profile(target_dir=target_dir, first=True)
            load from file after create it
        set_profile(target_dir=target_dir) *
            load from file by default
        set_profile(target_dir=target_dir, first=False) *
            load from file by default
        set_profile(path_to_profile=path_to_profile) **
            load from the file assigned
        set_profile(path_to_profile=path_to_profile, first=False) **
            load from the file assigned
        NOTE: * are same and ** are same.
        """
        first = kwargs.pop('first', False)
        target_dir = kwargs.pop('target_dir', None)
        path_to_profile = kwargs.pop('path_to_profile', None)

        if len(args):
            profile = args[0]
        else:
            profile = None

        if profile is not None:
            self.profile = profile
            return

        if target_dir is None:
            self.path_to_profile = path_to_profile
        else:
            self.path_to_profile = os.path.join(target_dir, 'profile.yaml')

        if first:
            self.create_empty_profile()
        self.load_from_profile()
        self.init_profile()

    @abc.abstractmethod
    def is_empty_profile(self):
        pass

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

    # components
    @abc.abstractmethod
    def set_path_to_vmlinux(self, *args, **kwargs):
        pass

    @abc.abstractmethod
    def get_path_to_vmlinux(self, *args, **kwargs):
        pass

    @abc.abstractmethod
    def set_path_to_makeout(self, *args, **kwargs):
        pass

    @abc.abstractmethod
    def get_path_to_makeout(self, *args, **kwargs):
        pass

    @abc.abstractmethod
    def set_path_to_gcc(self, *args, **kwargs):
        pass

    @abc.abstractmethod
    def get_path_to_gcc(self, *args, **kwargs):
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
        SERIAL_ATTRIBUTES = [
            'id', 'name', 'base', 'size',
            'reg_shift', 'baud_rate', 'irqn'
        ]
        return self.get_uart_num() > 0

    # ==== flash ====
    def probe_flash(self, *args, **kwargs):
        FLASH_ATTRIBUTES = [
            'id', 'name', 'base', 'size',
            'type', 'interface', 'section_size'
        ]
        return self.get_flash_num() > 0

    # ==== bamboo devices ====
    @abc.abstractmethod
    def get_bamboo_devices(self, *args, **kwargs):
        pass

    @abc.abstractmethod
    def print_bamboo_devices(self, *args, **kwargs):
        pass

    @abc.abstractmethod
    def load_bamboo_devices(self, *args, **kwargs):
        pass

    @abc.abstractmethod
    def update_bamboo_devices(self, *args, **kwargs):
        pass

    @abc.abstractmethod
    def insert_bamboo_devices(self, *args, **kwargs):
        pass

    # ==== mapping ====
    @abc.abstractmethod
    def set_va_pa_mapping(self, *args, **kwargs):
        # va, pa, size
        pass

    @abc.abstractmethod
    def get_va_pa_mapping(self, *args, **kwargs):
        pass

    # ==== runtime ==
    @abc.abstractmethod
    def set_iteration(self, *args, **kwargs):
        pass

    @abc.abstractmethod
    def get_iteration(self, *args, **kwargs):
        pass

    @abc.abstractmethod
    def set_stage(self, *args, **kwargs):
        pass

    @abc.abstractmethod
    def get_stage(self, *args, **kwargs):
        pass
