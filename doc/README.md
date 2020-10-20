Table of Contents
=================

   * [Subcommand](#subcommand)
      * [./firmguide and its command-level arguments](#firmguide-and-its-command-level-arguments)
      * [CORE subcommands](#core-subcommands)
         * [synthesize](#synthesize)
         * [upload](#upload)
         * [diagnose](#diagnose)
         * [traversrc](#traversrc)
      * [PLUGIN subcommands](#plugin-subcommands)
         * [itopology](#itopology)
         * [dtcovereup](#dtcovereup)
         * [newhwdt](#newhwdt)
         * [unpack](#unpack)
         * [cmdcoverup](#cmdcoverup)
         * [loaddr](#loaddr)
         * [ofinitsrc](#ofinitsrc)
         * [ofinitcbs](#ofinitcbs)
         * [coverup](#coverup)
         * [debugsrc](#debugsrc)
         * [archive](#archive)
         * [usntest](#usntest)
         * [analysrc](#analysrc)
   * [Development](#development)
      * [Add analysis (group)](#add-analysis-group)
      * [APIs for analysis (group)](#apis-for-analysis-group)
         * [Analysis Manager](#analysis-manager)
         * [Frimware profile getter/setter](#frimware-profile-gettersetter)
         * [Components getter/setter](#components-gettersetter)
         * [Device tree parsers (dt_parsers)](#device-tree-parsers-dt_parsers)
         * [Database](#database)
         * [QEMU controller](#qemu-controller)
         * [Source controller](#source-controller)
      * [Add subcommand](#add-subcommand)

# Subcommand

FirmGuide is a command-oriented project just like `git`.
You can enter `./firmware -h` for more information.

It has many subcommands consisting of `CORE` subcommands
and `PLUGIN` subcommands, where the latter are very small and useful tools.
Each subcommand has its arguments and
you can enter `./firmguide subcommand -h` for more information.

## `./firmguide` and its command-level arguments

FirgGuide has several command-level arguments.
You can enter `./firmware -h` for more information.
Besides `-d`, `-p`, and `-lg` that are easy to understand and use,
we list how others (`-a`, `-e`, `-ld`) would be used by subcommands.
N means don't need this argument. P means sometimes need this argument.
Y means always need this argument.

|  Subcommand | synthesize | upload | diagnose | traversrc | itopology | dtcoverup | newhwdt | unpack | cmdcoverup | loaddr | ofinitcbs | coverup | debugsrc | usntest | analysrc |
|:-----------:|:----------:|:------:|:--------:|:---------:|:---------:|:---------:|:-------:|:------:|:----------:|:------:|:---------:|:-------:|:--------:|:-------:|:---------|
|  -a/--arch  |      N     |    N   |     N    |     N     |     N     |     N     |    N    |    N   |      N     |    N   |     N     |    Y    |     N    |    N    |     N    |
| -e/--endian |      P     |    P   |     P    |     N     |     N     |     N     |    N    |    N   |      P     |    N   |     N     |    Y    |     N    |    N    |     N    |
|  -ld/--load |      P     |    P   |     P    |     N     |     N     |     N     |    N    |    N   |      P     |    N   |     N     |    N    |     N    |    N    |     N    |

## `CORE` subcommands

### `synthesize`

This core subcommand converts a device tree to a QEMU virtual machine.

```txt
root@esv:~/firmguide# ./firmguide synthesize -dtb examples/plxtech_nas782x.dtb
2020-10-16 09:15:13,285 - INFO - AnalysesManager - chain - bfilter(invalid)->msearch(invalid)->unpack(invalid)->preprocdt->synthesisdt
2020-10-16 09:15:13,286 - INFO - AnalysesManager - chain cont'd - install
2020-10-16 09:15:13,294 - INFO - DTPreprocessing - preprocdt - dtb at examples/plxtech_nas782x.dtb
2020-10-16 09:15:13,294 - INFO - DTPreprocessing - preprocdt - dts at /root/esv-latest/plxtech_nas782x.dtb.dts
2020-10-16 09:15:13,294 - INFO - DTPreprocessing - preprocdt - board id 0xFFFFFFFF is chosen automatically
2020-10-16 09:15:13,331 - INFO - DTPreprocessing - preprocdt - arch arm is chosen automatically
2020-10-16 09:15:13,331 - INFO - DTPreprocessing - preprocdt - endian l is chosen automatically
2020-10-16 09:15:13,331 - INFO - DTPreprocessing - preprocdt - load address 0x00008000 is chosen automatically
2020-10-16 09:15:14,032 - WARNING - SynthesisDT - synthesisdt - cannot support intc ['plxtech,nas782x-gpio']
2020-10-16 09:15:14,103 - WARNING - SynthesisDT - synthesisdt - cannot support intc ['plxtech,nas782x-gpio']
2020-10-16 09:15:14,288 - WARNING - SynthesisDT - synthesisdt - cannot suport intc plxtech,nas782x-rps, intcp is missing
2020-10-16 09:15:18,394 - WARNING - SynthesisDT - synthesisdt - cannot support mmio ['plxtech,nas782x-rps']
2020-10-16 09:15:18,868 - INFO - SynthesisDT - synthesisdt - save at /root/esv-latest/plxtech_nas7820_plxtech_nas782x/hw/arm/plxtech_nas7820_plxtech_nas782x.c
2020-10-16 09:15:18,868 - INFO - SynthesisDT - synthesisdt - save at /root/esv-latest/plxtech_nas7820_plxtech_nas782x/hw/timer/plxtech_nas782x_rps_timer.c
2020-10-16 09:15:18,868 - INFO - SynthesisDT - synthesisdt - save at /root/esv-latest/plxtech_nas7820_plxtech_nas782x/include/hw/timer/plxtech_nas782x_rps_timer.h
2020-10-16 09:15:18,878 - INFO - Install - install - install /root/esv-latest/plxtech_nas7820_plxtech_nas782x
2020-10-16 09:15:21,519 - INFO - QEMUController - compile - CC      arm-softmmu/hw/timer/plxtech_nas782x_rps_timer.o
2020-10-16 09:15:21,522 - INFO - QEMUController - compile - CC      arm-softmmu/hw/arm/plxtech_nas7820_plxtech_nas782x.o
2020-10-16 09:15:21,650 - INFO - QEMUController - compile - LINK    mipsel-softmmu/qemu-system-mipsel
2020-10-16 09:15:21,651 - INFO - QEMUController - compile - LINK    mips-softmmu/qemu-system-mips
2020-10-16 09:15:22,076 - INFO - QEMUController - compile - LINK    arm-softmmu/qemu-system-arm
2020-10-16 09:15:32,792 - INFO - AnalysesManager - snapshot - profile at /root/esv-latest/.profile
```

### `upload`

This core subcommand first extracts a device tree in an uploaded firmware image,
then generate a a QEMU virtual machine, next test the image with the virtual machine
whether the image can be booted.
The test is quite simple. It enables QEMU trace,
checks user-mode and shell indicators,
and delete the QEMU trace finally.
If the test is failed, neither further analysis nor QEMU GDB interface is available.

```txt
root@esv:~/firmguide# ./firmguide upload -f examples/62771d14b82e554a95d048af99866c404acb196f.bin
2020-10-16 09:20:04,208 - INFO - AnalysesManager - chain cont'd - bfilter(invalid)->msearch(invalid)->unpack->preprocdt->synthesisdt
2020-10-16 09:20:04,209 - INFO - AnalysesManager - chain cont'd - install->loaddr(invalid)->preparation->tracing->loadtrace
2020-10-16 09:20:04,209 - INFO - AnalysesManager - chain cont'd - fastuserlevel->userlevel(invalid)->deltrace
2020-10-16 09:20:07,484 - INFO - Unpack - unpack - find /root/esv-latest/_62771d14b82e554a95d048af99866c404acb196f.bin.extracted/3DFB18.dtb
2020-10-16 09:20:07,492 - INFO - DTPreprocessing - preprocdt - dtb at /root/esv-latest/_62771d14b82e554a95d048af99866c404acb196f.bin.extracted/3DFB18.dtb
2020-10-16 09:20:07,492 - INFO - DTPreprocessing - preprocdt - dts at /root/esv-latest/3DFB18.dtb.dts
2020-10-16 09:20:07,492 - INFO - DTPreprocessing - preprocdt - board id 0xFFFFFFFF is chosen automatically
2020-10-16 09:20:07,531 - INFO - DTPreprocessing - preprocdt - arch arm is chosen automatically
2020-10-16 09:20:07,531 - INFO - DTPreprocessing - preprocdt - endian l is chosen automatically
2020-10-16 09:20:07,531 - INFO - DTPreprocessing - preprocdt - load address 0x00008000 is chosen automatically
2020-10-16 09:20:08,265 - WARNING - SynthesisDT - synthesisdt - cannot support intc ['plxtech,nas782x-gpio']
2020-10-16 09:20:08,338 - WARNING - SynthesisDT - synthesisdt - cannot support intc ['plxtech,nas782x-gpio']
2020-10-16 09:20:08,524 - WARNING - SynthesisDT - synthesisdt - cannot suport intc plxtech,nas782x-rps, intcp is missing
2020-10-16 09:20:12,714 - WARNING - SynthesisDT - synthesisdt - cannot support mmio ['plxtech,nas782x-rps']
2020-10-16 09:20:13,194 - INFO - SynthesisDT - synthesisdt - save at /root/esv-latest/plxtech_nas7820_plxtech_nas782x/hw/arm/plxtech_nas7820_plxtech_nas782x.c
2020-10-16 09:20:13,194 - INFO - SynthesisDT - synthesisdt - save at /root/esv-latest/plxtech_nas7820_plxtech_nas782x/hw/timer/plxtech_nas782x_rps_timer.c
2020-10-16 09:20:13,194 - INFO - SynthesisDT - synthesisdt - save at /root/esv-latest/plxtech_nas7820_plxtech_nas782x/include/hw/timer/plxtech_nas782x_rps_timer.h
2020-10-16 09:20:13,216 - INFO - Install - install - install /root/esv-latest/plxtech_nas7820_plxtech_nas782x
2020-10-16 09:20:15,849 - INFO - QEMUController - compile - CC      arm-softmmu/hw/timer/plxtech_nas782x_rps_timer.o
2020-10-16 09:20:15,852 - INFO - QEMUController - compile - CC      arm-softmmu/hw/arm/plxtech_nas7820_plxtech_nas782x.o
2020-10-16 09:20:15,966 - INFO - QEMUController - compile - LINK    mipsel-softmmu/qemu-system-mipsel
2020-10-16 09:20:15,975 - INFO - QEMUController - compile - LINK    mips-softmmu/qemu-system-mips
2020-10-16 09:20:16,396 - INFO - QEMUController - compile - LINK    arm-softmmu/qemu-system-arm
2020-10-16 09:20:30,667 - INFO - Preparation - preparation - repack kernel with arm/0x00008000/0x00008000
2020-10-16 09:20:30,667 - INFO - Preparation - preparation - get command: /tmp/qemu-4.0.0/arm-softmmu/qemu-system-arm -M plxtech_nas7820_plxtech_nas782x -kernel /root/esv-latest/_62771d14b82e554a95d048af99866c404acb196f.bin.extracted/_A0000.uimage.kernel.extracted/0.uimage -dtb /root/esv-latest/_62771d14b82e554a95d048af99866c404acb196f.bin.extracted/3DFB18.dtb -nographic -initrd /root/esv-latest/rootfs/armel.cpio.rootfs -append "console=ttyS0 nowatchdog nokaslr"
2020-10-16 09:20:30,667 - INFO - Tracing - tracing - tracing QEMU machine plxtech_nas7820_plxtech_nas782x
2020-10-16 09:20:35,980 - INFO - QEMUController - tracing - Uncompressing Linux... done, booting the kernel.
2020-10-16 09:20:45,446 - INFO - QEMUController - tracing - [    0.000000] Booting Linux on physical CPU 0x0
2020-10-16 09:20:45,508 - INFO - QEMUController - tracing - [    0.000000] Linux version 4.4.92 (buildbot@debian8) (gcc version 5.4.0 (LEDE GCC 5.4.0 r3560-79f57e422d) ) #0 SMP Tue Oct 17 17:46:20 2017
2020-10-16 09:20:45,508 - INFO - QEMUController - tracing - [    0.000000] CPU: ARMv6-compatible processor [410fb022] revision 2 (ARMv7), cr=00c0387d
2020-10-16 09:20:45,509 - INFO - QEMUController - tracing - [    0.000000] CPU: PIPT / VIPT nonaliasing data cache, VIPT aliasing instruction cache
2020-10-16 09:20:45,509 - INFO - QEMUController - tracing - [    0.000000] Machine model: Pogoplug V3
2020-10-16 09:20:45,509 - INFO - QEMUController - tracing - [    0.000000] Memory policy: Data cache writealloc
2020-10-16 09:20:45,510 - INFO - QEMUController - tracing - [    0.000000] DT missing boot CPU MPIDR[23:0], fall back to default cpu_logical_map
2020-10-16 09:20:45,511 - INFO - QEMUController - tracing - [    0.000000] PERCPU: Embedded 12 pages/cpu @cfde6000 s17696 r8192 d23264 u49152
2020-10-16 09:20:45,512 - INFO - QEMUController - tracing - [    0.000000] Built 1 zonelists in Zone order, mobility grouping on.  Total pages: 65024
2020-10-16 09:20:45,514 - INFO - QEMUController - tracing - [    0.000000] Kernel command line: console=ttyS0 nowatchdog nokaslr
2020-10-16 09:20:45,514 - INFO - QEMUController - tracing - [    0.000000] Bootloader command line not present
2020-10-16 09:20:45,515 - INFO - QEMUController - tracing - [    0.000000] PID hash table entries: 1024 (order: 0, 4096 bytes)
2020-10-16 09:20:45,515 - INFO - QEMUController - tracing - [    0.000000] Dentry cache hash table entries: 32768 (order: 5, 131072 bytes)
2020-10-16 09:20:45,516 - INFO - QEMUController - tracing - [    0.000000] Inode-cache hash table entries: 16384 (order: 4, 65536 bytes)
2020-10-16 09:20:45,517 - INFO - QEMUController - tracing - [    0.000000] Memory: 233976K/262144K available (3716K kernel code, 151K rwdata, 544K rodata, 6168K init, 226K bss, 28168K reserved, 0K cma-reserved)
2020-10-16 09:20:45,517 - INFO - QEMUController - tracing - [    0.000000] Virtual kernel memory layout:
2020-10-16 09:20:45,518 - INFO - QEMUController - tracing - [    0.000000]     vector  : 0xffff0000 - 0xffff1000   (   4 kB)
2020-10-16 09:20:45,518 - INFO - QEMUController - tracing - [    0.000000]     fixmap  : 0xffc00000 - 0xfff00000   (3072 kB)
2020-10-16 09:20:45,518 - INFO - QEMUController - tracing - [    0.000000]     vmalloc : 0xd0800000 - 0xff800000   ( 752 MB)
2020-10-16 09:20:45,519 - INFO - QEMUController - tracing - [    0.000000]     lowmem  : 0xc0000000 - 0xd0000000   ( 256 MB)
2020-10-16 09:20:45,519 - INFO - QEMUController - tracing - [    0.000000]     modules : 0xbf000000 - 0xc0000000   (  16 MB)
2020-10-16 09:20:45,519 - INFO - QEMUController - tracing - [    0.000000]       .text : 0xc0008000 - 0xc04314fc   (4262 kB)
2020-10-16 09:20:45,520 - INFO - QEMUController - tracing - [    0.000000]       .init : 0xc0432000 - 0xc0a38000   (6168 kB)
2020-10-16 09:20:45,520 - INFO - QEMUController - tracing - [    0.000000]       .data : 0xc0a38000 - 0xc0a5dd48   ( 152 kB)
2020-10-16 09:20:45,520 - INFO - QEMUController - tracing - [    0.000000]        .bss : 0xc0a5dd48 - 0xc0a96898   ( 227 kB)
2020-10-16 09:20:45,521 - INFO - QEMUController - tracing - [    0.000000] SLUB: HWalign=32, Order=0-3, MinObjects=0, CPUs=1, Nodes=1
2020-10-16 09:20:45,521 - INFO - QEMUController - tracing - [    0.000000] Hierarchical RCU implementation.
2020-10-16 09:20:45,522 - INFO - QEMUController - tracing - [    0.000000]      RCU restricting CPUs from NR_CPUS=2 to nr_cpu_ids=1.
2020-10-16 09:20:45,533 - INFO - QEMUController - tracing - [    0.000000] RCU: Adjusting geometry for rcu_fanout_leaf=16, nr_cpu_ids=1
2020-10-16 09:20:45,533 - INFO - QEMUController - tracing - [    0.000000] NR_IRQS:160
2020-10-16 09:20:45,534 - INFO - QEMUController - tracing - [    0.000000] clocksource: rps_clocksource_timer: mask: 0xffffff max_cycles: 0xffffff, max_idle_ns: 19112603332 ns
2020-10-16 09:20:45,535 - INFO - QEMUController - tracing - [    0.001548] sched_clock: 24 bits at 390kHz, resolution 2560ns, wraps every 21474835200ns
2020-10-16 09:20:45,535 - INFO - QEMUController - tracing - [    0.044052] Calibrating delay loop... 666.41 BogoMIPS (lpj=3332096)
2020-10-16 09:20:45,535 - INFO - QEMUController - tracing - [    0.152629] pid_max: default: 32768 minimum: 301
2020-10-16 09:20:45,536 - INFO - QEMUController - tracing - [    0.165585] Mount-cache hash table entries: 1024 (order: 0, 4096 bytes)
2020-10-16 09:20:45,536 - INFO - QEMUController - tracing - [    0.166028] Mountpoint-cache hash table entries: 1024 (order: 0, 4096 bytes)
2020-10-16 09:20:45,537 - INFO - QEMUController - tracing - [    0.261066] CPU: Testing write buffer coherency: ok
2020-10-16 09:20:45,537 - INFO - QEMUController - tracing - [    0.376266] Setting up static identity map for 0x8280 - 0x82b8
2020-10-16 09:20:45,538 - INFO - QEMUController - tracing - [    0.462999] Brought up 1 CPUs
2020-10-16 09:20:45,538 - INFO - QEMUController - tracing - [    0.464079] SMP: Total of 1 processors activated (666.41 BogoMIPS).
2020-10-16 09:20:45,539 - INFO - QEMUController - tracing - [    0.688593] clocksource: jiffies: mask: 0xffffffff max_cycles: 0xffffffff, max_idle_ns: 19112604462750000 ns
2020-10-16 09:20:45,539 - INFO - QEMUController - tracing - [    0.689597] futex hash table entries: 256 (order: 1, 8192 bytes)
2020-10-16 09:20:45,540 - INFO - QEMUController - tracing - [    0.705571] pinctrl core: initialized pinctrl subsystem
2020-10-16 09:20:45,540 - INFO - QEMUController - tracing - [    0.863050] NET: Registered protocol family 16
2020-10-16 09:20:45,541 - INFO - QEMUController - tracing - [    0.881592] DMA: preallocated 256 KiB pool for atomic coherent allocations
2020-10-16 09:20:45,541 - INFO - QEMUController - tracing - [    0.913031] cpuidle: using governor ladder
2020-10-16 09:20:45,541 - INFO - QEMUController - tracing - [    0.914647] cpuidle: using governor menu
2020-10-16 09:20:45,557 - INFO - QEMUController - tracing - [    1.120501] gpio-oxnas 44000000.gpio: at address d0848000
2020-10-16 09:20:45,557 - INFO - QEMUController - tracing - [    1.132093] gpio-oxnas 44100000.gpio: at address d084a000
2020-10-16 09:20:45,558 - INFO - QEMUController - tracing - [    1.161093] pinctrl-oxnas pinctrl: initialized OX820 pinctrl driver
2020-10-16 09:20:45,558 - INFO - QEMUController - tracing - [    1.796044] SCSI subsystem initialized
2020-10-16 09:20:45,558 - INFO - QEMUController - tracing - [    1.810357] usbcore: registered new interface driver usbfs
2020-10-16 09:20:45,559 - INFO - QEMUController - tracing - [    1.814763] usbcore: registered new interface driver hub
2020-10-16 09:20:45,559 - INFO - QEMUController - tracing - [    1.817684] usbcore: registered new device driver usb
2020-10-16 09:20:45,560 - INFO - QEMUController - tracing - [    1.822771] pps_core: LinuxPPS API ver. 1 registered
2020-10-16 09:20:45,560 - INFO - QEMUController - tracing - [    1.823063] pps_core: Software ver. 5.3.6 - Copyright 2005-2007 Rodolfo Giometti <giometti@linux.it>
2020-10-16 09:20:45,561 - INFO - QEMUController - tracing - [    1.824335] PTP clock support registered
2020-10-16 09:20:45,561 - INFO - QEMUController - tracing - [    1.998407] clocksource: Switched to clocksource rps_clocksource_timer
2020-10-16 09:20:45,562 - INFO - QEMUController - tracing - [    2.049643] NET: Registered protocol family 2
2020-10-16 09:20:45,563 - INFO - QEMUController - tracing - [    2.096614] TCP established hash table entries: 2048 (order: 1, 8192 bytes)
2020-10-16 09:20:45,564 - INFO - QEMUController - tracing - [    2.098201] TCP bind hash table entries: 2048 (order: 2, 16384 bytes)
2020-10-16 09:20:45,564 - INFO - QEMUController - tracing - [    2.099440] TCP: Hash tables configured (established 2048 bind 2048)
2020-10-16 09:20:45,565 - INFO - QEMUController - tracing - [    2.109585] UDP hash table entries: 256 (order: 1, 8192 bytes)
2020-10-16 09:20:45,565 - INFO - QEMUController - tracing - [    2.111388] UDP-Lite hash table entries: 256 (order: 1, 8192 bytes)
2020-10-16 09:20:45,566 - INFO - QEMUController - tracing - [    2.122995] NET: Registered protocol family 1
2020-10-16 09:20:45,566 - INFO - QEMUController - tracing - [    4.443822] Unpacking initramfs...
2020-10-16 09:20:45,566 - INFO - QEMUController - tracing - [    8.184596] Freeing initrd memory: 14948K
2020-10-16 09:20:45,567 - INFO - QEMUController - tracing - [    8.221004] Crashlog allocated RAM at address 0x3f00000
2020-10-16 09:20:45,567 - INFO - QEMUController - tracing - [    8.683855] squashfs: version 4.0 (2009/01/31) Phillip Lougher
2020-10-16 09:20:45,567 - INFO - QEMUController - tracing - [    8.749647] io scheduler noop registered
2020-10-16 09:20:45,568 - INFO - QEMUController - tracing - [    8.750259] io scheduler deadline registered (default)
2020-10-16 09:20:45,568 - INFO - QEMUController - tracing - [    8.773880] Serial: 8250/16550 driver, 16 ports, IRQ sharing enabled
2020-10-16 09:20:45,569 - INFO - QEMUController - tracing - [    8.931645] console [ttyS0] disabled
2020-10-16 09:20:45,569 - INFO - QEMUController - tracing - [    8.939911] 44200000.uart: ttyS0 at MMIO 0x44200000 (irq = 6, base_baud = 390625) is a 16550A
2020-10-16 09:20:45,570 - INFO - QEMUController - tracing - [    9.078830] console [ttyS0] enabled
2020-10-16 09:20:45,626 - INFO - QEMUController - tracing - [    9.134627] nand: No NAND device found
2020-10-16 09:20:45,669 - INFO - QEMUController - tracing - [    9.177646] oxnas-gmac 40400000.ethernet: no reset control found
2020-10-16 09:20:45,671 - INFO - QEMUController - tracing - [    9.179545]  Ring mode enabled
2020-10-16 09:20:45,673 - INFO - QEMUController - tracing - [    9.181271]  No HW DMA feature register supported
2020-10-16 09:20:45,674 - INFO - QEMUController - tracing - [    9.182062]  Normal descriptors
2020-10-16 09:20:45,674 - INFO - QEMUController - tracing - [    9.183124]  Wake-Up On Lan supported
2020-10-16 09:20:48,685 - INFO - QEMUController - tracing - [   12.193653] stmmac: Cannot register as MDIO bus
2020-10-16 09:20:48,692 - INFO - QEMUController - tracing - [   12.200258] oxnas-gmac: probe of 40400000.ethernet failed with error -5
2020-10-16 09:20:48,700 - INFO - QEMUController - tracing - [   12.209021] stmmaceth 40400000.ethernet: no reset control found
2020-10-16 09:20:48,701 - INFO - QEMUController - tracing - [   12.209625]  Ring mode enabled
2020-10-16 09:20:48,702 - INFO - QEMUController - tracing - [   12.210065]  No HW DMA feature register supported
2020-10-16 09:20:48,702 - INFO - QEMUController - tracing - [   12.211018]  Normal descriptors
2020-10-16 09:20:48,703 - INFO - QEMUController - tracing - [   12.211543]  Wake-Up On Lan supported
2020-10-16 09:20:51,704 - INFO - QEMUController - tracing - [   15.212206] stmmac: Cannot register as MDIO bus
2020-10-16 09:20:51,705 - INFO - QEMUController - tracing - [   15.213975] stmmaceth: probe of 40400000.ethernet failed with error -5
2020-10-16 09:20:51,746 - INFO - QEMUController - tracing - [   15.254766] NET: Registered protocol family 10
2020-10-16 09:20:51,897 - INFO - QEMUController - tracing - [   15.406069] NET: Registered protocol family 17
2020-10-16 09:20:51,904 - INFO - QEMUController - tracing - [   15.412538] bridge: automatic filtering via arp/ip/ip6tables has been deprecated. Update your scripts to load br_netfilter if you need this.
2020-10-16 09:20:51,905 - INFO - QEMUController - tracing - [   15.413721] 8021q: 802.1Q VLAN Support v1.8
2020-10-16 09:20:52,006 - INFO - QEMUController - tracing - [   15.514191] hctosys: unable to open rtc device (rtc0)
2020-10-16 09:20:52,233 - INFO - QEMUController - tracing - [   15.741875] Freeing unused kernel memory: 6168K
2020-10-16 09:20:53,956 - INFO - QEMUController - tracing - [   17.464675] devpts: called with bogus options
2020-10-16 09:20:56,408 - INFO - QEMUController - tracing - Starting syslogd: OK
2020-10-16 09:20:57,045 - INFO - QEMUController - tracing - Starting klogd: OK
2020-10-16 09:21:00,469 - INFO - QEMUController - tracing - Running sysctl: OK
2020-10-16 09:21:01,540 - INFO - QEMUController - tracing - Saving random seed: [   25.048655] random: dd: uninitialized urandom read (512 bytes read, 0 bits of entropy available)
2020-10-16 09:21:01,609 - INFO - QEMUController - tracing - OK
2020-10-16 09:21:03,814 - INFO - QEMUController - tracing - Starting network: OK
2020-10-16 09:21:04,124 - INFO - QEMUController - tracing -
2020-10-16 09:21:04,124 - INFO - QEMUController - tracing -
2020-10-16 09:21:04,140 - INFO - QEMUController - tracing - Welcome to Buildroot
2020-10-16 09:21:04,154 - INFO - QEMUController - tracing -
2020-10-16 09:21:17,421 - INFO - QEMUController - tracing - buildroot login:
2020-10-16 09:21:17,421 - INFO - QEMUController - tracing -
2020-10-16 09:21:17,426 - INFO - QEMUController - tracing - Welcome to Buildroot
2020-10-16 09:21:17,428 - INFO - QEMUController - tracing -
2020-10-16 09:21:18,121 - INFO - QEMUController - tracing - buildroot login:
2020-10-16 09:21:18,121 - INFO - QEMUController - tracing -
2020-10-16 09:21:18,123 - INFO - QEMUController - tracing - Welcome to Buildroot
2020-10-16 09:21:18,126 - INFO - QEMUController - tracing -
2020-10-16 09:21:30,681 - INFO - QEMUController - tracing - buildroot login:
2020-10-16 09:21:30,682 - INFO - LoadTrace - loadtrace - loading firmguide.trace ...
2020-10-16 09:21:37,012 - INFO - LoadTrace - loadtrace - load 103580 basic blocks
2020-10-16 09:21:37,013 - INFO - CheckUserLevelF - fastuserlevel - scan user level indicators in firmguide.trace
2020-10-16 09:21:37,729 - INFO - CheckUserLevelF - fastuserlevel - have entered the user level
2020-10-16 09:21:37,729 - INFO - DeleteTrace - deltrace - remove firmguide.trace
2020-10-16 09:21:37,764 - INFO - AnalysesManager - snapshot - profile at /root/esv-latest/.profile
```

### `diagnose`

This core subcommand does most of the same things as `upload`.
However, the test in `diagnose` is not simple.
If the test is failed, it will analyze the root cause
and exposes GDB interfaces finally.

### `traversrc`

This core subcommand walks through the startup process of Linux kernel
and shows interesting functions for manual analysis. Assign `-dtb` to
solve part of indirect call problems. This core subcommand is not complete
because of poor implementation that should be improved in the future.
Note that `<noindent>` is the indirect call that `sparse` cannot handle.

```txt
root@openwrt-builder:~/firmguide# ./firmguide traversrc -s linux-3.18.20 -cc /mnt/iscsi/openwrt-build-docker/share/15.05-bfae3162fb949c343763ad9ea7ab3fe0/./chaos_calmer-15.05/build_dir/target-arm_mpcore_uClibc-0.9.33.2_eabi/OpenWrt-SDK-15.05-oxnas_gcc-4.8-linaro_uClibc-0.9.33.2_eabi.Linux-x86_64/staging_dir/toolchain-arm_mpcore_gcc-4.8-linaro_uClibc-0.9.33.2_eabi/bin/arm-openwrt-linux- -dtb examples/plxtech_nas782x.dtb
2020-10-20 02:35:03,266 - INFO - AnalysesManager - chain cont'd - bfilter->ktraversal
2020-10-20 02:35:03,280 - INFO - CheckBoard - bfilter - arch/arm/mach-oxnas is under our consideration
2020-10-20 02:35:03,280 - INFO - TraverseKernel - ktraversal - -d mach-oxnas automatically by bfilter
2020-10-20 02:35:05,877 - INFO - TraverseKernel - ktraversal - [done] init/main.c
2020-10-20 02:35:06,428 - INFO - TraverseKernel - ktraversal - [done] arch/arm/kernel/irq.c
2020-10-20 02:35:08,190 - INFO - TraverseKernel - ktraversal - [done] arch/arm/kernel/setup.c
2020-10-20 02:35:08,541 - INFO - TraverseKernel - ktraversal - [done] arch/arm/kernel/time.c
2020-10-20 02:35:09,294 - INFO - TraverseKernel - ktraversal - [done] arch/arm/mach-oxnas/mach-ox820.c
2020-10-20 02:35:10,042 - INFO - TraverseKernel - ktraversal - [done] arch/arm/mach-oxnas/platsmp.c
2020-10-20 02:35:10,207 - INFO - TraverseKernel - ktraversal - [done] arch/arm/mach-oxnas/hotplug.c
2020-10-20 02:35:11,082 - INFO - TraverseKernel - ktraversal - [done] drivers/clk/clk-fixed-rate.c
2020-10-20 02:35:11,484 - INFO - TraverseKernel - ktraversal - [done] drivers/clk/clk-fixed-factor.c
2020-10-20 02:35:11,788 - INFO - TraverseKernel - ktraversal - [done] drivers/clocksource/clksrc-of.c
2020-10-20 02:35:12,100 - INFO - TraverseKernel - ktraversal - [done] drivers/irqchip/irqchip.c
2020-10-20 02:35:13,239 - INFO - TraverseKernel - ktraversal - [done] drivers/of/irq.c
2020-10-20 02:35:13,628 - INFO - TraverseKernel - ktraversal - |-start_kernel->setup_arch[intermediate]
2020-10-20 02:35:13,771 - INFO - TraverseKernel - ktraversal -   |-setup_arch-><noident>[unknown]
2020-10-20 02:35:13,982 - INFO - TraverseKernel - ktraversal -   |-setup_arch-><noident>[unknown]
2020-10-20 02:35:14,296 - INFO - TraverseKernel - ktraversal - |-start_kernel->init_IRQ[intermediate]
2020-10-20 02:35:14,396 - INFO - TraverseKernel - ktraversal -   |-init_IRQ-><noident>[unknown]
2020-10-20 02:35:14,607 - INFO - TraverseKernel - ktraversal -   |-init_IRQ->irqchip_init[intermediate]
[-] cannot recognize "arm,gic-400",IRQCHIP_DECLARE(cortex_a15_gic, "arm,cortex-a15-gic" in linux-3.18.20/patches/platform/320-oxnas-irqchip.patch
2020-10-20 02:36:33,302 - INFO - TraverseKernel - ktraversal -     |-irqchip_init->of_irq_init[handled]
2020-10-20 02:36:33,302 - INFO - TraverseKernel - ktraversal -       |-of_irq_init->gic_of_init[indirected]
2020-10-20 02:36:33,508 - INFO - TraverseKernel - ktraversal -       |-of_irq_init->rps_of_init[indirected]
2020-10-20 02:36:33,889 - INFO - TraverseKernel - ktraversal - |-start_kernel->time_init[intermediate]
2020-10-20 02:36:34,003 - INFO - TraverseKernel - ktraversal -   |-time_init-><noident>[unknown]
2020-10-20 02:36:48,849 - INFO - TraverseKernel - ktraversal -   |-time_init->of_clk_init[handled]
2020-10-20 02:36:48,850 - INFO - TraverseKernel - ktraversal -     |-of_clk_init->of_fixed_clk_setup[indirected]
2020-10-20 02:36:49,096 - INFO - TraverseKernel - ktraversal -       |-of_fixed_clk_setup->clk_register_fixed_rate_with_accuracy[unknown]
2020-10-20 02:36:49,364 - INFO - TraverseKernel - ktraversal -         |-clk_register_fixed_rate_with_accuracy->clk_register[handled]
2020-10-20 02:36:49,429 - INFO - TraverseKernel - ktraversal -     |-of_clk_init->of_fixed_factor_clk_setup[indirected]
2020-10-20 02:36:49,733 - INFO - TraverseKernel - ktraversal -       |-of_fixed_factor_clk_setup->clk_register_fixed_factor[unknown]
2020-10-20 02:36:49,983 - INFO - TraverseKernel - ktraversal -         |-clk_register_fixed_factor->clk_register[handled]
2020-10-20 02:36:50,019 - INFO - TraverseKernel - ktraversal -     |-of_clk_init->oxnas_init_stdclk[indirected]
2020-10-20 02:36:50,314 - INFO - TraverseKernel - ktraversal -     |-of_clk_init->oxnas_init_pllb[indirected]
2020-10-20 02:36:50,590 - INFO - TraverseKernel - ktraversal -     |-of_clk_init->oxnas_init_plla[indirected]
2020-10-20 02:36:55,360 - INFO - TraverseKernel - ktraversal -   |-time_init->clocksource_of_init[handled]
2020-10-20 02:36:55,360 - INFO - TraverseKernel - ktraversal -     |-clocksource_of_init->rps_timer_init[indirected]
2020-10-20 02:36:55,599 - INFO - TraverseKernel - ktraversal -     |-clocksource_of_init->twd_local_timer_of_register[indirected]
2020-10-20 02:36:55,927 - INFO - TraverseKernel - ktraversal - |-start_kernel-><noident>[unknown]
2020-10-20 02:36:56,196 - INFO - TraverseKernel - ktraversal - |-start_kernel->rest_init[ignored]
2020-10-20 02:36:56,330 - INFO - TraverseKernel - ktraversal - You may add the unknown functions below to the skip list
2020-10-20 02:36:56,330 - INFO - TraverseKernel - ktraversal - ['of_fixed_clk_setup', '<noident>', 'oxnas_init_plla', 'gic_of_init', 'oxnas_init_stdclk', 'of_fixed_factor_clk_setup', 'rps_of_init', 'oxnas_init_pllb', 'twd_local_timer_of_register', 'rps_timer_init', 'clk_register_fixed_factor', 'clk_register_fixed_rate_with_accuracy']
2020-10-20 02:36:56,425 - INFO - TraverseKernel - ktraversal - slicing info saved as /root/firmguide/.slicing
2020-10-20 02:36:56,426 - INFO - AnalysesManager - snapshot - profile at /root/firmguide/.profile
```

## `PLUGIN` subcommands

### `itopology`

This plugin reads a a device tree blob, parses its interrupt topology
(how peripherals are connected to interrupt controllers and
how the interrupt controllers are connected to processors), and prints the topology in dot.
You can plot the dot file in `https://edotor.net`.

```txt
root@esv:~/firmguide# ./firmguide itopology -dtb examples/plxtech_nas782x.dtb
2020-10-13 08:48:13,154 - INFO - AnalysesManager - chain cont'd - tolologydt
digraph {
        graph [rankdir=LR]
        "arm,arm11mp-gic" -> cpu
        "plxtech,nas782x-ehci" -> "arm,arm11mp-gic" [label=7]
        "snps,dwmac" -> "arm,arm11mp-gic" [label=8]
        "snps,dwmac" -> "arm,arm11mp-gic" [label=772]
        "plxtech,nas782x-sata" -> "arm,arm11mp-gic" [label=18]
        ns16550a -> "arm,arm11mp-gic" [label=23]
        mpcore_wdt -> "arm,arm11mp-gic" [label=14]
        "arm,arm11mp-twd-timer" -> "arm,arm11mp-gic" [label=13]
        "plxtech,nas782x-gpio" -> "arm,arm11mp-gic" [label=22]
        "plxtech,nas782x-gpio" -> "arm,arm11mp-gic" [label=21]
}
2020-10-13 08:48:13,189 - INFO - TopologyDT - tolologydt - ONLINE GRAPHIVZ VIEWER: https://edotor.net
2020-10-13 08:48:13,190 - INFO - AnalysesManager - snapshot - profile at /root/firmguide/.profile
```

### `dtcovereup`

This plugin lists each hardware in the given a device tree blob.

```txt
root@esv:~/firmguide# ./firmguide dtcoverup -dtb examples/plxtech_nas782x.dtb
2020-10-13 08:53:03,185 - INFO - AnalysesManager - chain cont'd - disclosedt
2020-10-13 08:53:03,193 - INFO - DiscloseDT - disclosedt - [CPU] of /cpus/cpu@0/['arm,arm11mpcore']
2020-10-13 08:53:03,197 - INFO - DiscloseDT - disclosedt - [MEM] base 0x00000000 size 0x10000000 of /memory/['ram,generic']
2020-10-13 08:53:03,208 - INFO - DiscloseDT - disclosedt - [TIMER] base 0x44400200 size 0x00000040 of /timer@44400200/['plxtech,nas782x-rps-timer']
2020-10-13 08:53:03,208 - INFO - DiscloseDT - disclosedt - [TIMER] base 0x47000600 size 0x00000020 of /local-timer@47000600/['arm,arm11mp-twd-timer']
2020-10-13 08:53:03,213 - INFO - DiscloseDT - disclosedt - [SERIAL] base 0x44200000 size 0x00000100 of /uart@44200000/['ns16550a']
2020-10-13 08:53:03,218 - INFO - DiscloseDT - disclosedt - [MMIO] base 0x40200100 size 0x00000f00 of /ehci@40200100/['plxtech,nas782x-ehci'] overlap:None
2020-10-13 08:53:03,218 - INFO - DiscloseDT - disclosedt - [MMIO] base 0x40400000 size 0x00002000 of /ethernet@40400000/['plxtech,nas782x-gmac', 'snps,dwmac'] overlap:None
2020-10-13 08:53:03,218 - INFO - DiscloseDT - disclosedt - [MMIO] base 0x41000000 size 0x00100000 of /nand@41000000/['plxtech,nand-nas782x', 'gen_nand'] overlap:None
2020-10-13 08:53:03,218 - INFO - DiscloseDT - disclosedt - [MMIO] base 0x41c00000 size 0x00000020 of /nand@41000000/['plxtech,nand-nas782x', 'gen_nand'] overlap:None
2020-10-13 08:53:03,218 - INFO - DiscloseDT - disclosedt - [MMIO] base 0x44000000 size 0x00000100 of /pinctrl/gpio@44000000/['plxtech,nas782x-gpio'] overlap:None
2020-10-13 08:53:03,218 - INFO - DiscloseDT - disclosedt - [MMIO] base 0x44e00000 size 0x00000200 of /pinctrl/gpio@44000000/['plxtech,nas782x-gpio'] overlap:['plxtech,nas782x-plla']
2020-10-13 08:53:03,218 - INFO - DiscloseDT - disclosedt - [MMIO] base 0x44100000 size 0x00000100 of /pinctrl/gpio@44100000/['plxtech,nas782x-gpio'] overlap:None
2020-10-13 08:53:03,218 - INFO - DiscloseDT - disclosedt - [MMIO] base 0x44f00000 size 0x00000200 of /pinctrl/gpio@44100000/['plxtech,nas782x-gpio'] overlap:['plxtech,nas782x-pllb']
2020-10-13 08:53:03,218 - INFO - DiscloseDT - disclosedt - [MMIO] base 0x44200000 size 0x00000100 of /uart@44200000/['ns16550a'] overlap:None
2020-10-13 08:53:03,218 - INFO - DiscloseDT - disclosedt - [MMIO] base 0x44400000 size 0x00000014 of /rps@44400000/['plxtech,nas782x-rps'] overlap:None
2020-10-13 08:53:03,218 - INFO - DiscloseDT - disclosedt - [MMIO] base 0x44400200 size 0x00000040 of /timer@44400200/['plxtech,nas782x-rps-timer'] overlap:None
2020-10-13 08:53:03,219 - INFO - DiscloseDT - disclosedt - [MMIO] base 0x44e00034 size 0x00000008 of /reset-controller@44E00034/['plxtech,nas782x-reset'] overlap:['plxtech,nas782x-gpio']
2020-10-13 08:53:03,219 - INFO - DiscloseDT - disclosedt - [MMIO] base 0x44e001f0 size 0x00000010 of /plla@44e001f0/['plxtech,nas782x-plla'] overlap:['plxtech,nas782x-gpio']
2020-10-13 08:53:03,219 - INFO - DiscloseDT - disclosedt - [MMIO] base 0x44f001f0 size 0x00000010 of /pllb@44f001f0/['plxtech,nas782x-pllb'] overlap:['plxtech,nas782x-gpio']
2020-10-13 08:53:03,219 - INFO - DiscloseDT - disclosedt - [MMIO] base 0x45900000 size 0x00020000 of /sata@45900000/['plxtech,nas782x-sata'] overlap:None
2020-10-13 08:53:03,219 - INFO - DiscloseDT - disclosedt - [MMIO] base 0x459a0000 size 0x00000040 of /sata@45900000/['plxtech,nas782x-sata'] overlap:None
2020-10-13 08:53:03,219 - INFO - DiscloseDT - disclosedt - [MMIO] base 0x459b0000 size 0x00000020 of /sata@45900000/['plxtech,nas782x-sata'] overlap:None
2020-10-13 08:53:03,219 - INFO - DiscloseDT - disclosedt - [MMIO] base 0x459e0000 size 0x00002000 of /sata@45900000/['plxtech,nas782x-sata'] overlap:None
2020-10-13 08:53:03,219 - INFO - DiscloseDT - disclosedt - [MMIO] base 0x44900000 size 0x0000000c of /sata@45900000/['plxtech,nas782x-sata'] overlap:None
2020-10-13 08:53:03,219 - INFO - DiscloseDT - disclosedt - [MMIO] base 0x50000000 size 0x00001000 of /sata@45900000/['plxtech,nas782x-sata'] overlap:None
2020-10-13 08:53:03,219 - INFO - DiscloseDT - disclosedt - [MMIO] base 0x47000600 size 0x00000020 of /local-timer@47000600/['arm,arm11mp-twd-timer'] overlap:None
2020-10-13 08:53:03,219 - INFO - DiscloseDT - disclosedt - [MMIO] base 0x47000620 size 0x00000020 of /watchdog@47000620/['mpcore_wdt'] overlap:None
2020-10-13 08:53:03,219 - INFO - DiscloseDT - disclosedt - [MMIO] base 0x47001000 size 0x00001000 of /gic@47001000/['arm,arm11mp-gic'] overlap:None
2020-10-13 08:53:03,219 - INFO - DiscloseDT - disclosedt - [MMIO] base 0x47000100 size 0x00000100 of /gic@47001000/['arm,arm11mp-gic'] overlap:None
2020-10-13 08:53:03,220 - INFO - DiscloseDT - disclosedt - [MMIO] base 0x47c00000 size 0x00001000 of /pcie-controller@47C00000/['plxtech,nas782x-pcie'] overlap:None
2020-10-13 08:53:03,220 - INFO - DiscloseDT - disclosedt - [MMIO] base 0x47d00000 size 0x00000100 of /pcie-controller@47C00000/['plxtech,nas782x-pcie'] overlap:None
2020-10-13 08:53:03,220 - INFO - DiscloseDT - disclosedt - [MMIO] base 0x44a00000 size 0x00000010 of /pcie-controller@47C00000/['plxtech,nas782x-pcie'] overlap:None
2020-10-13 08:53:03,220 - INFO - DiscloseDT - disclosedt - [MMIO] base 0x47e00000 size 0x00001000 of /pcie-controller@47E00000/['plxtech,nas782x-pcie'] overlap:None
2020-10-13 08:53:03,220 - INFO - DiscloseDT - disclosedt - [MMIO] base 0x47f00000 size 0x00000100 of /pcie-controller@47E00000/['plxtech,nas782x-pcie'] overlap:None
2020-10-13 08:53:03,220 - INFO - DiscloseDT - disclosedt - [MMIO] base 0x44a00000 size 0x00000010 of /pcie-controller@47E00000/['plxtech,nas782x-pcie'] overlap:None
2020-10-13 08:53:03,225 - INFO - DiscloseDT - disclosedt - [FLASH] base 0x41000000 size 0x00100000 of /nand@41000000/['plxtech,nand-nas782x', 'gen_nand']
2020-10-13 08:53:03,225 - INFO - DiscloseDT - disclosedt - [FLASH] base 0x41c00000 size 0x00000020 of /nand@41000000/['plxtech,nand-nas782x', 'gen_nand']
2020-10-13 08:53:03,225 - INFO - DiscloseDT - disclosedt - save dts at examples/plxtech_nas782x.dtb.dts
2020-10-13 08:53:03,226 - INFO - AnalysesManager - snapshot - profile at /root/firmguide/.profile
```

### `newhwdt`

This plugin adds hardware listed in the given a device tree blob
to our hardware database. This plugin is used at the very beginning
and will be rarely used in the future.

```txt
root@esv:~/firmguide# ./firmguide -d newhwdt -dtb examples/plxtech_nas782x.dtb
2020-10-13 09:05:58,797 - INFO - AnalysesManager - chain cont'd - scanhwdt
2020-10-13 09:05:58,840 - DEBUG - UpdateHardwareDT - scanhwdt - skip supported ['arm,arm11mpcore']
2020-10-13 09:05:58,858 - DEBUG - UpdateHardwareDT - scanhwdt - skip supported ['ram,generic']
2020-10-13 09:05:58,948 - DEBUG - UpdateHardwareDT - scanhwdt - skip supported ['arm,arm11mp-gic']
2020-10-13 09:05:59,236 - DEBUG - UpdateHardwareDT - scanhwdt - skip supported ['plxtech,nas782x-rps']
2020-10-13 09:05:59,263 - DEBUG - UpdateHardwareDT - scanhwdt - skip supported ['ns16550a']
2020-10-13 09:05:59,376 - DEBUG - UpdateHardwareDT - scanhwdt - skip supported ['plxtech,nas782x-rps-timer']
2020-10-13 09:05:59,376 - DEBUG - UpdateHardwareDT - scanhwdt - skip improper or duplicated ['arm,arm11mp-twd-timer']
2020-10-13 09:05:59,528 - DEBUG - UpdateHardwareDT - scanhwdt - skip supported ['plxtech,nand-nas782x', 'gen_nand']
2020-10-13 09:05:59,961 - DEBUG - UpdateHardwareDT - scanhwdt - skip supported ['plxtech,nas782x-ehci']
2020-10-13 09:06:00,617 - DEBUG - UpdateHardwareDT - scanhwdt - skip supported ['plxtech,nas782x-gmac', 'snps,dwmac']
2020-10-13 09:06:00,617 - DEBUG - UpdateHardwareDT - scanhwdt - skip improper or duplicated ['plxtech,nand-nas782x', 'gen_nand']
2020-10-13 09:06:01,038 - DEBUG - UpdateHardwareDT - scanhwdt - skip supported ['plxtech,nas782x-sata']
2020-10-13 09:06:01,039 - DEBUG - UpdateHardwareDT - scanhwdt - skip improper or duplicated ['ns16550a']
2020-10-13 09:06:01,039 - DEBUG - UpdateHardwareDT - scanhwdt - skip improper or duplicated ['plxtech,nas782x-rps-timer']
2020-10-13 09:06:01,039 - DEBUG - UpdateHardwareDT - scanhwdt - skip improper or duplicated ['mpcore_wdt']
2020-10-13 09:06:01,039 - DEBUG - UpdateHardwareDT - scanhwdt - skip improper or duplicated ['arm,arm11mp-twd-timer']
2020-10-13 09:06:01,466 - DEBUG - UpdateHardwareDT - scanhwdt - skip supported ['plxtech,nas782x-pcie']
2020-10-13 09:06:01,895 - DEBUG - UpdateHardwareDT - scanhwdt - skip supported ['plxtech,nas782x-gpio']
2020-10-13 09:06:02,317 - DEBUG - UpdateHardwareDT - scanhwdt - skip supported ['plxtech,nas782x-pllb']
2020-10-13 09:06:02,751 - DEBUG - UpdateHardwareDT - scanhwdt - skip supported ['plxtech,nas782x-plla']
2020-10-13 09:06:02,751 - DEBUG - UpdateHardwareDT - scanhwdt - skip improper or duplicated ['plxtech,nas782x-rps']
2020-10-13 09:06:03,174 - DEBUG - UpdateHardwareDT - scanhwdt - skip supported ['plxtech,nas782x-reset']
2020-10-13 09:06:03,174 - DEBUG - UpdateHardwareDT - scanhwdt - skip improper or duplicated ['arm,arm11mp-gic']
2020-10-13 09:06:03,175 - INFO - AnalysesManager - snapshot - profile at /root/firmguide/.profile
```

### `unpack`

This plugin unpacks firmware to components (Please see the example below. The components start with path_to.)
It extends `Binwalk` and is compatible with more firmware.

```txt
root@esv:~/firmguide# ./firmguide unpack -f example/62771d14b82e554a95d048af99866c404acb196f.bin
2020-10-13 09:14:03,579 - INFO - AnalysesManager - chain cont'd - unpack
2020-10-13 09:14:06,832 - INFO - Unpack - unpack - find /root/firmguide/_62771d14b82e554a95d048af99866c404acb196f.bin.extracted/3DFB18.dtb
2020-10-13 09:14:06,832 - INFO - Unpack - unpack - output: 0x000590D0    SHA256 hash constants, little endian
2020-10-13 09:14:06,832 - INFO - Unpack - unpack - output: 0x00064404    CRC32 polynomial table, little endian
2020-10-13 09:14:06,832 - INFO - Unpack - unpack - output: 0x00064804    CRC32 polynomial table, little endian
2020-10-13 09:14:06,832 - INFO - Unpack - unpack - output: 0x00066D21    LZO compressed data
2020-10-13 09:14:06,832 - INFO - Unpack - unpack - output: 0x000A0000    flattened image tree, total size: 3414504 bytes, timestamp: 2017-10-18 13:12:42, description: ARM OpenWrt FIT (Flattened Image Tree)
2020-10-13 09:14:06,832 - INFO - Unpack - unpack - output: 0x000A00E4    LZMA compressed data, properties: 0x6D, dictionary size: 8388608 bytes, uncompressed size: 3372000 bytes
2020-10-13 09:14:06,832 - INFO - Unpack - unpack - output: 0x003DFB18    Flattened a device tree, size: 7083 bytes, version: 17
2020-10-13 09:14:06,832 - INFO - Unpack - unpack - supported: True
2020-10-13 09:14:06,832 - INFO - Unpack - unpack - path_to_raw: /root/images/62771d14b82e554a95d048af99866c404acb196f.bin
2020-10-13 09:14:06,832 - INFO - Unpack - unpack - type: 3
2020-10-13 09:14:06,832 - INFO - Unpack - unpack - path_to_image: /root/firmguide/_62771d14b82e554a95d048af99866c404acb196f.bin.extracted/A0000.uimage.fit
2020-10-13 09:14:06,833 - INFO - Unpack - unpack - path_to_kernel: /root/firmguide/_62771d14b82e554a95d048af99866c404acb196f.bin.extracted/_A0000.uimage.kernel.extracted/0
2020-10-13 09:14:06,833 - INFO - Unpack - unpack - path_to_dtb: /root/firmguide/_62771d14b82e554a95d048af99866c404acb196f.bin.extracted/3DFB18.dtb
2020-10-13 09:14:06,833 - INFO - Unpack - unpack - path_to_rootfs: None
2020-10-13 09:14:06,833 - INFO - Unpack - unpack - path_to_uimage: /root/firmguide/_62771d14b82e554a95d048af99866c404acb196f.bin.extracted/_A0000.uimage.kernel.extracted/0.uimage
2020-10-13 09:14:06,838 - INFO - AnalysesManager - snapshot - profile at /root/firmguide/.profile
```

### `cmdcoverup`

This plugin unpacks the firmware, repacks the inside Linux kernel with a uImage header
(such that you have to pass a load address by `-ld`), and constructs a command line
that boots the Linux kernel with QEMU (such that you have to pass
extra architecture information by `-a` and `-e`). It optionally constructs a command line
that exposes a QEMU GDB interface
(such that you have to pass extra source information by `-s`).

```txt
root@esv:~/firmguide# ./firmguide cmdcoverup -f /root/images/62771d14b82e554a95d048af99866c404acb196f.bin -s /mnt/iscsi/openwrt-build-docker/share/15.05-bfae3162fb949c343763ad9ea7ab3fe0/./chaos_calmer-15.05/build_dir/target-arm_mpcore_uClibc-0.9.33.2_eabi/linux-oxnas/linux-3.18.20
2020-10-16 09:29:17,904 - INFO - AnalysesManager - chain - msearch(invalid)->bfilter(invalid)->unpack->preprocdt->synthesisdt(invalid)
2020-10-16 09:29:17,904 - INFO - AnalysesManager - chain cont'd - loaddr(invalid)->preparation->pbtngcmd
2020-10-16 09:29:21,204 - INFO - Unpack - unpack - find /root/esv-latest/_62771d14b82e554a95d048af99866c404acb196f.bin.extracted/3DFB18.dtb
2020-10-16 09:29:21,212 - INFO - DTPreprocessing - preprocdt - dtb at /root/esv-latest/_62771d14b82e554a95d048af99866c404acb196f.bin.extracted/3DFB18.dtb
2020-10-16 09:29:21,212 - INFO - DTPreprocessing - preprocdt - dts at /root/esv-latest/3DFB18.dtb.dts
2020-10-16 09:29:21,212 - INFO - DTPreprocessing - preprocdt - board id 0xFFFFFFFF is chosen automatically
2020-10-16 09:29:21,251 - INFO - DTPreprocessing - preprocdt - arch arm is chosen automatically
2020-10-16 09:29:21,251 - INFO - DTPreprocessing - preprocdt - endian l is chosen automatically
2020-10-16 09:29:21,251 - INFO - DTPreprocessing - preprocdt - load address 0x00008000 is chosen automatically
2020-10-16 09:29:24,108 - INFO - Preparation - preparation - repack kernel with arm/0x00008000/0x00008000
2020-10-16 09:29:24,109 - INFO - Preparation - preparation - get command: /tmp/qemu-4.0.0/arm-softmmu/qemu-system-arm -M plxtech_nas7820_plxtech_nas782x -kernel /root/esv-latest/_62771d14b82e554a95d048af99866c404acb196f.bin.extracted/_A0000.uimage.kernel.extracted/0.uimage -dtb /root/esv-latest/_62771d14b82e554a95d048af99866c404acb196f.bin.extracted/3DFB18.dtb -nographic -initrd /root/esv-latest/rootfs/armel.cpio.rootfs -append "console=ttyS0 nowatchdog nokaslr"
2020-10-16 09:29:24,109 - INFO - PBtngCMD - pbtngcmd - /tmp/qemu-4.0.0/arm-softmmu/qemu-system-arm -M plxtech_nas7820_plxtech_nas782x -kernel /root/esv-latest/_62771d14b82e554a95d048af99866c404acb196f.bin.extracted/_A0000.uimage.kernel.extracted/0.uimage -dtb /root/esv-latest/_62771d14b82e554a95d048af99866c404acb196f.bin.extracted/3DFB18.dtb -nographic -initrd /root/esv-latest/rootfs/armel.cpio.rootfs -append "console=ttyS0 nowatchdog nokaslr"
2020-10-16 09:29:24,109 - INFO - PBtngCMD - pbtngcmd - RUN /tmp/qemu-4.0.0/arm-softmmu/qemu-system-arm -M plxtech_nas7820_plxtech_nas782x -kernel /root/esv-latest/_62771d14b82e554a95d048af99866c404acb196f.bin.extracted/_A0000.uimage.kernel.extracted/0.uimage -dtb /root/esv-latest/_62771d14b82e554a95d048af99866c404acb196f.bin.extracted/3DFB18.dtb -nographic -initrd /root/esv-latest/rootfs/armel.cpio.rootfs -append "console=ttyS0 nowatchdog nokaslr" -s -S
2020-10-16 09:29:24,109 - INFO - PBtngCMD - pbtngcmd - PRESS ctrl-a x to exit; PRESS ctrl-a c to QEMU console
2020-10-16 09:29:24,109 - INFO - PBtngCMD - pbtngcmd - In QEMU console: enter system_reset to reset
2020-10-16 09:29:24,109 - INFO - PBtngCMD - pbtngcmd - In QEMU console: enter info mtree to show memory layout
2020-10-16 09:29:24,109 - INFO - PBtngCMD - pbtngcmd - In QEMU console: enter info qtree to show device layout
2020-10-16 09:29:24,109 - INFO - PBtngCMD - pbtngcmd - OPEN *ANOTHER* SHELL and RUN gdb-multiarch --cd=/mnt/iscsi/openwrt-build-docker/share/15.05-bfae3162fb949c343763ad9ea7ab3fe0/./chaos_calmer-15.05/build_dir/target-arm_mpcore_uClibc-0.9.33.2_eabi/linux-oxnas/linux-3.18.20 /mnt/iscsi/openwrt-build-docker/share/15.05-bfae3162fb949c343763ad9ea7ab3fe0/./chaos_calmer-15.05/build_dir/target-arm_mpcore_uClibc-0.9.33.2_eabi/linux-oxnas/linux-3.18.20/vmlinux -ex "target remote:1234"
2020-10-16 09:29:24,109 - INFO - PBtngCMD - pbtngcmd - SEVERAL BPS YOU MAY INTERESTED IN:
2020-10-16 09:29:24,109 - INFO - PBtngCMD - pbtngcmd -     b kernel_entry # MIPS
2020-10-16 09:29:24,109 - INFO - PBtngCMD - pbtngcmd -     b start_kernel
2020-10-16 09:29:24,109 - INFO - PBtngCMD - pbtngcmd -     b setup_arch
2020-10-16 09:29:24,109 - INFO - PBtngCMD - pbtngcmd -     b prom_init # MIPS
2020-10-16 09:29:24,110 - INFO - PBtngCMD - pbtngcmd -     b prom_putchar # MIPS
2020-10-16 09:29:24,110 - INFO - PBtngCMD - pbtngcmd -     b init_IRQ
2020-10-16 09:29:24,110 - INFO - PBtngCMD - pbtngcmd -     b time_init
2020-10-16 09:29:24,110 - INFO - PBtngCMD - pbtngcmd -     b calibrate_delay    b rest_init
2020-10-16 09:29:24,110 - INFO - PBtngCMD - pbtngcmd -     b kernel_init
2020-10-16 09:29:24,110 - INFO - PBtngCMD - pbtngcmd -     b populate_rootfs
2020-10-16 09:29:24,110 - INFO - PBtngCMD - pbtngcmd -     b run_init_process
2020-10-16 09:29:24,110 - INFO - PBtngCMD - pbtngcmd -     b panic
2020-10-16 09:29:24,110 - INFO - PBtngCMD - pbtngcmd - SOMETHING YOU NEED TO KNOW:
2020-10-16 09:29:24,110 - INFO - PBtngCMD - pbtngcmd -     calibrate_delay in start_kernel should never be stuck
2020-10-16 09:29:24,110 - INFO - PBtngCMD - pbtngcmd -     do_initcalls in do_basic_setup should never be stuck
2020-10-16 09:29:24,110 - INFO - PBtngCMD - pbtngcmd -     prepare_namespace in kernel_init_freeable should never be called
2020-10-16 09:29:24,116 - INFO - AnalysesManager - snapshot - profile at /root/esv-latest/.profile
```

### `loaddr`

This plugin finds the load address of a Linux kernel image
with the help of the source code.

```txt
root@esv:~/firmguide# ./firmguide loaddr -s /mnt/iscsi/openwrt-build-docker/share/15.05-bfae3162fb949c343763ad9ea7ab3fe0/./chaos_calmer-15.05/build_dir/target-arm_mpcore_uClibc-0.9.33.2_eabi/linux-oxnas/linux-3.18.20
2020-10-16 09:59:42,168 - INFO - AnalysesManager - chain cont'd - loaddr
2020-10-16 09:59:42,168 - INFO - CalcLoadAddr - loaddr - get arm loading address 0x8000 from lds
2020-10-16 09:59:42,169 - INFO - AnalysesManager - snapshot - profile at /root/esv-latest/.profile
```

### `ofinitsrc`

This plugin finds all `IRQCHIP_DECLARE`, etc. declares and updates this information
in our hardware database. This plugin is used at the very beginning
and will be rarely used in the future. No example because of too much output.

### `ofinitcbs`

This plugin finds all callback functions defined in `IRQCHIP_DECLARE`, etc. for
hardware listed in the given a device tree blob. It is quite useful for manual analysis.

```txt
root@esv:~/firmguide# ./firmguide ofinitcbs -dtb slcore/database/archivedtb/plxtech_nas782x.dtb -s /mnt/iscsi/openwrt-build-docker/share/15.05-bfae3162fb949c343763ad9ea7ab3fe0/./chaos_calmer-15.05/build_dir/target-arm_mpcore_uClibc-0.9.33.2_eabi/linux-oxnas/linux-3.18.20
2020-10-13 09:48:01,397 - INFO - AnalysesManager - chain cont'd - ofinitsrc
2020-10-13 09:48:01,404 - INFO - OfInitSrc - ofinitsrc - searching compatible = ['plxtech,nas7820', 'plxtech,nas782x']
2020-10-13 09:48:05,205 - INFO - OfInitSrc - ofinitsrc - searching compatible = ['gpio-leds']
2020-10-13 09:48:07,001 - INFO - OfInitSrc - ofinitsrc - searching compatible = ['plxtech,nas782x-ehci']
2020-10-13 09:48:08,885 - INFO - OfInitSrc - ofinitsrc - searching compatible = ['plxtech,nas782x-gmac', 'snps,dwmac']
2020-10-13 09:48:12,582 - INFO - OfInitSrc - ofinitsrc - searching compatible = ['plxtech,nand-nas782x', 'gen_nand']
2020-10-13 09:48:16,422 - INFO - OfInitSrc - ofinitsrc - searching compatible = ['plxtech,nas782x-sata']
2020-10-13 09:48:18,329 - INFO - OfInitSrc - ofinitsrc - searching compatible = ['ns16550a']
2020-10-13 09:48:20,118 - INFO - OfInitSrc - ofinitsrc - searching compatible = ['plxtech,nas782x-rps-timer']
2020-10-13 09:48:22,010 - INFO - OfInitSrc - ofinitsrc - [bingo] ('CLOCKSOURCE_OF_DECLARE', 'plxtech,nas782x-rps-timer', 'rps_timer_init') in ...ux-oxnas/linux-3.18.20/drivers/clocksource/oxnas_rps_timer.c
2020-10-13 09:48:22,011 - INFO - OfInitSrc - ofinitsrc - searching compatible = ['mpcore_wdt']
2020-10-13 09:48:23,794 - INFO - OfInitSrc - ofinitsrc - searching compatible = ['arm,arm11mp-twd-timer']
2020-10-13 09:48:25,679 - INFO - OfInitSrc - ofinitsrc - [bingo] ('CLOCKSOURCE_OF_DECLARE', 'arm,arm11mp-twd-timer', 'twd_local_timer_of_register') in ...ux-oxnas/linux-3.18.20/arch/arm/kernel/smp_twd.c
2020-10-13 09:48:25,683 - INFO - OfInitSrc - ofinitsrc - searching compatible = ['plxtech,nas782x-pcie']
2020-10-13 09:48:27,633 - INFO - OfInitSrc - ofinitsrc - searching compatible = ['plxtech,nas782x-pcie']
2020-10-13 09:48:29,608 - INFO - OfInitSrc - ofinitsrc - searching compatible = ['plxtech,nas782x-pinctrl', 'simple-bus']
2020-10-13 09:48:33,671 - INFO - OfInitSrc - ofinitsrc - searching compatible = ['plxtech,nas782x-gpio']
2020-10-13 09:48:35,676 - INFO - OfInitSrc - ofinitsrc - searching compatible = ['plxtech,nas782x-gpio']
2020-10-13 09:48:37,691 - INFO - OfInitSrc - ofinitsrc - searching compatible = ['fixed-clock']
2020-10-13 09:48:39,637 - INFO - OfInitSrc - ofinitsrc - [bingo] ('CLK_OF_DECLARE', 'fixed-clock', 'of_fixed_clk_setup') in ...ux-oxnas/linux-3.18.20/drivers/clk/clk-fixed-rate.c
2020-10-13 09:48:39,659 - INFO - OfInitSrc - ofinitsrc - searching compatible = ['fixed-factor-clock']
2020-10-13 09:48:41,569 - INFO - OfInitSrc - ofinitsrc - [bingo] ('CLK_OF_DECLARE', 'fixed-factor-clock', 'of_fixed_factor_clk_setup') in ...ux-oxnas/linux-3.18.20/drivers/clk/clk-fixed-factor.c
2020-10-13 09:48:41,570 - INFO - OfInitSrc - ofinitsrc - searching compatible = ['plxtech,nas782x-stdclk']
2020-10-13 09:48:43,450 - INFO - OfInitSrc - ofinitsrc - [bingo] ('CLK_OF_DECLARE', 'plxtech,nas782x-stdclk', 'oxnas_init_stdclk') in ...ux-oxnas/linux-3.18.20/drivers/clk/clk-oxnas.c
2020-10-13 09:48:43,484 - INFO - OfInitSrc - ofinitsrc - searching compatible = ['plxtech,nas782x-pllb']
2020-10-13 09:48:45,388 - INFO - OfInitSrc - ofinitsrc - [bingo] ('CLK_OF_DECLARE', 'plxtech,nas782x-pllb', 'oxnas_init_pllb') in ...ux-oxnas/linux-3.18.20/drivers/clk/clk-oxnas.c
2020-10-13 09:48:45,420 - INFO - OfInitSrc - ofinitsrc - searching compatible = ['plxtech,nas782x-plla']
2020-10-13 09:48:47,311 - INFO - OfInitSrc - ofinitsrc - [bingo] ('CLK_OF_DECLARE', 'plxtech,nas782x-plla', 'oxnas_init_plla') in ...ux-oxnas/linux-3.18.20/drivers/clk/clk-oxnas.c
2020-10-13 09:48:47,343 - INFO - OfInitSrc - ofinitsrc - searching compatible = ['fixed-factor-clock']
2020-10-13 09:48:49,263 - INFO - OfInitSrc - ofinitsrc - [bingo] ('CLK_OF_DECLARE', 'fixed-factor-clock', 'of_fixed_factor_clk_setup') in ...ux-oxnas/linux-3.18.20/drivers/clk/clk-fixed-factor.c
2020-10-13 09:48:49,264 - INFO - OfInitSrc - ofinitsrc - searching compatible = ['fixed-clock']
2020-10-13 09:48:51,221 - INFO - OfInitSrc - ofinitsrc - [bingo] ('CLK_OF_DECLARE', 'fixed-clock', 'of_fixed_clk_setup') in ...ux-oxnas/linux-3.18.20/drivers/clk/clk-fixed-rate.c
2020-10-13 09:48:51,244 - INFO - OfInitSrc - ofinitsrc - searching compatible = ['plxtech,nas782x-rps']
2020-10-13 09:48:53,142 - INFO - OfInitSrc - ofinitsrc - [bingo] ('IRQCHIP_DECLARE', 'plxtech,nas782x-rps', 'rps_of_init') in ...ux-oxnas/linux-3.18.20/drivers/irqchip/irq-rps.c
2020-10-13 09:48:53,175 - INFO - OfInitSrc - ofinitsrc - searching compatible = ['plxtech,nas782x-reset']
2020-10-13 09:48:55,104 - INFO - OfInitSrc - ofinitsrc - searching compatible = ['arm,arm11mp-gic']
2020-10-13 09:48:57,093 - INFO - OfInitSrc - ofinitsrc - [bingo] ('IRQCHIP_DECLARE', 'arm,arm11mp-gic', 'gic_of_init') in ...ux-oxnas/linux-3.18.20/drivers/irqchip/irq-gic.c
[-] cannot recognize "arm,gic-400",IRQCHIP_DECLARE(cortex_a15_gic, "arm,cortex-a15-gic" in ...ild_dir/target-arm_mpcore_uClibc-0.9.33.2_eabi/linux-oxnas/linux-3.18.20/patches/platform/320-oxnas-irqchip.patch
2020-10-13 09:48:57,093 - INFO - OfInitSrc - ofinitsrc - [bingo] ('IRQCHIP_DECLARE', 'arm,arm11mp-gic', 'gic_of_init') in ...ux-oxnas/linux-3.18.20/patches/platform/320-oxnas-irqchip.patch
2020-10-13 09:48:57,094 - INFO - OfInitSrc - ofinitsrc - searching compatible = ['arm,arm11mpcore']
2020-10-13 09:48:58,967 - INFO - AnalysesManager - snapshot - profile at /root/firmguide/.profile
```

### `coverup`

This plugin covers up a QEMU debug trace (firmguide.trace by default).
Architecture information (`-a`, `-e`) is needed
because the trace is architecture-dependent.
If `-s` is available, a call stack is then printed.

```txt
root@esv:~/firmguide#  ./firmguide -a arm -e l coverup -s /mnt/iscsi/openwrt-build-docker/share/15.05-bfae3162fb949c343763ad9ea7ab3fe0/./chaos_calmer-15.05/build_dir/target-arm_mpcore_uClibc-0.9.33.2_eabi/linux-oxnas/linux-3.18.20
2020-10-13 09:53:31,852 - INFO - AnalysesManager - chain cont'd - userlevel(invalid)->fastuserlevel(invalid)->tracing(invalid)->preparation(invalid)->loadtrace
2020-10-13 09:53:31,852 - INFO - AnalysesManager - chain cont'd - codemissing->tlbexcep->callstack->deadloop->undefinst
2020-10-13 09:53:31,852 - INFO - AnalysesManager - chain cont'd - databort
2020-10-13 09:53:31,852 - INFO - LoadTrace - loadtrace - loading firmguide.trace ...
2020-10-13 09:53:38,232 - INFO - LoadTrace - loadtrace - load 110386 basic blocks
2020-10-13 09:53:58,899 - INFO - ShowCallstack - callstack - ln 110994 0xc0432c04 -> 0xc0432c08 returned False cpucache_init -> __schedule
2020-10-13 09:53:59,734 - INFO - ShowCallstack - callstack - ln 223986 --0xc0033468 -> 0xc003346c returned False alloc_unbound_pwq -> __release_region
2020-10-13 09:54:07,653 - INFO - ShowCallstack - callstack - ln 1914763 ----0xc017307c -> 0xc0173080 returned False argv_split -> generic_file_direct_write
2020-10-13 09:54:07,663 - INFO - ShowCallstack - callstack - ln 1914789 ------0xc0080500 -> 0xc0080504 returned False generic_file_direct_write -> __release_region
2020-10-13 09:54:13,163 - INFO - ShowCallstack - callstack - ln 2270169 --------0x17ae8 -> 0x17aec returned False None -> None
2020-10-13 09:54:13,213 - INFO - ShowCallstack - callstack - ln 2273818 ----------0x18304 -> 0x18308 returned False None -> None
2020-10-13 09:54:13,233 - INFO - ShowCallstack - callstack - ln 2274208 ------------0x1821c -> 0x18220 returned False None -> None
2020-10-13 09:54:13,587 - INFO - ShowCallstack - callstack - ln 2311056 --------------0x98574 -> 0x98578 returned False None -> None
2020-10-13 09:54:13,607 - INFO - ShowCallstack - callstack - ln 2311295 ----------------0x98424 -> 0x98428 returned False None -> None
2020-10-13 09:54:13,625 - INFO - ShowCallstack - callstack - ln 2311380 ------------------0xb6e88fb8 -> 0xb6e88fbc returned False None -> None
2020-10-13 09:54:14,013 - INFO - ShowCallstack - callstack - ln 2349450 --------------------0x17ed4 -> 0x17ed8 returned False None -> None
2020-10-13 09:54:14,032 - INFO - ShowCallstack - callstack - ln 2349474 ----------------------0x18974 -> 0x18978 returned False None -> None
2020-10-13 09:54:14,050 - INFO - ShowCallstack - callstack - ln 2349499 ------------------------0xb6deefd8 -> 0xb6deefdc returned False None -> None
2020-10-13 09:54:14,091 - INFO - ShowCallstack - callstack - ln 2351802 --------------------------0xb6deef70 -> 0xb6deef74 returned False None -> None
2020-10-13 09:54:14,103 - INFO - ShowCallstack - callstack - ln 2351915 ----------------------------0xc00252d4 -> 0xc00252d8 returned False proc_taint -> __release_region
2020-10-13 09:54:14,694 - INFO - ShowCallstack - callstack - ln 2416234 ------------------------------0xb6e28fd8 -> 0xb6e28fdc returned False None -> None
2020-10-13 09:54:14,741 - INFO - ShowCallstack - callstack - ln 2419495 --------------------------------0xb6e28f70 -> 0xb6e28f74 returned False None -> None
2020-10-13 09:54:15,072 - INFO - ShowCallstack - callstack - ln 2457910 ----------------------------------0xb6ddffd8 -> 0xb6ddffdc returned False None -> None
2020-10-13 09:54:15,113 - INFO - ShowCallstack - callstack - ln 2460253 ------------------------------------0xb6ddff70 -> 0xb6ddff74 returned False None -> None
2020-10-13 09:54:15,617 - INFO - ShowCallstack - callstack - ln 2517456 --------------------------------------0xb6e22fd8 -> 0xb6e22fdc returned False None -> None
2020-10-13 09:54:15,663 - INFO - ShowCallstack - callstack - ln 2520552 ----------------------------------------0xb6e22f70 -> 0xb6e22f74 returned False None -> None
2020-10-13 09:54:16,051 - INFO - ShowCallstack - callstack - ln 2564395 ------------------------------------------0xb6da5fd8 -> 0xb6da5fdc returned False None -> None
2020-10-13 09:54:16,095 - INFO - ShowCallstack - callstack - ln 2567126 --------------------------------------------0xb6da5f70 -> 0xb6da5f74 returned False None -> None
2020-10-13 09:54:16,477 - INFO - ShowCallstack - callstack - ln 2610735 ----------------------------------------------0xb6de1fd8 -> 0xb6de1fdc returned False None -> None
2020-10-13 09:54:16,516 - INFO - ShowCallstack - callstack - ln 2612928 ------------------------------------------------0xb6de1f70 -> 0xb6de1f74 returned False None -> None
2020-10-13 09:54:16,836 - INFO - ShowCallstack - callstack - ln 2650077 --------------------------------------------------0xb6e80fd8 -> 0xb6e80fdc returned False None -> None
2020-10-13 09:54:16,877 - INFO - ShowCallstack - callstack - ln 2652600 ----------------------------------------------------0xb6e80f70 -> 0xb6e80f74 returned False None -> None
2020-10-13 09:54:17,224 - INFO - ShowCallstack - callstack - ln 2689322 ------------------------------------------------------0xb6e3dfd8 -> 0xb6e3dfdc returned False None -> None
2020-10-13 09:54:17,578 - INFO - ShowCallstack - callstack - ln 2728196 --------------------------------------------------------0xb6e12fd8 -> 0xb6e12fdc returned False None -> None
2020-10-13 09:54:17,618 - INFO - ShowCallstack - callstack - ln 2730599 ----------------------------------------------------------0xb6e12f70 -> 0xb6e12f74 returned False None -> None
2020-10-13 09:54:17,978 - INFO - ShowCallstack - callstack - ln 2772021 ------------------------------------------------------------0xb6dd3fd8 -> 0xb6dd3fdc returned False None -> None
2020-10-13 09:54:18,024 - INFO - ShowCallstack - callstack - ln 2774747 --------------------------------------------------------------0xb6dd3f70 -> 0xb6dd3f74 returned False None -> None
2020-10-13 09:54:18,615 - INFO - ShowCallstack - callstack - ln 2841940 ----------------------------------------------------------------0x527b0 -> 0x527b4 returned False None -> None
2020-10-13 09:54:18,632 - INFO - ShowCallstack - callstack - ln 2841959 ------------------------------------------------------------------0x516f4 -> 0x516f8 returned False None -> None
2020-10-13 09:54:19,399 - INFO - ShowCallstack - callstack - ln 2930535 --------------------------------------------------------------------0x85208 -> 0x8520c returned False None -> None
2020-10-13 09:54:19,416 - INFO - ShowCallstack - callstack - ln 2930609 ----------------------------------------------------------------------0xb6e85fb8 -> 0xb6e85fbc returned False None -> None
2020-10-13 09:54:20,603 - INFO - ShowCallstack - callstack - ln 3075878 ------------------------------------------------------------------------0xb6e09fb8 -> 0xb6e09fbc returned False None -> None
2020-10-13 09:54:23,120 - INFO - ShowCallstack - callstack - ln 3407281 --------------------------------------------------------------------------0xb6da8fd8 -> 0xb6da8fdc returned False None -> None
2020-10-13 09:54:23,145 - INFO - ShowCallstack - callstack - ln 3408296 ----------------------------------------------------------------------------0xa590c -> 0xa5910 returned False None -> None
2020-10-13 09:54:23,251 - INFO - ShowCallstack - callstack - ln 3419825 ------------------------------------------------------------------------------0xb6da8f70 -> 0xb6da8f74 returned False None -> None
2020-10-13 09:54:23,602 - INFO - ShowCallstack - callstack - ln 3458798 --------------------------------------------------------------------------------0x7f5f0 -> 0x7f5f4 returned False None -> None
2020-10-13 09:54:23,643 - INFO - ShowCallstack - callstack - ln 3462439 ----------------------------------------------------------------------------------0x9b0b0 -> 0x9b0b4 returned False None -> None
2020-10-13 09:54:23,660 - INFO - ShowCallstack - callstack - ln 3462453 ------------------------------------------------------------------------------------0xb6dedfd8 -> 0xb6dedfdc returned False None -> None
2020-10-13 09:54:24,454 - INFO - ShowCallstack - callstack - ln 3553945 --------------------------------------------------------------------------------------0xb6e0ffd8 -> 0xb6e0ffdc returned False None -> None
2020-10-13 09:54:24,479 - INFO - ShowCallstack - callstack - ln 3554805 ----------------------------------------------------------------------------------------0xb6e79fd8 -> 0xb6e79fdc returned False None -> None
2020-10-13 09:54:24,548 - INFO - ShowCallstack - callstack - ln 3560468 ------------------------------------------------------------------------------------------0xb6e0ff70 -> 0xb6e0ff74 returned False None -> None
2020-10-13 09:54:24,570 - INFO - ShowCallstack - callstack - ln 3561641 --------------------------------------------------------------------------------------------0xb6e79f70 -> 0xb6e79f74 returned False None -> None
2020-10-13 09:54:24,600 - INFO - ShowCallstack - callstack - ln 3564600 ----------------------------------------------------------------------------------------------0xb6e5ffd8 -> 0xb6e5ffdc returned False None -> None
2020-10-13 09:54:24,653 - INFO - ShowCallstack - callstack - ln 3569755 ------------------------------------------------------------------------------------------------0xb6e5ff70 -> 0xb6e5ff74 returned False None -> None
2020-10-13 09:54:25,397 - INFO - ShowCallstack - callstack - ln 3681917 --------------------------------------------------------------------------------------------------0xb6e7dfd8 -> 0xb6e7dfdc returned False None -> None
2020-10-13 09:54:25,480 - INFO - ShowCallstack - callstack - ln 3693416 ----------------------------------------------------------------------------------------------------0x4d620 -> 0x4d624 returned False None -> None
2020-10-13 09:54:25,497 - INFO - ShowCallstack - callstack - ln 3693557 ------------------------------------------------------------------------------------------------------0xb6e4b6a4 -> 0xb6e4b6a8 returned False None -> None
2020-10-13 09:54:25,515 - INFO - ShowCallstack - callstack - ln 3693624 --------------------------------------------------------------------------------------------------------0x59810 -> 0x59814 returned False None -> None
2020-10-13 09:54:25,578 - INFO - ShowCallstack - callstack - ln 3702714 ----------------------------------------------------------------------------------------------------------0xb6e8bfd8 -> 0xb6e8bfdc returned False None -> None
2020-10-13 09:54:25,629 - INFO - ShowCallstack - callstack - ln 3706932 ------------------------------------------------------------------------------------------------------------0xb6e8bf70 -> 0xb6e8bf74 returned False None -> None
2020-10-13 09:54:26,354 - INFO - ShowCallstack - callstack - ln 3799120 --------------------------------------------------------------------------------------------------------------0xb6dfbfd8 -> 0xb6dfbfdc returned False None -> None
2020-10-13 09:54:26,394 - INFO - ShowCallstack - callstack - ln 3801523 ----------------------------------------------------------------------------------------------------------------0xb6dfbf70 -> 0xb6dfbf74 returned False None -> None
2020-10-13 09:54:26,780 - INFO - ShowCallstack - callstack - ln 3848167 ------------------------------------------------------------------------------------------------------------------0xb6dabfd8 -> 0xb6dabfdc returned False None -> None
2020-10-13 09:54:26,820 - INFO - ShowCallstack - callstack - ln 3850650 --------------------------------------------------------------------------------------------------------------------0xb6dabf70 -> 0xb6dabf74 returned False None -> None
2020-10-13 09:54:26,884 - INFO - ShowCallstack - callstack - ln 3859867 ----------------------------------------------------------------------------------------------------------------------0xb6e886a4 -> 0xb6e886a8 returned False None -> None
2020-10-13 09:54:27,279 - INFO - ShowCallstack - callstack - ln 3908028 ------------------------------------------------------------------------------------------------------------------------0xb6d9bfd8 -> 0xb6d9bfdc returned False None -> None
2020-10-13 09:54:27,321 - INFO - ShowCallstack - callstack - ln 3910511 --------------------------------------------------------------------------------------------------------------------------0xb6d9bf70 -> 0xb6d9bf74 returned False None -> None
2020-10-13 09:54:28,005 - INFO - ShowCallstack - callstack - ln 3992632 ----------------------------------------------------------------------------------------------------------------------------0xb6de9fd8 -> 0xb6de9fdc returned False None -> None
2020-10-13 09:54:28,045 - INFO - ShowCallstack - callstack - ln 3994840 ------------------------------------------------------------------------------------------------------------------------------0xb6de9f70 -> 0xb6de9f74 returned False None -> None
2020-10-13 09:54:28,500 - INFO - ShowCallstack - callstack - ln 4047641 --------------------------------------------------------------------------------------------------------------------------------0x317c8 -> 0x317cc returned False None -> None
2020-10-13 09:54:28,518 - INFO - ShowCallstack - callstack - ln 4047773 ----------------------------------------------------------------------------------------------------------------------------------0xb6e35c5c -> 0xb6e35c60 returned False None -> None
2020-10-13 09:54:28,583 - INFO - ShowCallstack - callstack - ln 4057559 ------------------------------------------------------------------------------------------------------------------------------------0x59d94 -> 0x59d98 returned False None -> None
2020-10-13 09:54:28,938 - INFO - ShowCallstack - callstack - ln 4096825 --------------------------------------------------------------------------------------------------------------------------------------0xb6e05fb8 -> 0xb6e05fbc returned False None -> None
2020-10-13 09:54:29,289 - INFO - ShowCallstack - callstack - ln 4136105 ----------------------------------------------------------------------------------------------------------------------------------------0xb6d93fd8 -> 0xb6d93fdc returned False None -> None
2020-10-13 09:54:29,327 - INFO - ShowCallstack - callstack - ln 4138218 ------------------------------------------------------------------------------------------------------------------------------------------0xb6d93f70 -> 0xb6d93f74 returned False None -> None
2020-10-13 09:54:30,119 - INFO - ShowCallstack - callstack - ln 4226578 --------------------------------------------------------------------------------------------------------------------------------------------0xb6e53fd8 -> 0xb6e53fdc returned False None -> None
2020-10-13 09:54:30,159 - INFO - ShowCallstack - callstack - ln 4229206 ----------------------------------------------------------------------------------------------------------------------------------------------0xb6e53f70 -> 0xb6e53f74 returned False None -> None
2020-10-13 09:54:31,031 - INFO - ShowCallstack - callstack - ln 4340010 ------------------------------------------------------------------------------------------------------------------------------------------------0xb6e3afd8 -> 0xb6e3afdc returned False None -> None
2020-10-13 09:54:31,072 - INFO - ShowCallstack - callstack - ln 4342783 --------------------------------------------------------------------------------------------------------------------------------------------------0xb6e3af70 -> 0xb6e3af74 returned False None -> None
2020-10-13 09:54:31,146 - INFO - ShowCallstack - callstack - ln 4350694 ----------------------------------------------------------------------------------------------------------------------------------------------------0xb6dc3fd8 -> 0xb6dc3fdc returned False None -> None
2020-10-13 09:54:31,183 - INFO - ShowCallstack - callstack - ln 4352927 ------------------------------------------------------------------------------------------------------------------------------------------------------0xb6dc3f70 -> 0xb6dc3f74 returned False None -> None
2020-10-13 09:54:31,231 - INFO - ShowCallstack - callstack - ln 4357854 --------------------------------------------------------------------------------------------------------------------------------------------------------0x4faf0 -> 0x4faf4 returned False None -> None
2020-10-13 09:54:31,249 - INFO - ShowCallstack - callstack - ln 4357905 ----------------------------------------------------------------------------------------------------------------------------------------------------------0xb6e456a4 -> 0xb6e456a8 returned False None -> None
2020-10-13 09:54:31,854 - INFO - ShowCallstack - callstack - ln 4429930 ------------------------------------------------------------------------------------------------------------------------------------------------------------0xc01e8098 -> 0xc01e809c returned False dma_buf_describe -> irq_domain_remove
2020-10-13 09:54:31,906 - INFO - ShowCallstack - callstack - ln 4438049 --------------------------------------------------------------------------------------------------------------------------------------------------------------0x98b80 -> 0x98b84 returned False None -> None
2020-10-13 09:54:34,717 - INFO - ShowDeadLoop - deadloop - deap loop from 0xc0066fe8(posix_clock_poll) to 0xc0066fd4(posix_clock_poll)
2020-10-13 09:55:12,901 - INFO - AnalysesManager - snapshot - profile at /root/firmguide/.profile
```

### `debugsrc`

This plugin moves and removes generated a QEMU virtual machine code
to QEMU source tree for debugging (`-m` is needed to locate which code to be operated).

```txt
root@esv:~/firmguide# ./firmguide debugsrc -m plxtech_nas7820_plxtech_nas782x/
2020-10-16 10:14:52,419 - INFO - AnalysesManager - chain cont'd - qdebug
2020-10-16 10:14:52,422 - INFO - QEMUDbgMachSrc - qdebug - copy /tmp/qemu-4.0.0/./hw/timer/plxtech_nas782x_rps_timer.c
2020-10-16 10:14:52,425 - INFO - QEMUDbgMachSrc - qdebug - copy /tmp/qemu-4.0.0/./hw/arm/plxtech_nas7820_plxtech_nas782x.c
2020-10-16 10:14:52,428 - INFO - QEMUDbgMachSrc - qdebug - copy /tmp/qemu-4.0.0/./include/hw/timer/plxtech_nas782x_rps_timer.h
2020-10-16 10:14:52,430 - INFO - AnalysesManager - snapshot - profile at /root/esv-latest/.profile
root@openwrt-builder:~/esv-latest# ./firmguide debugsrc -m plxtech_nas7820_plxtech_nas782x/  -c
2020-10-16 10:14:56,613 - INFO - AnalysesManager - chain cont'd - qdebug
2020-10-16 10:14:56,615 - INFO - QEMUDbgMachSrc - qdebug - remove /tmp/qemu-4.0.0/./hw/timer/plxtech_nas782x_rps_timer.c
2020-10-16 10:14:56,618 - INFO - QEMUDbgMachSrc - qdebug - remove /tmp/qemu-4.0.0/./hw/arm/plxtech_nas7820_plxtech_nas782x.c
2020-10-16 10:14:56,621 - INFO - QEMUDbgMachSrc - qdebug - remove /tmp/qemu-4.0.0/./include/hw/timer/plxtech_nas782x_rps_timer.h
2020-10-16 10:14:56,622 - INFO - AnalysesManager - snapshot - profile at /root/esv-latest/.profile
```

### `archive`

This plugin archives the synthesis profile to our database.
This plugin can be used after `synthesize` directly and it will use `.profile` by default.

```txt
root@esv:~/firmguide# ./firmguide archive -p plxtech_nas7820_plxtech_nas782x.yaml
2020-10-18 05:47:40,822 - INFO - AnalysesManager - chain cont'd - archive
2020-10-18 05:47:40,849 - INFO - Archive - archive - archive /root/esv-latest/slcore/database/by_compatible/plxtech_nas7820_plxtech_nas782x.yaml
2020-10-18 05:47:40,851 - INFO - AnalysesManager - snapshot - profile at /root/esv-latest/.profile
```

### `usntest`

This plugin checks the serial model and SMP status of an SoC.

```txt
root@esv:~/firmguide# ./firmguide usntest -dtb examples/plxtech_nas782x.dtb
2020-10-16 02:34:19,439 - INFO - AnalysesManager - chain cont'd - usntest
2020-10-16 02:34:19,472 - INFO - TestUSN - usntest - support serial ['ns16550a']
2020-10-16 02:34:19,473 - INFO - TestUSN - usntest - there is only 1 processor.
2020-10-16 02:34:19,474 - INFO - AnalysesManager - snapshot - profile at /root/firmguide/.profile
```

### `analysrc`

This plugin preprocesses the file given or containing a given function for further analysis.

```txt
root@esv:~/firmguide# ./firmguide analysrc -e setup_arch -s linux-3.18.20 -cc /mnt/iscsi/openwrt-build-docker/share/15.05-bfae3162fb949c343763ad9ea7ab3fe0/./chaos_calmer-15.05/build_dir/target-arm_mpcore_uClibc-0.9.33.2_eabi/OpenWrt-SDK-15.05-oxnas_gcc-4.8-linaro_uClibc-0.9.33.2_eabi.Linux-x86_64/staging_dir/toolchain-arm_mpcore_gcc-4.8-linaro_uClibc-0.9.33.2_eabi/bin/arm-openwrt-linux-
2020-10-20 02:20:03,865 - INFO - AnalysesManager - chain cont'd - quicksrca
2020-10-20 02:20:04,892 - INFO - QuickSrcA - quicksrca - find setup_arch in arch/arm/kernel/setup.c
2020-10-20 02:20:04,971 - INFO - QuickSrcA - quicksrca - preprocess and save as linux-3.18.20/arch/arm/kernel/setup.i
2020-10-20 02:20:04,973 - INFO - AnalysesManager - snapshot - profile at /root/firmguide/.profile
```

# Development

## Add analysis (group)

An analysis focuses on a specific task, such as parsing a device tree blob,
which is the basic schedule unit in FirmGuide. Each analysis is a Python
class and all of them are put under `slcore/analysis`.
Several analyses work together as an analysis group that is more powerful
to accomplish a complex task. The group of analysis is defined in `slcore/aconfigs`.

Here is the template of an analysis.
```Python
# slcore/analyses/analysis_name.py
from slcore.amanager import Analysis

class AnalysisClassName(Analysis):
      def __init__(self, analysis_manager):
         super().__init__(analysis_manager)
         self.name = 'analysis_name'
         self.description = 'analysis description'
         self.required = []  # what other analysis that should be executed in advance

      def run(self):
         return True
```

Here is an example of the analysis group definition.

```yaml
# touch slcore/aconfigs/plugins/xxx.a.yaml
AnalysisGroupClassName:
   analyses: [AnalysisClassName1, AnalysisClassName2, AnalysisClassName3]
   description: 'analysis group description'
```

## APIs for analysis (group)

### Analysis Manager

```python
def run(self, **kwargs):
    # get details of the project
    self.analysis_manager.project.attrs['path']
    self.analysis_manager.project.attrs['base_dir']
    # log
    self.warning('message', 1)
    self.info('message', 1)
    self.debug('message', 1)
    # return False after setting an error information
    if False:
        self.error_info = 'error_info'
        return False
    return True
```

### Frimware profile getter/setter

```python
def run(self, **kwargs):
    self.analysis_manager.firmware.get_realdtb() # set_realdtb('path')
    self.analysis_manager.firmware.get_machine_name() # set_machine_name('plx-nas782x')
    self.analysis_manager.firmware.get_arch() # set_arch('arm')
    self.analysis_manager.firmware.get_endian() # set_endian('l')
    self.analysis_manager.firmware.get_components() # set_components(components)
    return True
```

### Components getter/setter

```python
def run(self, **kwargs):
    components = self.analysis_manager.firmware.get_components()

    components.get_path_to_raw() # set_path_to_raw('path')
    components.get_type() # set_type(LEGACY_UIMAGE)
    components.get_path_to_kernel() # set_path_to_kernel('path')
    components.get_path_to_dtb() #  et_path_to_dtb('path')
    components.get_path_to_uimage() # set_path_to_uimage('path')
    return True
```

### Device tree parsers (dt_parsers)

```python
from slcore.dt_parsers.common import load_dtb
from slcore.dt_parsers.compatible import find_compatible_in_fdt
from slcore.dt_parsers.cpu import find_flatten_cpu_in_fdt
from slcore.dt_parsers.serial import find_flatten_serial_in_fdt
from slcore.dt_parsers.intc import find_flatten_intc_in_fdt
from slcore.dt_parsers.timer import find_flatten_timer_in_fdt
from slcore.dt_parsers.flash import find_flatten_flash_in_fdt
from slcore.dt_parsers.misc import find_flatten_misc_in_fdt
from slcore.dt_parsers.memory import find_flatten_ram_in_fdt
from slcore.dt_parsers.mmio import find_flatten_mmio_in_fdt

def run(self, **kwargs):
    dtb = self.analysis_manager.firmware.get_realdtb()
    dts = load_dtb(dtb)
    
    find_compatible_in_fdt(dts)
    find_flatten_cpu_in_fdt(dts)
    find_flatten_serial_in_fdt(dts)
    find_flatten_intc_in_fdt(dts)
    find_flatten_timer_in_fdt(dts)
    find_flatten_flash_in_fdt(dts)
    find_flatten_misc_in_fdt(dts)
    find_flatten_ram_in_fdt(dts)
    find_flatten_mmio_in_fdt(dts)
    return True
```

### Database

Please check the implementation of [brick.py](../slcore/brick.py#L311).

### QEMU controller

Please check the implementation of [install.py](../slcore/analyses/install.py#L20).

### Source controller

Please check the implementation of [quicksrc.py](../slcore/analyses/quicksrca.py#L17)
and [ktraversal.py](../slcore/analyses/ktraversal.py#L164).

## Add subcommand

A subcommand focuses on a specific user interface,
such as uploading and booting a firmware image.
The subcommand is registered in `slcore/cmdconfigs`.

Here is an example of the subcommand registration.

```yaml
touch slcore/cmdconfigs/plugins/xxx.cmd.yaml
subcommand:
   help: "Subcommand help information"
   optional:
      opt1:
            short: o1
            # prop: val
   callback: lower_case_of_analysis_class_name_or_analysis_group_class_name
```

Note that the `prop` and `val` should follow the argument list in
[argparse.add_argument()](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.add_argument).
