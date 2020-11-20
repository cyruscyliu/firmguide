# This will replace setup.sh in the future.

PRONAME 	= FirmGuide
VERSION		= 0.8.0

TOPDIR 	        = ${shell pwd}
TMPDIR 		= /tmp

QEMU_VERSION 	?= 4.0.0
QEMU_FLAGS      ?=
FIRMGUID_BUILD 	?= ${TMPDIR}

export TOPDIR TMPDIR QEMU_VERSION FIRMGUID_BUILD PRONAME VERSION

all: python binwalk qemu

test_qemu_version:
ifneq ($(wildcard ${TOPDIR}/externals/qemu-${QEMU_VERSION}.patch), )
	@echo [+] QEMU-${QEMU_VERSION} supported.
else
	@echo [-] QEMU-${QEMU_VERSION} not supported. && exit 1
endif

qemu: test_qemu_version
	@echo [+] Install QEMU-${QEMU_VERSION} ...
	sudo apt-get install -y git libglib2.0-dev libfdt-dev libpixman-1-dev \
		zlib1g-dev bison flex libcapstone3 libcapstone-dev u-boot-tools \
		p7zip-full squashfs-tools device-tree-compiler gawk
	@echo [+] Download QEMU-${QEMU_VERSION}
	rm -rf ${TMPDIR}/qemu-${QEMU_VERSION}
	wget -nc https://download.qemu.org/qemu-${QEMU_VERSION}.tar.xz \
		-O ${TMPDIR}/qemu-${QEMU_VERSION}.tar.xz || true && \
		tar --skip-old-files -Jxf ${TMPDIR}/qemu-${QEMU_VERSION}.tar.xz -C ${TMPDIR}
	@echo [+] Patch QEMU-${QEMU_VERSION}
	patch -d ${TMPDIR}/qemu-${QEMU_VERSION} -N -p1 < ${TOPDIR}/externals/qemu-${QEMU_VERSION}.patch
	@echo [+] Compile QEMU-${QEMU_VERSION}
	cd ${TMPDIR}/qemu-${QEMU_VERSION} && ./configure \
		--target-list=arm-softmmu,mips-softmmu,mipsel-softmmu \
		--enable-autoboard \
		--enable-debug --extra-cflags="-g3" --extra-ldflags="-g3" \
		--disable-strip --disable-pie ${QEMU_FLAGS} && make -j$(nproc)
	@echo ${TMPDIR}/qemu-${QEMU_VERSION} > .qemu
	@echo [+] Change qemutemplates to qemutempltes-${QEMU_VERSION}
	mkdir -p ${TOPDIR}/slcore/qemutemplates-${QEMU_VERSION}
	rm -f ${TOPDIR}/slcore/qemutemplates
	cd ${TOPDIR}/slcore && ln -s qemutemplates-${QEMU_VERSION} qemutemplates
	@echo [+] Done

python: python3.6

python3.6: 
ifeq (, $(shell which python3.6))
	@echo [+] Install Python3.6
	@echo =========================================
	apt-get install -y python3.6
endif
	@echo [+] Install Python requirments
	@echo =========================================
	apt-get install -y python3-pip
	python3.6 -m pip install --upgrade pip
	pip3.6 install --upgrade pip
	pip3.6 install qmp fdt capstone pydot graphviz pyyaml
	test /tmp/pyqemulog/pyqemulog.py >/dev/null 2>&1 || \
		(rm -rf /tmp/pyqemulog && \
		git clone https://github.com/cyruscyliu/pyqemulog /tmp/pyqemulog && \
		cd /tmp/pyqemulog && pip3.6 install . && cd $(OLDPWD))
	@echo [+] Done

binwalk: 
	@echo [+] Install Binwalk
	@echo =========================================
	wget -nc https://github.com/ReFirmLabs/binwalk/archive/v2.1.1.tar.gz \
		-O /tmp/v2.1.1.tar.gz || true
	tar --skip-old-files -zxf /tmp/v2.1.1.tar.gz -C /tmp && \
		cp -r ./externals/binwalk/* /tmp/binwalk-2.1.1/src/ && \
	cd /tmp/binwalk-2.1.1 && python3.6 setup.py -q install && cd $(OLDPWD)
ifeq (, $(shell which sasquatch))
	apt-get install -y zlib1g-dev liblzma-dev liblzo2-dev && \
		git clone https://github.com/devttys0/sasquatch /tmp/sasquatch && \
		cd /tmp/sasquatch && ./build.sh && cd $(OLDPWD)
endif
	@echo [+] Done

sparse:
	@echo [+] Install Sparse
	@echo =========================================
	wget -nc https://git.kernel.org/pub/scm/devel/sparse/sparse.git/snapshot/sparse-0.6.2.tar.gz \
		-O /tmp/sparse-0.6.2.tar.gz || true
	tar --skip-old-files -zxf /tmp/sparse-0.6.2.tar.gz -C /tmp
	cp -rL --remove-destination ./externals/sparse/* /tmp/sparse-0.6.2/
	make -C /tmp/sparse-0.6.2
	echo /tmp/sparse-0.6.2 > .sparse
	@echo [+] Done

help:
	@echo "  all     	install all below by default"
	@echo "  python     	install Python 3.6"
	@echo "  binwalk     	install Binwalk 2.1.1"
	@echo "  qemu     	install QEMU 4.0.0"
	@echo "  sparse		install Sparse 0.6.2"

clean:
	rm -rf *.dts *.extracted *.log .qemu .sparse .slicing *.fcbs
 
.PHONY: all clean help
