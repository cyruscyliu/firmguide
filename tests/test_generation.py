from unittest import TestCase

import os
import yaml

from generation.compiler import CompilerToQEMUMachine
from profile.simple import SimpleFirmware


class TestGeneration(TestCase):
    def test_nas7820(self):
        # test nas7820
        firmware = SimpleFirmware(uuid=0, name=None, path=None, size=0)
        with open('tests/machines/nas7820.yaml') as f:
            firmware.profile = yaml.safe_load(f)
        machine_compiler = CompilerToQEMUMachine()
        machine_compiler.solve(firmware)
        machine_compiler.link(firmware)
        machine_compiler.install(firmware)
        # machine_compiler.run(firmware)
        # os.system('dd if=tests/files/2b38a390ba53209a1fa4c6aed8489c14774db4c9.bin '
        #           'of=tests/files/fitimage bs=1 skip=655360 >/dev/null 2>&1')
        # os.system('dumpimage -T flat_dt -i tests/files/fitimage -p 0 tests/files/nas7820.kernel >/dev/null 2>&1')
        # os.system('dumpimage -T flat_dt -i tests/files/fitimage -p 1 tests/files/nas7820.dtb >/dev/null 2>&1')
        # os.system('mkimage -A arm -C none -O linux -T kernel -d tests/files/nas7820.kernel -a 0x8000 -e 0x8000 '
        #           'tests/files/nas7820.uImage >/dev/null 2>&1')
        os.system('cd build/qemu-4.0.0 && make -j4')
        os.system('build/qemu-4.0.0/arm-softmmu/qemu-system-arm '
                  '-M nas7820 -kernel tests/files/nas7820.uImage -dtb tests/files/nas7820.dtb -nographic')

    def test_wrt320n_n1(self):
        firmware = SimpleFirmware(uuid=0, name=None, path=None, size=0)
        with open('tests/machines/wrt320n_v1.yaml') as f:
            firmware.profile = yaml.safe_load(f)
        machine_compiler = CompilerToQEMUMachine()
        machine_compiler.solve(firmware)
        machine_compiler.link(firmware)
        machine_compiler.install(firmware)
        # machine_compiler.run(firmware)
        os.system('cd build/qemu-4.0.0 && make -j4')
        os.system('build/qemu-4.0.0/mipsel-softmmu/qemu-system-mipsel '
                  '-M wrt320n_v1 -kernel tests/files/vmlinux.elf '
                  '-drive file=tests/files/rootfs.fill,if=pflash,format=raw'
                  ' -nographic')

    def test_wrt350n_v2(self):
        firmware = SimpleFirmware(uuid=0, name=None, path=None, size=0)
        with open('tests/machines/wrt350n_v2.yaml') as f:
            firmware.profile = yaml.safe_load(f)
        machine_compiler = CompilerToQEMUMachine()
        machine_compiler.solve(firmware)
        machine_compiler.link(firmware)
        machine_compiler.install(firmware)
        # machine_compiler.run(firmware)
        # os.system(
        #     'dd if=tests/files/ec5859077831e078987ebb05461d4ec834896f3e.bin of=tests/files/uImage bs=1 count=889320')
        os.system(
            'build/qemu-4.0.0/arm-softmmu/qemu-system-arm '
            '-M wrt350n_v2 '
            '-kernel tests/files/uImage '
            '-drive file=tests/files/ec5859077831e078987ebb05461d4ec834896f3e.bin,format=raw,if=pflash '
            '-nographic'
        )
