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
        self.type = 'diag'

        # store trace context
        self.pql = None

    def run(self, **kwargs):
        path_to_trace = kwargs.pop('path_to_trace')
        if path_to_trace is None:
            self.error_info = 'there is no trace available'
            return False
        if not os.path.exists(path_to_trace):
            self.error_info = '{} doesn\'t exist'.format(path_to_trace)
            return False

        self.info('loading {} ...'.format(path_to_trace), 1)
        if self.firmware.get_arch() == 'arm':
            if self.firmware.get_endian() == 'l':
                self.pql = get_pql('aarch32', 'little', path_to_trace)
            else:
                self.pql = get_pql('aarch32', 'big', path_to_trace)
        elif self.firmware.get_arch() == 'mips':
            if self.firmware.get_endian() == 'l':
                self.pql = get_pql('mips', 'little', path_to_trace)
            else:
                self.pql = get_pql('mips', 'big', path_to_trace)
        else:
            self.error_info = 'cannot support parsing log except arm/mips'
            return False

        self.pql.load_cpurf(dump=False)
        self.info('load {} cpu register files'.format(len(self.pql.cpurfs)), 1)
        self.pql.load_in_asm(dump=False)
        self.info('load {} basic blocks'.format(len(self.pql.bbs)), 1)
        return True


class Tracing(Analysis):
    def run(self, **kwargs):
        kwargs['running_command'] = self.firmware.running_command
        self.info('tracing QEMU machine {}'.format(
            self.firmware.get_machine_name()), 1)
        return self.analysis_manager.qemuc.trace(**kwargs)

    def __init__(self, analysis_manager):
        super().__init__(analysis_manager)
        self.name = 'tracing'
        self.description = 'Trace QEMU execution for diagnosis.'
        self.critical = True
        self.required = ['preparation', 'install']
        self.type = 'diag'


class DeleteTrace(Analysis):
    def run(self, **kwargs):
        path_to_trace = kwargs.pop('path_to_trace')
        if not os.path.exists(path_to_trace):
            return True

        delete = kwargs.pop('delete')
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
        self.type = 'diag'
