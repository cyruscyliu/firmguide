import os

from slcore.amanager import Analysis


class CalcLoadAddr(Analysis):
    def run(self, **kwargs):
        srcodec = self.analysis_manager.srcodec
        if not srcodec.supported:
            self.error_info = 'please set the source code'
            return False

        path_to_srcode = srcodec.get_path_to_source_code()
        lds_names = [
            'kernel/vmlinux.lds', 'vmlinux.lds',
            'ld.script', 'kernel/ld.script']
        archs = ['arm', 'mips']

        def get_target(lds_names, archs):
            for lds_name in lds_names:
                for arch in archs:
                    yield arch, os.path.join(path_to_srcode, 'arch/{}'.format(arch), lds_name)

        for arch, target in get_target(lds_names, archs):
            if not os.path.exists(target):
                continue

            #  SECTIONS
            #  {
            #   . = 0xffffffff80001000;
            state = 0
            address = 0xBFC00000
            with open(target) as f:
                for line in f:
                    if state == 0 and line.startswith('SECTIONS'):
                        state = 1
                    elif state == 1 and line.find('. = 0x') != -1:
                        address = \
                            int(line.strip().strip(';').split()[-1], 16) & \
                            0xFFFFFFFF
                        state = 0
            self.analysis_manager.firmware.set_kernel_load_address(hex(address))
            self.info('get {} loading address 0x{:x} from lds'.format(arch, address), 1)
            return True

        self.error_info = 'lds script does not exist'
        return False

    def __init__(self, analysis_manager):
        super().__init__(analysis_manager)
        self.name = 'loaddr'
        self.description = 'Find load address.'
        self.required = []
        self.critical = True
