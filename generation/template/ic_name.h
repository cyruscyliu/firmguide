{{license}}

#ifndef {{ic_name|upper}}_H
#define {{ic_name|upper}}_H

#include "hw/sysbus.h"

#define TYPE_{{ic_name|upper}} "{{ic_name}}"
#define {{ic_name|upper}}(obj) \
    OBJECT_CHECK({{ic_name|upper|concat}}State, (obj), TYPE_{{ic_name|upper}})

#define {{ic_name|upper}}_IRQ "{{ic_name}}_irq"
#define {{ic_name|upper}}_N_IRQS {{ic_n_irqs}}
{% for register in ic_registers %}
#define {{register.name|upper}} {{register.offset}}{% endfor %}

#define {{ic_name|upper}}_RAM_SIZE {{ic_mmio_size}}
#define {{ic_name|upper}}_RAM_BASE {{ic_mmio_base}}

typedef struct {{ic_name|upper|concat}}State {
    /*< private >*/
    SysBusDevice sys_bus;
    /*< public >*/

    MemoryRegion mmio;
    /* output to the cpu */
    qemu_irq irq;

    {% for register in ic_registers %}uint32_t {{register.name}};
    {% endfor %}

} {{ic_name|upper|concat}}State;

#endif /* {{ic_name|upper}}_H */