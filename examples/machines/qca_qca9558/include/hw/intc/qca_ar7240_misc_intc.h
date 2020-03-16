/*
 * automatically generated, don't change
 */

#ifndef QCA_AR7240_MISC_INTC_H
#define QCA_AR7240_MISC_INTC_H

#include "hw/sysbus.h"

#define TYPE_QCA_AR7240_MISC_INTC "qca_ar7240_misc_intc"
#define QCA_AR7240_MISC_INTC(obj) \
    OBJECT_CHECK(QCA_AR7240_MISC_INTCState, (obj), TYPE_QCA_AR7240_MISC_INTC)

/*
 * interrupt actions
 */
#define STATE_REST      0
#define STATE_NOISE     1
#define STATE_ALARM     2

#define N_IRQ           32

typedef struct QCA_AR7240_MISC_INTCState {
    /*< private >*/
    SysBusDevice sys_bus;
    /*< public >*/

    MemoryRegion mmio;
    /* output to the parent device */
    qemu_irq irq;
    /* registers known by the outside */
    uint32_t r0;
    uint32_t r1;
    /* internal state for every interrupt source */
    uint32_t state[N_IRQ];
    bool pending[N_IRQ];
    bool masked[N_IRQ];
} QCA_AR7240_MISC_INTCState;

#endif /* QCA_AR7240_MISC_INTC_H */

