# firmware building and working environment

- `*-kernel` provides the kernel building environment
- `*-work` provides the working environment
- `ws` is the shared directory for dockers & host, which contains all working data

## 1. How to Use Docker

### 1.1 meaning of \*.sh in *-\*

Docker image is responsible for providing most of the dependency packages, thus every time running the image we can get 
a new, clean working/build environment. First, build a docker by `build-docker-image.sh`. Then, the docker started by 
`start.sh` will run in background and never stop by itself. If you want to use the docker env, run `in.sh` and you will 
get a shell. Use `remove.sh` to destroy the background running docker and then use `start.sh` to create a new one.

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

### 1.2 shared dir between host & dockers

`ws` is a shared directory among the 2 dockers and host machine, and it is mapped to `/root/firmware` in docker. 
When you are in docker's shell, anything you do under the path `/root/firmware` is actually do under the host path of `ws`.

### 1.3 common FAQ

#### install a docker

- Install Manual: https://docs.docker.com/install/linux/docker-ce/ubuntu/
- Post Manual: https://docs.docker.com/install/linux/linux-postinstall/
- Get Started: https://docs.docker.com/get-started/

#### start the docker

../wrt350nv2-kernel/start.sh: line 1: docker-compose: command not found

```bash
sudo -H pip3.7 install docker-compose
```

Can't find a suitable configuration file in this directory or any parent. Are you in the right directory?

```bash
cd path/to/wrt350nv2-kernel
```

ERROR: Couldn't connect to Docker daemon at http+docker://localhost - is it running?

```bash
systemctl enable docker
systemctl start docker
```

ERROR: pull access denied for wrt350nv2-build-env, repository does not exist or may require 'docker login': 
denied: requested access to the resource is denied

```bash
./build-docker-image.sh
```

## 2. Build the kernel 

Using the container from docker image wrt350nv2-build-env:latest
+ Kernel version: 2.6.32.10
+ Openwrt version: backfire 10.0.3
+ Download [Backfire 10.0.3](https://archive.openwrt.org/backfire/10.03/orion/OpenWrt-ImageBuilder-orion-for-Linux-i686.tar.bz2)
+ Download [.config for Backfire 10.0.3](https://archive.openwrt.org/backfire/10.03/orion/OpenWrt.config)

Using the container from docker image nas7820-build-evn:latest
+ Kernel version: 3.18.20
+ Openwrt version: chaos calmer 15.05
+ Download [Chaos Calmer 15.05](https://archive.openwrt.org/chaos_calmer/15.05/oxnas/generic/OpenWrt-ImageBuilder-15.05-oxnas.Linux-x86_64.tar.bz2)
+ Check [config.diff for Backfire 10.0.3](https://archive.openwrt.org/chaos_calmer/15.05/oxnas/generic/config.diff)

### 2.1 Patches & Config 

Here lists the patches for building the kernel. You should first apply these patches before building.

For wrt350nv2, you should

```bash
# for basic build
cp patches/download.pl ../ws/path/to/backfire_10.03/scripts/download.pl
cp patches/Makefile ../ws/path/to/backfire_10.03/toolchain/binutils/Makefile
cp patches/OpenWrt.config ../ws/path/to/backfire_10.03/.config
# for debug-info
cp patches/kernel-defaults.mk ../ws/path/to/backfire_10.03/include/kernel-defaults.mk
cp patches/kernel-config-extra ../ws/path/to/backfire_10.03/kernel-config-extra
```

For nas7820, you could run `build.sh` in `nas7820-kernel` .

### 2.2 Build (In wrt350nv2-build-env docker)

You have a docker container started by `wrt350nv2-kernel/start.sh`, and you run `in.sh` in that dir, you get a shell of the docker container, which has ubuntu:12.04 env and a user `openwrt`.

The user & passwd are both `openwrt`, and has the sudo priviledge.

1. Before building, make sure the whole directory has the right permission(the patch before & dl may broke this).
```bash
# if suitable
tar xf dl.tar.gz
mv dl ws/path/to/backfire_10.03
# then
cd ws/path/to/backfire_10.03
sudo chown -R openwrt:openwrt .
```

2. Building
```bash
make -j8
# or verbose
make -j8 V=99
# or verbose & record
make -j12 V=99 2>&1 | tee klog
```

3. You should find the following files after building

```
# uImage for qemu
bin/orion/openwrt-wrt350nv2-uImage
# elf with debug info
build_dir/linux-orion_generic/vmlinux-debug-info.elf
# linux source code with patch
build_dir/linux-orion_generic/linux-2.6.32.10/
```

## 3. Build the working env (Using the container from docker image wrt350nv2-work-env:latest)

### 3.0 docker image

The docker image wrt350nv2-work-env:latest provides the basic building & working env.

But you may still need to manually compile & install the following packages if you need them:
- capstone (just compile)
- qemu (just compile)
- panda (self install the dependency)


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

### 4.1 Work Flow

```bash
# terminal 1
./panda-build/arm-softmmu/qemu-system-arm -nographic -machine versatilepb \
                                          -S -s ./openwrt-wrt350nv2-uImage

# terminal 2
gdb-multiarch
(gdb) file ws/path/to/backfire_10.03/build_dir/linux-orion_generic/vmlinux-debug-info.elf
(gdb) directory ws/path/to/backfire_10.03/build_dir/linux-orion_generic/linux-2.6.32.10/ 
(gdb) target remote localhost:1234
(gdb) ...
```

### 4.2 FAQ

- the target of `file` command should be `backfire_10.03/build_dir/linux-orion_generic/vmlinux-debug-info.elf`
- the target of `directory` command should be `backfire_10.03/build_dir/linux-orion_generic/linux-2.6.32.10`
