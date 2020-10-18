# FirmGuide

FirmGuide is a project aiming to boost the capability of dynamic analysis
of the Linux kernel in embedded firmware. It basically converts a device tree
to a QEMU virtual machine by a new technique named `model-guided kernel execution.
Each QEMU virtual machine is composed of many peripheral models that
can be automatically or manually (complementary method) generated.

## Usage

FirmGuide is a command-oriented tool like `git`.
It has three modes for different scenarios.

### Install

```bash
git clone xxx
cd firmguide && make
```

### Scenario 1: Boot Linux-based firmware for further dynamic analysis.

Suppose there is a firmware image that has a Linux kernel with device tree,
just upload this firmware with the load address of the Linux kernel
(0x00008000 for ARM by default).

```bash
./firmware -ld 0x00008000 upload -f path/to/firmware
```
## License
[MIT License](./LICENSE)
