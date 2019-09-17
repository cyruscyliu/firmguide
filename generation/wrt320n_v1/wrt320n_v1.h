/* 
 * automatically generated, don't change
 */

#ifndef WRT320N_V1_H
#define WRT320N_V1_H

#include "qemu/osdep.h"
#include "hw/mips/BCM4717A1.h"
#include "hw/block/flash.h"

#define TYPE_WRT320N_V1 "wrt320n_v1"

typedef struct WRT320N_V1State {
    BCM4717A1State soc;
    MemoryRegion ram;
} WRT320N_V1State;

#endif /* WRT320N_V1_H */
