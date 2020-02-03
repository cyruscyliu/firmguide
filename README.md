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

```
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
./slbin.py -f /root/images/2cdf62cd8169db1760eacb0bd1d2aa32039828c9.trx -u 14256 -a mips -e l -b openwrt -l http://archive.openwrt.org/chaos_calmer/15.05/brcm47xx/mips74k/openwrt-15.05-brcm47xx-mips74k-asus-rt-n66w-squashfs.trx
./slbin.py -f /root/images/fff34ff978a4c4ee98fb0e32c293c3be52840a63.trx -u 14229 -a mips -e l -b openwrt -l http://archive.openwrt.org/chaos_calmer/15.05/brcm47xx/mips74k/openwrt-15.05-brcm47xx-mips74k-asus-rt-n10-squashfs.trx
./slbin.py -f /root/images/155a86c671a812602f49a559178449ecc234c2b9.trx -u 14234 -a mips -e l -b openwrt -l http://archive.openwrt.org/chaos_calmer/15.05/brcm47xx/mips74k/openwrt-15.05-brcm47xx-mips74k-asus-rt-n10p-v2-squashfs.trx
./slbin.py -f /root/images/9e919948cede44f4ad42b14c212020587f32cf91.trx -u 14239 -a mips -e l -b openwrt -l http://archive.openwrt.org/chaos_calmer/15.05/brcm47xx/mips74k/openwrt-15.05-brcm47xx-mips74k-asus-rt-n12-b1-squashfs.trx
./slbin.py -f /root/images/6da1a4cc6ed7f0b8bea53db0777e0f9bb8657499.trx -u 14243 -a mips -e l -b openwrt -l http://archive.openwrt.org/chaos_calmer/15.05/brcm47xx/mips74k/openwrt-15.05-brcm47xx-mips74k-asus-rt-n12-c1-squashfs.trx
./slbin.py -f /root/images/b11bb7967ec706cfcf9124123a1d6720d87e3fdf.trx -u 14244 -a mips -e l -b openwrt -l http://archive.openwrt.org/chaos_calmer/15.05/brcm47xx/mips74k/openwrt-15.05-brcm47xx-mips74k-asus-rt-n12-d1-squashfs.trx
./slbin.py -f /root/images/09131f26942a9cf902046fe00a0947e7477cae25.trx -u 14248 -a mips -e l -b openwrt -l http://archive.openwrt.org/chaos_calmer/15.05/brcm47xx/mips74k/openwrt-15.05-brcm47xx-mips74k-asus-rt-n12hp-squashfs.trx
./slbin.py -f /root/images/d0db1822f2bb315a9a13fdfd6f16481e1f572a03.trx -u 14250 -a mips -e l -b openwrt -l http://archive.openwrt.org/chaos_calmer/15.05/brcm47xx/mips74k/openwrt-15.05-brcm47xx-mips74k-asus-rt-n14uhp-squashfs.trx
./slbin.py -f /root/images/a6d25de39767a199ebfcd85781920ff22cbf8144.trx -u 14252 -a mips -e l -b openwrt -l http://archive.openwrt.org/chaos_calmer/15.05/brcm47xx/mips74k/openwrt-15.05-brcm47xx-mips74k-asus-rt-n15u-squashfs.trx
./slbin.py -f /root/images/22144d687c7ad280db0f1b83d9d96af2aec9165c.trx -u 14253 -a mips -e l -b openwrt -l http://archive.openwrt.org/chaos_calmer/15.05/brcm47xx/mips74k/openwrt-15.05-brcm47xx-mips74k-asus-rt-n16-squashfs.trx
./slbin.py -f /root/images/90b6ddb6153c35a903e558fd07a8cfd78fd64a2c.trx -u 14258 -a mips -e l -b openwrt -l http://archive.openwrt.org/chaos_calmer/15.05/brcm47xx/mips74k/openwrt-15.05-brcm47xx-mips74k-asus-rt-n53-squashfs.trx
./slbin.py -f /root/images/ea61143f2612b595b1af538a3375978239168fb9.bin -u 14263 -a mips -e l -b openwrt -l http://archive.openwrt.org/chaos_calmer/15.05/brcm47xx/mips74k/openwrt-15.05-brcm47xx-mips74k-linksys-e1200-v1-squashfs.bin
./slbin.py -f /root/images/e9cd5cd309fc55c10df396c8183dbb3371e5cd24.bin -u 14262 -a mips -e l -b openwrt -l http://archive.openwrt.org/chaos_calmer/15.05/brcm47xx/mips74k/openwrt-15.05-brcm47xx-mips74k-linksys-e1000-v1-v2-v2.1-squashfs.bin
./slbin.py -f /root/images/ddc2660be05a4b12fd920ec9cb4ce57ab6e424dc.bin -u 14266 -a mips -e l -b openwrt -l http://archive.openwrt.org/chaos_calmer/15.05/brcm47xx/mips74k/openwrt-15.05-brcm47xx-mips74k-linksys-e1500-v1-squashfs.bin
./slbin.py -f /root/images/b7e42766cca952f3838b2738519c7a85514dd849.bin -u 14264 -a mips -e l -b openwrt -l http://archive.openwrt.org/chaos_calmer/15.05/brcm47xx/mips74k/openwrt-15.05-brcm47xx-mips74k-linksys-e1200-v2-squashfs.bin
./slbin.py -f /root/images/d7b92a102b9b89bfe8315bad88c91b8d2fb8afd5.bin -u 14267 -a mips -e l -b openwrt -l http://archive.openwrt.org/chaos_calmer/15.05/brcm47xx/mips74k/openwrt-15.05-brcm47xx-mips74k-linksys-e1550-v1-squashfs.bin
./slbin.py -f /root/images/05c7f69a1ef3e786adc50a11aa74f8d2c233ce3a.bin -u 14269 -a mips -e l -b openwrt -l http://archive.openwrt.org/chaos_calmer/15.05/brcm47xx/mips74k/openwrt-15.05-brcm47xx-mips74k-linksys-e2000-v1-squashfs.bin
./slbin.py -f /root/images/2a787e058f08aa396f229fd6a5f3a1d4aa66a019.bin -u 14270 -a mips -e l -b openwrt -l http://archive.openwrt.org/chaos_calmer/15.05/brcm47xx/mips74k/openwrt-15.05-brcm47xx-mips74k-linksys-e2500-v1-squashfs.bin
./slbin.py -f /root/images/970cb22a5f1c4f92bbaf0448298ff7ab7d86dedd.bin -u 14272 -a mips -e l -b openwrt -l http://archive.openwrt.org/chaos_calmer/15.05/brcm47xx/mips74k/openwrt-15.05-brcm47xx-mips74k-linksys-e2500-v2.1-squashfs.bin
./slbin.py -f /root/images/937fbe7d26ae46b6129895d41f1ab8fe0804b205.bin -u 14274 -a mips -e l -b openwrt -l http://archive.openwrt.org/chaos_calmer/15.05/brcm47xx/mips74k/openwrt-15.05-brcm47xx-mips74k-linksys-e2500-v3-squashfs.bin
./slbin.py -f /root/images/6bcd550b6dece1aaf12c8b5b52ca7b1ca3aa0349.bin -u 14281 -a mips -e l -b openwrt -l http://archive.openwrt.org/chaos_calmer/15.05/brcm47xx/mips74k/openwrt-15.05-brcm47xx-mips74k-linksys-e3200-v1-squashfs.bin
./slbin.py -f /root/images/ee0daa31acdf04f68171c48996e90c73f626ba0e.bin -u 14279 -a mips -e l -b openwrt -l http://archive.openwrt.org/chaos_calmer/15.05/brcm47xx/mips74k/openwrt-15.05-brcm47xx-mips74k-linksys-e4200-v1-squashfs.bin
./slbin.py -f /root/images/12f41f96b81dda9f51a1ee3a62c27e58e70a8dbc.bin -u 14284 -a mips -e l -b openwrt -l http://archive.openwrt.org/chaos_calmer/15.05/brcm47xx/mips74k/openwrt-15.05-brcm47xx-mips74k-linksys-wrt160n-v3-squashfs.bin
./slbin.py -f /root/images/a7af242b273e72a3dbda1bc0dff8a4e1d1ce63c6.bin -u 14285 -a mips -e l -b openwrt -l http://archive.openwrt.org/chaos_calmer/15.05/brcm47xx/mips74k/openwrt-15.05-brcm47xx-mips74k-linksys-e900-v1-squashfs.bin
./slbin.py -f /root/images/2028f81fb258905836791bffc37a47b97f8af602.bin -u 14288 -a mips -e l -b openwrt -l http://archive.openwrt.org/chaos_calmer/15.05/brcm47xx/mips74k/openwrt-15.05-brcm47xx-mips74k-linksys-wrt310n-v2-squashfs.bin
./slbin.py -f /root/images/9874f62ffd1d5d1ccdfa919cc29794f03d1f08db.bin -u 14292 -a mips -e l -b openwrt -l http://archive.openwrt.org/chaos_calmer/15.05/brcm47xx/mips74k/openwrt-15.05-brcm47xx-mips74k-linksys-wrt320n-v1-squashfs.bin
./slbin.py -f /root/images/9695ea2386973e9cbee69008b79c033a30609180.chk -u 14291 -a mips -e l -b openwrt -l http://archive.openwrt.org/chaos_calmer/15.05/brcm47xx/mips74k/openwrt-15.05-brcm47xx-mips74k-netgear-wgr614-v10_north-america-squashfs.chk
./slbin.py -f /root/images/a69ab2a7cdded820fe48499e5ebe7d19faa1b141.chk -u 14298 -a mips -e l -b openwrt -l http://archive.openwrt.org/chaos_calmer/15.05/brcm47xx/mips74k/openwrt-15.05-brcm47xx-mips74k-netgear-wndr3400-v2-squashfs.chk
./slbin.py -f /root/images/93c33c84ce8b508448c895b587ef07231bcf078a.chk -u 14293 -a mips -e l -b openwrt -l http://archive.openwrt.org/chaos_calmer/15.05/brcm47xx/mips74k/openwrt-15.05-brcm47xx-mips74k-netgear-wgr614-v10_other-regions-squashfs.chk
./slbin.py -f /root/images/76b300e2e11560c1770ffb377d1457fef331adbb.chk -u 14296 -a mips -e l -b openwrt -l http://archive.openwrt.org/chaos_calmer/15.05/brcm47xx/mips74k/openwrt-15.05-brcm47xx-mips74k-netgear-wndr3400-v1-squashfs.chk
./slbin.py -f /root/images/f00c1acd1a71e66e227cfa870a2caea15120519f.chk -u 14303 -a mips -e l -b openwrt -l http://archive.openwrt.org/chaos_calmer/15.05/brcm47xx/mips74k/openwrt-15.05-brcm47xx-mips74k-netgear-wndr3700-v3-squashfs.chk
./slbin.py -f /root/images/a28c5d02660ba89d9412844ff02d735451c27724.chk -u 14305 -a mips -e l -b openwrt -l http://archive.openwrt.org/chaos_calmer/15.05/brcm47xx/mips74k/openwrt-15.05-brcm47xx-mips74k-netgear-wndr4000-squashfs.chk
./slbin.py -f /root/images/ecff64e5a50cf65d5a197d917bb0f831459a5ad5.chk -u 14302 -a mips -e l -b openwrt -l http://archive.openwrt.org/chaos_calmer/15.05/brcm47xx/mips74k/openwrt-15.05-brcm47xx-mips74k-netgear-wndr3400-v3-squashfs.chk
./slbin.py -f /root/images/25c63aaa09c179c78d4d7ab05d844983d8b8e9b0.chk -u 14309 -a mips -e l -b openwrt -l http://archive.openwrt.org/chaos_calmer/15.05/brcm47xx/mips74k/openwrt-15.05-brcm47xx-mips74k-netgear-wnr3000rp-squashfs.chk
./slbin.py -f /root/images/61f0e104008a9a3b633e80dc29531d0e831ea56e.chk -u 14304 -a mips -e l -b openwrt -l http://archive.openwrt.org/chaos_calmer/15.05/brcm47xx/mips74k/openwrt-15.05-brcm47xx-mips74k-netgear-wnr2000v2-squashfs.chk
./slbin.py -f /root/images/1fac04f300917ca3226761cdb2fd708a84992817.chk -u 14307 -a mips -e l -b openwrt -l http://archive.openwrt.org/chaos_calmer/15.05/brcm47xx/mips74k/openwrt-15.05-brcm47xx-mips74k-netgear-wnr3500-v2-squashfs.chk
./slbin.py -f /root/images/0fb2085a88df1cc87e8b183ceda98bb5b39d7ed1.chk -u 14314 -a mips -e l -b openwrt -l http://archive.openwrt.org/chaos_calmer/15.05/brcm47xx/mips74k/openwrt-15.05-brcm47xx-mips74k-netgear-wnr3500l-v1-other-regions-squashfs.chk
./slbin.py -f /root/images/d4de0e838e2893af0abafe3d9c8d8baf82b9cb08.chk -u 14319 -a mips -e l -b openwrt -l http://archive.openwrt.org/chaos_calmer/15.05/brcm47xx/mips74k/openwrt-15.05-brcm47xx-mips74k-netgear-wnr3500l-v2-squashfs.chk
./slbin.py -f /root/images/bee2bb5a8556717445c21156d28c30264dbce2a1.trx -u 14322 -a mips -e l -b openwrt -l http://archive.openwrt.org/chaos_calmer/15.05/brcm47xx/mips74k/openwrt-15.05-brcm47xx-mips74k-squashfs.trx
./slbin.py -f /root/images/e3ea7234d10a0eb83d2b469382ea3f91b8864114.trx -u 14321 -a mips -e l -b openwrt -l http://archive.openwrt.org/chaos_calmer/15.05/brcm47xx/mips74k/openwrt-15.05-brcm47xx-mips74k-squashfs-noloader-nodictionary.trx
./slbin.py -f /root/images/a4388278fb5721aca6465232e92c62ce6072550b.trx -u 14318 -a mips -e l -b openwrt -l http://archive.openwrt.org/chaos_calmer/15.05/brcm47xx/mips74k/openwrt-15.05-brcm47xx-mips74k-squashfs-gz.trx
./slbin.py -f /root/images/7ff399c790b774f6f1023813e6f34d62b76f382f.trx -u 10175 -a mips -e l -b openwrt -l http://archive.openwrt.org/chaos_calmer/15.05.1/brcm47xx/mips74k/openwrt-15.05.1-brcm47xx-mips74k-asus-rt-ac53u-squashfs.trx
./slbin.py -f /root/images/5407f9892ed407b7aed5c94fbca485cf82ada2d6.trx -u 10181 -a mips -e l -b openwrt -l http://archive.openwrt.org/chaos_calmer/15.05.1/brcm47xx/mips74k/openwrt-15.05.1-brcm47xx-mips74k-asus-rt-n10-squashfs.trx
./slbin.py -f /root/images/3313d563fc70bbc4bbbf0d3d089b57a9e9d93a3f.trx -u 10183 -a mips -e l -b openwrt -l http://archive.openwrt.org/chaos_calmer/15.05.1/brcm47xx/mips74k/openwrt-15.05.1-brcm47xx-mips74k-asus-rt-n10p-squashfs.trx
./slbin.py -f /root/images/77eb80fdea73163d1a6013bf1cab850e30a32f22.trx -u 10186 -a mips -e l -b openwrt -l http://archive.openwrt.org/chaos_calmer/15.05.1/brcm47xx/mips74k/openwrt-15.05.1-brcm47xx-mips74k-asus-rt-n10p-v2-squashfs.trx
./slbin.py -f /root/images/323e2c904fd31915c4a37372884be901c80c6403.trx -u 10199 -a mips -e l -b openwrt -l http://archive.openwrt.org/chaos_calmer/15.05.1/brcm47xx/mips74k/openwrt-15.05.1-brcm47xx-mips74k-asus-rt-n12-b1-squashfs.trx
./slbin.py -f /root/images/d77ef9178744307869e38b5961e270934d516db2.trx -u 10206 -a mips -e l -b openwrt -l http://archive.openwrt.org/chaos_calmer/15.05.1/brcm47xx/mips74k/openwrt-15.05.1-brcm47xx-mips74k-asus-rt-n12-c1-squashfs.trx
./slbin.py -f /root/images/85fb042f8235ba250e146fff73f1d5ac74dc02c4.trx -u 10215 -a mips -e l -b openwrt -l http://archive.openwrt.org/chaos_calmer/15.05.1/brcm47xx/mips74k/openwrt-15.05.1-brcm47xx-mips74k-asus-rt-n12-d1-squashfs.trx
./slbin.py -f /root/images/bf8a76c2bf47e2d8e763eb96ea0eacd3e8aba493.trx -u 10218 -a mips -e l -b openwrt -l http://archive.openwrt.org/chaos_calmer/15.05.1/brcm47xx/mips74k/openwrt-15.05.1-brcm47xx-mips74k-asus-rt-n12-squashfs.trx
./slbin.py -f /root/images/6a16b6a9cf8e1d1b2339772dd796ba9347076833.trx -u 10229 -a mips -e l -b openwrt -l http://archive.openwrt.org/chaos_calmer/15.05.1/brcm47xx/mips74k/openwrt-15.05.1-brcm47xx-mips74k-asus-rt-n12hp-squashfs.trx
./slbin.py -f /root/images/097730fe1943e7f07214660782559dbd80185a8a.trx -u 10246 -a mips -e l -b openwrt -l http://archive.openwrt.org/chaos_calmer/15.05.1/brcm47xx/mips74k/openwrt-15.05.1-brcm47xx-mips74k-asus-rt-n15u-squashfs.trx
./slbin.py -f /root/images/f4825bc4bb3d6d9a28fdf20a8a8c37e273fcdf3c.trx -u 10253 -a mips -e l -b openwrt -l http://archive.openwrt.org/chaos_calmer/15.05.1/brcm47xx/mips74k/openwrt-15.05.1-brcm47xx-mips74k-asus-rt-n16-squashfs.trx
./slbin.py -f /root/images/c7a9a0b5d150f8a3a5f3ea4cca2185354e0e422a.trx -u 10260 -a mips -e l -b openwrt -l http://archive.openwrt.org/chaos_calmer/15.05.1/brcm47xx/mips74k/openwrt-15.05.1-brcm47xx-mips74k-asus-rt-n53-squashfs.trx
./slbin.py -f /root/images/43baf56619217fcc27c3bb1fa8d2718945b4d7c4.trx -u 10235 -a mips -e l -b openwrt -l http://archive.openwrt.org/chaos_calmer/15.05.1/brcm47xx/mips74k/openwrt-15.05.1-brcm47xx-mips74k-asus-rt-n14uhp-squashfs.trx
./slbin.py -f /root/images/9f942648d32317f67a50249216d0497df8d3e1dd.bin -u 10290 -a mips -e l -b openwrt -l http://archive.openwrt.org/chaos_calmer/15.05.1/brcm47xx/mips74k/openwrt-15.05.1-brcm47xx-mips74k-linksys-e1000-v1-v2-v2.1-squashfs.bin
./slbin.py -f /root/images/dfe0eb5dc13a507fb82e9f69250b7fe708b3c3c5.bin -u 10295 -a mips -e l -b openwrt -l http://archive.openwrt.org/chaos_calmer/15.05.1/brcm47xx/mips74k/openwrt-15.05.1-brcm47xx-mips74k-linksys-e1200-v1-squashfs.bin
./slbin.py -f /root/images/3aa16958c4704d649dd68327391138e3323d0290.bin -u 10300 -a mips -e l -b openwrt -l http://archive.openwrt.org/chaos_calmer/15.05.1/brcm47xx/mips74k/openwrt-15.05.1-brcm47xx-mips74k-linksys-e1200-v2-squashfs.bin
./slbin.py -f /root/images/68c35826f11832e2b6ef9555a6661e10ef35968e.bin -u 10310 -a mips -e l -b openwrt -l http://archive.openwrt.org/chaos_calmer/15.05.1/brcm47xx/mips74k/openwrt-15.05.1-brcm47xx-mips74k-linksys-e1500-v1-squashfs.bin
./slbin.py -f /root/images/2a92d4cfb9fd98802127d73aa466b73c9ee413fa.bin -u 10316 -a mips -e l -b openwrt -l http://archive.openwrt.org/chaos_calmer/15.05.1/brcm47xx/mips74k/openwrt-15.05.1-brcm47xx-mips74k-linksys-e1550-v1-squashfs.bin
./slbin.py -f /root/images/d34d8ec4dfd6eb0af9ce8c86abcdddfa1e47efbf.bin -u 10333 -a mips -e l -b openwrt -l http://archive.openwrt.org/chaos_calmer/15.05.1/brcm47xx/mips74k/openwrt-15.05.1-brcm47xx-mips74k-linksys-e2000-v1-squashfs.bin
./slbin.py -f /root/images/abde7456963dff3c2f0806fa07904e46ebd7fd1e.bin -u 10357 -a mips -e l -b openwrt -l http://archive.openwrt.org/chaos_calmer/15.05.1/brcm47xx/mips74k/openwrt-15.05.1-brcm47xx-mips74k-linksys-e2500-v2.1-squashfs.bin
./slbin.py -f /root/images/9eb89f2c1e4010e18e53a8563df366dbd3e33d24.bin -u 10369 -a mips -e l -b openwrt -l http://archive.openwrt.org/chaos_calmer/15.05.1/brcm47xx/mips74k/openwrt-15.05.1-brcm47xx-mips74k-linksys-e2500-v3-squashfs.bin
./slbin.py -f /root/images/a9c5a2f6221fcdf4426bbd39afa5bce2f82baf39.bin -u 10379 -a mips -e l -b openwrt -l http://archive.openwrt.org/chaos_calmer/15.05.1/brcm47xx/mips74k/openwrt-15.05.1-brcm47xx-mips74k-linksys-e3200-v1-squashfs.bin
./slbin.py -f /root/images/f01ae518ab483210560f2eec70979ef95fe931c9.bin -u 10399 -a mips -e l -b openwrt -l http://archive.openwrt.org/chaos_calmer/15.05.1/brcm47xx/mips74k/openwrt-15.05.1-brcm47xx-mips74k-linksys-wrt160n-v3-squashfs.bin
./slbin.py -f /root/images/6a6f413ee2d8894792cea92127f04b46b6f92878.bin -u 10396 -a mips -e l -b openwrt -l http://archive.openwrt.org/chaos_calmer/15.05.1/brcm47xx/mips74k/openwrt-15.05.1-brcm47xx-mips74k-linksys-wrt310n-v2-squashfs.bin
./slbin.py -f /root/images/6afe402157bcf2946136f789b4c89f6564c52c2f.bin -u 10344 -a mips -e l -b openwrt -l http://archive.openwrt.org/chaos_calmer/15.05.1/brcm47xx/mips74k/openwrt-15.05.1-brcm47xx-mips74k-linksys-e2500-v2-squashfs.bin
./slbin.py -f /root/images/0f52ee5f029a85c70aa2b44bc0830fa4bb92ba6a.bin -u 10389 -a mips -e l -b openwrt -l http://archive.openwrt.org/chaos_calmer/15.05.1/brcm47xx/mips74k/openwrt-15.05.1-brcm47xx-mips74k-linksys-e4200-v1-squashfs.bin
./slbin.py -f /root/images/c2d2b3e23245b1716d146953f7def4aa21195a8f.bin -u 10387 -a mips -e l -b openwrt -l http://archive.openwrt.org/chaos_calmer/15.05.1/brcm47xx/mips74k/openwrt-15.05.1-brcm47xx-mips74k-linksys-e900-v1-squashfs.bin
./slbin.py -f /root/images/c52b835c1aebe660cf123fc6d6a7f726b415e38b.bin -u 10400 -a mips -e l -b openwrt -l http://archive.openwrt.org/chaos_calmer/15.05.1/brcm47xx/mips74k/openwrt-15.05.1-brcm47xx-mips74k-linksys-wrt320n-v1-squashfs.bin
./slbin.py -f /root/images/bbd488b23c63e49cd26474ad8c6c85d83fbcff6c.chk -u 10412 -a mips -e l -b openwrt -l http://archive.openwrt.org/chaos_calmer/15.05.1/brcm47xx/mips74k/openwrt-15.05.1-brcm47xx-mips74k-netgear-wgr614-v10_north-america-squashfs.chk
./slbin.py -f /root/images/a17ca687477fe6444565206a9186dafa1fe5eab3.chk -u 10423 -a mips -e l -b openwrt -l http://archive.openwrt.org/chaos_calmer/15.05.1/brcm47xx/mips74k/openwrt-15.05.1-brcm47xx-mips74k-netgear-wndr3400-v2-squashfs.chk
./slbin.py -f /root/images/ea4a5fbb326c387e6fc6d1fcfef8d974d6c06aae.chk -u 10445 -a mips -e l -b openwrt -l http://archive.openwrt.org/chaos_calmer/15.05.1/brcm47xx/mips74k/openwrt-15.05.1-brcm47xx-mips74k-netgear-wnr1000-v3-squashfs.chk
./slbin.py -f /root/images/312870d0a0c59d477a4bc01b746854ce620addbf.chk -u 10450 -a mips -e l -b openwrt -l http://archive.openwrt.org/chaos_calmer/15.05.1/brcm47xx/mips74k/openwrt-15.05.1-brcm47xx-mips74k-netgear-wnr2000v2-squashfs.chk
./slbin.py -f /root/images/0c944f44142d71cce5981d20fecb2ceab6af8cd1.chk -u 10415 -a mips -e l -b openwrt -l http://archive.openwrt.org/chaos_calmer/15.05.1/brcm47xx/mips74k/openwrt-15.05.1-brcm47xx-mips74k-netgear-wgr614-v10_other-regions-squashfs.chk
./slbin.py -f /root/images/a34f3d809dea34eac84822a909f099e8950dcb8b.chk -u 10420 -a mips -e l -b openwrt -l http://archive.openwrt.org/chaos_calmer/15.05.1/brcm47xx/mips74k/openwrt-15.05.1-brcm47xx-mips74k-netgear-wndr3400-v1-squashfs.chk
./slbin.py -f /root/images/0b73343f0f4ff58f29211c548f17da7c9f007de3.chk -u 10428 -a mips -e l -b openwrt -l http://archive.openwrt.org/chaos_calmer/15.05.1/brcm47xx/mips74k/openwrt-15.05.1-brcm47xx-mips74k-netgear-wndr3400-v3-squashfs.chk
./slbin.py -f /root/images/5f1f968314759cfba072db4c3b34acee9e187c59.chk -u 10432 -a mips -e l -b openwrt -l http://archive.openwrt.org/chaos_calmer/15.05.1/brcm47xx/mips74k/openwrt-15.05.1-brcm47xx-mips74k-netgear-wndr3700-v3-squashfs.chk
./slbin.py -f /root/images/829863f818a7b359f1397548ce139b6a42556a02.chk -u 10444 -a mips -e l -b openwrt -l http://archive.openwrt.org/chaos_calmer/15.05.1/brcm47xx/mips74k/openwrt-15.05.1-brcm47xx-mips74k-netgear-wndr4000-squashfs.chk
./slbin.py -f /root/images/fe560c33e640e36f029711db209b7cf47534163c.chk -u 10468 -a mips -e l -b openwrt -l http://archive.openwrt.org/chaos_calmer/15.05.1/brcm47xx/mips74k/openwrt-15.05.1-brcm47xx-mips74k-netgear-wnr3500-v2-squashfs.chk
./slbin.py -f /root/images/5b3d05c1a179de55a7d2820a2441dc5d798fc01a.chk -u 10480 -a mips -e l -b openwrt -l http://archive.openwrt.org/chaos_calmer/15.05.1/brcm47xx/mips74k/openwrt-15.05.1-brcm47xx-mips74k-netgear-wnr3500l-v1-other-regions-squashfs.chk
./slbin.py -f /root/images/74392f4de9b87e8821016969c0ec4c39cbac7351.chk -u 10484 -a mips -e l -b openwrt -l http://archive.openwrt.org/chaos_calmer/15.05.1/brcm47xx/mips74k/openwrt-15.05.1-brcm47xx-mips74k-netgear-wnr3500l-v2-squashfs.chk
./slbin.py -f /root/images/2d9391b89c79c62046dbac91fa8ec340bd1f2d6c.trx -u 10492 -a mips -e l -b openwrt -l http://archive.openwrt.org/chaos_calmer/15.05.1/brcm47xx/mips74k/openwrt-15.05.1-brcm47xx-mips74k-squashfs-gz.trx
./slbin.py -f /root/images/42acbdb58010188e204ac14c3c9f804f34e3d065.trx -u 10495 -a mips -e l -b openwrt -l http://archive.openwrt.org/chaos_calmer/15.05.1/brcm47xx/mips74k/openwrt-15.05.1-brcm47xx-mips74k-squashfs-noloader-nodictionary.trx
./slbin.py -f /root/images/741d7f31dba598c2348df55e0fb62d24765c8ebd.trx -u 10500 -a mips -e l -b openwrt -l http://archive.openwrt.org/chaos_calmer/15.05.1/brcm47xx/mips74k/openwrt-15.05.1-brcm47xx-mips74k-squashfs.trx
./slbin.py -f /root/images/ffec4629c2a0f1a336d78b536ce1da5f4e109acd.trx -u 10271 -a mips -e l -b openwrt -l http://archive.openwrt.org/chaos_calmer/15.05.1/brcm47xx/mips74k/openwrt-15.05.1-brcm47xx-mips74k-asus-rt-n66w-squashfs.trx
./slbin.py -f /root/images/0e8b143255022b1b4b6d4d0e8305888934e02738.trx -u 8660 -a mips -e l -b openwrt -l http://archive.openwrt.org/barrier_breaker/14.07/brcm47xx/mips74k/openwrt-brcm47xx-mips74k-squashfs-gz.trx
./slbin.py -f /root/images/858efd925edfb84f0738092f0ff5ab19547e6a16.trx -u 8661 -a mips -e l -b openwrt -l http://archive.openwrt.org/barrier_breaker/14.07/brcm47xx/mips74k/openwrt-brcm47xx-mips74k-squashfs-noloader-nodictionary.trx
./slbin.py -f /root/images/5e54dcf30b60c779af597db1749ad6808b4c2a22.trx -u 8665 -a mips -e l -b openwrt -l http://archive.openwrt.org/barrier_breaker/14.07/brcm47xx/mips74k/openwrt-brcm47xx-mips74k-squashfs.trx
./slbin.py -f /root/images/a7a89b1e8f7cf0ec419ba416d67a6e1aec5ef801.bin -u 10331 -a mips -e l -b openwrt -l http://archive.openwrt.org/chaos_calmer/15.05.1/brcm47xx/mips74k/openwrt-15.05.1-brcm47xx-mips74k-linksys-e2500-v1-squashfs.bin
./slbin.py -f /root/images/fc19807e9f523576bc5929de0e98de7c9d12f65a.chk -u 10474 -a mips -e l -b openwrt -l http://archive.openwrt.org/chaos_calmer/15.05.1/brcm47xx/mips74k/openwrt-15.05.1-brcm47xx-mips74k-netgear-wnr3500l-v1-north-america-squashfs.chk
./slbin.py -f /root/images/1f1474f2966e9506979a9ed246d17bb182015f30.trx -u 14225 -a mips -e l -b openwrt -l http://archive.openwrt.org/chaos_calmer/15.05/brcm47xx/mips74k/openwrt-15.05-brcm47xx-mips74k-asus-rt-ac53u-squashfs.trx
./slbin.py -f /root/images/8fc8c9548f80ad9324c20e6892c6d71763ebc5e9.chk -u 14312 -a mips -e l -b openwrt -l http://archive.openwrt.org/chaos_calmer/15.05/brcm47xx/mips74k/openwrt-15.05-brcm47xx-mips74k-netgear-wnr3500l-v1-north-america-squashfs.chk
./slbin.py -f /root/images/56649171528eb19811801666706072cb47dd103a.trx -u 14230 -a mips -e l -b openwrt -l http://archive.openwrt.org/chaos_calmer/15.05/brcm47xx/mips74k/openwrt-15.05-brcm47xx-mips74k-asus-rt-n10p-squashfs.trx
./slbin.py -f /root/images/09504287ac27e5d20e21d85a8548d7b2c48ad5d2.trx -u 14235 -a mips -e l -b openwrt -l http://archive.openwrt.org/chaos_calmer/15.05/brcm47xx/mips74k/openwrt-15.05-brcm47xx-mips74k-asus-rt-n10u-squashfs.trx
./slbin.py -f /root/images/68c92d58b255a738ec447a912a96aa5912c49dc1.trx -u 14246 -a mips -e l -b openwrt -l http://archive.openwrt.org/chaos_calmer/15.05/brcm47xx/mips74k/openwrt-15.05-brcm47xx-mips74k-asus-rt-n12-squashfs.trx
./slbin.py -f /root/images/7b93b4f4f812783ea5573ea6c6131cb683106f46.bin -u 14273 -a mips -e l -b openwrt -l http://archive.openwrt.org/chaos_calmer/15.05/brcm47xx/mips74k/openwrt-15.05-brcm47xx-mips74k-linksys-e2500-v2-squashfs.bin
./slbin.py -f /root/images/764481eee24abdfa0a3462018c68af9ceee7592e.chk -u 10459 -a mips -e l -b openwrt -l http://archive.openwrt.org/chaos_calmer/15.05.1/brcm47xx/mips74k/openwrt-15.05.1-brcm47xx-mips74k-netgear-wnr3000rp-squashfs.chk
./slbin.py -f /root/images/6ab6e09f965e1680c4f356978f6bb8389294eaf5.trx -u 10192 -a mips -e l -b openwrt -l http://archive.openwrt.org/chaos_calmer/15.05.1/brcm47xx/mips74k/openwrt-15.05.1-brcm47xx-mips74k-asus-rt-n10u-squashfs.trx
```
