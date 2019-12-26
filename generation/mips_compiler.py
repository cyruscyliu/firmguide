from generation.common import to_irq
from generation.compiler import CompilerToQEMUMachine


class MIPSCompiler(CompilerToQEMUMachine):
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
