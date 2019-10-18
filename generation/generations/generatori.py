import abc


class CodeGenerationInterface(object):
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
    def lget_bamboo_devices(self):
        pass

    @abc.abstractmethod
    def sget_board_id(self):
        pass

    @abc.abstractmethod
    def sget_path_to_kernel(self):
        pass
