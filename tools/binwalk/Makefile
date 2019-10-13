PACKAGE_URL:=https://github.com/ReFirmLabs/binwalk/archive/v2.1.1.tar.gz
PACKAGE_NAME:=v2.1.1.tar.gz
PACKAGE_DIR_NAME:=binwalk-2.1.1

all: prepare build

prepare:
	wget -nc $(PACKAGE_URL) -O $(DIR_TO_BUILD)/$(PACKAGE_NAME) || true
	tar --skip-old-files -zxf $(DIR_TO_BUILD)/$(PACKAGE_NAME) -C $(DIR_TO_BUILD)

build:
	cd $(DIR_TO_BUILD)/$(PACKAGE_DIR_NAME) && git init -q && git add .gitignore && git add * && git commit -q -m "init"
	cp -r files/* $(DIR_TO_BUILD)/$(PACKAGE_DIR_NAME)/src/
	cd $(DIR_TO_BUILD)/$(PACKAGE_DIR_NAME) && git add * && git commit -q -m "patch $(PACKAGE_DIR_NAME)" && git format-patch -q HEAD^1
	mv $(DIR_TO_BUILD)/$(PACKAGE_DIR_NAME)/*.patch ./patches/
	cd $(DIR_TO_BUILD)/$(PACKAGE_DIR_NAME) && sudo $(PYTHON) setup.py -q uninstall && sudo $(PYTHON) setup.py -q install
	cd $(DIR_TO_BUILD)/$(PACKAGE_DIR_NAME) && sudo cp src/build/scripts-3.7/binwalk /usr/local/bin

clean:
	rm -rf $(DIR_TO_BUILD)/$(PACKAGE_DIR_NAME)


clean_all:
	rm -rf $(DIR_TO_BUILD)/$(PACKAGE_DIR_NAME) $(DIR_TO_BUILD)/${PACKAGE_NAME}


