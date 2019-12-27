# Salamander

[![CircleCI](https://circleci.com/gh/cyruscyliu/esv/tree/master.svg?style=svg&circle-token=7f12caaa351d02731d57d8165e634dc3e3537d33)](https://circleci.com/gh/cyruscyliu/esv/tree/master)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/a7aacb11a3b14a7d8e069d8a440a43c0)](https://www.codacy.com?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=cyruscyliu/esv&amp;utm_campaign=Badge_Grade)

Salamander is a project aiming to run and test any given firmware blob dynamically in a pure software way.

###### features
Currently, we provide a modular framework to analysis a firmware under the guide of its source code. We 
will generate a new machine for QEMU, and you can play with this new machine for fun! By adding more analysis
we will get more code coverage and achieve more goals. The goal just now is to run a linux based firmware
entering the user mode and getting the shell. Let's start and enjoy our trip.

###### who will need the Salamander
+ who want to get a shell of a linux based firmware but has no hardware emulation
+ who would like to learn how to add a new machine to QEMU but has no time to dig into the QEMU
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
git clone git@github.com:cyruscyliu/pymake.git ~/pymake && cd ~/pymake && sudo -H pip3.7 install .
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

Before using salamander, you must prepare your firmware and provide information listed below.
+ the path to firmware [required]
+ the uuid of the firmware [required]
+ the architecture and the endian [required]
+ the brand of the firmware [required]
+ the source code to the firmware [optional]

To test your firmware, simply run your command as shown in the example. And the first run may be slow.

```shell script
./salamander.py -f tests/files/2b38a3.bin -u 13882 -a arm -e l -b openwrt -wd ../salamander-build
./salamander.py -f tests/files/ec5859.bin -u 15007 -a arm -e l -b openwrt -wd ../salamander-build
./salamander.py -f tests/files/9874f6.bin -u 14292 -a mips -e l -b openwrt -wd ../salamander-build
```

#### Re-Analysis

Sometimes we would like to re-analysis the whole firmware. The solution is using `-r` in your command line.

```shell script
./salamander.py -u 13882 -wd ../salamander-build -r
./salamander.py -u 15007 -wd ../salamander-build -r 
./salamander.py -u 14292 -wd ../salamander-build -r
```

#### Device Profile

Sometimes we just want to get the device profile not to diagnose whether we boot the firmware up or not.
The solution is using `-q` in your command line.

````shell script
# for the first time
./salamander.py -f tests/files/2b38a3.bin -u 13882 -a arm -e l -b openwrt -wd ../salamander-build -q
# later use a shorter command
./salamander.py -u 13882 -wd ../salamander-build -q
````

And, in other situation, if we already have the device profile, we want to generation QEMU code directly.
BTW, the architecture information is still necessary. Still, the first run may be slow.

```shell script
./salamander.py -g tests/files/2b38a3.yaml -wd ../salamander-build/
./salamander.py -g tests/files/ec5859.yaml -wd ../salamander-build/
./salamander.py -g tests/files/9874f6.yaml -wd ../salamander-build/
```

#### Diagnosis

Sometimes we just want to check our trace offline to gain more insights.

```shell script
 ./salamander.py -t log/13882.trace
 ./salamander.py -t log/15007.trace
 ./salamander.py -t log/14292.trace # mips not be supported well
```

### Visualization

After running, it is better to have a page to show the analysis results rather than checking massive logs. Simply run
`python dashboard/__init__.py` and follow its instructions you will see the statistics of your analysis in your browser.

![dashboard](./dashboard/dashboard.png)

### Add an analysis

If the built-in analyses can not boot the kernel to its shell, you have to add your own analysis. 
More analyses you provide, more powerful the salamander will be. The visualization results will tell you what specific 
analysis you should add. The analysis you add will solve the abelia devices a kernel required. Please read 
this [paper]() to get familiar with the abelia devices and read [this](./analyses/README.md) then to understand
how we implement the analysis framework.

### Contributors
[cyruscyliu*](https://github.com/cyruscyliu/esv), [occia*](https://github.com/occia)

### License
[MIT License](./LICENSE)
