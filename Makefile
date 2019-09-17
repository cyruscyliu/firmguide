all:
	@mkdir build
	${MAKE} -C binwalk
	${MAKE} -C qemu

clean:
	${MAKE} -C binwalk clean
	${MAKE} -C qemu clean
	rm -r build