{{license}}

#ifndef {{soc_name|upper}}_H
#define {{soc_name|upper}}_H

#include "hw/arm/arm.h"
#include "hw/intc/{{ic_name}}.h"
#include "hw/arm/{{peripheral_name}}.h"

#define TYPE_{{soc_name|upper}} "{{soc_name}}"
#define {{soc_name|upper}}(obj) \
    OBJECT_CHECK({{soc_name|upper}}State, (obj), TYPE_{{soc_name|upper}})
{% for register in cam_registers %}
#define {{register.name|upper}} {{register.offset}}{% endfor %}
{% for register in dsc_registers %}
#define {{register.name|upper}} {{register.offset}}{% endfor %}
{% for register in mpp_registers %}
#define {{register.name|upper}} {{register.offset}}{% endfor %}
{% for register in pci_registers %}
#define {{register.name|upper}} {{register.offset}}{% endfor %}
{% for register in pcie_registers %}
#define {{register.name|upper}} {{register.offset}}{% endfor %}
{% for register in eth_registers %}
#define {{register.name|upper}} {{register.offset}}{% endfor %}

#define {{cam_mmio_name|upper}}_MMIO_SIZE {{cam_mmio_size}}
#define {{cam_mmio_name|upper}}_MMIO_BASE {{cam_mmio_base}}
#define {{dsc_mmio_name|upper}}_MMIO_SIZE {{dsc_mmio_size}}
#define {{dsc_mmio_name|upper}}_MMIO_BASE {{dsc_mmio_base}}
#define {{mpp_mmio_name|upper}}_MMIO_SIZE {{mpp_mmio_size}}
#define {{mpp_mmio_name|upper}}_MMIO_BASE {{mpp_mmio_base}}
#define {{pci_name|upper}}_MMIO_SIZE {{pci_mmio_size}}
#define {{pci_name|upper}}_MMIO_BASE {{pci_mmio_base}}
#define {{pcie_name|upper}}_MMIO_SIZE {{pcie_mmio_size}}
#define {{pcie_name|upper}}_MMIO_BASE {{pcie_mmio_base}}
#define {{eth_name|upper}}_MMIO_SIZE {{eth_mmio_size}}
#define {{eth_name|upper}}_MMIO_BASE {{eth_mmio_base}}

typedef struct {{soc_name|upper}}State {
    /*< private >*/
    SysBusDevice sys_bus;
    /*< public >*/

    const char *cpu_type;
    ARMCPU *cpu;
    qemu_irq irq, fiq;

    MemoryRegion cpu_address_map_mmio;
    {% for register in cam_registers %}uint32_t {{register.name}};
    {% endfor %}
    MemoryRegion ddr_sdram_controller_mmio;
    {% for register in dsc_registers %}uint32_t {{register.name}};
    {% endfor %}
    MemoryRegion pins_multiplexing_interface_mmio;
    {% for register in mpp_registers %}uint32_t {{register.name}};
    {% endfor %}
    MemoryRegion pci_interface_mmio;
    {% for register in pci_registers %}uint32_t {{register.name}};
    {% endfor %}
    MemoryRegion pcie_interface_mmio;
    {% for register in pcie_registers %}uint32_t {{register.name}};
    {% endfor %}
    MemoryRegion gigabit_ethernet_controller_mmio;
    {% for register in eth_registers %}uint32_t {{register.name}};
    {% endfor %}
    {{ic_name|upper|concat}}State ic;
    {{peripheral_name|upper|concat}}State peripherals;
} {{soc_name|upper}}State;

#endif /* {{soc_name|upper}}_H */