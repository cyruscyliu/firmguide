#!/bin/bash

REQUIRED_UTILS="wget tar python3.8"
APTCMD="apt-get"
YUMCMD="yum"
APT_CANDIDATES="git build-essential libqt4-opengl mtd-utils gzip bzip2 tar arj lhasa p7zip p7zip-full cabextract cramfsprogs cramfsswap squashfs-tools zlib1g-dev liblzma-dev liblzo2-dev sleuthkit"
PYTHON2_APT_CANDIDATES="python-lzo python-lzma python-pip python-opengl python-qt4 python-qt4-gl python-numpy python-scipy"
PYTHON3_APT_CANDIDATES="python3-pip python3-opengl python3-pyqt4 python3-pyqt4.qtopengl python3-numpy python3-scipy"
PYTHON3_YUM_CANDIDATES=""
YUM_CANDIDATES="git gcc gcc-c++ make openssl-devel qtwebkit-devel qt-devel gzip bzip2 tar arj p7zip p7zip-plugins cabextract squashfs-tools zlib zlib-devel lzo lzo-devel xz xz-compat-libs xz-libs xz-devel xz-lzma-compat python-backports-lzma lzip pyliblzma perl-Compress-Raw-Lzma"
PYTHON2_YUM_CANDIDATES="python-pip python-opengl python-qt4 numpy python-numdisplay numpy-2f python-Bottleneck scipy"
APT_CANDIDATES="$APT_CANDIDATES $PYTHON2_APT_CANDIDATES"
YUM_CANDIDATES="$YUM_CANDIDATES $PYTHON2_YUM_CANDIDATES"
PIP_COMMANDS="pip3.8"
PYTHON_COMMANDS="python3.8"

# Check for root privileges
if [ $UID -eq 0 ]
then
    SUDO=""
else
    SUDO="sudo"
    REQUIRED_UTILS="sudo $REQUIRED_UTILS"
fi

function install_sasquatch
{
    git clone https://github.com/devttys0/sasquatch
    (cd sasquatch && ./build.sh)
    $SUDO rm -rf sasquatch
}

function install_jefferson
{
    $SUDO $PIP_COMMANDS install cstruct
    git clone https://github.com/sviehb/jefferson
    (cd jefferson && $SUDO $PYTHON_COMMANDS setup.py install)
    $SUDO rm -rf jefferson
}

function install_pip_package
{
    PACKAGE="$1"

    for PIP_COMMAND in $PIP_COMMANDS
    do
        $SUDO $PIP_COMMAND install $PACKAGE
    done
}

function find_path
{
    FILE_NAME="$1"

    echo -ne "checking for $FILE_NAME..."
    which $FILE_NAME > /dev/null
    if [ $? -eq 0 ]
    then
        echo "yes"
        return 0
    else
        echo "no"
        return 1
    fi
}

# Check to make sure we have all the required utilities installed
NEEDED_UTILS=""
for UTIL in $REQUIRED_UTILS
do
    find_path $UTIL
    if [ $? -eq 1 ]
    then
        NEEDED_UTILS="$NEEDED_UTILS $UTIL"
    fi
done

# Check for supported package managers and set the PKG_* envars appropriately
find_path $APTCMD
if [ $? -eq 1 ]
then
    find_path $YUMCMD
    if [ $? -eq 1 ]
    then
        NEEDED_UTILS="$NEEDED_UTILS $APTCMD/$YUMCMD"
    else
        PKGCMD="$YUMCMD"
        PKGCMD_OPTS="-y install"
        PKG_CANDIDATES="$YUM_CANDIDATES"
        PKG_PYTHON3_CANDIDATES="$PYTHON3_YUM_CANDIDATES"
    fi
else
    PKGCMD="$APTCMD"
    PKGCMD_OPTS="install -y"
    PKG_CANDIDATES="$APT_CANDIDATES"
    PKG_PYTHON3_CANDIDATES="$PYTHON3_APT_CANDIDATES"
fi

if [ "$NEEDED_UTILS" != "" ]
then
    echo "Please install the following required utilities: $NEEDED_UTILS"
    exit 1
fi

# Do the install(s)
cd /tmp
sudo $PKGCMD $PKGCMD_OPTS $PKG_CANDIDTES
install_pip_package pyqtgraph
install_pip_package capstone
install_pip_package ubi_reader
install_sasquatch
install_jefferson

