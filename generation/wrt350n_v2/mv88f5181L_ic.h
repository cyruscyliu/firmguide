/* 
 * automatically generated, don't change
 */

#ifndef MV88F5181L_IC_H
#define MV88F5181L_IC_H

#include "hw/sysbus.h"

#define TYPE_MV88F5181L_IC "mv88f5181L_ic"
#define MV88F5181L_IC(obj) \
    OBJECT_CHECK(MV88F5181LICState, (obj), TYPE_MV88F5181L_IC)

#define MV88F5181L_IC_IRQ "irq"

#define MAIN_INTERRUPT_CAUSE_REGISTER         0x00
#define MAIN_IRQ_INTERRUPT_MASK_REGISTER      0x04
#define MAIN_FIQ_INTERRUPT_MASK_REGISTER      0x08
#define MAIN_ENDPOINT_INTERRUPT_MASK_REGISTER 0x0C

typedef struct MV88F5181LICState {
    /*< private >*/
    SysBusDevice sysbus;
    /*< public >*/

    MemoryRegion mmio;
    qemu_irq irq;
    qemu_irq fiq;

    /* 32 IRQs */
    uint32_t irq_level_0;
    uint32_t irq_enable_0;
    uint32_t fiq_enable_0;
} MV88F5181LICState;

#endif /* MV88F5181L_IC_H */