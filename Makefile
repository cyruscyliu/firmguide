DIR_TO_BUILD = $(realpath $(CURDIR)/build)
PYTHON = python3.7

export DIR_TO_BUILD PYTHON

all:
	mkdir -p build
	${MAKE} -C tools/binwalk
	${MAKE} -C tools/qemu

clean:
	${MAKE} -C tools/binwalk clean
	${MAKE} -C tools/qemu clean

clean_all:
	${MAKE} -C tools/binwalk clean_all
	${MAKE} -C tools/qemu clean_all
	rm -r build