/*
 * automatically generated, don't change
 */

#ifndef PLXTECH_NAS782X_RPS_TIMER_H
#define PLXTECH_NAS782X_RPS_TIMER_H

#include "hw/sysbus.h"
#include "hw/ptimer.h"

#define TYPE_PLXTECH_NAS782X_RPS_TIMER "plxtech_nas782x_rps_timer"
#define PLXTECH_NAS782X_RPS_TIMER(obj) \
    OBJECT_CHECK(PLXTECH_NAS782X_RPS_TIMERState, (obj), TYPE_PLXTECH_NAS782X_RPS_TIMER)

typedef struct PLXTECH_NAS782X_RPS_TIMERState {
    /*< private >*/
    SysBusDevice sys_bus;
    /*< public >*/

    MemoryRegion mmio;

    qemu_irq irq[1];

    /* timer for clock source */
    ptimer_state *ptimer[1];
    /* timer for clock event */
    QEMUTimer *timer[1];

} PLXTECH_NAS782X_RPS_TIMERState;

#endif /* PLXTECH_NAS782X_RPS_TIMER_H */
