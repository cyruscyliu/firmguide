/*
 * automatically generated, don't change
 */

#ifndef PLXTECH_NAS782X_RPS_TIMER_H
#define PLXTECH_NAS782X_RPS_TIMER_H

#include "hw/sysbus.h"
#include "qemu/timer.h"

#define TYPE_PLXTECH_NAS782X_RPS_TIMER "plxtech_nas782x_rps_timer"
#define PLXTECH_NAS782X_RPS_TIMER(obj) \
    OBJECT_CHECK(PLXTECH_NAS782X_RPS_TIMERState, (obj), TYPE_PLXTECH_NAS782X_RPS_TIMER)

typedef struct PLXTECH_NAS782X_RPS_TIMERState {
    /*< private >*/
    SysBusDevice sys_bus;
    /*< public >*/

    MemoryRegion mmio;
    /* output to the intc */
    qemu_irq irq[1];
    QEMUTimer *timer[1];
    uint32_t counter[1];

    uint32_t reserved;
} PLXTECH_NAS782X_RPS_TIMERState;

#endif /* PLXTECH_NAS782X_RPS_TIMER_H */
