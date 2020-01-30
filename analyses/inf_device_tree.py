import os
import fdt

from analyses.analysis import Analysis
from slcore.database.dbf import get_database


def machine_name_wrapper(name):
    return '_'.join(name.split()).lower().replace('-', '_')

class DeviceTree(Analysis):
    def get_path_to_uart(self):
        supported_uart = ['ns16550a', 'ns8250']
        path_to = []
        for pa, no, pros in self.dts.walk():
            compatibles = self.dts.get_property('compatible', pa)
            if compatibles is None:
                continue
            for compatible in compatibles.data:
                if compatible in supported_uart:
                    path_to.append(pa)

        if len(path_to) == 0:
            return None
        return path_to

    def cpu07_parse_cpu_from_device_tree(self, firmware):
        path_to_cpu = '/cpus/cpu@0'

        compatible = self.dts.get_property('compatible', path_to_cpu).data[0]
        compatible = self.qemu_devices.select('cpu', like=compatible)
        firmware.set_cpu_model(compatible)
        self.info(firmware, 'get cpu model: {}'.format(compatible), 1)

    def ic01_parse_ic_from_device_tree(self, firmware):
        ic_parent = self.dts.get_property('interrupt-parent').data[0]
        path_to_ic = None
        for pa, no, pros in self.dts.walk():
            if len(no):
                continue
            if self.dts.exist_property('interrupt-controller', pa) \
                    and self.dts.exist_property('phandle', pa) \
                    and self.dts.get_property('phandle', pa).data[0] == ic_parent:
                path_to_ic = pa
        assert path_to_ic is not None, 'there is bugs in device parsing code'

        ic_name = self.dts.get_property('compatible', path_to_ic).data[0]
        firmware.set_interrupt_controller_name(ic_name)
        self.info(firmware, 'interrupt controller {} found'.format(ic_name), 1)

        ic_registers = self.dts.get_property('reg', path_to_ic).data
        self.info(firmware, 'interrupt controller mmio region found', 1)
        # TODO add cell analysis
        ic_mmio_base = []
        ic_mmio_size = []
        for i in range(0, len(ic_registers), 2):
            cpu_pp_name = firmware.get_cpu_pp_name()
            if cpu_pp_name == 'arm11mpcore-priv':
                cpu_pp_mmio_base = hex(ic_registers[i] & 0xFFFF0000)
                firmware.set_cpu_pp_mmio_base(cpu_pp_mmio_base)
                self.info(firmware, 'arm11mpcore-priv base {} found'.format(cpu_pp_mmio_base), 1)
            ic_mmio_base.append(hex(ic_registers[i]))
            ic_mmio_size.append(hex(ic_registers[i + 1]))
        firmware.set_interrupt_controller_mmio_base(*ic_mmio_base)
        firmware.set_interrupt_controller_mmio_size(*ic_mmio_base)

    def parse_uart_from_device_tree(self, firmware):
        path_to_uarts = self.get_path_to_uart()
        if path_to_uarts is None:
            self.info(firmware, 'there is no uart supported in this device tree', 0)
            return False

        # parse interrupt levels
        masters = self.parse_interrupt_levels(firmware)

        firmware.set_uart_num(len(path_to_uarts))
        for i, path_to_uart in enumerate(path_to_uarts):
            offset = self.get_parent_address(path_to_uart)

            compatible = self.dts.get_property('compatible', path_to_uart).data[0]
            self.used_compatibles.append(compatible)
            firmware.set_uart_name(compatible, i)
            self.info(firmware, 'uart model {} found'.format(compatible), 1)

            uart_mmio_base, _ = self.dts.get_property('reg', path_to_uart).data
            uart_mmio_base = uart_mmio_base + offset
            firmware.set_uart_mmio_base(str(hex(uart_mmio_base)), i)
            self.info(firmware, 'uart mmio base {} found'.format(hex(uart_mmio_base)), 1)

            try:
                uart_baud_rate = self.dts.get_property('current-speed', path_to_uart).data[0]
            except AttributeError as e:
                uart_baud_rate = 0x1c200
            firmware.set_uart_baud_rate(str(hex(uart_baud_rate)), i)
            self.info(firmware, 'uart baud rate {} found'.format(hex(uart_baud_rate)), 1)

            uart_reg_shift = self.dts.get_property('reg-shift', path_to_uart).data[0]
            firmware.set_uart_reg_shift(str(hex(uart_reg_shift)), i)
            self.info(firmware, 'uart reg shift {} found'.format(hex(uart_reg_shift)), 1)

            interrupt_parent = self.dts.get_property('interrupt-parent', path_to_uart).data[0]
            interrupt_cells = masters[interrupt_parent]['#interrupt-cells']
            # in the future, we must have a table to illustrate how to use the (multi-level) intc
            uart_irqs = self.dts.get_property('interrupts', path_to_uart).data
            if interrupt_cells == 1:
                uart_irq = uart_irqs[0]
            else:
                uart_irq = uart_irqs[1]  # for 11882
            firmware.set_uart_irq(str(hex(uart_irq)), i)
            self.info(firmware, 'uart reg irq {} found'.format(hex(uart_irq)), 1)

    def get_parent_address(self, path):
        # at most too levels
        node = self.dts.get_node(path)
        parent = node.parent

        if parent is None:
            return 0

        path = os.path.join(parent.path, parent.name)
        # there must be one start address
        if self.dts.exist_property('reg', path):
            return self.dts.get_property('reg', path).data[0]
        else:
            return 0

    def get_parent_address_sells(self, path):
        node = self.dts.get_node(path)
        parent = node.parent

        if parent is None:
            return self.global_address_cells

        path = os.path.join(parent.path, parent.name)
        if self.dts.exist_property('#address-cells', path):
            return self.dts.get_property('#address-cells', path).data[0]
        else:
            return self.get_parent_address_sells(os.path.join(parent.path, parent.name))

    def get_parent_size_cells(self, path):
        node = self.dts.get_node(path)
        parent = node.parent

        if parent is None:
            return self.global_size_cells

        path = os.path.join(parent.path, parent.name)
        if self.dts.exist_property('#size-cells', path):
            return self.dts.get_property('#size-cells', path).data[0]
        else:
            return self.get_parent_size_cells(path)

    def parse_mmio_io(self, firmware):
        self.global_address_cells = self.dts.get_property('#address-cells', '/').data[0]
        self.global_size_cells = self.dts.get_property('#size-cells', '/').data[0]

        duplicated_mmios = []
        if firmware.probe_cpu_pp_model():
            cpu_pp_name = firmware.get_cpu_pp_name()
            qemu_apis = get_database('qemu.apis')
            duplicated_mmios = qemu_apis.select(cpu_pp_name, 'compatibles')
        duplicated_mmios += self.used_compatibles

        firmware.load_bamboo_devices()
        for pa, no, pros in self.dts.walk():
            if pa.find('pinctrl') != -1:
                continue
            if not self.dts.exist_property('compatible', pa):
                continue
            duplicated = False
            for compatible in self.dts.get_property('compatible', pa).data:
                if compatible in duplicated_mmios:
                    duplicated = True
                    break
            if duplicated:
                continue

            size_cells = self.get_parent_size_cells(pa)
            if size_cells == 0:
                continue
            if not self.dts.exist_property('reg', pa):
                continue
            if pa == '/memory':
                continue
            address_cells = self.get_parent_address_sells(pa)
            mmios = self.dts.get_property('reg', pa).data

            # if has offsets
            offset = self.get_parent_address(pa)

            for i in range(len(mmios) // (size_cells + address_cells)):
                base = 0
                for j in range(address_cells):
                    base += mmios[i * (size_cells + address_cells) + j]
                size = 0
                for j in range(size_cells):
                    size += mmios[i * (size_cells + address_cells) + address_cells + j]
                firmware.insert_bamboo_devices(base + offset, size, value=0)
                self.info(firmware, 'find {} {} {} value=0'.format(pa, hex(base + offset), hex(size)), 1)
        firmware.update_bamboo_devices()

    def parse_interrupt_levels(self, firmware):
        intc = {}
        for pa, no, pros in self.dts.walk():
            if self.dts.exist_property('interrupt-controller', pa):
                intc_t = {
                    '#interrupt-cells': self.dts.get_property('#interrupt-cells', pa).data[0],
                }
                if not self.dts.exist_property('phandle', pa):
                    continue
                intc_t['phandle'] = self.dts.get_property('phandle', pa).data[0]
                if self.dts.exist_property('interrupt-parent', pa):
                    intc_t['master'] = False
                    intc_t['interrupt-parent'] = self.dts.get_property('interrupt-parent', pa).data[0]
                    intc_t['interrupts'] = self.dts.get_property('interrupts', pa).data
                else:
                    intc_t['master'] = True
                intc[pa] = intc_t
            else:
                if self.dts.exist_property('interrupt-parent', pa):
                    intc_t = {'interrupt-parent': self.dts.get_property('interrupt-parent', pa).data[0],
                              'interrupts': self.dts.get_property('interrupts', pa).data}
                    intc[pa] = intc_t
        level = 0
        masters = {}
        for k, v in intc.items():
            if 'master' in v:
                level += 1
                masters[v['phandle']] = v
        # 2 levels interrupt
        # {1: {'#interrupt-cells': 1, 'phandle': 1, 'master': False, 'interrupt-parent': 3, 'interrupts': [2]},
        # 3: {'#interrupt-cells': 1, 'phandle': 3, 'master': True}}
        self.info(firmware, '{} level(s) interrupt found'.format(level), 1)
        return masters

    def get_path_to_flash(self):
        supported_flash = ['cfi-flash']
        path_to = []
        for pa, no, pros in self.dts.walk():
            compatibles = self.dts.get_property('compatible', pa)
            if compatibles is None:
                continue
            for compatible in compatibles.data:
                if compatible in supported_flash:
                    path_to.append(pa)

        if len(path_to) == 0:
            return None
        return path_to

    def parse_flash_from_device_tree(self, firmware):
        path_to_flashes = self.get_path_to_flash()
        if path_to_flashes is None:
            self.info(firmware, 'there is no flash supported in this device tree', 0)
            return False

        #  compatible = "cfi-flash";
        #  reg = <0x1f000000 0x800000>;
        #  bank-width = <0x2>;
        #  device-width = <0x2>;
        #  #address-cells = <0x1>;
        #  #size-cells = <0x1>;

        # take the first one
        path_to_flash = path_to_flashes[0]
        compatible = self.dts.get_property('compatible', path_to_flash).data
        if 'cfi-flash' in compatible:
            firmware.set_flash_type('nor')

            mmios = self.dts.get_property('reg', path_to_flash).data
            address_cells = self.get_parent_address_sells(path_to_flash)
            size_cells = self.get_parent_size_cells(path_to_flash)

            for i in range(len(mmios) // (size_cells + address_cells)):
                base = 0
                for j in range(address_cells):
                    base += mmios[i * (size_cells + address_cells) + j]
                size = 0
                for j in range(size_cells):
                    size += mmios[i * (size_cells + address_cells) + address_cells + j]
                firmware.set_flash_size(hex(size))
                firmware.set_flash_base(hex(base))
                self.info(firmware, 'nor flash found, start from {}, size {}'.format(hex(base), hex(size)), 1)

    def run(self, firmware):
        dtb = firmware.get_path_to_dtb()
        if dtb is None:
            self.context['input'] = 'assign the path to the device tree blob'
            return False
        with open(dtb, 'rb') as f:
            dtb = f.read()
        self.dts = fdt.parse_dtb(dtb)

        model = self.dts.get_property('model').data[0]
        firmware.set_machine_name(machine_name_wrapper(model))

        self.cpu07_parse_cpu_from_device_tree(firmware)

        # check whether the cpu private peripheral is supported or not
        cpu = firmware.get_cpu_model()
        cpu_pp_name = self.qemu_devices.select('cpu_private', like=cpu)
        if cpu_pp_name is not None:
            firmware.set_cpu_pp_name(cpu_pp_name)
            self.info(firmware, 'cpu private peripheral {} found'.format(cpu_pp_name), 1)
        else:
            self.ic01_parse_ic_from_device_tree(firmware)

        self.parse_uart_from_device_tree(firmware)
        self.parse_flash_from_device_tree(firmware)

        self.parse_mmio_io(firmware)

        # firmware.set_dts(dts)
        self.info(firmware, 'merge the device tree to our profile', 1)
        return True

    def __init__(self, analysis_manager):
        super().__init__(analysis_manager)
        self.name = 'device_tree'
        self.description = 'parse firmware\'s device tree'
        self.required = ['extraction', 'strings']
        self.context['hint'] = 'device tree is not available'
        self.critical = False
        self.settings = ['dtc']
        #
        self.dts = None
        self.qemu_devices = get_database('qemu.devices')
        self.global_address_cells = 1
        self.global_size_cells = 1
        self.used_compatibles = []

