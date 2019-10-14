{{license}}

#ifndef {{bridge_name|upper}}_H
#define {{bridge_name|upper}}_H

#include "hw/sysbus.h"

#define TYPE_{{bridge_name|upper}} "{{bridge_name}}"
#define {{bridge_name|upper}}(obj) \
    OBJECT_CHECK({{bridge_name|upper|concat}}State, (obj),  TYPE_{{bridge_name|upper}})

{% for register in bridge_registers %}
#define {{register.name|upper}} {{register.offset}}{% endfor %}

#define {{bridge_name|upper}}_MMIO_SIZE {{bridge_mmio_size}}
#define {{bridge_name|upper}}_MMIO_BASE {{bridge_mmio_base}}
#define {{bridge_name|upper}}_IRQ "{{bridge_name}}_irq"

typedef struct {{bridge_name|upper|concat}}State {
    /*< private >*/
    SysBusDevice sys_bus;
    /*< public >*/

    MemoryRegion bridge_mmio;
    qemu_irq irq;

    {% for register in bridge_registers %}uint32_t {{register.name}};
    {% endfor %}
} {{bridge_name|upper|concat}}State;

#endif /* {{bridge_name|upper}}_H */