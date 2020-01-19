from analyses.analysis import Analysis
from analyses.diag_tracing import LoadTrace
from capstone import *
import struct


def get_next_cpurf_from(pql, s):
    for k, cpurf in pql.cpurfs.items():
        if k <= s:
            continue
        yield cpurf


class CallRecord(object):
    def __init__(self, pc, ir, ignored=False, returned=False, cpurf=None, bb=None, indent=0):
        self.where_to_be_called = pc
        self.where_to_return = ir
        self.returned = returned
        self.cpurf = cpurf
        self.indent = indent

    def __str__(self):
        return 'ln {:5} {}0x{:x} -> 0x{:x} returned {}'.format(
            self.cpurf['ln'], self.indent * 4 * '-',
            self.where_to_be_called, self.where_to_return, self.returned == 1)


class CallStackI(object):
    def __init__(self):
        self.md = None
        self.guard = 0

        self.callstack = []
        self.callbacks = {}

        # status
        self.ret = False
        self.skip = False
        # levels
        self.level = 0

    def construct(self, pql):
        for k, cpurf in pql.cpurfs.items():
            if int(pql.get_pc(cpurf), 16) == self.guard:
                self.skip = False
            if self.skip:
                continue

            self.ret = False
            # find bl/jal instructions
            bb = pql.get_bb(cpurf)
            for instruction in bb['instructions']:
                for insn in self.md.disasm(
                        struct.pack('I', int(instruction['raw'], 16)),
                        int(instruction['address'], 16)):
                    if insn.mnemonic not in self.callbacks:
                        continue

                    # find lr
                    lr = self.callbacks[insn.mnemonic](insn)
                    self.guard = lr
                    self.skip = True

                    # an optimize way, if it returns, its bb must exist
                    if '{:08x}'.format(lr) in pql.bbs:
                        self.skip = False
                        self.ret = True

                    if not self.ret:
                        self.callstack.append(CallRecord(
                            insn.address, lr, cpurf=cpurf, returned=False, indent=self.level))
                        self.skip = False
                        break
                if self.ret:
                    break


class ARMCallStack(CallStackI):
    def arm_bl(self, insn):
        return insn.address + 4

    def __init__(self):
        super().__init__()
        self.callbacks = {'bl': self.arm_bl}
        self.md = Cs(CS_ARCH_ARM, CS_MODE_ARM + CS_MODE_LITTLE_ENDIAN)
        self.md.detail = True


class MIPSCallStack(CallStackI):
    def mips_jal(self, insn):
        return insn.address + 8

    def __init__(self):
        super().__init__()
        self.callbacks = {'jal': self.mips_jal}
        self.md = Cs(CS_ARCH_MIPS, CS_MODE_MIPS32 + CS_MODE_LITTLE_ENDIAN)
        self.md.detail = True


class CallStack(Analysis):
    def run(self, firmware):
        trace = self.analysis_manager.get_analysis('load_trace')
        assert isinstance(trace, LoadTrace)
        pql = trace.pql

        if firmware.get_architecture() == 'arm':
            callstack = ARMCallStack()
        elif firmware.get_architecture() == 'mips':
            callstack = MIPSCallStack()
        else:
            self.context['input'] = 'cannot support this architecture'
            return False

        callstack.construct(pql)
        for c in callstack.callstack:
            self.info(firmware, c.__str__(), 1)
        self.callstack = callstack.callstack
        return True

    def __init__(self, analysis_manager):
        super().__init__(analysis_manager)
        self.name = 'callstack'
        self.description = 'show callstack in the trace'
        self.context['hint'] = 'bad bad bad trace'
        self.critical = False
        self.required = ['check']
        self.type = 'diag'
        #
        self.callstack = None
