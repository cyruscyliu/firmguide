{{license}}

#ifndef {{peripheral_name|upper}}_H
#define {{peripheral_name|upper}}_H

#include "hw/sysbus.h"
#include "hw/timer/{{timer_name}}.h"
#include "hw/char/{{uart_name}}.h"
#include "hw/gpio/{{gpio_name}}.h"
#include "hw/pci-host/{{pcie_name}}.h"

#define TYPE_{{peripheral_name|upper}} "{{peripheral_name}}"
#define {{peripheral_name|upper}}(obj) \
    OBJECT_CHECK({{peripheral_name|upper|concat}}State, (obj),  TYPE_{{peripheral_name|upper}})

{% for register in bridge_registers %}
#define {{register.name|upper}} {{register.offset}}{% endfor %}

#define {{bridge_mmio_name|upper}}_RAM_SIZE {{bridge_mmio_size}}
#define {{bridge_mmio_name|upper}}_RAM_BASE {{bridge_mmio_base}}

#define {{bridge_mmio_name|upper}}_IRQ "{{bridge_mmio_name}}_irq"

typedef struct {{peripheral_name|upper|concat}}State {
    /*< private >*/
    SysBusDevice sys_bus;
    /*< public >*/

    MemoryRegion bridge_mmio;
    qemu_irq irq;

    {% for register in bridge_registers %}uint32_t {{register.name}};
    {% endfor %}
    {{timer_name|upper|concat}}State timer;
    {{uart_name|upper|concat}}State uart;
    {{gpio_name|upper|concat}}State gpio;
    {{pcie_name|upper|concat}}State pcie;
} {{peripheral_name|upper|concat}}State;

#endif /* {{peripheral_name|upper}}_H */