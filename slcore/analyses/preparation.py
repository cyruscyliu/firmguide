from slcore.generation.compilerf import get_compiler
from slcore.compositor import pack_kernel, pack_image, \
    pack_initramfs, fix_cmdline, fix_choosen_bootargs
from slcore.generation.dt_renderer import DTRenderer
from slcore.generation.common import to_upper
from slcore.analyses.analysis import Analysis
from settings import *


class Preparation(Analysis):
    def run(self, firmware):

        # 1. generate code(render in multi-levels)
        # compiler only link files locally
        # 1.1 the old fashion
        if firmware.get_dtb() is None:
            machine_compiler = get_compiler(firmware)
            machine_compiler.compile()
            machine_compiler.link()
        # 1.2 the latest dt_renderer
        else:
            if firmware.get_components().get_path_to_dtb() is not None:
                firmware.set_dtb(firmware.get_components().get_path_to_dtb())
            dt_renderer = DTRenderer(firmware)
            dt_renderer.load_template()
            status = dt_renderer.render()
            if not status:
                raise NotImplementedError('error in dt rendering')

        # 2. install and make(compile qemu)
        if not firmware.cancle_compilation:
            # 2.1 the old fashion
            if firmware.get_dtb() is None:
                prefix = os.path.join(firmware.get_target_dir(), 'qemu-4.0.0')
                for root, dirs, files in os.walk(prefix):
                    if len(dirs):
                        continue
                    for f in files:
                        full = os.path.join(root, f)
                        target = firmware.qemuc.patch(full, full[len(prefix)+1:])
                        self.debug(firmware, 'install {} at {}'.format(f, target), 'install')
                firmware.qemuc.add_target(
                    to_upper(firmware.get_machine_name()), (firmware.get_machine_name()),
                    t='hw', arch=firmware.get_arch(), endian=firmware.get_endian())
                if machine_compiler.has_sintc():
                    firmware.qemuc.add_target(
                        to_upper(firmware.get_machine_name()), 'sintc', t='intc')
                firmware.qemuc.compile(cflags='-Wmaybe-uninitialized', cpu=4)
                # guarentee qemu is clean
                firmware.qemuc.recover()
            # 2.2 the latest dt_renderer
            else:
                # 6.1 copy files to qemu/
                prefix = os.path.join(firmware.get_target_dir(), 'qemu-4.0.0')
                firmware.qemuc.install(prefix)
                # 6.2 update compilation targets
                firmware.qemuc.add_target(
                    (firmware.get_machine_name()), firmware.get_machine_name(),
                    t='hw',arch=firmware.get_arch(), endian=firmware.get_endian())
                for k, v in dt_renderer.external.items():
                    firmware.qemuc.add_target((firmware.get_machine_name()), k, t=v['type'])
                # 6.3 compile
                firmware.qemuc.compile(cflags='-Wmaybe-uninitialized', cpu=4)
                # 6.4 keep qemu clean
                # firmware.qemuc.recover()

        # 3. prepare -k path/to/kernel
        # 3.1 If a mips firmware has CMDLINE: filled, it will use our customed cmdline.
        fix_cmdline(firmware.get_components())
        # 3.1 If a firmware has console=ttyS0,115200, then remove it
        fix_choosen_bootargs(firmware.get_components())
        # 3.2 add a uimage header on the kernel image
        load_address = firmware.get_kernel_load_address()
        if firmware.get_arch() == 'arm':
            entry_point = load_address
        else:
            entry_point = firmware.get_kernel_entry_point()
        # Why we don't use vmlinux if any?
        # ARM32 has two head.S, the one is in side of the vmlinux
        # the other is outside of the vmlinux. Due to historical
        # reasons, some critical code related to page tables is
        # put in the outside head.s, so we cannot use vmlinux directly
        # MIPS has built-in device tree patched in a later stage. That
        # is to say, the vmlinux has a empty built-in device tree. If
        # we use the vmlinux, we will get it crashed.
        kernel = pack_kernel(
            firmware.get_components(), load_address=load_address,
            entry_point=entry_point, arch=firmware.get_arch())

        # 4. prepare -initrd path/to/cpio
        path_to_initramfs = \
            os.path.join(BASE_DIR, 'examples/rootfs/{}e{}.cpio.rootfs'.format(
                firmware.get_arch(), firmware.get_endian()))
        path_to_initramfs = pack_initramfs(
            firmware.get_components(), mounted_to=path_to_initramfs)
        running_command = firmware.qemuc.get_command(
            firmware.get_arch(), firmware.get_endian(), firmware.get_machine_name(),
            kernel, initrd=path_to_initramfs, dtb=firmware.get_components().get_path_to_dtb(),
            n_serial=firmware.get_uart_num()
        )
        self.debug(firmware, 'get command: {}'.format(running_command), 1)
        firmware.running_command = running_command

        return True

    def __init__(self, analysis_manager):
        super().__init__(analysis_manager)
        self.name = 'preparation'
        self.description = 'generate qemu code from profile'
        self.context['hint'] = 'some properties are not satisfied'
        self.critical = True
        self.required = ['preprocdt', 'initvalue']
        self.type = 'diag'

