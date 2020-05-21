import os

from slcore.amanager import Analysis


class Install(Analysis):
    def run(self, **kwargs):
        nocompilation = kwargs.pop('nocompilation', True)
        if nocompilation:
            self.info('don\'t install and compile this new machine', 0)
            return True

        synthesisdt = self.analysis_manager.get_analysis('synthesisdt')
        # 1 copy files to qemu/
        prefix = os.path.join(
            self.analysis_manager.project.attrs['path'], 'qemu-4.0.0')
        self.analysis_manager.qemuc.install(prefix)
        self.info('install {}'.format(prefix), 1)
        # 2 update compilation targets
        self.analysis_manager.qemuc.add_target(
            self.firmware.get_machine_name(), self.firmware.get_machine_name(),
            t='hw', arch=self.firmware.get_arch(), endian=self.firmware.get_endian())
        for k, v in synthesisdt.external.items():
            self.analysis_manager.qemuc.add_target(
                self.firmware.get_machine_name(), k, t=v['type'])
        # 3 compile
        self.analysis_manager.qemuc.compile(
            cflags='-Wmaybe-uninitialized', cpu=4)
        # 4 keep qemu clean
        self.analysis_manager.qemuc.recover()
        return True

    def __init__(self, analysis_manager):
        super().__init__(analysis_manager)
        self.name = 'install'
        self.description = 'Install and compile QEMU machine.'
        self.critical = True
        self.required = ['preprocdt', 'synthesisdt']
        self.type = 'diag'
