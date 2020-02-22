/*
 * Salamander Generic Timer
 */

#ifndef SLGTIMER_H
#define SLGTIMER_H

#include "hw/sysbus.h"
#include "qemu/timer.h"

#define TYPE_SLGTIMER "slgtimer"
#define SLGTimer(obj) \
    OBJECT_CHECK(SLGTimerState, (obj), TYPE_SLGTIMER)

typedef struct SLGTimerState {
    /*< private >*/
    SysBusDevice sys_bus;
    /*< public >*/

    /* output to the intc */
    qemu_irq irq;

    QEMUTimer *timer;
} SLGTimerState;

#endif /* SLGTIMER_H */
