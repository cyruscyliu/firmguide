import subprocess
import qmp

from analyses.analysis import Analysis
from supervisor.logging_setup import logger_info
from pyqemulog import *


class LoadTrace(Analysis):
    def __init__(self, analysis_manager):
        super().__init__(analysis_manager)

        self.name = 'load_trace'
        self.description = 'load trace from do_tracing'
        self.context['hint'] = 'bad bad bad trace'
        self.critical = True
        self.required = ['do_tracing']

        # store trace context
        self.cpurfs = None
        self.bbs = None

    def run(self, firmware):
        self.cpurfs = load_cpurf(firmware.path_to_trace, dump=False)
        self.info(firmware, 'load {} cpu register files'.format(self.cpurfs.__len__()), 1)
        self.bbs = load_in_asm(firmware.path_to_trace, dump=False)
        self.info(firmware, 'load {} basic blocks'.format(self.bbs.__len__()), 1)
        return True


class DoTracing(Analysis):
    def __init__(self, analysis_manager):
        super().__init__(analysis_manager)

        self.name = 'do_tracing'
        self.description = 'tracing for diagnosis'
        self.context['hint'] = 'user interruption or QEMU internal error'
        self.critical = True
        self.required = []

    def analysis_status(self, status):
        return not status

    def run(self, firmware):
        # nochain is too too slow
        trace_flags = '-d in_asm,int,cpu -D {}'.format(firmware.path_to_trace)
        qmp_flags = '-qmp tcp:localhost:4444,server,nowait'
        full_command = ' '.join([firmware.running_command, trace_flags, qmp_flags])
        try:
            logger_info(firmware.get_uuid(), 'tracing', 'qemudebug', full_command, 0)
            status = subprocess.run(full_command, timeout=20, shell=True).returncode
        except subprocess.TimeoutExpired:
            status = 0
            qemu = qmp.QEMUMonitorProtocol(('localhost', 4444))
            qemu.connect()
            qemu.cmd('quit')
            qemu.close()
            logger_info(firmware.get_uuid(), 'tracing', 'qemudebug', 'done', 0)
        return self.analysis_status(status)
