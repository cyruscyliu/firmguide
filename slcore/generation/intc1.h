{{ license }}

#ifndef {{ name|upper }}_H
#define {{ name|upper }}_H

#include "hw/sysbus.h"

#define TYPE_{{ name|upper }} "{{ name }}"
#define {{ name|upper }}(obj) \
    OBJECT_CHECK({{ name|upper }}State, (obj), TYPE_{{ name|upper }})

#define STATE_IDLE      0
#define STATE_SET_ALARM 1
#define STATE_MASK_ACK  2
#define STATE_MASK      3
#define STATE_CLEAR     4
#define STATE_UNMASK    5

struct {{ name }}_to_reg {
    uint32_t offset;
    uint32_t value;
    uint32_t size;
};

struct {{ name }}_irqn_table_entry {
    int32_t irqn;
    struct {{ name }}_to_reg *to_regs;
};

typedef struct {{ name|upper }}State {
    /*< private >*/
    SysBusDevice sys_bus;
    /*< public >*/

    MemoryRegion mmio;
    /* output to the parent device */
    qemu_irq irq;
    /* registers known by the outside */{% for register in intc_get_registers %}
    uint32_t {{ register.rname }};{% endfor %}
    /* internal state for every interrupt source */
    uint32_t state[32];
} {{ name|upper }}State;

#endif /* {{ name|upper }}_H */

