import os

from slcore.amanager import Analysis


class Install(Analysis):
    def run(self, **kwargs):
        if not self.analysis_manager.qemuc.supported:
            self.error_info = 'please setup the QEMU'
            return False
        nocompilation = kwargs.pop('nocompilation', True)
        if nocompilation:
            self.info('don\'t install and compile this new machine', 0)
            return True

        synthesisdt = self.analysis_manager.get_analysis('synthesisdt')
        # 1 copy files to qemu/
        prefix = os.path.join(
            self.analysis_manager.project.attrs['path'],
            self.analysis_manager.firmware.get_machine_name())
        self.analysis_manager.qemuc.install(prefix)
        self.info('install {}'.format(prefix), 1)
        # 2 update compilation targets
        self.analysis_manager.qemuc.add_target(
            self.analysis_manager.firmware.get_machine_name(), self.analysis_manager.firmware.get_machine_name(),
            t='hw', arch=self.analysis_manager.firmware.get_arch(), endian=self.analysis_manager.firmware.get_endian())
        for k, v in synthesisdt.external.items():
            self.analysis_manager.qemuc.add_target(
                self.analysis_manager.firmware.get_machine_name(), k, t=v['type'])
        # 3 compile
        self.analysis_manager.qemuc.compile()
        # 4 keep qemu clean
        self.analysis_manager.qemuc.recover()
        return True

    def __init__(self, analysis_manager):
        super().__init__(analysis_manager)
        self.name = 'install'
        self.description = 'Install and compile QEMU machine.'
        self.critical = True
        self.required = ['preprocdt', 'synthesisdt']
