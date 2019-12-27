import abc

from supervisor.logging_setup import logger_info, logger_warning


class Analysis(object):
    def __init__(self, analysis_manager):
        self.analysis_manager = analysis_manager
        self.name = None
        self.description = None
        self.required = []
        self.context = {'hint': '', 'input': ''}
        self.critical = False
        self.args = None

    def is_critical(self):
        return self.critical

    def has_required(self):
        return len(self.required)

    def add_required(self, analysis_name):
        pass

    @abc.abstractmethod
    def run(self, firmware):
        pass

    def info(self, firmware, message, status):
        logger_info(firmware.get_uuid(), 'analysis', self.name, message, status)

    def error(self, firmware):
        if self.context['input'].find('\n') != -1:
            logger_warning(firmware.get_uuid(), 'analysis', self.name, self.context['hint'], 0)
            lines = self.context['input'].split('\n')
            for line in lines:
                if len(line):
                    logger_warning(firmware.get_uuid(), 'analysis', self.name, line, 0)
        else:
            logger_warning(
                firmware.get_uuid(), 'analysis', self.name, ', '.join([self.context['hint'], self.context['input']]), 0)


class AnalysisGroup(object):
    def __init__(self):
        self.name = None
        self.description = None
        self.members = []
        self.required = []

    @abc.abstractmethod
    def run(self, firmware):
        pass
