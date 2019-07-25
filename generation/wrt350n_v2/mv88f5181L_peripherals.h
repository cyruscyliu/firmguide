/* 
 * automatically generated, don't change
 */

#ifndef MV88F5181L_PERIPHERALS_H
#define MV88F5181L_PERIPHERALS_H

#include "hw/sysbus.h"
#include "hw/timer/mv88f5181L_timer.h"

#define TYPE_MV88F5181L_PERIPHERALS "MV88F5181L_PERIPHERALS"
#define MV88F5181L_PERIPHERALS(obj) \
    OBJECT_CHECK(MV88F5181LPERIPHERALSState, (obj),  TYPE_MV88F5181L_PERIPHERALS)
#define MV88F5181L_PERIPHERALS_RAM_SIZE 0x10000000

#define MV88F5181L_TIMER_RAM_BASE 0x00020300

typedef struct MV88F5181LPERIPHERALSState {
    /*< private >*/
    SysBusDevice sys_bus;
    /*< public >*/

    MemoryRegion mmio;
    MV88F5181LTIMERState timer;
} MV88F5181LPERIPHERALSState;

static void mv88f5181L_peripherals_realize(DeviceState *dev, Error **errp);

static void mv88f5181L_peripherals_init(Object *obj);
static void mv88f5181L_peripherals_class_init(ObjectClass *oc, void *data);
static void mv88f5181L_peripherals_register_types(void);

#endif /* MV88F5181L_PERIPHERALS_H */