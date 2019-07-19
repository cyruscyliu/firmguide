#ifndef MV88F5181L_IC_H
#define MV88F5181L_IC_H

#include "hw/sysbus.h"

#define TYPE_MV88F5181L_IC "mv88f5181L-ic"
#define MV88F5181L_IC(obj) OBJECT_CHECK(MV88F5181LICState, (obj), TYPE_MV88F5181L_IC)

#define MV88F5181L_IC_IRQ "mv88f5181L-irq"

typedef struct MV88F5181LICState {
    /*< private >*/
    SysBusDevice sysbus;
    /*< public >*/

    MemoryRegion mmio;
    qemu_irq irq;
    qemu_irq fiq;

    /* 32 IRQs */
    uint32_t irq_level_0, irq_enable_0;

    bool fiq_enable;
    uint8_t fiq_select;
} MV88F5181LICState