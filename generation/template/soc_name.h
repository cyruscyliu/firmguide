{{license}}

#ifndef {{soc_name|upper}}_H
#define {{soc_name|upper}}_H

#include "hw/arm/arm.h"
#include "hw/intc/{{ic_name}}.h"
#include "hw/arm/{{peripheral_name}}.h"

#define TYPE_{{soc_name|upper}} "{{soc_name}}"
#define {{soc_name|upper}}(obj) \
    OBJECT_CHECK({{soc_name|upper}}State, (obj), TYPE_{{soc_name|upper}})

#define {{soc_mmio_name|upper}}_RAM_SIZE {{soc_mmio_size}}
#define {{soc_mmio_name|upper}}_RAM_BASE {{soc_mmio_base}}

typedef struct {{soc_name|upper}}State {
    /*< private >*/
    DeviceState parent_obj;
    /*< public >*/

    const char *cpu_type;
    ARMCPU *cpu;
    qemu_irq irq, fiq;

    MemoryRegion cpu_address_map_mmio;
    {% for register in soc_registers %}uint32_t {{register.name}};
    {% endfor %}
    {{ic_name|upper|concat}}State ic;
    {{peripheral_name|upper|concat}}State peripherals;
} {{soc_name|upper}}State;

#endif /* {{soc_name|upper}}_H */