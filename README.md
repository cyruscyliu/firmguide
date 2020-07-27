# Salamander

Salamander is a project to boot the Linux kernel in embedded firmware.
It extracts the Linux kernel from the firmware, and then boots it with a well-modeled QEMU machine.
We provide normal users with several well-modeled machines.
For others who are familiar with the Linux hardware development, we have tutorials that you can follow to make new well-modeled machines.

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

## Contributors
[cyruscyliu*](https://github.com/cyruscyliu/esv), [occia*](https://github.com/occia)

## License
[MIT License](./LICENSE)
