from generation.arm_compiler import ARMCompiler
from generation.mips_compiler import MIPSCompiler


def get_compiler(firmware):
    architecture = firmware.get_architecture()
    if architecture == 'arm':
        return ARMCompiler(firmware)
    elif architecture == 'mips':
        return MIPSCompiler(firmware)
    else:
        raise NotImplementedError
