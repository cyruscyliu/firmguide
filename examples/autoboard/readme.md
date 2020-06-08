# Autoboard qemu code sample

This directory contains the source code example for autoboard intc, timer, etc.


# For record

Use qemu 4.0.0 with salamader's patch.
The build command is:

```shell
./configure --enable-debug --extra-cflags="-g3" --extra-ldflags="-g3" --disable-strip --disable-pie --target-list=arm-softmmu,mips-softmmu,mipsel-softmmu
make -j30
```
