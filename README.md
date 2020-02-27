# Salamander

[![CircleCI](https://circleci.com/gh/cyruscyliu/esv/tree/master.svg?style=svg&circle-token=7f12caaa351d02731d57d8165e634dc3e3537d33)](https://circleci.com/gh/cyruscyliu/esv/tree/master)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/a7aacb11a3b14a7d8e069d8a440a43c0)](https://www.codacy.com?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=cyruscyliu/esv&amp;utm_campaign=Badge_Grade)

Salamander is a project aiming to boot any Linux-based firmware blob in a pure software way.

#### who will need the Salamander
+ who want to run a Linux based firmware not supported officially
+ who would like to dynamically analyze a Linux based firmware

#### support list
+ arm/mach-orion5x
+ arm/mach-oxnas
+ mips/bcm47xx
+ mips/ath79

## Usage

##### if you have a firmware blob
+ the path to the firmware [required]
+ the uuid of the firmware [required]
+ the architecture and the endianness [required]
+ the brand of the firmware [optional]
+ the download url [optional]

```
cd ~/salamander
./bin.py -f /root/images/ec5859077831e078987ebb05461d4ec834896f3e.bin -u 15007 -a arm -e l -b openwrt -l http://archive.openwrt.org/backfire/10.03/orion/openwrt-wrt350nv2-squashfs-recovery.bin
```

##### if you have compilable Linux kernel source code
+ the uuid of the board
+ the path to source code [required]
+ the prefix of the toolchain used to compile the source code [required]
+ the architecture and the endianness [optional]
+ the make details when you compiled the source code [optional]
+ the brand of the firmware [optional]

```
./src.py -u oxnas_generic -a arm -e l -b openwrt -s /mnt/iscsi/openwrt-build-docker/share/15.05-bfae3162fb949c343763ad9ea7ab3fe0/./chaos_calmer-15.05/build_dir/target-arm_mpcore_uClibc-0.9.33.2_eabi/linux-oxnas/linux-3.18.20 -mkout /mnt/iscsi/openwrt-build-docker/share/15.05-bfae3162fb949c343763ad9ea7ab3fe0/./chaos_calmer-15.05/build_dir/target-arm_mpcore_uClibc-0.9.33.2_eabi/OpenWrt-ImageBuilder-15.05-oxnas.Linux-x86_64/build_dir/target-arm_mpcore_uClibc-0.9.33.2_eabi/linux-oxnas/makeout.txt -gcc /mnt/iscsi/openwrt-build-docker/share/15.05-bfae3162fb949c343763ad9ea7ab3fe0/./chaos_calmer-15.05/build_dir/target-arm_mpcore_uClibc-0.9.33.2_eabi/OpenWrt-SDK-15.05-oxnas_gcc-4.8-linaro_uClibc-0.9.33.2_eabi.Linux-x86_64/staging_dir/toolchain-arm_mpcore_gcc-4.8-linaro_uClibc-0.9.33.2_eabi/bin/arm-openwrt-linux- -f /mnt/iscsi/openwrt-build-docker/share/15.05-bfae3162fb949c343763ad9ea7ab3fe0/./chaos_calmer-15.05/bin/oxnas/openwrt-15.05-oxnas-kd20-u-boot-initramfs.bin
```
## Install

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
sudo -H pip3.7 install qmp pyyaml fdt fuzzywuzzy networkx pyquery prettytable capstone python-Levenshtein z3-solver pydot pyelftools
git clone https://github.com/cyruscyliu/pymake.git ~/pymake && cd ~/pymake && sudo -H pip3.7 install .
git clone https://github.com/cyruscyliu/pyqemulog ~/pyqemulog && cd ~/pyqemulog && sudo -H pip3.7 install .

# install other dependency
sudo apt-get install -y git libglib2.0-dev libfdt-dev libpixman-1-dev zlib1g-dev
sudo apt-get install -y bison flex
sudo apt-get install -y libcapstone3 libcapstone-dev
sudo apt-get install -y u-boot-tools p7zip-full squashfs-tools device-tree-compiler
sudo apt-get install -y gawk

# install salamander 
git clone https://github.com/cyruscyliu/esv.git salamander && cd salamander && mkdir log && mkdir ~/build

# install modified binwalk
sudo apt-get install -y zlib1g-dev liblzma-dev liblzo2-dev && \
git clone https://github.com/devttys0/sasquatch ~/sasquatch && \
cd ~/sasquatch && ./build.sh && cd ~-

wget -nc https://github.com/ReFirmLabs/binwalk/archive/v2.1.1.tar.gz -O ~/build/v2.1.1.tar.gz || true && \
tar --skip-old-files -zxf ~/build/v2.1.1.tar.gz -C ~/build && \
cp -r patches/binwalk/* ~/build/binwalk-2.1.1/src/ && \
cd ~/build/binwalk-2.1.1 && sudo python3.7 setup.py -q install && cd ~-
# cd ~/build/binwalk-2.1.1 && sudo ./deps.sh && cd ~- && \

# install modified qemu
wget -nc https://download.qemu.org/qemu-4.0.0.tar.xz -O ~/build/qemu-4.0.0.tar.xz || true && \
tar --skip-old-files -Jxf ~/build/qemu-4.0.0.tar.xz -C ~/build && \
cp -r patches/qemu/* ~/build/qemu-4.0.0/ && \
cd ~/build/qemu-4.0.0 && ./configure --target-list=arm-softmmu,mipsel-softmmu,mips-softmmu && make -j4 && cd ~-

# install llvm-9
apt-get update && apt-get install -y build-essential wget lsb-core software-properties-common vim && \
wget https://apt.llvm.org/llvm.sh && chmod +x llvm.sh && ./llvm.sh 9 && \
ln -s /usr/bin/clang-9 /usr/bin/clang && ln -s /usr/bin/llvm-link-9 /usr/bin/llvm-link  && ln -s /usr/bin/opt-9 /usr/bin/opt
pip3.7 install networkx matplotlib graphviz

# install sparse
git clone git://git.kernel.org/pub/scm/devel/sparse/sparse.git ~/sparse && \
cd ~/sparse && make && sudo cp ./graph /usr/bin && cd ~-
```

## Contributors
[cyruscyliu*](https://github.com/cyruscyliu/esv), [occia*](https://github.com/occia)

## License
[MIT License](./LICENSE)

