import struct

from slcore.amanager import Analysis
from capstone import Cs, CS_ARCH_ARM, CS_ARCH_MIPS,\
    CS_MODE_ARM, CS_MODE_MIPS32, CS_MODE_LITTLE_ENDIAN, \
    CS_MODE_BIG_ENDIAN


class CallRecord(object):
    def __init__(self, pc, ir, target, ignored=False,
                 returned=False, cpurf=None, bb=None, indent=0):
        self.be_called = pc
        self.to_return = ir
        self.returned = returned
        self.cpurf = cpurf
        self.bb = bb
        self.indent = indent
        self.target = target

    def __str__(self, symbol=None):
        summary = 'ln {:5} {}0x{:x} -> 0x{:x} returned {}'.format(
            self.cpurf['ln'], self.indent * 2 * '-',
            self.be_called, self.to_return, self.returned == 1)
        if symbol:
            summary = ' '.join([summary, symbol])
        return summary


class CallStackI(object):
    def __init__(self):
        self.md = None
        self.callbacks = {}
        self.guard = 0
        self.skip = False
        self.ret = False
        self.level = 0

    def find_lr(self, insn):
        return self.callbacks[insn.mnemonic](insn)

    def get_insn(self, insns):
        for instruction in insns:
            for insn in self.md.disasm(
                    struct.pack('I', int(instruction['raw'], 16)),
                    int(instruction['address'], 16)):
                yield insn

    def construct(self, pql):
        for k, cpurf in pql.cpurfs.items():
            # we will firstly skip returned functions
            if int(pql.get_pc(cpurf), 16) == self.guard:
                self.skip = False
            # if self.skip:
            #     continue
            # every basic block is assumed to be not returned
            bb = pql.get_bb(cpurf)
            for insn in self.get_insn(bb['instructions']):
                # find the bl/jal instruction and test it
                if insn.mnemonic not in self.callbacks:
                    continue
                if insn.op_str.startswith('#'):
                    target = int(insn.op_str[1:], 16)
                else:
                    target = int(insn.op_str, 16)
                # find it!
                lr = self.find_lr(insn)
                self.guard = lr
                # test it! if it returns, its bb must exist
                if '{:08x}'.format(lr) in pql.bbs:
                    self.skip = True
                    self.ret = True
                else:
                    self.skip = False
                    self.ret = False

                if self.ret:
                    continue

                yield CallRecord(
                    insn.address, lr, target, cpurf=cpurf, bb=bb,
                    returned=self.ret, indent=self.level)

                if not self.ret:
                    self.level += 1


class ARMCallStack(CallStackI):
    def arm_bl(self, insn):
        return insn.address + 4

    def __init__(self, endian):
        super().__init__()
        self.callbacks = {'bl': self.arm_bl}
        # QEMU helps us to make everything little endian
        self.md = Cs(CS_ARCH_ARM, CS_MODE_ARM + CS_MODE_LITTLE_ENDIAN)
        self.md.detail = True


class MIPSCallStack(CallStackI):
    def mips_jal(self, insn):
        return insn.address + 8

    def __init__(self, endian):
        super().__init__()
        self.callbacks = {'jal': self.mips_jal}
        # QEMU helps us to make everything little endian
        self.md = Cs(CS_ARCH_MIPS, CS_MODE_MIPS32 + CS_MODE_LITTLE_ENDIAN)
        self.md.detail = True


class ShowCallstack(Analysis):
    def address2symbol(self, address):
        srcodec = self.analysis_manager.srcodec
        if not srcodec.supported:
            self.warning('please set the source code', 1)
            return None
        return srcodec.address2symbol(address)

    def run(self, **kwargs):
        nocallstack = kwargs.pop('nocallstack')
        if nocallstack:
            self.debug('skip callstack analysis', 1)
            return True

        trace = self.analysis_manager.get_analysis('loadtrace')
        pql = trace.pql

        if self.firmware.get_arch() == 'arm':
            callstack = ARMCallStack(self.firmware.get_endian())
        elif self.firmware.get_arch() == 'mips':
            callstack = MIPSCallStack(self.firmware.get_endian())
        else:
            self.error_info = \
                'cannot support {}e{}'.format(
                    self.firmware.get_arch(), self.firmware.get_arch())
            return False

        for c in callstack.construct(pql):
            symbol_from = self.address2symbol(c.be_called)
            symbol_to = self.address2symbol(c.target)
            self.callstack.append(c)
            self.info(c.__str__(symbol='{} -> {}'.format(
                symbol_from, symbol_to)), 1)
        return True

    def __init__(self, analysis_manager):
        super().__init__(analysis_manager)
        self.name = 'callstack'
        self.description = 'Show callstack of given trace.'
        self.critical = False
        self.required = ['userlevel', 'fastuserlevel', 'loadtrace']
        self.type = 'diag'
        self.callstack = []
