import os

from analyses.analysis import Analysis


class LoadAddr(Analysis):
    def run(self, firmware):
        if firmware.get_architecture() == 'arm':
            firmware.set_kernel_load_address('0x00008000')
            return True

        path_to_srcode = firmware.get_path_to_source_code()
        lds_names = ['kernel/vmlinux.lds', 'vmlinux.lds', 'ld.script', 'kernel/ld.script']

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
                        address = int(line.strip().strip(';').split()[-1], 16) & 0xFFFFFFFF
                        state = 0

            kernel = firmware.get_path_to_kernel()
            uimage = firmware.get_path_to_uimage()
            firmware.set_kernel_load_address(hex(address))
            os.system('mkimage -A mips -C none -O linux -T kernel -d {0} '
                      '-a 0x{1:x} -e 0x{1:x} {2} >/dev/null 2>&1'.format(kernel, address, uimage))
            self.info(firmware, 'get mips loading address 0x{:x} from lds'.format(address), 1)
            return True

        self.context['input'] = 'lds script does not exist'
        return False

    def __init__(self, analysis_manager):
        super().__init__(analysis_manager)
        self.name = 'loaddr'
        self.description = 'resolve mips image loading address'
        self.context['hint'] = 'problem in getting mips image loading address'
        self.critical = False
        self.required = ['srcode']
