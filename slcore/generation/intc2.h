{{ license }}

#ifndef {{ name|upper }}_H
#define {{ name|upper }}_H

#include "hw/sysbus.h"

#define TYPE_{{ name|upper }} "{{ name }}"
#define {{ name|upper }}(obj) \
    OBJECT_CHECK({{ name|upper }}State, (obj), TYPE_{{ name|upper }})

#define STATE_IDLE      0
#define STATE_SET_SLARM 1
#define STATE_MASK_ACK  2
#define STATE_MASK      3
#define STATE_CLAER     4
#define STATE_UNMASK    5

struct {{ name }}_to_reg {
    const uint32_t offset;
    const uint32_t value;
    const uint32_t size;
}

struct {{ name }}_irqn_table_entry {
    const int32_t irqn;
    const int32_t n_to_reg;
    struct {{ name }}_to_reg *to_regs;
}

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

