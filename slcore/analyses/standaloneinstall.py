import os

from slcore.amanager import Analysis


class StandaloneInstall(Analysis):
    def run(self, **kwargs):
        if not self.analysis_manager.qemuc.supported:
            self.error_info = 'please setup the QEMU'
            return False

        machine_name = kwargs.pop('machine_name')
        machine_source = os.path.realpath(kwargs.pop('machine_source'))
        if machine_name is None:
            machine_name = os.path.basename(machine_source)
        arch = kwargs.pop('arch')
        if arch is None:
            self.error_info = "please set the architecture"
            return False
        endian = kwargs.pop('endian')
        if endian is None:
            self.error_info = "please set the endianness"
            return False

        # 1 copy files to qemu/
        prefix = machine_source
        self.analysis_manager.qemuc.install(prefix)
        self.info('install {}'.format(prefix), 1)
        # 2 update compilation targets
        for k_dot_c in os.listdir(os.path.join(machine_source, 'hw', arch)):
            k = k_dot_c[:-2]
            self.analysis_manager.qemuc.add_target(
                machine_name, k, 'hw', arch=arch, endian=endian)
        for t in os.listdir(os.path.join(machine_source, 'hw')):
            if t == arch:
                continue
            for k_dot_c in os.listdir(os.path.join(machine_source, 'hw', t)):
                k = k_dot_c[:-2]
                self.analysis_manager.qemuc.add_target(machine_name, k, t)
        # 3 compile
        self.analysis_manager.qemuc.compile()
        # 4 keep qemu clean
        self.analysis_manager.qemuc.recover()
        return True

    def __init__(self, analysis_manager):
        super().__init__(analysis_manager)
        self.name = 'standaloneinstall'
        self.description = 'Install and compile QEMU machine standalone.'
        self.critical = True
        self.required = []
