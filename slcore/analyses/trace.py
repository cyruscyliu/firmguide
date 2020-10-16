import os

from slcore.amanager import Analysis
from pyqemulog import get_pql


class LoadTrace(Analysis):
    def __init__(self, analysis_manager):
        super().__init__(analysis_manager)
        self.name = 'loadtrace'
        self.description = 'Load QEMU trace from file.'
        self.critical = True
        self.required = ['tracing', 'preparation']

        # store trace context
        self.pql = None

    def run(self, **kwargs):
        path_to_trace = self.analysis_manager.path_to_trace
        if path_to_trace is None:
            self.error_info = 'there is no trace available'
            return False
        if not os.path.exists(path_to_trace):
            self.error_info = '{} doesn\'t exist'.format(path_to_trace)
            return False

        self.info('loading {} ...'.format(path_to_trace), 1)
        if self.analysis_manager.firmware.get_arch() is None:
            self.error_info = 'there is arch available'
            return False
        if self.analysis_manager.firmware.get_endian() is None:
            self.error_info = 'there is endian available'
            return False
        self.pql = get_pql('{}e{}'.format(
            self.analysis_manager.firmware.get_arch(), self.analysis_manager.firmware.get_endian()),
            path_to_trace, mode='generator')

        self.pql.load_in_asm()
        self.info('load {} basic blocks'.format(len(self.pql.bbs)), 1)
        if len(self.pql.bbs) == 0:
            self.error_info = 'there is no trace at all'
            return False
        return True


class Tracing(Analysis):
    def run(self, **kwargs):
        if not self.analysis_manager.qemuc.supported:
            self.error_info = 'please setup the QEMU'
            return False
        kwargs['running_command'] = self.analysis_manager.firmware.running_command
        kwargs['path_to_trace'] = self.analysis_manager.path_to_trace
        self.info('tracing QEMU machine {}'.format(
            self.analysis_manager.firmware.get_machine_name()), 1)
        return self.analysis_manager.qemuc.trace(**kwargs)

    def __init__(self, analysis_manager):
        super().__init__(analysis_manager)
        self.name = 'tracing'
        self.description = 'Trace QEMU execution for diagnosis.'
        self.critical = True
        self.required = ['preparation', 'install']


class DeleteTrace(Analysis):
    def run(self, **kwargs):
        path_to_trace = self.analysis_manager.path_to_trace
        if not os.path.exists(path_to_trace):
            return True

        delete = kwargs.pop('delete', True)
        if not delete:
            return True
        if delete:
            self.info('remove {}'.format(path_to_trace), 1)
            os.remove(path_to_trace)
            return True

    def __init__(self, analysis_manager):
        super().__init__(analysis_manager)
        self.name = 'deltrace'
        self.description = 'Delete trace to save space after trace analysis.'
        self.critical = False
        self.required = ['userlevel', 'fastuserlevel']
