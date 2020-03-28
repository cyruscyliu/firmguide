/*
 * automatically generated, don't change
 */

#ifndef MARVELL_ORION_BRIDGE_INTC_H
#define MARVELL_ORION_BRIDGE_INTC_H

#include "hw/sysbus.h"

#define TYPE_MARVELL_ORION_BRIDGE_INTC "marvell_orion_bridge_intc"
#define MARVELL_ORION_BRIDGE_INTC(obj) \
    OBJECT_CHECK(MARVELL_ORION_BRIDGE_INTCState, (obj), TYPE_MARVELL_ORION_BRIDGE_INTC)

/*
 * interrupt actions
 */
#define STATE_REST      0
#define STATE_NOISE     1
#define STATE_ALARM     2

#define N_IRQ           32

typedef struct MARVELL_ORION_BRIDGE_INTCState {
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
} MARVELL_ORION_BRIDGE_INTCState;

#endif /* MARVELL_ORION_BRIDGE_INTC_H */

