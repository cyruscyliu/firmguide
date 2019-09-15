.ONESHELL:

PACKAGE_URL="https://download.qemu.org/qemu-4.0.0.tar.xz"
PACKAGE_NAME="qemu-4.0.0.tar.xz"
PACKAGE_DIR_NAME="qemu-4.0.0"

DIR_TO_BUILD=$(realpath $(CURDIR)/../build)

build_dir:
	@echo "path to qemu is" $(DIR_TO_BUILD)
ifeq ("$(wildcard $(DIR_TO_BUILD))", "")
	mkdir $(DIR_TO_BUILD)
endif

download:
	@cd $(DIR_TO_BUILD)
ifeq ("$(wildcard $(PACKAGE_NAME))", "")
	@echo $(PACKAGE_NAME) "exists"
else
	wget $(PACKAGE_URL)
endif

ifeq ("$(wildcard $(PACKAGE_DIR_NAME))", "")
	@rm -rf $(PACKAGE_DIR_NAME)
endif
	tar Jxf $(PACKAGE_NAME)

binwalk: build_dir download
	cd $(DIR_TO_BUILD)/$(PACKAGE_DIR_NAME)
	git init -q && git add .gitignore && git add * && git commit -q -m "init"
	cd -
	cp -r files/* $(DIR_TO_BUILD)/$(PACKAGE_DIR_NAME)/
	cd $(DIR_TO_BUILD)/$(PACKAGE_DIR_NAME)
	git add * && git commit -q -m "patch $(PACKAGE_DIR_NAME)"
	git format-patch -q HEAD^1
	cd -
	mv $(DIR_TO_BUILD)/$(PACKAGE_DIR_NAME)/*.patch ./patches/
	cd $(DIR_TO_BUILD)/$(PACKAGE_DIR_NAME)
	./configure --target-list arm-softmmu
	make -j4

