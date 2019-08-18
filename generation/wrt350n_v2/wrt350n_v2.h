/* 
 * automatically generated, don't change
 */

#ifndef WRT350N_V2_H
#define WRT350N_V2_H

#include "qemu/osdep.h"
#include "hw/arm/mv88f5181l.h"
#include "hw/block/flash.h"

#define WRT350N_V2_FLASH_ADDR      0xf4000000
#define WRT350N_V2_FLASH_SIZE      (8 * MiB)
#define WRT350N_V2_FLASH_SECT_SIZE (64 * KiB)

#define TYPE_WRT350N_V2 "wrt350n_v2"

typedef struct WRT350N_V2State {
    MV88F5181LState soc;
    MemoryRegion ram;
    PFlashCFI01 *flash;
} WRT350N_V2State;

#endif /* WRT350N_V2_H */