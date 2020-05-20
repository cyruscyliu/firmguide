import os
import qmp
import tempfile
import subprocess

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
    def __init__(self, analysis_manager):
        super().__init__(analysis_manager)
        self.name = 'tracing'
        self.description = 'Trace QEMU execution for diagnosis.'
        self.critical = True
        self.required = ['preparation']
        self.type = 'diag'

    def analysis_status(self, status):
        return not status

    def run(self, **kwargs):
        path_to_trace = kwargs.pop('path_to_trace')

        # nochain is too too slow
        trace_flags = '-d in_asm,int,cpu -D {}'.format(path_to_trace)
        socket = tempfile.NamedTemporaryFile()
        qmp_flags = '-qmp unix:{},server,nowait'.format(socket.name)
        full_command = ' '.join(
            [self.firmware.running_command, trace_flags, qmp_flags])
        try:
            self.info(full_command, 1)
            status = subprocess.run(
                full_command, timeout=60, shell=True).returncode
        except subprocess.TimeoutExpired:
            status = 0
            qemu = qmp.QEMUMonitorProtocol(socket.name)
            qemu.connect()
            qemu.cmd('quit')
            qemu.close()
            socket.close()
        return self.analysis_status(status)
