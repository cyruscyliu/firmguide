#!/bin/bash

PATCH_DIR=
OPENWRT_DIR=
KERNEL_DIR=
OPENWRT_CFG=
KERNEL_VER=
KERNEL_PATCHVER=
BOARD=

error() {
    printf "ERROR: %s" $1 && exit 1
}

gen_packageinfo() {
    cp ${PATCH_DIR}/include/toplevel.mk ${OPENWRT_DIR}/include

    cd ${OPENWRT_DIR}
    make esv-prepare-tmpinfo

    if [ $? -ne 0 ]
    then
        error "make esv-prepare-tmpinfo failed"
    fi
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

get_generic_cfg() {
    for f in "${OPENWRT_DIR}/target/linux/generic-${KERNEL_VER}/config-${KERNEL_PATCHVER}" \
             "${OPENWRT_DIR}/target/linux/generic-${KERNEL_VER}/config-default" 
    do
        [ -f "$f" ] && echo "$f" && return
    done
}

get_platform_cfg() {
    # TODO: this logic may not be 100% as the original one
    # TODO: not finished yet
    local conf=
    local subconf=

    for f in "${OPENWRT_DIR}/target/linux/${BOARD}/config-${KERNEL_PATCHVER}" \
             "${OPENWRT_DIR}/target/linux/${BOARD}/config-default" 
    do
        [ -f "$f" ] && echo "$f" && return
    done
}

dot_config_generation() {
    local kconfig=${OPENWRT_DIR}/scripts/kconfig.pl
    local metadata=${OPENWRT_DIR}/scripts/metadata.pl
    local generic_cfg=
    local platform_cfg=
    local dir=${KERNEL_DIR}

    generic_cfg=``
    platform_cfg=``

    cd ${KERNEL_DIR}
    ${kconfig} + ${generic_cfg} ${platform_cfg} > ${dir}/.config.target

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

            # TODO: for TARGET_DIR, we need to investigate more when we meet about this kind of firmware
            # INITRAMFS_EXTRA_FILES ?= $(GENERIC_PLATFORM_DIR)/image/initramfs-base-files.txt
            #echo 'CONFIG_INITRAMFS_SOURCE="$(strip $(TARGET_DIR) $(INITRAMFS_EXTRA_FILES))"' >> ${dir}/.config
            echo "ERROR: meet a feature that is not fully supported" && exit 1

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
    local KERNEL_DIR=

    # 1. unzip kernel

    # 2. gen .packageinfo
    gen_packageinfo 

    # 3. .config generation flow
    dot_config_generation
}

main() {
    get_dot_config "$@"
}

main "$@"
