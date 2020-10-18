import abc


class StatisticsForFirmware2(object):
    @abc.abstractmethod
    def add_entry(self, entry):
        pass
