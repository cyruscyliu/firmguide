#!/usr/bin/env bash

# run this script in ./nas7820-kernel

cd ../ws
# download the package
wget https://archive.openwrt.org/chaos_calmer/15.05/oxnas/generic/OpenWrt-ImageBuilder-15.05-oxnas.Linux-x86_64.tar.bz2
tar jxvf OpenWrt-ImageBuilder-15.05-oxnas.Linux-x86_64.tar.bz2
# then, you will get uncompressed OpenWrt-ImageBuilder-15.05-oxnas.Linux-x86_64

# patch and config
target="./OpenWrt-ImageBuilder-15.05-oxnas.Linux-x86_64"
patch="../nas7820-kernel/patches"
cp "$patch/download.pl" "$target/scripts/download.pl"
cp "$patch/kernel-defaults.mk" "$target/include/kernel-defaults.mk"
cp "$patch/kernel-config-extra" "$target/kernel-config-extra"

cd ../nas7820-kernel
# build the docker
chmod +x build-docker-image.sh
./build-docker-image.sh
# start the docker
chmod +x start.sh
./start.sh
# enter the docker
chmod +x in.h
./in.sh

# update the packages
cd "$target"





