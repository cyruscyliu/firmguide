#!/usr/bin/env bash

# run this script in ./nas7820-kernel

cd ../ws
# download the package
DOWNLOAD_URL="https://github.com/openwrt/chaos_calmer/archive/v15.05.zip"
PACKAGE_NAME="v15.05.zip"
PACKAGE_DIR_NAME="chaos_calmer-15.05"
if [ ! -f $PACKAGE_NAME  ];then
    wget $DOWNLOAD_URL
    unzip $PACKAGE_NAME
    mv $PACKAGE_DIR_NAME chaos_camler_1505_oxnas
fi
if [ -d $PACKAGE_DIR_NAME ];then
    mv $PACKAGE_DIR_NAME chaos_camler_1505_oxnas
fi
# patch and config
target="./chaos_camler_1505_oxnas"
patch="../nas7820-kernel/patches"
cp "$patch/.config" "$target/.config"
cp "$patch/build.sh" "$target/build.sh"
cp "$patch/download.pl" "$target/scripts/download.pl"
cp "$patch/libjson-c.makefile" "$target/package/libs/libjson-c/Makefile"
cp "$patch/kernel-defaults.mk" "$target/include/kernel-defaults.mk"
cp "$patch/kernel-config-extra" "$target/kernel-config-extra"

cd ../nas7820-kernel
# build the docker
./build-docker-image.sh
# start the docker
./start.sh
# enter the docker
./in.sh $target/build.sh
