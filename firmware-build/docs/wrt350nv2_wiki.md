# wrt350nv2 wiki

## 1. MTD分区

关于MTD分区、uboot、kernel三方面的关系，可参见相关引用：

- [bootloader与内核关于mtd cmdline的完整过程](http://www.embeddedlinux.org.cn/emb-linux/kernel-driver/201709/21-7400.html)， 建议细读
- [uboot与kernel在mtd分区上的关系，相关1](https://blog.csdn.net/u013562393/article/details/50868033)，建议略读
- [相关2](https://blog.csdn.net/yjp19871013/article/details/6933455)，建议略读
- [相关3](https://blog.csdn.net/yusiguyuan/article/details/9471577)，建议略读

在wrt350nv2中，mtd分区被openwrt patch过，具体可参见`backfire_10.03/target/linux/orion/patches/`。



**mtd本身知识的额外补充链接**：

- [mtd official faq](http://www.linux-mtd.infradead.org/faq/general.html)

## 2. build system

可参加由openwrt/doc编译出的pdf文档。 

## 3. 内核编译


相关引用：
  - [General linux build guide]( https://github.com/umiddelb/armhf/wiki/How-To-compile-a-custom-Linux-kernel-for-your-ARM-device)
  - [useful kernel debug with gdb link]( https://www.binss.me/blog/how-to-debug-linux-kernel/)
  - [official manual gdb & kernel]( https://www.kernel.org/doc/html/v4.14/dev-tools/kgdb.html)
  - [important kernel configs]( https://ownyourbits.com/2018/05/09/debugging-the-linux-kernel/)
  - [kernel debug with gdb]( https://www.kernel.org/doc/html/latest/dev-tools/gdb-kernel-debugging.html)

**openwrt 相关**

- 下载官网提供的Openwrt.config，直接复制到源目录下的.config
- **不要用make menuconfig来新增或修改配置**，直接修改.config

**kernel 编译**

- openwrt在build内核前，会根据`target/linux/orion/config-default`文件内容生成初步的config
- 并根据`include/kernel-build.mk`和`include/kernel-default.mk`中的逻辑进行后续config的调整和build

### 3.3 tools/wrt350nv2-builder

这是一个用于拼接各mtd分区（uboot，kernel，rootfs等区）内容制作出img的工具，img内容是直接刷入到wrt350nv2的nor flash中。

这一部分工作在uboot的前一层：

- [相关信息介绍](https://stackoverflow.com/questions/29494321/what-is-different-between-u-boot-bin-and-u-boot-img)
- u-boot.img contains u-boot.bin along with an additional header to be used by the boot ROM to determine how and where to load and execute U-Boot.
- Boot ROMs are generally provided by the SoC/CPU vendor. 

## 4. 其他

### 4.1 version

**Linux**

编译linux 2.6.32.10，环境：
- ubuntu 12.04
- backfire 10.0.3
- make version <= 3.82.rc3，建议3.81
- gcc 用12.04自带的version

**U-Boot**

For booting the wrt350nv2, openwrt choose `u-boot-2009.11.tar.bz2`.

**Qemu**

We compile & use the latest `Qemu-4.0.0-rc4.tar.xz`.

### 4.2 refs

- openwrt
  - [backfire 10.03下载链接]( https://archive.openwrt.org/backfire/10.03/orion/)
  - [Dev guide]( https://openwrt.org/docs/guide-developer/start)
  - [user guide]( https://openwrt.org/docs/guide-user/start)
- wrt350nv2 相关链接
  - [cpu etc misc]( https://oldwiki.archive.openwrt.org/toh/linksys/wrt350nv2#technical_details)
  - [Register info in shell]( https://forum.archive.openwrt.org/viewtopic.php?id=12358&p=1#p60299)
  - [inside the wrt350nv2(photos, ports ftp) ]( http://www.maddes.net/files/hardware/)
  - [inside the wrt350nv2(thread)]( https://forum.dd-wrt.com/phpBB2/viewtopic.php?t=10835)
  - [Wrt350nv2 linksys wiki]( https://wikidevi.com/wiki/Linksys_WRT350N_v2)


