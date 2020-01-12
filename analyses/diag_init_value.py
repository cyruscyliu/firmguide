"""
This analysis combines backwards slicing and symbolic execution
"""
import struct

from pyqemulog import PQLI

from analyses.analysis import Analysis
from analyses.diag_tracing import LoadTrace

from z3 import *
from capstone import *
from capstone.mips import *


def iv_solver(*args, **kwargs):
    s = Solver()
    s.set(**kwargs)
    s.add(*args)

    r = s.check()
    if r == unsat:
        return None
    elif r == unknown:
        return None
    else:
        return s.model()


class InitValueI(object):
    def __init__(self):
        self.md = None

        # reg_name(i.reg) as keys
        # init as the new cpurf comes
        self.cpu_state = {}

        self.symbols = {}
        self.tainted = []
        self.constraints = []
        self.callbacks = {}

        # state control
        self.start = None
        self.stop = False
        self.cease = False
        self.save = True

        # backward slicing
        self.selected_instructions = []
        self.ordered_selected_instructions = []

        # constraint solving
        self.model = None
        self.cs_f = 'self.model = self.iv_solver(Not(And({})))\n'

    def _backward_slicing(self, cpurf, bb):
        order_reserved_instructions = []
        for instruction in bb['instructions']:
            for insn in self.md.disasm(
                    struct.pack('I', int(instruction['raw'], 16)),
                    int(instruction['address'], 16)):
                if insn.mnemonic in self.callbacks:
                    self.callbacks[insn.mnemonic](insn)
                else:
                    self.callbacks['other'](insn)
            if self.save:
                order_reserved_instructions.append(instruction)
            if self.stop:
                self.start = int(cpurf['instructions'][0]['address'], 16)
                break
        return order_reserved_instructions

    def update_cpurf(self, cpurf):
        self.cpu_state = {}
        for k, v in cpurf['register_files']:
            self.cpu_state[k.lower()] = int(v, 16)

    def backward_slicing(self, pql, cpurf):
        # accept starting cpurf
        while cpurf:
            # 1) no need to analysis start bb
            if int(cpurf['in'], 16) == self.start:
                continue
            # 2) find the tainted instructions
            self.cease = False
            bb = pql.get_bb(cpurf)
            # update cpurf before going on
            self.update_cpurf(cpurf)
            oris = self._backward_slicing(cpurf, bb)
            self.selected_instructions.append(oris)
            if self.cease:
                break
            cpurf = pql.get_last_cpurf(cpurf)

        # re-order
        for ti in reversed(self.selected_instructions):
            for instruction in ti:
                self.ordered_selected_instructions.append(instruction)

    def symbolic_execution(self):
        for instruction in self.ordered_selected_instructions:
            for insn in self.md.disasm(
                    struct.pack('I', int(instruction['raw'], 16)), int(instruction['address'], 16)):
                if insn.mnemonic == 'bne':
                    self.callbacks['bne'](insn, taken=instruction['taken'], se=True)
                elif insn.mnemonic in self.callbacks:
                    self.callbacks[insn.mnemonic](insn)
                else:
                    self.callbacks['other'](insn)

    def constraint_solving(self):
        # [+] symbol {} from 0x{:x}'.format(
        #   symbol['reg_name'], symbol['base'] + symbol['offset'])

        # collect the constraint
        css = []
        for constraint in self.constraints:
            cs = constraint['constraint']
            # '[+] constraint {}'.format(constraint['constraint'])
            css.append(cs)

        exec(self.cs_f.format(','.join(css)))
        assert isinstance(self.model, ModelRef)

        feedback = {}
        for result in self.model:
            for k, symbol in self.symbols.items():
                if symbol['reg_name'] == result.name():
                    # '[+] init value for 0x{:x} is'.format(
                    #   symbol['base'] + symbol['offset']), model[result]
                    feedback[symbol['base'] + symbol['offset']] = self.model[result]
        return feedback


class ARM32InitValue(InitValueI):
    pass


class MIPSInitValue(InitValueI):
    def mips_addiu(self, insn):
        # ADDIU rt, rs, imm
        assert isinstance(insn, CsInsn)

        rt = insn.operands[0].reg
        rs = insn.operands[1].reg
        imm = insn.operands[2].imm

        self.cpu_state[insn.reg_name(rt)] = self.cpu_state[insn.reg_name(rs)] + imm

    def mips_lui(self, insn):
        # LUI rt, imm
        assert isinstance(insn, CsInsn)

        rt = insn.operands[0].reg
        imm = insn.operands[1].imm
        self.cpu_state[insn.reg_name(rt)] = imm

    def mips_lw(self, insn):
        # LW rt, offset(base)
        assert isinstance(insn, CsInsn)

        rt = insn.operands[0].reg
        base = self.cpu_state[insn.reg_name(insn.operands[1].mem.base)]
        offset = insn.operands[1].mem.disp

        self.symbols[rt] = {'type': 'mmio', 'base': base, 'offset': offset, 'reg_name': insn.reg_name(rt)}

        self.cease = True

    def mips_bne(self, insn, taken=False, se=False):
        # BNE rs, rt, offset
        assert isinstance(insn, CsInsn)

        rs = insn.operands[0].reg
        rt = insn.operands[1].reg
        offset = insn.operands[2].imm

        self.tainted.append(rs)
        self.tainted.append(rt)

        if se:
            if rs not in self.symbols:
                rs = self.cpu_state[insn.reg_name(rs)]
            else:
                rs = 'Int(\'{}\')'.format(insn.reg_name(rs))
            if rt not in self.symbols:
                rt = self.cpu_state[insn.reg_name(rt)]
            else:
                rt = 'Int(\'{}\')'.format(insn.reg_name(rt))
            if taken:
                constraint = {'constraint': '{} != {}'.format(rs, rt), 'target': offset}
            else:
                constraint = {'constraint': '{} == {}'.format(rs, rt), 'target': offset}
            self.constraints.append(constraint)

        if offset == self.start:
            self.stop = True

        return offset

    def mips_jal(self, insn):
        # JAL target
        assert isinstance(insn, CsInsn)

        target = insn.operands[0].imm

        # no need to select following insns
        if self.start == target:
            self.stop = True

    def mips_other(self, insn):
        assert isinstance(insn, CsInsn)

        regs = []
        for i in insn.operands:
            if i.type == MIPS_OP_REG:
                regs.append(i.reg)

        for reg in regs:
            if reg in self.tainted:
                self.save = True
        self.save = False

    def __init__(self):
        super().__init__()
        self.callbacks = {
            'lui': self.mips_lui, 'addiu': self.mips_addiu,
            'jal': self.mips_jal, 'bne': self.mips_bne, 'lw': self.mips_lw,
            'other': self.mips_other}
        self.md = Cs(CS_ARCH_MIPS, CS_MODE_MIPS32 + CS_MODE_LITTLE_ENDIAN)
        self.md.detail = True


class InitValue(Analysis):
    def run(self, firmware):
        trace = self.analysis_manager.get_analysis('load_trace')
        assert isinstance(trace, LoadTrace)
        pql = trace.pql
        assert isinstance(pql, PQLI)

        panic_cpurf = self.analysis_manager.get_analysis('panic').panic_cpurf
        if panic_cpurf is None:
            self.context['input'] = 'there is no panic'
            return False

        if firmware.get_architecture() == 'arm':
            self.init_value = ARM32InitValue()
        elif firmware.get_architecture() == 'mips':
            self.init_value = MIPSInitValue()
        else:
            self.context['input'] = 'cannot support this architecture'
            return False

        self.init_value.start = int(panic_cpurf['in'], 16)
        self.init_value.backward_slicing(pql, panic_cpurf)
        self.init_value.symbolic_execution()
        self.feedback = self.init_value.constraint_solving()
        return True

    def __init__(self, analysis_manager):
        super().__init__(analysis_manager)
        self.name = 'init_value'
        self.description = 'solve the init value for a certain register'
        self.context['hint'] = 'very difficult program analysis'
        self.critical = False
        self.required = ['panic']
        self.type = 'diag'
        #
        self.init_value = None
        self.feedback = {}
