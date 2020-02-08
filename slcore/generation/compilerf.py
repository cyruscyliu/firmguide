from slcore.generation.arm_compiler import ARMCompiler
from slcore.generation.mips_compiler import MIPSCompiler


def get_compiler(firmware):
    architecture = firmware.get_arch()
    if architecture == 'arm':
        return ARMCompiler(firmware)
    elif architecture == 'mips':
        return MIPSCompiler(firmware)
    else:
        raise NotImplementedError
