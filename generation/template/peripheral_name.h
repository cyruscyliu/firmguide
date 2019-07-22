{{license}}

#ifndef {{peripheral_name|upper}}_H
#define {{peripheral_name|upper}}_H

#include "hw/sysbus.h"

#define TYPE_{{peripheral_name|upper}} "{{peripheral_name|upper}}"
#define {{peripheral_name|upper}}(obj) \
    OBJECT_CHECK({{soc_name|upper}}PeripheralsState, (obj),  TYPE_{{peripheral_name|upper}})

typedef struct {{soc_name|upper}}PeripheralsState {
    /*< private >*/
    SysBusDevice sys_bus;
    /*< public >*/

    MemoryRegion peri_mr;
    qemu_irq irq, fiq;

    {{soc_name|upper}}ICState ic;
} {{soc_name|upper}}PeripheralsState;

#endif /* {{peripheral_name|upper}}_H */