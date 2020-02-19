import subprocess
import tempfile
import qmp

from analyses.analysis import Analysis
from pyqemulog import get_pql


class LoadTrace(Analysis):
    def __init__(self, analysis_manager):
        super().__init__(analysis_manager)
        self.name = 'load_trace'
        self.description = 'load trace from do_tracing'
        self.context['hint'] = 'bad bad bad trace'
        self.critical = True
        self.required = ['do_tracing', 'preparation']
        self.type = 'diag'

        # store trace context
        self.pql = None

    def run(self, firmware):
        if firmware.get_arch() == 'arm':
            if firmware.get_endian() == 'l':
                self.pql = get_pql('aarch32', 'little', firmware.path_to_trace)
            else:
                self.pql = get_pql('aarch32', 'big', firmware.path_to_trace)
        elif firmware.get_arch() == 'mips':
            if firmware.get_endian() == 'l':
                self.pql = get_pql('mips', 'little', firmware.path_to_trace)
            else:
                self.pql = get_pql('mips', 'big', firmware.path_to_trace)
        else:
            self.context['input'] = 'can not support parsing log except arm/mips'
            return False

        self.pql.load_cpurf(dump=False)
        self.info(firmware, 'load {} cpu register files'.format(self.pql.cpurfs.__len__()), 1)
        self.pql.load_in_asm(dump=False)
        self.info(firmware, 'load {} basic blocks'.format(self.pql.bbs.__len__()), 1)
        return True


class DoTracing(Analysis):
    def __init__(self, analysis_manager):
        super().__init__(analysis_manager)
        self.name = 'do_tracing'
        self.description = 'tracing for diagnosis'
        self.context['hint'] = 'user interrup or QEMU internal error'
        self.critical = True
        self.required = ['preparation']
        self.type = 'diag'

    def analysis_status(self, status):
        return not status

    def run(self, firmware):
        # nochain is too too slow
        if firmware.uuid in ['9692', '9703', '9707', '9715', '7998', '13882', '13890', '13893', '13901']:
            trace_flags = '-d in_asm,int -D {}'.format(firmware.path_to_trace)
        else:
            trace_flags = '-d in_asm,int,cpu -D {}'.format(firmware.path_to_trace)
        socket = tempfile.NamedTemporaryFile()
        qmp_flags = '-qmp unix:{},server,nowait'.format(socket.name)
        full_command = ' '.join([firmware.running_command, trace_flags, qmp_flags])
        try:
            self.info(firmware, full_command, 1)
            status = subprocess.run(full_command, timeout=40, shell=True).returncode
        except subprocess.TimeoutExpired:
            status = 0
            qemu = qmp.QEMUMonitorProtocol(socket.name)
            qemu.connect()
            qemu.cmd('quit')
            qemu.close()
            socket.close()
        return self.analysis_status(status)

