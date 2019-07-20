#ifndef MV88F5181L_PERIPHERALS_H
#define MV88F5181L_PERIPHERALS_H

#include "hw/sysbus.h"
#include "hw/initc/mv88f5181L_ic.h"
#include "hw/gpio/mv88f5181L_gpio"

#define TYPE_MV88F5181L_PERIPHERALS "MV88F5181L_PERIPHERALS"
#define MV88F5181L_PERIPHERALS(obj) \
    OBJECT_CHECK(MV88F5181L_PERIPHERALSState, (obj),  TYPE_MV88F5181L_PERIPHERALS)

typedef struct MV88F5181L_PERIPHERALSState {
    /*< private >*/
    SysBusDevice sys_bus;
    /*< public >*/

    MemoryRegion peri_mr, peri_mr_alias;
    qemu_irq irq, fiq;

    MV88F5181LICState ic;
    MV88F5181LGPIOState gpio;

} MV88F5181L_PERIPHERALSState;

#endif /* MV88F5181L_PERIPHERALS_H */