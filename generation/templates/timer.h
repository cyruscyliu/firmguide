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

#define {{timer_name|upper}}_MMIO_SIZE {{timer_mmio_size}}
#define {{timer_name|upper}}_MMIO_BASE {{timer_mmio_base}}

typedef struct {{timer_name|upper|concat}}State {
    /* <private> */
    SysBusDevice sys_bus;
    /* <public> */

    MemoryRegion mmio;
    QEMUTimer *timer;
    qemu_irq irq_0, irq_1;

    {% for register in timer_registers %}uint32_t {{register.name}};
    {% endfor %}
    uint32_t reserved_0;
    uint32_t reserved_1;
    uint32_t reserved_2;
} {{timer_name|upper|concat}}State;

#endif /* {{timer_name|upper}}_H */
