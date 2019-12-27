import subprocess

import qmp

from analyses.analysis import Analysis
from supervisor.logging_setup import logger_info


class DoTracing(Analysis):
    def __init__(self):
        super().__init__()

        self.nane = 'do_tracing'
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
            status = subprocess.run(full_command, timeout=60, shell=True).returncode
        except subprocess.TimeoutExpired:
            status = 0
            qemu = qmp.QEMUMonitorProtocol(('localhost', 4444))
            qemu.connect()
            qemu.cmd('quit')
            qemu.close()
        return self.analysis_status(status)
