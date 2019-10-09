#!/bin/bash

#
# Inputs Variable
#

PATCH_DIR=
OPENWRT_DIR=
KERNEL_DIR=

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
        ${kconfig} + ${generic_cfg} ${linux_config} > ${dir}/.config.target
    else
        ${kconfig} + ${generic_cfg} + ${linux_config} ${linux_subconfig} > ${dir}/.config.target
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
}

get_dot_config() {
    # 1. unzip kernel
    # TODO: interface with outside

    # 2. gen .packageinfo
    gen_packageinfo 

    # 3. .config generation flow
    dot_config_generation
}

main() {
    get_dot_config "$@"
}

#
# Run
#

main "$@"
