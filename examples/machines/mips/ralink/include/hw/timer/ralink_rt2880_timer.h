/*
 * automatically generated, don't change
 */

#ifndef RALINK_RT2880_TIMER_H
#define RALINK_RT2880_TIMER_H

#include "hw/sysbus.h"
#include "qemu/timer.h"

#define TYPE_RALINK_RT2880_TIMER "ralink_rt2880_timer"
#define RALINK_RT2880_TIMER(obj) \
    OBJECT_CHECK(RALINK_RT2880_TIMERState, (obj), TYPE_RALINK_RT2880_TIMER)

typedef struct RALINK_RT2880_TIMERState {
    /*< private >*/
    SysBusDevice sys_bus;
    /*< public >*/

    MemoryRegion mmio;
    /* output to the intc */
    qemu_irq irq[1];
    QEMUTimer *timer[1];

    uint32_t reserved;
} RALINK_RT2880_TIMERState;

#endif /* RALINK_RT2880_TIMER_H */

