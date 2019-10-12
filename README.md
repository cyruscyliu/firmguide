# Salamander

This is a project aiming to run and test any given firmware blob dynamically in a pure software way.
That is to say, the given firmware becomes a traditional program that can be run smoothly
and instrumented easily. Moreover, any dynamic analysis approaches can be extended and there is no gap at all.

BTW, this project has a name `Salamander` which is from `Fantastic Beasts: The Crimes of Grindelwald` :).

>Newt (to Tian): You have eyes like a salamander

## Features

We are very happy to release the `Salamander 0.5` with following features:
+ support thousands of linux-based firmware among several brands
+ [SPECIAL] provide lots of summary to embedded system fragmentation
+ build-in dozens of metadata extractors and a static analysis tool
+ [SPECIAL] a light and effective static analysis tool for hardware things in linux kernel
+ support 3 device profiles, device tree, ipxact, and a custom simple protocol
+ [SPECIAL] extend device tree to support virtualization
+ generate QEMU code with device profiles as input
+ [SPECAIL] interface messy QEMU code to developer, and redefine the way to write a new machine
+ build-in a dynamic engine to track and solve peripheral register initial values
+ [SPECIAL] guarantee several peripheral' functionality

## Quick Start

This section is not QUICK at all, make sure to follow us.
 
### dependency

```bash
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt-get update
sudo apt-get install -y python3.7
sudo -H python3.7 -m pip install --upgrade pip
sudo -H pip3.7 install -r requirements.txt
sudo apt-get install -y git libglib2.0-dev libfdt-dev libpixman-1-dev zlib1g-dev
sudo apt-get install -y git-email
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

### install
```bash
make
```

## start
```bash
python3.7 main.py -dbt text -wd ./build
```
