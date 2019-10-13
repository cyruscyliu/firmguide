# ktracer for QEMU

The ktracer is firstly a plugin for PANDA. However, PANDA is somehow too heavy
and not scalable to lots of cpu arches. We have already ported the ktracer to QEMU by 
simple instrumentation. Just enjoy it.

## patch
To use ktracer for QEMU, you need patch `qemu-4.0.0/accel/tcg/cpu-exec.c`. Only `QEMU-4.0.0`
is supported now, we don't test other QEMU release versions.

```bash
cd path/to/qemu-4.0.0
git am path/to/add_ktracer.patch
```

## usage
By default, you'll find `/tmp/log` which stores the execution records. Use 
`reader.py` to get readable content. You can also use `read.sh` directly.

You'll see the tons of records like below.

```text
r0=00000000  r1=00000000  r2=00000000  r3=00000000  r4=00000000  r5=00000000
r6=00000000  r7=00000000  r8=00000000  r9=00000000 r10=00000000 r11=00000000
ip=00000000  sp=00000000  cl=00000000  pc=00000000 cspr=400001d3 xspr=40000000
0x0 :mov		r0, #0
0x4 :ldr		r1, [pc, #4]
0x8 :ldr		r2, [pc, #4]
0xc :ldr		pc, [pc, #4]
```
