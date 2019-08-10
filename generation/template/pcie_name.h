{{license}}

#ifndef {{pcie_name|upper}}_H
#define {{pcie_name|upper}}_H

#include "hw/sysbus.h"

#define TYPE_{{pcie_name|upper}} "{{pcie_name}}"
#define {{pcie_name|upper}}(obj) \
    OBJECT_CHECK({{pcie_name|upper|concat}}State, (obj), TYPE_{{pcie_name|upper}})
{% for register in pcie_registers %}
#define {{register.name|upper}} {{register.offset}}{% endfor %}

#define {{pcie_name|upper}}_MMIO_SIZE {{pcie_mmio_size}}
#define {{pcie_name|upper}}_MMIO_BASE {{pcie_mmio_base}}

typedef struct {{pcie_name|upper|concat}}State {
    /*< private >*/
    SysBusDevice sys_bus;
    /*< public >*/

    MemoryRegion mmio;
    {% for register in pcie_registers %}uint32_t {{register.name}};
    {% endfor %}
} {{pcie_name|upper|concat}}State;

#endif /* {{pcie_name|upper}}_H */