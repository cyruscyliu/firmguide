from slcore.database.dbf import get_database
from slcore.generation.common import indent
from slcore.generation.compiler import CompilerToQEMUMachine


class ARMCompiler(CompilerToQEMUMachine):
    def resolve_cpu(self):
        self.machine['includings'].extend(['target/arm/cpu-qom.h'])
        self.machine_struct['fields'].extend([indent('ARMCPU *cpu;', 1)])
        self.machine_init['body'].extend([
            indent('s->cpu = ARM_CPU(object_new(machine->cpu_type));')
        ])
        self.machine_init['body'].extend([
            indent('object_property_set_bool(OBJECT(s->cpu), true, "realized", &err);', 1)])

    def resolve_cpu_private_peripheral(self):
        qemu_apis = get_database('qemu.apis')
        cpu_pp_name = self.firmware.get_cpu_pp_name()
        cpu_pp_mmio_base = self.firmware.get_cpu_pp_mmio_base()
        self.check_analysis(cpu_pp_mmio_base, 'cpu_pp_mmio_base')
        self.machine['includings'].extend([qemu_apis.select(cpu_pp_name, 'header')])
        self.machine_struct['fields'].extend(
            [indent('{} cpu_pp;'.format(qemu_apis.select(cpu_pp_name, 'state_struct')), 1)])
        self.machine_init['body'].extend([
            indent('object_initialize(&s->cpu_pp, sizeof(s->cpu_pp), {});'.format(
                qemu_apis.select(cpu_pp_name, 'type_macro'))),
            indent('object_property_set_bool(OBJECT(&s->cpu_pp), true, "realized", &err);', 1),
            indent('sysbus_mmio_map(SYS_BUS_DEVICE(&s->cpu_pp), 0, {});'.format(cpu_pp_mmio_base), 1)
        ])

    def resolve_irq_to_cpu(self):
        if self.cpu_pp_model:
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
        elif not self.interrupt_controller:
            return
        else:
            self.machine_init['body'].extend([
                indent('qdev_connect_gpio_out_named(DEVICE(&s->ic), "irq", 0, '
                       'qdev_get_gpio_in(DEVICE(s->cpu), ARM_CPU_IRQ));')
            ])

    def resolve_uart_irq_api(self, uart_irq):
        if self.cpu_pp_model:
            uart_irq_api = 'qdev_get_gpio_in(DEVICE(&s->cpu_pp), {})'.format(uart_irq)
        elif self.interrupt_controller:
            uart_irq_api = 'NULL'
            # ic_name = self.firmware.get_interrupt_controller_name()
            # uart_irq_api = 'qdev_get_gpio_in_named(DEVICE(&s->ic), {}, {})'.format(
            #     to_irq(ic_name), uart_irq)
        else:
            uart_irq_api = 'NULL'
        return uart_irq_api

    def __init__(self, firmware):
        super().__init__(firmware)
        self.location['configs'] = 'default-configs/arm-softmmu.mak'
        self.location['kconfig'] = 'hw/arm/Kconfig'

