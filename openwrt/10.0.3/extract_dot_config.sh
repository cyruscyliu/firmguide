#!/bin/bash

set -e

##################################################################
#
# Params should be passed in:
# 1. url for downloading openwrt.tar
# 2. url for downloading kernel.tar
# 3. url for downloading .config for openwrt
# 4. kernel detail version (like "2.6.32")
# 5. board info (like "orion")
# 6. subtarget info (like "")
# 7. output file name (the output file copy from final .config, 
#                      if use relative path, it will base on
#                      the working directory)
# 8. working directory (if not set, will use "./build" as default
#                       if default, will clean the ./build first
#                       if set, assume it is an empty or not-exist
#                       dir)
#
##################################################################

#
# Global Variable Needs to be inited
#

WORK_DIR=
PATCH_DIR=
OPENWRT_DIR=
KERNEL_DIR=
OUTPUT_FILE=

OPENWRT_CFG=

KERNEL_VER=
KERNEL_PATCHVER=

# can come from openwrt .config
BOARD=
# SUBTARGET:=$(strip $(foreach subdir,$(patsubst $(PLATFORM_DIR)/%/target.mk,%,$(wildcard $(PLATFORM_DIR)/*/target.mk)),$(if $(CONFIG_TARGET_$(call target_conf,$(BOARD)_$(subdir))),$(subdir))))
# target_conf=$(subst .,_,$(subst -,_,$(subst /,_,$(1))))
SUBTARGET=

# TODO: I don't know where this env comes from, maybe is set before the most outside make command of openwrt, now left it empty
SHARED_LINUX_CONFIG=


#
# Function
#

error() {
    printf "ERROR: %s" $1 && exit 1
}

fake-prepare() {
    # fake prepare for testing, take openwrt 10.03 & linux 2.6.32.10 as an exampe
    rm -rf ./build && mkdir ./build
    WORK_DIR=`realpath ./build`

    cp backfire_10.03_source.tar.bz2 linux-2.6.32.10.tar.xz OpenWrt.config ${WORK_DIR}
    cp -r patches ${WORK_DIR}

    cd ${WORK_DIR}
    tar xf backfire_10.03_source.tar.bz2 || error "unzip openwrt 10.03 error"
    tar xf linux-2.6.32.10.tar.xz || error "unzip kernel 2.6.32.10 error"
    cp OpenWrt.config backfire_10.03/.config

    PATCH_DIR="`realpath ${WORK_DIR}/patches`"
    OPENWRT_DIR="`realpath ${WORK_DIR}/backfire_10.03`"
    KERNEL_DIR="`realpath ${WORK_DIR}/linux-2.6.32.10`"
    OPENWRT_CFG="${OPENWRT_DIR}/.config"
    KERNEL_VER="2.6"
    KERNEL_PATCHVER="2.6.32"
    BOARD="orion"
    SUBTARGET=""
    SHARED_LINUX_CONFIG=""
}

prepare() {
    local openwrt_url="$1"
    local kernel_url="$2"
    local openwrt_cfg_url="$3"
    local kernel_version="$4"
    local board="$5"
    local subtarget="$6"
    local output_file="$7"
    local work_dir="$8"

    [ $# -lt 7 ] && error "Should pass 7 or 8 parameters to this script"
    [ $# -gt 8 ] && error "Should pass 7 or 8 parameters to this script"

    # set up env
    if [ -z "${work_dir}" ] 
    then
        rm -rf ./build && mkdir -p ./build
        WORK_DIR="`realpath ./build`"
    else
        mkdir -p ${work_dir}
        [ "`ls -A ${work_dir} | wc -l`" -ne 0 ] && error "param 8 work_dir '${work_dir}' not empty"
        WORK_DIR="`realpath ${work_dir}`"
    fi

    cp -r patches "${WORK_DIR}"
    PATCH_DIR="${WORK_DIR}/patches"

    cd ${WORK_DIR}

    wget ${openwrt_url} || error "could not download openwrt tar from '${openwrt_url}'"
    ls -t | head -n 1 | xargs tar --touch -xf || error "could not unzip openwrt tar"
    OPENWRT_DIR="`ls -t | head -n 1 | xargs realpath`"

    wget ${kernel_url} || error "could not download openwrt tar from '${kernel_url}'"
    ls -t | head -n 1 | xargs tar --touch -xf || error "could not unzip kernel tar"
    KERNEL_DIR="`ls -t | head -n 1 | xargs realpath`"

    wget ${openwrt_cfg_url} || error "could not download openwrt tar from '${openwrt_cfg_url}'"
    OPENWRT_CFG="`ls -t | head -n 1 | xargs realpath`"

    KERNEL_VER=`echo ${kernel_version} | awk -F"." '{printf("%s.%s", $1, $2);}'`

    KERNEL_PATCHVER=`echo ${kernel_version} | awk -F"." '{printf("%s.%s.%s", $1, $2, $3);}'`

    BOARD="${board}"

    [ "${subtarget}" != "NULL" ] && SUBTARGET="${subtarget}"

    OUTPUT_FILE="realpath ${output_file}"
}

gen_packageinfo() {
    cp ${PATCH_DIR}/include/toplevel.mk ${OPENWRT_DIR}/include

    cd ${OPENWRT_DIR} && make esv-prepare-tmpinfo || error "make esv-prepare-tmpinfo failed"
}

has_cfg() {
    grep "$1"=y "$2" >/dev/null 2>&1 && return 0 || return 1
}

set_cfg() {
    if has_cfg "$1" "${OPENWRT_CFG}" 
    then
        [ "$2" != "" ] && echo $5 "$2" >> $4 
    else
        [ "$3" != "" ] && echo $5 "$3" >> $4
    fi
}

get_generic_linux_config() {
    local generic_platform_dir=

    generic_platform_dir="${OPENWRT_DIR}/target/linux/generic-${KERNEL_VER}"

    for f in "${generic_platform_dir}/config-${KERNEL_PATCHVER}" \
             "${generic_platform_dir}/config-default" 
    do
        [ -f "$f" ] && echo "$f" && return 0
    done

    return 1
}

get_linux_config() {
    local platform_dir=
    local platform_subdir=

    platform_dir="${OPENWRT_DIR}/target/linux/${BOARD}"
    if [ "${SUBTARGET}" != "" ]
    then
        platform_subdir="${OPENWRT_DIR}/target/linux/${BOARD}/${SUBTARGET}"
    fi

    for f in "${platform_dir}/config-${KERNEL_PATCHVER}" \
             "${platform_dir}/config-default" \
             "${platform_subdir}/config-${KERNEL_PATCHVER}" \
             "${platform_subdir}/config-default" 
    do
        [ -f "$f" ] && echo "$f" && return 0
    done
    
    return 1
}

get_linux_subconfig() {
    local linux_config="$1"
    local platform_subdir=
    local linux_subconfig=
    
    [ -n "${SHARED_LINUX_CONFIG}" ] && return 1

    if [ "${SUBTARGET}" != "" ]
    then
        platform_subdir="${OPENWRT_DIR}/target/linux/${BOARD}/${SUBTARGET}"
    fi

    for f in "${platform_subdir}/config-${KERNEL_PATCHVER}" \
             "${platform_subdir}/config-default" 
    do
        [ -f "$f" ] && linux_subconfig="$f" && break
    done

    [ "${linux_subconfig}" = "${linux_config}" ] && return 1

    echo "${linux_subconfig}" && return 0
}

dot_config_generation() {
    local kconfig=${OPENWRT_DIR}/scripts/kconfig.pl
    local metadata=${OPENWRT_DIR}/scripts/metadata.pl
    local generic_linux_config=
    local linux_config=
    local linux_subconfig=
    local platform_cfg=
    local dir=${KERNEL_DIR}

    cd ${KERNEL_DIR}

    generic_linux_config=`get_generic_linux_config`
    linux_config=`get_linux_config`
    linux_subconfig=`get_linux_subconfig "${linux_config}"`

    if [ -z "${linux_subconfig}" ]
    then
        ${kconfig} + ${generic_linux_config} ${linux_config} > ${dir}/.config.target
    else
        ${kconfig} + ${generic_linux_config} + ${linux_config} ${linux_subconfig} > ${dir}/.config.target
    fi

    set_cfg "CONFIG_KERNEL_KALLSYMS" \
            "CONFIG_KALLSYMS=y" \
            "# CONFIG_KALLSYMS is not set" \
            ${dir}/.config.target

    set_cfg "CONFIG_KERNEL_PROFILING" \
            "CONFIG_PROFILING=y" \
            "# CONFIG_PROFILING is not set" \
            ${dir}/.config.target

    set_cfg "CONFIG_KERNEL_DEBUG_FS" \
            "CONFIG_DEBUG_FS=y" \
            "# CONFIG_DEBUG_FS is not set" \
            ${dir}/.config.target

    echo "# CONFIG_KALLSYMS_EXTRA_PASS is not set" \
        >> ${dir}/.config.target

    echo "# CONFIG_KALLSYMS_ALL is not set" \
        >> ${dir}/.config.target

    set_cfg "CONFIG_WHATEVER" \
            "# CONFIG_KPROBES is not set" \
            "# CONFIG_KPROBES is not set" \
            ${dir}/.config.target

    if has_cfg "CONFIG_EABI_SUPPORT" "${OPENWRT_CFG}"
    then
        sed -i -e 's,.*CONFIG_AEABI.*,CONFIG_AEABI=y,' ${dir}/.config.target
    else
        sed -i -e 's,.*CONFIG_AEABI.*,# CONFIG_AEABI is not set,' ${dir}/.config.target
    fi

    set_cfg "CONFIG_EABI_SUPPORT" \
            "# CONFIG_OABI_COMPAT is not set" \
            "" \
            ${dir}/.config.target

    ${metadata} kconfig ${OPENWRT_DIR}/tmp/.packageinfo ${OPENWRT_CFG} > ${dir}/.config.override
    ${kconfig} 'm+' '+' ${dir}/.config.target /dev/null ${dir}/.config.override > ${dir}/.config

    if [ "${KERNEL_VER}" = 2.6 ] 
    then
        if has_cfg "CONFIG_TARGET_ROOTFS_INITRAMFS" "${OPENWRT_CFG}" 
        then
            mv ${dir}/.config ${dir}/.config.old
            grep -v -e INITRAMFS -e CONFIG_RD_ -e CONFIG_BLK_DEV_INITRD ${dir}/.config.old > ${dir}/.config

            echo 'CONFIG_BLK_DEV_INITRD=y' >> ${dir}/.config

            # TODO: I don't know where this TARGET_DIR come from, we need to investigate more when we meet the firmware uses this config logic
            # INITRAMFS_EXTRA_FILES ?= $(GENERIC_PLATFORM_DIR)/image/initramfs-base-files.txt
            #echo 'CONFIG_INITRAMFS_SOURCE="$(strip $(TARGET_DIR) $(INITRAMFS_EXTRA_FILES))"' >> ${dir}/.config
            error "ERROR: meet a feature that is not fully supported"

            echo "CONFIG_INITRAMFS_ROOT_UID=`shell id -u`" >> ${dir}/.config

            echo "CONFIG_INITRAMFS_ROOT_GID=`shell id -g`" >> ${dir}/.config

            set_cfg "CONFIG_TARGET_INITRAMFS_COMPRESSION_NONE" \
                    "CONFIG_INITRAMFS_COMPRESSION_NONE=y" \
                    "# CONFIG_INITRAMFS_COMPRESSION_NONE is not set" \
                    ${dir}/.config

            set_cfg "CONFIG_TARGET_INITRAMFS_COMPRESSION_GZIP" \
                    "CONFIG_INITRAMFS_COMPRESSION_GZIP=y\nCONFIG_RD_GZIP=y" \
                    "# CONFIG_INITRAMFS_COMPRESSION_GZIP is not set\n# CONFIG_RD_GZIP is not set" \
                    ${dir}/.config -e

            set_cfg "CONFIG_TARGET_INITRAMFS_COMPRESSION_BZIP2" \
                    "CONFIG_INITRAMFS_COMPRESSION_BZIP2=y\nCONFIG_RD_BZIP2=y" \
                    "# CONFIG_INITRAMFS_COMPRESSION_BZIP2 is not set\n# CONFIG_RD_BZIP2 is not set" \
                    ${dir}/.config -e

            set_cfg "CONFIG_TARGET_INITRAMFS_COMPRESSION_LZMA" \
                    "CONFIG_INITRAMFS_COMPRESSION_LZMA=y\nCONFIG_RD_LZMA=y" \
                    "# CONFIG_INITRAMFS_COMPRESSION_LZMA is not set\n# CONFIG_RD_LZMA is not set" \
                    ${dir}/.config -e

            set_cfg "CONFIG_TARGET_INITRAMFS_COMPRESSION_LZO" \
                    "CONFIG_INITRAMFS_COMPRESSION_LZO=y\nCONFIG_RD_LZO=y" \
                    "# CONFIG_INITRAMFS_COMPRESSION_LZO is not set\n# CONFIG_RD_LZO is not set" \
                    ${dir}/.config -e
        else
            mv ${dir}/.config ${dir}/.config.old
            grep -v INITRAMFS ${dir}/.config.old > ${dir}/.config

            echo 'CONFIG_INITRAMFS_SOURCE=""' >> ${dir}/.config
        fi
    fi

    [ -f "${dir}/.config" ] || error "generate final kernel config file ${dir}/.config failed"
}

postprocess() {
    if [ -n "${OUTPUT_FILE}" ]
    then
        cp ${KERNEL_DIR}/.config ${OUTPUT_FILE}
    fi
}

get_dot_config() {
    # 1. prepare, like set variable & unzip kernel
    #fake-prepare "$@"
    prepare "$@"

    # 2. gen .packageinfo
    gen_packageinfo 

    # 3. .config generation flow
    dot_config_generation

    # 4. post process, like copy & rename the ouput to target place
    postprocess
}

main() {
    get_dot_config "$@"
}

#
# Run
#

main "$@"
