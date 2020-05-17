import os

from slcore.amanager import Analysis


class EntryPoint(Analysis):
    def run(self, **kwargs):
        srcodec = self.analysis_manager.srcodec
        if not srcodec.supported:
            self.error_info = 'please set the source code'
            return False

        path_to_vmlinux = srcodec.get_path_to_vmlinux()

        with os.popen('readelf -h {}'.format(path_to_vmlinux)) as f:
            for line in f:
                # Entry point address:  0x800090e0
                if line.find('Entry point address') == -1:
                    continue
                ep = int(line.strip().split()[-1], 16)
                self.firmware.set_kernel_entry_point(hex(ep))
                self.info('get kernel entry point address 0x{:x} from vmlinux'.format(ep), 1)
            return True

        self.error_info = 'vmlinux not correct'
        return False

    def __init__(self, analysis_manager):
        super().__init__(analysis_manager)
        self.name = 'entrypoint'
        self.description = 'Resolve kernel entry point.'
        self.critical = True
        self.required = ['bfilter']
