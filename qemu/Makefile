.ONESHELL:

PACKAGE_URL=https://download.qemu.org/qemu-4.0.0.tar.xz
PACKAGE_NAME=qemu-4.0.0.tar.xz
PACKAGE_DIR_NAME=qemu-4.0.0

DIR_TO_BUILD=$(realpath $(CURDIR)/../build)
DIR_TO_PATCH=$(realpath $(CURDIR))
PYTHON=python3.7
PREFIX=[QEMU]

all: download build

download:
	@echo $(PREFIX) "path to qemu is" $(DIR_TO_BUILD)
	@cd $(DIR_TO_BUILD)
ifneq ("$(wildcard $(DIR_TO_BUILD)/$(PACKAGE_NAME))", "")
	@echo $(PREFIX) $(PACKAGE_NAME) "exists"
else
	@echo $(PREFIX) downloading from $(PACKAGE_URL) ...
	@wget $(PACKAGE_URL)
endif

ifneq ("$(wildcard $(DIR_TO_BUILD)/$(PACKAGE_DIR_NAME))", "")
	@rm -rf $(PACKAGE_DIR_NAME)
endif
	@echo $(PREFIX) uncompressing ...
	@tar Jxf $(PACKAGE_NAME)

build:
	@echo $(PREFIX) building ...
	@cd $(DIR_TO_BUILD)/$(PACKAGE_DIR_NAME)
	@git init -q && git add .gitignore && git add $(notdir $(wildcard $(DIR_TO_PATCH)/files/*)) && git commit -q -m "init"
	@cd $(DIR_TO_PATCH)
	@echo $(PREFIX) patching ...
	@cp -r files/* $(DIR_TO_BUILD)/$(PACKAGE_DIR_NAME)/
	@cd $(DIR_TO_BUILD)/$(PACKAGE_DIR_NAME)
	@git add $(notdir $(wildcard $(DIR_TO_PATCH)/files/*)) && git commit -q -m "patch $(PACKAGE_DIR_NAME)"
	@git format-patch -q HEAD^1
	@cd $(DIR_TO_PATCH)
	@mv $(DIR_TO_BUILD)/$(PACKAGE_DIR_NAME)/*.patch ./patches/
	@cd $(DIR_TO_BUILD)/$(PACKAGE_DIR_NAME)
	@echo $(PREFIX) installing ..
	./configure --target-list=arm-softmmu --enable-debug >/dev/null
	make -j4
	@echo $(PREFIX) done

clean:
	@cd $(DIR_TO_BUILD)
	rm -rf $(PACKAGE_DIR_NAME) ${PACKAGE_NAME}

