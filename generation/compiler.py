import os
import abc

from generation.common import to_state, to_mmio, to_ops, indent, to_type, to_read, to_write, to_update, \
    to_header, to_upper, to_cpu_pp_state, to_cpu_pp_type, concat, to_irq
from generation.preprocessor import PreProcessor
from generation.render import Template
from supervisor.logging_setup import logger_info, logger_debugging


class CompilerToQEMUMachine(object):
    def __init__(self, firmware):
        # input
        self.firmware = firmware
        # internal state
        self.license = ['/* \n * automatically generated, don\'t change\n */\n']
        self.source = None
        self.header = None
        self.location = {
            'root': 'build/qemu-4.0.0',
            'machine': {'arm': 'hw/arm', 'mips': 'hw/mips', 'timer': 'hw/timer', 'interrupt_controller': 'hw/intc',
                        'bridge': 'hw/arm'},
            'configs': {'arm': 'default-configs/arm-softmmu.mak', 'mips': 'default-configs/mips-softmmu.mak'},
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

        self.preprocessor = PreProcessor(firmware)

        # common part
        if firmware.get_endian() == 'l':
            self.endianness = 'DEVICE_LITTLE_ENDIAN'
        else:
            self.endianness = 'DEVICE_BIG_ENDIAN'
        self.architecture = firmware.get_architecture()
        self.cpu_pp_model = self.firmware.probe_cpu_pp_model()
        self.interrupt_controller = self.firmware.probe_interrupt_controller()

    def check_analysis(self, to_be_checked, name):
        if to_be_checked is None:
            raise NotImplementedError(self.feedback('analysis', name))

    def feedback(self, t, name):
        if t == 'analysis':
            return 'add an analysis to set firmware.{}'.format(name)

    def info(self, message, action):
        logger_info(self.firmware.get_uuid(), 'code_generation', action, message, 0)

    def debug(self, message, action):
        logger_debugging(self.firmware.get_uuid(), 'code_generation', action, message, 0)

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

    def solve_makefiles(self):
        machine_name = self.firmware.get_machine_name()
        architecture = self.firmware.get_architecture()
        #
        config = 'CONFIG_{}=y\n'.format(to_upper(machine_name))
        path = os.path.join(self.firmware.get_working_dir(), 'qemu-4.0.0', self.location['configs'][architecture])
        content = [config]
        self.solve_makefile(path, config, content)
        #
        kconfig = 'config {}\n'.format(to_upper(machine_name))
        path = os.path.join(self.firmware.get_working_dir(), 'qemu-4.0.0', self.location['kconfig'][architecture])
        content = ['\n', kconfig, '    bool\n']
        self.solve_makefile(path, kconfig, content)
        #
        if self.firmware.probe_bridge():
            bridge_name = self.firmware.get_bridge_name()
            makefile = 'obj-$(CONFIG_{}) += {}.o {}.o\n'.format(
                to_upper(machine_name), machine_name, bridge_name)
        else:
            makefile = 'obj-$(CONFIG_{}) += {}.o\n'.format(to_upper(machine_name), machine_name)
        path = os.path.join(self.firmware.get_working_dir(), 'qemu-4.0.0', self.location['makefile'][architecture])
        content = [makefile]
        self.solve_makefile(path, makefile, content)
        #
        if len(self.custom_devices['timer']['source']):
            timer_name = self.firmware.get_timer_name()
            makefile = 'obj-$(CONFIG_{}) += {}.o\n'.format(to_upper(machine_name), timer_name)
            path = os.path.join(self.firmware.get_working_dir(), 'qemu-4.0.0', self.location['makefile']['timer'])
            content = [makefile]
            self.solve_makefile(path, makefile, content)
        #
        if len(self.custom_devices['interrupt_controller']['source']):
            ic_name = self.firmware.get_interrupt_controller_name()
            makefile = 'obj-$(CONFIG_{}) += {}.o\n'.format(to_upper(machine_name), ic_name)
            path = os.path.join(self.firmware.get_working_dir(), 'qemu-4.0.0',
                                self.location['makefile']['interrupt_controller'])
            content = [makefile]
            self.solve_makefile(path, makefile, content)

    def install(self):
        os.system('cp -r {}/qemu/* {}'.format(self.firmware.get_working_dir(), self.location['root']))

    def make(self):
        # compile first
        os.system(
            'cd {}/qemu-4.0.0 && make CFLAGS=-Wmaybe-uninitialized -j4 && cd -'.format(self.firmware.get_working_dir()))
        # construct the command
        if self.firmware.get_architecture() == 'arm':
            running_command = '{}/qemu-4.0.0/arm-softmmu/qemu-system-arm'.format(self.firmware.get_working_dir())
        elif self.firmware.get_architecture() == 'mips':
            if self.firmware.get_endian() == 'l':
                running_command = '{}/qemu-4.0.0/mipsel-softmmu/qemu-system-mipsel'.format(
                    self.firmware.get_working_dir())
            else:
                running_command = '{}/qemu-4.0.0/mips-softmmu/qemu-system-mips'.format(
                    self.firmware.get_working_dir())
        else:
            raise NotImplementedError()
        machine_name = self.firmware.get_machine_name()
        running_command += ' -M {}'.format(machine_name)
        path_to_uimage = self.firmware.get_path_to_uimage()
        running_command += ' -kernel {}'.format(path_to_uimage)
        path_to_dtb = self.firmware.get_path_to_dtb()
        if path_to_dtb:
            running_command += ' -dtb {}'.format(path_to_dtb)
        if self.firmware.probe_flash():
            if self.firmware.get_flash_type() == 'nor':
                running_command += ' -drive file={},if=pflash,format=raw'.format(self.firmware.get_path())
            elif self.firmware.get_flash_type() == 'nand':
                running_command += ' -drive file={},if=mtd,format=raw'.format(self.firmware.get_path())
            else:
                raise NotImplementedError()
        running_command += ' -nographic'
        self.info(running_command, 'run')
        self.firmware.running_command = running_command

    def solve(self):
        self.preprocessor.preprocess()
        self.solve_machine_includings()
        self.solve_machine_defines()
        self.solve_machine_struct()
        self.solve_machine_init()
        self.solve_machine_class_init()
        self.solve_define_machine()

    def solve_machine_struct(self):
        machine_name = self.firmware.get_machine_name()
        self.check_analysis(machine_name, 'machine_name')
        self.machine_struct['declaration'].extend([
            'typedef struct {} {{'.format(to_state(machine_name)), '}} {};'.format(to_state(machine_name))
        ])
        self.info('solved machine struct', 'compile')

    def solve_machine_defines(self):
        machine_name = self.firmware.get_machine_name()
        self.check_analysis(machine_name, 'machine_name')
        self.machine['defines'].extend([
            '#define {} "{}"'.format(to_type(machine_name), machine_name),
            '#define {}(obj) \\\n    OBJECT_CHECK({}, (obj), {})'.format(
                machine_name.upper(), to_state(machine_name), to_type(machine_name))
        ])
        self.info('solved machine defines', 'compile')

    def solve_machine_includings(self):
        self.machine['includings'].extend(['qemu/osdep.h'])
        self.machine['includings'].extend(['qemu/log.h'])
        self.machine['includings'].extend(['hw/sysbus.h'])
        self.info('solved machine includings', 'compile')

    def solve_abelia_devices(self):
        # cpu
        architecture = self.firmware.get_architecture()
        self.check_analysis(architecture, 'architecture')
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
        self.info('solved abelia cpu', 'compile')

        # cpu_pp
        cpu_model = self.firmware.get_cpu_model()
        self.check_analysis(cpu_model, 'cpu_model')
        cpu_pp_model = self.firmware.probe_cpu_pp_model()
        if cpu_pp_model:
            if architecture == 'arm':
                cpu_pp_mmio_base = self.firmware.get_cpu_pp_mmio_base()
                self.check_analysis(cpu_pp_mmio_base, 'cpu_pp_mmio_base')
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
            self.info('solved abelia cpu private peripheral', 'compile')
        # ram
        ram_priority = self.firmware.get_ram_priority()
        self.check_analysis(ram_priority, 'ram_priority')
        self.machine['includings'].extend(['exec/address-spaces.h'])
        self.machine_struct['fields'].extend([indent('MemoryRegion ram;', 1)])
        self.machine_init['body'].extend([
            indent('memory_region_allocate_system_memory(&s->ram, OBJECT(machine), "ram", machine->ram_size);'),
            indent('memory_region_add_subregion_overlap(get_system_memory(), 0, &s->ram, {});'.format(ram_priority)),
        ])
        self.info('solved abelia ram', 'compile')
        # interrupt controller

        if not cpu_pp_model and self.firmware.probe_interrupt_controller():
            ic_name = self.firmware.get_interrupt_controller_name()
            self.check_analysis(ic_name, 'interrupt_controller_name')
            ic_registers = self.firmware.get_interrupt_controller_registers()
            self.check_analysis(ic_registers, 'interrupt_controller_registers')
            ic_mmio_size = self.firmware.get_interrupt_controller_mmio_size()
            self.check_analysis(ic_mmio_size, 'interrupt_controller_mmio_size')
            ic_mmio_base = self.firmware.get_interrupt_controller_mmio_base()
            self.check_analysis(ic_mmio_size, 'interrupt_controller_mmio_base')
            ic_n_irqs = self.firmware.get_n_irqs()
            self.check_analysis(ic_n_irqs, 'interrupt_controller_n_irqs')
            context = {'ic_name': ic_name, 'ic_registers': ic_registers, 'ic_mmio_size': ic_mmio_size,
                       'ic_mmio_base': ic_mmio_base, 'ic_n_irqs': ic_n_irqs, 'upper': lambda x: x.upper(),
                       'concat': lambda x: concat(x), 'license': ''.join(self.license)}
            with open('generation/templates/ic.c') as f:
                ic_c_lines = f.readlines()
            ic_c = Template(''.join(ic_c_lines)).render(context)
            self.custom_devices['interrupt_controller']['source'].extend(ic_c)
            with open('generation/templates/ic.h') as f:
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
            self.info('solved abelia interrupt controller', 'compile')
        # bridge
        if not cpu_pp_model and self.firmware.probe_bridge() and self.firmware.probe_interrupt_controller():
            bridge_name = self.firmware.get_bridge_name()
            self.check_analysis(bridge_name, 'bridge_name')
            bridge_mmio_base = self.firmware.get_bridge_mmio_base()
            self.check_analysis(bridge_name, 'bridge_mmio_base')
            bridge_mmio_size = self.firmware.get_bridge_mmio_size()
            self.check_analysis(bridge_name, 'bridge_mmio_zise')
            bridge_registers = self.firmware.get_bridge_registers()
            context = {'bridge_name': bridge_name, 'bridge_mmio_size': bridge_mmio_size,
                       'bridge_mmio_base': bridge_mmio_base, 'bridge_registers': bridge_registers,
                       'upper': lambda x: x.upper(), 'concat': lambda x: concat(x),
                       'license': ''.join(self.license)}
            with open('generation/templates/bridge.c') as f:
                bridge_c_lines = f.readlines()
            bridge_c = Template(''.join(bridge_c_lines)).render(context)
            self.custom_devices['bridge']['source'].extend(bridge_c)
            with open('generation/templates/bridge.h') as f:
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
            # bridge_connect_to = self.firmware.lget_bridge_connect_to()
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
            self.info('solved abelia bridge', 'compile')
        # timer
        if not cpu_pp_model and self.firmware.probe_timer():
            timer_name = self.firmware.get_timer_name()
            self.check_analysis(timer_name, 'timer_name')
            timer_mmio_size = self.firmware.get_timer_mmio_size()
            self.check_analysis(timer_mmio_size, 'timer_mmio_size')
            timer_mmio_base = self.firmware.get_timer_mmio_base()
            self.check_analysis(timer_mmio_base, 'timer_mmio_base')
            timer_registers = self.firmware.get_timer_registers()
            context = {'timer_name': timer_name, 'timer_mmio_size': timer_mmio_size, 'timer_mmio_base': timer_mmio_base,
                       'timer_registers': timer_registers, 'upper': lambda x: x.upper(), 'concat': lambda x: concat(x),
                       'license': ''.join(self.license)}
            with open('generation/templates/timer.c') as f:
                timer_c_lines = f.readlines()
            timer_c = Template(''.join(timer_c_lines)).render(context)
            self.custom_devices['timer']['source'].extend(timer_c)
            with open('generation/templates/timer.h') as f:
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
            # timer_connect_to = self.firmware.lget_timer_connect_to()
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
            self.info('solved abelia timer', 'compile')
        # uart
        if self.firmware.probe_uart():
            self.resolve_uart()
        # flash
        if self.firmware.probe_flash():
            flash_type = self.firmware.get_flash_type()
            self.check_analysis(flash_type, 'flash_type')
            self.machine['includings'].extend(['sysemu/blockdev.h', 'hw/block/flash.h'])
            self.machine_init['declaration'].extend([indent('DriveInfo *dinfo;', 1)])
            if flash_type == 'nor':
                flash_base = self.firmware.get_flash_base()
                self.check_analysis(flash_base, 'flash_base')
                flash_size = self.firmware.get_flash_size()
                self.check_analysis(flash_size, 'flash_size')
                flash_section_size = self.firmware.get_flash_section_size()
                self.check_analysis(flash_section_size, 'flash_section_size')
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
            self.info('soved abelia flash', 'compile')

    @abc.abstractmethod
    def resolve_uart_irq_api(self, uart_irq):
        pass

    def resolve_uart(self):
        # get uarts information
        uart_num = self.firmware.get_uart_num()
        for i in range(0, uart_num):
            uart_mmio_base = self.firmware.get_uart_mmio_base(i)
            self.check_analysis(uart_mmio_base, 'uart_mmio_base')
            uart_baud_rate = self.firmware.get_uart_baud_rate(i)
            self.check_analysis(uart_baud_rate, 'uart_baud_rate')
            uart_reg_shift = self.firmware.get_uart_reg_shift(i)
            self.check_analysis(uart_reg_shift, 'uart_reg_shift')
            uart_irq = self.firmware.get_uart_irq(i)
            self.check_analysis(uart_irq, 'uart_irq')

            # resolve their IRQs
            uart_irq_api = self.resolve_uart_irq_api(uart_irq)
            self.machine_init['body'].extend([
                indent(
                    'serial_mm_init(get_system_memory(), {}, {}, {}, {}, serial_hd({}), {});'.format(
                        uart_mmio_base, uart_reg_shift, uart_irq_api, uart_baud_rate, i, self.endianness))
            ])
        self.machine['includings'].extend(['hw/char/serial.h'])
        self.info('resolved abelia uart', 'compile')

    def solve_bamboo_devices(self):
        machine_name = self.firmware.get_machine_name()
        self.check_analysis(machine_name, 'machine_name')
        #
        self.machine_reset['signature'].extend(['static void {}_reset(void *opaque)'.format(machine_name)])
        #
        bamboos = self.firmware.get_bamboo_devices()
        self.check_analysis(bamboos, 'bamboo_devices')
        if len(bamboos):
            self.machine_reset['declaration'].extend([indent('{} *s = opaque;'.format(to_state(machine_name)), 1)])
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
                indent('.endianness = {},'.format(self.endianness), 1)
            ])
            self.machine_mmio_ops.append(ops)

    def solve_irq_to_cpu(self):
        cpu_pp_model = self.firmware.probe_cpu_pp_model()
        self.check_analysis(cpu_pp_model, 'cpu_pp_model')
        architecture = self.firmware.get_architecture()
        self.check_analysis(architecture, 'architecture')
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
        elif cpu_pp_model and architecture == 'mips':
            pass
        else:
            if not self.firmware.probe_interrupt_controller():
                return
            self.machine_init['body'].extend([
                indent('qdev_connect_gpio_out_named(DEVICE(&s->ic), "irq", 0, '
                       'qdev_get_gpio_in(DEVICE(s->cpu), ARM_CPU_IRQ));')
            ])

    def solve_load_kernel(self):
        architecture = self.firmware.get_architecture()
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

    def solve_machine_init(self):
        machine_name = self.firmware.get_machine_name()
        self.check_analysis(machine_name, 'machine_name')
        self.machine_init['signature'].extend(['static void {}_init(MachineState *machine)'.format(machine_name)])
        self.machine_init['declaration'].extend([
            indent('{0} *s = g_new0({0}, 1);'.format(to_state(machine_name)), 1),
            indent('Error *err = NULL;', 1)
        ])
        self.solve_abelia_devices()
        self.machine_init['body'].extend([''])
        self.solve_bamboo_devices()
        self.machine_init['body'].extend([''])
        self.machine_init['body'].extend([indent('{}_reset(s);'.format(machine_name), 1)])
        self.machine_init['body'].extend([''])
        self.solve_irq_to_cpu()
        self.solve_load_kernel()
        self.info('solved machine init', 'compile')

    def solve_machine_class_init(self):
        machine_desc = self.firmware.get_machine_description()
        self.check_analysis(machine_desc, 'machine_description')
        machine_name = self.firmware.get_machine_name()
        self.check_analysis(machine_name, 'machine_name')
        architecture = self.firmware.get_architecture()
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
        self.info('solved machine class init', 'compile')

    def solve_define_machine(self):
        machine_name = self.firmware.get_machine_name()
        self.check_analysis(machine_name, 'machine_name')
        self.machine['define_machine'].extend([
            'DEFINE_MACHINE(\"{}\", {}_machine_init)'.format(machine_name, machine_name)])
        self.machine['includings'].extend(['hw/boards.h'])
        self.info('solved define machine', 'compile')

    def link_and_install(self):
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
        #
        machine_name = self.firmware.get_machine_name()
        architecture = self.firmware.get_architecture()
        os.makedirs(os.path.join(self.firmware.get_working_dir(), 'qemu-4.0.0'), exist_ok=True)
        source_target = os.path.join(
            self.firmware.get_working_dir(), 'qemu-4.0.0', self.location['machine'][architecture],
            machine_name + '.c')
        os.makedirs(os.path.dirname(source_target), exist_ok=True)
        with open(source_target, 'w') as f:
            f.write(self.source)
            f.flush()
        if len(self.custom_devices['timer']['source']):
            timer_name = self.firmware.get_timer_name()
            self.check_analysis(timer_name, 'timer_name')
            source_target = os.path.join(
                self.firmware.get_working_dir(), 'qemu-4.0.0', self.location['machine']['timer'],
                timer_name + '.c'
            )
            os.makedirs(os.path.dirname(source_target), exist_ok=True)
            with open(source_target, 'w') as f:
                f.write(self.custom_devices['timer']['source'])
                f.flush()
            header_target = os.path.join(
                self.firmware.get_working_dir(), 'qemu-4.0.0', 'include', self.location['machine']['timer'],
                timer_name + '.h'
            )
            os.makedirs(os.path.dirname(header_target), exist_ok=True)
            with open(header_target, 'w') as f:
                f.write(self.custom_devices['timer']['header'])
                f.flush()

        if len(self.custom_devices['interrupt_controller']['source']):
            interrupt_controller_name = self.firmware.get_interrupt_controller_name()
            source_target = os.path.join(
                self.firmware.get_working_dir(), 'qemu-4.0.0', self.location['machine']['interrupt_controller'],
                interrupt_controller_name + '.c'
            )
            os.makedirs(os.path.dirname(source_target), exist_ok=True)
            with open(source_target, 'w') as f:
                f.write(self.custom_devices['interrupt_controller']['source'])
                f.flush()
            header_target = os.path.join(
                self.firmware.get_working_dir(), 'qemu-4.0.0', 'include',
                self.location['machine']['interrupt_controller'],
                interrupt_controller_name + '.h'
            )
            os.makedirs(os.path.dirname(header_target), exist_ok=True)
            with open(header_target, 'w') as f:
                f.write(self.custom_devices['interrupt_controller']['header'])
                f.flush()

        if len(self.custom_devices['bridge']['source']):
            bridge_name = self.firmware.get_bridge_name()
            source_target = os.path.join(
                self.firmware.get_working_dir(), 'qemu-4.0.0', self.location['machine']['bridge'],
                bridge_name + '.c'
            )
            os.makedirs(os.path.dirname(source_target), exist_ok=True)
            with open(source_target, 'w') as f:
                f.write(self.custom_devices['bridge']['source'])
                f.flush()
            header_target = os.path.join(
                self.firmware.get_working_dir(), 'qemu-4.0.0', 'include', self.location['machine']['bridge'],
                bridge_name + '.h'
            )
            os.makedirs(os.path.dirname(header_target), exist_ok=True)
            with open(header_target, 'w') as f:
                f.write(self.custom_devices['bridge']['header'])
                f.flush()
        self.info(
            'have linked them all at {}'.format(os.path.join(self.firmware.get_working_dir(), 'qemu-4.0.0')), 'link')
        self.solve_makefiles()
