{{ license }}

#ifndef {{ name|to_upper }}_H
#define {{ name|to_upper }}_H

#include "hw/sysbus.h"
#include "hw/ptimer.h"

#define TYPE_{{ name|to_upper }} "{{ name }}"
#define {{ name|to_upper }}(obj) \
    OBJECT_CHECK({{ name|to_upper }}State, (obj), TYPE_{{ name|to_upper }})

typedef struct {{ name|to_upper }}State {
    /*< private >*/
    SysBusDevice sys_bus;
    /*< public >*/

    MemoryRegion mmio;
    /* output to the intc */
    qemu_irq irq[{{ timer_n_irq }}];
    QEMUBH *bh[{{ timer_n_irq }}];
    ptimer_state *timer[{{ timer_n_irq }}];

    uint32_t reserved;
} {{ name|to_upper }}State;

#endif /* {{ name|to_upper }}_H */
