/* 
 * automatically generated, don't change
 */

#ifndef MV88F5181L_H
#define MV88F5181L_H

#include "hw/arm/arm.h"
#include "hw/intc/mv88f5181L_ic.h"

#define TYPE_MV88F5181L "mv88f5181L"
#define MV88F5181L(obj) \
    OBJECT_CHECK(MV88F5181LState, (obj), TYPE_MV88F5181L)

#define MV88F5181L_PERIPHERALS_RAM_BASE 0xfdd00000
#define MV88F5181L_IC_RAM_BASE 0xfdd20200

typedef struct MV88F5181LState {
    /*< private >*/
    DeviceState parent_obj;
    /*< public >*/

    char *cpu_type;
    ARMCPU cpu;
    qemu_irq irq, fiq;

    MV88F5181LICState ic;
    MV88F5181LPERIPHERALSState peripherals;
} MV88F5181LState;

static void mv88f5181L_realize(DeviceState *dev, Error **errp);

static void mv88f5181L_init(Object *obj);
static void mv88f5181L_class_init(ObjectClass *oc, void *data);
static const TypeInfo mv88f5181L_type_info(void);

#endif /* MV88F5181L_H */