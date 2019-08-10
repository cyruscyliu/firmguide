/* 
 * automatically generated, don't change
 */

#ifndef MV88F5181L_PCIE_H
#define MV88F5181L_PCIE_H

#include "hw/sysbus.h"

#define TYPE_MV88F5181L_PCIE "mv88f5181L_pcie"
#define MV88F5181L_PCIE(obj) \
    OBJECT_CHECK(MV88F5181LPCIEState, (obj), TYPE_MV88F5181L_PCIE)

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

#define MV88F5181L_PCIE_MMIO_SIZE 0x10000
#define MV88F5181L_PCIE_MMIO_BASE 0xf1040000

typedef struct MV88F5181LPCIEState {
    /*< private >*/
    SysBusDevice sys_bus;
    /*< public >*/

    MemoryRegion mmio;
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
    
} MV88F5181LPCIEState;

#endif /* MV88F5181L_PCIE_H */