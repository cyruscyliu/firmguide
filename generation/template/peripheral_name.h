{{license}}

#ifndef {{peripheral_name|upper}}_H
#define {{peripheral_name|upper}}_H

#include "hw/sysbus.h"
#include "hw/timer/{{timer_name}}.h"

#define TYPE_{{peripheral_name|upper}} "{{peripheral_name|upper}}"
#define {{peripheral_name|upper}}(obj) \
    OBJECT_CHECK({{peripheral_name|upper|concat}}State, (obj),  TYPE_{{peripheral_name|upper}})
#define {{peripheral_name|upper}}_RAM_SIZE {{peripheral_ram_size}}

#define {{timer_name|upper}}_RAM_BASE {{timer_ram_base}}

typedef struct {{peripheral_name|upper|concat}}State {
    /*< private >*/
    SysBusDevice sys_bus;
    /*< public >*/

    MemoryRegion mmio;
    {{timer_name|upper|concat}}State timer;
} {{peripheral_name|upper|concat}}State;

static void {{peripheral_name}}_realize(DeviceState *dev, Error **errp);

static void {{peripheral_name}}_init(Object *obj);
static void {{peripheral_name}}_class_init(ObjectClass *oc, void *data);
static void {{peripheral_name}}_register_types(void);

#endif /* {{peripheral_name|upper}}_H */