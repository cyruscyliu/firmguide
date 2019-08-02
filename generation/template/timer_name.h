{{license}}

#include "hw/sysbus.h"
#include "qemu/timer.h"

#ifndef {{timer_name|upper}}_H
#define {{timer_name|upper}}_H

#define TYPE_{{timer_name|upper}} "{{timer_name}}"
#define {{timer_name|upper}}(obj) \
    OBJECT_CHECK({{timer_name|upper|concat}}State, (obj), TYPE_{{timer_name|upper}})
{% for register in timer_registers %}
#define {{register.name|upper}} {{register.offset}}{% endfor %}

#define {{timer_name|upper}}_RAM_SIZE {{timer_ram_size}}
#define {{timer_name|upper}}_RAM_BASE {{timer_ram_base}}

typedef struct {{timer_name|upper|concat}}State {
    /* <private> */
    SysBusDevice sys_bus;
    /* <public> */

    MemoryRegion mmio;
    QEMUTimer *timer;
    qemu_irq irq;

    {% for register in timer_registers %}uint32_t {{register.name}};
    {% endfor %}
} {{timer_name|upper|concat}}State;

#endif /* {{timer_name|upper}}_H */
