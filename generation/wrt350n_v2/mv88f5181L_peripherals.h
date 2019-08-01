/* 
 * automatically generated, don't change
 */

#ifndef MV88F5181L_PERIPHERALS_H
#define MV88F5181L_PERIPHERALS_H

#include "hw/sysbus.h"
#include "hw/timer/mv88f5181L_timer.h"
#include "hw/char/mv88f5181L_uart.h"
#include "hw/gpio/mv88f5181L_gpio.h"
#include "hw/pci-host/mv88f5181L_pcie.h"

#define TYPE_MV88F5181L_PERIPHERALS "MV88F5181L_PERIPHERALS"
#define MV88F5181L_PERIPHERALS(obj) \
    OBJECT_CHECK(MV88F5181LPERIPHERALSState, (obj),  TYPE_MV88F5181L_PERIPHERALS)

#define MV88F5181L_PERIPHERALS_RAM_SIZE 0x00100000
#define MV88F5181L_PERIPHERALS_RAM_BASE 0xf1000000

#define BRIDGE_CONFIGURATION_REGISTER      0x00
#define BRIDGE_CONTROL_AND_STATUS_REGISTER 0x04
#define BRIDGE_RSTOUTn_MASK_RESTIER        0x08
#define BRIDGE_SYSTEM_SOFT_RESET_REGISTER  0x0C
#define BRIDGE_INTERRUPT_CAUSE_REGISTER    0x10
#define BRIDGE_INTERRUPT_MASK_REGISTER     0x14

#define MV88F5181L_BRIDGE_RAM_SIZE 0x100
#define MV88F5181L_BRIDGE_RAM_BASE 0xf1020100

typedef struct MV88F5181LPERIPHERALSState {
    /*< private >*/
    SysBusDevice sys_bus;
    /*< public >*/

    MemoryRegion bridge_mmio;
    uint32_t bridge_interrupt_cause_register;
    uint32_t bridge_interrupt_mask_register;
    MV88F5181LTIMERState timer;
    MV88F5181LUARTState uart;
    MV88F5181LGPIOState gpio;
    MV88F5181LPCIEState pcie;
} MV88F5181LPERIPHERALSState;

#endif /* MV88F5181L_PERIPHERALS_H */