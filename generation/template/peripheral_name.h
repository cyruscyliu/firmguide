{{license}}

#ifndef {{peripheral_name|upper}}_H
#define {{peripheral_name|upper}}_H

#include "hw/sysbus.h"

#define TYPE_{{peripheral_name|upper}} "{{peripheral_name|upper}}"
#define {{peripheral_name|upper}}(obj) \
    OBJECT_CHECK({{peripheral_name|upper|concat}}State, (obj),  TYPE_{{peripheral_name|upper}})

typedef struct {{peripheral_name|upper}}PeripheralsState {
    /*< private >*/
    SysBusDevice sys_bus;
    /*< public >*/

    MemoryRegion peri_mr;
    qemu_irq irq, fiq;

    {{ic_name|upper|concat}}State ic;
} {{peripheral_name|upper|concat}}State;

#endif /* {{peripheral_name|upper}}_H */