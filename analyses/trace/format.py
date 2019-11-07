import os
import abc


class Trace(object):
    def __init__(self, *args, **kwargs):
        self.trace_tool = None
        self.path_to_trace = args[0]

    @abc.abstractmethod
    def load(self, *args, **kwargs):
        """
        Load trace file fast.
        :return:
        """
        pass

    @abc.abstractmethod
    def scan_user_level(self, *args, **kwargs):
        pass


class QEMUDebug(Trace):
    def scan_user_level(self, *args, **kwargs):
        cmd = 'grep usr {} >/dev/null 2>&1'.format(self.path_to_trace)
        not_find_user_level = os.system(cmd)
        return not not_find_user_level

    def load_in_asm(self, *args, **kwargs):
        pass

    def load_cpu(self, *args, **kwargs):
        pass

    def load(self, *args, **kwargs):
        pass

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.trace_tool = 'qemu debug'
        self.flags = ['in_asm', 'cpu']


class KTracer(Trace):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.trace_tool = 'ktracer'
