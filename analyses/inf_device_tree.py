import fdt

from analyses.analysis import Analysis
from database.dbf import get_database


class DeviceTree(Analysis):
    def get_path_to(self, name):
        path_to = []
        for pa, no, pros in self.dts.walk():
            if pa.find(name) == -1:
                continue
            compatible = self.dts.get_property('compatible', pa)
            if compatible is None:
                continue
            path_to.append(pa)

        if len(path_to) == 0:
            return None
        elif len(path_to) > 1:
            # if there are more than 1 uarts we will use the first one by default
            path_to_uart = path_to[0]
        else:
            path_to_uart = path_to[0]
        return path_to_uart

    def cpu07_parse_cpu_from_device_tree(self, firmware):
        path_to_cpu = self.get_path_to('cpu')

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
        self.info(firmware, 'interrupt controller mmio region {} found'.format(ic_registers), 1)
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

    def uart09_parse_uart_from_device_tree(self, firmware):
        path_to_uart = self.get_path_to('uart')
        if path_to_uart is None:
            self.info(firmware, 'there is no uart in this device tree', 0)
            return False

        compatible = self.dts.get_property('compatible', path_to_uart).data[0]
        firmware.set_uart_name(compatible, firmware.get_uart_num())
        self.info(firmware, 'uart model {} found'.format(compatible), 1)

        uart_mmio_base, _ = self.dts.get_property('reg', path_to_uart).data
        firmware.set_uart_mmio_base(str(hex(uart_mmio_base)), firmware.get_uart_num())
        self.info(firmware, 'uart mmio base {} found'.format(hex(uart_mmio_base)), 1)

        uart_baud_rate = self.dts.get_property('current-speed', path_to_uart).data[0]
        firmware.set_uart_baud_rate(str(hex(uart_baud_rate)), firmware.get_uart_num())
        self.info(firmware, 'uart baud rate {} found'.format(hex(uart_baud_rate)), 1)

        uart_reg_shift = self.dts.get_property('reg-shift', path_to_uart).data[0]
        firmware.set_uart_reg_shift(str(hex(uart_reg_shift)), firmware.get_uart_num())
        self.info(firmware, 'uart reg shift {} found'.format(hex(uart_reg_shift)), 1)

        _, uart_irq, _ = self.dts.get_property('interrupts', path_to_uart).data
        firmware.set_uart_irq(str(hex(uart_irq)), firmware.get_uart_num())
        self.info(firmware, 'uart reg irq {} found'.format(hex(uart_irq)), 1)

        firmware.set_uart_num(firmware.get_uart_num() + 1)

    def run(self, firmware):
        dtb = firmware.get_path_to_dtb()
        if dtb is None:
            self.context['input'] = 'assign the path to the device tree blob'
            return False
        with open(dtb, 'rb') as f:
            dtb = f.read()
        self.dts = fdt.parse_dtb(dtb)

        model = self.dts.get_property('model').data[0]
        firmware.set_machine_name('_'.join(model.split()).lower())

        self.cpu07_parse_cpu_from_device_tree(firmware)

        # check whether the cpu private peripheral is supported or not
        cpu = firmware.get_cpu_model()
        cpu_pp_name = self.qemu_devices.select('cpu_private', like=cpu)
        if cpu_pp_name is not None:
            firmware.set_cpu_pp_name(cpu_pp_name)
            self.info(firmware, 'cpu private peripheral {} found'.format(cpu_pp_name), 1)
        self.ic01_parse_ic_from_device_tree(firmware)

        self.uart09_parse_uart_from_device_tree(firmware)

        # firmware.set_dts(dts)
        self.info(firmware, 'merge the device tree to our profile', 1)
        return True

    def __init__(self, analysis_manager):
        super().__init__(analysis_manager)
        self.name = 'dt'
        self.description = 'parse firmware\'s device tree'
        self.required = ['extraction', 'strings']
        self.context['hint'] = 'device tree is not available'
        self.critical = False
        self.settings = ['dtc']
        #
        self.dts = None
        self.qemu_devices = get_database('qemu.devices')
