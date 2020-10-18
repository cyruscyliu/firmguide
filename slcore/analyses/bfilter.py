import os

from slcore.amanager import Analysis
from slcore.database.dbf import get_database


class CheckBoard(Analysis):
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

    def is_unsupport_arm_machine(self):
        exclude = [
            'boot', 'common', 'configs', 'crypto', 'firmware', 'include',
            'kernel', 'kvm', 'lib', 'mm', 'net', 'nvfpe', 'oprofile',
            'tools', 'xen', 'vfp', 'vdso', 'probes', 'plat-orion']
        target = self.find_dir_compiled(exclude=exclude)
        if target is None:
            self.error_info = \
                'no available target found, please compile the source code'
            return False
        support = get_database('support')
        status = support.select('board', board=target, arch='arm')
        if status:
            self.info('arm/{} is supported'.format(target), 1)
            self.analysis_manager.firmware.set_board(target)
            return True
        else:
            self.error_info = 'arm/{} is not supported yet'.format(target)
            return False

    def is_unsupport_mips_machine(self):
        exclude = [
            'boot', 'configs', 'fw', 'include', 'kernel', 'kvm', 'lib', 'mm',
            'math-emu', 'lib', 'net', 'oprofile', 'paravirt', 'pci', 'power',
            'vdso'
        ]
        target = self.find_dir_compiled(exclude=exclude)
        if target is None:
            self.error_info = \
                'no available target found, please check the source code'
            return False
        support = get_database('support')
        status = support.select('board', board=target, arch='mips')
        if status:
            self.analysis_manager.firmware.set_board(target)
            self.info('mips/{} is supported'.format(target), 1)
            return True
        else:
            self.error_info = 'mips/{} is not supported yet'.format(target)
            return False

    def run(self, **kwargs):
        srcodec = self.analysis_manager.srcodec
        if not srcodec.supported:
            self.error_info = 'please set the source code'
            return False
        self.path_to_srcode = srcodec.get_path_to_source_code()

        arch = self.analysis_manager.firmware.get_arch()
        self.arch = arch
        if arch == 'arm':
            return self.is_unsupport_arm_machine()
        elif arch == 'mips':
            return self.is_unsupport_mips_machine()
        else:
            self.error_info = 'unsupported arch {}'.format(arch)
            return False

    def __init__(self, analysis_manager):
        super().__init__(analysis_manager)
        self.name = 'bfilter'
        self.description = \
            'Filter our Linux kernels board which are supported.'
        self.required = []
        self.critical = True
        self.path_to_srcode = None
        self.arch = None
