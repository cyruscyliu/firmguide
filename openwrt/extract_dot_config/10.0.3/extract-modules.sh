#!/bin/bash


#
# EXPORTED FUNCTIONS
#

module_openwrt_patch_setup() {
    cp -r ${OPENWRT_VER}/patches "${WORK_DIR}"
    PATCH_DIR="${WORK_DIR}/patches"
}

module_openwrt_patch_do() {
    cp ${PATCH_DIR}/include/toplevel.mk ${OPENWRT_DIR}/include
}

