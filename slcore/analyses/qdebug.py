import os

from slcore.amanager import Analysis


class QEMUDbgMachSrc(Analysis):
    def run(self, **kwargs):
        clean = kwargs.pop('clean')

        prefix_from = os.path.join(
            self.analysis_manager.project.attrs['path'], 'qemu-4.0.0')
        prefix_to = self.analysis_manager.project.attrs['qemu_dir']

        if not clean:
            # copy files to qemu/
            cwd = os.getcwd()
            os.chdir(prefix_from)
            for rt, ds, fs, in os.walk('.'):
                for f in fs:
                    f_from = os.path.join(prefix_from, rt, f)
                    f_to = os.path.join(prefix_to, rt, f)
                    status = os.system('cp {} {}'.format(f_from, f_to))
                    if not status:
                        self.info('copy {}'.format(f_to), 1)
            os.chdir(cwd)
        else:
            # delete files in qemu/
            cwd = os.getcwd()
            os.chdir(prefix_from)
            for rt, ds, fs, in os.walk('.'):
                for f in fs:
                    # f_from = os.path.join(prefix_from, rt, f)
                    f_to = os.path.join(prefix_to, rt, f)
                    status = os.system('rm {}'.format(f_to))
                    if not status:
                        self.info('remove {}'.format(f_to), 1)
            os.chdir(cwd)
        return True

    def __init__(self, analysis_manager):
        super().__init__(analysis_manager)
        self.name = 'qdebug'
        self.description = 'Add and delete machine source for debugging QEMU.'
        self.critical = True
        self.required = []
        self.type = 'diag'
