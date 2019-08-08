/* 
 * automatically generated, don't change
 */

#ifndef MV88F5181L_H
#define MV88F5181L_H

#include "hw/arm/arm.h"
#include "hw/intc/mv88f5181L_ic.h"
#include "hw/arm/mv88f5181L_peripherals.h"

#define TYPE_MV88F5181L "mv88f5181L"
#define MV88F5181L(obj) \
    OBJECT_CHECK(MV88F5181LState, (obj), TYPE_MV88F5181L)

#define MV88F5181_CPU_ADDRESS_MAP_RAM_SIZE 0x100
#define MV88F5181_CPU_ADDRESS_MAP_RAM_BASE 0xf1020000

typedef struct MV88F5181LState {
    /*< private >*/
    DeviceState parent_obj;
    /*< public >*/

    const char *cpu_type;
    ARMCPU *cpu;
    qemu_irq irq, fiq;

    MemoryRegion cpu_address_map_mmio;
    uint32_t window0_control_register;
    uint32_t window0_base_register;
    uint32_t window0_remap_low_register;
    uint32_t window0_remap_high_register;
    uint32_t window1_control_register;
    uint32_t window1_base_register;
    uint32_t window1_remap_low_register;
    uint32_t window1_remap_high_register;
    uint32_t window2_control_register;
    uint32_t window2_base_register;
    uint32_t window2_remap_low_register;
    uint32_t window2_remap_high_register;
    uint32_t window3_control_register;
    uint32_t window3_base_register;
    uint32_t window4_control_register;
    uint32_t window4_base_register;
    uint32_t window5_control_register;
    uint32_t window5_base_register;
    uint32_t window6_control_register;
    uint32_t window6_base_register;
    uint32_t window7_control_register;
    uint32_t window7_base_register;
    uint32_t _88f5181_internal_registers_base_address_register;
    
    MV88F5181LICState ic;
    MV88F5181LPERIPHERALSState peripherals;
} MV88F5181LState;

#endif /* MV88F5181L_H */