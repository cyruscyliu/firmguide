# ktracer for PANDA

This is a plugin for PANDA which can track the guest processor's execution flow.

Every execution record consists of the CPU registers and the code of the current basic block.

## port to QEMU-4.0.0

PANDA fails to support the latest QEMU-4.0.0, so I port the ktracer to QEMU-4.0.0 in order to
use the latest APIs and new devices like `pfalsh_cfi01`.

Replace `your/path/to/qemu-4.0.0/accel/tcg/cpu-exec.c` to 
this patched [cpu-exec.c](./qemu-4.0.0/accel/tcg/cpu-exec.c). 
Search `/* patch ` in it and you'll find what I've changed.

Use `your/path/to/qemu-4.0.0/arm-softmmu/qemu-system-arm` directly
and no need `-panda ktracer` parameter. The log is still in `/tmp/log`
and you can parse it with `ktrace_reader.py`.

BTW, the only update of the ktracer is that I enlarge the buffer size for more
instructions.

```c
uint8_t *mem = (uint8_t *) malloc(10240 * sizeof(uint8_t));
```

## prepare 

```bash
echo ktracer >> path_to_panda/panda/plugins/config.panda
mkdir path_to_panda/panda/plugins/ktracer
cp ktracer.cpp path_to_panda/panda/plugins/ktracer/
cp Makefile path_to_panda/panda/plugins/ktracer/
```

## compile

```bash
mkdir build-panda && cd build-panda
# for more debug information
../path_to_panda/configure \
    --enable-debug \
    --extra-cflags="-g3" --extra-ldflags="-g3" \
    --disable-strip \
    --disable-pie
../path_to_panda/build.sh --target-list=arm-softmmu
```

## usage

```bash
cd build-panda
./arm-softmmu/qemu-system-arm \ 
    -machine versatileab \
    -kernel path_to_vmlinux_or_uimage \
    --nographic \
    -panda ktracer
```

By default, you'll find `/tmp/log` which stores
the execution records. And it is of binary format.

Use `ktracer_reader.py` to get readable content.

```bash
# python3.x is required
python3.7 ktracer_reader.py /tmp/log
```

You'll see the tons of records like below.

```text
r0=00000000  r1=00000000  r2=00000000  r3=00000000  r4=00000000  r5=00000000
r6=00000000  r7=00000000  r8=00000000  r9=00000000 r10=00000000 r11=00000000
ip=00000000  sp=00000000  cl=00000000  pc=00000000 cspr=400001d3 xspr=40000000
0x0 :mov		r0, #0
0x4 :ldr		r1, [pc, #4]
0x8 :ldr		r2, [pc, #4]
0xc :ldr		pc, [pc, #4]
 -------------------------------
r0=00000000  r1=00000000  r2=00000000  r3=00000000  r4=00000000  r5=00000000
r6=00000000  r7=00000000  r8=00000000  r9=00000000 r10=00000000 r11=00000000
ip=00000000  sp=00000000  cl=00000000  pc=00000000 cspr=400001d3 xspr=40000000
0x0 :mov		r0, #0
0x4 :ldr		r1, [pc, #4]
0x8 :ldr		r2, [pc, #4]
0xc :ldr		pc, [pc, #4]
 -------------------------------
```