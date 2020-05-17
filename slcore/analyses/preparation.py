import os

# from slcore.generation.compilerf import get_compiler
from slcore.compositor import pack_kernel, fix_smp, \
    pack_initramfs, fix_cmdline, fix_builtin_dtb, fix_armdtb
# from slcore.generation.dt_renderer import DTRenderer
# from slcore.generation.common import to_upper
from slcore.amanager import Analysis
from rootfs.rootfs import get_initramfs


class Preparation(Analysis):
    def run(self, **kwargs):
        nocompilation = kwargs.pop('nocompilation', True)
        # if not nocompilation:
            # # 1. generate code(render in multi-levels)
            # # compiler only link files locally
            # # 1.1 the old fashion
            # if self.firmware.get_dtb() is None:
                # machine_compiler = get_compiler(self.firmware)
                # # machine_compiler.compile()
                # machine_compiler.link()
            # # 1.2 the latest dt_renderer
            # else:
                # if self.firmware.get_components().get_path_to_dtb() is not None:
                    # self.firmware.set_dtb(self.firmware.get_components().get_path_to_dtb())
                # dt_renderer = DTRenderer(self.firmware)
                # dt_renderer.load_template()
                # # status = dt_renderer.render()
                # if not status:
                    # raise NotImplementedError('error in dt rendering')
            # # 2. install and make(compile qemu)
            # # 2.1 the old fashion
            # if self.firmware.get_dtb() is None:
                # prefix = os.path.join(self.firmware.get_target_dir(), 'qemu-4.0.0')
                # for root, dirs, files in os.walk(prefix):
                    # if len(dirs):
                        # continue
                    # for f in files:
                        # full = os.path.join(root, f)
                        # target = self.firmware.qemuc.patch(full, full[len(prefix)+1:])
                        # self.debug('install {} at {}'.format(f, target), 'install')
                # self.firmware.qemuc.add_target(
                    # to_upper(self.firmware.get_machine_name()), (self.firmware.get_machine_name()),
                    # t='hw', arch=self.firmware.get_arch(), endian=self.firmware.get_endian())
                # if machine_compiler.has_sintc():
                    # self.firmware.qemuc.add_target(
                        # to_upper(self.firmware.get_machine_name()), 'sintc', t='intc')
                # self.firmware.qemuc.compile(cflags='-Wmaybe-uninitialized', cpu=4)
                # # guarentee qemu is clean
                # self.firmware.qemuc.recover()
            # # 2.2 the latest dt_renderer
            # else:
                # # 6.1 copy files to qemu/
                # prefix = os.path.join(self.firmware.get_target_dir(), 'qemu-4.0.0')
                # self.firmware.qemuc.install(prefix)
                # # 6.2 update compilation targets
                # self.firmware.qemuc.add_target(
                    # (self.firmware.get_machine_name()), self.firmware.get_machine_name(),
                    # t='hw',arch=self.firmware.get_arch(), endian=self.firmware.get_endian())
                # for k, v in dt_renderer.external.items():
                    # self.firmware.qemuc.add_target((self.firmware.get_machine_name()), k, t=v['type'])
                # # 6.3 compile
                # self.firmware.qemuc.compile(cflags='-Wmaybe-uninitialized', cpu=4)
                # 6.4 keep qemu clean
                # self.firmware.qemuc.recover()

        # 3. prepare -k path/to/kernel
        if self.firmware.get_arch() == 'mips':
            # 3.1 If a mips firmware has CMDLINE label,
            # we replace what after CMDLINE with our cmdline.
            fix_cmdline(self.firmware.get_components())
            # 3.3 find the builtin dtb
            offset = fix_builtin_dtb(self.firmware.get_components())
        elif self.firmware.get_arch() == 'arm':
            # 3.3 If an arm firmware has a built-in dtb, disable it.
            fix_armdtb(self.firmware.get_components(), self.firmware.get_realdtb())
            offset = None
        # 3.4 we cannot handle SMP
        fix_smp(self.firmware.get_components())
        # 3.2 add a uimage header on the kernel image
        load_address = self.firmware.get_kernel_load_address()
        if self.firmware.get_arch() == 'arm':
            entry_point = load_address
        else:
            # entry_point = firmware.get_kernel_entry_point()
            # we move our metadata to a higher place, so maybe
            # 0x80000000 is safe, sometimes a specific
            # entry point is not such universal
            entry_point = '0x80000000'
        # Why we don't use vmlinux if any?
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

        # 4. prepare -initrd path/to/cpio
        path_to_initramfs = get_initramfs(
            self.firmware.get_arch(), self.firmware.get_endian())
        path_to_initramfs = pack_initramfs(
            self.firmware.get_components(), mounted_to=path_to_initramfs)
        running_command = self.analysis_manager.qemuc.get_command(
            self.firmware.get_arch(), self.firmware.get_endian(),
            self.firmware.get_machine_name(), kernel, initrd=path_to_initramfs,
            dtb=self.firmware.get_components().get_path_to_dtb(),
            n_serial=self.firmware.get_uart_num(), dtb_offset=offset,
        )
        self.debug('get command: {}'.format(running_command), 1)
        self.firmware.running_command = running_command

        return True

    def __init__(self, analysis_manager):
        super().__init__(analysis_manager)
        self.name = 'preparation'
        self.description = 'Prepare to boot the image.'
        self.critical = True
        self.required = ['preprocdt']
        self.type = 'diag'
