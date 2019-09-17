.ONESHELL:

PACKAGE_URL=https://github.com/ReFirmLabs/binwalk/archive/v2.1.1.tar.gz
PACKAGE_NAME=v2.1.1.tar.gz
PACKAGE_DIR_NAME=binwalk-2.1.1

DIR_TO_BUILD=$(realpath $(CURDIR)/../build)
DIR_TO_PATCH=$(realpath $(CURDIR))
PYTHON=python3.7
PREFIX=[BINWALK]

all: download build

download:
	@echo $(PREFIX) "path to binwalk is" $(DIR_TO_BUILD)
	@cd $(DIR_TO_BUILD)
ifneq ("$(wildcard $(DIR_TO_BUILD)/$(PACKAGE_NAME))", "")
	@echo $(PREFIX) $(PACKAGE_NAME) "exists"
else
	@echo $(PREFIX) downloading from $(PACKAGE_URL) ...
	@wget $(PACKAGE_URL)
endif

ifneq ("$(wildcard $(DIR_TO_BUILD)$(PACKAGE_DIR_NAME))", "")
	@rm -rf $(PACKAGE_DIR_NAME)
endif
	@echo $(PREFIX) uncompressing ...
	@tar zxf $(PACKAGE_NAME)

build:
	@echo $(PREFIX) building ...
	@cd $(DIR_TO_BUILD)/$(PACKAGE_DIR_NAME)
	@git init -q && git add .gitignore && git add * && git commit -q -m "init"
	@cd $(DIR_TO_PATCH)
	@echo $(PREFIX) patching ...
	@cp -r files/* $(DIR_TO_BUILD)/$(PACKAGE_DIR_NAME)/src/
	@cd $(DIR_TO_BUILD)/$(PACKAGE_DIR_NAME)
	@git add * && git commit -q -m "patch $(PACKAGE_DIR_NAME)"
	@git format-patch -q HEAD^1
	@cd $(DIR_TO_PATCH)
	@mv $(DIR_TO_BUILD)/$(PACKAGE_DIR_NAME)/*.patch ./patches/
	@cd $(DIR_TO_BUILD)/$(PACKAGE_DIR_NAME)
	@echo $(PREFIX) installing ..
	@sudo $(PYTHON) setup.py -q uninstall && sudo $(PYTHON) setup.py -q install
	@sudo cp src/build/scripts-3.7/binwalk /usr/local/bin
	@sudo chmod 755 /usr/local/bin
	@echo $(PREFIX) done

clean:
	@cd $(DIR_TO_BUILD)
	rm -rf $(PACKAGE_DIR_NAME) ${PACKAGE_NAME}


