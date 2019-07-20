#ifndef MV88F5181L_H
#define MV88F5181L_H

#include "hw/sysbus.h"
#include "hw/initc/mv88f5181L_ic.h"
#include "hw/gpio/mv88f5181L_gpio"

#define TYPE_MV88F5181L "mv88f5181L"
#define MV88F5181L(obj) \
    OBJECT_CHECK(MV88F5181LState, (obj), TYPE_MV88F5181L)
#define TYPE_MV88F5181L_PERIPHERALS "mv88f5181L-peripherals"
#define MV88F5181L_PERIPHERALS(obj) \
    OBJECT_CHECK(MV88F5181LPeripheralState, (obj),  TYPE_MV88F5181L_PERIPHERALS)

#define MV88F5181L_NCPUS 1

typedef struct MV88F5181LPeripheralState {
    /*< private >*/
    SysBusDevice sys_bus;
    /*< public >*/

    MemoryRegion peri_mr, peri_mr_alias;
    qemu_irq irq, fiq;

    MV88F5181LICState ic;
    MV88F5181LGPIOState gpio;

} MV88F5181LPeripheralState;

typedef struct MV88F5181LState {
    /*< private >*/
    DeviceState parent_obj;
    /*< public >*/

    char *cpu_type;
    uint32_t enabled_cpus;

    ARMCPU cpus[MV88F5181L_NCPUS];
    MV88F5181LPeripheralState peripherals;
} MV88F5181LState;

typedef struct MV88F5181LClass {
    /*< private >*/
    DeviceClass parent_class;
    /*< public >*/

    const char *name;
    const char *cpu_type;
    int clusterid;
} MV88F5181LClass;

#define MV88F5181L_CLASS(klass) \
    OBJECT_CLASS_CHECK(MV88F5181LClass, (klass), TYPE_MV88F5181L)
#define MV88F5181LL_GET_CLASS(obj) \
    OBJECT_GET_CLASS(MV88F5181LClass, (obj), TYPE_MV88F5181L)

#define ERROR_PROPAGATE(errp, err) \
    if (err) { \
        error_propagate(errp, err); \
        return; \
    }

#endif /* MV88F5181L_H */