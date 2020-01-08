/* 
 * automatically generated, don't change
 */


#ifndef SINTC_H
#define SINTC_H

#include "hw/sysbus.h"
#include "qemu/timer.h"

#define TYPE_SINTC "sintc"
#define SINTC(obj) \
    OBJECT_CHECK(SIntCState, (obj), TYPE_SINTC)

#define INTERRUPT_CAUSE_REGISTER 0x100
#define INTERRUPT_MASK_REGISTER  0x104
#define INTERRUPT_CLEAR_REGISTER 0x010

#define SINTC_MMIO_SIZE 0x200
#define SINTC_MMIO_BASE 0xf1020100

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
