from generation.common import to_irq, indent
from generation.compiler import CompilerToQEMUMachine


class MIPSCompiler(CompilerToQEMUMachine):
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
