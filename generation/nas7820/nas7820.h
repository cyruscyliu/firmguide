/* 
 * automatically generated, don't change
 */

#ifndef NAS7820_H
#define NAS7820_H

#include "qemu/osdep.h"
#include "hw/arm/ox820.h"
#include "hw/block/flash.h"

#define NAS7820_FLASH_ADDR      0x41000000
#define NAS7820_FLASH_SIZE      (128 * MiB)
#define NAS7820_FLASH_SECT_SIZE (None)

#define TYPE_NAS7820 "nas7820"

typedef struct NAS7820State {
    OX820State soc;
    MemoryRegion ram;
    PFlashCFI01 *flash;
} NAS7820State;

#endif /* NAS7820_H */