# FirmGuide

FirmGuide is a project aiming to boost the capability of dynamic analysis
of the Linux kernel for embedded system in virtual execution environment.
In the virtual execution environment, you can debug, trace, and test
the Linux kernel to collect runtime information that can be used to
understand vulnerabilities, PoCs, root causes of crashes happend in the Linux kernel.
FirmGuide is a effectively complementary dynamic analysis platform to Firmadyne
that focuses on user space programs - FirmGuide focuses on the Linux kernel.

To support the Linux kernel, FirmGuide generates a QEMU virtual machine for it,
which is quite easy to understand,
a QEMU virtual machine meaning a full control of the Linux kernel.
The QEMU virtual machine is generated automatically according to a list of hardware
and their topology described in the device tree blob packed together with the Linux kernel image.
Then the Linux kernel could be booted with the generated QEMU virutal machine.
Any further dynamic analysis then can be performed by modifying QEMU or
putting a driver in a rootfs file (qemu-system-arm ... -initrd path/to/rootfs).

### Install

```bash
git clone xxx
cd firmguide && make
```

## Usage

> FirmGuide is a command-oriented tool like `git`.
Please look at [Subcommand](doc/Subcommand.md) for more information.

Upload a firmware image and boot it.

```bash
root@esv:~/firmguide# ./firmguide upload -f examples/62771d14b82e554a95d048af99866c404acb196f.bin
```

If the `upload` is failed, you may take one or several following steps.

+ There is no device tree avaiable.
> If you have another firmware image with device tree, use it.
Othersize, the firmware image cannot be supported.

+ There is one or two peripherals unsupported, and the synthesis of QEMU virtual machine is failed.
> Please report it, or you can manually support the peripherals.
Please check [Advanced Development](#advanced-development).

+ Any other troubles should be caused by bugs in FirmGuide.
> Please report them to us.

## Advanced Development

+ [Manual analysis to support new peripherals](#)
+ [Automatic analysis to support new peripherals](#)
+ [FirmGuide internals and development](#doc/Development.md)

## SoC Support List

WIP

## Case Study for Dynamic Analysis

WIP

## License
[MIT License](./LICENSE)
