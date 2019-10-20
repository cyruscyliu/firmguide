import os
import abc

from generation.common import to_state, to_mmio, to_ops, indent, to_type, to_read, to_write, to_update, \
    to_header, to_upper, to_cpu_pp_state, to_cpu_pp_type, concat, to_irq
from generation.render import Template


class CompilerToQEMUMachine(object):
    def __init__(self):
        self.license = ['/* \n * automatically generated, don\'t change\n */\n']
        self.source = None
        self.header = None
        self.location = {
            'root': 'build/qemu-4.0.0',
            'machine': {'arm': 'hw/arm', 'mips': 'hw/mips', 'timer': 'hw/timer', 'interrupt_controller': 'hw/intc',
                        'bridge': 'hw/arm'},
            'configs': {'arm': 'default-configs/arm-softmmu.mak', 'mips': 'default-configs/mipsel-softmmu.mak'},
            'kconfig': {'arm': 'hw/arm/Kconfig', 'mips': 'hw/mips/Kconfig'},
            'makefile': {'arm': 'hw/arm/Makefile.objs', 'mips': 'hw/mips/Makefile.objs',
                         'timer': 'hw/timer/Makefile.objs', 'interrupt_controller': 'hw/intc/Makefile.objs'}
        }
        self.machine = {'includings': [], 'defines': [], 'define_machine': []}
        self.machine_mmio_ops = []
        self.machine_reset = {'signature': [], 'declaration': [], 'body': []}
        self.machine_struct = {'declaration': [], 'fields': []}
        self.machine_class_init = {'signature': [], 'declaration': [], 'body': []}
        self.machine_init = {'signature': [], 'declaration': [], 'body': []}
        self.custom_devices = {'timer': {'source': [], 'header': []},
                               'interrupt_controller': {'source': [], 'header': []},
                               'bridge': {'source': [], 'header': []}}

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

    @staticmethod
    def solve_makefile(path, label, content):
        """
        :param path: path to makefile, str
        :param label: label to be checked, str
        :param content: content to be extend, list
        """
        with open(path) as f:
            lines = f.readlines()
        if not lines[-1].endswith('\n'):
            lines[-1] = lines[-1] + '\n'
        if label not in lines:
            lines.extend(content)
        with open(path, 'w') as f:
            f.writelines(lines)
            f.flush()

    def solve_makefiles(self, firmware):
        machine_name = firmware.sget_machine_name()
        architecture = firmware.sget_architecture()
        #
        config = 'CONFIG_{}=y\n'.format(to_upper(machine_name))
        path = os.path.join(self.location['root'], self.location['configs'][architecture])
        content = [config]
        self.solve_makefile(path, config, content)
        #
        kconfig = 'config {}\n'.format(to_upper(machine_name))
        path = os.path.join(self.location['root'], self.location['kconfig'][architecture])
        content = ['\n', kconfig, '    bool\n']
        self.solve_makefile(path, kconfig, content)
        #
        if firmware.probe_bridge():
            bridge_name = firmware.sget_bridge_name()
            makefile = 'obj-$(CONFIG_{}) += {}.o {}.o\n'.format(
                to_upper(machine_name), machine_name, bridge_name)
        else:
            makefile = 'obj-$(CONFIG_{}) += {}.o\n'.format(to_upper(machine_name), machine_name)
        path = os.path.join(self.location['root'], self.location['makefile'][architecture])
        content = [makefile]
        self.solve_makefile(path, makefile, content)
        #
        if len(self.custom_devices['timer']['source']):
            timer_name = firmware.sget_timer_name()
            makefile = 'obj-$(CONFIG_{}) += {}.o\n'.format(to_upper(machine_name), timer_name)
            path = os.path.join(self.location['root'], self.location['makefile']['timer'])
            content = [makefile]
            self.solve_makefile(path, makefile, content)
        #
        if len(self.custom_devices['interrupt_controller']['source']):
            ic_name = firmware.sget_interrupt_controller_name()
            makefile = 'obj-$(CONFIG_{}) += {}.o\n'.format(to_upper(machine_name), ic_name)
            path = os.path.join(self.location['root'], self.location['makefile']['interrupt_controller'])
            content = [makefile]
            self.solve_makefile(path, makefile, content)

    def install(self, firmware):
        machine_name = firmware.sget_machine_name()
        architecture = firmware.sget_architecture()
        source_target = os.path.join(
            self.location['root'], self.location['machine'][architecture], machine_name + '.c')
        with open(source_target, 'w') as f:
            f.write(self.source)
            f.flush()
        if len(self.custom_devices['timer']['source']):
            timer_name = firmware.sget_timer_name()
            source_target = os.path.join(
                self.location['root'], self.location['machine']['timer'], timer_name + '.c'
            )
            with open(source_target, 'w') as f:
                f.write(self.custom_devices['timer']['source'])
                f.flush()
            header_target = os.path.join(
                self.location['root'], 'include', self.location['machine']['timer'], timer_name + '.h'
            )
            with open(header_target, 'w') as f:
                f.write(self.custom_devices['timer']['header'])
                f.flush()

        if len(self.custom_devices['interrupt_controller']['source']):
            interrupt_controller_name = firmware.sget_interrupt_controller_name()
            source_target = os.path.join(
                self.location['root'], self.location['machine']['interrupt_controller'],
                interrupt_controller_name + '.c'
            )
            with open(source_target, 'w') as f:
                f.write(self.custom_devices['interrupt_controller']['source'])
                f.flush()
            header_target = os.path.join(
                self.location['root'], 'include', self.location['machine']['interrupt_controller'],
                interrupt_controller_name + '.h'
            )
            with open(header_target, 'w') as f:
                f.write(self.custom_devices['interrupt_controller']['header'])
                f.flush()

        if len(self.custom_devices['bridge']['source']):
            bridge_name = firmware.sget_bridge_name()
            source_target = os.path.join(
                self.location['root'], self.location['machine']['bridge'],
                bridge_name + '.c'
            )
            with open(source_target, 'w') as f:
                f.write(self.custom_devices['bridge']['source'])
                f.flush()
            header_target = os.path.join(
                self.location['root'], 'include', self.location['machine']['bridge'],
                bridge_name + '.h'
            )
            with open(header_target, 'w') as f:
                f.write(self.custom_devices['bridge']['header'])
                f.flush()

    def run(self, firmware):
        architecture = firmware.sget_architecture()
        machine_name = firmware.sget_machine_name()
        path_to_kernel = firmware.sget_path_to_kernel()

    def solve(self, firmware):
        self.solve_machine_includings(firmware)
        self.solve_machine_defines(firmware)
        self.solve_machine_struct(firmware)
        self.solve_machine_init(firmware)
        self.solve_machine_class_init(firmware)
        self.solve_define_machine(firmware)
        self.solve_makefiles(firmware)

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
            self.machine['includings'].extend(['target/arm/cpu-qom.h'])
            self.machine_struct['fields'].extend([indent('MIPSCPU *cpu;', 1)])
            self.machine_init['body'].extend([
                indent('s->cpu = MIPS_CPU(object_new(machine->cpu_type));')])
        else:
            raise NotImplementedError()
        self.machine_init['body'].extend([
            indent('object_property_set_bool(OBJECT(s->cpu), true, "realized", &err);', 1)])
        # cpu_pp
        cpu_model = firmware.sget_cpu_model()
        cpu_pp_model = firmware.probe_cpu_pp_model()
        if cpu_pp_model:
            if architecture == 'arm':
                cpu_pp_mmio_base = firmware.sget_cpu_pp_mmio_base()
                self.machine['includings'].extend(['hw/cpu/arm11mpcore.h'])
                self.machine_struct['fields'].extend([indent('{} cpu_pp;'.format(to_cpu_pp_state(cpu_model)), 1)])
                self.machine_init['body'].extend([
                    indent('object_initialize(&s->cpu_pp, sizeof(s->cpu_pp), {});'.format(to_cpu_pp_type(cpu_model))),
                    indent('object_property_set_bool(OBJECT(&s->cpu_pp), true, "realized", &err);', 1),
                    indent('sysbus_mmio_map(SYS_BUS_DEVICE(&s->cpu_pp), 0, {});'.format(cpu_pp_mmio_base), 1)
                ])
            elif architecture == 'mips':
                self.machine['includings'].extend(['hw/mips/cpudevs.h'])
                self.machine_init['body'].extend([
                    indent('cpu_mips_irq_init_cpu(s->cpu);', 1),
                    indent('cpu_mips_clock_init(s->cpu);', 1)
                ])
        # ram
        ram_priority = firmware.sget_ram_priority()
        self.machine['includings'].extend(['exec/address-spaces.h'])
        self.machine_struct['fields'].extend([indent('MemoryRegion ram;', 1)])
        self.machine_init['body'].extend([
            indent('memory_region_allocate_system_memory(&s->ram, OBJECT(machine), "ram", machine->ram_size);'),
            indent('memory_region_add_subregion_overlap(get_system_memory(), 0, &s->ram, {});'.format(ram_priority)),
        ])
        # interrupt controller
        if not cpu_pp_model:
            ic_name = firmware.sget_interrupt_controller_name()
            ic_registers = firmware.lget_interrupt_controller_registers()
            ic_mmio_size = firmware.sget_interrupt_controller_mmio_size()
            ic_mmio_base = firmware.sget_interrupt_controller_mmio_base()
            ic_n_irqs = firmware.sget_n_irqs()
            context = {'ic_name': ic_name, 'ic_registers': ic_registers, 'ic_mmio_size': ic_mmio_size,
                       'ic_mmio_base': ic_mmio_base, 'ic_n_irqs': ic_n_irqs, 'upper': lambda x: x.upper(),
                       'concat': lambda x: concat(x), 'license': ''.join(self.license)}
            with open('generation/template/ic.c') as f:
                ic_c_lines = f.readlines()
            ic_c = Template(''.join(ic_c_lines)).render(context)
            self.custom_devices['interrupt_controller']['source'].extend(ic_c)
            with open('generation/template/ic.h') as f:
                ic_h_lines = f.readlines()
            ic_h = Template(''.join(ic_h_lines)).render(context)
            self.custom_devices['interrupt_controller']['header'].extend(ic_h)
            #
            self.machine['includings'].extend(['hw/intc/{}.h'.format(ic_name)])
            self.machine_struct['fields'].extend([indent('{} ic;'.format(to_state(ic_name)), 1)])
            self.machine_init['body'].extend([
                indent('object_initialize(&s->ic, sizeof(s->ic), {});'.format(to_type(ic_name))),
                indent('qdev_set_parent_bus(DEVICE(&s->ic), sysbus_get_default());'),
                indent('object_property_set_bool(OBJECT(&s->ic), true, "realized", &err);', 1),
                indent('sysbus_mmio_map(SYS_BUS_DEVICE(&s->ic), 0, {});'.format(ic_mmio_base), 1)
            ])
        # bridge
        if firmware.probe_bridge():
            bridge_name = firmware.sget_bridge_name()
            bridge_mmio_base = firmware.sget_bridge_mmio_base()
            bridge_mmio_size = firmware.sget_bridge_mmio_size()
            bridge_registers = firmware.lget_bridge_registers()
            context = {'bridge_name': bridge_name, 'bridge_mmio_size': bridge_mmio_size,
                       'bridge_mmio_base': bridge_mmio_base, 'bridge_registers': bridge_registers,
                       'upper': lambda x: x.upper(), 'concat': lambda x: concat(x),
                       'license': ''.join(self.license)}
            with open('generation/template/bridge.c') as f:
                bridge_c_lines = f.readlines()
            bridge_c = Template(''.join(bridge_c_lines)).render(context)
            self.custom_devices['bridge']['source'].extend(bridge_c)
            with open('generation/template/bridge.h') as f:
                bridge_h_lines = f.readlines()
            bridge_h = Template(''.join(bridge_h_lines)).render(context)
            self.custom_devices['bridge']['header'].extend(bridge_h)
            #
            self.machine['includings'].extend(['hw/arm/{}.h'.format(bridge_name)])
            self.machine_struct['fields'].extend([indent('{} bridge;'.format(to_state(bridge_name)))])
            self.machine_init['body'].extend([
                indent('object_initialize(&s->bridge, sizeof(s->bridge), {});'.format(to_type(bridge_name))),
                indent('qdev_set_parent_bus(DEVICE(&s->bridge), sysbus_get_default());'),
                indent('object_property_set_bool(OBJECT(&s->bridge), true, "realized", &err);', 1),
                indent('sysbus_mmio_map(SYS_BUS_DEVICE(&s->bridge), 0, {});'.format(bridge_mmio_base), 1)
            ])
            # bridge_connect_to = firmware.lsget_bridge_connect_to()
            # bridge_connect_to = [
            #     {'output': 0, 'input': {'device': 'ic', 'input': 0}},
            # ]
            # for connection in bridge_connect_to:
            #     self.machine_init['body'].extend([
            #         indent('sysbus_connect_irq(SYS_BUS_DEVICE(&bridge), {}, '
            #                'qdev_get_gpio_in_named(DEVICE(&s->{}), {}, {})));'.format(
            #             connection['output'], connection['input']['device'], to_irq(connection['input']['device']),
            #             connection['input']['input']
            #         ))])
            self.machine_init['body'].extend([
                indent(
                    'sysbus_connect_irq(SYS_BUS_DEVICE(&s->bridge), 0, '
                    'qdev_get_gpio_in_named(DEVICE(&s->ic), {}, 0));'.format(to_irq(ic_name))
                )])
        # timer
        if not cpu_pp_model:
            timer_name = firmware.sget_timer_name()
            timer_registers = firmware.lget_timer_registers()
            timer_mmio_size = firmware.sget_timer_mmio_size()
            timer_mmio_base = firmware.sget_timer_mmio_base()
            context = {'timer_name': timer_name, 'timer_mmio_size': timer_mmio_size, 'timer_mmio_base': timer_mmio_base,
                       'timer_registers': timer_registers, 'upper': lambda x: x.upper(), 'concat': lambda x: concat(x),
                       'license': ''.join(self.license)}
            with open('generation/template/timer.c') as f:
                timer_c_lines = f.readlines()
            timer_c = Template(''.join(timer_c_lines)).render(context)
            self.custom_devices['timer']['source'].extend(timer_c)
            with open('generation/template/timer.h') as f:
                timer_h_lines = f.readlines()
            timer_h = Template(''.join(timer_h_lines)).render(context)
            self.custom_devices['timer']['header'].extend(timer_h)
            #
            self.machine['includings'].extend(['hw/timer/{}.h'.format(timer_name)])
            self.machine_struct['fields'].extend([indent('{} timer;'.format(to_state(timer_name)))])
            self.machine_init['body'].extend([
                indent('object_initialize(&s->timer, sizeof(s->timer), {});'.format(to_type(timer_name))),
                indent('qdev_set_parent_bus(DEVICE(&s->timer), sysbus_get_default());'),
                indent('object_property_set_bool(OBJECT(&s->timer), true, "realized", &err);', 1),
                indent('sysbus_mmio_map(SYS_BUS_DEVICE(&s->timer), 0, {});'.format(timer_mmio_base), 1)
            ])
            # timer_connect_to = firmware.lsget_timer_connect_to()
            timer_connect_to = [
                {'output': 0, 'input': {'device': 'bridge', 'input': 1}},
                {'output': 1, 'input': {'device': 'bridge', 'input': 2}}
            ]
            for connection in timer_connect_to:
                self.machine_init['body'].extend([
                    indent('sysbus_connect_irq(SYS_BUS_DEVICE(&s->timer), {}, '
                           'qdev_get_gpio_in_named(DEVICE(&s->{}), {}, {}));'.format(
                        connection['output'], connection['input']['device'], to_irq(connection['input']['device']),
                        connection['input']['input']
                    ))])
        # uart
        uart_mmio_base = firmware.sget_uart_mmio_base()
        uart_baud_rate = firmware.sget_uart_baud_rate()
        uart_reg_shift = firmware.sget_uart_reg_shift()
        uart_irq = firmware.sget_uart_irq()
        uart_irq_api = ''
        if cpu_pp_model:
            if architecture == 'arm':
                uart_irq_api = 'qdev_get_gpio_in(DEVICE(&s->cpu_pp), {})'.format(uart_irq)
            elif architecture == 'mips':
                uart_irq_api = 's->cpu->env.irq[{}]'.format(uart_irq)
            else:
                raise NotImplementedError()
        else:
            uart_irq_api = 'qdev_get_gpio_in_named(DEVICE(&s->ic), {}, {})'.format(to_irq(ic_name), uart_irq)

        self.machine['includings'].extend(['hw/char/serial.h'])
        self.machine_init['body'].extend([
            indent(
                'serial_mm_init(get_system_memory(), {}, {}, {}, {}, serial_hd(0), DEVICE_LITTLE_ENDIAN);'.format(
                    uart_mmio_base, uart_reg_shift, uart_irq_api, uart_baud_rate))
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
        architecture = firmware.sget_architecture()
        if cpu_pp_model and architecture == 'arm':
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
        else:
            self.machine_init['body'].extend([
                indent('qdev_connect_gpio_out_named(DEVICE(&s->ic), "irq", 0, '
                       'qdev_get_gpio_in(DEVICE(s->cpu), ARM_CPU_IRQ));')
            ])

    def solve_load_kernel(self, firmware):
        architecture = firmware.sget_architecture()
        if architecture == 'arm':
            self.machine['includings'].extend(['hw/arm/arm.h'])
            self.machine_init['declaration'].extend([indent('static struct arm_boot_info binfo;', 1)])
            board_id = firmware.sget_board_id()
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
        if architecture == 'arm':
            self.machine['includings'].extend(['target/arm/cpu.h'])
        elif architecture == 'mips':
            self.machine['includings'].extend(['target/mips/cpu.h'])
        else:
            raise NotImplementedError()

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
            '    mc->ignore_memory_transaction_failures = true;',
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
        #
        for k, v in self.custom_devices.items():
            v['source'] = ''.join(v['source'])
            v['header'] = ''.join(v['header'])
