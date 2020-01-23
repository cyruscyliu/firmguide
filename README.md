# Salamander

[![CircleCI](https://circleci.com/gh/cyruscyliu/esv/tree/master.svg?style=svg&circle-token=7f12caaa351d02731d57d8165e634dc3e3537d33)](https://circleci.com/gh/cyruscyliu/esv/tree/master)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/a7aacb11a3b14a7d8e069d8a440a43c0)](https://www.codacy.com?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=cyruscyliu/esv&amp;utm_campaign=Badge_Grade)

Salamander is a project aiming to run and test any given firmware blob dynamically in a pure software way.

###### who will need the Salamander
+ who wants to get a shell of a linux based firmware but has no hardware emulation
+ who would like to learn how to add a new machine to QEMU but has no time to dig into QEMU
+ who would like to dynamically analysis a linux based firmware
+ who is interested re-hosting and emulation

## Dependency

```shell script
# install python 3.7
sudo apt-get install -y software-properties-common
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt-get update
sudo apt-get install -y python3.7
sudo apt-get install -y python3-pip
sudo apt-get install -y python3.7-dev
sudo -H python3.7 -m pip install --upgrade pip
sudo rm /usr/bin/python && sudo ln -s /usr/bin/python3.7 /usr/bin/python

# install required python packages
sudo -H pip3.7 install qmp pyyaml fdt fuzzywuzzy networkx pyquery prettytable capstone python-Levenshtein z3-solver
git clone https://github.com/cyruscyliu/pymake.git ~/pymake && cd ~/pymake && sudo -H pip3.7 install .
git clone https://github.com/cyruscyliu/pyqemulog ~/pyqemulog && cd ~/pyqemulog && sudo -H pip3.7 install .

# install other dependency
sudo apt-get install -y git libglib2.0-dev libfdt-dev libpixman-1-dev zlib1g-dev
sudo apt-get install -y bison flex
sudo apt-get install -y libcapstone3 libcapstone-dev
sudo apt-get install -y u-boot-tools p7zip-full squashfs-tools device-tree-compiler
sudo apt-get install -y gawk
```

#### Build Binwalk and QEMU

```shell script
# ubuntu 16.04
git clone https://github.com/cyruscyliu/esv.git salamander && cd salamander && mkdir log && mkdir ~/build

# instal binwalk
wget -nc https://github.com/ReFirmLabs/binwalk/archive/v2.1.1.tar.gz -O ~/build/v2.1.1.tar.gz || true && \
tar --skip-old-files -zxf ~/build/v2.1.1.tar.gz -C ~/build && \
cp -r patches/binwalk/* ~/build/binwalk-2.1.1/src/ && \
cd ~/build/binwalk-2.1.1 && sudo python3.7 setup.py -q install && cd ~-

# install qemu
wget -nc https://download.qemu.org/qemu-4.0.0.tar.xz -O ~/build/qemu-4.0.0.tar.xz || true && \
tar --skip-old-files -Jxf ~/build/qemu-4.0.0.tar.xz -C ~/build && \
cp -r patches/qemu/* ~/build/qemu-4.0.0/ && \
cd ~/build/qemu-4.0.0 && ./configure --target-list=arm-softmmu,mipsel-softmmu,mips-softmmu && make -j4 && cd ~-
```

##Usage

what you need to provide
+ the path to firmware [required]
+ the uuid of the firmware [required]
+ the architecture and the endian [required]
+ the brand of the firmware [required]
+ the source code to the firmware [optional]
+ the gcc used to compile the source code [optional]
+ the make details when you compiled the source code [optional]

```
./salamander.py -u 15007 -a arm -e l -b openwrt \
    -s /mnt/salamander/srcode/share/10.03-0432e31f4e2b38424921fa78247f6b27/./\
        backfire_10.03/build_dir/\
        linux-orion_generic/linux-2.6.32.10 
    -mkout /mnt/salamander/srcode/share/10.03-0432e31f4e2b38424921fa78247f6b27/./\
        backfire_10.03/build_dir/\
        linux-orion_generic/makeout.txt 
    -gcc /mnt/salamander/srcode/share/10.03-0432e31f4e2b38424921fa78247f6b27/./\
        backfire_10.03/staging_dir/toolchain-arm_v5t_gcc-4.3.3+cs_uClibc-0.9.30.1_eabi/\
        usr/bin/arm-openwrt-linux-gcc 
    -q -wd ../salamander-build \
    -f /mnt/salamander/srcode/share/10.03-0432e31f4e2b38424921fa78247f6b27/./\
        backfire_10.03/bin/orion/openwrt-wrt350nv2-squashfs-recovery.bin
```

use a shorter one to avoid such a long and annoying command

```
./salamander.py -u 15007 -wd ../salamander-build
```

use `-r` to **re-analysis**

```shell script
./salamander.py -u 15007 -wd ../salamander-build -r 
```

use `-q` to **early stop** with a profile generated

````shell script
./salamander.py -u 15007 -wd ../salamander-build -r -q
````

## Debug

statistics all

````shell script
./salamander.py -wd ../salamander-build -stat
````

diagnose trace

````shell script
./salamander.py -t path/to/uuid-arch-endian.trace
````

generate qemu code from profile

````shell script
./salamander.py -g path/to/profile.yaml -wd ../salamander-build 
````

## Analysis

If the built-in analyses can not boot the kernel to its shell, you have to add your own analysis. 
More analyses you provide, more powerful the salamander will be. The visualization results will tell you what specific 
analysis you should add. The analysis you add will solve the abelia devices a kernel required. Please read 
this [paper]() to get familiar with the abelia devices and read [this](./analyses/README.md) then to understand
how we implement the analysis framework.

## Contributors
[cyruscyliu*](https://github.com/cyruscyliu/esv), [occia*](https://github.com/occia)

## License
[MIT License](./LICENSE)
