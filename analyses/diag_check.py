import os

from analyses.analysis import Analysis


class Checking(Analysis):
    def scan_user_level_qemudebug(self, firmware):
        cmd = 'grep usr {} >/dev/null 2>&1'.format(firmware.path_to_trace)
        not_find_user_level = os.system(cmd)
        if not_find_user_level:
            self.context['input'] = 'have not entered the user level'
        return not not_find_user_level

    def scan_user_level_ktracer(self, firmware):
        return False

    def run(self, firmware):
        self.info(firmware, 'scan user level indicators in {}'.format(firmware.path_to_trace), 1)
        if firmware.trace_format == 'qemudebug':
            return self.scan_user_level_qemudebug(firmware)
        else:
            return self.scan_user_level_ktracer(firmware)

    def __init__(self):
        super().__init__()
        self.name = 'check'
        self.description = 'check whether we have done our job'
        self.context['hint'] = 'bad bad bad trace'
        self.critical = False
        self.required = ['do_tracing']
