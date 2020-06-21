/*
 * simple dual state machine
 */

#ifndef RALINK_RT3050_ESW_H
#define RALINK_RT3050_ESW_H

#include "hw/sysbus.h"

#define TYPE_RALINK_RT3050_ESW "ralink_rt3050_esw"
#define RALINK_RT3050_ESW(obj) \
    OBJECT_CHECK(RALINK_RT3050_ESWState, (obj), TYPE_RALINK_RT3050_ESW)

typedef struct RALINK_RT3050_ESWState {
    /*< private >*/
    SysBusDevice sys_bus;
    /*< public >*/

    MemoryRegion mmio;

    uint32_t pcr0;
} RALINK_RT3050_ESWState;

#endif /* RALINK_RT3050_ESW_H */
