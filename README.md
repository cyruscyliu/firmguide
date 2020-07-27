# Salamander

Salamander is a project to boot the Linux kernel in embedded firmware.
It extracts the Linux kernel from the firmware, and then boots it with a well-modeled QEMU machine.
We provide normal users with several well-modeled machines; 
for others who are familiar with the Linux hardware development, we have tutorials that you can follow to make new machines. 
Please check the table of the supported machines and our development plan.

## Installation

```shell script
git clone https://github.com/cyruscyliu/esv.git salamander && cd salamander && mkdir ~/build && ./setup.sh
```

## Usage

+ step 1, update your firmware and valid the result

```
./salamander upload -f test_firmware -del

...

2020-07-26 05:16:04,237 - INFO - LoadTrace - loadtrace - loading ~/build/test_project/test_firmware.trace ...
2020-07-26 05:16:11,265 - INFO - LoadTrace - loadtrace - load xxx basic blocks
2020-07-26 05:16:11,265 - INFO - CheckUserLevel - userlevel - scan user level indicators in ~/build/test_project/test_firmware.trace
2020-07-26 05:16:20,793 - INFO - CheckUserLevel - userlevel - have entered the user level
```

+ step 2, retrieve your commandline

```
./salamander printcmd
```

## Supported Machines

|brand|target/subtarget|OS|board|note|
|:---:|:---:|:---:|:---:|:---:|
|OpenWrt|kirkwood/generic|Linux kernel|arch/arm/mach-mvebu|done|
|OpenWrt|bcm53xx/generic|Linux kernel|arch/arm/mach-bcm|done|
|OpenWrt|ramips/rt305x|Linux kernel|arch/mips/ralink|done|
|OpenWrt|ath79/generic|Linux kernel|arch/mips/ath79|done|
|OpenWrt|oxnas/generic|Linux kernel|arch/arm/mach-oxnas|done|

## Contributors
[cyruscyliu*](https://github.com/cyruscyliu/esv), [occia*](https://github.com/occia)

## License
[MIT License](./LICENSE)
