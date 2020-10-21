# FirmGuide

FirmGuide is a project aiming to boost the capability of dynamic analysis
of the Linux kernel in embedded firmware. It basically converts a device tree
to a QEMU virtual machine by a new technique named `model-guided kernel execution.
Each QEMU virtual machine is composed of many peripheral models that
can be automatically or manually (complementary method) generated.


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
