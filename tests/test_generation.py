from unittest import TestCase

import os
import yaml
import signal

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
        os.system('dd if=tests/files/2b38a390ba53209a1fa4c6aed8489c14774db4c9.bin '
                  'of=tests/files/fitimage bs=1 skip=655360 >/dev/null 2>&1')
        os.system('dumpimage -T flat_dt -i tests/files/fitimage -p 0 tests/files/nas7820.kernel >/dev/null 2>&1')
        os.system('dumpimage -T flat_dt -i tests/files/fitimage -p 1 tests/files/nas7820.dtb >/dev/null 2>&1')
        os.system('mkimage -A arm -C none -O linux -T kernel -d tests/files/nas7820.kernel -a 0x8000 -e 0x8000 '
                  'tests/files/nas7820.uImage >/dev/null 2>&1')
        # os.system('cd build/qemu-4.0.0 && make -j4')
        import subprocess
        process = subprocess.Popen(
            'build/qemu-4.0.0/arm-softmmu/qemu-system-arm '
            '-M nas7820 -kernel tests/files/nas7820.uImage -dtb tests/files/nas7820.dtb -nographic', shell=True)

    def test_wrt320n_n1(self):
        firmware = SimpleFirmware(uuid=0, name=None, path=None, size=0)
        with open('tests/machines/wrt320n_v1.yaml') as f:
            firmware.profile = yaml.safe_load(f)
        machine_compiler = CompilerToQEMUMachine()
        machine_compiler.solve(firmware)
        machine_compiler.link(firmware)
        machine_compiler.install(firmware)
        machine_compiler.run(firmware)
        # print(prepare_nas7820)

    def test_wrt350n_v2(self):
        firmware = SimpleFirmware(uuid=0, name=None, path=None, size=0)
        firmware.profile = yaml.safe_load(open('samples/wrt350n_v2.yaml'))
        machine_compiler = CompilerToQEMUMachine()
        machine_compiler.solve(firmware)
        machine_compiler.link(firmware)
        machine_compiler.install(firmware)
        machine_compiler.run(firmware)
