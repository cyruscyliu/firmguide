import abc

from slcore.common import Common


class Analysis(Common):
    def __init__(self, analysis_manager):
        super().__init__()

        self.analysis_manager = analysis_manager
        self.name = None
        self.description = None
        self.required = []
        self.settings = []
        self.context = {'hint': '', 'input': ''}
        self.critical = False
        self.args = None
        self.type = 'inf'

    def is_critical(self):
        return self.critical

    def has_required(self):
        return len(self.required)

    def add_required(self, analysis_name):
        pass

    @abc.abstractmethod
    def run(self, firmware, **kwargs):
        pass

    def info(self, firmware, message, status):
        super().info(self.name, message, status)

    def debug(self, firmware, message, status):
        super().debug(self.name, message, status)

    def warning(self, firmware, message, status):
        super().warning(self.name, message, status)

    def error(self, firmware):
        if self.context['input'].find('\n') != -1:
            self.warning(self.name, self.context['hint'], 0)
            lines = self.context['input'].split('\n')
            for line in lines:
                if len(line):
                    self.warning(self.name, line, 0)
        else:
            self.warning(self.name, ', '.join([self.context['hint'], self.context['input']]), 0)


class AnalysisGroup(object):
    def __init__(self):
        self.name = None
        self.description = None
        self.members = []
        self.required = []

    @abc.abstractmethod
    def run(self, firmware):
        pass

