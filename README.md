# Embedded System Virtualization 

## dependency

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
```

## install
```bash
make
```

## start
```bash
python3.7 main.py -dbt text -s1
```

```text
2019-09-19 18:36:54,004 - INFO - there are 11 firmware in the repo
2019-09-19 18:36:54,013 - INFO - [0] firmware 7276 at /tmp/7276/988a648617eab1121cc9893296dac74a06611561.bin
2019-09-19 18:36:54,013 - INFO - extract kernel and dtb by binwalk
2019-09-19 18:36:55,632 - INFO - Legacy uImage found, offset 0, uImage header, header size: 64 bytes, created: 2013-03-24 03:00:11, image size: 960520 bytes, Data Address: 0x8000, Entry Point: 0x8000, OS: Linux, CPU: ARM, image name: "Linux-3.3.8"
2019-09-19 18:36:55,632 - INFO - extract kernel and dtb by uboot_tools
2019-09-19 18:36:56,930 - INFO - get kernel image 0.kernel at /tmp/7276/_988a648617eab1121cc9893296dac74a06611561.bin-90.extracted/0.kernel
2019-09-19 18:36:56,930 - INFO - get metadata by file
2019-09-19 18:36:56,937 - INFO - get the kernel version: Linux-3.3.8, confidence: 1
2019-09-19 18:36:56,937 - INFO - get the operating system: Linux, confidence: 1
2019-09-19 18:36:56,937 - INFO - get the architecture: ARM, confidence: 1
2019-09-19 18:37:03,179 - INFO - search possible target(s) by strings
2019-09-19 18:37:03,179 - INFO - >> mxs, confidence: 0.06, ['mxs']
2019-09-19 18:37:03,180 - INFO - >> orion, confidence: 0.47, ['orion_irq', 'orion_clocksource', 'orion_tick', 'orion_spi', 'orion_wdt', 'orion-ehci', 'orion_gpio_irq', 'orion_gpio_set_blink']
2019-09-19 18:37:03,180 - INFO - >> sata, confidence: 0.06, ['sata_mv']
2019-09-19 18:37:03,180 - INFO - >> legacy, confidence: 0.06, ['legacy_va_layout']
2019-09-19 18:37:03,180 - INFO - >> omap, confidence: 0.29, ['mtd-romap', 'pci_iomap', 'pcim_iomap_table', 'pcim_iomap_regions', 'pcim_iomap']
2019-09-19 18:37:03,180 - INFO - >> nand, confidence: 0.06, ['nand']
2019-09-19 18:37:03,180 - INFO - get the most possible target orion
2019-09-19 18:37:03,185 - INFO - [1] firmware 9692 at /tmp/9692/278a494b4a543f4a48dbb56d7ce226a23a3fbcc3.bin
2019-09-19 18:37:03,185 - INFO - extract kernel and dtb by binwalk
2019-09-19 18:37:05,033 - INFO - FIT uImage found, offset 655360, flattened image tree, total size: 3152444 bytes, timestamp: 2016-02-02 12:51:49, description: ARM OpenWrt FIT (Flattened Image Tree)
2019-09-19 18:37:05,033 - INFO - extract kernel and dtb by uboot_tools
2019-09-19 18:37:05,037 - INFO - get kernel image A0000.kernel at /tmp/9692/_278a494b4a543f4a48dbb56d7ce226a23a3fbcc3.bin-40.extracted/A0000.kernel
2019-09-19 18:37:05,039 - INFO - get device tree image A0000.kernel at /tmp/9692/_278a494b4a543f4a48dbb56d7ce226a23a3fbcc3.bin-40.extracted/A0000.dtb
2019-09-19 18:37:05,039 - INFO - get metadata by file
2019-09-19 18:37:05,042 - INFO - get the kernel version: Linux-3.18.23, confidence: 1
2019-09-19 18:37:05,042 - INFO - get the operating system: Linux, confidence: 1
2019-09-19 18:37:05,042 - INFO - get the architecture: ARM, confidence: 1
2019-09-19 18:37:05,042 - INFO - search possible target(s) by device tree
2019-09-19 18:37:05,050 - INFO - get the platform ['plxtech,nas7820', 'plxtech,nas782x'], confidence: 1
2019-09-19 18:37:05,050 - INFO - get the model ['Shuttle KD20'], confidence: 1
```

