export DIR_TO_BUILD=$(realpath $(CURDIR)/build)
export PYTHON=python3.7

all:
	mkdir -p build
	${MAKE} -C binwalk
	${MAKE} -C qemu

clean:
	${MAKE} -C binwalk clean
	${MAKE} -C qemu clean

clean_all:
	${MAKE} -C binwalk clean_all
	${MAKE} -C qemu clean_all
	rm -r build