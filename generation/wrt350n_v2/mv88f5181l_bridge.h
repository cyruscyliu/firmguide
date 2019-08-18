/* 
 * automatically generated, don't change
 */

#ifndef MV88F5181L_BRIDGE_H
#define MV88F5181L_BRIDGE_H

#include "hw/sysbus.h"

#define TYPE_MV88F5181L_BRIDGE "mv88f5181l_bridge"
#define MV88F5181L_BRIDGE(obj) \
    OBJECT_CHECK(MV88F5181LBRIDGEState, (obj),  TYPE_MV88F5181L_BRIDGE)


#define BRIDGE_CONFIGURATION_REGISTER 0x00
#define BRIDGE_CONTROL_AND_STATUS_REGISTER 0x04
#define BRIDGE_RSTOUTN_MASK_REGISTER 0x08
#define BRIDGE_SYSTEM_SOFT_RESET_REGISTER 0x0c
#define BRIDGE_INTERRUPT_CAUSE_REGISTER 0x10
#define BRIDGE_INTERRUPT_MASK_REGISTER 0x14

#define MV88F5181L_BRIDGE_MMIO_SIZE 0x100
#define MV88F5181L_BRIDGE_MMIO_BASE 0xf1020100
#define MV88F5181L_BRIDGE_IRQ "mv88f5181l_bridge_irq"

typedef struct MV88F5181LBRIDGEState {
    /*< private >*/
    SysBusDevice sys_bus;
    /*< public >*/

    MemoryRegion bridge_mmio;
    qemu_irq irq;

    uint32_t bridge_configuration_register;
    uint32_t bridge_control_and_status_register;
    uint32_t bridge_rstoutn_mask_register;
    uint32_t bridge_system_soft_reset_register;
    uint32_t bridge_interrupt_cause_register;
    uint32_t bridge_interrupt_mask_register;
    
} MV88F5181LBRIDGEState;

#endif /* MV88F5181L_BRIDGE_H */