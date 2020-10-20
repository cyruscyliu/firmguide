import os

from slcore.amanager import Analysis
from slcore.database.dbf import get_database


class CheckBoard(Analysis):
    def find_dir_compiled(self, arch, exclude=None):
        if exclude is None:
            exclude = []

        candidates = []
        for root, ds, fs in os.walk(
                os.path.join(self.path_to_srcode, 'arch', arch)):
            if root.endswith(arch):
                continue
            if '.built-in.o.cmd' in fs:
                candidates.append(root)

        results = []
        for candidate in candidates:
            things = candidate.split('/')
            target = things[things.index(arch) + 1]
            if target in exclude:
                continue
            results.append(target)

        if len(results):
            return results[0]
        else:
            return None

    def is_unsupport_arm_machine(self):
        exclude = [
            'boot', 'common', 'configs', 'crypto', 'firmware', 'include',
            'kernel', 'kvm', 'lib', 'mm', 'net', 'nvfpe', 'oprofile',
            'tools', 'xen', 'vfp', 'vdso', 'probes', 'plat-orion']
        target = self.find_dir_compiled('arm', exclude=exclude)
        if target is None:
            self.error_info = \
                'no available target found, please compile the source code'
            return False
        self.info('arm/{} is under our consideration'.format(target), 1)
        return True

    def is_unsupport_mips_machine(self):
        exclude = [
            'boot', 'configs', 'fw', 'include', 'kernel', 'kvm', 'lib', 'mm',
            'math-emu', 'lib', 'net', 'oprofile', 'paravirt', 'pci', 'power',
            'vdso'
        ]
        target = self.find_dir_compiled('mips', exclude=exclude)
        if target is None:
            self.error_info = \
                'no available target found, please check the source code'
            return False
        self.info('mips/{} is under our consideration'.format(target), 1)

    def run(self, **kwargs):
        srcodec = self.analysis_manager.srcodec
        if not srcodec.supported:
            self.error_info = 'please set the source code'
            return False
        self.path_to_srcode = srcodec.get_path_to_source_code()

        if self.is_unsupport_arm_machine():
            return True
        if self.is_unsupport_mips_machine():
            return True

        self.error_info = 'no arch/xxx is supported or recognized'
        return False

    def __init__(self, analysis_manager):
        super().__init__(analysis_manager)
        self.name = 'bfilter'
        self.description = 'Decide which Linux kenrel board is supported.'
        self.critical = True
        self.path_to_srcode = None
