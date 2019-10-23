#!/bin/bash

openwrt_ver=10.0.3
openwrt_url="http://archive.openwrt.org/backfire/10.03/backfire_10.03_source.tar.bz2"
kernel_url="https://mirrors.edge.kernel.org/pub/linux/kernel/v2.6/linux-2.6.32.10.tar.bz2"
openwrt_cfg_url="http://archive.openwrt.org/backfire/10.03/orion/OpenWrt.config"
kernel_version="2.6.32.10"
board="orion"
subtarget="NULL"
output_dir="NULL"
work_dir=""

bash extract_kernel.sh "${openwrt_ver}" "${openwrt_url}" "${kernel_url}" "${openwrt_cfg_url}" "${kernel_version}" "${board}" "${subtarget}" "${output_dir}" "${work_dir}"

