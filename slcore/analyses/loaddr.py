import os

from slcore.amanager import Analysis


class CalcLoadAddr(Analysis):
    def run(self, firmware):
        if firmware.get_arch() == 'arm':
            firmware.set_kernel_load_address('0x00008000')
            self.info(
                firmware,
                'get arm loading address 0x{:x} by default'.format(0x8000), 1)
            return True

        srcodec = firmware.get_srcodec()
        if srcodec is None:
            self.context['input'] = 'please set the source code'
            return False

        path_to_srcode = firmware.get_srcodec().get_path_to_source_code()
        lds_names = [
            'kernel/vmlinux.lds', 'vmlinux.lds',
            'ld.script', 'kernel/ld.script']

        for lds_name in lds_names:
            path_to_lds = os.path.join(path_to_srcode, 'arch/mips', lds_name)
            if not os.path.exists(path_to_lds):
                continue

            #  SECTIONS
            #  {
            #   . = 0xffffffff80001000;
            state = 0
            address = 0xBFC00000
            with open(path_to_lds) as f:
                for line in f:
                    if state == 0 and line.startswith('SECTIONS'):
                        state = 1
                    elif state == 1 and line.find('. = 0x') != -1:
                        address = \
                            int(line.strip().strip(';').split()[-1], 16) & 0xFFFFFFFF
                        state = 0

            firmware.set_kernel_load_address(hex(address))
            self.info(
                firmware,
                'get mips loading address 0x{:x} from lds'.format(address), 1)
            return True

        self.context['input'] = 'lds script does not exist'
        return False

    def __init__(self, analysis_manager):
        super().__init__(analysis_manager)
        self.name = 'loaddr'
        self.description = 'Resolve image loading address.'
        self.context['hint'] = 'problem in getting image loading address'
        self.required = ['bfilter']
