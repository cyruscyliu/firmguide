#!/bin/bash


#
# Fixed Variables
#

DEFAULT_WORK_DIR=extract_tmp

#
# Global Variable Needs to be initialized
#

WORK_DIR=

# can come from openwrt .config
BOARD=
# SUBTARGET:=$(strip $(foreach subdir,$(patsubst $(PLATFORM_DIR)/%/target.mk,%,$(wildcard $(PLATFORM_DIR)/*/target.mk)),$(if $(CONFIG_TARGET_$(call target_conf,$(BOARD)_$(subdir))),$(subdir))))
# target_conf=$(subst .,_,$(subst -,_,$(subst /,_,$(1))))
SUBTARGET=
# TODO: I don't know where this env comes from, maybe is set before the most outside make command of openwrt, now left it empty
SHARED_LINUX_CONFIG=

OPENWRT_DIR=
OPENWRT_VER=
OPENWRT_CFG=

KERNEL_DIR=
KERNEL_VER=
KERNEL_PATCHVER=

PATCH_DIR=

OUTPUT_DIR=


#
# Util Functions
#

usage() {
    printf "ERROR: %s\n" "$1" && {
    echo "
##################################################################
#
# Params should be passed in:
# 1. openwrt version (like "10.0.3" or "15.05")
# 2. url for downloading or file path of openwrt.tar
# 3. url for downloading or file path of kernel.tar
# 4. url for downloading or file path of .config for openwrt
# 5. kernel detail version (like "2.6.32")
# 6. board info (like "orion")
# 7. subtarget info (string, but notice that pass "NULL" means '')
# 8. output directory (the final kernel source copy from work dir,
#                      if use relative path, it will base on
#                      the working directory;
#                      if pass "NULL", means '';)
# 9. working directory (if not set, will use "./${DEFAULT_WORK_DIR}"
#                       as default
#                       if default, will clean the ./${DEFAULT_WORK_DIR}
#                       first;
#                       NOTICE: will clean the target directory first)
#
##################################################################
"
    } && exit 1
}

error() {
    printf "ERROR: %s\n" "$1" && exit 1
}

latest() {
    cd "$1" > /dev/null 2>&1
    ls -At "$1" | head -n 1 | xargs realpath
    cd - > /dev/null 2>&1
}

#
# Function
#


prepare() {
    local openwrt_ver="$1"
    local openwrt_url="$2"
    local kernel_url="$3"
    local openwrt_cfg_url="$4"
    local kernel_version="$5"
    local board="$6"
    local subtarget="$7"
    local output_dir="$8"
    local work_dir="$9"

    # 1. setup openwrt version specific env
    if [ -d "${openwrt_ver}" ]
    then
        for sh in ${openwrt_ver}/*.sh
        do
            . ${sh}
        done
        OPENWRT_VER="${openwrt_ver}"
    else
        error "not supported openwrt version '${openwrt_ver}'"
    fi

    # 2. setup work dir
    if [ -z "${work_dir}" ]
    then
        rm -rf "${DEFAULT_WORK_DIR}" && mkdir -p "${DEFAULT_WORK_DIR}"
        WORK_DIR="`realpath ${DEFAULT_WORK_DIR}`"
    else
        mkdir -p ${work_dir}
        #[ "`ls -A ${work_dir} | wc -l`" -ne 0 ] && error "param 8 work_dir '${work_dir}' not empty"
        local path=`realpath ${work_dir}`
        [ -d "${path}" ] && rm -rf ${path}/* || error "the param 9 is weird, realpath of '${work_dir}' is ${path} which doesn't exist & cannot been created"
        WORK_DIR="${path}"
    fi

    # 3. setup patch env
    module_openwrt_patch_setup

    # 4. setup all the rest global variables
    if [[ "${openwrt_url}" =~ ^http[s]?://.*$ ]] || [[ "${openwrt_url}" =~ ^ftp://.*$ ]]
    then
        wget -P "${WORK_DIR}" --no-use-server-timestamps ${openwrt_url} || error "could not download openwrt tar from '${openwrt_url}'"
        latest "${WORK_DIR}" | xargs tar --touch -C "${WORK_DIR}" -xf || error "could not unzip openwrt tar"
    else
        cp "${openwrt_url}" "${WORK_DIR}" || error "could not make a copy of '${openwrt_url}' to work dir '${WORK_DIR}'"
        latest "${WORK_DIR}" | xargs tar --touch -C "${WORK_DIR}" -xf || error "could not unzip openwrt tar"
    fi
    OPENWRT_DIR="`latest ${WORK_DIR}`"

    if [[ "${kernel_url}" =~ ^http[s]?://.*$ ]] || [[ "${kernel_url}" =~ ^ftp://.*$ ]]
    then
        wget -P "${WORK_DIR}" --no-use-server-timestamps ${kernel_url} || error "could not download kernel tar from '${kernel_url}'"
        latest "${WORK_DIR}" | xargs tar --touch -C "${WORK_DIR}" -xf || error "could not unzip kernel tar"
    else
        cp "${kernel_url}" "${WORK_DIR}" || error "could not make a copy of '${kernel_url}' to work dir '${WORK_DIR}'"
        latest "${WORK_DIR}" | xargs tar --touch -C "${WORK_DIR}" -xf || error "could not unzip kernel tar"
    fi
    KERNEL_DIR="`latest ${WORK_DIR}`"

    if [[ "${openwrt_cfg_url}" =~ ^http[s]?://.*$ ]] || [[ "${openwrt_cfg_url}" =~ ^ftp://.*$ ]]
    then
        wget -P "${WORK_DIR}" --no-use-server-timestamps ${openwrt_cfg_url} || error "could not download openwrt config file from '${openwrt_cfg_url}'"
    else
        cp "${openwrt_cfg_url}" "${WORK_DIR}" || error "could not make a copy of '${openwrt_cfg_url}' to work dir '${WORK_DIR}'"
    fi
    OPENWRT_CFG="`latest ${WORK_DIR}`"

    module_openwrt_var_init "${kernel_version}" "${board}" "${subtarget}"

    if [ "${output_dir}" != "" ] && [ "${output_dir}" != "NULL" ]
    then
        OUTPUT_DIR=`realpath ${output_dir}`
    fi
}

gen_packageinfo() {
    module_openwrt_patch_do

    cd ${OPENWRT_DIR} && make esv-prepare-tmpinfo || error "make esv-prepare-tmpinfo failed"
}

dot_config_generation() {
    module_dot_config_generation
}

postprocess() {
    if [ -n "${OUTPUT_DIR}" ]
    then
        if [ "${KERNEL_DIR}" != "${OUTPUT_DIR}" ]
        then
            cp -r ${KERNEL_DIR} ${OUTPUT_DIR}
        fi
    fi
}

get_dot_config() {
    # 1. prepare, like set variable & unzip kernel
    prepare "$@"

    # 2. gen .packageinfo
    gen_packageinfo

    # 3. patch kernel source code
    module_kernel_patch_do

    # 4. .config generation flow
    dot_config_generation

    # 5. post process, like copy & rename the ouput to target place
    postprocess
}

main() {
    [ $# -lt 8 ] && usage "Should pass 8 or 9 parameters to this script"
    [ $# -gt 9 ] && usage "Should pass 8 or 9 parameters to this script"

    get_dot_config "$@"
}


#
# Run
#

main "$@"
