import os
import abc

from slcore.generation.common import to_state, to_mmio, to_ops, indent, to_type, to_read, to_write, to_update, \
    to_upper, concat
from slcore.generation.preprocessor import PreProcessor
from slcore.generation.render import Template
from logger import logger_info, logger_debug


class CompilerToQEMUMachine(object):
    def __init__(self, firmware):
        # input
        self.firmware = firmware

        # internal state
        self.license = ['/* \n * automatically generated, don\'t change\n */\n']

        self.source = None
        self.header = None

        self.location = {
            'machine': {'arm': 'hw/arm', 'mips': 'hw/mips', 'interrupt_controller': 'hw/intc'},
        }
        self.machine = {'includings': [], 'defines': [], 'define_machine': []}
        self.machine_mmio_ops = []
        self.machine_reset = {'signature': [], 'declaration': [], 'body': []}
        self.machine_struct = {'declaration': [], 'fields': []}
        self.machine_class_init = {'signature': [], 'declaration': [], 'body': []}
        self.machine_init = {'signature': [], 'declaration': [], 'body': []}
        self.custom_devices = {'interrupt_controller': {'source': [], 'header': []}}

        self.preprocessor = PreProcessor(firmware)

        # common part
        if firmware.get_endian() == 'l':
            self.endianness = 'DEVICE_LITTLE_ENDIAN'
        else:
            self.endianness = 'DEVICE_BIG_ENDIAN'
        self.architecture = firmware.get_arch()
        self.cpu_pp_model = self.firmware.probe_cpu_pp_model()
        self.interrupt_controller = self.firmware.probe_interrupt_controller()

    def check_analysis(self, to_be_checked, name):
        if to_be_checked is None:
            raise NotImplementedError(self.feedback('analysis', name))

    def has_sintc(self):
        return len(self.custom_devices['interrupt_controller']['source']) > 0

    def feedback(self, t, name):
        if t == 'analysis':
            return 'add an analysis to set firmware.{}'.format(name)

    def info(self, message, action):
        logger_info(self.firmware.get_uuid(), 'code_generation', action, message, 0)

    def debug(self, message, action):
        logger_debug(self.firmware.get_uuid(), 'code_generation', action, message, 0)

    @staticmethod
    def render_lines(lines):
        """
        input:
            ['a', 'b', 'c']
        output:
            a
            b
            c
        """
        lines_ = []
        for line in lines:
            lines_.append(line + '\n')
        return lines_

    def render_includes(self, lines):
        """
        input:
            ['a.h', 'b.h', 'c.h']
        output:
            #include "a.h"
            #include "b.h"
            #incldue "c.h"
        """
        lines_ = []
        for line in lines:
            lines_.append('#include "{}"'.format(line))
        lines_ = self.render_lines(lines_)
        return lines_

    def render_function(self, function):
        """
        input:
            {'signature': ['void a()'], 'declaration': ['    int a = 0;'],
             'body': ['    a = 1;', '    return;']}
        output:
            void a()
            {
                a = 1;
                return;
            }
        """
        lines = []
        lines.extend(function['signature'])
        lines.append('\n{\n')
        lines.extend(self.render_lines(function['declaration']))
        if len(function['declaration']) and len(function['body']):
            lines.append('\n')
        lines.extend(self.render_lines(function['body']))
        lines.append('}\n')
        return lines

    def render_struct(self, struct):
        """
        input:
            {'declaration': ['typedef struct AState {', '} AState;'], 'fields': ['    int a;']}
        output:
            typedef struct AState {
                int a;
            } AState;
        """
        lines = [struct['declaration'][0], '\n']
        lines.extend(self.render_lines(struct['fields']))
        lines.append(struct['declaration'][1] + '\n')
        return lines

    def render_structure(self, structure):
        """
        input:
            {'declaration': ['static const A a'], 'values': ['.b = c,']}
        output:
            static const A a = {
                .b = c,
            };
        """
        lines = [structure['declaration'][0], ' = {\n']
        lines.extend(self.render_lines(structure['values']))
        lines.append('};\n')
        return lines

    def compile(self):
        self.preprocessor.preprocess()
        self.resolve_machine_includings()
        self.resolve_machine_defines()
        self.resolve_machine_struct()
        self.resolve_machine_class_init()
        self.resolve_machine_init()
        self.resolve_define_machine()

    # independent
    def resolve_machine_struct(self):
        machine_name = self.firmware.get_machine_name()
        self.check_analysis(machine_name, 'machine_name')
        self.machine_struct['declaration'].extend([
            'typedef struct {} {{'.format(to_state(machine_name)), '}} {};'.format(to_state(machine_name))
        ])
        self.debug('resolve machine struct', 'compile')

    # independent
    def resolve_machine_defines(self):
        machine_name = self.firmware.get_machine_name()
        self.check_analysis(machine_name, 'machine_name')
        self.machine['defines'].extend([
            '#define {} "{}"'.format(to_type(machine_name), machine_name),
            '#define {}(obj) \\\n    OBJECT_CHECK({}, (obj), {})'.format(
                machine_name.upper(), to_state(machine_name), to_type(machine_name))
        ])
        self.debug('resolve machine defines', 'compile')

    # independent
    def resolve_machine_includings(self):
        self.machine['includings'].extend(['qemu/osdep.h'])
        self.machine['includings'].extend(['qemu/log.h'])
        self.machine['includings'].extend(['hw/sysbus.h'])
        self.debug('resolve machine includings', 'compile')

    # independent
    def render_templates(self, context, template):
        with open(template) as f:
            lines = f.readlines()
        return Template(''.join(lines)).render(context)

    # dependent
    @abc.abstractmethod
    def resolve_cpu(self):
        pass

    # dependent
    @abc.abstractmethod
    def resolve_cpu_private_peripheral(self):
        pass

    # independent
    def resolve_interrupt_controller(self):
        ic_name = self.firmware.get_interrupt_controller_name()
        self.check_analysis(ic_name, 'interrupt_controller_name')
        ic_registers = self.firmware.get_interrupt_controller_registers()
        self.check_analysis(ic_registers, 'interrupt_controller_registers')
        ic_mmio_size = self.firmware.get_interrupt_controller_mmio_size()
        self.check_analysis(ic_mmio_size, 'interrupt_controller_mmio_size')
        ic_mmio_base = self.firmware.get_interrupt_controller_mmio_base()
        self.check_analysis(ic_mmio_size, 'interrupt_controller_mmio_base')
        timer_irq = self.firmware.get_timer_irq()
        self.check_analysis(timer_irq, 'timer_irq')

        context = {'interrupt_cause_register': ic_registers['interrupt_cause_register'],
                   'interrupt_mask_register': ic_registers['interrupt_mask_register'],
                   'interrupt_clear_register': ic_registers['interrupt_clear_register'],
                   'ic_mmio_size': ic_mmio_size, 'ic_mmio_base': ic_mmio_base,
                   'timer_irq': timer_irq, 'license': ''.join(self.license),
                   'upper': lambda x: x.upper(), 'concat': lambda x: concat(x)}
        ic_c = self.render_templates(context, 'slcore/generation/models/sintc.c')
        self.custom_devices['interrupt_controller']['source'].extend(ic_c)
        ic_h = self.render_templates(context, 'slcore/generation/models/sintc.h')
        self.custom_devices['interrupt_controller']['header'].extend(ic_h)

        self.machine['includings'].extend(['hw/intc/{}.h'.format(ic_name)])
        self.machine_struct['fields'].extend([indent('SIntCState ic;', 1)])
        self.machine_init['body'].extend([
            indent('object_initialize(&s->ic, sizeof(s->ic), TYPE_SINTC);'),
            indent('qdev_set_parent_bus(DEVICE(&s->ic), sysbus_get_default());'),
            indent('object_property_set_bool(OBJECT(&s->ic), true, "realized", &err);', 1),
            indent('sysbus_mmio_map(SYS_BUS_DEVICE(&s->ic), 0, {});'.format(ic_mmio_base), 1)
        ])
        self.debug('solved abelia interrupt controller', 'compile')

    @abc.abstractmethod
    def resolve_uart_irq_api(self, uart_irq):
        pass

    # half independent
    def resolve_uart(self):
        # get uarts information
        for i, uart in enumerate(self.firmware.get_uart()):
            uart_mmio_base = uart['base']
            self.check_analysis(uart_mmio_base, 'uart_mmio_base')
            uart_baud_rate = uart['baud_rate']
            self.check_analysis(uart_baud_rate, 'uart_baud_rate')
            uart_reg_shift = uart['reg_shift']
            self.check_analysis(uart_reg_shift, 'uart_reg_shift')
            uart_irq = uart['irqn']
            self.check_analysis(uart_irq, 'uart_irq')

            # resolve their IRQs
            uart_irq_api = self.resolve_uart_irq_api(uart_irq)
            self.machine_init['body'].extend([
                indent(
                    'serial_mm_init(get_system_memory(), {}, {}, {}, {}, serial_hd({}), {});'.format(
                        uart_mmio_base, uart_reg_shift, uart_irq_api, uart_baud_rate, i, self.endianness))
            ])
        self.machine['includings'].extend(['hw/char/serial.h'])

    # half independent
    def resolve_abelia_devices(self):
        # cpu
        self.resolve_cpu()
        self.debug('resolve abelia cpu', 'compile')
        # cpu_pp
        if self.cpu_pp_model:
            self.resolve_cpu_private_peripheral()
            self.debug('resolve abelia cpu private peripheral(intc/timer)', 'compile')
        # ram
        ram_priority = self.firmware.get_ram_priority()
        self.check_analysis(ram_priority, 'ram_priority')
        self.machine['includings'].extend(['exec/address-spaces.h'])
        self.machine_struct['fields'].extend([indent('MemoryRegion ram;', 1)])
        self.machine_init['body'].extend([
            indent('memory_region_allocate_system_memory(&s->ram, OBJECT(machine), "ram", machine->ram_size);'),
            indent('memory_region_add_subregion_overlap(get_system_memory(), 0, &s->ram, {});'.format(ram_priority)),
        ])
        self.debug('resolve abelia ram', 'compile')

        # sintc
        if not self.cpu_pp_model and self.firmware.probe_interrupt_controller():
            self.resolve_interrupt_controller()
            self.debug('resolve abelia sintc', 'compile')

        # uart
        if self.firmware.probe_uart():
            self.resolve_uart()
            self.debug('resolve abelia uart', 'compile')

    def resolve_bamboo_devices(self):
        machine_name = self.firmware.get_machine_name()
        self.check_analysis(machine_name, 'machine_name')
        #
        self.machine_reset['signature'].extend(['static void {}_reset(void *opaque)'.format(machine_name)])
        #
        bamboos = self.firmware.get_bamboo_devices()
        self.check_analysis(bamboos, 'bamboo_devices')
        if len(bamboos):
            self.machine_reset['declaration'].extend([indent('{} *s = opaque;'.format(to_state(machine_name)), 1)])
        for name, bamboo in bamboos.items():
            mmio_size = bamboo['mmio_size']
            mmio_base = bamboo['mmio_base']
            self.debug('resolve bamboo devices mmio base {}, size {}'.format(mmio_base, mmio_size), 'compile')
            registers = bamboo['registers']
            #
            self.machine_struct['fields'].extend([indent('MemoryRegion {};'.format(to_mmio(name), 1))])
            #
            for rname, register in registers.items():
                self.machine_struct['fields'].extend([indent('uint32_t {};'.format(rname))])
                self.machine_reset['body'].extend([indent('s->{} = {};'.format(rname, register['value']))])
            if 'mmio_priority' in bamboo:
                mmio_priority = bamboo['mmio_priority']
            else:
                mmio_priority = 0
            self.machine_init['body'].extend([
                indent('memory_region_init_io(&s->{}, NULL, &{}, s, {}, {});'.format(
                    to_mmio(name), to_ops(name), to_type(machine_name), mmio_size), 1),
                indent('memory_region_add_subregion_overlap(get_system_memory(), {}, &s->{}, {});'.format(
                    bamboo['mmio_base'], to_mmio(name), mmio_priority), 1)
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
            for rname, register in registers.items():
                read['body'].extend([
                    indent('case {}:'.format(register['offset']), 1),
                    indent('res = s->{};'.format(rname), 2),
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
            for rname, register in registers.items():
                write['body'].extend([
                    indent('case {}:'.format(register['offset']), 1),
                    indent('s->{} = val;'.format(rname), 2),
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
                indent('.endianness = {},'.format(self.endianness), 1)
            ])
            self.machine_mmio_ops.append(ops)

    @abc.abstractmethod
    def resolve_irq_to_cpu(self):
        pass

    # half dependent
    def resolve_load_kernel(self):
        architecture = self.firmware.get_arch()
        self.check_analysis(architecture, 'architecture')
        if architecture == 'arm':
            self.machine['includings'].extend(['hw/arm/arm.h'])
            self.machine_init['declaration'].extend([indent('static struct arm_boot_info binfo;', 1)])
            board_id = self.firmware.get_board_id()
            self.check_analysis(board_id, 'board_id')
            self.machine_init['body'].extend([
                indent('binfo.board_id = {};'.format(board_id), 1),
            ])
        elif architecture == 'mips':
            self.machine['includings'].extend(['hw/mips/mips.h'])
            self.machine_init['declaration'].extend([indent('static struct mips_boot_info binfo;', 1)])
        else:
            raise NotImplementedError()

        self.machine_init['body'].extend([
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

    def resolve_machine_init(self):
        machine_name = self.firmware.get_machine_name()
        self.check_analysis(machine_name, 'machine_name')
        self.machine_init['signature'].extend(['static void {}_init(MachineState *machine)'.format(machine_name)])
        self.machine_init['declaration'].extend([
            indent('{0} *s = g_new0({0}, 1);'.format(to_state(machine_name)), 1),
            indent('Error *err = NULL;', 1)
        ])
        self.resolve_abelia_devices()
        self.machine_init['body'].extend([''])
        self.resolve_bamboo_devices()
        self.machine_init['body'].extend([''])
        self.machine_init['body'].extend([indent('{}_reset(s);'.format(machine_name), 1)])
        self.machine_init['body'].extend([''])
        # TODO topology
        self.resolve_irq_to_cpu()
        self.resolve_load_kernel()
        self.debug('resolve machine init', 'compile')

    def resolve_machine_class_init(self):
        machine_desc = self.firmware.get_machine_description()
        self.check_analysis(machine_desc, 'machine_description')
        machine_name = self.firmware.get_machine_name()
        self.check_analysis(machine_name, 'machine_name')
        architecture = self.firmware.get_arch()
        self.check_analysis(architecture, 'architecture')
        ram_size = self.firmware.get_ram_size()
        self.check_analysis(ram_size, 'ram_size')
        cpu_model = self.firmware.get_cpu_model()
        self.check_analysis(cpu_model, 'cpu_model')

        self.machine['includings'].extend(['qemu/units.h'])
        if architecture == 'arm':
            self.machine['includings'].extend(['target/arm/cpu.h'])
        elif architecture == 'mips':
            self.machine['includings'].extend(['target/mips/cpu.h'])
        else:
            raise NotImplementedError('cannot support this arch {}'.format(architecture))

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
            '    /* mc->is_default = ; */',
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
        self.debug('resolve machine class init', 'compile')

    def resolve_define_machine(self):
        machine_name = self.firmware.get_machine_name()
        self.check_analysis(machine_name, 'machine_name')
        self.machine['define_machine'].extend([
            'DEFINE_MACHINE(\"{}\", {}_machine_init)'.format(machine_name, machine_name)])
        self.machine['includings'].extend(['hw/boards.h'])
        self.debug('resolve define machine', 'compile')

    def link(self):
        #
        source = []
        source.extend(self.license)
        source.append('\n')
        source.extend(self.render_includes(self.machine['includings']))
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
        # save it locally
        machine_name = self.firmware.get_machine_name()
        architecture = self.firmware.get_arch()

        os.makedirs(os.path.join(self.firmware.get_target_dir(), 'qemu-4.0.0'), exist_ok=True)
        source_target = os.path.join(
            self.firmware.get_target_dir(), 'qemu-4.0.0', self.location['machine'][architecture],
            machine_name + '.c')
        os.makedirs(os.path.dirname(source_target), exist_ok=True)
        with open(source_target, 'w') as f:
            f.write(self.source)
            f.flush()
        self.debug('link abelia and bamboo devices at {}'.format(source_target), 'link')

        #
        for k, v in self.custom_devices.items():
            v['source'] = ''.join(v['source'])
            v['header'] = ''.join(v['header'])

        # save them locally
        if len(self.custom_devices['interrupt_controller']['source']):
            interrupt_controller_name = self.firmware.get_interrupt_controller_name()
            source_target = os.path.join(
                self.firmware.get_target_dir(), 'qemu-4.0.0', self.location['machine']['interrupt_controller'],
                interrupt_controller_name + '.c'
            )
            os.makedirs(os.path.dirname(source_target), exist_ok=True)
            with open(source_target, 'w') as f:
                f.write(self.custom_devices['interrupt_controller']['source'])
                f.flush()
            self.debug('link {} source at {}'.format(k, source_target), 'link')
            header_target = os.path.join(
                self.firmware.get_target_dir(), 'qemu-4.0.0', 'include',
                self.location['machine']['interrupt_controller'],
                interrupt_controller_name + '.h'
            )
            os.makedirs(os.path.dirname(header_target), exist_ok=True)
            with open(header_target, 'w') as f:
                f.write(self.custom_devices['interrupt_controller']['header'])
                f.flush()
            self.debug('link {} header at {}'.format(k, source_target), 'link')

