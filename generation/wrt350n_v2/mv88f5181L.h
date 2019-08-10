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

#define MPP_CONTROL_0_REGISTER 0x00
#define MPP_CONTROL_1_REGISTER 0x04
#define MPP_CONTROL_2_REGISTER 0x50
#define DEVICE_MULTIPLEX_CONTROL_REGISTER 0x08
#define SAMPLE_AT_RESET_REGISTER 0x10

#define CSN0_BAR_SIZE 0x0c08
#define CSN1_BAR_SIZE 0x0d08
#define CSN2_BAR_SIZE 0x0c0c
#define CSN3_BAR_SIZE 0x0d0c
#define DEVCSN0_BAR_SIZE 0x0c10
#define DEVCSN1_BAR_SIZE 0x0d10
#define DEVCSN2_BAR_SIZE 0x0d18
#define BOOT_CSN_BAR_SIZE 0x0d14
#define P2P_MEM0_BAR_SIZE 0x0d1c
#define P2P_I_OR_O_BAR_SIZE 0x0d24
#define EXPANSION_ROM_BAR_SIZE 0x0d2c
#define BASE_ADDRESS_REGISTERS_ENABLE 0x0c3c
#define CSN0_BASE_ADDRESS_REMAP 0x0c48
#define CSN1_BASE_ADDRESS_REMAP 0x0d48
#define CSN2_BASE_ADDRESS_REMAP 0x0c4c
#define CSN3_BASE_ADDRESS_REMAP 0x0d4c
#define DEVCSN0_BASE_ADDRESS_REMAP 0x0c50
#define DEVCSN1_BASE_ADDRESS_REMAP 0x0d50
#define DEVCSN2_BASE_ADDRESS_REMAP 0x0d58
#define BOOTCSN_BASE_ADDRESS_REMAP 0x0d54
#define P2P_MEM0_BASE_ADDRESS_REMAP_LOW 0x0d5c
#define P2P_MEM0_BASE_ADDRESS_REMAP_HIGH 0x0d60
#define P2P_I_OR_O_BASE_ADDRESS_REMAP 0x0d6c
#define EXPANSION_ROM_BASE_ADDRESS_REMAP 0x0f38
#define DRAM_BAR_BANK_SELECT 0x0c1c
#define PCI_ADDRESS_DECODE_CONTROL 0x0d3c
#define PCI_DLL_CONTROL 0x1d20
#define PCI_OR_MPP_PADS_CALIBRATION 0x1d1c
#define PCI_COMMAND 0x0c00
#define PCI_MODE 0x0d00
#define PCI_RETRY 0x0c04
#define PCI_DISCARD_TIMER 0x0d04
#define MSI_TRIGGER_TIMER 0x0c38
#define PCI_ARBITER_CONTROL 0x1d00
#define PCI_P2P_CONFIGURATION 0x1d14
#define PCI_ACCESS_CONTROL_BASE_0_LOW 0x1e00
#define PCI_ACCESS_CONTROL_BASE_0_HIGH 0x1e04
#define PCI_ACCESS_CONTROL_SIZE_0 0x1e08
#define PCI_ACCESS_CONTROL_BASE_1_LOW 0x1e10
#define PCI_ACCESS_CONTROL_BASE_1_HIGH 0x1e14
#define PCI_ACCESS_CONTROL_SIZE_1 0x1e18
#define PCI_ACCESS_CONTROL_BASE_2_LOW 0x1e20
#define PCI_ACCESS_CONTROL_BASE_2_HIGH 0x1e24
#define PCI_ACCESS_CONTROL_SIZE_2 0x1e28
#define PCI_ACCESS_CONTROL_BASE_3_LOW 0x1e30
#define PCI_ACCESS_CONTROL_BASE_3_HIGH 0x1e34
#define PCI_ACCESS_CONTROL_SIZE_3 0x1e38
#define PCI_ACCESS_CONTROL_BASE_4_LOW 0x1e40
#define PCI_ACCESS_CONTROL_BASE_4_HIGH 0x1e44
#define PCI_ACCESS_CONTROL_SIZE_4 0x1e48
#define PCI_ACCESS_CONTROL_BASE_5_LOW 0x1e50
#define PCI_ACCESS_CONTROL_BASE_5_HIGH 0x1e54
#define PCI_ACCESS_CONTROL_SIZE_5 0x1e58
#define PCI_CONFIGURATION_ADDRESS 0x0c78
#define PCI_CONFIGURATION_DATA 0x0c7c
#define PCI_INTERRUPT_ACKNOWLEDGE 0x0c34
#define PCI_SERRN_MASK 0x0c28
#define PCI_INTERRUPT_CAUSE 0x1d58
#define PCI_INTERRUPT_MASK 0x1d5c
#define PCI_ERROR_ADDRESS_LOW 0x1d40
#define PCI_ERROR_ADDRESS_HIGH 0x1d44
#define PCI_ERROR_COMMAND 0x1d50

#define PCI_EXPRESS_DEVICE_AND_VENDOR_ID_REGISTER 0x0000
#define PCI_EXPRESS_COMMAND_AND_STATUS_REGISTER 0x0004
#define PCI_EXPRESS_CLASS_CODE_AND_REVISION_ID_REGISTER 0x0008
#define PCI_EXPRESS_BIST_HEADER_TYPE_AND_CACHE_LINE_SIZE_REGISTER 0x000c
#define PCI_EXPRESS_BAR0_INTERNAL_REGISTER 0x0010
#define PCI_EXPRESS_BAR0_INTERNAL_HIGH_REGISTER 0x0014
#define PCI_EXPRESS_BAR1_REGISTER 0x0018
#define PCI_EXPRESS_BAR1_HIGH_REGISTER 0x001c
#define PCI_EXPRESS_BAR2_REGISTER 0x0020
#define PCI_EXPRESS_BAR2_HIGH_REGISTER 0x0024
#define PCI_EXPRESS_SUBSYSTEM_DEVICE_AND_VENDOR_ID 0x002c
#define PCI_EXPRESS_EXPANSION_ROM_BAR_REGISTER 0x0030
#define PCI_EXPRESS_CAPABILITY_LIST_POINTER_REGISTER 0x0034
#define PCI_EXPRESS_INTERRUPT_PIN_AND_LINE_REGISTER 0x003c
#define PCI_EXPRESS_POWER_MANAGEMENT_CAPABILITY_HEADER_REGISTER 0x0040
#define PCI_EXPRESS_POWER_MANAGEMENT_CONTROL_AND_STATUS_REGISTER 0x0044
#define PCI_EXPRESS_MSI_MESSAGE_CONTROL_REGISTER 0x0050
#define PCI_EXPRESS_MSI_MESSAGE_ADDRESS_REGISTER 0x0054
#define PCI_EXPRESS_MSI_MESSAGE_ADDRESS_HIGH_REGISTER 0x0058
#define PCI_EXPRESS_MSI_MESSAGE_DATA_REGISTER 0x005c
#define PCI_EXPRESS_CAPABILITY_REGISTER 0x0060
#define PCI_EXPRESS_DEVICE_CAPABILITIES_REGISTER 0x0064
#define PCI_EXPRESS_DEVICE_CONTROL_STATUS_REGISTER 0x0068
#define PCI_EXPRESS_LINK_CAPABILITIES_REGISTER 0x006c
#define PCI_EXPRESS_LINK_CONTROL_STATUS_REGISTER 0x0070
#define PCI_EXPRESS_ADVANCED_ERROR_REPORT_HEADER_REGISTER 0x0100
#define PCI_EXPRESS_UNCORRECTABLE_ERROR_STATUS_REGISTER 0x0104
#define PCI_EXPRESS_UNCORRECTABLE_ERROR_MASK_REGISTER 0x0108
#define PCI_EXPRESS_UNCORRECTABLE_ERROR_SEVERITY_REGISTER 0x010c
#define PCI_EXPRESS_CORRECTABLE_ERROR_STATUS_REGISTER 0x0110
#define PCI_EXPRESS_CORRECTABLE_ERROR_MASK_REGISTER 0x0114
#define PCI_EXPRESS_ADVANCED_ERROR_CAPABILITY_AND_CONTROL_REGISTER 0x0118
#define PCI_EXPRESS_HEADER_LOG_FIRST_DWORD_REGISTER 0x011c
#define PCI_EXPRESS_HEADER_LOG_SECOND_DWORD_REGISTER 0x0120
#define PCI_EXPRESS_HEADER_LOG_THIRD_DWORD_REGISTER 0x0124
#define PCI_EXPRESS_HEADER_LOG_FOURTH_DWORD_REGISTER 0x0128
#define PCI_EXPRESS_BAR1_CONTROL_REGISTER 0x1804
#define PCI_EXPRESS_BAR2_CONTROL_REGISTER 0x1808
#define PCI_EXPRESS_EXPANSION_ROM_BAR_CONTROL_REGISTER 0x180c
#define PCI_EXPRESS_CONFIGURATION_ADDRESS_REGISTER 0x18f8
#define PCI_EXPRESS_CONFIGURATION_DATA_REGISTER 0x18fc
#define PCI_EXPRESS_INTERRUPT_CAUSE 0x1900
#define PCI_EXPRESS_INTERRUPT_MASK 0x1910
#define PCI_EXPRESS_WINDOW0_CONTROL_REGISTER 0x1820
#define PCI_EXPRESS_WINDOW0_BASE_REGISTER 0x1824
#define PCI_EXPRESS_WINDOW0_REMAP_REGISTER 0x182c
#define PCI_EXPRESS_WINDOW1_CONTROL_REGISTER 0x1830
#define PCI_EXPRESS_WINDOW1_BASE_REGISTER 0x1834
#define PCI_EXPRESS_WINDOW1_REMAP_REGISTER 0x183c
#define PCI_EXPRESS_WINDOW2_CONTROL_REGISTER 0x1840
#define PCI_EXPRESS_WINDOW2_BASE_REGISTER 0x1844
#define PCI_EXPRESS_WINDOW2_REMAP_REGISTER 0x184c
#define PCI_EXPRESS_WINDOW3_CONTROL_REGISTER 0x1850
#define PCI_EXPRESS_WINDOW3_BASE_REGISTER 0x1854
#define PCI_EXPRESS_WINDOW3_REMAP_REGISTER 0x185c
#define PCI_EXPRESS_WINDOW4_CONTROL_REGISTER 0x1860
#define PCI_EXPRESS_WINDOW4_BASE_REGISTER 0x1864
#define PCI_EXPRESS_WINDOW4_REMAP_REGISTER 0x186c
#define PCI_EXPRESS_WINDOW5_CONTROL_REGISTER 0x1880
#define PCI_EXPRESS_WINDOW5_BASE_REGISTER 0x1884
#define PCI_EXPRESS_WINDOW5_REMAP_REGISTER 0x188c
#define PCI_EXPRESS_DEFAULT_WINDOW_CONTROL_REGISTER 0x18b0
#define PCI_EXPRESS_EXPANSION_ROM_WINDOW_CONTROL_REGISTER 0x18c0
#define PCI_EXPRESS_EXPANSION_ROM_WINDOW_REMAP_REGISTER 0x18c4
#define PCI_EXPRESS_CONTROL_REGISTER 0x1a00
#define PCI_EXPRESS_STATUS_REGISTER 0x1a04
#define PCI_EXPRESS_COMPLETION_TIMEOUT_REGISTER 0x1a10
#define PCI_EXPRESS_FLOW_CONTROL_REGISTER 0x1a20
#define PCI_EXPRESS_ACKNOWLEDGE_TIMERS_1X_REGISTER 0x1a40
#define PCI_EXPRESS_DEBUG_CONTROL_REGISTER 0x1a60
#define PCI_EXPRESS_TL_CONTROL_REGISTER 0x1ab0

#define MV88F5181_CPU_ADDRESS_MAP_MMIO_SIZE 0x100
#define MV88F5181_CPU_ADDRESS_MAP_MMIO_BASE 0xf1020000
#define MV88F5181_DDR_SDRAM_CONTROLLER_MMIO_SIZE 0x200
#define MV88F5181_DDR_SDRAM_CONTROLLER_MMIO_BASE 0xf1001400
#define MV88F5181L_PINS_MULTIPLEXING_INTERFACE_MMIO_SIZE 0x100
#define MV88F5181L_PINS_MULTIPLEXING_INTERFACE_MMIO_BASE 0xf1010000
#define MV88F5181L_PCI_INTERFACE_MMIO_SIZE 0x2000
#define MV88F5181L_PCI_INTERFACE_MMIO_BASE 0xf1030000
#define MV88F5181L_PCIE_INTERFACE_MMIO_SIZE 0x2000
#define MV88F5181L_PCIE_INTERFACE_MMIO_BASE 0xf1040000

typedef struct MV88F5181LState {
    /*< private >*/
    SysBusDevice sys_bus;
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
    
    MemoryRegion ddr_sdram_controller_mmio;
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
    
    MemoryRegion pins_multiplexing_interface_mmio;
    uint32_t mpp_control_0_register;
    uint32_t mpp_control_1_register;
    uint32_t mpp_control_2_register;
    uint32_t device_multiplex_control_register;
    uint32_t sample_at_reset_register;
    
    MemoryRegion pci_interface_mmio;
    uint32_t csn0_bar_size;
    uint32_t csn1_bar_size;
    uint32_t csn2_bar_size;
    uint32_t csn3_bar_size;
    uint32_t devcsn0_bar_size;
    uint32_t devcsn1_bar_size;
    uint32_t devcsn2_bar_size;
    uint32_t boot_csn_bar_size;
    uint32_t p2p_mem0_bar_size;
    uint32_t p2p_i_or_o_bar_size;
    uint32_t expansion_rom_bar_size;
    uint32_t base_address_registers_enable;
    uint32_t csn0_base_address_remap;
    uint32_t csn1_base_address_remap;
    uint32_t csn2_base_address_remap;
    uint32_t csn3_base_address_remap;
    uint32_t devcsn0_base_address_remap;
    uint32_t devcsn1_base_address_remap;
    uint32_t devcsn2_base_address_remap;
    uint32_t bootcsn_base_address_remap;
    uint32_t p2p_mem0_base_address_remap_low;
    uint32_t p2p_mem0_base_address_remap_high;
    uint32_t p2p_i_or_o_base_address_remap;
    uint32_t expansion_rom_base_address_remap;
    uint32_t dram_bar_bank_select;
    uint32_t pci_address_decode_control;
    uint32_t pci_dll_control;
    uint32_t pci_or_mpp_pads_calibration;
    uint32_t pci_command;
    uint32_t pci_mode;
    uint32_t pci_retry;
    uint32_t pci_discard_timer;
    uint32_t msi_trigger_timer;
    uint32_t pci_arbiter_control;
    uint32_t pci_p2p_configuration;
    uint32_t pci_access_control_base_0_low;
    uint32_t pci_access_control_base_0_high;
    uint32_t pci_access_control_size_0;
    uint32_t pci_access_control_base_1_low;
    uint32_t pci_access_control_base_1_high;
    uint32_t pci_access_control_size_1;
    uint32_t pci_access_control_base_2_low;
    uint32_t pci_access_control_base_2_high;
    uint32_t pci_access_control_size_2;
    uint32_t pci_access_control_base_3_low;
    uint32_t pci_access_control_base_3_high;
    uint32_t pci_access_control_size_3;
    uint32_t pci_access_control_base_4_low;
    uint32_t pci_access_control_base_4_high;
    uint32_t pci_access_control_size_4;
    uint32_t pci_access_control_base_5_low;
    uint32_t pci_access_control_base_5_high;
    uint32_t pci_access_control_size_5;
    uint32_t pci_configuration_address;
    uint32_t pci_configuration_data;
    uint32_t pci_interrupt_acknowledge;
    uint32_t pci_serrn_mask;
    uint32_t pci_interrupt_cause;
    uint32_t pci_interrupt_mask;
    uint32_t pci_error_address_low;
    uint32_t pci_error_address_high;
    uint32_t pci_error_command;
    
    MemoryRegion pcie_interface_mmio;
    uint32_t pci_express_device_and_vendor_id_register;
    uint32_t pci_express_command_and_status_register;
    uint32_t pci_express_class_code_and_revision_id_register;
    uint32_t pci_express_bist_header_type_and_cache_line_size_register;
    uint32_t pci_express_bar0_internal_register;
    uint32_t pci_express_bar0_internal_high_register;
    uint32_t pci_express_bar1_register;
    uint32_t pci_express_bar1_high_register;
    uint32_t pci_express_bar2_register;
    uint32_t pci_express_bar2_high_register;
    uint32_t pci_express_subsystem_device_and_vendor_id;
    uint32_t pci_express_expansion_rom_bar_register;
    uint32_t pci_express_capability_list_pointer_register;
    uint32_t pci_express_interrupt_pin_and_line_register;
    uint32_t pci_express_power_management_capability_header_register;
    uint32_t pci_express_power_management_control_and_status_register;
    uint32_t pci_express_msi_message_control_register;
    uint32_t pci_express_msi_message_address_register;
    uint32_t pci_express_msi_message_address_high_register;
    uint32_t pci_express_msi_message_data_register;
    uint32_t pci_express_capability_register;
    uint32_t pci_express_device_capabilities_register;
    uint32_t pci_express_device_control_status_register;
    uint32_t pci_express_link_capabilities_register;
    uint32_t pci_express_link_control_status_register;
    uint32_t pci_express_advanced_error_report_header_register;
    uint32_t pci_express_uncorrectable_error_status_register;
    uint32_t pci_express_uncorrectable_error_mask_register;
    uint32_t pci_express_uncorrectable_error_severity_register;
    uint32_t pci_express_correctable_error_status_register;
    uint32_t pci_express_correctable_error_mask_register;
    uint32_t pci_express_advanced_error_capability_and_control_register;
    uint32_t pci_express_header_log_first_dword_register;
    uint32_t pci_express_header_log_second_dword_register;
    uint32_t pci_express_header_log_third_dword_register;
    uint32_t pci_express_header_log_fourth_dword_register;
    uint32_t pci_express_bar1_control_register;
    uint32_t pci_express_bar2_control_register;
    uint32_t pci_express_expansion_rom_bar_control_register;
    uint32_t pci_express_configuration_address_register;
    uint32_t pci_express_configuration_data_register;
    uint32_t pci_express_interrupt_cause;
    uint32_t pci_express_interrupt_mask;
    uint32_t pci_express_window0_control_register;
    uint32_t pci_express_window0_base_register;
    uint32_t pci_express_window0_remap_register;
    uint32_t pci_express_window1_control_register;
    uint32_t pci_express_window1_base_register;
    uint32_t pci_express_window1_remap_register;
    uint32_t pci_express_window2_control_register;
    uint32_t pci_express_window2_base_register;
    uint32_t pci_express_window2_remap_register;
    uint32_t pci_express_window3_control_register;
    uint32_t pci_express_window3_base_register;
    uint32_t pci_express_window3_remap_register;
    uint32_t pci_express_window4_control_register;
    uint32_t pci_express_window4_base_register;
    uint32_t pci_express_window4_remap_register;
    uint32_t pci_express_window5_control_register;
    uint32_t pci_express_window5_base_register;
    uint32_t pci_express_window5_remap_register;
    uint32_t pci_express_default_window_control_register;
    uint32_t pci_express_expansion_rom_window_control_register;
    uint32_t pci_express_expansion_rom_window_remap_register;
    uint32_t pci_express_control_register;
    uint32_t pci_express_status_register;
    uint32_t pci_express_completion_timeout_register;
    uint32_t pci_express_flow_control_register;
    uint32_t pci_express_acknowledge_timers_1x_register;
    uint32_t pci_express_debug_control_register;
    uint32_t pci_express_tl_control_register;
    
    MV88F5181LICState ic;
    MV88F5181LPERIPHERALSState peripherals;
} MV88F5181LState;

#endif /* MV88F5181L_H */