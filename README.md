# FirmGuide

FirmGuide is a set of tools
that help you to quickly develop an embedded QEMU emulator or virtual machine
for a Linux-based embedded system,
especially boosting the capability of dynamic analysis of the corresponding Linux kernel.

In the emulator, you can debug, trace, and test
the Linux kernel to collect runtime information that can be used to
understand vulnerabilities, PoCs, root causes of crashes in the Linux kernel.
FirmGuide is an effectively complementary to Firmadyne
that focuses on user space programs - FirmGuide focuses on the Linux kernel.

The emulator can be automatically generated according to the list of hardware
described in the device tree blob packed together with the Linux kernel image.
FirmGuide searches the implementation of each hardware in a database,
composites all the implementation together to be compiled with QEMU source tree.
FirmGuide cannot handle the images without device tree blobs.

In theory, each part of the emulator, that is, the implementation of each hardware,
is supposed to be provided manually and precisely. However, FirmGuide tells us
only the interrupt controller, the timer and the serial are necessary
to boot a Linux kernel and to spawn a shell finally.
Focus on the three hardware and FirmGuide will handle all other hardware for you.

We have three policies to deal with each of the three necessary hardware.
1. If QEMU has supported that hardware, use it.
2. If not, you can follow our paper to automatically generate what FirmGuide needs.
3. Otherwise, you can read its datasheet and seed a patch to QEMU, then going back to policy 1.

## Install

``` bash
git clone xxx --depth=1; cd firmguide; make; make qemu sparse
```

If you just use [Tools](#Tools) of FirmGuide, please just `make`. There is no
need to install `qemu` and `sparse`.

## Usage

> FirmGuide is a command-oriented tool like `git`.
Please look at [Subcommand](doc/Subcommand.md) for more information.

The basic of FirmGuide is to convert a device tree file to a QEMU virtual
machine.

``` bash
./firmguide synthesize -dtb examples/plxtech_nas782x.dtb
```

Upon `synthesize`, you can upload a firmware image then. For mips, you are
supposed to provide `-e` and `-ld` (`./firmguide loaddr`) as well.

``` bash
./firmguide upload -f /path/to/a/firmware/image
```

## Tools

Given the source of Linux kernel with a makeout.txt (`make -Bnk`) in the same
directory, you can generate the preprocessed file (.i) of an file that contains
a specific function. Please assign the cross compiler at the same time.

``` bash
./firmguide analysrc -s /path/to/source -cc /path/to/cross_compile_prefix -e start_kernel
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
