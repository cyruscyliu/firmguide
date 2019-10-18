import os
import abc

from generation.generations.common import to_state, to_mmio, to_ops, indent, to_type, to_read, to_write, to_update, \
    to_header, to_upper, to_cpu_pp_state, to_cpu_pp_type


class CompilerToQEMU(object):
    def __init__(self):
        self.license = ['/* \n * automatically generated, don\'t change\n */\n']
        self.source = None
        self.header = None
        self.location = {
            'root': '../../build/qemu-4.0.0',
            'machine': {'arm': 'hw/arm', 'mips': 'hw/mips'},
            'configs': {'arm': 'default-configs/arm-softmmu.mak', 'mips': 'default-configs/mipsel-softmmu.mak'},
            'kconfig': {'arm': 'hw/arm/Kconfig', 'mips': 'hw/mips/Kconfig'},
            'makefile': {'arm': 'hw/arm/Makefile.objs', 'mips': 'hw/mips/Makefile.objs'}
        }

    @staticmethod
    def render_lines(lines):
        lines_ = []
        for line in lines:
            lines_.append(line + '\n')
        return lines_

    @staticmethod
    def render_includings(lines):
        """
        example: ['a.h', 'b.h', 'c.h']
        """
        lines_ = []
        for line in lines:
            lines_.append('#include "{}"\n'.format(line))
        return lines_

    @staticmethod
    def render_function(function):
        """
        example: {'signature': ['void a()'], 'declaration': ['    int a = 0;'],
                'body': ['    a = 1;', '    return;']}
        """
        lines = []
        lines.extend(function['signature'])
        lines.append('\n{\n')
        for line in function['declaration']:
            lines.append(line + '\n')
        if len(function['declaration']) and len(function['body']):
            lines.append('\n')
        for line in function['body']:
            lines.append(line + '\n')
        lines.append('}\n')
        return lines

    @staticmethod
    def render_struct(struct):
        lines = [struct['declaration'][0], '\n']
        for line in struct['fields']:
            lines.append(line + '\n')
        lines.append(struct['declaration'][1] + '\n')
        return lines

    @staticmethod
    def render_structure(structure):
        lines = [structure['declaration'][0], ' = {\n']
        for line in structure['values']:
            lines.append(line + '\n')
        lines.append('};\n')
        return lines

    def solve_makefile(self, firmware):
        machine_name = firmware.sget_machine_name()
        architecture = firmware.sget_architecture()
        #
        config = 'CONFIG_{}=y\n'.format(to_upper(machine_name))
        with open(os.path.join(self.location['root'], self.location['configs'][architecture])) as f:
            configs = f.readlines()
        if config not in configs:
            configs.append(config)
        with open(os.path.join(self.location['root'], self.location['configs'][architecture]), 'w') as f:
            f.writelines(configs)
            f.flush()
        #
        kconfig = 'config {}\n'.format(to_upper(machine_name))
        with open(os.path.join(self.location['root'], self.location['kconfig'][architecture])) as f:
            kconfigs = f.readlines()
        if kconfig not in kconfigs:
            kconfigs.extend(['\n', kconfig, '    bool\n'])
        with open(os.path.join(self.location['root'], self.location['kconfig'][architecture]), 'w') as f:
            f.writelines(kconfigs)
            f.flush()
        #
        makefile = 'obj-$(CONFIG_{}) += {}.o\n'.format(to_upper(machine_name), machine_name)
        with open(os.path.join(self.location['root'], self.location['makefile'][architecture])) as f:
            makefiles = f.readlines()
        if makefile not in makefiles:
            makefiles.append(makefile)
        with open(os.path.join(self.location['root'], self.location['makefile'][architecture]), 'w') as f:
            f.writelines(makefiles)
            f.flush()

    @abc.abstractmethod
    def solve(self, firmware):
        pass

    @abc.abstractmethod
    def link(self, firmware):
        pass

    def install(self, firmware):
        machine_name = firmware.sget_machine_name()
        architecture = firmware.sget_architecture()
        source_target = os.path.join(
            self.location['root'], self.location['machine'][architecture], machine_name + '.c')
        with open(source_target, 'w') as f:
            f.write(self.source)
            f.flush()

    def run(self, firmware):
        architecture = firmware.sget_architecture()
        machine_name = firmware.sget_machine_name()
        path_to_kernel = firmware.sget_path_to_kernel()
        if architecture == 'arm':
            print('./configure --target-list=arm-softmmu')
        print('make -j4')
        if architecture == 'arm':
            print('qemu-system-arm -M {} -kernel {}'.format(machine_name, path_to_kernel, ))


class CompilerToQEMUMachine(CompilerToQEMU):

    def solve(self, firmware):
        self.solve_machine_includings(firmware)
        self.solve_machine_defines(firmware)
        self.solve_machine_struct(firmware)
        self.solve_machine_init(firmware)
        self.solve_machine_class_init(firmware)
        self.solve_define_machine(firmware)
        self.solve_makefile(firmware)

    def __init__(self):
        super().__init__()
        self.machine = {'includings': [], 'defines': [], 'define_machine': []}
        self.machine_mmio_ops = []
        self.machine_reset = {'signature': [], 'declaration': [], 'body': []}
        self.machine_struct = {'declaration': [], 'fields': []}
        self.machine_class_init = {'signature': [], 'declaration': [], 'body': []}
        self.machine_init = {'signature': [], 'declaration': [], 'body': []}

    def solve_machine_struct(self, firmware):
        machine_name = firmware.sget_machine_name()
        self.machine_struct['declaration'].extend([
            'typedef struct {} {{'.format(to_state(machine_name)), '}} {};'.format(to_state(machine_name))
        ])

    def solve_machine_defines(self, firmware):
        machine_name = firmware.sget_machine_name()
        self.machine['defines'].extend([
            '#define {} "{}"'.format(to_type(machine_name), machine_name),
            '#define {}(obj) \\\n    OBJECT_CHECK({}, (obj), {})'.format(
                machine_name.upper(), to_state(machine_name), to_type(machine_name))
        ])

    def solve_machine_includings(self, firmware):
        self.machine['includings'].extend(['qemu/osdep.h'])
        self.machine['includings'].extend(['qemu/log.h'])
        self.machine['includings'].extend(['hw/sysbus.h'])

    def solve_abelia_devices(self, firmware):
        # cpu
        architecture = firmware.sget_architecture()
        if architecture == 'arm':
            self.machine['includings'].extend(['target/arm/cpu-qom.h'])
            self.machine_struct['fields'].extend([indent('ARMCPU *cpu;', 1)])
            self.machine_init['body'].extend([
                indent('s->cpu = ARM_CPU(object_new(machine->cpu_type));')
            ])
        elif architecture == 'mips':
            self.machine_struct['fields'].extend([indent('MIPSCPU *cpu;', 1)])
            self.machine_init['body'].extend([indent('s->cpu = MIPS_CPU(object_new(machine->default_cpu_type));')])
        else:
            raise NotImplementedError()
        self.machine_init['body'].extend([
            indent('object_property_set_bool(OBJECT(s->cpu), true, "realized", &err);', 1)])
        # cpu_pp
        cpu_model = firmware.sget_cpu_model()
        cpu_pp_model = firmware.probe_cpu_pp_model()
        if cpu_pp_model is not None:
            cpu_pp_mmio_base = firmware.sget_cpu_pp_mmio_base()
            self.machine['includings'].extend(['hw/cpu/arm11mpcore.h'])
            self.machine_struct['fields'].extend([indent('{} cpu_pp;'.format(to_cpu_pp_state(cpu_model)), 1)])
            self.machine_init['body'].extend([
                indent('object_initialize(&s->cpu_pp, sizeof(s->cpu), {});'.format(to_cpu_pp_type(cpu_model))),
                indent('object_property_set_bool(OBJECT(&s->cpu_pp), true, "realized", &err);', 1),
                indent('sysbus_mmio_map(SYS_BUS_DEVICE(&s->cpu_pp), 0, {});'.format(cpu_pp_mmio_base), 1)
            ])
        # ram
        self.machine['includings'].extend(['exec/address-spaces.h'])
        self.machine_struct['fields'].extend([indent('MemoryRegion ram;', 1)])
        self.machine_init['body'].extend([
            indent('memory_region_allocate_system_memory(&s->ram, OBJECT(machine), "ram", machine->ram_size);'),
            indent('memory_region_add_subregion_overlap(get_system_memory(), 0, &s->ram, -1);'),
        ])
        # uart
        uart_mmio_base = firmware.sget_uart_mmio_base()
        self.machine['includings'].extend(['hw/char/serial.h'])
        self.machine_init['body'].extend([
            indent('serial_mm_init(get_system_memory(), {}, 0, qdev_get_gpio_in(DEVICE(&s->cpu_pp), 23), '
                   '115200, serial_hd(0), DEVICE_LITTLE_ENDIAN);'.format(uart_mmio_base))
        ])
        # flash
        flash_type = firmware.sget_flash_type()
        self.machine['includings'].extend(['sysemu/blockdev.h', 'hw/block/flash.h'])
        self.machine_init['declaration'].extend([indent('DriveInfo *dinfo;', 1)])
        if flash_type == 'nor':
            flash_base = firmware.sget_flash_base()
            flash_size = firmware.sget_flash_size()
            flash_section_size = firmware.sget_flash_section_size()
            self.machine_init['body'].extend([
                indent('dinfo = drive_get(IF_PFLASH, 0, 0);', 1),
                indent('pflash_cfi01_register({}, "flash", {}, dinfo ? blk_by_legacy_dinfo(dinfo): NULL, '
                       '{}, 4, 0, 0, 0, 0, 0);'.format(flash_base, flash_size, flash_section_size), 1)
            ])
        elif flash_type == 'nand':
            self.machine_init['body'].extend([
                indent('dinfo = drive_get(IF_MTD, 0, 0);', 1),
                indent('nand_init(dinfo ? blk_by_legacy_dinfo(dinfo): NULL, 0xec, 0x73);')
            ])
        else:
            raise NotImplementedError()

    def solve_bamboo_devices(self, firmware):
        machine_name = firmware.sget_machine_name()
        #
        self.machine_reset['signature'].extend(['static void {}_reset(void *opaque)'.format(machine_name)])
        self.machine_reset['declaration'].extend([indent('{} *s = opaque;'.format(to_state(machine_name)), 1)])
        #
        bamboos = firmware.lget_bamboo_devices()
        for id_, bamboo in enumerate(bamboos):
            name = bamboo['name']
            mmio_size = bamboo['mmio_size']
            registers = bamboo['registers']
            #
            self.machine_struct['fields'].extend([indent('MemoryRegion {};'.format(to_mmio(name), 1))])
            #
            for register in registers:
                self.machine_struct['fields'].extend([indent('uint32_t {};'.format(register['name']))])
                self.machine_reset['body'].extend([indent('s->{} = {};'.format(register['name'], register['value']))])
            self.machine_init['body'].extend([
                indent('memory_region_init_io(&s->{}, NULL, &{}, s, {}, {});'.format(
                    to_mmio(name), to_ops(name), to_type(machine_name), mmio_size), 1),
                indent('memory_region_add_subregion_overlap(get_system_memory(), {}, &s->{}, 0);'.format(
                    bamboo['mmio_base'], to_mmio(name)), 1)
            ])
            #
            update = {'signature': [], 'declaration': [], 'body': []}
            update['signature'].extend([
                'static void {}(void *opaque)'.format(to_update(name))
            ])
            update['declaration'].extend([
                indent('/* {} *s = opaque; */'.format(to_state(machine_name)), 1),
            ])
            self.machine_mmio_ops.append(update)
            #
            read = {'signature': [], 'declaration': [], 'body': []}
            read['signature'].extend([
                'static uint64_t {}(void *opaque, hwaddr offset, unsigned size)'.format(to_read(name))
            ])
            read['declaration'].extend([
                indent('{} *s = opaque;'.format(to_state(machine_name)), 1),
                indent('uint32_t res = 0;', 1),
            ])
            read['body'].extend([
                indent('switch (offset) {', 1),
                indent('default:', 1),
                indent('qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\\n", __func__, offset);', 2),
                indent('return 0;', 2),
            ])
            for register in registers:
                read['body'].extend([
                    indent('case {}:'.format(register['offset']), 1),
                    indent('res = s->{};'.format(register['name']), 2),
                    indent('break;', 2),
                ])
            read['body'].extend([indent('}', 1)])
            read['body'].extend([indent('return res;', 1)])
            self.machine_mmio_ops.append(read)
            #
            write = {'signature': [], 'declaration': [], 'body': []}
            write['signature'].extend([
                'static void {}(void *opaque, hwaddr offset, uint64_t val, unsigned size)'.format(to_write(name))
            ])
            write['declaration'].extend([
                indent('{} *s = opaque;'.format(to_state(machine_name)), 1),
            ])
            write['body'].extend([
                indent('switch (offset) {', 1),
                indent('default:', 1),
                indent('qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\\n", __func__, offset);', 2),
                indent('return;', 2),
            ])
            for register in registers:
                write['body'].extend([
                    indent('case {}:'.format(register['offset']), 1),
                    indent('s->{} = val;'.format(register['name']), 2),
                    indent('break;', 2),
                ])
            write['body'].extend([indent('}', 1)])
            write['body'].extend([indent('{}(s);'.format(to_update(name)), 1)])
            self.machine_mmio_ops.append(write)
            # 
            ops = {'declaration': [], 'values': []}
            ops['declaration'].extend([
                'static const MemoryRegionOps {}'.format(to_ops(name))
            ])
            ops['values'].extend([
                indent('.read = {},'.format(to_read(name)), 1),
                indent('.write = {},'.format(to_write(name)), 1),
                indent('.endianness = DEVICE_NATIVE_ENDIAN,', 1)
            ])
            self.machine_mmio_ops.append(ops)

    def solve_irq_to_cpu(self, firmware):
        cpu_pp_model = firmware.probe_cpu_pp_model()
        if cpu_pp_model:
            self.machine_init['body'].extend([
                indent('sysbus_connect_irq(SYS_BUS_DEVICE(&s->cpu_pp), 0, '
                       'qdev_get_gpio_in(DEVICE(s->cpu), ARM_CPU_IRQ));', 1),
                indent('sysbus_connect_irq(SYS_BUS_DEVICE(&s->cpu_pp), 1, '
                       'qdev_get_gpio_in(DEVICE(s->cpu), ARM_CPU_FIQ));', 1),
                indent('sysbus_connect_irq(SYS_BUS_DEVICE(&s->cpu_pp), 2, '
                       'qdev_get_gpio_in(DEVICE(s->cpu), ARM_CPU_VIRQ));', 1),
                indent('sysbus_connect_irq(SYS_BUS_DEVICE(&s->cpu_pp), 3, '
                       'qdev_get_gpio_in(DEVICE(s->cpu), ARM_CPU_VFIQ));', 1),
            ])

    def solve_load_kernel(self, firmware):
        architecture = firmware.sget_architecture()
        if architecture == 'arm':
            self.machine['includings'].extend(['hw/arm/arm.h'])
            self.machine_init['declaration'].extend([indent('static struct arm_boot_info binfo;', 1)])
        elif architecture == 'mips':
            self.machine_init['declaration'].extend([indent('static struct mips_boot_info binfo;', 1)])
        else:
            raise NotImplementedError()

        board_id = firmware.sget_board_id()
        self.machine_init['body'].extend([
            indent('binfo.board_id = {};'.format(board_id), 1),
            indent('binfo.ram_size = machine->ram_size;', 1),
            indent('binfo.kernel_filename = machine->kernel_filename;', 1),
            indent('binfo.kernel_cmdline = machine->kernel_cmdline;', 1),
            indent('binfo.initrd_filename = machine->initrd_filename;', 1),
        ])

        if architecture == 'arm':
            self.machine_init['body'].extend([indent('arm_load_kernel(ARM_CPU(first_cpu), &binfo);', 1)])
        elif architecture == 'mips':
            self.machine_init['body'].extend([indent('mips_load_kernel(MIPS_CPU(first_cpu), &binfo);', 1)])
        else:
            raise NotImplementedError()

    def solve_machine_init(self, firmware):
        machine_name = firmware.sget_machine_name()
        self.machine_init['signature'].extend(['static void {}_init(MachineState *machine)'.format(machine_name)])
        self.machine_init['declaration'].extend([
            indent('{0} *s = g_new0({0}, 1);'.format(to_state(machine_name)), 1),
            indent('Error *err = NULL;', 1)
        ])
        self.solve_abelia_devices(firmware)
        self.machine_init['body'].extend([''])
        self.solve_bamboo_devices(firmware)
        self.machine_init['body'].extend([''])
        self.machine_init['body'].extend([indent('{}_reset(s);'.format(machine_name), 1)])
        self.machine_init['body'].extend([''])
        self.solve_irq_to_cpu(firmware)
        self.solve_load_kernel(firmware)

    def solve_machine_class_init(self, firmware):
        machine_desc = firmware.sget_machine_description()
        machine_name = firmware.sget_machine_name()
        architecture = firmware.sget_architecture()
        ram_size = firmware.sget_ram_size()
        cpu_model = firmware.sget_cpu_model()

        self.machine['includings'].extend(['qemu/units.h'])
        self.machine['includings'].extend(['target/arm/cpu.h'])
        self.machine_class_init['signature'].extend(
            ['static void {}_machine_init(MachineClass *mc)'.format(machine_name)])
        self.machine_class_init['body'].extend([
            '    /* mc->family = ; */',
            '    /* mc->name = "{}"; */'.format(machine_name),
            '    /* mc->alias = ; */',
            '    mc->desc = "{}";'.format(machine_desc),
            '    /* mc->deprecation_reason = ; */',
            '    mc->init = {}_init;'.format(machine_name),
            '    /* mc->reset = ; */',
            '    /* mc->hot_add_cpu = ; */',
            '    /* mc->kvm_type = ; */',
            '    /* mc->block_default_type = ; */',
            '    /* mc->units_per_default_bus = ; */',
            '    /* mc->max_cpus = ; */',
            '    /* mc->min_cpus = ; */',
            '    /* mc->default_cpus = ; */',
            '    /* mc->no_serial = 1; */',
            '    /* mc->no_paralled = 1; */',
            '    /* mc->no_floppy = 1; */',
            '    /* mc->no_cdrom = 1; */',
            '    /* mc->no_sdcard = 1; */',
            '    /* mc->pci_allow_0_address = 1; */',
            '    /* mc->legacy_fw_cfg_order = 1; */',
            '    /* mc->is_dault = ; */',
            '    /* mc->default_machine_opts = ; */',
            '    /* mc->default_boot_order = ; */',
            '    /* mc->default_display = ; */',
            '    /* mc->compat_props = ; */',
            '    /* mc->hw_version = ; */',
            '    mc->default_ram_size = {};'.format(ram_size),
            '    mc->default_cpu_type = {}_CPU_TYPE_NAME("{}");'.format(architecture.upper(), cpu_model),
            '    /* mc->default_kernel_irqchip_split = ; */',
            '    /* mc->option_rom_has_mr = ; */',
            '    /* mc->minimum_page_bits = ; */',
            '    /* mc->has_hotpluggable_cpus = ; */',
            '    mc->ignore_memory_transaction_failures = false;',
            '    /* mc->numa_mem_align_shift = ; */',
            '    /* mc->valid_cpu_types = ; */',
            '    /* mc->allowed_dynamic_sysbus_devices = ; */',
            '    /* mc->auto_enable_numa_with_memhp = ; */',
            '    /* mc->numa_auto_assign_ram = ; */',
            '    /* mc->ignore_boot_device_suffixes = ; */',
            '    /* mc->smbus_no_migration_support = ; */',
            '    /* mc->nvdimm_supported = ; */',
            '    /* mc->get_hotplug_handler = ; */',
            '    /* mc->cpu_index_to_instance_props = ; */',
            '    /* mc->CPuArchIdList = ; */',
            '    /* mc->get_default_cpu_node_id = ; */',
        ])

    def solve_define_machine(self, firmware):
        machine_name = firmware.sget_machine_name()
        self.machine['define_machine'].extend([
            'DEFINE_MACHINE(\"{}\", {}_machine_init)'.format(machine_name, machine_name)])
        self.machine['includings'].extend(['hw/boards.h'])

    def link(self, firmware):
        source = []
        source.extend(self.license)
        source.append('\n')
        source.extend(self.render_includings(self.machine['includings']))
        source.append('\n')
        source.extend(self.render_lines(self.machine['defines']))
        source.append('\n')
        source.extend(self.render_struct(self.machine_struct))
        source.append('\n')
        for item in self.machine_mmio_ops:
            try:
                source.extend(self.render_function(item))
            except KeyError:
                source.extend(self.render_structure(item))
            source.append('\n')
        source.extend(self.render_function(self.machine_reset))
        source.append('\n')
        source.extend(self.render_function(self.machine_init))
        source.append('\n')
        source.extend(self.render_function(self.machine_class_init))
        source.append('\n')
        source.extend(self.machine['define_machine'])

        self.source = ''.join(source)
