#!/bin/bash


#
# UTIL FUNCTIONS
#

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


#
# EXPORTED FUNCTIONS
#


module_openwrt_var_init() {
    local kernel_version=$1
    local board=$2
    local subtarget=$3

    KERNEL_VER=`echo ${kernel_version} | awk -F"." '{printf("%s.%s", $1, $2);}'`

    KERNEL_PATCHVER=`echo ${kernel_version} | awk -F"." '{printf("%s.%s.%s", $1, $2, $3);}'`

    BOARD="${board}"

    [ "${subtarget}" != "NULL" ] && SUBTARGET="${subtarget}" || SUBTARGET=""
}

module_openwrt_patch_setup() {
    cp -r ${OPENWRT_VER}/patches "${WORK_DIR}"
    PATCH_DIR="${WORK_DIR}/patches"
}

module_openwrt_patch_do() {
    cp ${PATCH_DIR}/include/toplevel.mk ${OPENWRT_DIR}/include
}

module_dot_config_generation() {
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

    # TODO: fix the LINUX_CONF_CMD
    if [ -z "${linux_subconfig}" ]
    then
        ${kconfig} + ${generic_linux_config} ${linux_config} > ${dir}/.config.target
    else
        ${kconfig} + ${generic_linux_config} + ${linux_config} ${linux_subconfig} > ${dir}/.config.target
    fi

    awk '/^(#[[:space:]]+)?CONFIG_KERNEL/{sub("CONFIG_KERNEL_","CONFIG_");print}' ${OPENWRT_CFG} >> ${dir}/.config.target

    echo "# CONFIG_KALLSYMS_EXTRA_PASS is not set" \
        >> ${dir}/.config.target

    echo "# CONFIG_KALLSYMS_ALL is not set" \
        >> ${dir}/.config.target

    echo "# CONFIG_KALLSYMS_UNCOMPRESSED is not set" \
        >> ${dir}/.config.target

    ${metadata} kconfig ${OPENWRT_DIR}/tmp/.packageinfo ${OPENWRT_CFG} ${KERNEL_PATCHVER} > ${dir}/.config.override

    ${kconfig} 'm+' '+' ${dir}/.config.target /dev/null ${dir}/.config.override > ${dir}/.config

    if has_cfg "CONFIG_TARGET_ROOTFS_INITRAMFS" "${OPENWRT_CFG}"
    then
        # WITH INITRAMFS
        mv ${dir}/.config ${dir}/.config.old

        # TODO: investigate more when we meet this kind of firmware
        error "ERROR: meet a feature that is not fully supported"

        if has_cfg "CONFIG_EXTERNAL_CPIO" "${OPENWRT_CFG}"
        then
            grep -v INITRAMFS ${dir}/.config.old > ${dir}/.config
            #echo 'CONFIG_INITRAMFS_SOURCE="$(call qstrip,$(CONFIG_EXTERNAL_CPIO))"' >> ${dir}/.config
        else
            grep -v -e INITRAMFS -e CONFIG_RD_ -e CONFIG_BLK_DEV_INITRD ${dir}/.config.old > ${dir}/.config
            echo 'CONFIG_BLK_DEV_INITRD=y' >> ${dir}/.config
            #echo 'CONFIG_INITRAMFS_SOURCE="$(strip $(TARGET_DIR) $(INITRAMFS_EXTRA_FILES))"' >> $(LINUX_DIR)/.config
        fi

        # TODO: Maybe this 2 kernel config need more investigation?
        # I briefly serach the related, seems harmless to set it like this
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

        set_cfg "CONFIG_TARGET_INITRAMFS_COMPRESSION_XZ" \
                "CONFIG_INITRAMFS_COMPRESSION_XZ=y\nCONFIG_RD_XZ=y" \
                "# CONFIG_INITRAMFS_COMPRESSION_XZ is not set\n# CONFIG_RD_XZ is not set" \
                ${dir}/.config -e

        set_cfg "CONFIG_TARGET_INITRAMFS_COMPRESSION_LZ4" \
                "CONFIG_INITRAMFS_COMPRESSION_LZ4=y\nCONFIG_RD_LZ4=y" \
                "# CONFIG_INITRAMFS_COMPRESSION_LZ4 is not set\n# CONFIG_RD_LZ4 is not set" \
                ${dir}/.config -e
    else
        # WITHOUT INITRAMFS
        mv ${dir}/.config ${dir}/.config.old

        grep -v INITRAMFS ${dir}/.config.old > ${dir}/.config

        echo 'CONFIG_INITRAMFS_SOURCE=""' >> ${dir}/.config
    fi

    [ -f "${dir}/.config" ] || error "generate final kernel config file ${dir}/.config failed"
}

