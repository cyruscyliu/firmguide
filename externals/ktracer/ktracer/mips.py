#!/usr/bin/python3.7

import struct
from capstone import *

# Currently, this python support MIPS32 little endian

'''
Now run with this, you get sth like this:

    zero       at       v0       v1       a0       a1       a2       a3
00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000
      t0       t1       t2       t3       t4       t5       t6       t7
00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000
      s0       s1       s2       s3       s4       s5       s6       s7
00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000
      t8       t9       k0       k1       gp       sp       s8       ra
00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000
      sr       lo       hi      bad    cause       pc      fsr      fir
00400004 00000000 00000000 00000000 00000000 80005ce0 00000000 00739300
0x80005ce0:     mfc0    $t0, $t4, 0
0x80005ce4:     lui     $at, 0x1000
0x80005ce8:     ori     $at, $at, 0x1f
0x80005cec:     or      $t0, $t0, $at
0x80005cf0:     xori    $t0, $t0, 0x1f
0x80005cf4:     mtc0    $t0, $t4, 0

'''

# MIPS

BLOCK_ADDR, INSN_START, INSN_END, \
ZERO, AT, V0, V1, A0, A1, A2, A3, \
T0, T1, T2, T3, T4, T5, T6, T7, \
S0, S1, S2, S3, S4, S5, S6, S7, \
T8, T9, K0, K1, GP, SP, S8, RA, \
SR, LO, HI, BAD, CAUSE, PC, FSR, FIR = list(range(0, 43))

def parse_one_unit_trace(block_idx, ctx, exec):
    ctx_off = 43 * 4 * block_idx
    ctx.seek(ctx_off)
    ctx_unit = struct.unpack('<' + 'I' * 43, ctx.read(43 * 4))
    #print(ctx_unit)

    exec_off = 1 * 4 * ctx_unit[INSN_START]
    exec.seek(exec_off)
    exec_units = exec.read(4 * (ctx_unit[INSN_END] - ctx_unit[INSN_START]))
    #print(exec_units)

    print("%8s %8s %8s %8s %8s %8s %8s %8s" % ("zero", "at", "v0", "v1", "a0", "a1", "a2", "a3"))
    print("%08x %08x %08x %08x %08x %08x %08x %08x" % (ctx_unit[ZERO], ctx_unit[AT], ctx_unit[V0], ctx_unit[V1], ctx_unit[A0], ctx_unit[A1], ctx_unit[A2], ctx_unit[A3]))
    print("%8s %8s %8s %8s %8s %8s %8s %8s" % ("t0", "t1", "t2", "t3", "t4", "t5", "t6", "t7"))
    print("%08x %08x %08x %08x %08x %08x %08x %08x" % (ctx_unit[T0], ctx_unit[T1], ctx_unit[T2], ctx_unit[T3], ctx_unit[T4], ctx_unit[T5], ctx_unit[T6], ctx_unit[T7]))
    print("%8s %8s %8s %8s %8s %8s %8s %8s" % ("s0", "s1", "s2", "s3", "s4", "s5", "s6", "s7"))
    print("%08x %08x %08x %08x %08x %08x %08x %08x" % (ctx_unit[S0], ctx_unit[S1], ctx_unit[S2], ctx_unit[S3], ctx_unit[S4], ctx_unit[S5], ctx_unit[S6], ctx_unit[S7]))
    print("%8s %8s %8s %8s %8s %8s %8s %8s" % ("t8", "t9", "k0", "k1", "gp", "sp", "s8", "ra"))
    print("%08x %08x %08x %08x %08x %08x %08x %08x" % (ctx_unit[T8], ctx_unit[T9], ctx_unit[K0], ctx_unit[K1], ctx_unit[GP], ctx_unit[SP], ctx_unit[S8], ctx_unit[RA]))
    print("%8s %8s %8s %8s %8s %8s %8s %8s" % ("sr", "lo", "hi", "bad", "cause", "pc", "fsr", "fir"))
    print("%08x %08x %08x %08x %08x %08x %08x %08x" % (ctx_unit[SR], ctx_unit[LO], ctx_unit[HI], ctx_unit[BAD], ctx_unit[CAUSE], ctx_unit[PC], ctx_unit[FSR], ctx_unit[FIR]))

    cs = Cs(CS_ARCH_MIPS, CS_MODE_MIPS32 | CS_MODE_LITTLE_ENDIAN)
    for insn in cs.disasm(exec_units, ctx_unit[BLOCK_ADDR]):
        print("0x%x:\t%s\t%s" % (insn.address, insn.mnemonic, insn.op_str))
    print("")

