from slcore.compositor import Common
from slcore.dt_parsers.cpu import *
from slcore.dt_parsers.compatible import find_compatible_in_fdt
from slcore.dt_parsers.intc import *
from slcore.dt_parsers.mmio import *
from slcore.dt_parsers.uart import *
import os


CPU_ATTRIBUTES = ['path', 'compatible']


class CPU(Common):
    def __init__(self):
        super().__init__()
        self.set_attributes(CPU_ATTRIBUTES)

    def __str__(self):
        return '{}'.format(self.compatible)


RAM_ATTRIBUTES = []


class RAM(Common):
    def __init__(self):
        super().__init__()
        self.set_attributes(RAM_ATTRIBUTES)


INTC_ATTRIBUTES = ['path','compatible',  'intc', 'master', 'slave']


class INTC(Common):
    def __init__(self):
        super().__init__()
        self.set_attributes(INTC_ATTRIBUTES)

    def __str__(self):
        return '{}'.format(self.compatible)


UART_ATTRIBUTES = [
    'path', 'compatible', 'id',
    'irqn', 'baud_rate', 'base', 'size',
    'endian', 'intp'
]


class UART(Common):
    def __init__(self):
        super().__init__()
        self.set_attributes(UART_ATTRIBUTES)

    def __str__(self):
        return '{} -> {}({})'.format(self.compatible, self.intp, self.irqn)


BAMBOO_ATTRIBUTES = ['path', 'compatible', 'base', 'size']


class Bamboo(Common):
    def __init__(self):
        super().__init__()
        self.set_attributes(BAMBOO_ATTRIBUTES)

    def __str__(self):
        return '{}'.format(self.compatible)


MACHINE_ATTRIBUTES = [
    'machine_id', 'compatible', 'nvram', 'cmdline',
    'cpus', 'ram', 'intcs', 'timer', 'uarts', 'bamboos'
]


class Machine(Common):
    def __init__(self):
        super().__init__()
        self.set_attributes(MACHINE_ATTRIBUTES)

    def __str__(self):
        c = '{}'.format(self.compatible)
        s = ''
        for cpu in self.cpus:
            s += '{}: CPU {}\n'.format(c, cpu)
        for intc in self.intcs:
            s += '{}: INTC {}\n'.format(c, intc)
        for uart in self.uarts:
            s += '{}: UART {}\n'.format(c, uart)
        return s

    def parse_dts(self, dts):
        self.compatible = find_compatible_in_fdt(dts)

        self.cpus = []
        for k, v in find_flatten_cpu_in_fdt(dts).items():
            cpu = CPU()
            cpu.set_path(k)
            cpu.set_attributes(attrs=v)
            self.cpus.append(cpu)

        flatten_intc_tree = find_flatten_intc_tree_in_fdt(dts)
        flatten_mmio = find_flatten_mmio_in_fdt(dts)
        flatten_uart = find_flatten_uart_in_fdt(dts, flatten_intc_tree=flatten_intc_tree, flatten_mmio=flatten_mmio)

        self.intcs = []
        for k, v in flatten_intc_tree.items():
            if not v['intc']:
                continue
            intc = INTC()
            intc.set_path(k)
            intc.set_attributes(attrs=v)
            self.intcs.append(intc)

        self.uarts = []
        for uid, v in enumerate(flatten_uart):
            uart = UART()
            v['intp'] = find_intc_by_phandle(dts, v['intp'])['compatible']
            uart.set_attributes(attrs=v)
            uart.set_id(uid)
            self.uarts.append(uart)

        self.bamboos = []
        for k, v in flatten_mmio.items():
            if k in flatten_uart:
                continue
            if k in flatten_intc_tree and \
                    flatten_intc_tree[k]['intc']:
                continue
            bamboo = Bamboo()
            bamboo.set_attributes(attrs=v)
            self.bamboos.append(bamboo)

