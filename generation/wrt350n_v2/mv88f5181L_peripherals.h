/* 
 * automatically generated, don't change
 */

#ifndef MV88F5181L_PERIPHERALS_H
#define MV88F5181L_PERIPHERALS_H

#include "hw/sysbus.h"

#define TYPE_MV88F5181L_PERIPHERALS "MV88F5181L_PERIPHERALS"
#define MV88F5181L_PERIPHERALS(obj) \
    OBJECT_CHECK(MV88F5181LPeripheralsState, (obj),  TYPE_MV88F5181L_PERIPHERALS)

typedef struct MV88F5181LPeripheralsState {
    /*< private >*/
    SysBusDevice sys_bus;
    /*< public >*/

    MemoryRegion peri_mr;
    qemu_irq irq, fiq;

    MV88F5181LICState ic;
} MV88F5181LPeripheralsState;

#endif /* MV88F5181L_PERIPHERALS_H */