#!/bin/sh

install_python()
{
    python -V >/dev/null 2>&1 && PYTHON_VERSION=`python -V | awk '{print $2}'`
    python3 -V >/dev/null 2>&1 && PYTHON3_VERSION=`python3 -V | awk '{print $2}'`

    if [ ! ${PYTHON_VERSION} ]; then
        if [ ! ${PYTHON3_VERSION} ]; then
            echo [-] Python or Python3 doesn\'t exist
            INSTALL_PYTHON=1
        else
            ln -sf `which python3` /usr/bin/python >/dev/null 2>&1 || \
                echo [-] Please sudo to create system symbolic link && exit
        fi
    fi

    V1=`python -V 2>&1 | awk '{print $2}' | awk -F '.' '{print $1}'`
    V2=`python -V 2>&1 | awk '{print $2}' | awk -F '.' '{print $2}'`
    if [ ${V1} -lt 3 ]; then
        INSTALL_PYTHON=1
    else
        if [ ${V2} -lt 6 ]; then
            INSTALL_PYTHON=1
        else
            echo Python3 is satisfied
            echo =========================================
	    INSTALL_PYTHON=0
        fi
    fi

    if [ ${INSTALL_PYTHON} -eq 1 ]; then
        echo Install Python 3
        echo =========================================
        apt-get update && apt-get install -y python3.6 && \
            ln -sf `which python3.6` /usr/bin/python >/dev/null 2>&1
    fi

    install_python_requirments
}

install_python_requirments()
{
    echo Install Python requirments
    echo =========================================
    apt-get install -y python3-pip && \
        python -m pip install --upgrade pip && \
        ln -sf `which pip${V1}.${V2}` /usr/bin/pip >/dev/null 2>&1 && \
        pip install --upgrade pip
    pip install qmp fdt capstone pydot graphviz pyyaml
    $/tmp/pyqemulog/pyqemulog -h >/dev/null 2>&1 || \
        (rm -rf /tmp/pyqemulog && git clone https://github.com/cyruscyliu/pyqemulog /tmp/pyqemulog && \
        cd /tmp/pyqemulog && pip install . && cd $OLDPWD)
    echo Done
}

install_binwalk()
{
    echo Install Binwalk-2.1.1
    echo =========================================

    python -V >/dev/null 2>&1 && PYTHON_VERSION=`python -V | awk '{print $2}'`
    if [ ! ${PYTHON_VERSION} ]; then
        echo [-] Please setup Python first && exit
    else
        V1=`python -V 2>&1 | awk '{print $2}' | awk -F '.' '{print $1}'`
        if [ ${V1} -lt 3 ]; then
            echo [-] Please setup Python first && exit
        fi
    fi

    wget -qnc https://github.com/ReFirmLabs/binwalk/archive/v2.1.1.tar.gz \
        -O /tmp/v2.1.1.tar.gz
    tar --skip-old-files -zxf /tmp/v2.1.1.tar.gz -C /tmp && \
        cp -r ./externals/binwalk/* /tmp/binwalk-2.1.1/src/ && \
    cd /tmp/binwalk-2.1.1 && python setup.py -q install && cd $OLDPWD

    install_binwalk_dependency
    echo Done
}


install_binwalk_dependency()
{
    sasquatch --version >/dev/null 2>&1 && \
        (apt-get install -y zlib1g-dev liblzma-dev liblzo2-dev && \
        git clone https://github.com/devttys0/sasquatch /tmp/sasquatch && \
        cd /tmp/sasquatch && ./build.sh && cd $OLDPWD)
}

install_qemu()
{
    echo Install QEMU-4.0.0
    echo =========================================
    apt-get install -y git libglib2.0-dev libfdt-dev libpixman-1-dev \
        zlib1g-dev bison flex libcapstone3 libcapstone-dev u-boot-tools \
        p7zip-full squashfs-tools device-tree-compiler gawk
    wget -nc https://download.qemu.org/qemu-4.0.0.tar.xz \
        -O $SALAMANDER_BUILD/qemu-4.0.0.tar.xz || true && \
    tar --skip-old-files -Jxf $SALAMANDER_BUILD/qemu-4.0.0.tar.xz -C $SALAMANDER_BUILD && \
    cp -rL --remove-destination ./externals/qemu/* $SALAMANDER_BUILD/qemu-4.0.0/ && \
    cd $SALAMANDER_BUILD/qemu-4.0.0 && ./configure \
        --target-list=arm-softmmu,mips-softmmu,mipsel-softmmu \
        --enable-autoboard \
        --enable-debug --extra-cflags="-g3" --extra-ldflags="-g3" \
        --disable-strip --disable-pie \
        && \
        make -j4 && cd $OLDPWD
    echo $SALAMANDER_BUILD/qemu-4.0.0 > .qemu
    echo Done
}

install_sparse()
{
    echo Install sparse
    echo =========================================
    $SALAMANDER_BUILD/sparse/sparse --version >/dev/null 2>&1 || \
        git clone git://git.kernel.org/pub/scm/devel/sparse/sparse.git $SALAMANDER_BUILD/sparse
    cp -rL --remove-destination ./externals/sparse/* $SALAMANDER_BUILD/sparse/ && \
        cd $SALAMANDER_BUILD/sparse && make && cd $OLDPWD
    echo $SALAMANDER_BUILD/sparse > .sparse
    echo $SALAMANDER_BUILD/traverse> .traverse
    echo Done
}

install_llvm()
{
    echo =========================================
    llvm-link-9 --version >/dev/null 2>&1 && echo LLVM-9 is installed
    llvm-link-9 --version >/dev/null 2>&1 || (echo Install LLVM-9 && \
        cd $SALAMANDER_BUILD && mkdir -p llvm-9 && \
        sudo apt-get update && sudo apt-get install -y \
        build-essential wget lsb-core software-properties-common vim && \
        sudo wget https://apt.llvm.org/llvm.sh && sudo chmod +x llvm.sh && \
        sudo ./llvm.sh 9 && \
        ln -s /usr/bin/clang-9 $SALAMANDER_BUILD/llvm-9/clang && \
        ln -s /usr/bin/llvm-link-9 $SALAMANDER_BUILD/llvm-9/llvm-link && \
        ln -s /usr/bin/opt-9 $SALAMANDER_BUILD/llvm-9/opt && \
        cd $OLDPWD)
    echo $SALAMANDER_BUILD/llvm-9 > .llvmbin
    echo Done
}

install()
{
    install_python
    install_binwalk
    install_qemu
    install_sparse
    install_llvm
}

usage()
{
    echo "usage: $0 [hpbqsl]"
    echo ""
    echo "optional arguments:"
    echo "  -h     show this help message and exit"
    echo "  -a     install all below by default"
    echo "  -p     install Python 3.7"
    echo "  -b     install Binwalk 2.1.1"
    echo "  -q     install QEMU 4.0.0"
    echo "  -s     install sparse 0.9"
    echo "  -l     install LLVM 9.0"
}

mkdir -p ~/build-latest
SALAMANDER_BUILD=~/build-latest
export BUILD_DIR

while getopts "pbqslah" opt; do
    case $opt in
        p) install_python && exit;;
        b) install_binwalk && exit ;;
        q) install_qemu && exit;;
        s) install_sparse && exit;;
        l) install_llvm && exit;;
        h) usage && exit ;;
        a) install && exit ;;
        *) usage && exit ;;
    esac
done
