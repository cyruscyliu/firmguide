# FirmGuide

FirmGuide can help you to develop a QEMU virtual machine for a Linux-based
embedded system, especially boosting the capability of dynamic analysis of the
corresponding Linux kernel. In the emulator, you can debug, trace, and test the
Linux kernel to collect runtime information that can be used to understand
vulnerabilities, PoCs, root causes of crashes in the Linux kernel. FirmGuide is
an effectively complementary to Firmadyne that focuses on user space programs -
FirmGuide focuses on the Linux kernel. More details are in our
[paper](https://cyruscyliu.github.io/papers/firmguide-ase21.pdf).

## Plan

[ ] Upgrade QEMU 4.0.0 to the latest QEMU

## Install

``` bash
sudo make; sudo make qemu sparse
```

## Usage

Convert a device tree file to a QEMU virtual machine.

``` bash
./firmguide synthesize -dtb examples/plxtech_nas782x.dtb
```

Load a firmware image.

``` bash
./firmguide upload -f examples/62771d14b82e554a95d048af99866c404acb196f.bin
```

Please look at [Subcommand](doc/Subcommands.md) for more information.

## Authors

[Qiang Liu](https://github.com/cyruscyliu), and [Cen Zhang](https://github.com/occia)

## Contact

If you have any problems, please fire issues!
