{{ license }}

#ifndef {{ name|to_upper }}_H
#define {{ name|to_upper }}_H

#include "hw/sysbus.h"

#define TYPE_{{ name|to_upper }} "{{ name }}"
#define {{ name|to_upper }}(obj) \
    OBJECT_CHECK({{ name|to_upper }}State, (obj), TYPE_{{ name|to_upper }})

/*
 * interrupt actions
 */
#define STATE_REST      0
#define STATE_NOISE     1
#define STATE_ALARM     2

#define N_IRQ           {{ intc_n_irq }}

typedef struct {{ name|to_upper }}State {
    /*< private >*/
    SysBusDevice sys_bus;
    /*< public >*/

    MemoryRegion mmio;
    /* output to the parent device */
    qemu_irq irq;
    /* registers known by the outside */{% for register in intc_get_registers %}
    uint32_t {{ register.rname }};{% endfor %}
    /* internal state for every interrupt source */
    uint32_t state[N_IRQ];
    bool pending[N_IRQ];
    bool masked[N_IRQ];
} {{ name|to_upper }}State;

#endif /* {{ name|to_upper }}_H */
