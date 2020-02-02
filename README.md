# Salamander

[![CircleCI](https://circleci.com/gh/cyruscyliu/esv/tree/master.svg?style=svg&circle-token=7f12caaa351d02731d57d8165e634dc3e3537d33)](https://circleci.com/gh/cyruscyliu/esv/tree/master)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/a7aacb11a3b14a7d8e069d8a440a43c0)](https://www.codacy.com?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=cyruscyliu/esv&amp;utm_campaign=Badge_Grade)

Salamander is a project aiming to run and test any given firmware blob dynamically in a pure software way.

###### who will need the Salamander
+ who want to run a Linux based firmware not supported officially
+ who would like to dynamically analyze a Linux based firmware

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
sudo -H pip3.7 install qmp pyyaml fdt fuzzywuzzy networkx pyquery prettytable capstone python-Levenshtein z3-solver
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
```

## Usage

##### if you have a firmware blob
+ the path to firmware [required]
+ the uuid of the firmware [required]
+ the architecture and the endianness [required]
+ the brand of the firmware [optional]
+ the url where your download it [optional]

```
cd ~/salamander
./slbin.py -u 15007 -a arm -e l -f ../images/openwrt-wrt350nv2-squashfs-recovery.bin
```

##### if you have compilable Linux kernel source code
+ the uuid of the board
+ the path to source code [required]
+ the prefix of the toolchain used to compile the source code [required]
+ the architecture and the endianness [optional]
+ the make details when you compiled the source code [optional]
+ the brand of the firmware [optional]

```
./slsrc.py -u bcm47xx -a mips -e l -b openwrt -s /root/openwrt-build-docker/share/15.05-aef2aee99101287d643ad0dee7fb58fb/./chaos_calmer-15.05/build_dir/target-mipsel_mips32_uClibc-0.9.33.2/linux-brcm47xx_legacy/linux-3.18.20 -mkout /root/openwrt-build-docker/share/15.05-aef2aee99101287d643ad0dee7fb58fb/./chaos_calmer-15.05/build_dir/target-mipsel_mips32_uClibc-0.9.33.2/OpenWrt-ImageBuilder-15.05-brcm47xx-legacy.Linux-x86_64/build_dir/target-mipsel_mips32_uClibc-0.9.33.2/linux-brcm47xx_legacy/makeout.txt -gcc /root/openwrt-build-docker/share/15.05-aef2aee99101287d643ad0dee7fb58fb/./chaos_calmer-15.05/build_dir/target-mipsel_mips32_uClibc-0.9.33.2/OpenWrt-SDK-15.05-brcm47xx-legacy_gcc-4.8-linaro_uClibc-0.9.33.2.Linux-x86_64/staging_dir/toolchain-mipsel_mips32_gcc-4.8-linaro_uClibc-0.9.33.2/bin/mipsel-openwrt-linux-
./slsrc.py -u ar71xx -a mips -e l -b openwrt -s /root/openwrt-build-docker/share/15.05-cc3a47a374475253f93a08eea6eaadce/./chaos_calmer-15.05/build_dir/target-mips_34kc_uClibc-0.9.33.2/linux-ar71xx_generic/linux-3.18.20 -mkout /root/openwrt-build-docker/share/15.05-cc3a47a374475253f93a08eea6eaadce/./chaos_calmer-15.05/build_dir/target-mips_34kc_uClibc-0.9.33.2/linux-ar71xx_generic/makeout.txt -gcc /root/openwrt-build-docker/share/15.05-cc3a47a374475253f93a08eea6eaadce/./chaos_calmer-15.05/build_dir/target-mips_34kc_uClibc-0.9.33.2/OpenWrt-SDK-15.05-ar71xx-generic_gcc-4.8-linaro_uClibc-0.9.33.2.Linux-x86_64/staging_dir/toolchain-mips_34kc_gcc-4.8-linaro_uClibc-0.9.33.2/bin/mips-openwrt-linux-
./slsrc.py -u adm5120 -a mips -e l -b openwrt -s /root/openwrt-build-docker/share/15.05-169f8131948e735fd3f6b6a9697d8447/./chaos_calmer-15.05/build_dir/target-mipsel_mips32_uClibc-0.9.33.2/linux-adm5120_rb1xx/linux-3.18.20 -mkout /root/openwrt-build-docker/share/15.05-169f8131948e735fd3f6b6a9697d8447/./chaos_calmer-15.05/build_dir/target-mipsel_mips32_uClibc-0.9.33.2/OpenWrt-ImageBuilder-15.05-adm5120-rb1xx.Linux-x86_64/build_dir/target-mipsel_mips32_uClibc-0.9.33.2/linux-adm5120_rb1xx/makeout.txt -gcc /root/openwrt-build-docker/share/15.05-169f8131948e735fd3f6b6a9697d8447/./chaos_calmer-15.05/build_dir/target-mipsel_mips32_uClibc-0.9.33.2/OpenWrt-SDK-15.05-adm5120-rb1xx_gcc-4.8-linaro_uClibc-0.9.33.2.Linux-x86_64/staging_dir/toolchain-mipsel_mips32_gcc-4.8-linaro_uClibc-0.9.33.2/bin/mipsel-openwrt-linux-
./slsrc.py -u ar231x -a mips -e b -b openwrt -s /root/openwrt-build-docker/share/12.09-2969d81970c0b32c9894903ec3f82900/./archive-12.09/build_dir/linux-atheros/linux-3.3.8 -mkout /root/openwrt-build-docker/share/12.09-2969d81970c0b32c9894903ec3f82900/./archive-12.09/build_dir/target-mips_uClibc-0.9.33.2/OpenWrt-ImageBuilder-atheros-for-linux-x86_64/build_dir/linux-atheros/makeout.txt -gcc /root/openwrt-build-docker/share/12.09-2969d81970c0b32c9894903ec3f82900/./archive-12.09/build_dir/target-mips_uClibc-0.9.33.2/OpenWrt-Toolchain-atheros-for-mips-gcc-4.6-linaro_uClibc-0.9.33.2/toolchain-mips_gcc-4.6-linaro_uClibc-0.9.33.2/bin/mips-openwrt-linux-
./slsrc.py -u ralink -a mips -e l -b openwrt -s /root/openwrt-build-docker/share/15.05-02cb6b676c588f7e428c253b747d1ebb/./chaos_calmer-15.05/build_dir/target-mipsel_74kc+dsp2_uClibc-0.9.33.2/linux-ramips_rt3883/linux-3.18.20 -mkout /root/openwrt-build-docker/share/15.05-02cb6b676c588f7e428c253b747d1ebb/./chaos_calmer-15.05/build_dir/target-mipsel_74kc+dsp2_uClibc-0.9.33.2/OpenWrt-ImageBuilder-15.05-ramips-rt3883.Linux-x86_64/build_dir/target-mipsel_74kc+dsp2_uClibc-0.9.33.2/linux-ramips_rt3883/makeout.txt -gcc /root/openwrt-build-docker/share/15.05-02cb6b676c588f7e428c253b747d1ebb/./chaos_calmer-15.05/build_dir/target-mipsel_74kc+dsp2_uClibc-0.9.33.2/OpenWrt-SDK-15.05-ramips-rt3883_gcc-4.8-linaro_uClibc-0.9.33.2.Linux-x86_64/staging_dir/toolchain-mipsel_74kc+dsp2_gcc-4.8-linaro_uClibc-0.9.33.2/bin/mipsel-openwrt-linux-
./slsrc.py -u ar7 -a mips -e l -b openwrt -s /root/openwrt-build-docker/share/15.05-0b231aa8e236684985f52cbf79dc418e/./chaos_calmer-15.05/build_dir/target-mipsel_mips32_uClibc-0.9.33.2/linux-ar7_generic/linux-3.18.20 -mkout /root/openwrt-build-docker/share/15.05-0b231aa8e236684985f52cbf79dc418e/./chaos_calmer-15.05/build_dir/target-mipsel_mips32_uClibc-0.9.33.2/OpenWrt-ImageBuilder-15.05-ar7-generic.Linux-x86_64/build_dir/target-mipsel_mips32_uClibc-0.9.33.2/linux-ar7_generic/makeout.txt -gcc /root/openwrt-build-docker/share/15.05-0b231aa8e236684985f52cbf79dc418e/./chaos_calmer-15.05/build_dir/target-mipsel_mips32_uClibc-0.9.33.2/OpenWrt-SDK-15.05-ar7-generic_gcc-4.8-linaro_uClibc-0.9.33.2.Linux-x86_64/staging_dir/toolchain-mipsel_mips32_gcc-4.8-linaro_uClibc-0.9.33.2/bin/mipsel-openwrt-linux-
./slsrc.py -u mach-oxnas -a arm -e l -b openwrt -s /root/openwrt-build-docker/share/15.05-bfae3162fb949c343763ad9ea7ab3fe0/./chaos_calmer-15.05/build_dir/target-arm_mpcore_uClibc-0.9.33.2_eabi/linux-oxnas/linux-3.18.20 -mkout /root/openwrt-build-docker/share/15.05-bfae3162fb949c343763ad9ea7ab3fe0/./chaos_calmer-15.05/build_dir/target-arm_mpcore_uClibc-0.9.33.2_eabi/linux-oxnas/makeout.txt -gcc /root/openwrt-build-docker/share/15.05-bfae3162fb949c343763ad9ea7ab3fe0/./chaos_calmer-15.05/build_dir/target-arm_mpcore_uClibc-0.9.33.2_eabi/OpenWrt-SDK-15.05-oxnas_gcc-4.8-linaro_uClibc-0.9.33.2_eabi.Linux-x86_64/staging_dir/toolchain-arm_mpcore_gcc-4.8-linaro_uClibc-0.9.33.2_eabi/bin/arm-openwrt-linux-
```

## Debug

statistics all

````shell script
./salamander.py -wd ../salamander-build -stat
````

diagnose trace

````shell script
./salamander.py -t path/to/uuid-arch-endian.trace
````

## Support List

+ arm/mach-orion5x
+ arm/mach-oxnas
+ mips/bcm47xx

## Contributors
[cyruscyliu*](https://github.com/cyruscyliu/esv), [occia*](https://github.com/occia)

## License
[MIT License](./LICENSE)

## Commands

"""
./slbin.py -f /root/images/278a494b4a543f4a48dbb56d7ce226a23a3fbcc3.bin -u 9692 -a arm -e l -b openwrt -l http://archive.openwrt.org/chaos_calmer/15.05.1/oxnas/generic/openwrt-15.05.1-oxnas-kd20-u-boot-initramfs.bin
./slbin.py -f /root/images/95483e6f102fa1f462eeda09ed945325e5b1bfb9.bin -u 9703 -a arm -e l -b openwrt -l http://archive.openwrt.org/chaos_calmer/15.05.1/oxnas/generic/openwrt-15.05.1-oxnas-pogoplug-pro-u-boot-initramfs.bin
./slbin.py -f /root/images/6b6385ae3faf9b99ec2a290a5fb153752de395de.bin -u 9707 -a arm -e l -b openwrt -l http://archive.openwrt.org/chaos_calmer/15.05.1/oxnas/generic/openwrt-15.05.1-oxnas-pogoplug-v3-u-boot-initramfs.bin
./slbin.py -f /root/images/2da39a873a89312a9860cfe8785691944da6c00a.bin -u 9715 -a arm -e l -b openwrt -l http://archive.openwrt.org/chaos_calmer/15.05.1/oxnas/generic/openwrt-15.05.1-oxnas-stg212-u-boot-initramfs.bin
./slbin.py -f /root/images/988a648617eab1121cc9893296dac74a06611561.bin -u 7276 -a arm -e l -b openwrt -l http://archive.openwrt.org/attitude_adjustment/12.09/orion/generic/openwrt-wrt350nv2-squashfs-recovery.bin
./slbin.py -f /root/images/ec5859077831e078987ebb05461d4ec834896f3e.bin -u 15007 -a arm -e l -b openwrt -l http://archive.openwrt.org/backfire/10.03/orion/openwrt-wrt350nv2-squashfs-recovery.bin
./slbin.py -f /root/images/2b38a390ba53209a1fa4c6aed8489c14774db4c9.bin -u 13882 -a arm -e l -b openwrt -l http://archive.openwrt.org/chaos_calmer/15.05/oxnas/generic/openwrt-15.05-oxnas-kd20-u-boot-initramfs.bin
./slbin.py -f /root/images/e364e96ce9edaeab94ccd750cca20e03fcabad54.bin -u 13890 -a arm -e l -b openwrt -l http://archive.openwrt.org/chaos_calmer/15.05/oxnas/generic/openwrt-15.05-oxnas-pogoplug-pro-u-boot-initramfs.bin
./slbin.py -f /root/images/e976bfc45172ce4705ff926b31d82bf39e0879a8.bin -u 7996 -a arm -e l -b openwrt -l http://archive.openwrt.org/backfire/10.03.1/orion/openwrt-wrt350nv2-squashfs-recovery.bin
./slbin.py -f /root/images/a8a659c598a79e7d37101470952bfca1ccc16f7e.bin -u 13893 -a arm -e l -b openwrt -l http://archive.openwrt.org/chaos_calmer/15.05/oxnas/generic/openwrt-15.05-oxnas-pogoplug-v3-u-boot-initramfs.bin
./slbin.py -f /root/images/404b62b1d28d82b6420d28c2de39d55e7019b6d4.bin -u 13901 -a arm -e l -b openwrt -l http://archive.openwrt.org/chaos_calmer/15.05/oxnas/generic/openwrt-15.05-oxnas-stg212-u-boot-initramfs.bin
"""
