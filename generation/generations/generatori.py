import abc


class CodeGenerationInterface(object):
    @abc.abstractmethod
    def sget_flash_base(self):
        pass

    @abc.abstractmethod
    def sget_machine_description(self):
        pass

    @abc.abstractmethod
    def sget_machine_name(self):
        pass

    @abc.abstractmethod
    def sget_architecture(self):
        pass

    @abc.abstractmethod
    def sget_ram_size(self):
        pass

    @abc.abstractmethod
    def sget_cpu_model(self):
        pass

    @abc.abstractmethod
    def probe_cpu_pp_model(self):
        pass

    @abc.abstractmethod
    def sget_cpu_pp_mmio_base(self):
        pass

    @abc.abstractmethod
    def sget_uart_mmio_base(self):
        pass

    @abc.abstractmethod
    def sget_uart_baud_rate(self):
        pass

    @abc.abstractmethod
    def sget_uart_reg_shift(self):
        pass

    @abc.abstractmethod
    def sget_uart_irq(self):
        pass

    @abc.abstractmethod
    def lget_bamboo_devices(self):
        pass

    @abc.abstractmethod
    def sget_board_id(self):
        pass

    @abc.abstractmethod
    def sget_path_to_kernel(self):
        pass

    @abc.abstractmethod
    def sget_flash_type(self):
        pass

    @abc.abstractmethod
    def sget_flash_size(self):
        pass

    @abc.abstractmethod
    def sget_flash_section_size(self):
        pass
