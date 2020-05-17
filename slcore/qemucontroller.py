"""
QEMU controller

after several experiments, I conclude
    1) QEMU is likely to be supported on Windows with extra compilation efforts
    https://stackoverflow.com/questions/53084815/compile-qemu-under-windows-10-64-bit-for-windows-10-64-bit
    which is not elegant and not easy. I hope QEMU will be officially supported on Windows in the future.
    2) Multi-processing introduces more complexity than speed increment. If you'd like to
    analyze more than one firmware at the same time, you must consider QEMU pollution(synchronization) problem.
    Modifying QEMU source code at the same time makes everything messy and embarrassing. JIT solution is
    the idealest ways to solve this problem. BTW, running in different directories looks quick and dirty but is
    really helpful. Another solution is to have a qemu controller which can lock/unlock qemu source code
    read/write and compilation.

interfaces:
    + get_command()/trace()/debug()
    + install()/patch()/add_target()/compile()/recover()
"""
import os
import qmp
import tempfile


class QEMUController(object):
    def __init__(self, qemu_root):
        self.modified = []
        self.new = []
        self.qemu_root = qemu_root
        self.build_system = {
            'arml': {
                'defconfig': 'default-configs/arm-softmmu.mak', 'kconfig': 'hw/arm/Kconfig',
                'makefile': 'hw/arm/Makefile.objs',
            },'armb': {
                'defconfig': 'default-configs/arm-softmmu.mak', 'kconfig': 'hw/arm/Kconfig',
                'makefile': 'hw/arm/Makefile.objs',
            }, 'mipsl': {
                'defconfig': 'default-configs/mipsel-softmmu.mak', 'kconfig': 'hw/mips/Kconfig',
                'makefile':  'hw/mips/Makefile.objs',
            }, 'mipsb': {
                'defconfig': 'default-configs/mips-softmmu.mak', 'kconfig': 'hw/mips/Kconfig',
                'makefile':  'hw/mips/Makefile.objs',
            }, 'intc': {
                'makefile': 'hw/intc/Makefile.objs'
            }, 'timer': {
                'makefile': 'hw/timer/Makefile.objs'
            }
        }
        if qemu_root is None:
            self.supported = False
        else:
            self.supported = True

    def __get_file_path(self, path):
        return os.path.join(self.qemu_root, path)

    def __get_binary(self, arch, endian):
        if arch == 'arm':
            if endian == 'l':
                return '{}/arm-softmmu/qemu-system-arm'.format(self.qemu_root)
            else:
                raise NotImplementedError('QEMU won\'t support ARMEB machines.')
        elif arch == 'mips':
            if endian == 'l':
                return '{}/mipsel-softmmu/qemu-system-mipsel'.format(self.qemu_root)
            else:
                return '{}/mips-softmmu/qemu-system-mips'.format(self.qemu_root)

    def get_command(
            self, arch, endian, machine, kernel, dtb_offset=None,
            initrd=None, flash=None, image=None, flash_size=None, dtb=None, n_serial=1):
        running_command = self.__get_binary(arch, endian)
        if running_command is None:
            return None

        running_command += ' -M {}'.format(machine)
        running_command += ' -kernel {}'.format(kernel)

        if dtb:
            running_command += ' -dtb {}'.format(dtb)
        if dtb_offset:
            running_command += ',offset=0x{:x}'.format(dtb_offset)

        if flash == 'nor':
            running_command += ' -drive file={},if=pflash,format=raw'.format(image)
        elif flash == 'nand':
            running_command += ' -drive file={},if=mtd,format=raw'.format(image)

        running_command += ' -nographic'
        if initrd:
            running_command += ' -initrd {}'.format(initrd)
        running_command += ' -append "console=ttyS0 nowatchdog nokaslr"'

        if n_serial > 1:
            # -chardev stdio,mux=on,id=char0 -mon chardev=char0,mode=readline -serial chardev:char0 -serial chardev:char0
            running_command += ' -chardev stdio,mux=on,id=char0'
            running_command += ' -mon chardev=char0,mode=readline'
            for i in range(0, n_serial):
                if i >= 3:
                    continue
                running_command += ' -serial chardev:char0'

        return running_command

    def patch(self, *args, **kwargs):
        """
        this function is not thread safety, combining with
        recover, it can only guarantee the patch is valid

        patch(abs/p/t/src, rel/p/t/dst, bak=True) or
        patch(abs/p/t/old, rel/p/t/new, bak=True)
        """
        src, dst = args
        dst = self.__get_file_path(dst)
        if os.path.exists(dst):
            if dst not in self.modified:
                os.system('cp {0} {0}.bak'.format(dst))
                self.modified.append(dst)
        else:
            self.new.append(dst)
        os.system('cp {} {}'.format(src, dst))
        return dst

    def install(self, prefix):
        for root, dirs, files in os.walk(prefix):
            if len(dirs):
                continue
            for f in files:
                full = os.path.join(root, f)
                target = self.patch(full, full[len(prefix)+1:])

    def recover(self, *args, **kwargs):
        """
        recover()
        """
        for dst in self.modified:
            os.system('mv {0}.bak {0}'.format(dst))
        self.modified = []
        for dst in self.new:
            os.system('rm {}'.format(dst))
        self.new = []

    def compile(self, cflags=None, cpu=4):
        if cflags:
            os.system('cd {} && make -j{} CFLAGS={} && cd $OLDPWD'.format(self.qemu_root, cpu, cflags))
        else:
            os.system('cd {} && make -j{} && cd $OLDPWD'.format(self.qemu_root, cpu))

    def trace(self, *args, **kwargs):
        raise NotImplementedError()

    def debug(self, running_cmdline, path_to_vmlinux, **kwargs):
        """
        provide a GDB interface
        running_cmdline comes from get_cmdline()
        """
        if running_cmdline is None:
            return

        d = os.path.dirname(path_to_vmlinux)
        gdb_cmdline = 'gdb-multiarch --cd={} {} -ex "target remote:1234"'.format(d, path_to_vmlinux)
        print('\nOPEN *ANOTHER* SHELL and RUN\n    {}'.format(gdb_cmdline))
        print('SEVERAL BPS YOU MAY INTERESTED IN:')
        print('    b kernel_entry # MIPS')
        print('    b start_kernel')
        print('    b setup_arch')
        print('    b prom_init # MIPS')
        print('    b prom_putchar # MIPS')
        print('    b init_IRQ')
        print('    b time_init')
        print('    b calibrate_delay')
        print('    b rest_init')
        print('    b kernel_init')
        print('    b populate_rootfs')
        print('    b run_init_process')
        print('    b panic')
        print('SOMETHING YOU NEED TO KNOW:')
        print('    calibrate_delay in start_kernel should never be stuck')
        print('    do_initcalls in do_basic_setup should never be stuck')
        print('    prepare_namespace in kernel_init_freeable should never be called')

        debug_cmdline = running_cmdline + ' -s -S'
        print('RUNNING\n    {}'.format(debug_cmdline))
        print('PRESS ctrl-a x to exit; PRESS ctrl-a c to QEMU console')
        print('In QEMU console: enter system_reset to reset')
        print('In QEMU console: enter info mtree to show memory layout')
        print('In QEMU console: enter info qtree to show device layout')
        os.system(debug_cmdline)

    def __resolve_makefile(self, path, label, content):
        """
        :param path: path to makefile, str
        :param label: label to be checked, str
        :param content: content to be extend, list
        """
        original = self.__get_file_path(path)
        with open(original) as f:
            lines = f.readlines()

        if not lines[-1].endswith('\n'):
            lines[-1] = lines[-1] + '\n'
        if label not in lines:
            lines.extend(content)

        target = os.path.join(
            tempfile.gettempdir(), os.path.basename(path))
        with open(target, 'w') as f:
            f.writelines(lines)
            f.flush()
        self.patch(target, path, bak=True)

    def add_target(self, hwname, fname, t, arch=None, endian=None):
        """
        add_target('hwname', 'hwname', t='hw', arch='arm', endian='l')
        add_target('hwname', 'fname', t='intc')

        """
        if t == 'hw':
            build_system = self.build_system['{}{}'.format(arch, endian)]
            # update defconfig
            config = 'CONFIG_{}=y\n'.format(hwname.upper())
            path = os.path.join(build_system['defconfig'])
            content = [config]
            target = self.__resolve_makefile(path, config, content)
            # update kconfig
            kconfig = 'config {}\n'.format(hwname.upper())
            path = os.path.join(build_system['kconfig'])
            content = ['\n', kconfig, '    bool\n']
            target = self.__resolve_makefile(path, kconfig, content)
            # update makefile
            makefile = 'obj-$(CONFIG_{}) += {}.o\n'.format(hwname.upper(), fname)
            path = os.path.join(build_system['makefile'])
            content = [makefile]
            target = self.__resolve_makefile(path, makefile, content)
        # elif t in ['intc', 'timer']:
        else:
            build_system = self.build_system[t]
            makefile = 'obj-$(CONFIG_{}) += {}.o\n'.format(hwname.upper(), fname)
            path = os.path.join(build_system['makefile'])
            content = [makefile]
            target = self.__resolve_makefile(path, makefile, content)


def get_qemucontroller(qemu_root):
    return QEMUController(qemu_root)
