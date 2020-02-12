from slcore.compositor import Common
import os


CPU_ATTRIBUTES = []


class CPU(Common):
    def __init__(self):
        super().__init__()
        self.set_attributes(MACHINE_ATTRIBUTES)


RAM_ATTRIBUTES = []


class RAM(Common):
    def __init__(self):
        super().__init__()
        self.set_attributes(RAM_ATTRIBUTES)


INTC_ATTRIBUTES = []


class INTC(Common):
    def __init__(self):
        super().__init__()
        self.set_attributes(INTC_ATTRIBUTES)


UART_ATTRIBUTES = []


class UART(Common):
    def __init__(self):
        super().__init__()
        self.set_attributes(UART_ATTRIBUTES)


MACHINE_ATTRIBUTES = [
    'machine_id', 'compatible', 'nvram', 'cmdline',
    'cpu', 'ram', 'intc', 'timer', 'uart', 'bamboos'
]


class Machine(Common):
    def __init__(self):
        super().__init__()
        self.set_attributes(MACHINE_ATTRIBUTES)

    def parse_dts(self, dts):
        pass

