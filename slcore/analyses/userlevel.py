from slcore.amanager import Analysis


class CheckUserLevel(Analysis):
    def scan_user_level_qemudebug(self, pql):
        user_level = 'usr32' \
            if self.firmware.get_arch() == 'arm' else 'user'
        for k, cpurf in pql.cpurfs.items():
            if cpurf['mode'] == user_level:
                return True
        self.error_info = 'have not entered the user level'
        return False

    def scan_user_level_ktracer(self, pql):
        return False

    def run(self, **kwargs):
        trace_format = kwargs.pop('trace_format')
        path_to_trace = kwargs.pop('path_to_trace')

        self.info('scan user level indicators in {}'.format(
            path_to_trace), 1)

        trace = self.analysis_manager.get_analysis('loadtrace')
        pql = trace.pql

        if trace_format == 'qemudebug':
            result = self.scan_user_level_qemudebug(pql)
            if result:
                self.info('have entered the user level', 1)
                self.firmware.set_stage(True, 'user_mode')
                raise SystemExit()
            self.firmware.set_stage(False, 'user_mode')
            return result
        else:
            return self.scan_user_level_ktracer(pql)

    def __init__(self, analysis_manager):
        super().__init__(analysis_manager)
        self.name = 'userlevel'
        self.description = 'Check whether we have entered user level.'
        self.critical = False
        self.required = ['loadtrace', 'preparation', 'tracing']
        self.type = 'diag'


class CheckUserLevelF(Analysis):
    def __scan_arm_user_level_qemudebug(self, path_to_trace):
        with open(path_to_trace) as f:
            for line in f:
                if line.find('usr32') != -1:
                    return True
        self.error_info = 'have not entered the user level'
        return False

    def __scan_mips_user_level_qemudebug(self, path_to_trace):
        # CP0 Status  0x0100b413 Cause   0x00800028 EPC    0x76f31e68
        with open(path_to_trace) as f:
            for line in f:
                if line.find('CP0 Status') == -1:
                    continue
                status = (int(line.strip().split()[2], 16) >> 3) & 3
                if status == 2:
                    return True
        self.error_info = 'have not entered the user level'
        return False

    def scan_user_level_qemudebug(self, path_to_trace):
        if self.firmware.get_arch() == 'arm':
            return self.__scan_arm_user_level_qemudebug(path_to_trace)
        elif self.firmware.get_arch() == 'mips':
            return self.__scan_mips_user_level_qemudebug(path_to_trace)

    def scan_user_level_ktracer(self, path_to_trace):
        return False

    def run(self, **kwargs):
        trace_format = kwargs.pop('trace_format')
        path_to_trace = kwargs.pop('path_to_trace')
        self.info('scan user level indicators in {}'.format(
            path_to_trace), 1)

        if trace_format == 'qemudebug':
            result = self.scan_user_level_qemudebug(path_to_trace)
            if result:
                self.info('have entered the user level', 1)
                self.firmware.set_stage(True, 'user_mode')
                raise SystemExit()
            self.firmware.set_stage(False, 'user_mode')
            return result
        else:
            return self.scan_user_level_ktracer(path_to_trace)

    def __init__(self, analysis_manager):
        super().__init__(analysis_manager)
        self.name = 'fastuserlevel'
        self.description = \
            'Check whether we have entered user level in a faster way.'
        self.critical = False
        self.required = ['loadtrace', 'preparation', 'tracing']
        self.type = 'diag'
