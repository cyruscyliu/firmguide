#!/usr/bin/python3.7

import struct
from capstone import *

# Currently, this python support ARM32 little endian (without thumb)

'''
Now run this reader.py, you get sth like this:

r0=00000000 r1=00000000 r2=00000000 r3=00000000   r4=00000000   r5=00000000
r6=00000000 r7=00000000 r8=00000000 r9=00000000  r10=00000000   fp=00000000
ip=00000000 sp=00000000 lr=00000000 pc=00000000 cspr=400001d3 xspr=40000000
0x0:    mov     r0, #0
0x4:    ldr     r1, [pc, #4]
0x8:    ldr     r2, [pc, #4]
0xc:    ldr     pc, [pc, #4]

'''

# ARM

BLOCK_ADDR, INSN_START, INSN_END, \
R0, R1, R2, R3, R4, R5, \
R6, R7, R8, R9, R10, FP, \
IP, SP, LR, PC, CPSR, XPSR = list(range(0, 21))

def parse_one_unit_trace(block_idx, ctx, exec):
    ctx_off = 21 * 4 * block_idx
    ctx.seek(ctx_off)
    ctx_unit = struct.unpack('<IIIIIIIIIIIIIIIIIIIII', ctx.read(21 * 4))
    #print(ctx_unit)

    exec_off = 1 * 4 * ctx_unit[INSN_START]
    exec.seek(exec_off)
    exec_units = exec.read(4 * (ctx_unit[INSN_END] - ctx_unit[INSN_START]))

    print("r0=%08x r1=%08x r2=%08x r3=%08x   r4=%08x   r5=%08x" % (ctx_unit[R0], ctx_unit[R1], ctx_unit[R2], ctx_unit[R3], ctx_unit[R4], ctx_unit[R5]) )
    print("r6=%08x r7=%08x r8=%08x r9=%08x  r10=%08x   fp=%08x" % (ctx_unit[R6], ctx_unit[R7], ctx_unit[R8], ctx_unit[R9], ctx_unit[R10], ctx_unit[FP]) )
    print("ip=%08x sp=%08x lr=%08x pc=%08x cspr=%08x xspr=%08x" % (ctx_unit[IP], ctx_unit[SP], ctx_unit[LR], ctx_unit[PC], ctx_unit[CPSR], ctx_unit[XPSR]) )

    cs = Cs(CS_ARCH_ARM, CS_MODE_ARM | CS_MODE_LITTLE_ENDIAN)
    for insn in cs.disasm(exec_units, ctx_unit[BLOCK_ADDR]):
        print("0x%x:\t%s\t%s" % (insn.address, insn.mnemonic, insn.op_str))
    print("")

