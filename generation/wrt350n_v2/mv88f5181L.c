/* 
 * automatically generated, don't change
 */

#include "qemu/osdep.h"
#include "qemu/log.h"
#include "qapi/error.h"
#include "target/arm/cpu.h"
#include "hw/arm/mv88f5181L.h"

static void mv88f5181_cpu_address_map_update(void *opaque);
static uint64_t mv88f5181_cpu_address_map_read(void *opaque, hwaddr offset, unsigned size);
static void mv88f5181_cpu_address_map_write(void *opaque, hwaddr offset, uint64_t val, unsigned size);
static void mv88f5181_ddr_sdram_controller_update(void *opaque);
static uint64_t mv88f5181_ddr_sdram_controller_read(void *opaque, hwaddr offset, unsigned size);
static void mv88f5181_ddr_sdram_controller_write(void *opaque, hwaddr offset, uint64_t val, unsigned size);
static void mv88f5181l_pins_multiplexing_interface_update(void *opaque);
static uint64_t mv88f5181l_pins_multiplexing_interface_read(void *opaque, hwaddr offset, unsigned size);
static void mv88f5181l_pins_multiplexing_interface_write(void *opaque, hwaddr offset, uint64_t val, unsigned size);
static void mv88f5181l_pci_interface_update(void *opaque);
static uint64_t mv88f5181l_pci_interface_read(void *opaque, hwaddr offset, unsigned size);
static void mv88f5181l_pci_interface_write(void *opaque, hwaddr offset, uint64_t val, unsigned size);
static void mv88f5181l_pcie_interface_update(void *opaque);
static uint64_t mv88f5181l_pcie_interface_read(void *opaque, hwaddr offset, unsigned size);
static void mv88f5181l_pcie_interface_write(void *opaque, hwaddr offset, uint64_t val, unsigned size);

static void mv88f5181L_init(Object *obj);
static void mv88f5181L_realize(DeviceState *dev, Error **errp);
static void mv88f5181L_reset(DeviceState *d);

static void mv88f5181L_class_init(ObjectClass *oc, void *data);
static void mv88f5181L_register_types(void);

static void mv88f5181_cpu_address_map_update(void *opaque) {
    /* MV88F5181LState *s = opaque; */
}

static uint64_t mv88f5181_cpu_address_map_read(void *opaque, hwaddr offset, unsigned size) {
    MV88F5181LState *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case WINDOW0_CONTROL_REGISTER:
        res = s->window0_control_register;
        break;
    case WINDOW0_BASE_REGISTER:
        res = s->window0_base_register;
        break;
    case WINDOW0_REMAP_LOW_REGISTER:
        res = s->window0_remap_low_register;
        break;
    case WINDOW0_REMAP_HIGH_REGISTER:
        res = s->window0_remap_high_register;
        break;
    case WINDOW1_CONTROL_REGISTER:
        res = s->window1_control_register;
        break;
    case WINDOW1_BASE_REGISTER:
        res = s->window1_base_register;
        break;
    case WINDOW1_REMAP_LOW_REGISTER:
        res = s->window1_remap_low_register;
        break;
    case WINDOW1_REMAP_HIGH_REGISTER:
        res = s->window1_remap_high_register;
        break;
    case WINDOW2_CONTROL_REGISTER:
        res = s->window2_control_register;
        break;
    case WINDOW2_BASE_REGISTER:
        res = s->window2_base_register;
        break;
    case WINDOW2_REMAP_LOW_REGISTER:
        res = s->window2_remap_low_register;
        break;
    case WINDOW2_REMAP_HIGH_REGISTER:
        res = s->window2_remap_high_register;
        break;
    case WINDOW3_CONTROL_REGISTER:
        res = s->window3_control_register;
        break;
    case WINDOW3_BASE_REGISTER:
        res = s->window3_base_register;
        break;
    case WINDOW4_CONTROL_REGISTER:
        res = s->window4_control_register;
        break;
    case WINDOW4_BASE_REGISTER:
        res = s->window4_base_register;
        break;
    case WINDOW5_CONTROL_REGISTER:
        res = s->window5_control_register;
        break;
    case WINDOW5_BASE_REGISTER:
        res = s->window5_base_register;
        break;
    case WINDOW6_CONTROL_REGISTER:
        res = s->window6_control_register;
        break;
    case WINDOW6_BASE_REGISTER:
        res = s->window6_base_register;
        break;
    case WINDOW7_CONTROL_REGISTER:
        res = s->window7_control_register;
        break;
    case WINDOW7_BASE_REGISTER:
        res = s->window7_base_register;
        break;
    case _88F5181_INTERNAL_REGISTERS_BASE_ADDRESS_REGISTER:
        res = s->_88f5181_internal_registers_base_address_register;
        break;
    }
    return res;
}

static void mv88f5181_cpu_address_map_write(void *opaque, hwaddr offset, uint64_t val, unsigned size) {
    MV88F5181LState *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case WINDOW0_CONTROL_REGISTER:
        s->window0_control_register = val;
        break;
    case WINDOW0_BASE_REGISTER:
        s->window0_base_register = val;
        break;
    case WINDOW0_REMAP_LOW_REGISTER:
        s->window0_remap_low_register = val;
        break;
    case WINDOW0_REMAP_HIGH_REGISTER:
        s->window0_remap_high_register = val;
        break;
    case WINDOW1_CONTROL_REGISTER:
        s->window1_control_register = val;
        break;
    case WINDOW1_BASE_REGISTER:
        s->window1_base_register = val;
        break;
    case WINDOW1_REMAP_LOW_REGISTER:
        s->window1_remap_low_register = val;
        break;
    case WINDOW1_REMAP_HIGH_REGISTER:
        s->window1_remap_high_register = val;
        break;
    case WINDOW2_CONTROL_REGISTER:
        s->window2_control_register = val;
        break;
    case WINDOW2_BASE_REGISTER:
        s->window2_base_register = val;
        break;
    case WINDOW2_REMAP_LOW_REGISTER:
        s->window2_remap_low_register = val;
        break;
    case WINDOW2_REMAP_HIGH_REGISTER:
        s->window2_remap_high_register = val;
        break;
    case WINDOW3_CONTROL_REGISTER:
        s->window3_control_register = val;
        break;
    case WINDOW3_BASE_REGISTER:
        s->window3_base_register = val;
        break;
    case WINDOW4_CONTROL_REGISTER:
        s->window4_control_register = val;
        break;
    case WINDOW4_BASE_REGISTER:
        s->window4_base_register = val;
        break;
    case WINDOW5_CONTROL_REGISTER:
        s->window5_control_register = val;
        break;
    case WINDOW5_BASE_REGISTER:
        s->window5_base_register = val;
        break;
    case WINDOW6_CONTROL_REGISTER:
        s->window6_control_register = val;
        break;
    case WINDOW6_BASE_REGISTER:
        s->window6_base_register = val;
        break;
    case WINDOW7_CONTROL_REGISTER:
        s->window7_control_register = val;
        break;
    case WINDOW7_BASE_REGISTER:
        s->window7_base_register = val;
        break;
    case _88F5181_INTERNAL_REGISTERS_BASE_ADDRESS_REGISTER:
        s->_88f5181_internal_registers_base_address_register = val;
        break;
    }
    mv88f5181_cpu_address_map_update(s);
}

static const MemoryRegionOps mv88f5181_cpu_address_map_ops = {
    .read = mv88f5181_cpu_address_map_read,
    .write = mv88f5181_cpu_address_map_write,
    .endianness = DEVICE_NATIVE_ENDIAN,
};

static void mv88f5181_ddr_sdram_controller_update(void *opaque) {
    /* MV88F5181LState *s = opaque; */
}

static uint64_t mv88f5181_ddr_sdram_controller_read(void *opaque, hwaddr offset, unsigned size) {
    MV88F5181LState *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case CS0N_BASE_ADDRESS_REGISTER:
        res = s->cs0n_base_address_register;
        break;
    case CS0N_SIZE_REGISTER:
        res = s->cs0n_size_register;
        break;
    case CS1N_BASE_ADDRESS_REGISTER:
        res = s->cs1n_base_address_register;
        break;
    case CS1N_SIZE_REGISTER:
        res = s->cs1n_size_register;
        break;
    case CS2N_BASE_ADDRESS_REGISTER:
        res = s->cs2n_base_address_register;
        break;
    case CS2N_SIZE_REGISTER:
        res = s->cs2n_size_register;
        break;
    case CS3N_BASE_ADDRESS_REGISTER:
        res = s->cs3n_base_address_register;
        break;
    case CS3N_SIZE_REGISTER:
        res = s->cs3n_size_register;
        break;
    case DDR_SDRAM_CONFIGURATION_REGISTER:
        res = s->ddr_sdram_configuration_register;
        break;
    case DDR_SDRAM_CONTROL_REGISTER:
        res = s->ddr_sdram_control_register;
        break;
    case DDR_SDRAM_TIMING_LOW_REGISTER:
        res = s->ddr_sdram_timing_low_register;
        break;
    case DDR_SDRAM_TIMING_HIGH_REGISTER:
        res = s->ddr_sdram_timing_high_register;
        break;
    case DDR2_SDRAM_TIMING_LOW_REGISTER:
        res = s->ddr2_sdram_timing_low_register;
        break;
    case DDR2_SDRAM_TIMING_HIGH_REGISTER:
        res = s->ddr2_sdram_timing_high_register;
        break;
    case DDR_SDRAM_ADDRESS_CONTROL_REGISTER:
        res = s->ddr_sdram_address_control_register;
        break;
    case DDR_SDRAM_OPEN_PAGES_CONTROL_REGISTER:
        res = s->ddr_sdram_open_pages_control_register;
        break;
    case DDR_SDRAM_OPERATION_REGISTER:
        res = s->ddr_sdram_operation_register;
        break;
    case DDR_SDRAM_OPERATION_CONTROL_REGISTER:
        res = s->ddr_sdram_operation_control_register;
        break;
    case DDR_SDRAM_MODE_REGISTER:
        res = s->ddr_sdram_mode_register;
        break;
    case EXTENDED_DDR_SDRAM_MODE_REGISTER:
        res = s->extended_ddr_sdram_mode_register;
        break;
    case DDR_SDRAM_INITIALIZATION_CONTROL_REGISTER:
        res = s->ddr_sdram_initialization_control_register;
        break;
    case DDR_SDRAM_ADDRESS_OR_CONTROL_PADS_CALIBRATION_REGISTER:
        res = s->ddr_sdram_address_or_control_pads_calibration_register;
        break;
    case DDR_SDRAM_DATA_PADS_CALIBRATION_REGISTER:
        res = s->ddr_sdram_data_pads_calibration_register;
        break;
    case DDR2_SDRAM_ODT_CONTROL_LOW_REGISTER:
        res = s->ddr2_sdram_odt_control_low_register;
        break;
    case DDR2_SDRAM_ODT_CONTROL_HIGH_REGISTER:
        res = s->ddr2_sdram_odt_control_high_register;
        break;
    case DDR2_SDRAM_ODT_CONTROL_REGISTER:
        res = s->ddr2_sdram_odt_control_register;
        break;
    case DDR_SDRAM_INTERFACE_MBUS_CONTROL_LOW_REGISTER:
        res = s->ddr_sdram_interface_mbus_control_low_register;
        break;
    case DDR_SDRAM_INTERFACE_MBUS_CONTROL_HIGH_REGISTER:
        res = s->ddr_sdram_interface_mbus_control_high_register;
        break;
    case DDR_SDRAM_INTERFACE_MBUS_TIMEOUT_REGISTER:
        res = s->ddr_sdram_interface_mbus_timeout_register;
        break;
    case DDR_SDRAM_MMASK_REGISTER:
        res = s->ddr_sdram_mmask_register;
        break;
    }
    return res;
}

static void mv88f5181_ddr_sdram_controller_write(void *opaque, hwaddr offset, uint64_t val, unsigned size) {
    MV88F5181LState *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case CS0N_BASE_ADDRESS_REGISTER:
        s->cs0n_base_address_register = val;
        break;
    case CS0N_SIZE_REGISTER:
        s->cs0n_size_register = val;
        break;
    case CS1N_BASE_ADDRESS_REGISTER:
        s->cs1n_base_address_register = val;
        break;
    case CS1N_SIZE_REGISTER:
        s->cs1n_size_register = val;
        break;
    case CS2N_BASE_ADDRESS_REGISTER:
        s->cs2n_base_address_register = val;
        break;
    case CS2N_SIZE_REGISTER:
        s->cs2n_size_register = val;
        break;
    case CS3N_BASE_ADDRESS_REGISTER:
        s->cs3n_base_address_register = val;
        break;
    case CS3N_SIZE_REGISTER:
        s->cs3n_size_register = val;
        break;
    case DDR_SDRAM_CONFIGURATION_REGISTER:
        s->ddr_sdram_configuration_register = val;
        break;
    case DDR_SDRAM_CONTROL_REGISTER:
        s->ddr_sdram_control_register = val;
        break;
    case DDR_SDRAM_TIMING_LOW_REGISTER:
        s->ddr_sdram_timing_low_register = val;
        break;
    case DDR_SDRAM_TIMING_HIGH_REGISTER:
        s->ddr_sdram_timing_high_register = val;
        break;
    case DDR2_SDRAM_TIMING_LOW_REGISTER:
        s->ddr2_sdram_timing_low_register = val;
        break;
    case DDR2_SDRAM_TIMING_HIGH_REGISTER:
        s->ddr2_sdram_timing_high_register = val;
        break;
    case DDR_SDRAM_ADDRESS_CONTROL_REGISTER:
        s->ddr_sdram_address_control_register = val;
        break;
    case DDR_SDRAM_OPEN_PAGES_CONTROL_REGISTER:
        s->ddr_sdram_open_pages_control_register = val;
        break;
    case DDR_SDRAM_OPERATION_REGISTER:
        s->ddr_sdram_operation_register = val;
        break;
    case DDR_SDRAM_OPERATION_CONTROL_REGISTER:
        s->ddr_sdram_operation_control_register = val;
        break;
    case DDR_SDRAM_MODE_REGISTER:
        s->ddr_sdram_mode_register = val;
        break;
    case EXTENDED_DDR_SDRAM_MODE_REGISTER:
        s->extended_ddr_sdram_mode_register = val;
        break;
    case DDR_SDRAM_INITIALIZATION_CONTROL_REGISTER:
        s->ddr_sdram_initialization_control_register = val;
        break;
    case DDR_SDRAM_ADDRESS_OR_CONTROL_PADS_CALIBRATION_REGISTER:
        s->ddr_sdram_address_or_control_pads_calibration_register = val;
        break;
    case DDR_SDRAM_DATA_PADS_CALIBRATION_REGISTER:
        s->ddr_sdram_data_pads_calibration_register = val;
        break;
    case DDR2_SDRAM_ODT_CONTROL_LOW_REGISTER:
        s->ddr2_sdram_odt_control_low_register = val;
        break;
    case DDR2_SDRAM_ODT_CONTROL_HIGH_REGISTER:
        s->ddr2_sdram_odt_control_high_register = val;
        break;
    case DDR2_SDRAM_ODT_CONTROL_REGISTER:
        s->ddr2_sdram_odt_control_register = val;
        break;
    case DDR_SDRAM_INTERFACE_MBUS_CONTROL_LOW_REGISTER:
        s->ddr_sdram_interface_mbus_control_low_register = val;
        break;
    case DDR_SDRAM_INTERFACE_MBUS_CONTROL_HIGH_REGISTER:
        s->ddr_sdram_interface_mbus_control_high_register = val;
        break;
    case DDR_SDRAM_INTERFACE_MBUS_TIMEOUT_REGISTER:
        s->ddr_sdram_interface_mbus_timeout_register = val;
        break;
    case DDR_SDRAM_MMASK_REGISTER:
        s->ddr_sdram_mmask_register = val;
        break;
    }
    mv88f5181_ddr_sdram_controller_update(s);
}

static const MemoryRegionOps mv88f5181_ddr_sdram_controller_ops = {
    .read = mv88f5181_ddr_sdram_controller_read,
    .write = mv88f5181_ddr_sdram_controller_write,
    .endianness = DEVICE_NATIVE_ENDIAN,
};

static void mv88f5181l_pins_multiplexing_interface_update(void *opaque) {
    /* MV88F5181LState *s = opaque; */
}

static uint64_t mv88f5181l_pins_multiplexing_interface_read(void *opaque, hwaddr offset, unsigned size) {
    MV88F5181LState *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case MPP_CONTROL_0_REGISTER:
        res = s->mpp_control_0_register;
        break;
    case MPP_CONTROL_1_REGISTER:
        res = s->mpp_control_1_register;
        break;
    case MPP_CONTROL_2_REGISTER:
        res = s->mpp_control_2_register;
        break;
    case DEVICE_MULTIPLEX_CONTROL_REGISTER:
        res = s->device_multiplex_control_register;
        break;
    case SAMPLE_AT_RESET_REGISTER:
        res = s->sample_at_reset_register;
        break;
    }
    return res;
}

static void mv88f5181l_pins_multiplexing_interface_write(void *opaque, hwaddr offset, uint64_t val, unsigned size) {
    MV88F5181LState *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case MPP_CONTROL_0_REGISTER:
        s->mpp_control_0_register = val;
        break;
    case MPP_CONTROL_1_REGISTER:
        s->mpp_control_1_register = val;
        break;
    case MPP_CONTROL_2_REGISTER:
        s->mpp_control_2_register = val;
        break;
    case DEVICE_MULTIPLEX_CONTROL_REGISTER:
        s->device_multiplex_control_register = val;
        break;
    case SAMPLE_AT_RESET_REGISTER:
        s->sample_at_reset_register = val;
        break;
    }
    mv88f5181l_pins_multiplexing_interface_update(s);
}

static const MemoryRegionOps mv88f5181l_pins_multiplexing_interface_ops = {
    .read = mv88f5181l_pins_multiplexing_interface_read,
    .write = mv88f5181l_pins_multiplexing_interface_write,
    .endianness = DEVICE_NATIVE_ENDIAN,
};

static void mv88f5181l_pci_interface_update(void *opaque) {
    /* MV88F5181LState *s = opaque; */
}

static uint64_t mv88f5181l_pci_interface_read(void *opaque, hwaddr offset, unsigned size) {
    MV88F5181LState *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case CSN0_BAR_SIZE:
        res = s->csn0_bar_size;
        break;
    case CSN1_BAR_SIZE:
        res = s->csn1_bar_size;
        break;
    case CSN2_BAR_SIZE:
        res = s->csn2_bar_size;
        break;
    case CSN3_BAR_SIZE:
        res = s->csn3_bar_size;
        break;
    case DEVCSN0_BAR_SIZE:
        res = s->devcsn0_bar_size;
        break;
    case DEVCSN1_BAR_SIZE:
        res = s->devcsn1_bar_size;
        break;
    case DEVCSN2_BAR_SIZE:
        res = s->devcsn2_bar_size;
        break;
    case BOOT_CSN_BAR_SIZE:
        res = s->boot_csn_bar_size;
        break;
    case P2P_MEM0_BAR_SIZE:
        res = s->p2p_mem0_bar_size;
        break;
    case P2P_I_OR_O_BAR_SIZE:
        res = s->p2p_i_or_o_bar_size;
        break;
    case EXPANSION_ROM_BAR_SIZE:
        res = s->expansion_rom_bar_size;
        break;
    case BASE_ADDRESS_REGISTERS_ENABLE:
        res = s->base_address_registers_enable;
        break;
    case CSN0_BASE_ADDRESS_REMAP:
        res = s->csn0_base_address_remap;
        break;
    case CSN1_BASE_ADDRESS_REMAP:
        res = s->csn1_base_address_remap;
        break;
    case CSN2_BASE_ADDRESS_REMAP:
        res = s->csn2_base_address_remap;
        break;
    case CSN3_BASE_ADDRESS_REMAP:
        res = s->csn3_base_address_remap;
        break;
    case DEVCSN0_BASE_ADDRESS_REMAP:
        res = s->devcsn0_base_address_remap;
        break;
    case DEVCSN1_BASE_ADDRESS_REMAP:
        res = s->devcsn1_base_address_remap;
        break;
    case DEVCSN2_BASE_ADDRESS_REMAP:
        res = s->devcsn2_base_address_remap;
        break;
    case BOOTCSN_BASE_ADDRESS_REMAP:
        res = s->bootcsn_base_address_remap;
        break;
    case P2P_MEM0_BASE_ADDRESS_REMAP_LOW:
        res = s->p2p_mem0_base_address_remap_low;
        break;
    case P2P_MEM0_BASE_ADDRESS_REMAP_HIGH:
        res = s->p2p_mem0_base_address_remap_high;
        break;
    case P2P_I_OR_O_BASE_ADDRESS_REMAP:
        res = s->p2p_i_or_o_base_address_remap;
        break;
    case EXPANSION_ROM_BASE_ADDRESS_REMAP:
        res = s->expansion_rom_base_address_remap;
        break;
    case DRAM_BAR_BANK_SELECT:
        res = s->dram_bar_bank_select;
        break;
    case PCI_ADDRESS_DECODE_CONTROL:
        res = s->pci_address_decode_control;
        break;
    case PCI_DLL_CONTROL:
        res = s->pci_dll_control;
        break;
    case PCI_OR_MPP_PADS_CALIBRATION:
        res = s->pci_or_mpp_pads_calibration;
        break;
    case PCI_COMMAND:
        res = s->pci_command;
        break;
    case PCI_MODE:
        res = s->pci_mode;
        break;
    case PCI_RETRY:
        res = s->pci_retry;
        break;
    case PCI_DISCARD_TIMER:
        res = s->pci_discard_timer;
        break;
    case MSI_TRIGGER_TIMER:
        res = s->msi_trigger_timer;
        break;
    case PCI_ARBITER_CONTROL:
        res = s->pci_arbiter_control;
        break;
    case PCI_P2P_CONFIGURATION:
        res = s->pci_p2p_configuration;
        break;
    case PCI_ACCESS_CONTROL_BASE_0_LOW:
        res = s->pci_access_control_base_0_low;
        break;
    case PCI_ACCESS_CONTROL_BASE_0_HIGH:
        res = s->pci_access_control_base_0_high;
        break;
    case PCI_ACCESS_CONTROL_SIZE_0:
        res = s->pci_access_control_size_0;
        break;
    case PCI_ACCESS_CONTROL_BASE_1_LOW:
        res = s->pci_access_control_base_1_low;
        break;
    case PCI_ACCESS_CONTROL_BASE_1_HIGH:
        res = s->pci_access_control_base_1_high;
        break;
    case PCI_ACCESS_CONTROL_SIZE_1:
        res = s->pci_access_control_size_1;
        break;
    case PCI_ACCESS_CONTROL_BASE_2_LOW:
        res = s->pci_access_control_base_2_low;
        break;
    case PCI_ACCESS_CONTROL_BASE_2_HIGH:
        res = s->pci_access_control_base_2_high;
        break;
    case PCI_ACCESS_CONTROL_SIZE_2:
        res = s->pci_access_control_size_2;
        break;
    case PCI_ACCESS_CONTROL_BASE_3_LOW:
        res = s->pci_access_control_base_3_low;
        break;
    case PCI_ACCESS_CONTROL_BASE_3_HIGH:
        res = s->pci_access_control_base_3_high;
        break;
    case PCI_ACCESS_CONTROL_SIZE_3:
        res = s->pci_access_control_size_3;
        break;
    case PCI_ACCESS_CONTROL_BASE_4_LOW:
        res = s->pci_access_control_base_4_low;
        break;
    case PCI_ACCESS_CONTROL_BASE_4_HIGH:
        res = s->pci_access_control_base_4_high;
        break;
    case PCI_ACCESS_CONTROL_SIZE_4:
        res = s->pci_access_control_size_4;
        break;
    case PCI_ACCESS_CONTROL_BASE_5_LOW:
        res = s->pci_access_control_base_5_low;
        break;
    case PCI_ACCESS_CONTROL_BASE_5_HIGH:
        res = s->pci_access_control_base_5_high;
        break;
    case PCI_ACCESS_CONTROL_SIZE_5:
        res = s->pci_access_control_size_5;
        break;
    case PCI_CONFIGURATION_ADDRESS:
        res = s->pci_configuration_address;
        break;
    case PCI_CONFIGURATION_DATA:
        res = s->pci_configuration_data;
        break;
    case PCI_INTERRUPT_ACKNOWLEDGE:
        res = s->pci_interrupt_acknowledge;
        break;
    case PCI_SERRN_MASK:
        res = s->pci_serrn_mask;
        break;
    case PCI_INTERRUPT_CAUSE:
        res = s->pci_interrupt_cause;
        break;
    case PCI_INTERRUPT_MASK:
        res = s->pci_interrupt_mask;
        break;
    case PCI_ERROR_ADDRESS_LOW:
        res = s->pci_error_address_low;
        break;
    case PCI_ERROR_ADDRESS_HIGH:
        res = s->pci_error_address_high;
        break;
    case PCI_ERROR_COMMAND:
        res = s->pci_error_command;
        break;
    }
    return res;
}

static void mv88f5181l_pci_interface_write(void *opaque, hwaddr offset, uint64_t val, unsigned size) {
    MV88F5181LState *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case CSN0_BAR_SIZE:
        s->csn0_bar_size = val;
        break;
    case CSN1_BAR_SIZE:
        s->csn1_bar_size = val;
        break;
    case CSN2_BAR_SIZE:
        s->csn2_bar_size = val;
        break;
    case CSN3_BAR_SIZE:
        s->csn3_bar_size = val;
        break;
    case DEVCSN0_BAR_SIZE:
        s->devcsn0_bar_size = val;
        break;
    case DEVCSN1_BAR_SIZE:
        s->devcsn1_bar_size = val;
        break;
    case DEVCSN2_BAR_SIZE:
        s->devcsn2_bar_size = val;
        break;
    case BOOT_CSN_BAR_SIZE:
        s->boot_csn_bar_size = val;
        break;
    case P2P_MEM0_BAR_SIZE:
        s->p2p_mem0_bar_size = val;
        break;
    case P2P_I_OR_O_BAR_SIZE:
        s->p2p_i_or_o_bar_size = val;
        break;
    case EXPANSION_ROM_BAR_SIZE:
        s->expansion_rom_bar_size = val;
        break;
    case BASE_ADDRESS_REGISTERS_ENABLE:
        s->base_address_registers_enable = val;
        break;
    case CSN0_BASE_ADDRESS_REMAP:
        s->csn0_base_address_remap = val;
        break;
    case CSN1_BASE_ADDRESS_REMAP:
        s->csn1_base_address_remap = val;
        break;
    case CSN2_BASE_ADDRESS_REMAP:
        s->csn2_base_address_remap = val;
        break;
    case CSN3_BASE_ADDRESS_REMAP:
        s->csn3_base_address_remap = val;
        break;
    case DEVCSN0_BASE_ADDRESS_REMAP:
        s->devcsn0_base_address_remap = val;
        break;
    case DEVCSN1_BASE_ADDRESS_REMAP:
        s->devcsn1_base_address_remap = val;
        break;
    case DEVCSN2_BASE_ADDRESS_REMAP:
        s->devcsn2_base_address_remap = val;
        break;
    case BOOTCSN_BASE_ADDRESS_REMAP:
        s->bootcsn_base_address_remap = val;
        break;
    case P2P_MEM0_BASE_ADDRESS_REMAP_LOW:
        s->p2p_mem0_base_address_remap_low = val;
        break;
    case P2P_MEM0_BASE_ADDRESS_REMAP_HIGH:
        s->p2p_mem0_base_address_remap_high = val;
        break;
    case P2P_I_OR_O_BASE_ADDRESS_REMAP:
        s->p2p_i_or_o_base_address_remap = val;
        break;
    case EXPANSION_ROM_BASE_ADDRESS_REMAP:
        s->expansion_rom_base_address_remap = val;
        break;
    case DRAM_BAR_BANK_SELECT:
        s->dram_bar_bank_select = val;
        break;
    case PCI_ADDRESS_DECODE_CONTROL:
        s->pci_address_decode_control = val;
        break;
    case PCI_DLL_CONTROL:
        s->pci_dll_control = val;
        break;
    case PCI_OR_MPP_PADS_CALIBRATION:
        s->pci_or_mpp_pads_calibration = val;
        break;
    case PCI_COMMAND:
        s->pci_command = val;
        break;
    case PCI_MODE:
        s->pci_mode = val;
        break;
    case PCI_RETRY:
        s->pci_retry = val;
        break;
    case PCI_DISCARD_TIMER:
        s->pci_discard_timer = val;
        break;
    case MSI_TRIGGER_TIMER:
        s->msi_trigger_timer = val;
        break;
    case PCI_ARBITER_CONTROL:
        s->pci_arbiter_control = val;
        break;
    case PCI_P2P_CONFIGURATION:
        s->pci_p2p_configuration = val;
        break;
    case PCI_ACCESS_CONTROL_BASE_0_LOW:
        s->pci_access_control_base_0_low = val;
        break;
    case PCI_ACCESS_CONTROL_BASE_0_HIGH:
        s->pci_access_control_base_0_high = val;
        break;
    case PCI_ACCESS_CONTROL_SIZE_0:
        s->pci_access_control_size_0 = val;
        break;
    case PCI_ACCESS_CONTROL_BASE_1_LOW:
        s->pci_access_control_base_1_low = val;
        break;
    case PCI_ACCESS_CONTROL_BASE_1_HIGH:
        s->pci_access_control_base_1_high = val;
        break;
    case PCI_ACCESS_CONTROL_SIZE_1:
        s->pci_access_control_size_1 = val;
        break;
    case PCI_ACCESS_CONTROL_BASE_2_LOW:
        s->pci_access_control_base_2_low = val;
        break;
    case PCI_ACCESS_CONTROL_BASE_2_HIGH:
        s->pci_access_control_base_2_high = val;
        break;
    case PCI_ACCESS_CONTROL_SIZE_2:
        s->pci_access_control_size_2 = val;
        break;
    case PCI_ACCESS_CONTROL_BASE_3_LOW:
        s->pci_access_control_base_3_low = val;
        break;
    case PCI_ACCESS_CONTROL_BASE_3_HIGH:
        s->pci_access_control_base_3_high = val;
        break;
    case PCI_ACCESS_CONTROL_SIZE_3:
        s->pci_access_control_size_3 = val;
        break;
    case PCI_ACCESS_CONTROL_BASE_4_LOW:
        s->pci_access_control_base_4_low = val;
        break;
    case PCI_ACCESS_CONTROL_BASE_4_HIGH:
        s->pci_access_control_base_4_high = val;
        break;
    case PCI_ACCESS_CONTROL_SIZE_4:
        s->pci_access_control_size_4 = val;
        break;
    case PCI_ACCESS_CONTROL_BASE_5_LOW:
        s->pci_access_control_base_5_low = val;
        break;
    case PCI_ACCESS_CONTROL_BASE_5_HIGH:
        s->pci_access_control_base_5_high = val;
        break;
    case PCI_ACCESS_CONTROL_SIZE_5:
        s->pci_access_control_size_5 = val;
        break;
    case PCI_CONFIGURATION_ADDRESS:
        s->pci_configuration_address = val;
        break;
    case PCI_CONFIGURATION_DATA:
        s->pci_configuration_data = val;
        break;
    case PCI_INTERRUPT_ACKNOWLEDGE:
        s->pci_interrupt_acknowledge = val;
        break;
    case PCI_SERRN_MASK:
        s->pci_serrn_mask = val;
        break;
    case PCI_INTERRUPT_CAUSE:
        s->pci_interrupt_cause = val;
        break;
    case PCI_INTERRUPT_MASK:
        s->pci_interrupt_mask = val;
        break;
    case PCI_ERROR_ADDRESS_LOW:
        s->pci_error_address_low = val;
        break;
    case PCI_ERROR_ADDRESS_HIGH:
        s->pci_error_address_high = val;
        break;
    case PCI_ERROR_COMMAND:
        s->pci_error_command = val;
        break;
    }
    mv88f5181l_pci_interface_update(s);
}

static const MemoryRegionOps mv88f5181l_pci_interface_ops = {
    .read = mv88f5181l_pci_interface_read,
    .write = mv88f5181l_pci_interface_write,
    .endianness = DEVICE_NATIVE_ENDIAN,
};

static void mv88f5181l_pcie_interface_update(void *opaque) {
    /* MV88F5181LState *s = opaque; */
}

static uint64_t mv88f5181l_pcie_interface_read(void *opaque, hwaddr offset, unsigned size) {
    MV88F5181LState *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
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

static void mv88f5181l_pcie_interface_write(void *opaque, hwaddr offset, uint64_t val, unsigned size) {
    MV88F5181LState *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
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
    mv88f5181l_pcie_interface_update(s);
}

static const MemoryRegionOps mv88f5181l_pcie_interface_ops = {
    .read = mv88f5181l_pcie_interface_read,
    .write = mv88f5181l_pcie_interface_write,
    .endianness = DEVICE_NATIVE_ENDIAN,
};

static void mv88f5181L_reset(DeviceState *d) {
    MV88F5181LState *s = MV88F5181L(d);
    
    s->window0_control_register = 0x1FFF5941;
    s->window0_base_register = 0x80000000;
    s->window0_remap_low_register = 0x80000000;
    s->window0_remap_high_register = 0x0;
    s->window1_control_register = 0x1FFF5931;
    s->window1_base_register = 0xA0000000;
    s->window1_remap_low_register = 0xA0000000;
    s->window1_remap_high_register = 0x0;
    s->window2_control_register = 0x00005141;
    s->window2_base_register = 0xC0000000;
    s->window2_remap_low_register = 0xC0000000;
    s->window2_remap_high_register = 0x0;
    s->window3_control_register = 0x00005131;
    s->window3_base_register = 0xC8000000;
    s->window4_control_register = 0x00000091;
    s->window4_base_register = 0xC8010000;
    s->window5_control_register = 0x0;
    s->window5_base_register = 0x0;
    s->window6_control_register = 0x07FF1B11;
    s->window6_base_register = 0xF0000000;
    s->window7_control_register = 0x07FF0F11;
    s->window7_base_register = 0xF8000000;
    s->_88f5181_internal_registers_base_address_register = 0xD0000000;
    
    s->cs0n_base_address_register = 0x0 << 0 | 0x0 << 16 | 0x0 << 24;
    s->cs0n_size_register = 0x1 << 0 | 0x0 << 1 |  0xFF << 16 | 0x0F << 24;
    s->cs1n_base_address_register = 0x0 << 0 | 0x0 << 16 | 0x10 << 24;
    s->cs1n_size_register = 0x1 << 0 | 0x0 << 1 | 0xFF << 16 | 0x0F << 24;
    s->cs2n_base_address_register = 0x0 << 0 | 0xFF << 16 | 0x20 << 24;
    s->cs2n_size_register = 0x1 << 0 | 0x0 << 1 | 0xFF << 16 | 0x0F << 24;
    s->cs3n_base_address_register = 0x0 << 0 | 0x0 << 16 | 0x30 << 24;
    s->cs3n_size_register = 0x1 << 0 | 0x0 << 1 | 0xFF << 16 | 0x0F << 24;
    s->ddr_sdram_configuration_register = 0x400 << 0 | 0x2 << 14 | 0x1 << 18 | 0x2 << 20 | 0x1 << 24 | 0x1 << 25 // 0 14 17 18 19 20 22 24 25 26;
    s->ddr_sdram_control_register = 0x1 << 6 | 0x1 << 12 | 0x1 << 18 | 0x3 << 24 // 0 6 7 12 13 14 18 19 24 28;
    s->ddr_sdram_timing_low_register = 0x0 << 0 | 0x2 << 4 | 0x2 << 8 | 0x2 << 12 | 0x1 << 16 | 0x8 << 20 | 0x1 << 24 | 0x1 << 28;
    s->ddr_sdram_timing_high_register = 0xD << 0 | 0x0 << 4 | 0x0 << 6 | 0x0 << 8 | 0x0 << 10 | 0x0 << 12;
    s->ddr2_sdram_timing_low_register = 0x5 << 0 | 0x0 << 4 | 0x3 << 8 | 0x3 << 12 | 0x6 << 16 | 0x0 << 20;
    s->ddr2_sdram_timing_high_register = 0x0 << 0 | 0x3 << 4 | 0x3 << 8 | 0x6 << 12 | 0x0 << 16;
    s->ddr_sdram_address_control_register = 0x0 << 0 | 0x1 << 4 | 0x0 << 6;
    s->ddr_sdram_open_pages_control_register = 0x0 << 0 | 0x0 << 1;
    s->ddr_sdram_operation_register = 0x0 << 0 | 0x0 << 4;
    s->ddr_sdram_operation_control_register = 0x0 << 0 | 0x0 << 2;
    s->ddr_sdram_mode_register = 0x2 << 0 | 0x0 << 3 | 0x3 << 4 | 0x0 << 7 | 0x0 << 8 | 0x0 << 12 | 0x0 << 13 | 0x0 << 14;
    s->extended_ddr_sdram_mode_register = 0x0 << 0 | 0x0 << 1 | 0x0 << 7 | 0x0 << 13 | 0x0 << 14;
    s->ddr_sdram_initialization_control_register = 0x0 << 0 | 0x0 << 1;
    s->ddr_sdram_address_or_control_pads_calibration_register = 0x0 << 0 | 0x0 << 6 | 0x0 << 12 | 0x0 << 14 | 0x1 << 16 | 0x0 << 17 | 0x0 << 23 | 0x0 << 29 | 0x0 << 31;
    s->ddr_sdram_data_pads_calibration_register = 0x144 << 0;
    s->ddr2_sdram_odt_control_low_register = 0x0 << 0 | 0x0 << 4 | 0x0 << 8 | 0x0 << 12 | 0x0 << 16 | 0x0 << 20 | 0x0 << 24 | 0x0 << 28;
    s->ddr2_sdram_odt_control_high_register = 0x0 << 0 | 0x0 << 2 | 0x0 << 4 | 0x0 << 6 | 0x0 << 8;
    s->ddr2_sdram_odt_control_register = 0x0 << 0 | 0x0 << 4 | 0x0 << 8 | 0x0 << 10 | 0x0 << 12;
    s->ddr_sdram_interface_mbus_control_low_register = 0x0 << 0 | 0x1 << 4 | 0x2 << 8 | 0x3 << 12 | 0x4 << 16 | 0x5 << 20 | 0x6 << 24 | 0x7 << 28;
    s->ddr_sdram_interface_mbus_control_high_register = 0x8 << 0 | 0x9 << 4 | 0xA << 8 | 0xB << 12 | 0xC << 16 | 0xD << 20 | 0xE << 24 | 0xF << 28;
    s->ddr_sdram_interface_mbus_timeout_register = 0xFF << 0 | 0x0 << 8 | 0x1 << 16 | 0x0 << 17;
    s->ddr_sdram_mmask_register = 0x0 << 0 | 0x0 << 2 | 0x0 << 4 | 0xF << 5 | 0x0 << 9;
    
    s->mpp_control_0_register = 0;
    s->mpp_control_1_register = 0;
    s->mpp_control_2_register = 0;
    s->device_multiplex_control_register = 0;
    s->sample_at_reset_register = 0;
    
    s->csn0_bar_size = 0x0 << 0 | 0x0FFFF << 12;
    s->csn1_bar_size = 0x0FFFF000 << 0;
    s->csn2_bar_size = 0x0FFFF000 << 0;
    s->csn3_bar_size = 0x0FFFF000 << 0;
    s->devcsn0_bar_size = 0x07FFF000 << 0;
    s->devcsn1_bar_size = 0x07FFF000 << 0;
    s->devcsn2_bar_size = 0x07FFF000 << 0;
    s->boot_csn_bar_size = 0x07FFF000 << 0;
    s->p2p_mem0_bar_size = 0x1FFFF000 << 0;
    s->p2p_i_or_o_bar_size = 0xF000 << 0;
    s->expansion_rom_bar_size = 0x0 << 0;
    s->base_address_registers_enable = 0x1 << 4 | 0x1 << 5 | 0x1 << 7 | 0x1 << 10 | 0x1 << 11 | 0x1 << 12 | 0x1 << 13 // 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 16;
    s->csn0_base_address_remap = 0x0 // 0 12;
    s->csn1_base_address_remap = 0x10000000 << 0;
    s->csn2_base_address_remap = 0x20000000 << 0;
    s->csn3_base_address_remap = 0x30000000 << 0;
    s->devcsn0_base_address_remap = 0xE0000000 << 0;
    s->devcsn1_base_address_remap = 0xE8000000 << 0;
    s->devcsn2_base_address_remap = 0xF0000000 << 0;
    s->bootcsn_base_address_remap = 0xF8000000 << 0;
    s->p2p_mem0_base_address_remap_low = 0x80000000 << 0;
    s->p2p_mem0_base_address_remap_high = 0x0 << 0;
    s->p2p_i_or_o_base_address_remap = 0xC0000000 << 0;
    s->expansion_rom_base_address_remap = 0xE0000000 << 0;
    s->dram_bar_bank_select = 0x0 << 0 | 0x1 << 2 | 0x2 << 4 | 0x3 << 6 | 0x0 << 8;
    s->pci_address_decode_control = 0x1 << 3 // 0 1 3 4 8 25;
    s->pci_dll_control = 0x1 << 1 | 0x1 << 20 // 0 1 3 5 9 13 15 16 17 20 22 31;
    s->pci_or_mpp_pads_calibration = 0xF << 0 | 0xF << 4 | 0xF << 8 | 0xF << 12 | 0x1 << 16 | 0x1 << 17 | 0x0 << 18 | 0x0 << 22 | 0x0 << 31;
    s->pci_command = 0x1 << 0 | 0x1 << 4 |  0x1 << 5 | 0x1 << 6 | 0x1 << 8 | 0x1 << 9 | 0x1 << 13 | 0x1 << 14 | 0x1 << 16 | 0x1 << 17 | 0x1 << 24 // 0 1 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 24 26 28 29;
    s->pci_mode = 0x1 << 31 // 0 2 3 4 6 8 9 31;
    s->pci_retry = 0x0 // 0 16 24;
    s->pci_discard_timer = 0x0 // 0 16;
    s->msi_trigger_timer = 0xFFFF << 0 | 0x0 << 16;
    s->pci_arbiter_control = 0x6 << 3 // 0 1 2 3 7 14 21 31;
    s->pci_p2p_configuration = 0xFF << 0 | 0x0 << 16 | 0x0 << 24 | 0x0 << 29;
    s->pci_access_control_base_0_low = 0x0 // 0 1 4 5 6 8 10 12;
    s->pci_access_control_base_0_high = 0x0 << 0;
    s->pci_access_control_size_0 = 0x0 // 0 4 5 8 19 11 12;
    s->pci_access_control_base_1_low = 0x0 << 0;
    s->pci_access_control_base_1_high = 0x0 << 0;
    s->pci_access_control_size_1 = 0x0 << 0;
    s->pci_access_control_base_2_low = 0x0 << 0;
    s->pci_access_control_base_2_high = 0x0 << 0;
    s->pci_access_control_size_2 = 0x0 << 0;
    s->pci_access_control_base_3_low = 0x0 << 0;
    s->pci_access_control_base_3_high = 0x0 << 0;
    s->pci_access_control_size_3 = 0x0 << 0;
    s->pci_access_control_base_4_low = 0x0 << 0;
    s->pci_access_control_base_4_high = 0x0 << 0;
    s->pci_access_control_size_4 = 0x0 << 0;
    s->pci_access_control_base_5_low = 0x0 << 0;
    s->pci_access_control_base_5_high = 0x0 << 0;
    s->pci_access_control_size_5 = 0x0 << 0;
    s->pci_configuration_address = 0x0 // 0 2 8 11 16 24 31;
    s->pci_configuration_data = 0x0 << 0;
    s->pci_interrupt_acknowledge = 0x0 << 0;
    s->pci_serrn_mask = 0x0 // 0 1 2 3 5 6 7 8 9 10 11 12 17 18 20 21 22;
    s->pci_interrupt_cause = 0x0 // 0 24 25 26 27;
    s->pci_interrupt_mask = 0x0 // 0 27;
    s->pci_error_address_low = 0x0 << 0;
    s->pci_error_address_high = 0x0 << 0;
    s->pci_error_command = 0x0 // 0 4 5;
    
    s->pci_express_device_and_vendor_id_register = 0x11AB << 0 | 0x5181 << 16;
    s->pci_express_command_and_status_register = 0x1 << 20 // 0 1 2 3 6 7 8 9 10 11 19 20 21 24 25 27 29 30 31;
    s->pci_express_class_code_and_revision_id_register = 0x3 << 0 | 0x80 << 16 | 0x05 << 24;
    s->pci_express_bist_header_type_and_cache_line_size_register = 0x0 // 0 8 16 24 28 30 31;
    s->pci_express_bar0_internal_register = 0x0 << 0 | 0x2 << 1 | 0x1 << 3 | 0x0 << 4 | 0xD00 << 20;
    s->pci_express_bar0_internal_high_register = 0x0 << 0;
    s->pci_express_bar1_register = 0x0 << 0 | 0x2 << 1 | 0x1 << 3 | 0x0 << 4 | 0x0 << 16;
    s->pci_express_bar1_high_register = 0x0 << 0;
    s->pci_express_bar2_register = 0x0 << 0 | 0x2 << 1 | 0x1 << 3 | 0x0 << 4 | 0xF000 << 16;
    s->pci_express_bar2_high_register = 0x0 << 0;
    s->pci_express_subsystem_device_and_vendor_id = 0x11AB << 0 | 0x11AB << 16;
    s->pci_express_expansion_rom_bar_register = 0x0 // 0 1 19 22;
    s->pci_express_capability_list_pointer_register = 0x40 << 0 | 0x0 << 8;
    s->pci_express_interrupt_pin_and_line_register = 0x0 << 0 | 0x1 << 8 | 0x0 << 16;
    s->pci_express_power_management_capability_header_register = 0x01 << 0 | 0x50 << 8 | 0x2 << 16 // 0 8 16 19 21 22 25 26 27;
    s->pci_express_power_management_control_and_status_register = 0x0 // 0 2 8 9 13 15 16 24;
    s->pci_express_msi_message_control_register = 0x5 << 0 | 0x60 << 8 | 0x1 << 23 // 0 8 16 17 20 23 24;
    s->pci_express_msi_message_address_register = 0x0 << 0 | 0x0 << 2;
    s->pci_express_msi_message_address_high_register = 0x0 << 0;
    s->pci_express_msi_message_data_register = 0x0 << 0 | 0x0 << 16;
    s->pci_express_capability_register = 0x10 << 0 | 0x1 << 16 // 0 8 16 20 24 25 30;
    s->pci_express_device_capabilities_register = 0x2 << 6 // 0 3 6 9 12 13 14 15 18 26 28;
    s->pci_express_device_control_status_register = 0x2 << 12 // 0 1 2 3 4 5 8 10 11 12 15 16 17 18 19 20 21 22;
    s->pci_express_link_capabilities_register = 0x1 << 0 | 0x0 << 4 | 0x1 << 10 | 0x0 << 12 | 0x7 << 15 | 0x0 << 18 | 0x0 << 24;
    s->pci_express_link_control_status_register = 0x1 << 3 | 0x1 << 16 | 0x1 << 28 // 0 2 3 4 5 6 7 8 16 20 26 27 28 29;
    s->pci_express_advanced_error_report_header_register = 0x1 << 0 | 0x1 << 16 | 0x0 << 20;
    s->pci_express_uncorrectable_error_status_register = 0x0 // 0 4 5 12 13 14 15 16 17 18 19 20 21;
    s->pci_express_uncorrectable_error_mask_register = 0x0 << 0;
    s->pci_express_uncorrectable_error_severity_register = 0x60010 << 0;
    s->pci_express_correctable_error_status_register = 0x0 // 0 1 6 7 8 9 12 13;
    s->pci_express_correctable_error_mask_register = 0x0 << 0;
    s->pci_express_advanced_error_capability_and_control_register = 0x0 << 0 | 0x0 << 5;
    s->pci_express_header_log_first_dword_register = 0x0 << 0;
    s->pci_express_header_log_second_dword_register = 0x0 << 0;
    s->pci_express_header_log_third_dword_register = 0x0 << 0;
    s->pci_express_header_log_fourth_dword_register = 0x0 << 0;
    s->pci_express_bar1_control_register = 0x1 << 0 | 0x0 << 1 | 0x3FFF << 16;
    s->pci_express_bar2_control_register = 0x1 << 0 | 0x0 << 1 | 0x0FFF << 16;
    s->pci_express_expansion_rom_bar_control_register = 0x0 << 0 | 0x0 << 1 | 0x0 << 19 | 0x0 << 22;
    s->pci_express_configuration_address_register = 0x0 << 0 | 0x0 << 2 | 0x0 << 8 | 0x0 << 11 | 0x0 << 16 | 0x0 << 24 | 0x0 << 28 | 0x0 << 31;
    s->pci_express_configuration_data_register = 0x0 << 0;
    s->pci_express_interrupt_cause = 0x0 << 0 // 0 1 2 3 4 5 8 9 10 11 12 13 16 17 18 19 20 21 22 23 24 25 26 27 28;
    s->pci_express_interrupt_mask = 0x0 << 0;
    s->pci_express_window0_control_register = 0x1 << 0 | 0x0 << 1 | 0x0 << 4 | 0x0E << 8 | 0x0FFF << 16;
    s->pci_express_window0_base_register = 0x0 << 0 | 0x0 << 16;
    s->pci_express_window0_remap_register = 0x0 << 0 | 0x0 << 1 | 0x0 << 16;
    s->pci_express_window1_control_register = 0x1 << 0 | 0x0 << 1 | 0x0 << 2 | 0x0 << 4 | 0x0D << 8 | 0x0FFF << 16;
    s->pci_express_window1_base_register = 0x0 << 0 | 0x1000 << 16;
    s->pci_express_window1_remap_register = 0x0 << 0 | 0x0 << 1 | 0x0 << 16;
    s->pci_express_window2_control_register = 0x0 << 0 | 0x0 << 1 | 0x0 << 2 | 0x0 << 4 | 0x0B  << 8 | 0x0FFF << 16;
    s->pci_express_window2_base_register = 0x0 << 0 | 0x2000 << 16;
    s->pci_express_window2_remap_register = 0x0 << 0 | 0x0 << 1 | 0x0 << 16;
    s->pci_express_window3_control_register = 0x0 << 0 | 0x0 << 1 | 0x0 << 2 | 0x0 << 4 | 0x07  << 8 | 0x0FFF << 16;
    s->pci_express_window3_base_register = 0x0 << 0 | 0x3000 << 16;
    s->pci_express_window3_remap_register = 0x0 << 0 | 0x0 << 1 | 0x0 << 16;
    s->pci_express_window4_control_register = 0x1 << 0 | 0x1 << 1 | 0x0 << 2 | 0x1 << 4 | 0x1B  << 8 | 0x07FF << 16;
    s->pci_express_window4_base_register = 0x0 << 0 | 0xF000 << 16;
    s->pci_express_window4_remap_register = 0x0 << 0 | 0x0 << 1 | 0x0 << 16;
    s->pci_express_window5_control_register = 0x1 << 0 | 0x1 << 1 | 0x0 << 2 | 0x1 << 4 | 0x0F << 8 | 0x07FF << 16;
    s->pci_express_window5_base_register = 0x0 << 0 | 0xF800 << 16;
    s->pci_express_window5_remap_register = 0x0 << 0 | 0x0 << 1 | 0x0 << 16;
    s->pci_express_default_window_control_register = 0x0 << 0 | 0x0 << 4 | 0x0 << 8 | 0x0 << 16;
    s->pci_express_expansion_rom_window_control_register = 0x0 << 0 | 0x1 << 4 | 0xF << 8 | 0x0 << 16;
    s->pci_express_expansion_rom_window_remap_register = 0x0 << 0 | 0x0 << 1 | 0x0 << 16;
    s->pci_express_control_register = 0x1 << 0 | 0x1 << 3 | 0x3 << 8 | 0x14 << 16 // 0 1 2 3 8 19 16 24 25 26 27 28 29;
    s->pci_express_status_register = 0x0 // 0 1 5 8 16 21 24 25 26 27 28;
    s->pci_express_completion_timeout_register = 0x2710 << 0 | 0x0 << 16;
    s->pci_express_flow_control_register = 0x0 << 0 | 0x8 << 8 | 0x0 << 16 | 0x78 << 24;
    s->pci_express_acknowledge_timers_1x_register = 0x4 << 0 | 0x320 << 16;
    s->pci_express_debug_control_register = 0x0 << 0 | 0x1 << 16 | 0x17 << 1 | 0x0 << 0 | 0x1 << 19 | 0x0 << 20;
    s->pci_express_tl_control_register = 0x0 << 0;
}

static void mv88f5181L_init(Object *obj) {
    MV88F5181LState *s = MV88F5181L(obj);

    /* initialize cpus and add the cpu as soc's child */
    s->cpu_type = ARM_CPU_TYPE_NAME("arm926");
    s->cpu = ARM_CPU(object_new(s->cpu_type));

    /* initialize cpu address map registers */
    memory_region_init_io(&s->cpu_address_map_mmio, obj,
        &mv88f5181_cpu_address_map_ops, s, TYPE_MV88F5181L, MV88F5181_CPU_ADDRESS_MAP_MMIO_SIZE);
    sysbus_init_mmio(SYS_BUS_DEVICE(s), &s->cpu_address_map_mmio);

    /* initialize ddr sdram controller registers */
    memory_region_init_io(&s->ddr_sdram_controller_mmio, obj,
        &mv88f5181_ddr_sdram_controller_ops, s, TYPE_MV88F5181L, MV88F5181_DDR_SDRAM_CONTROLLER_MMIO_SIZE);
    sysbus_init_mmio(SYS_BUS_DEVICE(s), &s->ddr_sdram_controller_mmio);

    /* initialize pins multiplexing interface registers */
    memory_region_init_io(&s->pins_multiplexing_interface_mmio, obj,
        &mv88f5181l_pins_multiplexing_interface_ops, s, TYPE_MV88F5181L, MV88F5181L_PINS_MULTIPLEXING_INTERFACE_MMIO_SIZE);
    sysbus_init_mmio(SYS_BUS_DEVICE(s), &s->pins_multiplexing_interface_mmio);

    /* initialize pci interface registers */
    memory_region_init_io(&s->pci_interface_mmio, obj,
        &mv88f5181l_pci_interface_ops, s, TYPE_MV88F5181L, MV88F5181L_PCI_INTERFACE_MMIO_SIZE);
    sysbus_init_mmio(SYS_BUS_DEVICE(s), &s->pci_interface_mmio);

    /* initialize pcie interface registers */
    memory_region_init_io(&s->pcie_interface_mmio, obj,
        &mv88f5181l_pcie_interface_ops, s, TYPE_MV88F5181L, MV88F5181L_PCIE_INTERFACE_MMIO_SIZE);
    sysbus_init_mmio(SYS_BUS_DEVICE(s), &s->pcie_interface_mmio);

    /* initialize the interrupt controller and add the ic as soc and sysbus's child*/
    sysbus_init_child_obj(
        obj, "ic", &s->ic, sizeof(s->ic), TYPE_MV88F5181L_IC);

    /* initialize peripherals and add the peripherals as soc and sysbus's child */
    sysbus_init_child_obj(
        obj, "peripherals", &s->peripherals, sizeof(s->peripherals), TYPE_MV88F5181L_PERIPHERALS);
}

static void mv88f5181L_realize(DeviceState *dev, Error **errp) {
    MV88F5181LState *s = MV88F5181L(dev);
    Error *err = NULL;

    /* realize the peripherals  */
    object_property_set_bool(OBJECT(&s->peripherals), true, "realized", &err);
    if (err) {
        error_propagate(errp, err);
        return;
    }

    /* map peripheral's mmio */
    sysbus_mmio_map(SYS_BUS_DEVICE(&s->peripherals), 0, MV88F5181_BRIDGE_RAM_BASE);

    /* realize the local interrupt controller */
    object_property_set_bool(OBJECT(&s->ic), true, "realized", &err);
    if (err) {
        error_propagate(errp, err);
        return;
    }

    /* map ic's mmio */
    sysbus_mmio_map(SYS_BUS_DEVICE(&s->ic), 0, MV88F5181L_IC_RAM_BASE);

    /* realize the cpu */
    object_property_set_bool(OBJECT(s->cpu), true, "realized", &err);
    if (err) {
        error_propagate(errp, err);
        return;
    }

    /* connect irq from the peripheral to the interrupt controller */
    sysbus_connect_irq(SYS_BUS_DEVICE(&s->peripherals), 0,
        qdev_get_gpio_in_named(DEVICE(&s->ic), MV88F5181L_IC_IRQ, 0));

    /* connect irq from the gpio to the interrupt controller */
    sysbus_connect_irq(SYS_BUS_DEVICE(&s->peripherals.gpio), 0,
        qdev_get_gpio_in_named(DEVICE(&s->ic), MV88F5181L_IC_IRQ, 6));
    sysbus_connect_irq(SYS_BUS_DEVICE(&s->peripherals.gpio), 1,
        qdev_get_gpio_in_named(DEVICE(&s->ic), MV88F5181L_IC_IRQ, 7));
    sysbus_connect_irq(SYS_BUS_DEVICE(&s->peripherals.gpio), 2,
        qdev_get_gpio_in_named(DEVICE(&s->ic), MV88F5181L_IC_IRQ, 8));
    sysbus_connect_irq(SYS_BUS_DEVICE(&s->peripherals.gpio), 3,
        qdev_get_gpio_in_named(DEVICE(&s->ic), MV88F5181L_IC_IRQ, 9));

    /* connect irq/fiq outputs from the interrupt controller to the cpu */
    qdev_connect_gpio_out_named(DEVICE(&s->ic), "irq", 0,
            qdev_get_gpio_in(DEVICE(s->cpu), ARM_CPU_IRQ));
}


static void mv88f5181L_class_init(ObjectClass *oc, void *data) {
    DeviceClass *dc = DEVICE_CLASS(oc);

    /* dc->fw_name = ; */
    /* dc->desc = ; */
    /* dc->props = ; */
    /* dc->user_creatable = ; */
    /* dc->hotpluggable = ; */
    dc->reset = mv88f5181L_reset;
    dc->realize = mv88f5181L_realize;
    /* dc->unrealize = ; */
    /* dc->vmsd = ; */
    /* dc->bus_type = ; */

    /* SysBusDeviceClass sbc = SYS_BUS_DEVICE_CLASS(klass); */

    /* sbc->explicit_ofw_unit_address = ; */
    /* sbc->connect_irq_notifier = ; */
}

static const TypeInfo mv88f5181L_type_info = {
    .name = TYPE_MV88F5181L,
    .parent = TYPE_SYS_BUS_DEVICE,
    .instance_size = sizeof(MV88F5181LState),
    .instance_init = mv88f5181L_init,
    /* .class_size = sizeof(SysBusDeviceClass), */
    .class_init = mv88f5181L_class_init,
};

static void mv88f5181L_register_types(void) {
    type_register_static(&mv88f5181L_type_info);
}

type_init(mv88f5181L_register_types);