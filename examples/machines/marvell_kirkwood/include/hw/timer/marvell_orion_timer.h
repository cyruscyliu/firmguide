/*
 * automatically generated, don't change
 */

#ifndef MARVELL_ORION_TIMER_H
#define MARVELL_ORION_TIMER_H

#include "hw/sysbus.h"
#include "hw/ptimer.h"

#define TYPE_MARVELL_ORION_TIMER "marvell_orion_timer"
#define MARVELL_ORION_TIMER(obj) \
    OBJECT_CHECK(MARVELL_ORION_TIMERState, (obj), TYPE_MARVELL_ORION_TIMER)

typedef struct MARVELL_ORION_TIMERState {
    /*< private >*/
    SysBusDevice sys_bus;
    /*< public >*/

    MemoryRegion mmio;

    qemu_irq irq[2];

    /* timer for clock source */
    ptimer_state *ptimer[2];
    /* timer for clock event */
    QEMUTimer *timer[2];

} MARVELL_ORION_TIMERState;

#endif /* MARVELL_ORION_TIMER_H */
