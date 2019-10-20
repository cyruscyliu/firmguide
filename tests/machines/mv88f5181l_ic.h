/* 
 * automatically generated, don't change
 */


#ifndef MV88F5181L_IC_H
#define MV88F5181L_IC_H

#include "hw/sysbus.h"

#define TYPE_MV88F5181L_IC "mv88f5181l_ic"
#define MV88F5181L_IC(obj) \
    OBJECT_CHECK(MV88F5181LICState, (obj), TYPE_MV88F5181L_IC)

#define MV88F5181L_IC_IRQ "mv88f5181l_ic_irq"
#define MV88F5181L_IC_N_IRQS 32

#define MAIN_INTERRUPT_CAUSE_REGISTER 0x00
#define MAIN_IRQ_INTERRUPT_MASK_REGISTER 0x04
#define MAIN_FIQ_INTERRUPT_MASK_REGISTER 0x08
#define MAIN_ENDPOINT_INTERRUPT_MASK_REGISTER 0x0c

#define MV88F5181L_IC_MMIO_SIZE 0x100
#define MV88F5181L_IC_MMIO_BASE 0xf1020200

typedef struct MV88F5181LICState {
    /*< private >*/
    SysBusDevice sys_bus;
    /*< public >*/

    MemoryRegion mmio;
    /* output to the cpu */
    qemu_irq irq;

    uint32_t main_interrupt_cause_register;
    uint32_t main_irq_interrupt_mask_register;
    uint32_t main_fiq_interrupt_mask_register;
    uint32_t main_endpoint_interrupt_mask_register;
    

} MV88F5181LICState;

#endif /* MV88F5181L_IC_H */