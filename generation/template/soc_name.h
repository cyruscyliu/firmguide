{{license}}

#ifndef {{soc_name|upper}}_H
#define {{soc_name|upper}}_H

#include "hw/arm/arm.h"
#include "hw/intc/{{ic_name}}.h"
#include "hw/arm/{{peripheral_name}}.h"

#define TYPE_{{soc_name|upper}} "{{soc_name}}"
#define {{soc_name|upper}}(obj) \
    OBJECT_CHECK({{soc_name|upper}}State, (obj), TYPE_{{soc_name|upper}})

#define {{peripheral_name|upper}}_RAM_BASE {{peripheral_ram_base}}
#define {{ic_name|upper}}_RAM_BASE {{ic_ram_base}}

#define TIMER_INTERRUPT 0

typedef struct {{soc_name|upper}}State {
    /*< private >*/
    DeviceState parent_obj;
    /*< public >*/

    char *cpu_type;
    ARMCPU *cpu;
    qemu_irq irq, fiq;

    {{ic_name|upper|concat}}State ic;
    {{peripheral_name|upper|concat}}State peripherals;
} {{soc_name|upper}}State;

static void {{soc_name}}_realize(DeviceState *dev, Error **errp);

static void {{soc_name}}_init(Object *obj);
static void {{soc_name}}_class_init(ObjectClass *oc, void *data);
static void {{soc_name}}_register_types(void);

#endif /* {{soc_name|upper}}_H */