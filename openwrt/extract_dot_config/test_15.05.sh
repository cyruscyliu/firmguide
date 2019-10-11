#!/bin/bash

openwrt_ver=15.05
openwrt_url="https://github.com/openwrt/chaos_calmer/archive/v15.05.tar.gz"
#openwrt_url="/root/zhangcen/workspace/zju-iot-emulator/ws/wrt320nv1/v15.05.tar.gz"
kernel_url="https://cdn.kernel.org/pub/linux/kernel/v3.0/linux-3.18.20.tar.gz" 
#kernel_url="/root/zhangcen/workspace/zju-iot-emulator/ws/wrt320nv1/chaos_calmer-15.05/dl/linux-3.18.20.tar.xz"
openwrt_cfg_url="/root/zhangcen/workspace/zju-iot-emulator/ws/wrt320nv1/OpenWrt-ImageBuilder-15.05-brcm47xx-mips74k.Linux-x86_64/.config"
kernel_version="3.18.20"
board="brcm47xx"
subtarget="mips74k"
output_dir="NULL"
work_dir=""

bash extract_dot_config.sh "${openwrt_ver}" "${openwrt_url}" "${kernel_url}" "${openwrt_cfg_url}" "${kernel_version}" "${board}" "${subtarget}" "${output_dir}" "${work_dir}"

