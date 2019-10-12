#!/bin/bash


#
# UTIL FUNCTIONS
#


get_kernel_files() {
    local kernel_files=
    local generic_platform_dir=
    local generic_files_dir=
    local files_dir=

    generic_platform_dir="${OPENWRT_DIR}/target/linux/generic"
    
    for dir in "${generic_platform_dir}/files" "${generic_platform_dir}/files-${KERNEL_PATCHVER}"
    do
        if [ -d "${dir}" ]
        then
            generic_files_dir="${generic_files_dir} ${dir}/*"
        fi
    done

    # TODO:
    # this FILES_DIR's definition hasn't strictly follow makefile
    if [ "${SUBTARGET}" != "" ]
    then
        subtarget_path="${OPENWRT_DIR}/target/linux/${BOARD}/${SUBTARGET}/files ${OPENWRT_DIR}/target/linux/${BOARD}/${SUBTARGET}/files-${KERNEL_PATCHVER}"
    fi
    for dir in  "${OPENWRT_DIR}/target/linux/${BOARD}/files" \
                "${OPENWRT_DIR}/target/linux/${BOARD}/files-${KERNEL_PATCHVER}" \
                ${subtarget_path}
    do
        if [ -d "${dir}" ]
        then
            files_dir="${files_dir} ${dir}/*"
        fi
    done

    kernel_files="${generic_files_dir} ${files_dir}"

    echo -n "${kernel_files}"
}

copy_part() {
    local kernel_files=

    rm -rf ${KERNEL_DIR}/patches && mkdir -p ${KERNEL_DIR}/patches

    kernel_files=`get_kernel_files`

    if [[ ! "${kernel_files}" =~ ^\ *$ ]]
    then
        cp -fpR ${kernel_files} ${KERNEL_DIR}
    fi

    find ${KERNEL_DIR}/ -name \*.rej -or -name \*.orig | xargs -r rm -f

}

patchdir_func() {
    # we only use quilt solution here as we can see QUILT will always be set
    local build_dir=$1
    local source=$2
    local dest=$3

    mkdir -p "${build_dir}/patches/${dest}"
    if [ -s "${source}/series" ]
    then
        mkdir -p "${build_dir}/patches/${dest}"
        cp "${source}/series" "${build_dir}/patches/${dest}"
    fi

    for patch in `cd ${source} && if [ -f series ]; then sed -e s,\\\#.*,, "${source}/series" | grep -E \[a-zA-Z0-9\]; else ls | sort; fi 2>/dev/null`
    do
        cp "${source}/${patch}" "${build_dir}/patches/${dest}"
        echo "${dest}/${patch}" >> "${build_dir}/patches/series"
    done

    [ -n "${dest}" ] && echo "${dest}" > "${build_dir}/patches/.subdirs"
}

patch_part() {
    local generic_platform_dir=
    local generic_patch_dir=
    local patch_dir=
    local subtarget_path=

    generic_platform_dir="${OPENWRT_DIR}/target/linux/generic"

    for dir in  "${generic_platform_dir}/patches-${KERNEL_PATCHVER}" \
                "${generic_platform_dir}/patches"
    do
        if [ -d "${dir}" ]
        then
            generic_patch_dir="${dir}"
            break
        fi
    done

    # TODO:
    # this FILES_DIR's definition hasn't strictly follow makefile
    [ "${SUBTARGET}" = "" ] && subtarget_path= || subtarget_path=${SUBTARGET}/
    for dir in  "${OPENWRT_DIR}/target/linux/${BOARD}/${subtarget_path}patches-${KERNEL_PATCHVER}" \
                "${OPENWRT_DIR}/target/linux/${BOARD}/${subtarget_path}patches" \
                "${OPENWRT_DIR}/target/linux/${BOARD}/patches-${KERNEL_PATCHVER}" \
                "${OPENWRT_DIR}/target/linux/${BOARD}/patches" 
    do
        if [ -d "${dir}" ]
        then
            patch_dir="${dir}"
            break
        fi
    done

    patchdir_func "${KERNEL_DIR}" "${generic_patch_dir}" generic
    patchdir_func "${KERNEL_DIR}" "${patch_dir}" platform

    if [ -s "${KERNEL_DIR}/patches/series" ]
    then
        cd ${KERNEL_DIR} 2>&1

        if quilt --quiltrc=- next >/dev/null 2>&1
        then
            quilt --quiltrc=- push -a
        else
            quilt --quiltrc=- top >/dev/null 2>&1
        fi

        cd - >/dev/null 2>&1
    fi
}


#
# EXPORTED FUNCTIONS
#


module_kernel_patch_do() {
    # TODO:
    # here only handles the downloaded kernel case
    copy_part
    patch_part
}

