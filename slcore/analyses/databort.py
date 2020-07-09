import struct

from capstone.mips_const import MIPS_OP_REG, MIPS_OP_IMM, MIPS_OP_MEM
from slcore.amanager import Analysis
from capstone import *


def get_raw_code(address, bb):
    instruction = None
    for instruction in bb['instructions']:
        if int(instruction['address'], 16) == address:
            break
    return instruction['raw']

def get_readable_code(address, bb):
    instruction = None
    for instruction in bb['instructions']:
        if int(instruction['address'], 16) == address:
            break
    return ' '.join([instruction['opcode']] + instruction['operand'])


def get_instruction(address, bb):
    instruction = None
    for instruction in bb['instructions']:
        if int(instruction['address'], 16) == address:
            break
    return ' '.join([instruction['opcode'], ' '.join(instruction['operand'])])


class CheckDataAbort(Analysis):
    def handle_arm_dabt(self, pql):
        dabts = []
        for k, cpurf in pql.get_cpurf():
            if 'exception' in cpurf and \
                    'type' in cpurf['exception'] and cpurf['exception']['type'] == 'dabt':
                dabts.append(cpurf)

        if not len(dabts):
            self.error_info = 'no data abort'
            return True

        for cpurf in dabts[:10]:
            # dabt
            # current bb has where to abort -> next bb has where to return
            if pql.get_exception_return_cpurf(cpurf) is None:
                self.info('line {}:0x{} has a data abort at {}, return abnormally'.format(
                    cpurf['ln'], cpurf['register_files']['R15'], cpurf['register_files']['DFAR']), 1)
            else:
                self.info('line {}:0x{} has a data abort at {}, return normally'.format(
                    cpurf['ln'], cpurf['register_files']['R15'], cpurf['register_files']['DFAR']), 1)
                next_cpurf = pql.get_next_cpurf(cpurf)
                where_to_return = int(next_cpurf['register_files']['R14'], 16) - 8
                self.info('the program should re-entry 0x{:x} {}'.format(
                    where_to_return, get_instruction(where_to_return, pql.get_bb(cpurf))), 1)
                if int(cpurf['register_files']['DFAR'], 16) == 0:
                    self.info('kernel panic by accessing 0', 1)
                    continue
                self.dead_addresses.append(cpurf['register_files']['DFAR'])
        return True

    def handle_mips_dabt(self, pql):
        dbes = []
        for k, cpurf in pql.get_cpurf():
            if 'exception' in cpurf and 'type' in cpurf['exception'] and \
                    cpurf['exception']['type'] == 'dbe':
                dbes.append(cpurf)

        if not len(dbes):
            self.debug('there is no data abort', 1)
            return True

        for cpurf in dbes[:10]:
            # current cpurf tells us where to return
            # and current bb tells us where to abort
            where_to_return = cpurf['register_files']['EPC']
            self.info('line {}:0x{} has a data abort at PC {}'.format(
                cpurf['ln'], cpurf['register_files']['pc'], where_to_return), 1)
            bb = pql.get_bb(cpurf)
            where_to_return = int(where_to_return, 16)

            instruction = get_raw_code(where_to_return, bb)
            cs = Cs(CS_ARCH_MIPS, CS_MODE_MIPS32)
            cs.detail = True
            for cs_instruction in cs.disasm(struct.pack('I', int(instruction, 16)), where_to_return):
                c = -1
                for operand in cs_instruction.operands:
                    c += 1
                    if operand.type == MIPS_OP_MEM:
                        if operand.mem.base != 0:
                            base = cs_instruction.reg_name(operand.mem.base)
                        else:
                            continue
                        disp = operand.mem.disp
                        bad_addr = int(cpurf['register_files'][base], 16) + disp
                        self.dead_addresses.append(hex(bad_addr))
                        self.info('line {}:0x{} has a data abort at 0x{:x}'.format(
                            cpurf['ln'], cpurf['register_files']['pc'], bad_addr), 1)
            self.info('please also check next instruction {}'.format(
                      get_readable_code(where_to_return + 4, bb)), 1)
        return True

    def run(self, **kwargs):
        self.dead_addresses = []

        trace = self.analysis_manager.get_analysis('loadtrace')
        pql = trace.pql

        if self.firmware.get_arch() == 'arm':
            return self.handle_arm_dabt(pql)
        else:
            return self.handle_mips_dabt(pql)

    def __init__(self, analysis_manager):
        super().__init__(analysis_manager)
        self.name = 'databort'
        self.description = 'Find data abort info.'
        self.critical = False
        self.required = ['userlevel', 'fastuserlevel', 'loadtrace']
        self.type = 'diag'
        #
        self.dead_addresses = []
