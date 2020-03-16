# Salamander

[![CircleCI](https://circleci.com/gh/cyruscyliu/esv/tree/master.svg?style=svg&circle-token=7f12caaa351d02731d57d8165e634dc3e3537d33)](https://circleci.com/gh/cyruscyliu/esv/tree/master)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/a7aacb11a3b14a7d8e069d8a440a43c0)](https://www.codacy.com?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=cyruscyliu/esv&amp;utm_campaign=Badge_Grade)

Firmware analysis matters in embedded system security, especially dynamic firmware analysis which can
discover deep and complicated vulnerabilities. However, we cannot do dynamic firmware analysis immediately
because of lack of virtual execution environment. Salamander is such a project that builds the virtual
execution environment in a pure software way, showing us a feasible way to boot up any firmware in
limited steps, which is of scale and reliable. In this very early stage, Salamander only targets Linux-based
firmware and can only be used standalone.

## Install

```shell script
# install python 3.7
sudo apt-get install -y software-properties-common && add-apt-repository ppa:deadsnakes/ppa && apt-get update
sudo apt-get install -y python3.7 python3-pip python3.7-dev
sudo -H python3.7 -m pip install --upgrade pip && sudo rm /usr/bin/python && sudo ln -s /usr/bin/python3.7 /usr/bin/python

# install required python packages
sudo -H pip3.7 install qmp pyyaml fdt fuzzywuzzy networkx pyquery prettytable capstone python-Levenshtein z3-solver pydot pyelftools
git clone https://github.com/cyruscyliu/pymake.git ~/pymake && cd ~/pymake && sudo -H pip3.7 install .
git clone https://github.com/cyruscyliu/pyqemulog ~/pyqemulog && cd ~/pyqemulog && sudo -H pip3.7 install .

# install other dependency
sudo apt-get install -y git libglib2.0-dev libfdt-dev libpixman-1-dev zlib1g-dev bison flex libcapstone3 \
libcapstone-dev u-boot-tools p7zip-full squashfs-tools device-tree-compiler gawk
sudo apt-get install -y zlib1g-dev liblzma-dev liblzo2-dev && git clone https://github.com/devttys0/sasquatch ~/sasquatch && \
cd ~/sasquatch && ./build.sh && cd ~-

# install salamander
git clone https://github.com/cyruscyliu/esv.git salamander && cd salamander && mkdir log && mkdir ~/build

# patch and install binwalk
wget -nc https://github.com/ReFirmLabs/binwalk/archive/v2.1.1.tar.gz -O ~/build/v2.1.1.tar.gz || true && \
tar --skip-old-files -zxf ~/build/v2.1.1.tar.gz -C ~/build && cp -r patches/binwalk/* ~/build/binwalk-2.1.1/src/ && \
cd ~/build/binwalk-2.1.1 && sudo python3.7 setup.py -q install && cd ~-

# install modified qemu
wget -nc https://download.qemu.org/qemu-4.0.0.tar.xz -O ~/build/qemu-4.0.0.tar.xz || true && \
tar --skip-old-files -Jxf ~/build/qemu-4.0.0.tar.xz -C ~/build && cp -r patches/qemu/* ~/build/qemu-4.0.0/ && \
cd ~/build/qemu-4.0.0 && ./configure --enable-debug --extra-cflags="-g3" --extra-ldflags="-g3" \
--disable-strip --disable-pie --target-list=arm-softmmu,mips-softmmu,mipsel-softmmu && make -j4 && cd ~-

# install sparse
git clone git://git.kernel.org/pub/scm/devel/sparse/sparse.git ~/sparse && cd ~/sparse && make && sudo cp ./graph /usr/bin && cd ~-
```

## Usage

Step 1, create a project. Salamander is a project-style tool. A project is a global information
center and will be used in every future step implicitly. The project is quite useful saving you
from long and forgettable command lines. See `./salamander create -h` for help to create a project.

Step 2, analyze your source. Salamander is a command-style tool. Salamander has three groups of
commands, core, plugins, settings. It is very simple to analyze your source if you've already create a project.

```
./salamander analyze
./salamander declare
```

Step 3, diagnose your model. Salamander is a config-style tool. The world of embedded systems is
full of fragmentation such that Salamander must be unchangeable to new models. We make all models
as configs, which all commands reading/writing  with a set of universal interfaces. We've built in
several models and once you've got a firmware with device tree, mostly, you will be working on your
own models, ICT modeling and IV resolving. It takes time to try and try again to finally get precise
models. Salamander has a QEMU debugging interface and some plugins to help your jobs.


```
./salamander batch -c 1 -e dir/to/images
./salamander -d diagnose
```

Step 4, boot up firmware. Salamander is a full solution from modeling to booting. We can boot up
firmware not only compiled with source but also scratched in the wild. Enjoy your time!

```
./salamander bootup -f path/to/image
```

## Contributors
[cyruscyliu*](https://github.com/cyruscyliu/esv), [occia*](https://github.com/occia)

## License
[MIT License](./LICENSE)

