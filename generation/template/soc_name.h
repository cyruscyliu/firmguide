{{license}}

#ifndef {{soc_name|upper}}_H
#define {{soc_name|upper}}_H

#include "hw/arm/arm.h"
#include "hw/intc/{{ic_name}}.h"

#define TYPE_{{soc_name|upper}} "{{soc_name}}"
#define {{soc_name|upper}}(obj) \
    OBJECT_CHECK({{soc_name|upper}}State, (obj), TYPE_{{soc_name|upper}})
{% for device in bamboo %}{% for register in device.registers %}
#define {{register.name|upper}} {{register.offset}}{% endfor %}{% endfor %}
{% for device in bamboo %}
#define {{device.name|upper}}_MMIO_SIZE {{device.mmio_size}}
#define {{device.name|upper}}_MMIO_BASE {{device.mmio_base}}{% endfor %}

#define {{uart_name|upper}}_MMIO_SIZE {{uart_mmio_size}}
#define {{uart_name|upper}}_MMIO_BASE {{uart_mmio_base}}

typedef struct {{soc_name|upper}}State {
    /*< private >*/
    SysBusDevice sys_bus;
    /*< public >*/

    const char *cpu_type;
    ARMCPU *cpu;
    qemu_irq irq, fiq;

    {% for device in bamboo %}MemoryRegion {{device.name}}_mmio;
    {% for register in device.registers %}uint32_t {{register.name}};
    {% endfor %}{% endfor %}
    {{ic_name|upper|concat}}State ic;
    {{timer_name|upper|concat}}State timer;
} {{soc_name|upper}}State;

#endif /* {{soc_name|upper}}_H */