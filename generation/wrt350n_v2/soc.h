#ifndef MV88F5181L_H
#define MV88F5181L_H

#include "hw/arm/arm.h"
#include "hw/sysbus.h"

#define TYPE_MV88F5181L "mv88f5181L"
#define MV88F5181L(obj) \
    OBJECT_CHECK(MV88F5181LState, (obj), TYPE_MV88F5181L)
#define TYPE_MV88F5181L_CONTROL "mv88f5181L-control"
#define MV88F5181L_CONTROL(obj) \
    OBJECT_CHECK(MV88F5181LControlState, (obj), TYPE_MV88F5181L_CONTROL)
#define TYPE_MV88F5181L_PERIPHERALS "mv88f5181L-peripherals"
#define MV88F5181L_PERIPHERALS(obj) \
    OBJECT_CHECK(MV88F5181LPeripheralState, (obj),  TYPE_MV88F5181L_PERIPHERALS)

#define MV88F5181L_NCPUS 1

typedef struct MV88F5181LControlState {
    /*< private >*/
    SysBusDevice sysbus;
    /*< public >*/

    MemoryRegion mmio;

    /* outputs to CPU cores */
    qemu_irq[MV88F5181L_NCPUS];
    qemu_fiq[MV88F5181L_NCPUS];
} MV88F5181LControlState;

typedef struct MV88F5181LPeripheralState {
    /*< private >*/
    SysBusDevice parent_obj;
    /*< public >*/

    MemoryRegion ram_alias[4];
    qemu_irq irq, fiq;
} MV88F5181LPeripheralState;

typedef struct MV88F5181LState {
    /*< private >*/
    DeviceState parent_obj;
    /*< public >*/

    char *cpu_type;
    uint32_t enabled_cpus;

    ARMCPU cpus[MV88F5181L_NCPUS];
    MV88F5181LControlState control;
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