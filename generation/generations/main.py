"""
The code generator interface for upper device profile layer.
"""
import yaml

from generation.generations.compilers import CompilerToQEMUMachine
from profile.simple import SimpleFirmware

if __name__ == '__main__':
    # test nas7820
    prepare_nas7820 = 'dd if=2b38a390ba53209a1fa4c6aed8489c14774db4c9.bin of=fitimage bs=1 skip=655360\n' \
                      'dumpimage -T flat_dt -i fitimage -p 0 nas7820.kernel\n' \
                      'dumpimage -T flat_dt -i fitimage -p 1 nas7820.dtb\n' \
                      'mkimage -A arm -C none -O linux -T kernel -d nas7820.kernel -a 0x8000 -e 0x8000 nas7820.uImage\n' \
                      './arm-softmmu/qemu-system-arm -M nas7820 -kernel ../13882/nas7820.uImage -dtb ../13882/nas7820.dtb -nographic'
    firmware = SimpleFirmware(uuid=0, name=None, path=None, size=0)
    firmware.profile = yaml.safe_load(open('samples/nas7820.yaml'))
    machine_compiler = CompilerToQEMUMachine()
    machine_compiler.solve(firmware)
    machine_compiler.link(firmware)
    machine_compiler.install(firmware)
    machine_compiler.run(firmware)
    print(prepare_nas7820)
    firmware.profile = yaml.safe_load(open('samples/wrt320n_v1.yaml'))
    machine_compiler = CompilerToQEMUMachine()
    machine_compiler.solve(firmware)
    machine_compiler.link(firmware)
    machine_compiler.install(firmware)
    machine_compiler.run(firmware)
    # print(prepare_nas7820)
