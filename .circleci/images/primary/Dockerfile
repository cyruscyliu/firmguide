FROM ubuntu:16.04

RUN apt-get update && apt-get install -y git libglib2.0-dev libfdt-dev libpixman-1-dev zlib1g-dev && \
apt-get install -y libaio-dev libbluetooth-dev libbrlapi-dev libbz2-dev && \
apt-get install -y libcap-dev libcap-ng-dev libcurl4-gnutls-dev libgtk-3-dev && \
apt-get install -y libibverbs-dev libjpeg8-dev libncurses5-dev libnuma-dev && \
apt-get install -y librbd-dev librdmacm-dev && \
apt-get install -y libsasl2-dev libsdl1.2-dev libseccomp-dev libsnappy-dev libssh2-1-dev && \
apt-get install -y valgrind xfslibs-dev && \
apt-get install -y libnfs-dev libiscsi-dev && \
apt-get install -y bison flex && \
apt-get install -y libcapstone3 libcapstone-dev && \
apt-get install -y u-boot-tools && \
apt-get install -y gawk && \
apt-get install -y software-properties-common

RUN add-apt-repository ppa:deadsnakes/ppa && apt-get update && \
apt-get install -y python3.7 && apt-get install -y python3-pip && python3.7 -m pip install --upgrade pip==19.2.3

RUN rm /usr/bin/python && ln -s /usr/bin/python3.7 /usr/bin/python

WORKDIR /root

RUN git config --global user.email "you@example.com" && git config --global user.name "Your Name" && \
apt-get install -y sudo

RUN pip3.7 install qmp pyyaml fdt fuzzywuzzy networkx pyquery prettytable
