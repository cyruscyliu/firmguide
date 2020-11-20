# FirmGuide

FirmGuide is a project aiming to boost the capability of dynamic analysis
of the Linux kernel for embedded system in virtual execution environment.
In the virtual execution environment, you can debug, trace, and test
the Linux kernel to collect runtime information that can be used to
understand vulnerabilities, PoCs, root causes of crashes happend in the Linux kernel.
FirmGuide is an effectively complementary dynamic analysis platform to Firmadyne
that focuses on user space programs - FirmGuide focuses on the Linux kernel.

To support the Linux kernel, FirmGuide generates a QEMU virtual machine for it,
which is quite easy to understand, to fully control of the Linux kernel.
The QEMU virtual machine is generated automatically according to the list of hardware
described in the device tree blob packed together with the Linux kernel image.
FirmGuide searches the implementation of each hardware in a database,
composites all the implementation together to be compiled with QEMU source tree.

Yes, you are supposed to provide the specific implementation of hardware in the database.
There are many ways to achicve that.
First, you can read datasheet and implement all functionality of that hardware.
Second, you can follow our paper where we provide several brand new insights to develop virtual hardware.
However, it is still an open research question to virtualize hardware in an automatical and scalable way.
Hope you can find a better solution!

## Install

```bash
git clone xxx; cd firmguide; make
```

## Usage

> FirmGuide is a command-oriented tool like `git`.
Please look at [Subcommand](doc/Subcommand.md) for more information.

The basic unit of FirmGuide is to convert a device tree file to a QEMU virtual machine.
`synthesize` will generate and compile the QEMU virtual machine automatically.

``` txt 
root@esv:~/firmguide# ./firmguide synthesize -dtb examples/plxtech_nas782x.dtb
```

## Virtual hardware development

To develop a virtual hardware, 
you are supposed to be familiar with the code structure of QEMU virtual hardware.
Having learned that,
you can read the datasheet of that hardware if any to start your coding.
You can also follow our paper to manually or automatically analyze
Linux kernel source code to implement an interrupt controller, a timer,
which is enough for the Linux kernel to finish its startup process.

If to follow our paper, please read
[FirmGuide rendering system](doc/Rendering.md),
[Manual FirmGuide offline](doc/Manual-FirmGuide-offline.md),
and [Automatic FirmGuide offline](doc/Automatic-FirmGuide-offline.md), respectively,
and have a try!

## Advanced topics

[FirmGuide internals and development](doc/Development.md)

## License
[MIT License](./LICENSE)