{{license}}

#ifndef {{gpio_name|upper}}_H
#define {{gpio_name|upper}}_H

#include "hw/sysbus.h"

#define TYPE_{{gpio_name|upper}} "{{gpio_name}}"
#define {{gpio_name|upper}}(obj) \
    OBJECT_CHECK({{gpio_name|upper|concat}}State, (obj), TYPE_{{gpio_name|upper}})
{% for register in gpio_registers %}
#define {{register.name|upper}} {{register.offset}}{% endfor %}

#define {{gpio_name|upper}}_MMIO_SIZE {{gpio_mmio_size}}
#define {{gpio_name|upper}}_MMIO_BASE {{gpio_mmio_base}}

typedef struct {{gpio_name|upper|concat}}State {
    /*< private >*/
    SysBusDevice sys_bus;
    /*< public >*/

    MemoryRegion gpio_mmio;
    qemu_irq irq[{{gpio_irq_n}}]
    qemu_irq out[{{gpio_in_out_n}}];

    {% for register in gpio_registers %}uint32_t {{register.name}};
    {% endfor %}
} {{gpio_name|upper|concat}}State;

#endif /* {{gpio_name|upper}}_H */