#ifndef {{peripheral_name|upper}}_H
#define {{peripheral_name|upper}}_H

#include "hw/sysbus.h"
#include "hw/initc/{{soc_name}}_ic.h"
#include "hw/gpio/{{soc_name}}_gpio"

#define TYPE_{{peripheral_name|upper}} "{{peripheral_name|upper}}"
#define {{peripheral_name|upper}}(obj) \
    OBJECT_CHECK({{peripheral_name|upper}}State, (obj),  TYPE_{{peripheral_name|upper}})

typedef struct {{peripheral_name|upper}}State {
    /*< private >*/
    SysBusDevice sys_bus;
    /*< public >*/

    MemoryRegion peri_mr;
    qemu_irq irq, fiq;

    {{soc_name|upper}}ICState ic;
    {{soc_name|upper}}GPIOState gpio;

} {{peripheral_name|upper}}State;

#endif /* {{peripheral_name|upper}}_H */