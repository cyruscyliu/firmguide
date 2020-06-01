import abc


class StatisticsForFirmware(object):
    @abc.abstractmethod
    def get_crm_num(self, *args, **kwargs):
        pass

    @abc.abstractmethod
    def set_crm_num(self, *args, **kwargs):
        pass

    @abc.abstractmethod
    def inc_crm_num(self, *args, **kwargs):
        pass

    @abc.abstractmethod
    def get_smm_num(self, *args, **kwargs):
        pass

    @abc.abstractmethod
    def set_smm_num(self, *args, **kwargs):
        pass

    @abc.abstractmethod
    def inc_smm_num(self, *args, **kwargs):
        pass

    @abc.abstractmethod
    def get_mrm_num(self, *args, **kwargs):
        pass

    @abc.abstractmethod
    def set_mrm_num(self, *args, **kwargs):
        pass

    @abc.abstractmethod
    def inc_mrm_num(self, *args, **kwargs):
        pass

    @abc.abstractmethod
    def get_iv_num(self, *args, **kwargs):
        pass

    @abc.abstractmethod
    def set_iv_num(self, *args, **kwargs):
        pass

    @abc.abstractmethod
    def inc_iv_num(self, *args, **kwargs):
        pass
