FROM ubuntu:18.04

# qemu build dep
RUN apt-get update
RUN apt-get install -y gcc g++ python pkg-config
RUN apt-get install -y git libglib2.0-dev libfdt-dev libpixman-1-dev zlib1g-dev
RUN apt-get install -y git-email
RUN apt-get install -y libaio-dev libbluetooth-dev libbrlapi-dev libbz2-dev
RUN apt-get install -y libcap-dev libcap-ng-dev libcurl4-gnutls-dev libgtk-3-dev
RUN apt-get install -y libibverbs-dev libjpeg8-dev libncurses5-dev libnuma-dev
RUN apt-get install -y librbd-dev librdmacm-dev
RUN apt-get install -y libsasl2-dev libsdl1.2-dev libseccomp-dev libsnappy-dev libssh2-1-dev
#RUN apt-get install -y libvde-dev libvdeplug-dev libvte-2.90-dev libxen-dev liblzo2-dev
RUN apt-get install -y libvde-dev libvdeplug-dev libxen-dev liblzo2-dev
RUN apt-get install -y valgrind xfslibs-dev
RUN apt-get install -y libnfs-dev libiscsi-dev

# part of the panda build dep
RUN apt-get install -y sudo lsb-release software-properties-common
COPY sources.list /etc/apt/sources.list
RUN apt-get update
RUN add-apt-repository ppa:ubuntu-toolchain-r/test
RUN apt-get update
RUN apt install -y gcc-6 g++-6
RUN update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-6 90 --slave /usr/bin/g++ g++ /usr/bin/g++-6
RUN update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-7 80 --slave /usr/bin/g++ g++ /usr/bin/g++-7

# qemu remote dbg
RUN apt-get install -y gdb-multiarch
