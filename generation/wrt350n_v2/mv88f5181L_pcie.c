/* 
 * automatically generated, don't change
 */

#include "qemu/osdep.h"
#include "qemu/log.h"
#include "hw/pci-host/mv88f5181L_pcie.h"

static void mv88f5181L_pcie_update(void *opaque);
static void mv88f5181L_pcie_reset(DeviceState *dev);

static uint64_t mv88f5181L_pcie_read(void *opaque, hwaddr offset, unsigned size);
static void mv88f5181L_pcie_write(void *opaque, hwaddr offset, uint64_t val, unsigned size);

static void mv88f5181L_pcie_init(Object *obj);
static void mv88f5181L_pcie_class_init(ObjectClass *klass, void *data);
static void mv88f5181L_pcie_register_types(void);

static void mv88f5181L_pcie_update(void *opaque) {
    /* MV88F5181LPCIEState *s = opaque; */
}

static uint64_t mv88f5181L_pcie_read(void *opaque, hwaddr offset, unsigned size) {
    MV88F5181LPCIEState *s = (MV88F5181LPCIEState *)opaque;

    uint64_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset 0x%"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case PCI_EXPRESS_DEVICE_AND_VENDOR_ID_REGISTER:
        res = s->pci_express_device_and_vendor_id_register;
        break;
    case PCI_EXPRESS_COMMAND_AND_STATUS_REGISTER:
        res = s->pci_express_command_and_status_register;
        break;
    case PCI_EXPRESS_CLASS_CODE_AND_REVISION_ID_REGISTER:
        res = s->pci_express_class_code_and_revision_id_register;
        break;
    case PCI_EXPRESS_BIST_HEADER_TYPE_AND_CACHE_LINE_SIZE_REGISTER:
        res = s->pci_express_bist_header_type_and_cache_line_size_register;
        break;
    case PCI_EXPRESS_BAR0_INTERNAL_REGISTER:
        res = s->pci_express_bar0_internal_register;
        break;
    case PCI_EXPRESS_BAR0_INTERNAL_HIGH_REGISTER:
        res = s->pci_express_bar0_internal_high_register;
        break;
    case PCI_EXPRESS_BAR1_REGISTER:
        res = s->pci_express_bar1_register;
        break;
    case PCI_EXPRESS_BAR1_HIGH_REGISTER:
        res = s->pci_express_bar1_high_register;
        break;
    case PCI_EXPRESS_BAR2_REGISTER:
        res = s->pci_express_bar2_register;
        break;
    case PCI_EXPRESS_BAR2_HIGH_REGISTER:
        res = s->pci_express_bar2_high_register;
        break;
    case PCI_EXPRESS_SUBSYSTEM_DEVICE_AND_VENDOR_ID:
        res = s->pci_express_subsystem_device_and_vendor_id;
        break;
    case PCI_EXPRESS_EXPANSION_ROM_BAR_REGISTER:
        res = s->pci_express_expansion_rom_bar_register;
        break;
    case PCI_EXPRESS_CAPABILITY_LIST_POINTER_REGISTER:
        res = s->pci_express_capability_list_pointer_register;
        break;
    case PCI_EXPRESS_INTERRUPT_PIN_AND_LINE_REGISTER:
        res = s->pci_express_interrupt_pin_and_line_register;
        break;
    case PCI_EXPRESS_POWER_MANAGEMENT_CAPABILITY_HEADER_REGISTER:
        res = s->pci_express_power_management_capability_header_register;
        break;
    case PCI_EXPRESS_POWER_MANAGEMENT_CONTROL_AND_STATUS_REGISTER:
        res = s->pci_express_power_management_control_and_status_register;
        break;
    case PCI_EXPRESS_MSI_MESSAGE_CONTROL_REGISTER:
        res = s->pci_express_msi_message_control_register;
        break;
    case PCI_EXPRESS_MSI_MESSAGE_ADDRESS_REGISTER:
        res = s->pci_express_msi_message_address_register;
        break;
    case PCI_EXPRESS_MSI_MESSAGE_ADDRESS_HIGH_REGISTER:
        res = s->pci_express_msi_message_address_high_register;
        break;
    case PCI_EXPRESS_MSI_MESSAGE_DATA_REGISTER:
        res = s->pci_express_msi_message_data_register;
        break;
    case PCI_EXPRESS_CAPABILITY_REGISTER:
        res = s->pci_express_capability_register;
        break;
    case PCI_EXPRESS_DEVICE_CAPABILITIES_REGISTER:
        res = s->pci_express_device_capabilities_register;
        break;
    case PCI_EXPRESS_DEVICE_CONTROL_STATUS_REGISTER:
        res = s->pci_express_device_control_status_register;
        break;
    case PCI_EXPRESS_LINK_CAPABILITIES_REGISTER:
        res = s->pci_express_link_capabilities_register;
        break;
    case PCI_EXPRESS_LINK_CONTROL_STATUS_REGISTER:
        res = s->pci_express_link_control_status_register;
        break;
    case PCI_EXPRESS_ADVANCED_ERROR_REPORT_HEADER_REGISTER:
        res = s->pci_express_advanced_error_report_header_register;
        break;
    case PCI_EXPRESS_UNCORRECTABLE_ERROR_STATUS_REGISTER:
        res = s->pci_express_uncorrectable_error_status_register;
        break;
    case PCI_EXPRESS_UNCORRECTABLE_ERROR_MASK_REGISTER:
        res = s->pci_express_uncorrectable_error_mask_register;
        break;
    case PCI_EXPRESS_UNCORRECTABLE_ERROR_SEVERITY_REGISTER:
        res = s->pci_express_uncorrectable_error_severity_register;
        break;
    case PCI_EXPRESS_CORRECTABLE_ERROR_STATUS_REGISTER:
        res = s->pci_express_correctable_error_status_register;
        break;
    case PCI_EXPRESS_CORRECTABLE_ERROR_MASK_REGISTER:
        res = s->pci_express_correctable_error_mask_register;
        break;
    case PCI_EXPRESS_ADVANCED_ERROR_CAPABILITY_AND_CONTROL_REGISTER:
        res = s->pci_express_advanced_error_capability_and_control_register;
        break;
    case PCI_EXPRESS_HEADER_LOG_FIRST_DWORD_REGISTER:
        res = s->pci_express_header_log_first_dword_register;
        break;
    case PCI_EXPRESS_HEADER_LOG_SECOND_DWORD_REGISTER:
        res = s->pci_express_header_log_second_dword_register;
        break;
    case PCI_EXPRESS_HEADER_LOG_THIRD_DWORD_REGISTER:
        res = s->pci_express_header_log_third_dword_register;
        break;
    case PCI_EXPRESS_HEADER_LOG_FOURTH_DWORD_REGISTER:
        res = s->pci_express_header_log_fourth_dword_register;
        break;
    case PCI_EXPRESS_BAR1_CONTROL_REGISTER:
        res = s->pci_express_bar1_control_register;
        break;
    case PCI_EXPRESS_BAR2_CONTROL_REGISTER:
        res = s->pci_express_bar2_control_register;
        break;
    case PCI_EXPRESS_EXPANSION_ROM_BAR_CONTROL_REGISTER:
        res = s->pci_express_expansion_rom_bar_control_register;
        break;
    case PCI_EXPRESS_CONFIGURATION_ADDRESS_REGISTER:
        res = s->pci_express_configuration_address_register;
        break;
    case PCI_EXPRESS_CONFIGURATION_DATA_REGISTER:
        res = s->pci_express_configuration_data_register;
        break;
    case PCI_EXPRESS_INTERRUPT_CAUSE:
        res = s->pci_express_interrupt_cause;
        break;
    case PCI_EXPRESS_INTERRUPT_MASK:
        res = s->pci_express_interrupt_mask;
        break;
    case PCI_EXPRESS_WINDOW0_CONTROL_REGISTER:
        res = s->pci_express_window0_control_register;
        break;
    case PCI_EXPRESS_WINDOW0_BASE_REGISTER:
        res = s->pci_express_window0_base_register;
        break;
    case PCI_EXPRESS_WINDOW0_REMAP_REGISTER:
        res = s->pci_express_window0_remap_register;
        break;
    case PCI_EXPRESS_WINDOW1_CONTROL_REGISTER:
        res = s->pci_express_window1_control_register;
        break;
    case PCI_EXPRESS_WINDOW1_BASE_REGISTER:
        res = s->pci_express_window1_base_register;
        break;
    case PCI_EXPRESS_WINDOW1_REMAP_REGISTER:
        res = s->pci_express_window1_remap_register;
        break;
    case PCI_EXPRESS_WINDOW2_CONTROL_REGISTER:
        res = s->pci_express_window2_control_register;
        break;
    case PCI_EXPRESS_WINDOW2_BASE_REGISTER:
        res = s->pci_express_window2_base_register;
        break;
    case PCI_EXPRESS_WINDOW2_REMAP_REGISTER:
        res = s->pci_express_window2_remap_register;
        break;
    case PCI_EXPRESS_WINDOW3_CONTROL_REGISTER:
        res = s->pci_express_window3_control_register;
        break;
    case PCI_EXPRESS_WINDOW3_BASE_REGISTER:
        res = s->pci_express_window3_base_register;
        break;
    case PCI_EXPRESS_WINDOW3_REMAP_REGISTER:
        res = s->pci_express_window3_remap_register;
        break;
    case PCI_EXPRESS_WINDOW4_CONTROL_REGISTER:
        res = s->pci_express_window4_control_register;
        break;
    case PCI_EXPRESS_WINDOW4_BASE_REGISTER:
        res = s->pci_express_window4_base_register;
        break;
    case PCI_EXPRESS_WINDOW4_REMAP_REGISTER:
        res = s->pci_express_window4_remap_register;
        break;
    case PCI_EXPRESS_WINDOW5_CONTROL_REGISTER:
        res = s->pci_express_window5_control_register;
        break;
    case PCI_EXPRESS_WINDOW5_BASE_REGISTER:
        res = s->pci_express_window5_base_register;
        break;
    case PCI_EXPRESS_WINDOW5_REMAP_REGISTER:
        res = s->pci_express_window5_remap_register;
        break;
    case PCI_EXPRESS_DEFAULT_WINDOW_CONTROL_REGISTER:
        res = s->pci_express_default_window_control_register;
        break;
    case PCI_EXPRESS_EXPANSION_ROM_WINDOW_CONTROL_REGISTER:
        res = s->pci_express_expansion_rom_window_control_register;
        break;
    case PCI_EXPRESS_EXPANSION_ROM_WINDOW_REMAP_REGISTER:
        res = s->pci_express_expansion_rom_window_remap_register;
        break;
    case PCI_EXPRESS_CONTROL_REGISTER:
        res = s->pci_express_control_register;
        break;
    case PCI_EXPRESS_STATUS_REGISTER:
        res = s->pci_express_status_register;
        break;
    case PCI_EXPRESS_COMPLETION_TIMEOUT_REGISTER:
        res = s->pci_express_completion_timeout_register;
        break;
    case PCI_EXPRESS_FLOW_CONTROL_REGISTER:
        res = s->pci_express_flow_control_register;
        break;
    case PCI_EXPRESS_ACKNOWLEDGE_TIMERS_1X_REGISTER:
        res = s->pci_express_acknowledge_timers_1x_register;
        break;
    case PCI_EXPRESS_DEBUG_CONTROL_REGISTER:
        res = s->pci_express_debug_control_register;
        break;
    case PCI_EXPRESS_TL_CONTROL_REGISTER:
        res = s->pci_express_tl_control_register;
        break;
    }
    return res;
}

static void mv88f5181L_pcie_write(void *opaque, hwaddr offset, uint64_t val, unsigned size) {
    MV88F5181LPCIEState *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset 0x%"HWADDR_PRIx"\n", __func__, offset);
        return;
    case PCI_EXPRESS_DEVICE_AND_VENDOR_ID_REGISTER:
        s->pci_express_device_and_vendor_id_register = val;
        break;
    case PCI_EXPRESS_COMMAND_AND_STATUS_REGISTER:
        s->pci_express_command_and_status_register = val;
        break;
    case PCI_EXPRESS_CLASS_CODE_AND_REVISION_ID_REGISTER:
        s->pci_express_class_code_and_revision_id_register = val;
        break;
    case PCI_EXPRESS_BIST_HEADER_TYPE_AND_CACHE_LINE_SIZE_REGISTER:
        s->pci_express_bist_header_type_and_cache_line_size_register = val;
        break;
    case PCI_EXPRESS_BAR0_INTERNAL_REGISTER:
        s->pci_express_bar0_internal_register = val;
        break;
    case PCI_EXPRESS_BAR0_INTERNAL_HIGH_REGISTER:
        s->pci_express_bar0_internal_high_register = val;
        break;
    case PCI_EXPRESS_BAR1_REGISTER:
        s->pci_express_bar1_register = val;
        break;
    case PCI_EXPRESS_BAR1_HIGH_REGISTER:
        s->pci_express_bar1_high_register = val;
        break;
    case PCI_EXPRESS_BAR2_REGISTER:
        s->pci_express_bar2_register = val;
        break;
    case PCI_EXPRESS_BAR2_HIGH_REGISTER:
        s->pci_express_bar2_high_register = val;
        break;
    case PCI_EXPRESS_SUBSYSTEM_DEVICE_AND_VENDOR_ID:
        s->pci_express_subsystem_device_and_vendor_id = val;
        break;
    case PCI_EXPRESS_EXPANSION_ROM_BAR_REGISTER:
        s->pci_express_expansion_rom_bar_register = val;
        break;
    case PCI_EXPRESS_CAPABILITY_LIST_POINTER_REGISTER:
        s->pci_express_capability_list_pointer_register = val;
        break;
    case PCI_EXPRESS_INTERRUPT_PIN_AND_LINE_REGISTER:
        s->pci_express_interrupt_pin_and_line_register = val;
        break;
    case PCI_EXPRESS_POWER_MANAGEMENT_CAPABILITY_HEADER_REGISTER:
        s->pci_express_power_management_capability_header_register = val;
        break;
    case PCI_EXPRESS_POWER_MANAGEMENT_CONTROL_AND_STATUS_REGISTER:
        s->pci_express_power_management_control_and_status_register = val;
        break;
    case PCI_EXPRESS_MSI_MESSAGE_CONTROL_REGISTER:
        s->pci_express_msi_message_control_register = val;
        break;
    case PCI_EXPRESS_MSI_MESSAGE_ADDRESS_REGISTER:
        s->pci_express_msi_message_address_register = val;
        break;
    case PCI_EXPRESS_MSI_MESSAGE_ADDRESS_HIGH_REGISTER:
        s->pci_express_msi_message_address_high_register = val;
        break;
    case PCI_EXPRESS_MSI_MESSAGE_DATA_REGISTER:
        s->pci_express_msi_message_data_register = val;
        break;
    case PCI_EXPRESS_CAPABILITY_REGISTER:
        s->pci_express_capability_register = val;
        break;
    case PCI_EXPRESS_DEVICE_CAPABILITIES_REGISTER:
        s->pci_express_device_capabilities_register = val;
        break;
    case PCI_EXPRESS_DEVICE_CONTROL_STATUS_REGISTER:
        s->pci_express_device_control_status_register = val;
        break;
    case PCI_EXPRESS_LINK_CAPABILITIES_REGISTER:
        s->pci_express_link_capabilities_register = val;
        break;
    case PCI_EXPRESS_LINK_CONTROL_STATUS_REGISTER:
        s->pci_express_link_control_status_register = val;
        break;
    case PCI_EXPRESS_ADVANCED_ERROR_REPORT_HEADER_REGISTER:
        s->pci_express_advanced_error_report_header_register = val;
        break;
    case PCI_EXPRESS_UNCORRECTABLE_ERROR_STATUS_REGISTER:
        s->pci_express_uncorrectable_error_status_register = val;
        break;
    case PCI_EXPRESS_UNCORRECTABLE_ERROR_MASK_REGISTER:
        s->pci_express_uncorrectable_error_mask_register = val;
        break;
    case PCI_EXPRESS_UNCORRECTABLE_ERROR_SEVERITY_REGISTER:
        s->pci_express_uncorrectable_error_severity_register = val;
        break;
    case PCI_EXPRESS_CORRECTABLE_ERROR_STATUS_REGISTER:
        s->pci_express_correctable_error_status_register = val;
        break;
    case PCI_EXPRESS_CORRECTABLE_ERROR_MASK_REGISTER:
        s->pci_express_correctable_error_mask_register = val;
        break;
    case PCI_EXPRESS_ADVANCED_ERROR_CAPABILITY_AND_CONTROL_REGISTER:
        s->pci_express_advanced_error_capability_and_control_register = val;
        break;
    case PCI_EXPRESS_HEADER_LOG_FIRST_DWORD_REGISTER:
        s->pci_express_header_log_first_dword_register = val;
        break;
    case PCI_EXPRESS_HEADER_LOG_SECOND_DWORD_REGISTER:
        s->pci_express_header_log_second_dword_register = val;
        break;
    case PCI_EXPRESS_HEADER_LOG_THIRD_DWORD_REGISTER:
        s->pci_express_header_log_third_dword_register = val;
        break;
    case PCI_EXPRESS_HEADER_LOG_FOURTH_DWORD_REGISTER:
        s->pci_express_header_log_fourth_dword_register = val;
        break;
    case PCI_EXPRESS_BAR1_CONTROL_REGISTER:
        s->pci_express_bar1_control_register = val;
        break;
    case PCI_EXPRESS_BAR2_CONTROL_REGISTER:
        s->pci_express_bar2_control_register = val;
        break;
    case PCI_EXPRESS_EXPANSION_ROM_BAR_CONTROL_REGISTER:
        s->pci_express_expansion_rom_bar_control_register = val;
        break;
    case PCI_EXPRESS_CONFIGURATION_ADDRESS_REGISTER:
        s->pci_express_configuration_address_register = val;
        break;
    case PCI_EXPRESS_CONFIGURATION_DATA_REGISTER:
        s->pci_express_configuration_data_register = val;
        break;
    case PCI_EXPRESS_INTERRUPT_CAUSE:
        s->pci_express_interrupt_cause = val;
        break;
    case PCI_EXPRESS_INTERRUPT_MASK:
        s->pci_express_interrupt_mask = val;
        break;
    case PCI_EXPRESS_WINDOW0_CONTROL_REGISTER:
        s->pci_express_window0_control_register = val;
        break;
    case PCI_EXPRESS_WINDOW0_BASE_REGISTER:
        s->pci_express_window0_base_register = val;
        break;
    case PCI_EXPRESS_WINDOW0_REMAP_REGISTER:
        s->pci_express_window0_remap_register = val;
        break;
    case PCI_EXPRESS_WINDOW1_CONTROL_REGISTER:
        s->pci_express_window1_control_register = val;
        break;
    case PCI_EXPRESS_WINDOW1_BASE_REGISTER:
        s->pci_express_window1_base_register = val;
        break;
    case PCI_EXPRESS_WINDOW1_REMAP_REGISTER:
        s->pci_express_window1_remap_register = val;
        break;
    case PCI_EXPRESS_WINDOW2_CONTROL_REGISTER:
        s->pci_express_window2_control_register = val;
        break;
    case PCI_EXPRESS_WINDOW2_BASE_REGISTER:
        s->pci_express_window2_base_register = val;
        break;
    case PCI_EXPRESS_WINDOW2_REMAP_REGISTER:
        s->pci_express_window2_remap_register = val;
        break;
    case PCI_EXPRESS_WINDOW3_CONTROL_REGISTER:
        s->pci_express_window3_control_register = val;
        break;
    case PCI_EXPRESS_WINDOW3_BASE_REGISTER:
        s->pci_express_window3_base_register = val;
        break;
    case PCI_EXPRESS_WINDOW3_REMAP_REGISTER:
        s->pci_express_window3_remap_register = val;
        break;
    case PCI_EXPRESS_WINDOW4_CONTROL_REGISTER:
        s->pci_express_window4_control_register = val;
        break;
    case PCI_EXPRESS_WINDOW4_BASE_REGISTER:
        s->pci_express_window4_base_register = val;
        break;
    case PCI_EXPRESS_WINDOW4_REMAP_REGISTER:
        s->pci_express_window4_remap_register = val;
        break;
    case PCI_EXPRESS_WINDOW5_CONTROL_REGISTER:
        s->pci_express_window5_control_register = val;
        break;
    case PCI_EXPRESS_WINDOW5_BASE_REGISTER:
        s->pci_express_window5_base_register = val;
        break;
    case PCI_EXPRESS_WINDOW5_REMAP_REGISTER:
        s->pci_express_window5_remap_register = val;
        break;
    case PCI_EXPRESS_DEFAULT_WINDOW_CONTROL_REGISTER:
        s->pci_express_default_window_control_register = val;
        break;
    case PCI_EXPRESS_EXPANSION_ROM_WINDOW_CONTROL_REGISTER:
        s->pci_express_expansion_rom_window_control_register = val;
        break;
    case PCI_EXPRESS_EXPANSION_ROM_WINDOW_REMAP_REGISTER:
        s->pci_express_expansion_rom_window_remap_register = val;
        break;
    case PCI_EXPRESS_CONTROL_REGISTER:
        s->pci_express_control_register = val;
        break;
    case PCI_EXPRESS_STATUS_REGISTER:
        s->pci_express_status_register = val;
        break;
    case PCI_EXPRESS_COMPLETION_TIMEOUT_REGISTER:
        s->pci_express_completion_timeout_register = val;
        break;
    case PCI_EXPRESS_FLOW_CONTROL_REGISTER:
        s->pci_express_flow_control_register = val;
        break;
    case PCI_EXPRESS_ACKNOWLEDGE_TIMERS_1X_REGISTER:
        s->pci_express_acknowledge_timers_1x_register = val;
        break;
    case PCI_EXPRESS_DEBUG_CONTROL_REGISTER:
        s->pci_express_debug_control_register = val;
        break;
    case PCI_EXPRESS_TL_CONTROL_REGISTER:
        s->pci_express_tl_control_register = val;
        break;
    }
    mv88f5181L_pcie_update(s);
    return;
}

static const MemoryRegionOps mv88f5181L_pcie_ops = {
    .read = mv88f5181L_pcie_read,
    .write = mv88f5181L_pcie_write,
    .endianness = DEVICE_NATIVE_ENDIAN,
};

static void mv88f5181L_pcie_init(Object *obj) {
    MV88F5181LPCIEState *s = MV88F5181L_PCIE(obj);

    /* initialize the mmio */
    memory_region_init_io(&s->mmio, obj, &mv88f5181L_pcie_ops, s, "mv88f5181L_pcie", MV88F5181L_PCIE_MMIO_SIZE);
    sysbus_init_mmio(SYS_BUS_DEVICE(s), &s->mmio);
}

static void mv88f5181L_pcie_reset(DeviceState *dev) {
    MV88F5181LPCIEState *s = MV88F5181L_PCIE(dev);
    
    s->pci_express_device_and_vendor_id_register = 0x11AB << 0 | 0x5181 << 16;
    s->pci_express_command_and_status_register = 0x0;
    s->pci_express_class_code_and_revision_id_register = 0x3;
    s->pci_express_bist_header_type_and_cache_line_size_register = 0x0;
    s->pci_express_bar0_internal_register = 0x0;
    s->pci_express_bar0_internal_high_register = 0x0;
    s->pci_express_bar1_register = 0x0;
    s->pci_express_bar1_high_register = 0x0;
    s->pci_express_bar2_register = 0x0;
    s->pci_express_bar2_high_register = 0x0;
    s->pci_express_subsystem_device_and_vendor_id = 0x0;
    s->pci_express_expansion_rom_bar_register = 0x0;
    s->pci_express_capability_list_pointer_register = 0x0;
    s->pci_express_interrupt_pin_and_line_register = 0x0;
    s->pci_express_power_management_capability_header_register = 0x0;
    s->pci_express_power_management_control_and_status_register = 0x0;
    s->pci_express_msi_message_control_register = 0x0;
    s->pci_express_msi_message_address_register = 0x0;
    s->pci_express_msi_message_address_high_register = 0x0;
    s->pci_express_msi_message_data_register = 0x0;
    s->pci_express_capability_register = 0x0;
    s->pci_express_device_capabilities_register = 0x0;
    s->pci_express_device_control_status_register = 0x0;
    s->pci_express_link_capabilities_register = 0x0;
    s->pci_express_link_control_status_register = 0x0;
    s->pci_express_advanced_error_report_header_register = 0x0;
    s->pci_express_uncorrectable_error_status_register = 0x0;
    s->pci_express_uncorrectable_error_mask_register = 0x0;
    s->pci_express_uncorrectable_error_severity_register = 0x0;
    s->pci_express_correctable_error_status_register = 0x0;
    s->pci_express_correctable_error_mask_register = 0x0;
    s->pci_express_advanced_error_capability_and_control_register = 0x0;
    s->pci_express_header_log_first_dword_register = 0x0;
    s->pci_express_header_log_second_dword_register = 0x0;
    s->pci_express_header_log_third_dword_register = 0x0;
    s->pci_express_header_log_fourth_dword_register = 0x0;
    s->pci_express_bar1_control_register = 0x0;
    s->pci_express_bar2_control_register = 0x0;
    s->pci_express_expansion_rom_bar_control_register = 0x0;
    s->pci_express_configuration_address_register = 0x0;
    s->pci_express_configuration_data_register = 0x0;
    s->pci_express_interrupt_cause = 0x0;
    s->pci_express_interrupt_mask = 0x0;
    s->pci_express_window0_control_register = 0x0;
    s->pci_express_window0_base_register = 0x0;
    s->pci_express_window0_remap_register = 0x0;
    s->pci_express_window1_control_register = 0x0;
    s->pci_express_window1_base_register = 0x0;
    s->pci_express_window1_remap_register = 0x0;
    s->pci_express_window2_control_register = 0x0;
    s->pci_express_window2_base_register = 0x0;
    s->pci_express_window2_remap_register = 0x0;
    s->pci_express_window3_control_register = 0x0;
    s->pci_express_window3_base_register = 0x0;
    s->pci_express_window3_remap_register = 0x0;
    s->pci_express_window4_control_register = 0x0;
    s->pci_express_window4_base_register = 0x0;
    s->pci_express_window4_remap_register = 0x0;
    s->pci_express_window5_control_register = 0x0;
    s->pci_express_window5_base_register = 0x0;
    s->pci_express_window5_remap_register = 0x0;
    s->pci_express_default_window_control_register = 0x0;
    s->pci_express_expansion_rom_window_control_register = 0x0;
    s->pci_express_expansion_rom_window_remap_register = 0x0;
    s->pci_express_control_register = 0x0;
    s->pci_express_status_register = 0x0;
    s->pci_express_completion_timeout_register = 0x0;
    s->pci_express_flow_control_register = 0x0;
    s->pci_express_acknowledge_timers_1x_register = 0x0;
    s->pci_express_debug_control_register = 0x0;
    s->pci_express_tl_control_register = 0x0;
}

static void mv88f5181L_pcie_class_init(ObjectClass *klass, void *data) {
    DeviceClass *dc = DEVICE_CLASS(klass);

    /* dc->fw_name = ; */
    /* dc->desc = ; */
    /* dc->props = ; */
    /* dc->user_creatable = ; */
    /* dc->hotpluggable = ; */
    dc->reset = mv88f5181L_pcie_reset;
    /* dc->realize = ; */
    /* dc->unrealize = ; */
    /* dc->vmsd = ; */
    /* dc->bus_type = ; */

    /* SysBusDeviceClass sbc = SYS_BUS_DEVICE_CLASS(klass); */

    /* sbc->explicit_ofw_unit_address = ; */
    /* sbc->connect_irq_notifier = ; */
}

static const TypeInfo mv88f5181L_pcie_info = {
    .name = TYPE_MV88F5181L_PCIE,
    .parent = TYPE_SYS_BUS_DEVICE,
    .instance_size = sizeof(MV88F5181LPCIEState),
    .instance_init = mv88f5181L_pcie_init,
    /* .class_zie = sizeof(SysBusDeviceClass), */
    .class_init = mv88f5181L_pcie_class_init,
};

static void mv88f5181L_pcie_register_types(void) {
    type_register_static(&mv88f5181L_pcie_info);
}

type_init(mv88f5181L_pcie_register_types)