PACKAGE_URL:=https://download.qemu.org/qemu-4.0.0.tar.xz
PACKAGE_NAME:=qemu-4.0.0.tar.xz
PACKAGE_DIR_NAME:=qemu-4.0.0

all: prepare build

prepare:
	wget -nc $(PACKAGE_URL) -O $(DIR_TO_BUILD)/$(PACKAGE_NAME) || true
	tar --skip-old-files -Jxf $(DIR_TO_BUILD)/$(PACKAGE_NAME) -C $(DIR_TO_BUILD)

build:
	cd $(DIR_TO_BUILD)/$(PACKAGE_DIR_NAME) && git init -q && git add .gitignore && git add * && git commit -q -m "init"
	cp -r files/* $(DIR_TO_BUILD)/$(PACKAGE_DIR_NAME)/
	cd $(DIR_TO_BUILD)/$(PACKAGE_DIR_NAME) && git add * && git commit -q -m "patch $(PACKAGE_DIR_NAME)" && git format-patch -q HEAD^1
	mv $(DIR_TO_BUILD)/$(PACKAGE_DIR_NAME)/*.patch ./patches/
	cd $(DIR_TO_BUILD)/$(PACKAGE_DIR_NAME) && ./configure --target-list=arm-softmmu --enable-debug >/dev/null
	cd $(DIR_TO_BUILD)/$(PACKAGE_DIR_NAME) && make -j4

clean:
	rm -rf $(DIR_TO_BUILD)/$(PACKAGE_DIR_NAME)

clean_all:
	rm -rf $(DIR_TO_BUILD)/$(PACKAGE_DIR_NAME) $(DIR_TO_BUILD)/${PACKAGE_NAME}

