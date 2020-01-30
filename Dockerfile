FROM ubuntu:16.04

# install python3.7
RUN apt-get install -y software-properties-common && \
add-apt-repository ppa:deadsnakes/ppa && apt-get update && \
apt-get install -y python3.7 python3-pip python3.7-dev && \
python3.7 -m pip install --upgrade pip

# install required packages
RUN pip3.7 install qmp pyyaml fdt fuzzywuzzy networkx pyquery prettytable capstone python-Levenshtein z3-solver && \
git clone https://github.com/cyruscyliu/pyqemulog ~/pyqemulog && cd ~/pyqemulog && pip3.7 install . && \
git clone https://github.com/cyruscyliu/pymake.git ~/pymake && cd ~/pymake && pip3.7 install .

# install QEMU/BINWALK etc.
RUN apt-get install -y git libglib2.0-dev libfdt-dev libpixman-1-dev zlib1g-dev wget sudo bison flex libcapstone3 libcapstone-dev u-boot-tools p7zip-full squashfs-tools device-tree-compiler gawk
RUN git clone https://github.com/cyruscyliu/esv.git salamander && cd salamander && mkdir log && mkdir ~/build
RUN wget -nc https://github.com/ReFirmLabs/binwalk/archive/v2.1.1.tar.gz -O ~/build/v2.1.1.tar.gz || true && tar --skip-old-files -zxf ~/build/v2.1.1.tar.gz -C ~/build &&  cp -r patches/binwalk/* ~/build/binwalk-2.1.1/src/ && cd ~/build/binwalk-2.1.1 && sudo python3.7 setup.py -q install && cd ~-
RUN wget -nc https://download.qemu.org/qemu-4.0.0.tar.xz -O ~/build/qemu-4.0.0.tar.xz || true && tar --skip-old-files -Jxf ~/build/qemu-4.0.0.tar.xz -C ~/build && cp -r patches/qemu/* ~/build/qemu-4.0.0/ && cd ~/build/qemu-4.0.0 && ./configure --target-list=arm-softmmu,mipsel-softmmu,mips-softmmu && make -j4 && cd ~-

# isntall llvm9
RUN apt-get update && apt-get install -y build-essential wget lsb-core software-properties-common vim && \
wget https://apt.llvm.org/llvm.sh && chmod +x llvm.sh && ./llvm.sh 9 && \
ln -s /usr/bin/clang-9 /usr/bin/clang && ln -s /usr/bin/llvm-link-9 /usr/bin/llvm-link && ln -s /usr/bin/opt-9 /usr/bin/opt
RUN pip3.7 install networkx matplotlib graphviz

WORKDIR /root
