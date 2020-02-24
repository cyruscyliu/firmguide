{{ license }}

#ifndef {{ name|upper }}_H
#define {{ name|upper }}_H

#include "hw/sysbus.h"
#include "qemu/timer.h"

#define TYPE_{{ name|upper }} "{{ name }}"
#define {{ name|upper }}(obj) \
    OBJECT_CHECK({{ name|upper }}State, (obj), TYPE_{{ name|upper }})

typedef struct {{ name|upper }}State {
    /*< private >*/
    SysBusDevice sys_bus;
    /*< public >*/

    MemoryRegion mmio;
    /* output to the intc */
    qemu_irq irq[{{ irqc }}];
    QEMUTimer *timer[{{ irqc }}];

    uint32_t reserved;
} {{ name|upper }}State;

#endif /* {{ name|upper }}_H */

