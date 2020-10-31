# FirmGuide

FirmGuide is a project aiming to boost the capability of dynamic analysis
of the Linux kernel for embedded system in virtual execution environment.
In the virtual execution environment, you can debug, trace, and test
the Linux kernel to collect runtime information that can be used to
understand vulnerabilities, PoCs, root causes of crashes happend in the Linux kernel.
FirmGuide is a effectively complementary dynamic analysis platform to Firmadyne
that focus on user space programs.

What FirmGuide does is, which is quite easy to understand, to generate a QEMU virtual machine.
The QEMU virtual machine is generated automatically according to a list of hardware
and their topology described in the device tree blob packed together with the Linux kernel image.
Then the Linux kernel could be booted with the generated QEMU virutal machine.
We provide you several subcommands to do so.
Any further dynamic analysis then can be performed by modifying QEMU or
putting a driver in a rootfs file (qemu-system-arm ... -initrd path/to/rootfs).

### Install

```bash
git clone xxx
cd firmguide && make
```

## Usage

FirmGuide is a command-oriented tool like `git`.
Please look at [Subcommand](doc/Subcommand.md) for more information.

### Scenario 1: Convert a device tree blob to a QEMU virtual machine.


```bash
root@esv:~/firmguide# ./firmguide synthesize -dtb examples/plxtech_nas782x.dtb
```

### Scenario 2: Upload a firmware image and boot it.

```bash
root@esv:~/firmguide# ./firmguide upload -f examples/62771d14b82e554a95d048af99866c404acb196f.bin
```

### Scenario 3: Manual analysis to support new peripherals.

Please check [Overview](doc/TemplateAndParameters.md#overview) and
[Manual Analysis](doc/TemplateAndParameters.md#manual-analysis) for more information.

### Scenario 4: Automatic analysis to support new peripherals.

WIP

## SoC Support List

WIP

## Case Study for Dynamic Analysis

WIP

## License
[MIT License](./LICENSE)
