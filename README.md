# Salamander

[![CircleCI](https://circleci.com/gh/cyruscyliu/esv/tree/master.svg?style=svg&circle-token=7f12caaa351d02731d57d8165e634dc3e3537d33)](https://circleci.com/gh/cyruscyliu/esv/tree/master)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/a7aacb11a3b14a7d8e069d8a440a43c0)](https://www.codacy.com?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=cyruscyliu/esv&amp;utm_campaign=Badge_Grade)

Salamander is a project aiming to run and test any given firmware blob dynamically in a pure software way.

###### features
Currently, we provide a modular framework to analysis a firmware under the guide of its source code. We 
will generate a new machine for QEMU. By adding more analysis
we will get more code coverage and achieve more goals. The goal just now is to run a linux based firmware
entering the user mode and getting the shell. Let's start and enjoy our trip.

###### who will need the Salamander
+ who want to get a shell of a linux based firmware but has no hardware emulation
+ who would like to learn how to add a new machine to QEMU but has no time to dig into QEMU
+ who would like to dynamically analysis a linux based firmware
+ who are interested re-hosting and emulation

### Install

First, clone the repo.

```shell script
git clone git@github.com:cyruscyliu/esv.git salamander && cd salamander
```

#### Docker Image

We recommend you using our docker image.

```shell script
docker build -t cyruscyliu/cci-salamander-docker-primary:latest .
docker run -it -v $PWD:/root cyruscyliu/cci-salamander-docker-primary:latest /bin/bash
```

#### ~~Manually Installation~~

It might be a long time to build Salamander, and see the instructions below.

###### install python 3.7

```shell script
sudo apt-get install -y software-properties-common
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt-get update
sudo apt-get install -y python3.7
sudo apt-get install -y python3-pip
sudo -H python3.7 -m pip install --upgrade pip
sudo rm /usr/bin/python && sudo ln -s /usr/bin/python3.7 /usr/bin/python
```

###### install required python packages

```shell script
sudo -H pip3.7 install qmp pyyaml fdt fuzzywuzzy networkx pyquery prettytable
git clone https://github.com/cyruscyliu/pymake.git ~/pymake && cd ~/pymake && sudo -H pip3.7 install .
git clone https://github.com/cyruscyliu/pyqemulog ~/pyqemulog && cd ~/pyqemulog && sudo -H pip3.7 install .
```

###### install other dependency

```shell script
sudo apt-get install -y git libglib2.0-dev libfdt-dev libpixman-1-dev zlib1g-dev
sudo apt-get install -y libaio-dev libbluetooth-dev libbrlapi-dev libbz2-dev
sudo apt-get install -y libcap-dev libcap-ng-dev libcurl4-gnutls-dev libgtk-3-dev
sudo apt-get install -y libibverbs-dev libjpeg8-dev libncurses5-dev libnuma-dev
sudo apt-get install -y librbd-dev librdmacm-dev
sudo apt-get install -y libsasl2-dev libsdl1.2-dev libseccomp-dev libsnappy-dev libssh2-1-dev
sudo apt-get install -y valgrind xfslibs-dev
sudo apt-get install -y libnfs-dev libiscsi-dev
sudo apt-get install -y bison flex
sudo apt-get install -y libcapstone3 libcapstone-dev
sudo apt-get install -y u-boot-tools
sudo apt-get install -y gawk
```

#### Build Binwalk and QEMU

```shell script
sudo make clean && make
```

### Usage

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

use a shorter one to avoid an annoying such long command

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

### Contributors
[cyruscyliu*](https://github.com/cyruscyliu/esv), [occia*](https://github.com/occia)

### License
[MIT License](./LICENSE)
