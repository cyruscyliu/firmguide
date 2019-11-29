import os

from analyses.common.analysis import Analysis


class Checking(Analysis):
    def scan_user_level_qemudebug(self):
        cmd = 'grep usr {} >/dev/null 2>&1'.format(self.args[1])
        not_find_user_level = os.system(cmd)
        return not not_find_user_level

    def scan_user_level_ktracer(self):
        return False

    def run(self, firmware):
        # arguments
        # args[0] = trace_format
        # args[1] = path_to_trace
        self.info(firmware, 'scan user level indicators in {}'.format(self.args[1]), 1)
        if self.args[0] == 'qemudebug':
            return self.scan_user_level_qemudebug()
        else:
            return self.scan_user_level_ktracer()

    def __init__(self):
        super().__init__()
        self.name = 'check'
        self.description = 'check whether we have done our job'
        self.context['hint'] = 'bad bad bad trace'
        self.critical = True
        self.required = []
