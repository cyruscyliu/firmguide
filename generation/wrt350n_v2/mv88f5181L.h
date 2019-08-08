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

#define WINDOW0_CONTROL_REGISTER 0x00
#define WINDOW0_BASE_REGISTER 0x04
#define WINDOW0_REMAP_LOW_REGISTER 0x08
#define WINDOW0_REMAP_HIGH_REGISTER 0x0C
#define WINDOW1_CONTROL_REGISTER 0x10
#define WINDOW1_BASE_REGISTER 0x14
#define WINDOW1_REMAP_LOW_REGISTER 0x18
#define WINDOW1_REMAP_HIGH_REGISTER 0x1C
#define WINDOW2_CONTROL_REGISTER 0x20
#define WINDOW2_BASE_REGISTER 0x24
#define WINDOW2_REMAP_LOW_REGISTER 0x28
#define WINDOW2_REMAP_HIGH_REGISTER 0x2C
#define WINDOW3_CONTROL_REGISTER 0x30
#define WINDOW3_BASE_REGISTER 0x34
#define WINDOW4_CONTROL_REGISTER 0x40
#define WINDOW4_BASE_REGISTER 0x44
#define WINDOW5_CONTROL_REGISTER 0x50
#define WINDOW5_BASE_REGISTER 0x54
#define WINDOW6_CONTROL_REGISTER 0x60
#define WINDOW6_BASE_REGISTER 0x64
#define WINDOW7_CONTROL_REGISTER 0x70
#define WINDOW7_BASE_REGISTER 0x74
#define _88F5181_INTERNAL_REGISTERS_BASE_ADDRESS_REGISTER 0x80

#define CS0N_BASE_ADDRESS_REGISTER 0x100
#define CS0N_SIZE_REGISTER 0x104
#define CS1N_BASE_ADDRESS_REGISTER 0x108
#define CS1N_SIZE_REGISTER 0x10C
#define CS2N_BASE_ADDRESS_REGISTER 0x110
#define CS2N_SIZE_REGISTER 0x114
#define CS3N_BASE_ADDRESS_REGISTER 0x118
#define CS3N_SIZE_REGISTER 0x11C
#define DDR_SDRAM_CONFIGURATION_REGISTER 0x00
#define DDR_SDRAM_CONTROL_REGISTER 0x04
#define DDR_SDRAM_TIMING_LOW_REGISTER 0x08
#define DDR_SDRAM_TIMING_HIGH_REGISTER 0x0C
#define DDR2_SDRAM_TIMING_LOW_REGISTER 0x28
#define DDR2_SDRAM_TIMING_HIGH_REGISTER 0x7C
#define DDR_SDRAM_ADDRESS_CONTROL_REGISTER 0x10
#define DDR_SDRAM_OPEN_PAGES_CONTROL_REGISTER 0x14
#define DDR_SDRAM_OPERATION_REGISTER 0x18
#define DDR_SDRAM_OPERATION_CONTROL_REGISTER 0x2C
#define DDR_SDRAM_MODE_REGISTER 0x1C
#define EXTENDED_DDR_SDRAM_MODE_REGISTER 0x20
#define DDR_SDRAM_INITIALIZATION_CONTROL_REGISTER 0x80
#define DDR_SDRAM_ADDRESS_OR_CONTROL_PADS_CALIBRATION_REGISTER 0xC0
#define DDR_SDRAM_DATA_PADS_CALIBRATION_REGISTER 0xC4
#define DDR2_SDRAM_ODT_CONTROL_LOW_REGISTER 0x94
#define DDR2_SDRAM_ODT_CONTROL_HIGH_REGISTER 0x98
#define DDR2_SDRAM_ODT_CONTROL_REGISTER 0x9C
#define DDR_SDRAM_INTERFACE_MBUS_CONTROL_LOW_REGISTER 0x30
#define DDR_SDRAM_INTERFACE_MBUS_CONTROL_HIGH_REGISTER 0x34
#define DDR_SDRAM_INTERFACE_MBUS_TIMEOUT_REGISTER 0x38
#define DDR_SDRAM_MMASK_REGISTER 0xB0

#define MV88F5181_CPU_ADDRESS_MAP_MMIO_SIZE 0x100
#define MV88F5181_CPU_ADDRESS_MAP_MMIO_BASE 0xf1020000
#define MV88F5181_DDR_SDRAM_CONTROLLER_MMIO_SIZE 0x200
#define MV88F5181_DDR_SDRAM_CONTROLLER_MMIO_BASE 0xf1001400

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
    
    MemoryRegion addr_sdram_controller_mmio;
    uint32_t cs0n_base_address_register;
    uint32_t cs0n_size_register;
    uint32_t cs1n_base_address_register;
    uint32_t cs1n_size_register;
    uint32_t cs2n_base_address_register;
    uint32_t cs2n_size_register;
    uint32_t cs3n_base_address_register;
    uint32_t cs3n_size_register;
    uint32_t ddr_sdram_configuration_register;
    uint32_t ddr_sdram_control_register;
    uint32_t ddr_sdram_timing_low_register;
    uint32_t ddr_sdram_timing_high_register;
    uint32_t ddr2_sdram_timing_low_register;
    uint32_t ddr2_sdram_timing_high_register;
    uint32_t ddr_sdram_address_control_register;
    uint32_t ddr_sdram_open_pages_control_register;
    uint32_t ddr_sdram_operation_register;
    uint32_t ddr_sdram_operation_control_register;
    uint32_t ddr_sdram_mode_register;
    uint32_t extended_ddr_sdram_mode_register;
    uint32_t ddr_sdram_initialization_control_register;
    uint32_t ddr_sdram_address_or_control_pads_calibration_register;
    uint32_t ddr_sdram_data_pads_calibration_register;
    uint32_t ddr2_sdram_odt_control_low_register;
    uint32_t ddr2_sdram_odt_control_high_register;
    uint32_t ddr2_sdram_odt_control_register;
    uint32_t ddr_sdram_interface_mbus_control_low_register;
    uint32_t ddr_sdram_interface_mbus_control_high_register;
    uint32_t ddr_sdram_interface_mbus_timeout_register;
    uint32_t ddr_sdram_mmask_register;
    
    MV88F5181LICState ic;
    MV88F5181LPERIPHERALSState peripherals;
} MV88F5181LState;

#endif /* MV88F5181L_H */