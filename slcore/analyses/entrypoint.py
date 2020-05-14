import os

from slcore.analysis import Analysis


class EntryPoint(Analysis):
    def run(self, firmware):
        srcodec = firmware.get_srcodec()
        if srcodec is None:
            self.context['input'] = 'please set the source code'
            return False

        path_to_vmlinux = firmware.get_srcodec().get_path_to_vmlinux()

        with os.popen('readelf -h {}'.format(path_to_vmlinux)) as f:
            for line in f:
                # Entry point address:  0x800090e0
                if line.find('Entry point address') == -1:
                    continue
                ep = int(line.strip().split()[-1], 16)
                firmware.set_kernel_entry_point(hex(ep))
                self.info(firmware, 'get kernel entry point address 0x{:x} from vmlinux'.format(ep), 1)
            return True

        self.context['input'] = 'vmlinux not correct'
        return False

    def __init__(self, analysis_manager):
        super().__init__(analysis_manager)
        self.name = 'entrypoint'
        self.description = 'Resolve kernel entry point.'
        self.context['hint'] = 'problem in getting kernel entry point'
        self.critical = True
        self.required = ['bfilter']

