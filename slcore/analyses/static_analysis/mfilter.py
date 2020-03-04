import os

from slcore.analyses.analysis import Analysis
from slcore.database.dbf import get_database


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
        exclude = [
            'boot', 'common', 'configs', 'crypto', 'firmware', 'include', 'kernel',
            'kvm', 'lib', 'mm', 'net', 'nvfpe', 'oprofile', 'tools', 'xen'
        ]
        self.path_to_srcode = firmware.get_srcodec().get_path_to_source_code()
        self.arch = 'arm'
        target = self.find_dir_compiled(exclude=exclude)
        if target is None:
            self.context['input'] = 'no available target found, please check the source code'
            return False
        support = get_database('support')
        status = support.select('board', board=target, arch='arm')
        if status:
            firmware.set_board(target)
            return True
        else:
            self.context['input'] = 'arm/{} is not supported yet'.format(target)
            return False

    def is_unsupport_mips_machine(self, firmware):
        exclude = [
            'boot', 'configs', 'fw', 'include', 'kernel', 'kvm', 'lib', 'mm',
            'math-emu', 'lib', 'net', 'oprofile', 'paravirt', 'pci', 'power'
        ]
        self.path_to_srcode = firmware.get_srcodec().get_path_to_source_code()
        self.arch = 'mips'
        target = self.find_dir_compiled(exclude=exclude)
        if target is None:
            self.context['input'] = 'no available target found, please check the source code'
            return False
        support = get_database('support')
        status = support.select('board', board=target, arch='mips')
        if status:
            firmware.set_board(target)
            self.info(firmware, 'mips/{} is supported'.format(target), 1)
            return True
        else:
            self.context['input'] = 'mips/{} is not supported yet'.format(target)
            return False

    def run(self, firmware):
        srcodec = firmware.get_srcodec()
        if srcodec is None:
            self.context['input'] = 'please set the source code'
            return False

        arch = firmware.get_arch()
        if arch == 'arm':
            return self.is_unsupport_arm_machine(firmware)
        elif arch == 'mips':
            return self.is_unsupport_mips_machine(firmware)
        else:
            return False

    def __init__(self, analysis_manager):
        super().__init__(analysis_manager)
        self.name = 'mfilter'
        self.description = 'some machines are not possible to support yet'
        self.required = []
        self.context['hint'] = 'cannot support this machine yet'
        self.critical = True
        #
        self.path_to_srcode = None
        self.arch = None

