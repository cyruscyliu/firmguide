################################################################################
#
# dirty cow
#
################################################################################

DIRTY_COW_VERSION = 2580beeef4063124df89d0f650e5f199fcdd09ff
DIRTY_COW_SITE = $(call github,FireFart,dirtycow,$(DIRTY_COW_VERSION))

define DIRTY_COW_BUILD_CMDS
	$(TARGET_CC) -pthread $(@D)/dirty.c -o $(@D)/dirty -lcrypt
endef

define DIRTY_COW_INSTALL_TARGET_CMDS
	$(INSTALL) -D -m 0755 $(@D)/dirty $(TARGET_DIR)/usr/bin
endef

$(eval $(generic-package))
