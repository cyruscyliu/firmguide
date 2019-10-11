import abc
import os


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
        # basics
        self.brand = None
        self.description = None
        self.format = None
        self.architecture = None
        self.endian = None
        self.url = None

        # components
        self.path_to_image = None
        self.path_to_kernel = None
        self.path_to_dtb = None

    def set_description(self, *args, **kwargs):
        description = args[0]
        self.description = description

    def get_description(self, *args, **kwargs):
        return self.description

    def set_url(self, *args, **kwargs):
        url = args[0]
        self.url = url

    def get_url(self, *args, **kwargs):
        return self.url

    def brief(self):
        brief_introduction = "uuid: {}, name: {}, brand: {}, architecture: {}, working_dir: {}, endian: {}".format(
            self.uuid, self.name, self.brand, self.architecture, self.working_dir, self.endian
        )
        return brief_introduction

    def set_working_env(self, dir, path):
        self.working_dir = dir
        self.working_path = path

    def set_path_to_image(self, *args, **kwargs):
        path = args[0]
        self.path_to_image = path

    def get_path_to_image(self, *args, **kwargs):
        return self.path_to_image

    def set_path_to_kernel(self, *args, **kwargs):
        path = args[0]
        self.path_to_kernel = path

    def get_path_to_kernel(self, *args, **kwargs):
        return self.path_to_kernel

    def set_path_to_dtb(self, *args, **kwargs):
        path = args[0]
        self.path_to_dtb = path

    def get_path_to_dtb(self, *args, **kwargs):
        return self.path_to_dtb

    def set_format(self, *args, **kwargs):
        format_ = args[0]
        assert format_ in ['legacy uImage', 'fit uImage', 'trx kernel', 'unknown']
        self.format = format_

    def get_format(self, *args, **kwargs):
        return self.format

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

    def get_brand(self, *args, **kwargs):
        return self.brand

    def set_brand(self, *args, **kwargs):
        brand = args[0]
        assert brand in ['openwrt']
        self.brand = brand

    def get_endian(self, *args, **kwargs):
        return self.endian

    def set_endian(self, *args, **kwargs):
        endian = args[0]
        assert endian in ['l', 'b']
        self.endian = endian

    def get_architecture(self, *args, **kwargs):
        return self.architecture

    def set_architecture(self, *args, **kwargs):
        architecture = args[0]
        assert architecture in ['arm', 'mips']
        self.architecture = architecture

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
    def get_timer_model(self, *args, **kwargs):
        pass

    @abc.abstractmethod
    def set_timer_model(self, *args, **kwargs):
        pass
