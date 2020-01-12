from analyses.analysis import Analysis
from analyses.diag_tracing import LoadTrace
from capstone import *
import struct


class CallRecord(object):
    def __init__(self, pc, ir, ignored=False, returned=False, cpurf=None, bb=None):
        self.where_to_be_called = pc
        self.where_to_return = ir
        self.ignored = ignored


class CallStackI(object):
    def __init__(self):
        self.md = None
        self.guard = 0

        self.callstack = []
        self.callbacks = {}

        # status
        self.ret = False

    def construct(self, pql):
        for k, cpurf in pql.cpurfs.items():
            if k < self.guard:
                continue

            self.ref = False
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

                    # the jump must be taken
                    # unless it is ignored by qemu
                    next_cpurf = pql.get_next_cpurf(cpurf)
                    next_bb = pql.get_bb(next_cpurf)
                    bb = pql.get_bb(cpurf)
                    if int(next_bb['in'], 16) == lr:
                        self.ret = True
                        self.guard = next_cpurf['id']
                        self.callstack.append(CallRecord(insn.address, lr, ignored=True, returned=True))
                        break

                    # otherwise find return bb in the future
                    for cpurf2 in pql.get_next_cpurf_from(k):
                        bb2 = pql.get_bb(cpurf2, pql.bbs)
                        if int(bb2['in'], 16) == lr:
                            self.ret = True
                            self.guard = cpurf2['id']
                            self.callstack.append(CallRecord(insn.address, lr, ignored=False, returned=True))
                            break
                    if not self.ret:
                        break
                if self.ret:
                    break
            if self.ret:
                break


class ARMCallStack(CallStackI):
    def arm_bl(self, insn):
        return insn.address + 4

    def __init__(self):
        super().__init__()
        self.callbacks = {'bl': self.arm_bl}


class MIPSCallStack(CallStackI):
    def mips_jal(self, insn):
        return insn.address + 8

    def __init__(self):
        super().__init__()
        self.callbacks = {'jal': self.mips_jal}


class CallStack(Analysis):
    def run(self, firmware):
        trace = self.analysis_manager.get_analysis('load_trace')
        assert isinstance(trace, LoadTrace)
        pql = trace.pql

        if firmware.get_architecture() == 'arm':
            self.callstack = ARMCallStack()
        elif firmware.get_architecture() == 'mips':
            self.callstack = MIPSCallStack()
        else:
            self.context['input'] = 'cannot support this architecture'

        self.callstack.construct(pql)
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
