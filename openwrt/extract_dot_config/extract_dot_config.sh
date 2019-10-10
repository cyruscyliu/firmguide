#!/bin/bash

set -e


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

OUTPUT_FILE=


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
# 2. url for downloading openwrt.tar
# 3. url for downloading kernel.tar
# 4. url for downloading .config for openwrt
# 5. kernel detail version (like "2.6.32")
# 6. board info (like "orion")
# 7. subtarget info (string, but notice that pass "NULL" means "")
# 8. output file name (the output file copy from final .config, 
#                      if use relative path, it will base on
#                      the working directory)
# 9. working directory (if not set, will use "./build" as default
#                       if default, will clean the ./build first
#                       if set, assume it is an empty or not-exist
#                       dir)
#
##################################################################
"
    } && exit 1
}

error() {
    printf "ERROR: %s\n" "$1" && exit 1
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
    local output_file="$8"
    local work_dir="$9"

    # 1. setup openwrt version specific env
    if [ -d "${openwrt_ver}" ] 
    then
        . ${openwrt_ver}/extract-modules.sh
        OPENWRT_VER="${openwrt_ver}"
    else
        error "not supported openwrt version '${openwrt_ver}'"
    fi

    # 2. setup work dir
    if [ -z "${work_dir}" ] 
    then
        rm -rf ./build && mkdir -p ./build
        WORK_DIR="`realpath ./build`"
    else
        mkdir -p ${work_dir}
        [ "`ls -A ${work_dir} | wc -l`" -ne 0 ] && error "param 8 work_dir '${work_dir}' not empty"
        WORK_DIR="`realpath ${work_dir}`"
    fi

    # 3. setup patch env
    module_openwrt_patch_setup

    # 4. setup all the rest global variables
    cd ${WORK_DIR}

    wget --no-use-server-timestamps ${openwrt_url} || error "could not download openwrt tar from '${openwrt_url}'"
    ls -t | head -n 1 | xargs tar --touch -xf || error "could not unzip openwrt tar"
    OPENWRT_DIR="`ls -t | head -n 1 | xargs realpath`"

    wget --no-use-server-timestamps ${kernel_url} || error "could not download openwrt tar from '${kernel_url}'"
    ls -t | head -n 1 | xargs tar --touch -xf || error "could not unzip kernel tar"
    KERNEL_DIR="`ls -t | head -n 1 | xargs realpath`"

    wget --no-use-server-timestamps ${openwrt_cfg_url} || error "could not download openwrt tar from '${openwrt_cfg_url}'"
    OPENWRT_CFG="`ls -t | head -n 1 | xargs realpath`"

    KERNEL_VER=`echo ${kernel_version} | awk -F"." '{printf("%s.%s", $1, $2);}'`

    KERNEL_PATCHVER=`echo ${kernel_version} | awk -F"." '{printf("%s.%s.%s", $1, $2, $3);}'`

    BOARD="${board}"

    [ "${subtarget}" != "NULL" ] && SUBTARGET="${subtarget}"

    OUTPUT_FILE=`realpath ${output_file}`
}

gen_packageinfo() {
    module_openwrt_patch_do

    cd ${OPENWRT_DIR} && make esv-prepare-tmpinfo || error "make esv-prepare-tmpinfo failed"
}

dot_config_generation() {
    module_dot_config_generation
}

postprocess() {
    if [ -n "${OUTPUT_FILE}" ]
    then
        cp ${KERNEL_DIR}/.config ${OUTPUT_FILE}
    fi
}

get_dot_config() {
    # 1. prepare, like set variable & unzip kernel
    prepare "$@"

    # 2. gen .packageinfo
    gen_packageinfo 

    # 3. .config generation flow
    dot_config_generation

    # 4. post process, like copy & rename the ouput to target place
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
