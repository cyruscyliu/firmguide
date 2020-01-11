import os

from analyses.analysis import Analysis
from database.dbf import get_database
from profile.firmware import Firmware


class Filter(Analysis):
    def find_dir_compiled(self, exclude=None):
        if exclude is None:
            exclude = []

        candidates = []
        for root, ds, fs in os.walk(
                os.path.join(self.path_to_srcode, 'arch', self.arch)):
            if root.endswith(self.arch):
                continue
            if '.built-in.o.cmd' in fs:
                candidates.append(root)

        results = []
        for candidate in candidates:
            things = candidate.split('/')
            target = things[things.index(self.arch) + 1]
            if target in exclude:
                continue
            results.append(target)

        if len(results):
            return results[0]
        else:
            return None

    def is_unsupport_arm_machine(self, firmware):
        assert isinstance(firmware, Firmware)

        exclude = [
            'boot', 'common', 'configs', 'crypto', 'firmware', 'include', 'kernel',
            'kvm', 'lib', 'mm', 'net', 'nvfpe', 'oprofile', 'tools', 'xen'
        ]
        self.path_to_srcode = firmware.get_path_to_source_code()
        self.arch = 'arm'
        target = self.find_dir_compiled(exclude=exclude)
        if target is None:
            self.context['input'] = 'no available target found, please check the source code'
            return False
        support = get_database('support')
        status = support.select(target, arch='arm32')
        if status:
            return True
        else:
            self.context['input'] = 'arm/{} is not supported yet'.format(target)
            return False

    def is_unsupport_mips_machine(self, firmware):
        assert isinstance(firmware, Firmware)
        exclude = [
            'boot', 'configs', 'fw', 'include', 'kernel', 'kvm', 'lib', 'mm',
            'math-emu', 'lib', 'net', 'oprofile', 'paravirt', 'pci', 'power'
        ]
        self.path_to_srcode = firmware.get_path_to_source_code()
        self.arch = 'mips'
        target = self.find_dir_compiled(exclude=exclude)
        if target is None:
            self.context['input'] = 'no available target found, please check the source code'
            return False
        support = get_database('support')
        status = support.select(target, arch='mips')
        if status:
            return True
        else:
            self.context['input'] = 'mips/{} is not supported yet'.format(target)
            return False

    def run(self, firmware):
        arch = firmware.get_architecture()
        if arch == 'arm':
            return self.is_unsupport_arm_machine(firmware)
        elif arch == 'mips':
            return self.is_unsupport_mips_machine(firmware)
        else:
            return False

    def __init__(self, analysis_manager):
        super().__init__(analysis_manager)
        self.name = 'filter'
        self.description = 'some machines are not possible to support yet'
        self.required = ['mips_cpu']
        self.context['hint'] = 'cannot support this machine yet'
        self.critical = True
        #
        self.path_to_srcode = None
        self.arch = None
