"""
The code generator interface for upper device profile layer.
"""
import yaml

from generation.generations.compilers import CompilerToQEMUMachine
from profile.simple import SimpleFirmware

if __name__ == '__main__':
    # this is just a test case
    firmware = SimpleFirmware(uuid=0, name=None, path=None, size=0)
    firmware.profile = yaml.safe_load(open('samples/nas7820.yaml'))
    # after get_timer_info
    machine_compiler = CompilerToQEMUMachine()
    machine_compiler.solve(firmware)
    machine_compiler.link(firmware)
    machine_compiler.install(firmware)
    machine_compiler.run(firmware)
