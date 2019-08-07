# Machine Model Generation

## Introduction

Just like the device tree, we draw machines with customized description files. 
See [wrt350n_v2.yaml](./machines/wrt350n_v2.yaml) as an example. 
You, of course, can add a new machine file like `wrt350n_v2` in `./machines`. 
Execute `main.py` and you will see the generated code for all the machine files in the directories
named after the machine names. Remember to tell your current operating system and root/path/to/qemu,
`main.py` will install these code after rendering.

```bash
liuqiang@liuqiang-VirtualBox:~/esv/generation$ python3.7 main.py -os linux
generating wrt350n_v2.c ...
generating mv88f5181L_ic.c ...
generating mv88f5181L.c ...
generating mv88f5181L_pcie.c ...
generating mv88f5181L_pcie.h ...
generating mv88f5181L_ic.h ...
generating mv88f5181L_peripherals.c ...
generating mv88f5181L_uart.h ...
generating mv88f5181L_gpio.h ...
generating mv88f5181L_timer.h ...
generating mv88f5181L_gpio.c ...
generating mv88f5181L_peripherals.h ...
generating mv88f5181L_timer.c ...
generating mv88f5181L.h ...
generating mv88f5181L_uart.c ...
generating wrt350n_v2.h ...

installing ..
wrt350n_v2/wrt350n_v2.h -> /home/liuqiang/qemu-4.0.0/include/hw/arm/wrt350n_v2.h
wrt350n_v2/mv88f5181L_ic.h -> /home/liuqiang/qemu-4.0.0/include/hw/intc/mv88f5181L_ic.h
wrt350n_v2/mv88f5181L_uart.h -> /home/liuqiang/qemu-4.0.0/include/hw/char/mv88f5181L_uart.h
wrt350n_v2/mv88f5181L_peripherals.h -> /home/liuqiang/qemu-4.0.0/include/hw/arm/mv88f5181L_peripherals.h
wrt350n_v2/mv88f5181L_uart.c -> /home/liuqiang/qemu-4.0.0/hw/char/mv88f5181L_uart.c
wrt350n_v2/mv88f5181L_pcie.h -> /home/liuqiang/qemu-4.0.0/include/hw/pci-host/mv88f5181L_pcie.h
wrt350n_v2/mv88f5181L_timer.h -> /home/liuqiang/qemu-4.0.0/include/hw/timer/mv88f5181L_timer.h
wrt350n_v2/mv88f5181L_gpio.c -> /home/liuqiang/qemu-4.0.0/hw/gpio/mv88f5181L_gpio.c
wrt350n_v2/mv88f5181L_timer.c -> /home/liuqiang/qemu-4.0.0/hw/timer/mv88f5181L_timer.c
wrt350n_v2/mv88f5181L_ic.c -> /home/liuqiang/qemu-4.0.0/hw/intc/mv88f5181L_ic.c
wrt350n_v2/mv88f5181L.c -> /home/liuqiang/qemu-4.0.0/hw/arm/mv88f5181L.c
wrt350n_v2/mv88f5181L_peripherals.c -> /home/liuqiang/qemu-4.0.0/hw/arm/mv88f5181L_peripherals.c
wrt350n_v2/mv88f5181L_pcie.c -> /home/liuqiang/qemu-4.0.0/hw/pci-host/mv88f5181L_pcie.c
wrt350n_v2/mv88f5181L.h -> /home/liuqiang/qemu-4.0.0/include/hw/arm/mv88f5181L.h
wrt350n_v2/mv88f5181L_gpio.h -> /home/liuqiang/qemu-4.0.0/include/hw/gpio/mv88f5181L_gpio.h
wrt350n_v2/wrt350n_v2.c -> /home/liuqiang/qemu-4.0.0/hw/arm/wrt350n_v2.c
makefiles/hw/char/Makefile.objs -> /home/liuqiang/qemu-4.0.0/hw/char/Makefile.objs
makefiles/hw/pci-host/Makefile.objs -> /home/liuqiang/qemu-4.0.0/hw/pci-host/Makefile.objs
makefiles/hw/timer/Makefile.objs -> /home/liuqiang/qemu-4.0.0/hw/timer/Makefile.objs
makefiles/hw/arm/Makefile.objs -> /home/liuqiang/qemu-4.0.0/hw/arm/Makefile.objs
makefiles/hw/arm/Kconfig -> /home/liuqiang/qemu-4.0.0/hw/arm/Kconfig
makefiles/hw/gpio/Makefile.objs -> /home/liuqiang/qemu-4.0.0/hw/gpio/Makefile.objs
makefiles/hw/intc/Makefile.objs -> /home/liuqiang/qemu-4.0.0/hw/intc/Makefile.objs
makefiles/default-configs/arm-softmmu.mak -> /home/liuqiang/qemu-4.0.0/default-configs/arm-softmmu.mak
done!
```

## debug

### debug with IDA

+ launch QEMU
```bash
./arm-softmmu/qemu-system-arm \
     -machine wrt350n_v2 \
     -kernel  ~/esv/firmware-build/ws/backfire_10.03/bin/orion/openwrt-wrt350nv2-uImage \
     --nographic -S -s
```

+ config the remote debugger

```text
application: path/to/vmlinux-debug-info.elf
input file: path/to/vmlinux-debug-info.elf
host name: ip/to/remote_debugger
port: 1234 (by default)
```
