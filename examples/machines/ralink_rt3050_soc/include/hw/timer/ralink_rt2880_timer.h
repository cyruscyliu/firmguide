/*
 * automatically generated, don't change
 */

#ifndef RALINK_RT2880_TIMER_H
#define RALINK_RT2880_TIMER_H

#include "hw/sysbus.h"
#include "hw/ptimer.h"

#define TYPE_RALINK_RT2880_TIMER "ralink_rt2880_timer"
#define RALINK_RT2880_TIMER(obj) \
    OBJECT_CHECK(RALINK_RT2880_TIMERState, (obj), TYPE_RALINK_RT2880_TIMER)

typedef struct RALINK_RT2880_TIMERState {
    /*< private >*/
    SysBusDevice sys_bus;
    /*< public >*/

    MemoryRegion mmio;

    qemu_irq irq[1];

    /* timer for clock source */
    ptimer_state *ptimer[1];
    /* timer for clock event */
    QEMUTimer *timer[1];

} RALINK_RT2880_TIMERState;

#endif /* RALINK_RT2880_TIMER_H */
