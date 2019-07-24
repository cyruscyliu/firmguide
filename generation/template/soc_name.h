{{license}}

#ifndef {{soc_name|upper}}_H
#define {{soc_name|upper}}_H

#include "hw/sysbus.h"
#include "hw/initc/{{soc_name}}_ic.h"
#include "hw/gpio/{{soc_name}}_gpio"

#define TYPE_{{soc_name|upper}} "{{soc_name}}"
#define {{soc_name|upper}}(obj) \
    OBJECT_CHECK({{soc_name|upper}}State, (obj), TYPE_{{soc_name|upper}})

#define {{peripheral_name|upper}}_RAM_BASE {{peripheral_ram_base}}
#define {{ic_name|upper}}_RAM_BASE {{ic_ram_base}}

typedef struct {{soc_name|upper}}State {
    /*< private >*/
    DeviceState parent_obj;
    /*< public >*/

    char *cpu_type;
    ARMCPU cpu;
    qemu_irq irq, fiq;

    {{ic_name|upper|concat}}State ic;
    {{peripheral_name|upper|concat}}State peripherals;
} {{soc_name|upper}}State;

#endif /* {{soc_name|upper}}_H */