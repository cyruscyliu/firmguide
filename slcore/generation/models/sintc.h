{{license}}

#ifndef SINTC_H
#define SINTC_H

#include "hw/sysbus.h"
#include "qemu/timer.h"

#define TYPE_SINTC "sintc"
#define SINTC(obj) \
    OBJECT_CHECK(SIntCState, (obj), TYPE_SINTC)

#define INTERRUPT_CAUSE_REGISTER {{interrupt_cause_register.offset}}
#define INTERRUPT_MASK_REGISTER  {{interrupt_mask_register.offset}}
#define INTERRUPT_CLEAR_REGISTER {{interrupt_clear_register.offset}}

#define SINTC_MMIO_SIZE {{ic_mmio_size}}
#define SINTC_MMIO_BASE {{ic_mmio_base}}

typedef struct SIntCState {
    /*< private >*/
    SysBusDevice sys_bus;
    /*< public >*/

    MemoryRegion mmio;
    /* output to the cpu */
    qemu_irq irq;

    uint32_t interrupt_cause_register;
    uint32_t interrupt_mask_register;
    bool clear;

    QEMUTimer *timer;
} SIntCState;

#endif /* SINTC_H */
