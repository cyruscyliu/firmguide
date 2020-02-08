import abc


class OpenWRTForFirmware(object):
    @abc.abstractmethod
    def set_url(self, *args, **kwargs):
        # where this firmware is download
        pass

    @abc.abstractmethod
    def get_url(self, *args, **kwargs):
        pass

    @abc.abstractmethod
    def set_homepage(self, *args, **kwargs):
        pass

    @abc.abstractmethod
    def get_homepage(self, *args, **kwargs):
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
    def get_revision(self, *args, **kwargs):
        pass

    @abc.abstractmethod
    def set_revision(self, *args, **kwargs):
        pass

    @abc.abstractmethod
    def set_toh(self, *args, **kwargs):
        pass

    @abc.abstractmethod
    def get_toh(self, *args, **kwargs):
        pass
