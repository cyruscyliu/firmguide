.ONESHELL:

PACKAGE_URL="https://github.com/ReFirmLabs/binwalk/archive/v2.1.1.tar.gz"
PACKAGE_NAME="v2.1.1.tar.gz"
PACKAGE_DIR_NAME="binwalk-2.1.1"

DIR_TO_BUILD=$(realpath $(CURDIR)/../build)

build_dir:
	@echo "path to binwalk is" $(DIR_TO_BUILD)
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
	tar zxf $(PACKAGE_NAME)

binwalk: build_dir download
	cd $(DIR_TO_BUILD)/$(PACKAGE_DIR_NAME)
	git init -q && git add .gitignore && git add * && git commit -q -m "init"
	cd -
	cp -r files/* $(DIR_TO_BUILD)/$(PACKAGE_DIR_NAME)/src/
	cd $(DIR_TO_BUILD)/$(PACKAGE_DIR_NAME)
	git add * && git commit -q -m "patch $(PACKAGE_DIR_NAME)"
	git format-patch -q HEAD^1
	cd -
	mv $(DIR_TO_BUILD)/$(PACKAGE_DIR_NAME)/*.patch ./patches/
	cd $(DIR_TO_BUILD)/$(PACKAGE_DIR_NAME)
	sudo python3.7 setup.py install

