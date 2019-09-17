/* 
 * automatically generated, don't change
 */

#ifndef BCM4717A1_H
#define BCM4717A1_H

#include "hw/mips/mips.h"
#include "hw/sysbus.h"
#include "hw/mips/bcma.h"

#define TYPE_BCM4717A1 "BCM4717A1"
#define BCM4717A1(obj) \
    OBJECT_CHECK(BCM4717A1State, (obj), TYPE_BCM4717A1)

typedef struct BCM4717A1State {
    /*< private >*/
    SysBusDevice sys_bus;
    /*< public >*/

    const char *cpu_type;
    MIPSCPU *cpu;

    BCMAState bridge;

} BCM4717A1State;

#endif /* BCM4717A1_H */
