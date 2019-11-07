import abc


class Firmware(object):
    def __init__(self, *args, **kwargs):
        self.id = None
        self.uuid = kwargs.pop('uuid')
        self.name = kwargs.pop('name')
        self.path = kwargs.pop('path')  # path to firmware
        self.size = kwargs.pop('size')
        self.working_dir = None
        self.working_path = None

        self.analysis_progress = None
        self.profile = None
        self.preset_cache = []

        # basics
        # brand, homepage, description, format, architecture, endian, url
        # components
        # path_to_image, path_to_kernel, path_to_dtb, path_to_source_code

    def handle_preset(self):
        for func, param in self.preset_cache:
            if param is None:
                continue
            func(param)

    @abc.abstractmethod
    def set_running_command(self, *args, **kwargs):
        pass

    @abc.abstractmethod
    def get_running_command(self, *args, **kwargs):
        pass

    @abc.abstractmethod
    def set_url(self, *args, **kwargs):
        # where this firmware is download
        pass

    @abc.abstractmethod
    def get_url(self, *args, **kwargs):
        pass

    @abc.abstractmethod
    def set_format(self, *args, **kwargs):
        pass

    @abc.abstractmethod
    def get_format(self, *args, **kwargs):
        pass

    @abc.abstractmethod
    def set_homepage(self, *args, **kwargs):
        pass

    @abc.abstractmethod
    def get_homepage(self, *args, **kwargs):
        pass

    @abc.abstractmethod
    def set_description(self, *args, **kwargs):
        pass

    @abc.abstractmethod
    def get_description(self, *args, **kwargs):
        pass

    def brief(self):
        brief_introduction = "uuid: {}, name: {}, brand: {}, architecture: {}, working_dir: {}, endian: {}".format(
            self.uuid, self.name, self.get_brand(), self.get_architecture(), self.working_dir, self.get_endian()
        )
        return brief_introduction

    def set_working_env(self, dir, path):
        self.working_dir = dir
        self.working_path = path

    @abc.abstractmethod
    def set_path_to_image(self, *args, **kwargs):
        pass

    @abc.abstractmethod
    def get_path_to_image(self, *args, **kwargs):
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
    def set_path_to_source_code(self, *args, **kwargs):
        pass

    @abc.abstractmethod
    def get_path_to_source_code(self, *args, **kwargs):
        pass

    @abc.abstractmethod
    def set_toh(self, *args, **kwargs):
        pass

    @abc.abstractmethod
    def get_toh(self, *args, **kwargs):
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

    @abc.abstractmethod
    def get_profile(self, *args, **kwargs):
        pass

    @abc.abstractmethod
    def save_profile(self, *args, **kwargs):
        pass

    @abc.abstractmethod
    def get_brand(self, *args, **kwargs):
        pass

    @abc.abstractmethod
    def set_brand(self, *args, **kwargs):
        pass

    @abc.abstractmethod
    def get_endian(self, *args, **kwargs):
        pass

    @abc.abstractmethod
    def set_endian(self, *args, **kwargs):
        pass

    @abc.abstractmethod
    def get_architecture(self, *args, **kwargs):
        pass

    @abc.abstractmethod
    def set_architecture(self, *args, **kwargs):
        pass

    @abc.abstractmethod
    def get_revision(self, *args, **kwargs):
        pass

    @abc.abstractmethod
    def set_revision(self, *args, **kwargs):
        pass

    @abc.abstractmethod
    def get_dts(self, *args, **kwargs):
        pass

    @abc.abstractmethod
    def set_dts(self, *args, **kwargs):
        pass

    @abc.abstractmethod
    def get_target(self, *args, **kwargs):
        pass

    @abc.abstractmethod
    def set_target(self, *args, **kwargs):
        pass

    @abc.abstractmethod
    def get_subtarget(self, *args, **kwargs):
        pass

    @abc.abstractmethod
    def set_subtarget(self, *args, **kwargs):
        pass

    @abc.abstractmethod
    def get_kernel_load_address(self, *args, **kwargs):
        pass

    @abc.abstractmethod
    def set_kernel_load_address(self, *args, **kwargs):
        pass

    @abc.abstractmethod
    def get_kernel_version(self, *args, **kwargs):
        pass

    @abc.abstractmethod
    def set_kernel_version(self, *args, **kwargs):
        pass

    @abc.abstractmethod
    def get_kernel_created_time(self, *args, **kwargs):
        pass

    @abc.abstractmethod
    def set_kernel_created_time(self, *args, **kwargs):
        pass

    @abc.abstractmethod
    def get_kernel_entry_point(self, *args, **kwargs):
        pass

    @abc.abstractmethod
    def set_kernel_entry_point(self, *args, **kwargs):
        pass

    @abc.abstractmethod
    def get_soc_model(self, *args, **kwargs):
        pass

    @abc.abstractmethod
    def set_soc_model(self, *args, **kwargs):
        pass

    @abc.abstractmethod
    def get_cpu_model(self, *args, **kwargs):
        pass

    @abc.abstractmethod
    def set_cpu_model(self, *args, **kwargs):
        pass

    @abc.abstractmethod
    def get_ram(self, *args, **kwargs):
        pass

    @abc.abstractmethod
    def set_ram(self, *args, **kwargs):
        pass

    @abc.abstractmethod
    def get_interrupt_controller_model(self, *args, **kwargs):
        pass

    @abc.abstractmethod
    def set_interrupt_controller_model(self, *args, **kwargs):
        pass

    @abc.abstractmethod
    def get_flash_model(self, *args, **kwargs):
        pass

    @abc.abstractmethod
    def set_flash_model(self, *args, **kwargs):
        pass

    @abc.abstractmethod
    def get_flash_size(self, *args, **kwargs):
        pass

    @abc.abstractmethod
    def set_flash_size(self, *args, **kwargs):
        pass

    @abc.abstractmethod
    def set_flash_type(self, *args, **kwargs):
        pass

    @abc.abstractmethod
    def get_flash_type(self, *args, **kwargs):
        pass

    @abc.abstractmethod
    def get_uart_model(self, *args, **kwargs):
        pass

    @abc.abstractmethod
    def set_uart_model(self, *args, **kwargs):
        pass

    @abc.abstractmethod
    def set_uart_baud(self, *args, **kwargs):
        pass

    @abc.abstractmethod
    def get_uart_baud(self, *args, **kwargs):
        pass

    @abc.abstractmethod
    def get_timer_model(self, *args, **kwargs):
        pass

    @abc.abstractmethod
    def set_timer_model(self, *args, **kwargs):
        pass
