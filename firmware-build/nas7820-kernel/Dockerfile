FROM ubuntu:14.04

# add nas7820 build deps
RUN apt-get update
RUN apt-get install -y libssl-dev zlib1g-dev autotools-dev zip automake gcc \
    g++ sudo vim wget build-essential subversion git-core libncurses5-dev zlib1g-dev \
    gawk flex quilt libssl-dev xsltproc libxml-parser-perl mercurial bzr ecj cvs unzip \
    mercurial ccache gettext

# add a user "openwrt" as it is suggested to build as non-root
RUN useradd -md /home/openwrt openwrt 
RUN echo 'openwrt:openwrt' | chpasswd
RUN usermod -aG sudo openwrt
RUN mkdir -p /root/firmware
RUN chown -R openwrt:openwrt /root
USER openwrt
