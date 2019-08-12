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

### launch directly

```text
liuqiang@liuqiang-VirtualBox:~/qemu-4.0.0$ ./arm-softmmu/qemu-system-arm -machine wrt350n_v2 -kernel  ~/esv/firmware-build/ws/backfire_10.03/bin/orion/openwrt-wrt350nv2-uImage --nographic
Uncompressing Linux... done, booting the kernel.
Linux version 2.6.32.10 (openwrt@65e79451f278) (gcc version 4.3.3 (GCC) ) #1 Wed Jul 31 02:29:48 UTC 2019
CPU: Feroceon [41069265] revision 5 (ARMv5TEJ), cr=00093177
CPU: VIVT data cache, VIVT instruction cache
Machine: Linksys WRT350N v2
Memory policy: ECC disabled, Data cache writeback
Built 1 zonelists in Zone order, mobility grouping on.  Total pages: 8128
Kernel command line: root=/dev/mtdblock1 rootfstype=squashfs,jffs2 noinitrd console=ttyS0,115200
PID hash table entries: 128 (order: -3, 512 bytes)
Dentry cache hash table entries: 4096 (order: 2, 16384 bytes)
Inode-cache hash table entries: 2048 (order: 1, 8192 bytes)
Memory: 32MB = 32MB total
Memory: 29576KB available (2564K code, 208K data, 96K init, 0K highmem)
Hierarchical RCU implementation.
NR_IRQS:64
Calibrating delay loop... 209.30 BogoMIPS (lpj=1046528)
Mount-cache hash table entries: 512
CPU: Testing write buffer coherency: ok
NET: Registered protocol family 16
Orion ID: Device-Unknown. TCLK=166666667.
PCI: bus0: Fast back to back transfers enabled
PCI: bus1: Fast back to back transfers disabled
bio: create slab <bio-0> at 0
Switching to clocksource orion_clocksource
NET: Registered protocol family 2
IP route cache hash table entries: 1024 (order: 0, 4096 bytes)
TCP established hash table entries: 1024 (order: 1, 8192 bytes)
TCP bind hash table entries: 1024 (order: 0, 4096 bytes)
TCP: Hash tables configured (established 1024 bind 1024)
TCP reno registered
NET: Registered protocol family 1
squashfs: version 4.0 (2009/01/31) Phillip Lougher
Registering mini_fo version $Id$
JFFS2 version 2.2. (NAND) (SUMMARY)  © 2001-2006 Red Hat, Inc.
msgmni has been set to 57
io scheduler noop registered
io scheduler deadline registered (default)
Serial: 8250/16550 driver, 2 ports, IRQ sharing disabled
serial8250.0: ttyS0 at MMIO 0xf1012000 (irq = 3) is a 16550A
console [ttyS0] enabled
physmap platform flash device: 00800000 at f4000000
physmap-flash.0: Found 1 x32 devices at 0x0 in 8-bit bank
 Intel/Sharp Extended Query Table at 0x0031
Using buffer write method
cmdlinepart partition parsing not available
RedBoot partition parsing not available
Using physmap partition information
Creating 7 MTD partitions on "physmap-flash.0":
0x000000000000-0x000000100000 : "kernel"
0x000000100000-0x000000750000 : "rootfs"
mtd: partition "rootfs" set to be root filesystem
split_squashfs: no squashfs found in "physmap-flash.0"
0x000000760000-0x0000007a0000 : "lang"
0x0000007a0000-0x0000007c0000 : "nvram"
0x0000007c0000-0x000000800000 : "u-boot"
0x000000750000-0x000000760000 : "eRcOmM_do_not_touch"
0x000000000000-0x000000750000 : "image"
MV-643xx 10/100/1000 ethernet driver version 1.4
mv643xx_eth smi: probed
net eth0: port 0 with MAC address 00:00:00:00:00:00
i2c /dev entries driver
Registered led device: wrt350nv2:green:power
Registered led device: wrt350nv2:green:security
Registered led device: wrt350nv2:orange:power
Registered led device: wrt350nv2:green:usb
Registered led device: wrt350nv2:green:wireless
TCP westwood registered
NET: Registered protocol family 17
Distributed Switch Architecture driver version 0.1
mv643xx_eth: SMI bus read not valid
eth0[0]: could not detect attached switch
eth0[0]: couldn't create dsa switch instance (error -22)
802.1Q VLAN Support v1.8 Ben Greear <greearb@candelatech.com>
All bugs added by David S. Miller <davem@redhat.com>
drivers/rtc/hctosys.c: unable to open rtc device (rtc0)
Cowardly refusing to erase blocks on filesystem with no valid JFFS2 nodes
empty_blocks 0, bad_blocks 0, c->nr_blocks 101
VFS: Cannot open root device "mtdblock1" or unknown-block(31,1)
Please append a correct "root=" boot option; here are the available partitions:
1f00            1024 mtdblock0 (driver?)
1f01            6464 mtdblock1 (driver?)
1f02             256 mtdblock2 (driver?)
1f03             128 mtdblock3 (driver?)
1f04             256 mtdblock4 (driver?)
1f05              64 mtdblock5 (driver?)
1f06            7488 mtdblock6 (driver?)
Kernel panic - not syncing: VFS: Unable to mount root fs on unknown-block(31,1)
```