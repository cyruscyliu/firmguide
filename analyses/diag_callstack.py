from analyses.analysis import Analysis
from analyses.diag_tracing import LoadTrace
from capstone import *
import struct


class InstRender:
    def __init__(self):
        self.md_arm = Cs(CS_ARCH_ARM, CS_MODE_ARM)
        self.md_arm.detail = True
        self.md_thumb = Cs(CS_ARCH_ARM, CS_MODE_THUMB)
        self.md_thumb.detail = True

    def cs_inst_arm(self, raw, address):
        raw_bytes = struct.pack('I', int(raw, 16))
        for i in self.md_arm.disasm(raw_bytes, address):
            return i

    def cs_inst_thumb(self, raw, address):
        raw_bytes = struct.pack('I', int(raw, 16))
        for i in self.md_thumb.disasm(raw_bytes, address):
            return i


class CallRecord(object):
    def __init__(self, pc, ir, cpurf=None, bb=None):
        self.where_to_be_called = pc
        self.where_to_return = ir
        self.bb = bb
        self.cpurf = cpurf

    def __str__(self):
        a = 'line {} jump at 0x{:x} and should return to 0x{:x}'.format(
            self.cpurf['ln'], self.where_to_be_called, self.where_to_return)
        return a


class CallStack(Analysis):
    def run(self, firmware):
        trace = self.analysis_manager.get_analysis('load_trace')
        assert isinstance(trace, LoadTrace)
        pql = trace.pql

        inst_render = InstRender()
        callstack = []
        guard = 0
        for k, cpurf in pql.cpurfs.items():
            if k < guard:
                continue
            bb = pql.get_bb(cpurf, pql.bbs)
            for instruction in bb['instructions']:
                cs_instruction = inst_render.cs_inst_arm(instruction['raw'], int(instruction['address'], 16))
                if cs_instruction.mnemonic == 'bl':
                    next_cpurf = pql.get_next_cpurf(cpurf, pql.cpurfs)
                    # lr = next_cpurf['register_files']['R14']  # str
                    lr = cs_instruction.address + 4
                    returned = False
                    # if the jump is not taken
                    next_bb = pql.get_bb(next_cpurf, pql.bbs)
                    if int(next_bb['in'], 16) == int(bb['in'], 16) + 4 * bb['size']:
                        continue
                    for cpurf2 in pql.get_next_cpurf_from(k, pql.cpurfs):
                        bb2 = pql.get_bb(cpurf2, pql.bbs)
                        if int(bb2['in'], 16) == lr:
                            returned = True
                            guard = cpurf2['id']
                            break
                    if not returned:
                        callstack.append(CallRecord(cs_instruction.address, lr, cpurf=cpurf, bb=bb))
        for call_record in callstack:
            self.info(firmware, call_record.__str__(), 1)

        return True

    def __init__(self, analysis_manager):
        super().__init__(analysis_manager)
        self.name = 'callstack'
        self.description = 'show callstack in the trace'
        self.context['hint'] = 'bad bad bad trace'
        self.critical = False
        self.required = ['check']