"""
The code generator interface for upper device profile layer.
"""
import abc

from generation.generations.compilers import CompilerToQEMUMachine


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
    def iget_ram_size(self):
        pass

    @abc.abstractmethod
    def sget_cpu_model(self):
        pass


class TestFirmware(CodeGenerationInterface):

    def sget_machine_description(self):
        return 'hello salamander'

    def sget_machine_name(self):
        return 'salamander'

    def sget_architecture(self):
        return 'arm'

    def iget_ram_size(self):
        return 32

    def sget_cpu_model(self):
        return 'arm926'


if __name__ == '__main__':
    # this is just a test case
    firmware = TestFirmware()
    # after get_timer_info
    machine_compiler = CompilerToQEMUMachine()
    machine_compiler.solve(firmware)
    machine_compiler.link(firmware)
    machine_compiler.install(firmware)
    machine_compiler.run(firmware)
