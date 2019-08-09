{{license}}

#include "hw/sysbus.h"
#include "chardev/char-fe.h"

#ifndef {{uart_name|upper}}_H
#define {{uart_name|upper}}_H

#define TYPE_{{uart_name|upper}} "{{uart_name}}"
#define {{uart_name|upper}}(obj) \
    OBJECT_CHECK({{uart_name|upper|concat}}State, (obj), TYPE_{{uart_name|upper}})
{% for register in uart_registers %}
#define {{register.name|upper}} {{register.offset}}{% endfor %}

#define {{uart_name|upper}}_MMIO_SIZE {{uart_mmio_size}}
#define {{uart_name|upper}}_MMIO_BASE {{uart_mmio_base}}

typedef struct {{uart_name|upper|concat}}State {
    /* <private> */
    SysBusDevice sys_bus;
    /* <public> */

    qemu_irq irq;
    CharBackend chr;

    MemoryRegion mmio;
    {% for register in uart_registers %}uint32_t {{register.name}};
    {% endfor %}
} {{uart_name|upper|concat}}State;

#endif /* {{uart_name|upper}}_H */