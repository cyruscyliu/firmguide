# Embedded System Virtualization 

## dependency

```bash
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
```

## install
```bash
make
```

## start
```bash
python3.7 main.py -dbt text -s1
2019-09-19 14:10:06,970 - INFO - there are 11 firmware in the repo
2019-09-19 14:10:06,979 - INFO - [0] firmware 7276 at /tmp/7276/988a648617eab1121cc9893296dac74a06611561.bin
2019-09-19 14:10:06,980 - INFO - extract kernel and dtb by binwalk
2019-09-19 14:10:08,595 - INFO - Legacy uImage found, offset 0, uImage header, header size: 64 bytes, created: 2013-03-24 03:00:11, image size: 960520 bytes, Data Address: 0x8000, Entry Point: 0x8000, OS: Linux, CPU: ARM, image name: "Linux-3.3.8"
2019-09-19 14:10:08,595 - INFO - extract kernel and dtb by uboot_tools
2019-09-19 14:10:09,878 - INFO - get kernel image 0.kernel at /tmp/7276/_988a648617eab1121cc9893296dac74a06611561.bin-36.extracted/0.kernel
2019-09-19 14:10:09,879 - INFO - get metadata by file
2019-09-19 14:10:09,884 - INFO - get the kernel version: Linux-3.3.8, confidence: 1
2019-09-19 14:10:09,885 - INFO - get the operating system: Linux, confidence: 1
2019-09-19 14:10:09,885 - INFO - get the architecture: ARM, confidence: 1
2019-09-19 14:10:09,888 - INFO - [1] firmware 9692 at /tmp/9692/278a494b4a543f4a48dbb56d7ce226a23a3fbcc3.bin
2019-09-19 14:10:09,888 - INFO - extract kernel and dtb by binwalk
2019-09-19 14:10:11,728 - INFO - FIT uImage found, offset 655360, flattened image tree, total size: 3152444 bytes, timestamp: 2016-02-02 12:51:49, description: ARM OpenWrt FIT (Flattened Image Tree)
2019-09-19 14:10:11,728 - INFO - extract kernel and dtb by uboot_tools
2019-09-19 14:10:11,732 - INFO - get kernel image A0000.kernel at /tmp/9692/_278a494b4a543f4a48dbb56d7ce226a23a3fbcc3.bin-28.extracted/A0000.kernel
2019-09-19 14:10:11,734 - INFO - get device tree image A0000.kernel at /tmp/9692/_278a494b4a543f4a48dbb56d7ce226a23a3fbcc3.bin-28.extracted/A0000.dtb
2019-09-19 14:10:11,734 - INFO - get metadata by file
2019-09-19 14:10:11,737 - INFO - get the kernel version: Linux-3.18.23, confidence: 1
2019-09-19 14:10:11,737 - INFO - get the operating system: Linux, confidence: 1
2019-09-19 14:10:11,737 - INFO - get the architecture: ARM, confidence: 1
```

