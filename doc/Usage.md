# Usage Scenarios of FirmGuide

FirmGuide has many usage scenarios.
+ Virtual Device Model Design
+ Type-II Driver Fuzzing (WIP)
+ Type-II Driver Vulnerability Analysis (WIP)

## Virtual Device Model Design

1. Prepare a uImage and a device tree blob.

```sh
make menuconfig
make zImage uImage modules dtbs
```

2. Check device tree entries and resolve warnings.

```sh
./firmguide dtcoverup -dtb path/to/dtb
```

3. Update peripheral database and resolve warnings.

```sh
./firmguide newhwdt -dtb path/to/dtb
```

4. Update existing peripheral model in QEMU and resolve warnings.


5. Synthesize QEMU virtual machine and resolve warnings.

```sh
./firmgduie 
```

## Common Warnings

```
>>>> ERROR <<<< update COMPATIBLE_INTERRUPTS_INDEX for ['brcm,bcm2836-l1-intc']
2021-04-11 15:39:22,418 - WARNING - SynthesisDT - synthesisdt - error in parsing, missing 'cpu_get_type'
2021-04-09 13:11:59,356 - WARNING - UpdateHardwareDT - scanhwdt - cannot find serial of bcm2709-rpi-2-b.dtb
```

