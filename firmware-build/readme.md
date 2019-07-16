# Intro

There are 3 dirs,  `wrt350v2-kernel`, `wrt350v2-work`, `ws`. 

- First 2 dirs are used for build, and manage docker images.
- `wrt350v2-kernel` provides the openwrt350-v2 kernel building env
- `wrt350v2-work` provides the working env
- `ws` is the shared directory for 2 dockers & host, it contains all working data

More info about using the docker, see following chapter 1.


## 1. Docker

### 1.1 Meaning of \*.sh in wrt350v2-\*

Docker image is responsible for providing most of the dependency packages, thus every time running the image we can get a new, clean working/build environment. 

Here, the docker started by start.sh will run in background and never stop by itself.

If you want to use the docker env, run in.sh and you will get a shell.

Use remove.sh to destroy the background running docker and then use start.sh to create a new one.


```bash
# build docker image
bash build-docker-image.sh 

# start docker image in background, and we can exec into it at any time
bash start.sh

# exec into docker image & use, exit if not needed
bash in.sh

# stop & destory the background running docker
bash remove.sh
```

### 1.2 Shared dir between host & 2 dockers

`ws` is a shared directory among the 2 dockers and host machine, and it is mapped to `/root/firmware` in docker.

When you are in docker's shell, anything you do under the path `/root/firmware` is actually do under the host path of `ws`.



##2. Build the kernel

Kernel version: 2.6.32.10

Openwrt version: backfire 10.0.3

Backfire 10.0.3 Download Link(https://archive.openwrt.org/backfire/10.03/orion/OpenWrt-ImageBuilder-orion-for-Linux-i686.tar.bz2)

OpenWrt.config Download Link(https://archive.openwrt.org/backfire/10.03/orion/OpenWrt.config)

### 2.1 Patches & Config to backfire 10.0.3

```bash
cp patches/download.pl ../ws/path/to/backfire_10.03/scripts/download.pl
cp patches/Makefile ../ws/path/to/backfire_10.03/toolchain/binutils/Makefile
cp OpenWrt.config ../ws/path/to/backfire_10.03/.config
```

### 2.2 Build 

```bash
make -j8
# or debug
make -j8 V=99
```



## 3. Build the working env

### 3.1 qemu

Qemu version: 4.0.0-rc3

```bash
mkdir build && cd build
../configure --enable-debug
make
```

### 3.2 panda & ktracer plugin

See ktracer/readme.md

### 3.3 capstone

```bash
git clone https://github.com/aquynh/capstone.git
cd capstone
./make.sh
make install
```

## 4. QEMU + GDB to debug the kernel

```bash
# terminal 1
./panda-build/arm-softmmu/qemu-system-arm -nographic -machine versatilepb \
                                          -S -s ./openwrt-wrt350nv2-uImage

# terminal 2
gdb-multiarch
(gdb) target remote localhost:1234
```
