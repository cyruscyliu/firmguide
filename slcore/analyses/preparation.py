from slcore.compositor import pack_kernel, fix_smp, \
    pack_initramfs, fix_cmdline, fix_builtin_dtb, fix_armdtb
from slcore.amanager import Analysis
from rootfs.rootfs import get_initramfs


class Preparation(Analysis):
    def run(self, **kwargs):
        # 1. prepare -k path/to/kernel
        if self.firmware.get_arch() == 'mips':
            # 1.1 If a mips firmware has CMDLINE label,
            # we replace what after CMDLINE with our cmdline.
            fix_cmdline(self.firmware.get_components())
            # 1.2 find the builtin dtb
            offset = fix_builtin_dtb(self.firmware.get_components())
        elif self.firmware.get_arch() == 'arm':
            # 1.2 If an arm firmware has a built-in dtb, disable it.
            fix_armdtb(
                self.firmware.get_components(), self.firmware.get_realdtb())
            offset = None
        # 1.3 we cannot handle SMP
        saved_dtb = self.firmware.get_components().get_path_to_dtb()
        self.firmware.get_components().set_path_to_dtb(
            self.firmware.get_realdtb())
        fix_smp(self.firmware.get_components())
        self.firmware.get_components().set_path_to_dtb(saved_dtb)
        # 1.4 add a uimage header on the kernel image
        if self.firmware.get_arch() == 'arm':
            entry_point = '0x00008000'
        else:
            # we move our metadata to a higher place, so maybe
            # 0x80000000 is safe, sometimes a specific
            # entry point is not such universal
            entry_point = '0x80000000'
        load_address = self.firmware.get_kernel_load_address()
        if load_address is None:
            self.error_info = 'there is no loading address'
            return False
        # 2 Why we don't use vmlinux if any?
        # ARM32 has two head.S, the one is in side of the vmlinux
        # the other is outside of the vmlinux. Due to historical
        # reasons, some critical code related to page tables is
        # put in the outside head.s, so we cannot use vmlinux directly
        # MIPS has built-in device tree patched in a later stage. That
        # is to say, the vmlinux has a empty built-in device tree. If
        # we use the vmlinux, we will get it crashed.
        kernel = pack_kernel(
            self.firmware.get_components(), load_address=load_address,
            entry_point=entry_point, arch=self.firmware.get_arch())
        self.info('repack kernel with {}/{}/{}'.format(
            self.firmware.get_arch(), load_address, entry_point), 1)

        # 4. prepare -initrd path/to/cpio
        path_to_initramfs = get_initramfs(
            self.firmware.get_arch(), self.firmware.get_endian())
        path_to_initramfs = pack_initramfs(
            self.firmware.get_components(), mounted_to=path_to_initramfs)
        running_command = self.analysis_manager.qemuc.get_command(
            self.firmware.get_arch(), self.firmware.get_endian(),
            self.firmware.get_machine_name(), kernel, initrd=path_to_initramfs,
            dtb=self.firmware.get_realdtb(),
            n_serial=self.firmware.get_uart_num(), dtb_offset=offset,
        )
        self.info('get command: {}'.format(running_command), 1)
        self.firmware.running_command = running_command

        return True

    def __init__(self, analysis_manager):
        super().__init__(analysis_manager)
        self.name = 'preparation'
        self.description = 'Prepare to boot the image.'
        self.critical = True
        self.required = ['preprocdt', 'synthesisdt', 'loaddr']
        self.type = 'diag'
