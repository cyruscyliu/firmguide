# This will replace setup.sh in the future.

PRONAME 				= FirmGuide
VERSION					= 0.9.1

TOPDIR 					= ${shell pwd}
TMPDIR 					= /tmp

QEMU_VERSION 		?= 4.0.0
QEMU_FLAGS      ?=
FIRMGUID_BUILD 	?= ${TMPDIR}

export TOPDIR TMPDIR QEMU_VERSION FIRMGUID_BUILD PRONAME VERSION

all: qemu

test_qemu_version:
ifneq ($(wildcard ${TOPDIR}/externals/qemu-${QEMU_VERSION}.patch), )
	@echo [+] QEMU-${QEMU_VERSION} supported.
else
	@echo [-] QEMU-${QEMU_VERSION} not supported. && exit 1
endif

qemu: test_qemu_version
	@echo [+] Install QEMU-${QEMU_VERSION} ...
	@sudo apt-get install -y git libglib2.0-dev libfdt-dev libpixman-1-dev \
		zlib1g-dev bison flex libcapstone3 libcapstone-dev u-boot-tools \
		p7zip-full squashfs-tools device-tree-compiler gawk
	@echo [+] Download QEMU-${QEMU_VERSION}
	@rm -rf ${TMPDIR}/qemu-${QEMU_VERSION}
	@wget -nc https://download.qemu.org/qemu-${QEMU_VERSION}.tar.xz \
		-O ${TMPDIR}/qemu-${QEMU_VERSION}.tar.xz || true && \
		tar --skip-old-files -Jxf ${TMPDIR}/qemu-${QEMU_VERSION}.tar.xz -C ${TMPDIR}
	@echo [+] Patch QEMU-${QEMU_VERSION}
	@patch -d ${TMPDIR}/qemu-${QEMU_VERSION} -N -p1 < ${TOPDIR}/externals/qemu-${QEMU_VERSION}.patch
	@echo [+] Compile QEMU-${QEMU_VERSION}
	@cd ${TMPDIR}/qemu-${QEMU_VERSION} && ./configure \
		--target-list=arm-softmmu,mips-softmmu,mipsel-softmmu \
		--enable-autoboard \
		--enable-debug --extra-cflags="-g3" --extra-ldflags="-g3" \
		--disable-strip --disable-pie ${QEMU_FLAGS} && make -j$(nproc)
	@echo ${TMPDIR}/qemu-${QEMU_VERSION} > .qemu
	@echo [+] Install QEMU-${QEMU_VERSION} done
