/*
 * automatically generated, don't change
 */

#ifndef MARVELL_ORION_TIMER_H
#define MARVELL_ORION_TIMER_H

#include "hw/sysbus.h"
#include "qemu/timer.h"

#define TYPE_MARVELL_ORION_TIMER "marvell_orion_timer"
#define MARVELL_ORION_TIMER(obj) \
    OBJECT_CHECK(MARVELL_ORION_TIMERState, (obj), TYPE_MARVELL_ORION_TIMER)

typedef struct MARVELL_ORION_TIMERState {
    /*< private >*/
    SysBusDevice sys_bus;
    /*< public >*/

    MemoryRegion mmio;
    /* output to the intc */
    qemu_irq irq[2];
    QEMUTimer *timer[2];
    uint32_t counter[2];

    uint32_t reserved;
} MARVELL_ORION_TIMERState;

#endif /* MARVELL_ORION_TIMER_H */

