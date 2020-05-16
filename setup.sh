#!/bin/sh

install_python()
{
    # V1.V2.V3, e.g. 3.7.7
    V1=`python -V 2>&1 | awk '{print $2}' | awk -F '.' '{print $1}'`
    V2=`python -V 2>&1 | awk '{print $2}' | awk -F '.' '{print $2}'`
    V3=`python -V 2>&1 | awk '{print $2}' | awk -F '.' '{print $3}'`


    echo =========================================
    if [ ${V1} -lt 3 ]; then
        echo Python ${V1}.${V2}.${V3} is not satisfied
        echo Install Python 3.7
        sudo apt-get install -y software-properties-common && \
            add-apt-repository ppa:deadsnakes/ppa && apt-get update
        sudo apt-get install -y python3.7 python3-pip python3.7-dev
        sudo -H python3.7 -m pip install --upgrade pip && \
            sudo rm /usr/bin/python && \
            sudo ln -s /usr/bin/python3.7 /usr/bin/python
    else
        echo Python ${V1}.${V2}.${V3} is satisfied
    fi

    echo =========================================
    echo Install Python requirments
    sudo -H pip3.7 install qmp fdt capstone pydot graphviz
    $SALAMANDER_BUILD/pyqemulog/pyqemulog -h >/dev/null 2>&1 || \
        (git clone https://github.com/cyruscyliu/pyqemulog $SALAMANDER_BUILD/pyqemulog && \
        cd $SALAMANDER_BUILD/pyqemulog && sudo -H pip3.7 install . && cd $OLDPWD)
}

install_binwalk()
{
    echo =========================================
    echo Install Binwalk-2.1.1
    wget -nc https://github.com/ReFirmLabs/binwalk/archive/v2.1.1.tar.gz \
        -O $SALAMANDER_BUILD/v2.1.1.tar.gz
    tar --skip-old-files -zxf $SALAMANDER_BUILD/v2.1.1.tar.gz -C $SALAMANDER_BUILD && \
        cp -r ./externals/binwalk/* $SALAMANDER_BUILD/binwalk-2.1.1/src/ && \
    cd $SALAMANDER_BUILD/binwalk-2.1.1 && sudo python3.7 setup.py -q install && cd $OLDPWD

    sasquatch --version >/dev/null 2>&1 && \
        (sudo apt-get install -y zlib1g-dev liblzma-dev liblzo2-dev && \
        git clone https://github.com/devttys0/sasquatch $SALAMANDER_BUILD/sasquatch && \
        cd $SALAMANDER_BUILD/sasquatch && ./build.sh && cd $OLDPWD)
}

install_qemu()
{
    echo =========================================
    echo Install QEMU-4.0.0
    sudo apt-get install -y git libglib2.0-dev libfdt-dev libpixman-1-dev \
        zlib1g-dev bison flex libcapstone3 libcapstone-dev u-boot-tools \
        p7zip-full squashfs-tools device-tree-compiler gawk
    wget -nc https://download.qemu.org/qemu-4.0.0.tar.xz \
        -O $SALAMANDER_BUILD/qemu-4.0.0.tar.xz || true && \
    tar --skip-old-files -Jxf $SALAMANDER_BUILD/qemu-4.0.0.tar.xz -C $SALAMANDER_BUILD && \
    cp -r ./externals/qemu/* $SALAMANDER_BUILD/qemu-4.0.0/ && \
    cd $SALAMANDER_BUILD/qemu-4.0.0 && ./configure \
        --target-list=arm-softmmu,mips-softmmu,mipsel-softmmu && \
        # --enable-debug --extra-cflags="-g3" --extra-ldflags="-g3" \
        # --disable-strip --disable-pie \
        make -j4 && cd $OLDPWD
    echo $SALAMANDER_BUILD/qemu-4.0.0 > .qemu
}

install_sparse()
{
    echo =========================================
    echo Install sparse
    $SALAMANDER_BUILD/sparse/sparse --version >/dev/null 2>&1 || \
        git clone git://git.kernel.org/pub/scm/devel/sparse/sparse.git $SALAMANDER_BUILD/sparse && \
        cd $SALAMANDER_BUILD/sparse && make && cd $OLDPWD
    echo $SALAMANDER_BUILD/sparse > .sparse
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

mkdir -p ~/build
SALAMANDER_BUILD=~/build
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

install
