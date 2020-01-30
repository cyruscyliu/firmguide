import abc


class KernelForFirmware(object):
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
