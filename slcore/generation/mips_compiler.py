from slcore.generation.common import to_irq, indent
from slcore.generation.compiler import CompilerToQEMUMachine


class MIPSCompiler(CompilerToQEMUMachine):
    def resolve_cpu(self):
        self.machine['includings'].extend(['target/arm/cpu-qom.h'])
        self.machine_struct['fields'].extend([indent('MIPSCPU *cpu;', 1)])
        self.machine_init['body'].extend([
            indent('s->cpu = MIPS_CPU(object_new(machine->cpu_type));')])
        self.machine_init['body'].extend([
            indent('object_property_set_bool(OBJECT(s->cpu), true, "realized", &err);', 1)])

    def resolve_cpu_private_peripheral(self):
        self.machine['includings'].extend(['hw/mips/cpudevs.h'])
        self.machine_init['body'].extend([
            indent('cpu_mips_irq_init_cpu(s->cpu);', 1),
            indent('cpu_mips_clock_init(s->cpu);', 1)
        ])

    def resolve_irq_to_cpu(self):
        if self.cpu_pp_model:
            return
        elif not self.firmware.probe_interrupt_controller():
            return
        else:
            self.machine_init['body'].extend([
                indent('qdev_connect_gpio_out_named(DEVICE(&s->ic), "irq", 0, '
                       'qdev_get_gpio_in(DEVICE(s->cpu), MIPS_CPU_IRQ));')
            ])

    def resolve_uart_irq_api(self, uart_irq):
        if self.cpu_pp_model:
            uart_irq_api = 's->cpu->env.irq[{}]'.format(uart_irq)
        elif self.interrupt_controller:
            ic_name = self.firmware.get_interrupt_controller_name()
            uart_irq_api = 'qdev_get_gpio_in_named(DEVICE(&s->ic), {}, {})'.format(
                to_irq(ic_name), uart_irq)
        else:
            uart_irq_api = 'NULL'
        return uart_irq_api

    def __init__(self, firmware):
        super().__init__(firmware)

