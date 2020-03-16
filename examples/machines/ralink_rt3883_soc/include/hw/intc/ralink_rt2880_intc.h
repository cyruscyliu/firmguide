/*
 * automatically generated, don't change
 */

#ifndef RALINK_RT2880_INTC_H
#define RALINK_RT2880_INTC_H

#include "hw/sysbus.h"

#define TYPE_RALINK_RT2880_INTC "ralink_rt2880_intc"
#define RALINK_RT2880_INTC(obj) \
    OBJECT_CHECK(RALINK_RT2880_INTCState, (obj), TYPE_RALINK_RT2880_INTC)

/*
 * interrupt actions
 */
#define STATE_REST      0
#define STATE_NOISE     1
#define STATE_ALARM     2

#define N_IRQ           32

typedef struct RALINK_RT2880_INTCState {
    /*< private >*/
    SysBusDevice sys_bus;
    /*< public >*/

    MemoryRegion mmio;
    /* output to the parent device */
    qemu_irq irq;
    /* registers known by the outside */
    uint32_t r0;
    uint32_t r1;
    uint32_t r2;
    /* internal state for every interrupt source */
    uint32_t state[N_IRQ];
    bool pending[N_IRQ];
    bool masked[N_IRQ];
} RALINK_RT2880_INTCState;

#endif /* RALINK_RT2880_INTC_H */

