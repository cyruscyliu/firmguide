from slcore.generation.compilerf import get_compiler
from slcore.compositor import pack_kernel, pack_image, pack_initramfs, fix_cmdline
from slcore.generation.common import to_upper
from analyses.analysis import Analysis
from settings import *


class Preparation(Analysis):
    def run(self, firmware):
        machine_compiler = get_compiler(firmware)
        # TODO detouch qemuc from compiler
        # compiler only link files locally

        # 1. generate code(render in multi-levels)
        machine_compiler.compile()
        machine_compiler.link()

        # 2. install and make(compile qemu)
        prefix = os.path.join(firmware.get_target_dir(), 'qemu-4.0.0')
        for root, dirs, files in os.walk(prefix):
            if len(dirs):
                continue
            for f in files:
                full = os.path.join(root, f)
                target = firmware.qemuc.patch(full, full[len(prefix)+1:])
                self.debug(firmware, 'install {} at {}'.format(f, target), 'install')
        firmware.qemuc.add_target(
            to_upper(firmware.get_machine_name()), type_='hw', arch=firmware.get_arch(), endian=firmware.get_endian())
        if machine_compiler.has_sintc():
            firmware.qemuc.add_target(
                to_upper(firmware.get_machine_name()), type_='sintc')
        firmware.qemuc.compile(cflags='-Wmaybe-uninitialized', cpu=4)

        # 3. prepare -k path/to/kernel
        # 3.1 If a mips firmware has CMDLINE: filled, it will not use our customed cmdline.
        fix_cmdline(firmware.get_components())
        # 3.2 add a uimage header on the kernel image
        load_address = firmware.get_kernel_load_address()
        if firmware.get_srcodec():
            # we use vmlinux if any
            if firmware.get_arch() == 'arm':
                # ARM32 has two head.S, the one is in side of the vmlinux
                # the other is outside of the vmlinux. Due to historical
                # reasons, some critical code related to page tables is
                # put in the outside head.s, so we cannot use vmlinux directly
                kernel = pack_kernel(
                    firmware.get_components(), load_address=load_address, arch='arm')
            else:
                kernel = firmware.get_srcodec().get_path_to_vmlinux()
        else:
            kernel = pack_kernel(
                firmware.get_components(), load_address=load_address, arch=firmware.get_arch())

        # 4. prepare -initrd path/to/cpio
        path_to_initramfs = \
            os.path.join(BASE_DIR, 'examples/rootfs/{}.cpio.rootfs'.format(firmware.get_arch()))
        path_to_initramfs = pack_initramfs(
            firmware.get_components(), mounted_to=path_to_initramfs)
        running_command = firmware.qemuc.get_command(
            firmware.get_arch(), firmware.get_endian(), firmware.get_machine_name(),
            kernel, initrd=path_to_initramfs, dtb=firmware.get_components().get_path_to_dtb()
        )
        self.debug(firmware, 'get command: {}'.format(running_command), 1)
        firmware.running_command = running_command

        # guarentee qemu is clean
        firmware.qemuc.recover()

        return True

    def __init__(self, analysis_manager):
        super().__init__(analysis_manager)
        self.name = 'preparation'
        self.description = 'generate qemu code from profile'
        self.context['hint'] = 'some properties are not satisfied'
        self.critical = True
        self.required = []
        self.type = 'diag'

