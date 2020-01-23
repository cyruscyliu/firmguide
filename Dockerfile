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

# install dependency for QEMU/BINWALK etc.
RUN apt-get install -y git libglib2.0-dev libfdt-dev libpixman-1-dev zlib1g-dev wget sudo && \
bison flex libcapstone3 libcapstone-dev u-boot-tools p7zip-full squashfs-tools device-tree-compiler gawk

# isntall llvm9
RUN apt-get update && apt-get install -y build-essential wget lsb-core software-properties-common vim && \
wget https://apt.llvm.org/llvm.sh && chmod +x llvm.sh && ./llvm.sh 9 && \
ln -s /usr/bin/clang-9 /usr/bin/clang && ln -s /usr/bin/llvm-link-9 /usr/bin/llvm-link && ln -s /usr/bin/opt-9 /usr/bin/opt
RUN pip3.7 install networkx matplotlib graphviz

WORKDIR /root
