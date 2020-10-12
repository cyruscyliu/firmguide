{{ license }}

#ifndef {{ name|to_upper }}_H
#define {{ name|to_upper }}_H

#include "hw/sysbus.h"
#include "qemu/timer.h"
#include "hw/ptimer.h"

#define TYPE_{{ name|to_upper }} "{{ name }}"
#define {{ name|to_upper }}(obj) \
    OBJECT_CHECK({{ name|to_upper }}State, (obj), TYPE_{{ name|to_upper }})

typedef struct {{ name|to_upper }}State {
    /*< private >*/
    SysBusDevice sys_bus;
    /*< public >*/

    MemoryRegion mmio;

    qemu_irq irq[{{ timer_n_irq }}];

    /* timer for clock source */
    ptimer_state *ptimer[{{ timer_n_irq }}];
    /* timer for clock event */
    QEMUTimer *timer[{{ timer_n_irq }}];

} {{ name|to_upper }}State;

#endif /* {{ name|to_upper }}_H */
