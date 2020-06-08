# ktracer for QEMU

The ktracer is firstly a plugin for PANDA. However, PANDA is somehow too heavy
and not scalable to lots of cpu arches. We have already ported the ktracer to QEMU by 
simple instrumentation. Just enjoy it.

## milestones

- [X] redesign trace format supporting random bb access in ARM32
- [X] refactor the tracer code in qemu to get a better development flow
- [X] **1st version**, support ARM32, MIPS32, including the tracer, reader
- [ ] add header in trace format, thus more scalable on combination of endianness & arch
- [ ] add option for ktracer in QEMU, thus can be integrated in qemu by default
- [ ] **2nd version**, add more use, error handle and debug friendly stuff 
- [ ] figure out why some basic block will be record duplicately
- [ ] figure out flush before stop thing etc, i.e. the challenges for using in dynamic analysis
- [ ] **3rd version**, add more features supporting dynamic analysis

## patch
To use ktracer for QEMU, copy the files in `patches/` to `qemu-4.0.0/accel/tcg`, and 
a more convenient way is under construction...

```bash
cp patches/* path/to/qemu-4.0.0/accel/tcg
```

The `xxxadd_ktracer.patch` are files in patch format showing the modification to the
original files of qemu.


## usage
By default, you'll find `/tmp/context.trace` and `/tmp/execution.trace` which stores 
the execution records. Use `reader.py` to get readable content. 

Currently, we support ARM32 (w/o thumb) & MIPS32, both only limited to little endian.
And current trace supports random access of the executed block.
The `reader.py` shows random access of 1 basic block.

You'll see the records like below.

For ARM:

```text
r0=00000000  r1=00000000  r2=00000000  r3=00000000  r4=00000000  r5=00000000
r6=00000000  r7=00000000  r8=00000000  r9=00000000 r10=00000000 r11=00000000
ip=00000000  sp=00000000  cl=00000000  pc=00000000 cspr=400001d3 xspr=40000000
0x0 :mov		r0, #0
0x4 :ldr		r1, [pc, #4]
0x8 :ldr		r2, [pc, #4]
0xc :ldr		pc, [pc, #4]

```

For MIPS:

```text
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

```
