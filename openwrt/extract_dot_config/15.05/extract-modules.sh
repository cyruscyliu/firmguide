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

find_kernel_config() {
    local dir=$1
    local __config_list=
    local __config_name_list=

    __config_name_list="${dir}/config-${KERNEL_PATCHVER} ${dir}/config-default"
    for f in ${__config_name_list}
    do 
        if [ -f "$f" ]
        then
            __config_list="$f"
            break
        fi
    done

    echo -n ${__config_list}
}

get_generic_linux_config() {
    local generic_linux_config=
    local generic_platform_dir=

    generic_platform_dir="${OPENWRT_DIR}/target/linux/generic"
    generic_linux_config=`find_kernel_config $generic_platform_dir`

    echo -n $generic_linux_config
}

get_linux_target_config() {
    local linux_target_config=
    local platform_dir=

    platform_dir="${OPENWRT_DIR}/target/linux/${BOARD}"
    linux_target_config=`find_kernel_config $platform_dir`

    echo -n $linux_target_config
}

get_linux_subtarget_config() {
    local linux_subtarget_config=
    local platform_subdir=

    if [ "${SUBTARGET}" != "" ]
    then
        platform_subdir="${OPENWRT_DIR}/target/linux/${BOARD}/${SUBTARGET}"
        linux_subtarget_config=`find_kernel_config $platform_subdir`
    fi

    echo -n $linux_subtarget_config
}

get_kernel_kconfig_list() {
    local kconfig_list=

    kconfig_list="${kconfig_list} `get_generic_linux_config`"
    kconfig_list="${kconfig_list} `get_linux_target_config`"
    kconfig_list="${kconfig_list} `get_linux_subtarget_config`"

    if [ -f ${OPENWRT_DIR}/env/kernel-config ]
    then
        kconfig_list="${kconfig_list} ${OPENWRT_DIR}/env/kernel-config"
    fi

    echo -n $kconfig_list
}

get_config_cmd() {
    local kernel_kconfig_list=
    local config_cmd=

    kernel_kconfig_list=`get_kernel_kconfig_list`

    config_cmd=`echo -n ${kernel_kconfig_list} | awk -F' ' 'END{for (i=1; i<NF; i++) {printf("%s ", "+");} printf("%s", $0)}'`

    echo -n $config_cmd
}


#
# EXPORTED FUNCTIONS
#


module_openwrt_var_init() {
    local kernel_version=$1
    local board=$2
    local subtarget=$3

    KERNEL_VER=`echo ${kernel_version} | awk -F"." '{printf("%s.%s", $1, $2);}'`

    KERNEL_PATCHVER=${KERNEL_VER}

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
    local dir=${KERNEL_DIR}

    cd ${KERNEL_DIR}

    ${kconfig} `get_config_cmd` > ${dir}/.config.target

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

