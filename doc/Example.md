# Example

```
root@openwrt-builder:/home/liuqiang/firmguide# ./firmguide upload -f /root/images/ff3c5bfdd72a2f71fc1620bce068e8a21d117562.bin
2021-07-15 10:22:16,159 - INFO - AnalysesManager - chain cont'd - bfilter(invalid)->msearch(invalid)->unpack->preprocdt->synthesisdt
2021-07-15 10:22:16,160 - INFO - AnalysesManager - chain cont'd - loaddr(invalid)->preparation->install->tracing->loadtrace
2021-07-15 10:22:16,160 - INFO - AnalysesManager - chain cont'd - fastuserlevel->userlevel(invalid)->deltrace
2021-07-15 10:22:19,485 - INFO - Unpack - unpack - find /home/liuqiang/firmguide/_ff3c5bfdd72a2f71fc1620bce068e8a21d117562.bin.extracted/3D9104.dtb
2021-07-15 10:22:19,494 - INFO - DTPreprocessing - preprocdt - dtb at /home/liuqiang/firmguide/_ff3c5bfdd72a2f71fc1620bce068e8a21d117562.bin.extracted/3D9104.dtb
2021-07-15 10:22:19,494 - INFO - DTPreprocessing - preprocdt - dts at /home/liuqiang/firmguide/3D9104.dtb.dts
2021-07-15 10:22:19,494 - INFO - DTPreprocessing - preprocdt - board id 0xFFFFFFFF is chosen automatically
2021-07-15 10:22:19,534 - INFO - DTPreprocessing - preprocdt - arch arm is chosen automatically
2021-07-15 10:22:19,535 - INFO - DTPreprocessing - preprocdt - endian l is chosen automatically
2021-07-15 10:22:19,535 - INFO - DTPreprocessing - preprocdt - load address 0x00008000 is chosen automatically
2021-07-15 10:22:20,327 - WARNING - SynthesisDT - synthesisdt - cannot support intc ['plxtech,nas782x-gpio']
2021-07-15 10:22:20,405 - WARNING - SynthesisDT - synthesisdt - cannot support intc ['plxtech,nas782x-gpio']
2021-07-15 10:22:20,608 - WARNING - SynthesisDT - synthesisdt - cannot suport intc plxtech,nas782x-rps, intcp is missing
2021-07-15 10:22:25,396 - WARNING - SynthesisDT - synthesisdt - cannot support mmio ['plxtech,nas782x-rps']
2021-07-15 10:22:25,933 - INFO - SynthesisDT - synthesisdt - save at /home/liuqiang/firmguide/fg_plxtech_nas7820_plxtech_nas782x/hw/arm/fg_plxtech_nas7820_plxtech_nas782x.c
2021-07-15 10:22:25,936 - INFO - SynthesisDT - synthesisdt - save at /home/liuqiang/firmguide/fg_plxtech_nas7820_plxtech_nas782x/hw/timer/plxtech_nas782x_rps_timer.c
2021-07-15 10:22:25,936 - INFO - SynthesisDT - synthesisdt - save at /home/liuqiang/firmguide/fg_plxtech_nas7820_plxtech_nas782x/include/hw/timer/plxtech_nas782x_rps_timer.h
2021-07-15 10:22:28,777 - INFO - Preparation - preparation - repack kernel with arm/0x00008000/0x00008000
2021-07-15 10:22:28,778 - INFO - Preparation - preparation - get command: /tmp/qemu-4.0.0/arm-softmmu/qemu-system-arm -M fg_plxtech_nas7820_plxtech_nas782x -kernel /home/liuqiang/firmguide/_ff3c5bfdd72a2f71fc1620bce068e8a21d117562.bin.extracted/_A0000.uimage.kernel.extracted/0.uimage -dtb /home/liuqiang/firmguide/_ff3c5bfdd72a2f71fc1620bce068e8a21d117562.bin.extracted/3D9104.dtb -nographic -initrd /home/liuqiang/firmguide/rootfs/armel.cpio.rootfs -append "console=ttyS0 nowatchdog nokaslr"
2021-07-15 10:22:28,789 - INFO - Install - install - install /home/liuqiang/firmguide/fg_plxtech_nas7820_plxtech_nas782x
2021-07-15 10:22:31,381 - INFO - QEMUController - compile - CC      arm-softmmu/hw/timer/plxtech_nas782x_rps_timer.o
2021-07-15 10:22:31,384 - INFO - QEMUController - compile - CC      arm-softmmu/hw/arm/fg_plxtech_nas7820_plxtech_nas782x.o
2021-07-15 10:22:31,499 - INFO - QEMUController - compile - LINK    mipsel-softmmu/qemu-system-mipsel
2021-07-15 10:22:31,508 - INFO - QEMUController - compile - LINK    mips-softmmu/qemu-system-mips
2021-07-15 10:22:31,919 - INFO - QEMUController - compile - LINK    arm-softmmu/qemu-system-arm
2021-07-15 10:22:41,723 - INFO - Tracing - tracing - tracing QEMU machine fg_plxtech_nas7820_plxtech_nas782x
2021-07-15 10:22:47,475 - INFO - QEMUController - tracing - Uncompressing Linux... done, booting the kernel.
2021-07-15 10:22:55,032 - INFO - QEMUController - tracing - [    0.000000] Booting Linux on physical CPU 0x0
2021-07-15 10:22:55,092 - INFO - QEMUController - tracing - [    0.000000] Linux version 4.4.47 (buildbot@builds-02.infra.lede-project.org) (gcc version 5.4.0 (LEDE GCC 5.4.0 r3103-1b51a49) ) #0 SMP Mon Feb 6 21:34:28 2017
2021-07-15 10:22:55,092 - INFO - QEMUController - tracing - [    0.000000] CPU: ARMv6-compatible processor [410fb022] revision 2 (ARMv7), cr=00c0387d
2021-07-15 10:22:55,093 - INFO - QEMUController - tracing - [    0.000000] CPU: PIPT / VIPT nonaliasing data cache, VIPT aliasing instruction cache
2021-07-15 10:22:55,093 - INFO - QEMUController - tracing - [    0.000000] Machine model: Akitio MyCloud mini
2021-07-15 10:22:55,093 - INFO - QEMUController - tracing - [    0.000000] Memory policy: Data cache writealloc
2021-07-15 10:22:55,096 - INFO - QEMUController - tracing - [    0.000000] DT missing boot CPU MPIDR[23:0], fall back to default cpu_logical_map
2021-07-15 10:22:55,097 - INFO - QEMUController - tracing - [    0.000000] PERCPU: Embedded 12 pages/cpu @cfde5000 s17696 r8192 d23264 u49152
2021-07-15 10:22:55,097 - INFO - QEMUController - tracing - [    0.000000] Built 1 zonelists in Zone order, mobility grouping on.  Total pages: 65024
2021-07-15 10:22:55,098 - INFO - QEMUController - tracing - [    0.000000] Kernel command line: console=ttyS0 nowatchdog nokaslr
2021-07-15 10:22:55,098 - INFO - QEMUController - tracing - [    0.000000] Bootloader command line not present
2021-07-15 10:22:55,099 - INFO - QEMUController - tracing - [    0.000000] PID hash table entries: 1024 (order: 0, 4096 bytes)
2021-07-15 10:22:55,099 - INFO - QEMUController - tracing - [    0.000000] Dentry cache hash table entries: 32768 (order: 5, 131072 bytes)
2021-07-15 10:22:55,100 - INFO - QEMUController - tracing - [    0.000000] Inode-cache hash table entries: 16384 (order: 4, 65536 bytes)
2021-07-15 10:22:55,100 - INFO - QEMUController - tracing - [    0.000000] Memory: 234084K/262144K available (3708K kernel code, 151K rwdata, 544K rodata, 6064K init, 226K bss, 28060K reserved, 0K cma-reserved)
2021-07-15 10:22:55,101 - INFO - QEMUController - tracing - [    0.000000] Virtual kernel memory layout:
2021-07-15 10:22:55,101 - INFO - QEMUController - tracing - [    0.000000]     vector  : 0xffff0000 - 0xffff1000   (   4 kB)
2021-07-15 10:22:55,102 - INFO - QEMUController - tracing - [    0.000000]     fixmap  : 0xffc00000 - 0xfff00000   (3072 kB)
2021-07-15 10:22:55,102 - INFO - QEMUController - tracing - [    0.000000]     vmalloc : 0xd0800000 - 0xff800000   ( 752 MB)
2021-07-15 10:22:55,102 - INFO - QEMUController - tracing - [    0.000000]     lowmem  : 0xc0000000 - 0xd0000000   ( 256 MB)
2021-07-15 10:22:55,103 - INFO - QEMUController - tracing - [    0.000000]     modules : 0xbf000000 - 0xc0000000   (  16 MB)
2021-07-15 10:22:55,103 - INFO - QEMUController - tracing - [    0.000000]       .text : 0xc0008000 - 0xc042f474   (4254 kB)
2021-07-15 10:22:55,103 - INFO - QEMUController - tracing - [    0.000000]       .init : 0xc0430000 - 0xc0a1c000   (6064 kB)
2021-07-15 10:22:55,104 - INFO - QEMUController - tracing - [    0.000000]       .data : 0xc0a1c000 - 0xc0a41cc8   ( 152 kB)
2021-07-15 10:22:55,104 - INFO - QEMUController - tracing - [    0.000000]        .bss : 0xc0a41cc8 - 0xc0a7a7f4   ( 227 kB)
2021-07-15 10:22:55,115 - INFO - QEMUController - tracing - [    0.000000] SLUB: HWalign=32, Order=0-3, MinObjects=0, CPUs=1, Nodes=1
2021-07-15 10:22:55,116 - INFO - QEMUController - tracing - [    0.000000] Hierarchical RCU implementation.
2021-07-15 10:22:55,116 - INFO - QEMUController - tracing - [    0.000000]      RCU restricting CPUs from NR_CPUS=2 to nr_cpu_ids=1.
2021-07-15 10:22:55,117 - INFO - QEMUController - tracing - [    0.000000] RCU: Adjusting geometry for rcu_fanout_leaf=16, nr_cpu_ids=1
2021-07-15 10:22:55,117 - INFO - QEMUController - tracing - [    0.000000] NR_IRQS:160
2021-07-15 10:22:55,118 - INFO - QEMUController - tracing - [    0.000000] clocksource: rps_clocksource_timer: mask: 0xffffff max_cycles: 0xffffff, max_idle_ns: 19112603332 ns
2021-07-15 10:22:55,118 - INFO - QEMUController - tracing - [    0.001528] sched_clock: 24 bits at 390kHz, resolution 2560ns, wraps every 21474835200ns
2021-07-15 10:22:55,119 - INFO - QEMUController - tracing - [    0.043640] Calibrating delay loop... 712.29 BogoMIPS (lpj=3561472)
2021-07-15 10:22:55,119 - INFO - QEMUController - tracing - [    0.132746] pid_max: default: 32768 minimum: 301
2021-07-15 10:22:55,120 - INFO - QEMUController - tracing - [    0.144552] Mount-cache hash table entries: 1024 (order: 0, 4096 bytes)
2021-07-15 10:22:55,120 - INFO - QEMUController - tracing - [    0.145000] Mountpoint-cache hash table entries: 1024 (order: 0, 4096 bytes)
2021-07-15 10:22:55,121 - INFO - QEMUController - tracing - [    0.238858] CPU: Testing write buffer coherency: ok
2021-07-15 10:22:55,121 - INFO - QEMUController - tracing - [    0.347013] Setting up static identity map for 0x8280 - 0x82b8
2021-07-15 10:22:55,121 - INFO - QEMUController - tracing - [    0.430709] Brought up 1 CPUs
2021-07-15 10:22:55,122 - INFO - QEMUController - tracing - [    0.432023] SMP: Total of 1 processors activated (712.29 BogoMIPS).
2021-07-15 10:22:55,122 - INFO - QEMUController - tracing - [    0.667489] clocksource: jiffies: mask: 0xffffffff max_cycles: 0xffffffff, max_idle_ns: 19112604462750000 ns
2021-07-15 10:22:55,123 - INFO - QEMUController - tracing - [    0.679070] pinctrl core: initialized pinctrl subsystem
2021-07-15 10:22:55,123 - INFO - QEMUController - tracing - [    0.828610] NET: Registered protocol family 16
2021-07-15 10:22:55,124 - INFO - QEMUController - tracing - [    0.847201] DMA: preallocated 256 KiB pool for atomic coherent allocations
2021-07-15 10:22:55,133 - INFO - QEMUController - tracing - [    0.877196] cpuidle: using governor ladder
2021-07-15 10:22:55,133 - INFO - QEMUController - tracing - [    0.878737] cpuidle: using governor menu
2021-07-15 10:22:55,133 - INFO - QEMUController - tracing - [    1.088325] gpio-oxnas 44000000.gpio: at address d0848000
2021-07-15 10:22:55,135 - INFO - QEMUController - tracing - [    1.099174] gpio-oxnas 44100000.gpio: at address d084a000
2021-07-15 10:22:55,136 - INFO - QEMUController - tracing - [    1.129218] pinctrl-oxnas pinctrl: initialized OX820 pinctrl driver
2021-07-15 10:22:55,136 - INFO - QEMUController - tracing - [    1.759641] SCSI subsystem initialized
2021-07-15 10:22:55,137 - INFO - QEMUController - tracing - [    1.773964] usbcore: registered new interface driver usbfs
2021-07-15 10:22:55,137 - INFO - QEMUController - tracing - [    1.778014] usbcore: registered new interface driver hub
2021-07-15 10:22:55,137 - INFO - QEMUController - tracing - [    1.780382] usbcore: registered new device driver usb
2021-07-15 10:22:55,138 - INFO - QEMUController - tracing - [    1.785548] pps_core: LinuxPPS API ver. 1 registered
2021-07-15 10:22:55,138 - INFO - QEMUController - tracing - [    1.785884] pps_core: Software ver. 5.3.6 - Copyright 2005-2007 Rodolfo Giometti <giometti@linux.it>
2021-07-15 10:22:55,139 - INFO - QEMUController - tracing - [    1.787171] PTP clock support registered
2021-07-15 10:22:55,139 - INFO - QEMUController - tracing - [    1.952360] clocksource: Switched to clocksource rps_clocksource_timer
2021-07-15 10:22:55,140 - INFO - QEMUController - tracing - [    2.000140] NET: Registered protocol family 2
2021-07-15 10:22:55,140 - INFO - QEMUController - tracing - [    2.047592] TCP established hash table entries: 2048 (order: 1, 8192 bytes)
2021-07-15 10:22:55,141 - INFO - QEMUController - tracing - [    2.050132] TCP bind hash table entries: 2048 (order: 2, 16384 bytes)
2021-07-15 10:22:55,141 - INFO - QEMUController - tracing - [    2.051706] TCP: Hash tables configured (established 2048 bind 2048)
2021-07-15 10:22:55,142 - INFO - QEMUController - tracing - [    2.061729] UDP hash table entries: 256 (order: 1, 8192 bytes)
2021-07-15 10:22:55,142 - INFO - QEMUController - tracing - [    2.063198] UDP-Lite hash table entries: 256 (order: 1, 8192 bytes)
2021-07-15 10:22:55,142 - INFO - QEMUController - tracing - [    2.074511] NET: Registered protocol family 1
2021-07-15 10:22:55,143 - INFO - QEMUController - tracing - [    4.281533] Unpacking initramfs...
2021-07-15 10:22:55,143 - INFO - QEMUController - tracing - [    6.319964] Freeing initrd memory: 14948K (c8000000 - c8e99000)
2021-07-15 10:22:55,144 - INFO - QEMUController - tracing - [    6.352335] futex hash table entries: 256 (order: 1, 8192 bytes)
2021-07-15 10:22:55,146 - INFO - QEMUController - tracing - [    6.357212] Crashlog allocated RAM at address 0x3f00000
2021-07-15 10:22:55,146 - INFO - QEMUController - tracing - [    6.815961] squashfs: version 4.0 (2009/01/31) Phillip Lougher
2021-07-15 10:22:55,146 - INFO - QEMUController - tracing - [    6.880227] io scheduler noop registered
2021-07-15 10:22:55,147 - INFO - QEMUController - tracing - [    6.880872] io scheduler deadline registered (default)
2021-07-15 10:22:55,147 - INFO - QEMUController - tracing - [    6.904691] Serial: 8250/16550 driver, 16 ports, IRQ sharing enabled
2021-07-15 10:22:55,148 - INFO - QEMUController - tracing - [    7.055987] console [ttyS0] disabled
2021-07-15 10:22:55,148 - INFO - QEMUController - tracing - [    7.064222] 44200000.uart: ttyS0 at MMIO 0x44200000 (irq = 6, base_baud = 390625) is a 16550A
2021-07-15 10:22:55,149 - INFO - QEMUController - tracing - [    7.196241] console [ttyS0] enabled
2021-07-15 10:22:55,204 - INFO - QEMUController - tracing - [    7.250629] nand: No NAND device found
2021-07-15 10:22:55,246 - INFO - QEMUController - tracing - [    7.293391] oxnas-gmac 40400000.ethernet: no reset control found
2021-07-15 10:22:55,248 - INFO - QEMUController - tracing - [    7.295244]  Ring mode enabled
2021-07-15 10:22:55,250 - INFO - QEMUController - tracing - [    7.296545]  No HW DMA feature register supported
2021-07-15 10:22:55,251 - INFO - QEMUController - tracing - [    7.297287]  Normal descriptors
2021-07-15 10:22:55,251 - INFO - QEMUController - tracing - [    7.298393]  Wake-Up On Lan supported
2021-07-15 10:22:58,257 - INFO - QEMUController - tracing - [   10.303966] stmmac: Cannot register as MDIO bus
2021-07-15 10:22:58,264 - INFO - QEMUController - tracing - [   10.310620] oxnas-gmac: probe of 40400000.ethernet failed with error -5
2021-07-15 10:22:58,273 - INFO - QEMUController - tracing - [   10.319654] stmmaceth 40400000.ethernet: no reset control found
2021-07-15 10:22:58,273 - INFO - QEMUController - tracing - [   10.320307]  Ring mode enabled
2021-07-15 10:22:58,275 - INFO - QEMUController - tracing - [   10.320770]  No HW DMA feature register supported
2021-07-15 10:22:58,275 - INFO - QEMUController - tracing - [   10.321848]  Normal descriptors
2021-07-15 10:22:58,275 - INFO - QEMUController - tracing - [   10.322362]  Wake-Up On Lan supported
2021-07-15 10:23:01,276 - INFO - QEMUController - tracing - [   13.322987] stmmac: Cannot register as MDIO bus
2021-07-15 10:23:01,278 - INFO - QEMUController - tracing - [   13.324858] stmmaceth: probe of 40400000.ethernet failed with error -5
2021-07-15 10:23:01,330 - INFO - QEMUController - tracing - [   13.377354] NET: Registered protocol family 10
2021-07-15 10:23:01,485 - INFO - QEMUController - tracing - [   13.532408] NET: Registered protocol family 17
2021-07-15 10:23:01,492 - INFO - QEMUController - tracing - [   13.538580] bridge: automatic filtering via arp/ip/ip6tables has been deprecated. Update your scripts to load br_netfilter if you need this.
2021-07-15 10:23:01,493 - INFO - QEMUController - tracing - [   13.539776] 8021q: 802.1Q VLAN Support v1.8
2021-07-15 10:23:01,587 - INFO - QEMUController - tracing - [   13.634219] hctosys: unable to open rtc device (rtc0)
2021-07-15 10:23:01,808 - INFO - QEMUController - tracing - [   13.854568] Freeing unused kernel memory: 6064K (c0430000 - c0a1c000)
2021-07-15 10:23:03,437 - INFO - QEMUController - tracing - [   15.483514] devpts: called with bogus options
2021-07-15 10:23:05,819 - INFO - QEMUController - tracing - Starting syslogd: OK
2021-07-15 10:23:06,578 - INFO - QEMUController - tracing - Starting klogd: OK
2021-07-15 10:23:10,049 - INFO - QEMUController - tracing - Running sysctl: OK
2021-07-15 10:23:10,641 - INFO - QEMUController - tracing - Saving random seed: [   22.688176] random: dd: uninitialized urandom read (512 bytes read, 0 bits of entropy available)
2021-07-15 10:23:10,689 - INFO - QEMUController - tracing - OK
2021-07-15 10:23:13,336 - INFO - QEMUController - tracing - Starting network: OK
2021-07-15 10:23:13,766 - INFO - QEMUController - tracing -
2021-07-15 10:23:13,766 - INFO - QEMUController - tracing -
2021-07-15 10:23:13,782 - INFO - QEMUController - tracing - Welcome to Buildroot
2021-07-15 10:23:13,797 - INFO - QEMUController - tracing -
2021-07-15 10:23:41,735 - INFO - QEMUController - tracing - buildroot login:
2021-07-15 10:23:41,736 - INFO - LoadTrace - loadtrace - loading firmguide.trace ...
2021-07-15 10:23:50,344 - INFO - LoadTrace - loadtrace - load 110599 basic blocks
2021-07-15 10:23:50,345 - INFO - CheckUserLevelF - fastuserlevel - scan user level indicators in firmguide.trace
2021-07-15 10:23:51,990 - INFO - CheckUserLevelF - fastuserlevel - have entered the user level
2021-07-15 10:23:51,991 - INFO - DeleteTrace - deltrace - remove firmguide.trace
2021-07-15 10:23:52,058 - INFO - AnalysesManager - snapshot - profile at /home/liuqiang/firmguide/.profile
```
