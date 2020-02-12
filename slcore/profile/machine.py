from slcore.compositor import Common
from slcore.dt_parsers.cpu import find_cpu_in_fdt
from slcore.dt_parsers.compatible import find_compatible_in_fdt
from slcore.dt_parsers.intc import *
from slcore.dt_parsers.mmio import *
from slcore.dt_parsers.uart import *
import os


CPU_ATTRIBUTES = ['compatible']


class CPU(Common):
    def __init__(self):
        super().__init__()
        self.set_attributes(MACHINE_ATTRIBUTES)


RAM_ATTRIBUTES = []


class RAM(Common):
    def __init__(self):
        super().__init__()
        self.set_attributes(RAM_ATTRIBUTES)


INTC_ATTRIBUTES = ['levels', 'intc', 'intc_tree', 'flatten_intc_tree']


class INTC(Common):
    def __init__(self):
        super().__init__()
        self.set_attributes(INTC_ATTRIBUTES)


UART_ATTRIBUTES = []


class UART(Common):
    def __init__(self):
        super().__init__()
        self.set_attributes(UART_ATTRIBUTES)

BAMBOO_ATTRIBUTES = [
    'base', 'size'
]


class Bamboo(Common):
    def __init__(self):
        super().__init__()
        self.set_attributes(BAMBOO_ATTRIBUTES)


MACHINE_ATTRIBUTES = [
    'machine_id', 'compatible', 'nvram', 'cmdline',
    'cpus', 'ram', 'intc', 'timer', 'uarts', 'bamboos'
]


class Machine(Common):
    def __init__(self):
        super().__init__()
        self.set_attributes(MACHINE_ATTRIBUTES)

    def parse_dts(self, dts):
        self.compatible = find_compatible_in_fdt(dts)

        cpu = CPU()
        cpu.set_compatible(find_cpu_in_fdt(dts))
        self.set_cpus([cpu])

        flatten_intc_tree = find_flatten_intc_tree_in_fdt(dts)
        flatten_mmio = find_flatten_mmio_in_fdt(dts)
        flatten_uart = find_flatten_uart_in_fdt(
            dts, flatten_intc_tree=flatten_intc_tree, flatten_mmio=flatten_mmio)

        intc = INTC()
        levels = 0
        for k, v in flatten_intc_tree.items():
            if v['intc'] and v['master']:
                levels += 1
        intc.set_levels(levels)
        intc.set_flatten_intc_tree(flatten_intc_tree)
        self.set_intc(intc)

        uarts = []
        for k, v in flatten_uart.items():
            uart = UART()
            uart.set_attributes(attrs=v)
            uarts.append(uart)
        self.set_uarts(uarts)

        bamboos = []
        for k, v in flatten_mmio.items():
            if k in flatten_uart:
                continue
            if k in flatten_intc_tree and \
                    flatten_intc_tree[k]['intc']:
                continue
            bamboo = Bamboo()
            bamboo.set_attributes(attrs=v)
            bamboos.append(bamboo)
        self.set_bamboos(bamboos)

