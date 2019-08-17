/* 
 * automatically generated, don't change
 */

#include "qemu/osdep.h"
#include "qemu/log.h"
#include "qapi/error.h"
#include "target/arm/cpu.h"
#include "hw/arm/mv88f5181l.h"
#include "hw/char/serial.h"
#include "exec/address-spaces.h"

static void mv88f5181l_gpio_update(void *opaque);
static uint64_t mv88f5181l_gpio_read(void *opaque, hwaddr offset, unsigned size);
static void mv88f5181l_gpio_write(void *opaque, hwaddr offset, uint64_t val, unsigned size);
static void mv88f5181l_cpu_address_map_update(void *opaque);
static uint64_t mv88f5181l_cpu_address_map_read(void *opaque, hwaddr offset, unsigned size);
static void mv88f5181l_cpu_address_map_write(void *opaque, hwaddr offset, uint64_t val, unsigned size);
static void mv88f5181l_ddr_sdram_controller_update(void *opaque);
static uint64_t mv88f5181l_ddr_sdram_controller_read(void *opaque, hwaddr offset, unsigned size);
static void mv88f5181l_ddr_sdram_controller_write(void *opaque, hwaddr offset, uint64_t val, unsigned size);
static void mv88f5181l_pins_multiplexing_interface_update(void *opaque);
static uint64_t mv88f5181l_pins_multiplexing_interface_read(void *opaque, hwaddr offset, unsigned size);
static void mv88f5181l_pins_multiplexing_interface_write(void *opaque, hwaddr offset, uint64_t val, unsigned size);
static void mv88f5181l_pci_interface_update(void *opaque);
static uint64_t mv88f5181l_pci_interface_read(void *opaque, hwaddr offset, unsigned size);
static void mv88f5181l_pci_interface_write(void *opaque, hwaddr offset, uint64_t val, unsigned size);
static void mv88f5181l_pcie_interface_update(void *opaque);
static uint64_t mv88f5181l_pcie_interface_read(void *opaque, hwaddr offset, unsigned size);
static void mv88f5181l_pcie_interface_write(void *opaque, hwaddr offset, uint64_t val, unsigned size);
static void mv88f5181l_usb_2_0_controller_update(void *opaque);
static uint64_t mv88f5181l_usb_2_0_controller_read(void *opaque, hwaddr offset, unsigned size);
static void mv88f5181l_usb_2_0_controller_write(void *opaque, hwaddr offset, uint64_t val, unsigned size);
static void mv88f5181l_gigabit_ethernet_controller_update(void *opaque);
static uint64_t mv88f5181l_gigabit_ethernet_controller_read(void *opaque, hwaddr offset, unsigned size);
static void mv88f5181l_gigabit_ethernet_controller_write(void *opaque, hwaddr offset, uint64_t val, unsigned size);
static void mv88f5181l_cesa_update(void *opaque);
static uint64_t mv88f5181l_cesa_read(void *opaque, hwaddr offset, unsigned size);
static void mv88f5181l_cesa_write(void *opaque, hwaddr offset, uint64_t val, unsigned size);

static void mv88f5181l_init(Object *obj);
static void mv88f5181l_realize(DeviceState *dev, Error **errp);
static void mv88f5181l_reset(DeviceState *d);

static void mv88f5181l_class_init(ObjectClass *oc, void *data);
static void mv88f5181l_register_types(void);

static void mv88f5181l_gpio_update(void *opaque) {
    /* MV88F5181LState *s = opaque; */
}

static uint64_t mv88f5181l_gpio_read(void *opaque, hwaddr offset, unsigned size) {
    MV88F5181LState *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case GPIO_DATA_OUT_REGISTER:
        res = s->gpio_data_out_register;
        break;
    case GPIO_DATA_OUT_ENABLE_CONTROL_REGISTER:
        res = s->gpio_data_out_enable_control_register;
        break;
    case GPIO_BLINK_ENABLE_REGISTER:
        res = s->gpio_blink_enable_register;
        break;
    case GPIO_DATA_IN_POLARITY_REGISTER:
        res = s->gpio_data_in_polarity_register;
        break;
    case GPIO_DATA_IN_REGISTER:
        res = s->gpio_data_in_register;
        break;
    case GPIO_INTERRUPT_CAUSE_REGISTER:
        res = s->gpio_interrupt_cause_register;
        break;
    case GPIO_INTERRUPT_MASK_REGISTER:
        res = s->gpio_interrupt_mask_register;
        break;
    case GPIO_INTERRUPT_LEVEL_MASK_REGISTER:
        res = s->gpio_interrupt_level_mask_register;
        break;
    }
    return res;
}

static void mv88f5181l_gpio_write(void *opaque, hwaddr offset, uint64_t val, unsigned size) {
    MV88F5181LState *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case GPIO_DATA_OUT_REGISTER:
        s->gpio_data_out_register = val;
        break;
    case GPIO_DATA_OUT_ENABLE_CONTROL_REGISTER:
        s->gpio_data_out_enable_control_register = val;
        break;
    case GPIO_BLINK_ENABLE_REGISTER:
        s->gpio_blink_enable_register = val;
        break;
    case GPIO_DATA_IN_POLARITY_REGISTER:
        s->gpio_data_in_polarity_register = val;
        break;
    case GPIO_DATA_IN_REGISTER:
        s->gpio_data_in_register = val;
        break;
    case GPIO_INTERRUPT_CAUSE_REGISTER:
        s->gpio_interrupt_cause_register = val;
        break;
    case GPIO_INTERRUPT_MASK_REGISTER:
        s->gpio_interrupt_mask_register = val;
        break;
    case GPIO_INTERRUPT_LEVEL_MASK_REGISTER:
        s->gpio_interrupt_level_mask_register = val;
        break;
    }
    mv88f5181l_gpio_update(s);
}

static const MemoryRegionOps mv88f5181l_gpio_ops = {
    .read = mv88f5181l_gpio_read,
    .write = mv88f5181l_gpio_write,
    .endianness = DEVICE_NATIVE_ENDIAN,
};

static void mv88f5181l_cpu_address_map_update(void *opaque) {
    /* MV88F5181LState *s = opaque; */
}

static uint64_t mv88f5181l_cpu_address_map_read(void *opaque, hwaddr offset, unsigned size) {
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

static void mv88f5181l_cpu_address_map_write(void *opaque, hwaddr offset, uint64_t val, unsigned size) {
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
    mv88f5181l_cpu_address_map_update(s);
}

static const MemoryRegionOps mv88f5181l_cpu_address_map_ops = {
    .read = mv88f5181l_cpu_address_map_read,
    .write = mv88f5181l_cpu_address_map_write,
    .endianness = DEVICE_NATIVE_ENDIAN,
};

static void mv88f5181l_ddr_sdram_controller_update(void *opaque) {
    /* MV88F5181LState *s = opaque; */
}

static uint64_t mv88f5181l_ddr_sdram_controller_read(void *opaque, hwaddr offset, unsigned size) {
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

static void mv88f5181l_ddr_sdram_controller_write(void *opaque, hwaddr offset, uint64_t val, unsigned size) {
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
    mv88f5181l_ddr_sdram_controller_update(s);
}

static const MemoryRegionOps mv88f5181l_ddr_sdram_controller_ops = {
    .read = mv88f5181l_ddr_sdram_controller_read,
    .write = mv88f5181l_ddr_sdram_controller_write,
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

static void mv88f5181l_usb_2_0_controller_update(void *opaque) {
    /* MV88F5181LState *s = opaque; */
}

static uint64_t mv88f5181l_usb_2_0_controller_read(void *opaque, hwaddr offset, unsigned size) {
    MV88F5181LState *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case PORT0_USB_2_0_ID:
        res = s->port0_usb_2_0_id;
        break;
    case PORT0_USB_2_0_HWGENERAL:
        res = s->port0_usb_2_0_hwgeneral;
        break;
    case PORT0_USB_2_0_HWHOST:
        res = s->port0_usb_2_0_hwhost;
        break;
    case PORT0_USB_2_0_HWDEVICE:
        res = s->port0_usb_2_0_hwdevice;
        break;
    case PORT0_USB_2_0_HWTXBUF:
        res = s->port0_usb_2_0_hwtxbuf;
        break;
    case PORT0_USB_2_0_HWRXBUF:
        res = s->port0_usb_2_0_hwrxbuf;
        break;
    case PORT0_USB_2_0_HWTTTXBUF:
        res = s->port0_usb_2_0_hwtttxbuf;
        break;
    case PORT0_USB_2_0_HWTTRXBUF:
        res = s->port0_usb_2_0_hwttrxbuf;
        break;
    case PORT0_USB_2_0_CAPLENGTH:
        res = s->port0_usb_2_0_caplength;
        break;
    case PORT0_USB_2_0_HCIVERSION:
        res = s->port0_usb_2_0_hciversion;
        break;
    case PORT0_USB_2_0_HCSPARAMS:
        res = s->port0_usb_2_0_hcsparams;
        break;
    case PORT0_USB_2_0_HCCPARAMS:
        res = s->port0_usb_2_0_hccparams;
        break;
    case PORT0_USB_2_0_DCIVERSION:
        res = s->port0_usb_2_0_dciversion;
        break;
    case PORT0_USB_2_0_DCCPARAMS:
        res = s->port0_usb_2_0_dccparams;
        break;
    case PORT0_USB_2_0_USBCMD:
        res = s->port0_usb_2_0_usbcmd;
        break;
    case PORT0_USB_2_0_USBSTS:
        res = s->port0_usb_2_0_usbsts;
        break;
    case PORT0_USB_2_0_USBINTR:
        res = s->port0_usb_2_0_usbintr;
        break;
    case PORT0_USB_2_0_FRINDEX:
        res = s->port0_usb_2_0_frindex;
        break;
    case PORT0_USB_2_0_PERIODICLISTBASE__OR__DEVICE_ADDR:
        res = s->port0_usb_2_0_periodiclistbase__or__device_addr;
        break;
    case PORT0_USB_2_0_ASYNCLISTADDR__OR__ENDPOINTLIST_ADDR:
        res = s->port0_usb_2_0_asynclistaddr__or__endpointlist_addr;
        break;
    case PORT0_USB_2_0_TTCTRL:
        res = s->port0_usb_2_0_ttctrl;
        break;
    case PORT0_USB_2_0_BURSTSIZE:
        res = s->port0_usb_2_0_burstsize;
        break;
    case PORT0_USB_2_0_TXFILLTUNING:
        res = s->port0_usb_2_0_txfilltuning;
        break;
    case PORT0_USB_2_0_TXTTFILLTUNING:
        res = s->port0_usb_2_0_txttfilltuning;
        break;
    case PORT0_USB_2_0_CONFIGFLAG:
        res = s->port0_usb_2_0_configflag;
        break;
    case PORT0_USB_2_0_PORTSC1:
        res = s->port0_usb_2_0_portsc1;
        break;
    case PORT0_USB_2_0_OTGSC:
        res = s->port0_usb_2_0_otgsc;
        break;
    case PORT0_USB_2_0_USBMODE:
        res = s->port0_usb_2_0_usbmode;
        break;
    case PORT0_USB_2_0_ENPDTSETUPSTAT:
        res = s->port0_usb_2_0_enpdtsetupstat;
        break;
    case PORT0_USB_2_0_ENDPTPRIME:
        res = s->port0_usb_2_0_endptprime;
        break;
    case PORT0_USB_2_0_ENDPTFLUSH:
        res = s->port0_usb_2_0_endptflush;
        break;
    case PORT0_USB_2_0_ENDPTSTATUS:
        res = s->port0_usb_2_0_endptstatus;
        break;
    case PORT0_USB_2_0_ENDPTCOMPLETE:
        res = s->port0_usb_2_0_endptcomplete;
        break;
    case PORT0_USB_2_0_ENDPTCTRL0:
        res = s->port0_usb_2_0_endptctrl0;
        break;
    case PORT0_USB_2_0_ENDPTCTRL1:
        res = s->port0_usb_2_0_endptctrl1;
        break;
    case PORT0_USB_2_0_ENDPTCTRL2:
        res = s->port0_usb_2_0_endptctrl2;
        break;
    case PORT0_USB_2_0_ENDPTCTRL3:
        res = s->port0_usb_2_0_endptctrl3;
        break;
    case PORT0_USB_2_0_BRIDGE_CONTROL_REGISTER:
        res = s->port0_usb_2_0_bridge_control_register;
        break;
    case PORT0_USB_2_0_BRIDGE_INTERRUPT_CAUSE_REGISTER:
        res = s->port0_usb_2_0_bridge_interrupt_cause_register;
        break;
    case PORT0_USB_2_0_BRIDGE_INTERRUPT_MASK_REGISTER:
        res = s->port0_usb_2_0_bridge_interrupt_mask_register;
        break;
    case PORT0_USB_2_0_BRIDGE_ERROR_ADDRESS_REGISTER:
        res = s->port0_usb_2_0_bridge_error_address_register;
        break;
    case PORT0_USB_2_0_WINDOW0_CONTROL_REGISTER:
        res = s->port0_usb_2_0_window0_control_register;
        break;
    case PORT0_USB_2_0_WINDOW0_BASE_REGISTER:
        res = s->port0_usb_2_0_window0_base_register;
        break;
    case PORT0_USB_2_0_WINDOW1_CONTROL_REGISTER:
        res = s->port0_usb_2_0_window1_control_register;
        break;
    case PORT0_USB_2_0_WINDOW1_BASE_REGISTER:
        res = s->port0_usb_2_0_window1_base_register;
        break;
    case PORT0_USB_2_0_WINDOW2_CONTROL_REGISTER:
        res = s->port0_usb_2_0_window2_control_register;
        break;
    case PORT0_USB_2_0_WINDOW2_BASE_REGISTER:
        res = s->port0_usb_2_0_window2_base_register;
        break;
    case PORT0_USB_2_0_WINDOW3_CONTROL_REGISTER:
        res = s->port0_usb_2_0_window3_control_register;
        break;
    case PORT0_USB_2_0_WINDOW3_BASE_REGISTER:
        res = s->port0_usb_2_0_window3_base_register;
        break;
    case PORT0_USB_2_0_POWER_CONTROL_REGISTER:
        res = s->port0_usb_2_0_power_control_register;
        break;
    }
    return res;
}

static void mv88f5181l_usb_2_0_controller_write(void *opaque, hwaddr offset, uint64_t val, unsigned size) {
    MV88F5181LState *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case PORT0_USB_2_0_ID:
        s->port0_usb_2_0_id = val;
        break;
    case PORT0_USB_2_0_HWGENERAL:
        s->port0_usb_2_0_hwgeneral = val;
        break;
    case PORT0_USB_2_0_HWHOST:
        s->port0_usb_2_0_hwhost = val;
        break;
    case PORT0_USB_2_0_HWDEVICE:
        s->port0_usb_2_0_hwdevice = val;
        break;
    case PORT0_USB_2_0_HWTXBUF:
        s->port0_usb_2_0_hwtxbuf = val;
        break;
    case PORT0_USB_2_0_HWRXBUF:
        s->port0_usb_2_0_hwrxbuf = val;
        break;
    case PORT0_USB_2_0_HWTTTXBUF:
        s->port0_usb_2_0_hwtttxbuf = val;
        break;
    case PORT0_USB_2_0_HWTTRXBUF:
        s->port0_usb_2_0_hwttrxbuf = val;
        break;
    case PORT0_USB_2_0_CAPLENGTH:
        s->port0_usb_2_0_caplength = val;
        break;
    case PORT0_USB_2_0_HCIVERSION:
        s->port0_usb_2_0_hciversion = val;
        break;
    case PORT0_USB_2_0_HCSPARAMS:
        s->port0_usb_2_0_hcsparams = val;
        break;
    case PORT0_USB_2_0_HCCPARAMS:
        s->port0_usb_2_0_hccparams = val;
        break;
    case PORT0_USB_2_0_DCIVERSION:
        s->port0_usb_2_0_dciversion = val;
        break;
    case PORT0_USB_2_0_DCCPARAMS:
        s->port0_usb_2_0_dccparams = val;
        break;
    case PORT0_USB_2_0_USBCMD:
        s->port0_usb_2_0_usbcmd = val;
        break;
    case PORT0_USB_2_0_USBSTS:
        s->port0_usb_2_0_usbsts = val;
        break;
    case PORT0_USB_2_0_USBINTR:
        s->port0_usb_2_0_usbintr = val;
        break;
    case PORT0_USB_2_0_FRINDEX:
        s->port0_usb_2_0_frindex = val;
        break;
    case PORT0_USB_2_0_PERIODICLISTBASE__OR__DEVICE_ADDR:
        s->port0_usb_2_0_periodiclistbase__or__device_addr = val;
        break;
    case PORT0_USB_2_0_ASYNCLISTADDR__OR__ENDPOINTLIST_ADDR:
        s->port0_usb_2_0_asynclistaddr__or__endpointlist_addr = val;
        break;
    case PORT0_USB_2_0_TTCTRL:
        s->port0_usb_2_0_ttctrl = val;
        break;
    case PORT0_USB_2_0_BURSTSIZE:
        s->port0_usb_2_0_burstsize = val;
        break;
    case PORT0_USB_2_0_TXFILLTUNING:
        s->port0_usb_2_0_txfilltuning = val;
        break;
    case PORT0_USB_2_0_TXTTFILLTUNING:
        s->port0_usb_2_0_txttfilltuning = val;
        break;
    case PORT0_USB_2_0_CONFIGFLAG:
        s->port0_usb_2_0_configflag = val;
        break;
    case PORT0_USB_2_0_PORTSC1:
        s->port0_usb_2_0_portsc1 = val;
        break;
    case PORT0_USB_2_0_OTGSC:
        s->port0_usb_2_0_otgsc = val;
        break;
    case PORT0_USB_2_0_USBMODE:
        s->port0_usb_2_0_usbmode = val;
        break;
    case PORT0_USB_2_0_ENPDTSETUPSTAT:
        s->port0_usb_2_0_enpdtsetupstat = val;
        break;
    case PORT0_USB_2_0_ENDPTPRIME:
        s->port0_usb_2_0_endptprime = val;
        break;
    case PORT0_USB_2_0_ENDPTFLUSH:
        s->port0_usb_2_0_endptflush = val;
        break;
    case PORT0_USB_2_0_ENDPTSTATUS:
        s->port0_usb_2_0_endptstatus = val;
        break;
    case PORT0_USB_2_0_ENDPTCOMPLETE:
        s->port0_usb_2_0_endptcomplete = val;
        break;
    case PORT0_USB_2_0_ENDPTCTRL0:
        s->port0_usb_2_0_endptctrl0 = val;
        break;
    case PORT0_USB_2_0_ENDPTCTRL1:
        s->port0_usb_2_0_endptctrl1 = val;
        break;
    case PORT0_USB_2_0_ENDPTCTRL2:
        s->port0_usb_2_0_endptctrl2 = val;
        break;
    case PORT0_USB_2_0_ENDPTCTRL3:
        s->port0_usb_2_0_endptctrl3 = val;
        break;
    case PORT0_USB_2_0_BRIDGE_CONTROL_REGISTER:
        s->port0_usb_2_0_bridge_control_register = val;
        break;
    case PORT0_USB_2_0_BRIDGE_INTERRUPT_CAUSE_REGISTER:
        s->port0_usb_2_0_bridge_interrupt_cause_register = val;
        break;
    case PORT0_USB_2_0_BRIDGE_INTERRUPT_MASK_REGISTER:
        s->port0_usb_2_0_bridge_interrupt_mask_register = val;
        break;
    case PORT0_USB_2_0_BRIDGE_ERROR_ADDRESS_REGISTER:
        s->port0_usb_2_0_bridge_error_address_register = val;
        break;
    case PORT0_USB_2_0_WINDOW0_CONTROL_REGISTER:
        s->port0_usb_2_0_window0_control_register = val;
        break;
    case PORT0_USB_2_0_WINDOW0_BASE_REGISTER:
        s->port0_usb_2_0_window0_base_register = val;
        break;
    case PORT0_USB_2_0_WINDOW1_CONTROL_REGISTER:
        s->port0_usb_2_0_window1_control_register = val;
        break;
    case PORT0_USB_2_0_WINDOW1_BASE_REGISTER:
        s->port0_usb_2_0_window1_base_register = val;
        break;
    case PORT0_USB_2_0_WINDOW2_CONTROL_REGISTER:
        s->port0_usb_2_0_window2_control_register = val;
        break;
    case PORT0_USB_2_0_WINDOW2_BASE_REGISTER:
        s->port0_usb_2_0_window2_base_register = val;
        break;
    case PORT0_USB_2_0_WINDOW3_CONTROL_REGISTER:
        s->port0_usb_2_0_window3_control_register = val;
        break;
    case PORT0_USB_2_0_WINDOW3_BASE_REGISTER:
        s->port0_usb_2_0_window3_base_register = val;
        break;
    case PORT0_USB_2_0_POWER_CONTROL_REGISTER:
        s->port0_usb_2_0_power_control_register = val;
        break;
    }
    mv88f5181l_usb_2_0_controller_update(s);
}

static const MemoryRegionOps mv88f5181l_usb_2_0_controller_ops = {
    .read = mv88f5181l_usb_2_0_controller_read,
    .write = mv88f5181l_usb_2_0_controller_write,
    .endianness = DEVICE_NATIVE_ENDIAN,
};

static void mv88f5181l_gigabit_ethernet_controller_update(void *opaque) {
    /* MV88F5181LState *s = opaque; */
}

static uint64_t mv88f5181l_gigabit_ethernet_controller_read(void *opaque, hwaddr offset, unsigned size) {
    MV88F5181LState *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case PHY_ADDRESS:
        res = s->phy_address;
        break;
    case SMI:
        res = s->smi;
        break;
    case ETHERNET_UNIT_DEFAULT_ADDRESS_EUDA:
        res = s->ethernet_unit_default_address_euda;
        break;
    case ETHERNET_UNIT_DEFAULT_ID_EUDID:
        res = s->ethernet_unit_default_id_eudid;
        break;
    case ETHERNET_UNIT_RESERVED_EU:
        res = s->ethernet_unit_reserved_eu;
        break;
    case ETHERNET_UNIT_INTERRUPT_CAUSE_EUIC:
        res = s->ethernet_unit_interrupt_cause_euic;
        break;
    case ETHERNET_UNIT_INTERRUPT_MASK_EUIM:
        res = s->ethernet_unit_interrupt_mask_euim;
        break;
    case ETHERNET_UNIT_ERROR_ADDRESS_EUEA:
        res = s->ethernet_unit_error_address_euea;
        break;
    case ETHERNET_UNIT_INTERNAL_ADDRESS_ERROR_EUIAE:
        res = s->ethernet_unit_internal_address_error_euiae;
        break;
    case ETHERNET_UNIT_PORT_PADS_CALIBRATION_EUPCR:
        res = s->ethernet_unit_port_pads_calibration_eupcr;
        break;
    case ETHERNET_UNIT_CONTROL_EUC:
        res = s->ethernet_unit_control_euc;
        break;
    case BASE_ADDRESS_0_BA0:
        res = s->base_address_0_ba0;
        break;
    case SIZE_S_0_SR0:
        res = s->size_s_0_sr0;
        break;
    case BASE_ADDRESS_1_BA1:
        res = s->base_address_1_ba1;
        break;
    case SIZE_S_1_SR1:
        res = s->size_s_1_sr1;
        break;
    case BASE_ADDRESS_2_BA2:
        res = s->base_address_2_ba2;
        break;
    case SIZE_S_2_SR2:
        res = s->size_s_2_sr2;
        break;
    case BASE_ADDRESS_3_BA3:
        res = s->base_address_3_ba3;
        break;
    case SIZE_S_3_SR3:
        res = s->size_s_3_sr3;
        break;
    case BASE_ADDRESS_4_BA4:
        res = s->base_address_4_ba4;
        break;
    case SIZE_S_4_SR4:
        res = s->size_s_4_sr4;
        break;
    case BASE_ADDRESS_5_BA5:
        res = s->base_address_5_ba5;
        break;
    case SIZE_S_5_SR5:
        res = s->size_s_5_sr5;
        break;
    case HIGH_ADDRESS_REMAP_HA_HARR0:
        res = s->high_address_remap_ha_harr0;
        break;
    case HIGH_ADDRESS_REMAP_HA_HARR1:
        res = s->high_address_remap_ha_harr1;
        break;
    case HIGH_ADDRESS_REMAP_HA_HARR2:
        res = s->high_address_remap_ha_harr2;
        break;
    case HIGH_ADDRESS_REMAP_HA_HARR3:
        res = s->high_address_remap_ha_harr3;
        break;
    case BASE_ADDRESS_ENABLE_BARE:
        res = s->base_address_enable_bare;
        break;
    case ETHERNET_PORT_ACCESS_PROTECT_EPAP:
        res = s->ethernet_port_access_protect_epap;
        break;
    case PORT_CONFIGURATION_GEC:
        res = s->port_configuration_gec;
        break;
    case PORT_CONFIGURATION_EXTEND_GECX:
        res = s->port_configuration_extend_gecx;
        break;
    case MII_SERIAL_PARAMETERS:
        res = s->mii_serial_parameters;
        break;
    case GMII_SERIAL_PARAMETERS:
        res = s->gmii_serial_parameters;
        break;
    case VLAN_ETHERTYPE_EVLANE:
        res = s->vlan_ethertype_evlane;
        break;
    case MAC_ADDRESS_LOW_MACAL:
        res = s->mac_address_low_macal;
        break;
    case MAC_ADDRESS_HIGH_MACAH:
        res = s->mac_address_high_macah;
        break;
    case SDMA_CONFIGURATION_SDC:
        res = s->sdma_configuration_sdc;
        break;
    case IP_DIFFERENTIATED_SERVICES_CODEPOINT_0_TO_PRIORITY_DSCP0:
        res = s->ip_differentiated_services_codepoint_0_to_priority_dscp0;
        break;
    case IP_DIFFERENTIATED_SERVICES_CODEPOINT_1_TO_PRIORITY_DSCP1:
        res = s->ip_differentiated_services_codepoint_1_to_priority_dscp1;
        break;
    case IP_DIFFERENTIATED_SERVICES_CODEPOINT_2_TO_PRIORITY_DSCP2:
        res = s->ip_differentiated_services_codepoint_2_to_priority_dscp2;
        break;
    case IP_DIFFERENTIATED_SERVICES_CODEPOINT_23_TO_PRIORITY_DSCP3:
        res = s->ip_differentiated_services_codepoint_23_to_priority_dscp3;
        break;
    case IP_DIFFERENTIATED_SERVICES_CODEPOINT_24_TO_PRIORITY_DSCP4:
        res = s->ip_differentiated_services_codepoint_24_to_priority_dscp4;
        break;
    case IP_DIFFERENTIATED_SERVICES_CODEPOINT_25_TO_PRIORITY_DSCP5:
        res = s->ip_differentiated_services_codepoint_25_to_priority_dscp5;
        break;
    case IP_DIFFERENTIATED_SERVICES_CODEPOINT_6_TO_PRIORITY_DSCP6:
        res = s->ip_differentiated_services_codepoint_6_to_priority_dscp6;
        break;
    case PORT_SERIAL_CONTROL_PSC:
        res = s->port_serial_control_psc;
        break;
    case VLAN_PRIORITY_TAG_TO_PRIORITY_VPT2P:
        res = s->vlan_priority_tag_to_priority_vpt2p;
        break;
    case ETHERNET_PORT_STATUS_PS:
        res = s->ethernet_port_status_ps;
        break;
    case TRANSMIT_QUEUE_COMMAND_TQC:
        res = s->transmit_queue_command_tqc;
        break;
    case MAXIMUM_TRANSMIT_UNIT_MTU:
        res = s->maximum_transmit_unit_mtu;
        break;
    case PORT_INTERRUPT_CAUSE_IC:
        res = s->port_interrupt_cause_ic;
        break;
    case PORT_INTERRUPT_CAUSE_EXTEND_ICE:
        res = s->port_interrupt_cause_extend_ice;
        break;
    case PORT_INTERRUPT_MASK_PIM:
        res = s->port_interrupt_mask_pim;
        break;
    case PORT_EXTEND_INTERRUPT_MASK_PEIM:
        res = s->port_extend_interrupt_mask_peim;
        break;
    case PORT_RX_FIFO_URGENT_THRESHOLD_PRFUT:
        res = s->port_rx_fifo_urgent_threshold_prfut;
        break;
    case PORT_TX_FIFO_URGENT_THRESHOLD_PTFUT:
        res = s->port_tx_fifo_urgent_threshold_ptfut;
        break;
    case PORT_RX_MINIMAL_FRAME_SIZE_PMFS:
        res = s->port_rx_minimal_frame_size_pmfs;
        break;
    case PORT_RX_DISCARD_FRAME_COUNTER_GEDFC:
        res = s->port_rx_discard_frame_counter_gedfc;
        break;
    case PORT_OVERRUN_FRAME_COUNTER_POFC:
        res = s->port_overrun_frame_counter_pofc;
        break;
    case PORT_INTERNAL_ADDRESS_ERROR_EUIAE:
        res = s->port_internal_address_error_euiae;
        break;
    case ETHERNET_CURRENT_RECEIVE_DESCRIPTOR_POINTERS_CRDP_Q0:
        res = s->ethernet_current_receive_descriptor_pointers_crdp_q0;
        break;
    case ETHERNET_CURRENT_RECEIVE_DESCRIPTOR_POINTERS_CRDP_Q1:
        res = s->ethernet_current_receive_descriptor_pointers_crdp_q1;
        break;
    case ETHERNET_CURRENT_RECEIVE_DESCRIPTOR_POINTERS_CRDP_Q2:
        res = s->ethernet_current_receive_descriptor_pointers_crdp_q2;
        break;
    case ETHERNET_CURRENT_RECEIVE_DESCRIPTOR_POINTERS_CRDP_Q3:
        res = s->ethernet_current_receive_descriptor_pointers_crdp_q3;
        break;
    case ETHERNET_CURRENT_RECEIVE_DESCRIPTOR_POINTERS_CRDP_Q4:
        res = s->ethernet_current_receive_descriptor_pointers_crdp_q4;
        break;
    case ETHERNET_CURRENT_RECEIVE_DESCRIPTOR_POINTERS_CRDP_Q5:
        res = s->ethernet_current_receive_descriptor_pointers_crdp_q5;
        break;
    case ETHERNET_CURRENT_RECEIVE_DESCRIPTOR_POINTERS_CRDP_Q6:
        res = s->ethernet_current_receive_descriptor_pointers_crdp_q6;
        break;
    case ETHERNET_CURRENT_RECEIVE_DESCRIPTOR_POINTERS_CRDP_Q7:
        res = s->ethernet_current_receive_descriptor_pointers_crdp_q7;
        break;
    case RECEIVE_QUEUE_COMMAND_RQC:
        res = s->receive_queue_command_rqc;
        break;
    case TRANSMIT_CURRENT_SERVED_DESCRIPTOR_POINTER:
        res = s->transmit_current_served_descriptor_pointer;
        break;
    case TRANSMIT_CURRENT_QUEUE_DESCRIPTOR_POINTER_TCQDP_Q0:
        res = s->transmit_current_queue_descriptor_pointer_tcqdp_q0;
        break;
    case TRANSMIT_QUEUE_TOKEN_BUCKET_COUNTER_TQXTBC_Q0:
        res = s->transmit_queue_token_bucket_counter_tqxtbc_q0;
        break;
    case TRANSMIT_QUEUE_TOKEN_BUCKET_CONFIGURATION_TQXTBC_Q0:
        res = s->transmit_queue_token_bucket_configuration_tqxtbc_q0;
        break;
    case TRANSMIT_QUEUE_ARBITER_CONFIGURATION_TQXAC_Q0:
        res = s->transmit_queue_arbiter_configuration_tqxac_q0;
        break;
    case TRANSMIT_QUEUE_TOKEN_BUCKET_COUNTER_TQXTBC_Q1:
        res = s->transmit_queue_token_bucket_counter_tqxtbc_q1;
        break;
    case TRANSMIT_QUEUE_TOKEN_BUCKET_CONFIGURATION_TQXTBC_Q1:
        res = s->transmit_queue_token_bucket_configuration_tqxtbc_q1;
        break;
    case TRANSMIT_QUEUE_ARBITER_CONFIGURATION_TQXAC_Q1:
        res = s->transmit_queue_arbiter_configuration_tqxac_q1;
        break;
    case TRANSMIT_QUEUE_TOKEN_BUCKET_COUNTER_TQXTBC_Q2:
        res = s->transmit_queue_token_bucket_counter_tqxtbc_q2;
        break;
    case TRANSMIT_QUEUE_TOKEN_BUCKET_CONFIGURATION_TQXTBC_Q2:
        res = s->transmit_queue_token_bucket_configuration_tqxtbc_q2;
        break;
    case TRANSMIT_QUEUE_ARBITER_CONFIGURATION_TQXAC_Q2:
        res = s->transmit_queue_arbiter_configuration_tqxac_q2;
        break;
    case TRANSMIT_QUEUE_TOKEN_BUCKET_COUNTER_TQXTBC_Q3:
        res = s->transmit_queue_token_bucket_counter_tqxtbc_q3;
        break;
    case TRANSMIT_QUEUE_TOKEN_BUCKET_CONFIGURATION_TQXTBC_Q3:
        res = s->transmit_queue_token_bucket_configuration_tqxtbc_q3;
        break;
    case TRANSMIT_QUEUE_ARBITER_CONFIGURATION_TQXAC_Q3:
        res = s->transmit_queue_arbiter_configuration_tqxac_q3;
        break;
    case TRANSMIT_QUEUE_TOKEN_BUCKET_COUNTER_TQXTBC_Q4:
        res = s->transmit_queue_token_bucket_counter_tqxtbc_q4;
        break;
    case TRANSMIT_QUEUE_TOKEN_BUCKET_CONFIGURATION_TQXTBC_Q4:
        res = s->transmit_queue_token_bucket_configuration_tqxtbc_q4;
        break;
    case TRANSMIT_QUEUE_ARBITER_CONFIGURATION_TQXAC_Q4:
        res = s->transmit_queue_arbiter_configuration_tqxac_q4;
        break;
    case TRANSMIT_QUEUE_TOKEN_BUCKET_COUNTER_TQXTBC_Q5:
        res = s->transmit_queue_token_bucket_counter_tqxtbc_q5;
        break;
    case TRANSMIT_QUEUE_TOKEN_BUCKET_CONFIGURATION_TQXTBC_Q5:
        res = s->transmit_queue_token_bucket_configuration_tqxtbc_q5;
        break;
    case TRANSMIT_QUEUE_ARBITER_CONFIGURATION_TQXAC_Q5:
        res = s->transmit_queue_arbiter_configuration_tqxac_q5;
        break;
    case TRANSMIT_QUEUE_TOKEN_BUCKET_COUNTER_TQXTBC_Q6:
        res = s->transmit_queue_token_bucket_counter_tqxtbc_q6;
        break;
    case TRANSMIT_QUEUE_TOKEN_BUCKET_CONFIGURATION_TQXTBC_Q6:
        res = s->transmit_queue_token_bucket_configuration_tqxtbc_q6;
        break;
    case TRANSMIT_QUEUE_ARBITER_CONFIGURATION_TQXAC_Q6:
        res = s->transmit_queue_arbiter_configuration_tqxac_q6;
        break;
    case TRANSMIT_QUEUE_TOKEN_BUCKET_COUNTER_TQXTBC_Q7:
        res = s->transmit_queue_token_bucket_counter_tqxtbc_q7;
        break;
    case TRANSMIT_QUEUE_TOKEN_BUCKET_CONFIGURATION_TQXTBC_Q7:
        res = s->transmit_queue_token_bucket_configuration_tqxtbc_q7;
        break;
    case TRANSMIT_QUEUE_ARBITER_CONFIGURATION_TQXAC_Q7:
        res = s->transmit_queue_arbiter_configuration_tqxac_q7;
        break;
    case MAC_MIB_COUNTERSNTERRUPT_CAUSE_REGISTER:
        res = s->mac_mib_countersnterrupt_cause_register;
        break;
    case DESTINATION_ADDRESS_FILTER_SPECIAL_MULTICAST_TABLE_DFSMT:
        res = s->destination_address_filter_special_multicast_table_dfsmt;
        break;
    case DESTINATION_ADDRESS_FILTER_OTHER_MULTICAST_TABLE_DFUT:
        res = s->destination_address_filter_other_multicast_table_dfut;
        break;
    case DESTINATION_ADDRESS_FILTER_UNICAST_TABLE_DFUT:
        res = s->destination_address_filter_unicast_table_dfut;
        break;
    }
    return res;
}

static void mv88f5181l_gigabit_ethernet_controller_write(void *opaque, hwaddr offset, uint64_t val, unsigned size) {
    MV88F5181LState *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case PHY_ADDRESS:
        s->phy_address = val;
        break;
    case SMI:
        s->smi = val;
        break;
    case ETHERNET_UNIT_DEFAULT_ADDRESS_EUDA:
        s->ethernet_unit_default_address_euda = val;
        break;
    case ETHERNET_UNIT_DEFAULT_ID_EUDID:
        s->ethernet_unit_default_id_eudid = val;
        break;
    case ETHERNET_UNIT_RESERVED_EU:
        s->ethernet_unit_reserved_eu = val;
        break;
    case ETHERNET_UNIT_INTERRUPT_CAUSE_EUIC:
        s->ethernet_unit_interrupt_cause_euic = val;
        break;
    case ETHERNET_UNIT_INTERRUPT_MASK_EUIM:
        s->ethernet_unit_interrupt_mask_euim = val;
        break;
    case ETHERNET_UNIT_ERROR_ADDRESS_EUEA:
        s->ethernet_unit_error_address_euea = val;
        break;
    case ETHERNET_UNIT_INTERNAL_ADDRESS_ERROR_EUIAE:
        s->ethernet_unit_internal_address_error_euiae = val;
        break;
    case ETHERNET_UNIT_PORT_PADS_CALIBRATION_EUPCR:
        s->ethernet_unit_port_pads_calibration_eupcr = val;
        break;
    case ETHERNET_UNIT_CONTROL_EUC:
        s->ethernet_unit_control_euc = val;
        break;
    case BASE_ADDRESS_0_BA0:
        s->base_address_0_ba0 = val;
        break;
    case SIZE_S_0_SR0:
        s->size_s_0_sr0 = val;
        break;
    case BASE_ADDRESS_1_BA1:
        s->base_address_1_ba1 = val;
        break;
    case SIZE_S_1_SR1:
        s->size_s_1_sr1 = val;
        break;
    case BASE_ADDRESS_2_BA2:
        s->base_address_2_ba2 = val;
        break;
    case SIZE_S_2_SR2:
        s->size_s_2_sr2 = val;
        break;
    case BASE_ADDRESS_3_BA3:
        s->base_address_3_ba3 = val;
        break;
    case SIZE_S_3_SR3:
        s->size_s_3_sr3 = val;
        break;
    case BASE_ADDRESS_4_BA4:
        s->base_address_4_ba4 = val;
        break;
    case SIZE_S_4_SR4:
        s->size_s_4_sr4 = val;
        break;
    case BASE_ADDRESS_5_BA5:
        s->base_address_5_ba5 = val;
        break;
    case SIZE_S_5_SR5:
        s->size_s_5_sr5 = val;
        break;
    case HIGH_ADDRESS_REMAP_HA_HARR0:
        s->high_address_remap_ha_harr0 = val;
        break;
    case HIGH_ADDRESS_REMAP_HA_HARR1:
        s->high_address_remap_ha_harr1 = val;
        break;
    case HIGH_ADDRESS_REMAP_HA_HARR2:
        s->high_address_remap_ha_harr2 = val;
        break;
    case HIGH_ADDRESS_REMAP_HA_HARR3:
        s->high_address_remap_ha_harr3 = val;
        break;
    case BASE_ADDRESS_ENABLE_BARE:
        s->base_address_enable_bare = val;
        break;
    case ETHERNET_PORT_ACCESS_PROTECT_EPAP:
        s->ethernet_port_access_protect_epap = val;
        break;
    case PORT_CONFIGURATION_GEC:
        s->port_configuration_gec = val;
        break;
    case PORT_CONFIGURATION_EXTEND_GECX:
        s->port_configuration_extend_gecx = val;
        break;
    case MII_SERIAL_PARAMETERS:
        s->mii_serial_parameters = val;
        break;
    case GMII_SERIAL_PARAMETERS:
        s->gmii_serial_parameters = val;
        break;
    case VLAN_ETHERTYPE_EVLANE:
        s->vlan_ethertype_evlane = val;
        break;
    case MAC_ADDRESS_LOW_MACAL:
        s->mac_address_low_macal = val;
        break;
    case MAC_ADDRESS_HIGH_MACAH:
        s->mac_address_high_macah = val;
        break;
    case SDMA_CONFIGURATION_SDC:
        s->sdma_configuration_sdc = val;
        break;
    case IP_DIFFERENTIATED_SERVICES_CODEPOINT_0_TO_PRIORITY_DSCP0:
        s->ip_differentiated_services_codepoint_0_to_priority_dscp0 = val;
        break;
    case IP_DIFFERENTIATED_SERVICES_CODEPOINT_1_TO_PRIORITY_DSCP1:
        s->ip_differentiated_services_codepoint_1_to_priority_dscp1 = val;
        break;
    case IP_DIFFERENTIATED_SERVICES_CODEPOINT_2_TO_PRIORITY_DSCP2:
        s->ip_differentiated_services_codepoint_2_to_priority_dscp2 = val;
        break;
    case IP_DIFFERENTIATED_SERVICES_CODEPOINT_23_TO_PRIORITY_DSCP3:
        s->ip_differentiated_services_codepoint_23_to_priority_dscp3 = val;
        break;
    case IP_DIFFERENTIATED_SERVICES_CODEPOINT_24_TO_PRIORITY_DSCP4:
        s->ip_differentiated_services_codepoint_24_to_priority_dscp4 = val;
        break;
    case IP_DIFFERENTIATED_SERVICES_CODEPOINT_25_TO_PRIORITY_DSCP5:
        s->ip_differentiated_services_codepoint_25_to_priority_dscp5 = val;
        break;
    case IP_DIFFERENTIATED_SERVICES_CODEPOINT_6_TO_PRIORITY_DSCP6:
        s->ip_differentiated_services_codepoint_6_to_priority_dscp6 = val;
        break;
    case PORT_SERIAL_CONTROL_PSC:
        s->port_serial_control_psc = val;
        break;
    case VLAN_PRIORITY_TAG_TO_PRIORITY_VPT2P:
        s->vlan_priority_tag_to_priority_vpt2p = val;
        break;
    case ETHERNET_PORT_STATUS_PS:
        s->ethernet_port_status_ps = val;
        break;
    case TRANSMIT_QUEUE_COMMAND_TQC:
        s->transmit_queue_command_tqc = val;
        break;
    case MAXIMUM_TRANSMIT_UNIT_MTU:
        s->maximum_transmit_unit_mtu = val;
        break;
    case PORT_INTERRUPT_CAUSE_IC:
        s->port_interrupt_cause_ic = val;
        break;
    case PORT_INTERRUPT_CAUSE_EXTEND_ICE:
        s->port_interrupt_cause_extend_ice = val;
        break;
    case PORT_INTERRUPT_MASK_PIM:
        s->port_interrupt_mask_pim = val;
        break;
    case PORT_EXTEND_INTERRUPT_MASK_PEIM:
        s->port_extend_interrupt_mask_peim = val;
        break;
    case PORT_RX_FIFO_URGENT_THRESHOLD_PRFUT:
        s->port_rx_fifo_urgent_threshold_prfut = val;
        break;
    case PORT_TX_FIFO_URGENT_THRESHOLD_PTFUT:
        s->port_tx_fifo_urgent_threshold_ptfut = val;
        break;
    case PORT_RX_MINIMAL_FRAME_SIZE_PMFS:
        s->port_rx_minimal_frame_size_pmfs = val;
        break;
    case PORT_RX_DISCARD_FRAME_COUNTER_GEDFC:
        s->port_rx_discard_frame_counter_gedfc = val;
        break;
    case PORT_OVERRUN_FRAME_COUNTER_POFC:
        s->port_overrun_frame_counter_pofc = val;
        break;
    case PORT_INTERNAL_ADDRESS_ERROR_EUIAE:
        s->port_internal_address_error_euiae = val;
        break;
    case ETHERNET_CURRENT_RECEIVE_DESCRIPTOR_POINTERS_CRDP_Q0:
        s->ethernet_current_receive_descriptor_pointers_crdp_q0 = val;
        break;
    case ETHERNET_CURRENT_RECEIVE_DESCRIPTOR_POINTERS_CRDP_Q1:
        s->ethernet_current_receive_descriptor_pointers_crdp_q1 = val;
        break;
    case ETHERNET_CURRENT_RECEIVE_DESCRIPTOR_POINTERS_CRDP_Q2:
        s->ethernet_current_receive_descriptor_pointers_crdp_q2 = val;
        break;
    case ETHERNET_CURRENT_RECEIVE_DESCRIPTOR_POINTERS_CRDP_Q3:
        s->ethernet_current_receive_descriptor_pointers_crdp_q3 = val;
        break;
    case ETHERNET_CURRENT_RECEIVE_DESCRIPTOR_POINTERS_CRDP_Q4:
        s->ethernet_current_receive_descriptor_pointers_crdp_q4 = val;
        break;
    case ETHERNET_CURRENT_RECEIVE_DESCRIPTOR_POINTERS_CRDP_Q5:
        s->ethernet_current_receive_descriptor_pointers_crdp_q5 = val;
        break;
    case ETHERNET_CURRENT_RECEIVE_DESCRIPTOR_POINTERS_CRDP_Q6:
        s->ethernet_current_receive_descriptor_pointers_crdp_q6 = val;
        break;
    case ETHERNET_CURRENT_RECEIVE_DESCRIPTOR_POINTERS_CRDP_Q7:
        s->ethernet_current_receive_descriptor_pointers_crdp_q7 = val;
        break;
    case RECEIVE_QUEUE_COMMAND_RQC:
        s->receive_queue_command_rqc = val;
        break;
    case TRANSMIT_CURRENT_SERVED_DESCRIPTOR_POINTER:
        s->transmit_current_served_descriptor_pointer = val;
        break;
    case TRANSMIT_CURRENT_QUEUE_DESCRIPTOR_POINTER_TCQDP_Q0:
        s->transmit_current_queue_descriptor_pointer_tcqdp_q0 = val;
        break;
    case TRANSMIT_QUEUE_TOKEN_BUCKET_COUNTER_TQXTBC_Q0:
        s->transmit_queue_token_bucket_counter_tqxtbc_q0 = val;
        break;
    case TRANSMIT_QUEUE_TOKEN_BUCKET_CONFIGURATION_TQXTBC_Q0:
        s->transmit_queue_token_bucket_configuration_tqxtbc_q0 = val;
        break;
    case TRANSMIT_QUEUE_ARBITER_CONFIGURATION_TQXAC_Q0:
        s->transmit_queue_arbiter_configuration_tqxac_q0 = val;
        break;
    case TRANSMIT_QUEUE_TOKEN_BUCKET_COUNTER_TQXTBC_Q1:
        s->transmit_queue_token_bucket_counter_tqxtbc_q1 = val;
        break;
    case TRANSMIT_QUEUE_TOKEN_BUCKET_CONFIGURATION_TQXTBC_Q1:
        s->transmit_queue_token_bucket_configuration_tqxtbc_q1 = val;
        break;
    case TRANSMIT_QUEUE_ARBITER_CONFIGURATION_TQXAC_Q1:
        s->transmit_queue_arbiter_configuration_tqxac_q1 = val;
        break;
    case TRANSMIT_QUEUE_TOKEN_BUCKET_COUNTER_TQXTBC_Q2:
        s->transmit_queue_token_bucket_counter_tqxtbc_q2 = val;
        break;
    case TRANSMIT_QUEUE_TOKEN_BUCKET_CONFIGURATION_TQXTBC_Q2:
        s->transmit_queue_token_bucket_configuration_tqxtbc_q2 = val;
        break;
    case TRANSMIT_QUEUE_ARBITER_CONFIGURATION_TQXAC_Q2:
        s->transmit_queue_arbiter_configuration_tqxac_q2 = val;
        break;
    case TRANSMIT_QUEUE_TOKEN_BUCKET_COUNTER_TQXTBC_Q3:
        s->transmit_queue_token_bucket_counter_tqxtbc_q3 = val;
        break;
    case TRANSMIT_QUEUE_TOKEN_BUCKET_CONFIGURATION_TQXTBC_Q3:
        s->transmit_queue_token_bucket_configuration_tqxtbc_q3 = val;
        break;
    case TRANSMIT_QUEUE_ARBITER_CONFIGURATION_TQXAC_Q3:
        s->transmit_queue_arbiter_configuration_tqxac_q3 = val;
        break;
    case TRANSMIT_QUEUE_TOKEN_BUCKET_COUNTER_TQXTBC_Q4:
        s->transmit_queue_token_bucket_counter_tqxtbc_q4 = val;
        break;
    case TRANSMIT_QUEUE_TOKEN_BUCKET_CONFIGURATION_TQXTBC_Q4:
        s->transmit_queue_token_bucket_configuration_tqxtbc_q4 = val;
        break;
    case TRANSMIT_QUEUE_ARBITER_CONFIGURATION_TQXAC_Q4:
        s->transmit_queue_arbiter_configuration_tqxac_q4 = val;
        break;
    case TRANSMIT_QUEUE_TOKEN_BUCKET_COUNTER_TQXTBC_Q5:
        s->transmit_queue_token_bucket_counter_tqxtbc_q5 = val;
        break;
    case TRANSMIT_QUEUE_TOKEN_BUCKET_CONFIGURATION_TQXTBC_Q5:
        s->transmit_queue_token_bucket_configuration_tqxtbc_q5 = val;
        break;
    case TRANSMIT_QUEUE_ARBITER_CONFIGURATION_TQXAC_Q5:
        s->transmit_queue_arbiter_configuration_tqxac_q5 = val;
        break;
    case TRANSMIT_QUEUE_TOKEN_BUCKET_COUNTER_TQXTBC_Q6:
        s->transmit_queue_token_bucket_counter_tqxtbc_q6 = val;
        break;
    case TRANSMIT_QUEUE_TOKEN_BUCKET_CONFIGURATION_TQXTBC_Q6:
        s->transmit_queue_token_bucket_configuration_tqxtbc_q6 = val;
        break;
    case TRANSMIT_QUEUE_ARBITER_CONFIGURATION_TQXAC_Q6:
        s->transmit_queue_arbiter_configuration_tqxac_q6 = val;
        break;
    case TRANSMIT_QUEUE_TOKEN_BUCKET_COUNTER_TQXTBC_Q7:
        s->transmit_queue_token_bucket_counter_tqxtbc_q7 = val;
        break;
    case TRANSMIT_QUEUE_TOKEN_BUCKET_CONFIGURATION_TQXTBC_Q7:
        s->transmit_queue_token_bucket_configuration_tqxtbc_q7 = val;
        break;
    case TRANSMIT_QUEUE_ARBITER_CONFIGURATION_TQXAC_Q7:
        s->transmit_queue_arbiter_configuration_tqxac_q7 = val;
        break;
    case MAC_MIB_COUNTERSNTERRUPT_CAUSE_REGISTER:
        s->mac_mib_countersnterrupt_cause_register = val;
        break;
    case DESTINATION_ADDRESS_FILTER_SPECIAL_MULTICAST_TABLE_DFSMT:
        s->destination_address_filter_special_multicast_table_dfsmt = val;
        break;
    case DESTINATION_ADDRESS_FILTER_OTHER_MULTICAST_TABLE_DFUT:
        s->destination_address_filter_other_multicast_table_dfut = val;
        break;
    case DESTINATION_ADDRESS_FILTER_UNICAST_TABLE_DFUT:
        s->destination_address_filter_unicast_table_dfut = val;
        break;
    }
    mv88f5181l_gigabit_ethernet_controller_update(s);
}

static const MemoryRegionOps mv88f5181l_gigabit_ethernet_controller_ops = {
    .read = mv88f5181l_gigabit_ethernet_controller_read,
    .write = mv88f5181l_gigabit_ethernet_controller_write,
    .endianness = DEVICE_NATIVE_ENDIAN,
};

static void mv88f5181l_cesa_update(void *opaque) {
    /* MV88F5181LState *s = opaque; */
}

static uint64_t mv88f5181l_cesa_read(void *opaque, hwaddr offset, unsigned size) {
    MV88F5181LState *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case DES_DATA_OUT_LOW_REGISTER:
        res = s->des_data_out_low_register;
        break;
    case DES_DATA_OUT_HIGH_REGISTER:
        res = s->des_data_out_high_register;
        break;
    case DES_DATA_BUFFER_LOW_REGISTER:
        res = s->des_data_buffer_low_register;
        break;
    case DES_DATA_BUFFER_HIGH_REGISTER:
        res = s->des_data_buffer_high_register;
        break;
    case DES_INITIAL_VALUE_LOW_REGISTER:
        res = s->des_initial_value_low_register;
        break;
    case DES_INITIAL_VALUE_HIGH_REGISTER:
        res = s->des_initial_value_high_register;
        break;
    case DES_KEY0_LOW_REGISTER:
        res = s->des_key0_low_register;
        break;
    case DES_KEY0_HIGH_REGISTER:
        res = s->des_key0_high_register;
        break;
    case DES_KEY1_LOW_REGISTER:
        res = s->des_key1_low_register;
        break;
    case DES_KEY1_HIGH_REGISTER:
        res = s->des_key1_high_register;
        break;
    case DES_KEY2_LOW_REGISTER:
        res = s->des_key2_low_register;
        break;
    case DES_KEY2_HIGH_REGISTER:
        res = s->des_key2_high_register;
        break;
    case DES_COMMAND_REGISTER:
        res = s->des_command_register;
        break;
    case SHA_1_OR_MD5_DATA_IN_REGISTER:
        res = s->sha_1_or_md5_data_in_register;
        break;
    case SHA_1_OR_MD5_BIT_COUNT_LOW_REGISTER:
        res = s->sha_1_or_md5_bit_count_low_register;
        break;
    case SHA_1_OR_MD5_BIT_COUNT_HIGH_REGISTER:
        res = s->sha_1_or_md5_bit_count_high_register;
        break;
    case SHA_1_OR_MD5_INITIAL_VALUE_OR_DIGEST_A_REGISTER:
        res = s->sha_1_or_md5_initial_value_or_digest_a_register;
        break;
    case SHA_1_OR_MD5_INITIAL_VALUE_OR_DIGEST_B_REGISTER:
        res = s->sha_1_or_md5_initial_value_or_digest_b_register;
        break;
    case SHA_1_OR_MD5_INITIAL_VALUE_OR_DIGEST_C_REGISTER:
        res = s->sha_1_or_md5_initial_value_or_digest_c_register;
        break;
    case SHA_1_OR_MD5_INITIAL_VALUE_OR_DIGEST_D_REGISTER:
        res = s->sha_1_or_md5_initial_value_or_digest_d_register;
        break;
    case SHA_1_INITIAL_VALUE_OR_DIGEST_E_REGISTER:
        res = s->sha_1_initial_value_or_digest_e_register;
        break;
    case SHA_1_OR_MD5_AUTHENTICATION_COMMAND_REGISTER:
        res = s->sha_1_or_md5_authentication_command_register;
        break;
    case AES_ENCRYPTION_DATA_IN_OR_OUT_COLUMN_3_REGISTER:
        res = s->aes_encryption_data_in_or_out_column_3_register;
        break;
    case AES_ENCRYPTION_DATA_IN_OR_OUT_COLUMN_2_REGISTER:
        res = s->aes_encryption_data_in_or_out_column_2_register;
        break;
    case AES_ENCRYPTION_DATA_IN_OR_OUT_COLUMN_1_REGISTER:
        res = s->aes_encryption_data_in_or_out_column_1_register;
        break;
    case AES_ENCRYPTION_DATA_IN_OR_OUT_COLUMN_0_REGISTER:
        res = s->aes_encryption_data_in_or_out_column_0_register;
        break;
    case AES_ENCRYPTION_KEY_COLUMN_3_REGISTER:
        res = s->aes_encryption_key_column_3_register;
        break;
    case AES_ENCRYPTION_KEY_COLUMN_2_REGISTER:
        res = s->aes_encryption_key_column_2_register;
        break;
    case AES_ENCRYPTION_KEY_COLUMN_1_REGISTER:
        res = s->aes_encryption_key_column_1_register;
        break;
    case AES_ENCRYPTION_KEY_COLUMN_0_REGISTER:
        res = s->aes_encryption_key_column_0_register;
        break;
    case AES_ENCRYPTION_KEY_COLUMN_7_REGISTER:
        res = s->aes_encryption_key_column_7_register;
        break;
    case AES_ENCRYPTION_KEY_COLUMN_6_REGISTER:
        res = s->aes_encryption_key_column_6_register;
        break;
    case AES_ENCRYPTION_KEY_COLUMN_5_REGISTER:
        res = s->aes_encryption_key_column_5_register;
        break;
    case AES_ENCRYPTION_KEY_COLUMN_4_REGISTER:
        res = s->aes_encryption_key_column_4_register;
        break;
    case AES_ENCRYPTION_COMMAND_REGISTER:
        res = s->aes_encryption_command_register;
        break;
    case AES_DECRYPTION_DATA_IN_OR_OUT_COLUMN_3_REGISTER:
        res = s->aes_decryption_data_in_or_out_column_3_register;
        break;
    case AES_DECRYPTION_DATA_IN_OR_OUT_COLUMN_2_REGISTER:
        res = s->aes_decryption_data_in_or_out_column_2_register;
        break;
    case AES_DECRYPTION_DATA_IN_OR_OUT_COLUMN_1_REGISTER:
        res = s->aes_decryption_data_in_or_out_column_1_register;
        break;
    case AES_DECRYPTION_DATA_IN_OR_OUT_COLUMN_0_REGISTER:
        res = s->aes_decryption_data_in_or_out_column_0_register;
        break;
    case AES_DECRYPTION_KEY_COLUMN_3_REGISTER:
        res = s->aes_decryption_key_column_3_register;
        break;
    case AES_DECRYPTION_KEY_COLUMN_2_REGISTER:
        res = s->aes_decryption_key_column_2_register;
        break;
    case AES_DECRYPTION_KEY_COLUMN_1_REGISTER:
        res = s->aes_decryption_key_column_1_register;
        break;
    case AES_DECRYPTION_KEY_COLUMN_0_REGISTER:
        res = s->aes_decryption_key_column_0_register;
        break;
    case AES_DECRYPTION_KEY_COLUMN_7_REGISTER:
        res = s->aes_decryption_key_column_7_register;
        break;
    case AES_DECRYPTION_KEY_COLUMN_6_REGISTER:
        res = s->aes_decryption_key_column_6_register;
        break;
    case AES_DECRYPTION_KEY_COLUMN_5_REGISTER:
        res = s->aes_decryption_key_column_5_register;
        break;
    case AES_DECRYPTION_KEY_COLUMN_4_REGISTER:
        res = s->aes_decryption_key_column_4_register;
        break;
    case AES_DECRYPTION_COMMAND_REGISTER:
        res = s->aes_decryption_command_register;
        break;
    case SECURITY_ACCELERATOR_COMMAND_REGISTER:
        res = s->security_accelerator_command_register;
        break;
    case SECURITY_ACCELERATOR_DESCRIPTOR_POINTER_SESSION_0_REGISTER:
        res = s->security_accelerator_descriptor_pointer_session_0_register;
        break;
    case SECURITY_ACCELERATOR_DESCRIPTOR_POINTER_SESSION_1_REGISTER:
        res = s->security_accelerator_descriptor_pointer_session_1_register;
        break;
    case SECURITY_ACCELERATOR_CONFIGURATION_REGISTER:
        res = s->security_accelerator_configuration_register;
        break;
    case SECURITY_ACCELERATOR_STATUS_REGISTER:
        res = s->security_accelerator_status_register;
        break;
    case CRYPTOGRAPHIC_ENGINES_AND_SECURITY_ACCELERATOR_INTERRUPT_CAUSE_REGISTER:
        res = s->cryptographic_engines_and_security_accelerator_interrupt_cause_register;
        break;
    case CRYPTOGRAPHIC_ENGINES_AND_SECURITY_ACCELERATOR_INTERRUPT_MASK_REGISTER:
        res = s->cryptographic_engines_and_security_accelerator_interrupt_mask_register;
        break;
    }
    return res;
}

static void mv88f5181l_cesa_write(void *opaque, hwaddr offset, uint64_t val, unsigned size) {
    MV88F5181LState *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case DES_DATA_OUT_LOW_REGISTER:
        s->des_data_out_low_register = val;
        break;
    case DES_DATA_OUT_HIGH_REGISTER:
        s->des_data_out_high_register = val;
        break;
    case DES_DATA_BUFFER_LOW_REGISTER:
        s->des_data_buffer_low_register = val;
        break;
    case DES_DATA_BUFFER_HIGH_REGISTER:
        s->des_data_buffer_high_register = val;
        break;
    case DES_INITIAL_VALUE_LOW_REGISTER:
        s->des_initial_value_low_register = val;
        break;
    case DES_INITIAL_VALUE_HIGH_REGISTER:
        s->des_initial_value_high_register = val;
        break;
    case DES_KEY0_LOW_REGISTER:
        s->des_key0_low_register = val;
        break;
    case DES_KEY0_HIGH_REGISTER:
        s->des_key0_high_register = val;
        break;
    case DES_KEY1_LOW_REGISTER:
        s->des_key1_low_register = val;
        break;
    case DES_KEY1_HIGH_REGISTER:
        s->des_key1_high_register = val;
        break;
    case DES_KEY2_LOW_REGISTER:
        s->des_key2_low_register = val;
        break;
    case DES_KEY2_HIGH_REGISTER:
        s->des_key2_high_register = val;
        break;
    case DES_COMMAND_REGISTER:
        s->des_command_register = val;
        break;
    case SHA_1_OR_MD5_DATA_IN_REGISTER:
        s->sha_1_or_md5_data_in_register = val;
        break;
    case SHA_1_OR_MD5_BIT_COUNT_LOW_REGISTER:
        s->sha_1_or_md5_bit_count_low_register = val;
        break;
    case SHA_1_OR_MD5_BIT_COUNT_HIGH_REGISTER:
        s->sha_1_or_md5_bit_count_high_register = val;
        break;
    case SHA_1_OR_MD5_INITIAL_VALUE_OR_DIGEST_A_REGISTER:
        s->sha_1_or_md5_initial_value_or_digest_a_register = val;
        break;
    case SHA_1_OR_MD5_INITIAL_VALUE_OR_DIGEST_B_REGISTER:
        s->sha_1_or_md5_initial_value_or_digest_b_register = val;
        break;
    case SHA_1_OR_MD5_INITIAL_VALUE_OR_DIGEST_C_REGISTER:
        s->sha_1_or_md5_initial_value_or_digest_c_register = val;
        break;
    case SHA_1_OR_MD5_INITIAL_VALUE_OR_DIGEST_D_REGISTER:
        s->sha_1_or_md5_initial_value_or_digest_d_register = val;
        break;
    case SHA_1_INITIAL_VALUE_OR_DIGEST_E_REGISTER:
        s->sha_1_initial_value_or_digest_e_register = val;
        break;
    case SHA_1_OR_MD5_AUTHENTICATION_COMMAND_REGISTER:
        s->sha_1_or_md5_authentication_command_register = val;
        break;
    case AES_ENCRYPTION_DATA_IN_OR_OUT_COLUMN_3_REGISTER:
        s->aes_encryption_data_in_or_out_column_3_register = val;
        break;
    case AES_ENCRYPTION_DATA_IN_OR_OUT_COLUMN_2_REGISTER:
        s->aes_encryption_data_in_or_out_column_2_register = val;
        break;
    case AES_ENCRYPTION_DATA_IN_OR_OUT_COLUMN_1_REGISTER:
        s->aes_encryption_data_in_or_out_column_1_register = val;
        break;
    case AES_ENCRYPTION_DATA_IN_OR_OUT_COLUMN_0_REGISTER:
        s->aes_encryption_data_in_or_out_column_0_register = val;
        break;
    case AES_ENCRYPTION_KEY_COLUMN_3_REGISTER:
        s->aes_encryption_key_column_3_register = val;
        break;
    case AES_ENCRYPTION_KEY_COLUMN_2_REGISTER:
        s->aes_encryption_key_column_2_register = val;
        break;
    case AES_ENCRYPTION_KEY_COLUMN_1_REGISTER:
        s->aes_encryption_key_column_1_register = val;
        break;
    case AES_ENCRYPTION_KEY_COLUMN_0_REGISTER:
        s->aes_encryption_key_column_0_register = val;
        break;
    case AES_ENCRYPTION_KEY_COLUMN_7_REGISTER:
        s->aes_encryption_key_column_7_register = val;
        break;
    case AES_ENCRYPTION_KEY_COLUMN_6_REGISTER:
        s->aes_encryption_key_column_6_register = val;
        break;
    case AES_ENCRYPTION_KEY_COLUMN_5_REGISTER:
        s->aes_encryption_key_column_5_register = val;
        break;
    case AES_ENCRYPTION_KEY_COLUMN_4_REGISTER:
        s->aes_encryption_key_column_4_register = val;
        break;
    case AES_ENCRYPTION_COMMAND_REGISTER:
        s->aes_encryption_command_register = val;
        break;
    case AES_DECRYPTION_DATA_IN_OR_OUT_COLUMN_3_REGISTER:
        s->aes_decryption_data_in_or_out_column_3_register = val;
        break;
    case AES_DECRYPTION_DATA_IN_OR_OUT_COLUMN_2_REGISTER:
        s->aes_decryption_data_in_or_out_column_2_register = val;
        break;
    case AES_DECRYPTION_DATA_IN_OR_OUT_COLUMN_1_REGISTER:
        s->aes_decryption_data_in_or_out_column_1_register = val;
        break;
    case AES_DECRYPTION_DATA_IN_OR_OUT_COLUMN_0_REGISTER:
        s->aes_decryption_data_in_or_out_column_0_register = val;
        break;
    case AES_DECRYPTION_KEY_COLUMN_3_REGISTER:
        s->aes_decryption_key_column_3_register = val;
        break;
    case AES_DECRYPTION_KEY_COLUMN_2_REGISTER:
        s->aes_decryption_key_column_2_register = val;
        break;
    case AES_DECRYPTION_KEY_COLUMN_1_REGISTER:
        s->aes_decryption_key_column_1_register = val;
        break;
    case AES_DECRYPTION_KEY_COLUMN_0_REGISTER:
        s->aes_decryption_key_column_0_register = val;
        break;
    case AES_DECRYPTION_KEY_COLUMN_7_REGISTER:
        s->aes_decryption_key_column_7_register = val;
        break;
    case AES_DECRYPTION_KEY_COLUMN_6_REGISTER:
        s->aes_decryption_key_column_6_register = val;
        break;
    case AES_DECRYPTION_KEY_COLUMN_5_REGISTER:
        s->aes_decryption_key_column_5_register = val;
        break;
    case AES_DECRYPTION_KEY_COLUMN_4_REGISTER:
        s->aes_decryption_key_column_4_register = val;
        break;
    case AES_DECRYPTION_COMMAND_REGISTER:
        s->aes_decryption_command_register = val;
        break;
    case SECURITY_ACCELERATOR_COMMAND_REGISTER:
        s->security_accelerator_command_register = val;
        break;
    case SECURITY_ACCELERATOR_DESCRIPTOR_POINTER_SESSION_0_REGISTER:
        s->security_accelerator_descriptor_pointer_session_0_register = val;
        break;
    case SECURITY_ACCELERATOR_DESCRIPTOR_POINTER_SESSION_1_REGISTER:
        s->security_accelerator_descriptor_pointer_session_1_register = val;
        break;
    case SECURITY_ACCELERATOR_CONFIGURATION_REGISTER:
        s->security_accelerator_configuration_register = val;
        break;
    case SECURITY_ACCELERATOR_STATUS_REGISTER:
        s->security_accelerator_status_register = val;
        break;
    case CRYPTOGRAPHIC_ENGINES_AND_SECURITY_ACCELERATOR_INTERRUPT_CAUSE_REGISTER:
        s->cryptographic_engines_and_security_accelerator_interrupt_cause_register = val;
        break;
    case CRYPTOGRAPHIC_ENGINES_AND_SECURITY_ACCELERATOR_INTERRUPT_MASK_REGISTER:
        s->cryptographic_engines_and_security_accelerator_interrupt_mask_register = val;
        break;
    }
    mv88f5181l_cesa_update(s);
}

static const MemoryRegionOps mv88f5181l_cesa_ops = {
    .read = mv88f5181l_cesa_read,
    .write = mv88f5181l_cesa_write,
    .endianness = DEVICE_NATIVE_ENDIAN,
};

static void mv88f5181l_reset(void *opaque) {
    MV88F5181LState *s = opaque;
    
    s->gpio_data_out_register = 0x0 << 0 | 0x0 << 26;
    s->gpio_data_out_enable_control_register = 0xFFFF << 0 | 0x0 << 26;
    s->gpio_blink_enable_register = 0x0 << 0 | 0x0 << 26;
    s->gpio_data_in_polarity_register = 0x0 << 0 | 0x0 << 26;
    s->gpio_data_in_register = 0x0 << 0 | 0x0 << 26;
    s->gpio_interrupt_cause_register = 0x0 << 0 | 0x0 << 26;
    s->gpio_interrupt_mask_register = 0x0 << 0 | 0x0 << 26;
    s->gpio_interrupt_level_mask_register = 0x0 << 0 | 0x0 << 26;
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
    s->ddr_sdram_configuration_register = 0x400 << 0 | 0x2 << 14 | 0x1 << 18 | 0x2 << 20 | 0x1 << 24 | 0x1 << 25 /* 0 14 17 18 19 20 22 24 25 26 */;
    s->ddr_sdram_control_register = 0x1 << 6 | 0x1 << 12 | 0x1 << 18 | 0x3 << 24 /* 0 6 7 12 13 14 18 19 24 28 */;
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
    s->mpp_control_0_register = 0x0;
    s->mpp_control_1_register = 0x0;
    s->mpp_control_2_register = 0x0;
    s->device_multiplex_control_register = 0x0;
    s->sample_at_reset_register = 0x0;
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
    s->base_address_registers_enable = 0x1 << 4 | 0x1 << 5 | 0x1 << 7 | 0x1 << 10 | 0x1 << 11 | 0x1 << 12 | 0x1 << 13 /* 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 16 */;
    s->csn0_base_address_remap = 0x0 /* 0 12 */;
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
    s->pci_address_decode_control = 0x1 << 3 /* 0 1 3 4 8 25 */;
    s->pci_dll_control = 0x1 << 1 | 0x1 << 20 /* 0 1 3 5 9 13 15 16 17 20 22 31 */;
    s->pci_or_mpp_pads_calibration = 0xF << 0 | 0xF << 4 | 0xF << 8 | 0xF << 12 | 0x1 << 16 | 0x1 << 17 | 0x0 << 18 | 0x0 << 22 | 0x0 << 31;
    s->pci_command = 0x1 << 0 | 0x1 << 4 |  0x1 << 5 | 0x1 << 6 | 0x1 << 8 | 0x1 << 9 | 0x1 << 13 | 0x1 << 14 | 0x1 << 16 | 0x1 << 17 | 0x1 << 24 /* 0 1 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 24 26 28 29 */;
    s->pci_mode = 0x1 << 31 /* 0 2 3 4 6 8 9 31 */;
    s->pci_retry = 0x0 /* 0 16 24 */;
    s->pci_discard_timer = 0x0 /* 0 16 */;
    s->msi_trigger_timer = 0xFFFF << 0 | 0x0 << 16;
    s->pci_arbiter_control = 0x6 << 3 /* 0 1 2 3 7 14 21 31 */;
    s->pci_p2p_configuration = 0xFF << 0 | 0x0 << 16 | 0x0 << 24 | 0x0 << 29;
    s->pci_access_control_base_0_low = 0x0 /* 0 1 4 5 6 8 10 12 */;
    s->pci_access_control_base_0_high = 0x0 << 0;
    s->pci_access_control_size_0 = 0x0 /* 0 4 5 8 19 11 12 */;
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
    s->pci_configuration_address = 0x0 /* 0 2 8 11 16 24 31 */;
    s->pci_configuration_data = 0x0 << 0;
    s->pci_interrupt_acknowledge = 0x0 << 0;
    s->pci_serrn_mask = 0x0 /* 0 1 2 3 5 6 7 8 9 10 11 12 17 18 20 21 22 */;
    s->pci_interrupt_cause = 0x0 /* 0 24 25 26 27 */;
    s->pci_interrupt_mask = 0x0 /* 0 27 */;
    s->pci_error_address_low = 0x0 << 0;
    s->pci_error_address_high = 0x0 << 0;
    s->pci_error_command = 0x0 /* 0 4 5 */;
    s->pci_express_device_and_vendor_id_register = 0x11AB << 0 | 0x5181 << 16;
    s->pci_express_command_and_status_register = 0x1 << 20 /* 0 1 2 3 6 7 8 9 10 11 19 20 21 24 25 27 29 30 31 */;
    s->pci_express_class_code_and_revision_id_register = 0x3 << 0 | 0x80 << 16 | 0x05 << 24;
    s->pci_express_bist_header_type_and_cache_line_size_register = 0x0 /* 0 8 16 24 28 30 31 */;
    s->pci_express_bar0_internal_register = 0x0 << 0 | 0x2 << 1 | 0x1 << 3 | 0x0 << 4 | 0xD00 << 20;
    s->pci_express_bar0_internal_high_register = 0x0 << 0;
    s->pci_express_bar1_register = 0x0 << 0 | 0x2 << 1 | 0x1 << 3 | 0x0 << 4 | 0x0 << 16;
    s->pci_express_bar1_high_register = 0x0 << 0;
    s->pci_express_bar2_register = 0x0 << 0 | 0x2 << 1 | 0x1 << 3 | 0x0 << 4 | 0xF000 << 16;
    s->pci_express_bar2_high_register = 0x0 << 0;
    s->pci_express_subsystem_device_and_vendor_id = 0x11AB << 0 | 0x11AB << 16;
    s->pci_express_expansion_rom_bar_register = 0x0 /* 0 1 19 22 */;
    s->pci_express_capability_list_pointer_register = 0x40 << 0 | 0x0 << 8;
    s->pci_express_interrupt_pin_and_line_register = 0x0 << 0 | 0x1 << 8 | 0x0 << 16;
    s->pci_express_power_management_capability_header_register = 0x01 << 0 | 0x50 << 8 | 0x2 << 16 /* 0 8 16 19 21 22 25 26 27 */;
    s->pci_express_power_management_control_and_status_register = 0x0 /* 0 2 8 9 13 15 16 24 */;
    s->pci_express_msi_message_control_register = 0x5 << 0 | 0x60 << 8 | 0x1 << 23 /* 0 8 16 17 20 23 24 */;
    s->pci_express_msi_message_address_register = 0x0 << 0 | 0x0 << 2;
    s->pci_express_msi_message_address_high_register = 0x0 << 0;
    s->pci_express_msi_message_data_register = 0x0 << 0 | 0x0 << 16;
    s->pci_express_capability_register = 0x10 << 0 | 0x1 << 16 /* 0 8 16 20 24 25 30 */;
    s->pci_express_device_capabilities_register = 0x2 << 6 /* 0 3 6 9 12 13 14 15 18 26 28 */;
    s->pci_express_device_control_status_register = 0x2 << 12 /* 0 1 2 3 4 5 8 10 11 12 15 16 17 18 19 20 21 22 */;
    s->pci_express_link_capabilities_register = 0x1 << 0 | 0x0 << 4 | 0x1 << 10 | 0x0 << 12 | 0x7 << 15 | 0x0 << 18 | 0x0 << 24;
    s->pci_express_link_control_status_register = 0x1 << 3 | 0x1 << 16 | 0x1 << 28 /* 0 2 3 4 5 6 7 8 16 20 26 27 28 29 */;
    s->pci_express_advanced_error_report_header_register = 0x1 << 0 | 0x1 << 16 | 0x0 << 20;
    s->pci_express_uncorrectable_error_status_register = 0x0 /* 0 4 5 12 13 14 15 16 17 18 19 20 21 */;
    s->pci_express_uncorrectable_error_mask_register = 0x0 << 0;
    s->pci_express_uncorrectable_error_severity_register = 0x60010 << 0;
    s->pci_express_correctable_error_status_register = 0x0 /* 0 1 6 7 8 9 12 13 */;
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
    s->pci_express_interrupt_cause = 0x0 << 0 /* 0 1 2 3 4 5 8 9 10 11 12 13 16 17 18 19 20 21 22 23 24 25 26 27 28 */;
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
    s->pci_express_control_register = 0x1 << 0 | 0x1 << 3 | 0x3 << 8 | 0x14 << 16 /* 0 1 2 3 8 19 16 24 25 26 27 28 29 */;
    s->pci_express_status_register = 0x0 /* 0 1 5 8 16 21 24 25 26 27 28 */;
    s->pci_express_completion_timeout_register = 0x2710 << 0 | 0x0 << 16;
    s->pci_express_flow_control_register = 0x0 << 0 | 0x8 << 8 | 0x0 << 16 | 0x78 << 24;
    s->pci_express_acknowledge_timers_1x_register = 0x4 << 0 | 0x320 << 16;
    s->pci_express_debug_control_register = 0x0 << 0 | 0x1 << 16 | 0x17 << 1 | 0x0 << 0 | 0x1 << 19 | 0x0 << 20;
    s->pci_express_tl_control_register = 0x0 << 0;
    s->port0_usb_2_0_id = 0x0;
    s->port0_usb_2_0_hwgeneral = 0x0;
    s->port0_usb_2_0_hwhost = 0x0;
    s->port0_usb_2_0_hwdevice = 0x0;
    s->port0_usb_2_0_hwtxbuf = 0x0;
    s->port0_usb_2_0_hwrxbuf = 0x0;
    s->port0_usb_2_0_hwtttxbuf = 0x0;
    s->port0_usb_2_0_hwttrxbuf = 0x0;
    s->port0_usb_2_0_caplength = 0x0;
    s->port0_usb_2_0_hciversion = 0x0;
    s->port0_usb_2_0_hcsparams = 0x0;
    s->port0_usb_2_0_hccparams = 0x0;
    s->port0_usb_2_0_dciversion = 0x0;
    s->port0_usb_2_0_dccparams = 0x0;
    s->port0_usb_2_0_usbcmd = 0x0;
    s->port0_usb_2_0_usbsts = 0x0;
    s->port0_usb_2_0_usbintr = 0x0;
    s->port0_usb_2_0_frindex = 0x0;
    s->port0_usb_2_0_periodiclistbase__or__device_addr = 0x0;
    s->port0_usb_2_0_asynclistaddr__or__endpointlist_addr = 0x0;
    s->port0_usb_2_0_ttctrl = 0x0;
    s->port0_usb_2_0_burstsize = 0x0;
    s->port0_usb_2_0_txfilltuning = 0x0;
    s->port0_usb_2_0_txttfilltuning = 0x0;
    s->port0_usb_2_0_configflag = 0x0;
    s->port0_usb_2_0_portsc1 = 0x0;
    s->port0_usb_2_0_otgsc = 0x0;
    s->port0_usb_2_0_usbmode = 0x0;
    s->port0_usb_2_0_enpdtsetupstat = 0x0;
    s->port0_usb_2_0_endptprime = 0x0;
    s->port0_usb_2_0_endptflush = 0x0;
    s->port0_usb_2_0_endptstatus = 0x0;
    s->port0_usb_2_0_endptcomplete = 0x0;
    s->port0_usb_2_0_endptctrl0 = 0x0;
    s->port0_usb_2_0_endptctrl1 = 0x0;
    s->port0_usb_2_0_endptctrl2 = 0x0;
    s->port0_usb_2_0_endptctrl3 = 0x0;
    s->port0_usb_2_0_bridge_control_register = 0x0;
    s->port0_usb_2_0_bridge_interrupt_cause_register = 0x0;
    s->port0_usb_2_0_bridge_interrupt_mask_register = 0x0;
    s->port0_usb_2_0_bridge_error_address_register = 0x0;
    s->port0_usb_2_0_window0_control_register = 0x0;
    s->port0_usb_2_0_window0_base_register = 0x0;
    s->port0_usb_2_0_window1_control_register = 0x0;
    s->port0_usb_2_0_window1_base_register = 0x0;
    s->port0_usb_2_0_window2_control_register = 0x0;
    s->port0_usb_2_0_window2_base_register = 0x0;
    s->port0_usb_2_0_window3_control_register = 0x0;
    s->port0_usb_2_0_window3_base_register = 0x0;
    s->port0_usb_2_0_power_control_register = 0x0;
    s->phy_address = 0x0;
    s->smi = 0x0;
    s->ethernet_unit_default_address_euda = 0x0;
    s->ethernet_unit_default_id_eudid = 0x0;
    s->ethernet_unit_reserved_eu = 0x0;
    s->ethernet_unit_interrupt_cause_euic = 0x0;
    s->ethernet_unit_interrupt_mask_euim = 0x0;
    s->ethernet_unit_error_address_euea = 0x0;
    s->ethernet_unit_internal_address_error_euiae = 0x0;
    s->ethernet_unit_port_pads_calibration_eupcr = 0x0;
    s->ethernet_unit_control_euc = 0x0;
    s->base_address_0_ba0 = 0x0;
    s->size_s_0_sr0 = 0x0;
    s->base_address_1_ba1 = 0x0;
    s->size_s_1_sr1 = 0x0;
    s->base_address_2_ba2 = 0x0;
    s->size_s_2_sr2 = 0x0;
    s->base_address_3_ba3 = 0x0;
    s->size_s_3_sr3 = 0x0;
    s->base_address_4_ba4 = 0x0;
    s->size_s_4_sr4 = 0x0;
    s->base_address_5_ba5 = 0x0;
    s->size_s_5_sr5 = 0x0;
    s->high_address_remap_ha_harr0 = 0x0;
    s->high_address_remap_ha_harr1 = 0x0;
    s->high_address_remap_ha_harr2 = 0x0;
    s->high_address_remap_ha_harr3 = 0x0;
    s->base_address_enable_bare = 0x0;
    s->ethernet_port_access_protect_epap = 0x0;
    s->port_configuration_gec = 0x0;
    s->port_configuration_extend_gecx = 0x0;
    s->mii_serial_parameters = 0x0;
    s->gmii_serial_parameters = 0x0;
    s->vlan_ethertype_evlane = 0x0;
    s->mac_address_low_macal = 0x0;
    s->mac_address_high_macah = 0x0;
    s->sdma_configuration_sdc = 0x0;
    s->ip_differentiated_services_codepoint_0_to_priority_dscp0 = 0x0;
    s->ip_differentiated_services_codepoint_1_to_priority_dscp1 = 0x0;
    s->ip_differentiated_services_codepoint_2_to_priority_dscp2 = 0x0;
    s->ip_differentiated_services_codepoint_23_to_priority_dscp3 = 0x0;
    s->ip_differentiated_services_codepoint_24_to_priority_dscp4 = 0x0;
    s->ip_differentiated_services_codepoint_25_to_priority_dscp5 = 0x0;
    s->ip_differentiated_services_codepoint_6_to_priority_dscp6 = 0x0;
    s->port_serial_control_psc = 0x0;
    s->vlan_priority_tag_to_priority_vpt2p = 0x0;
    s->ethernet_port_status_ps = 0x0;
    s->transmit_queue_command_tqc = 0x0;
    s->maximum_transmit_unit_mtu = 0x0;
    s->port_interrupt_cause_ic = 0x0;
    s->port_interrupt_cause_extend_ice = 0x0;
    s->port_interrupt_mask_pim = 0x0;
    s->port_extend_interrupt_mask_peim = 0x0;
    s->port_rx_fifo_urgent_threshold_prfut = 0x0;
    s->port_tx_fifo_urgent_threshold_ptfut = 0x0;
    s->port_rx_minimal_frame_size_pmfs = 0x0;
    s->port_rx_discard_frame_counter_gedfc = 0x0;
    s->port_overrun_frame_counter_pofc = 0x0;
    s->port_internal_address_error_euiae = 0x0;
    s->ethernet_current_receive_descriptor_pointers_crdp_q0 = 0x0;
    s->ethernet_current_receive_descriptor_pointers_crdp_q1 = 0x0;
    s->ethernet_current_receive_descriptor_pointers_crdp_q2 = 0x0;
    s->ethernet_current_receive_descriptor_pointers_crdp_q3 = 0x0;
    s->ethernet_current_receive_descriptor_pointers_crdp_q4 = 0x0;
    s->ethernet_current_receive_descriptor_pointers_crdp_q5 = 0x0;
    s->ethernet_current_receive_descriptor_pointers_crdp_q6 = 0x0;
    s->ethernet_current_receive_descriptor_pointers_crdp_q7 = 0x0;
    s->receive_queue_command_rqc = 0x0;
    s->transmit_current_served_descriptor_pointer = 0x0;
    s->transmit_current_queue_descriptor_pointer_tcqdp_q0 = 0x0;
    s->transmit_queue_token_bucket_counter_tqxtbc_q0 = 0x0;
    s->transmit_queue_token_bucket_configuration_tqxtbc_q0 = 0x0;
    s->transmit_queue_arbiter_configuration_tqxac_q0 = 0x0;
    s->transmit_queue_token_bucket_counter_tqxtbc_q1 = 0x0;
    s->transmit_queue_token_bucket_configuration_tqxtbc_q1 = 0x0;
    s->transmit_queue_arbiter_configuration_tqxac_q1 = 0x0;
    s->transmit_queue_token_bucket_counter_tqxtbc_q2 = 0x0;
    s->transmit_queue_token_bucket_configuration_tqxtbc_q2 = 0x0;
    s->transmit_queue_arbiter_configuration_tqxac_q2 = 0x0;
    s->transmit_queue_token_bucket_counter_tqxtbc_q3 = 0x0;
    s->transmit_queue_token_bucket_configuration_tqxtbc_q3 = 0x0;
    s->transmit_queue_arbiter_configuration_tqxac_q3 = 0x0;
    s->transmit_queue_token_bucket_counter_tqxtbc_q4 = 0x0;
    s->transmit_queue_token_bucket_configuration_tqxtbc_q4 = 0x0;
    s->transmit_queue_arbiter_configuration_tqxac_q4 = 0x0;
    s->transmit_queue_token_bucket_counter_tqxtbc_q5 = 0x0;
    s->transmit_queue_token_bucket_configuration_tqxtbc_q5 = 0x0;
    s->transmit_queue_arbiter_configuration_tqxac_q5 = 0x0;
    s->transmit_queue_token_bucket_counter_tqxtbc_q6 = 0x0;
    s->transmit_queue_token_bucket_configuration_tqxtbc_q6 = 0x0;
    s->transmit_queue_arbiter_configuration_tqxac_q6 = 0x0;
    s->transmit_queue_token_bucket_counter_tqxtbc_q7 = 0x0;
    s->transmit_queue_token_bucket_configuration_tqxtbc_q7 = 0x0;
    s->transmit_queue_arbiter_configuration_tqxac_q7 = 0x0;
    s->mac_mib_countersnterrupt_cause_register = 0x0;
    s->destination_address_filter_special_multicast_table_dfsmt = 0x0;
    s->destination_address_filter_other_multicast_table_dfut = 0x0;
    s->destination_address_filter_unicast_table_dfut = 0x0;
    s->des_data_out_low_register = 0x0;
    s->des_data_out_high_register = 0x0;
    s->des_data_buffer_low_register = 0x0;
    s->des_data_buffer_high_register = 0x0;
    s->des_initial_value_low_register = 0x0;
    s->des_initial_value_high_register = 0x0;
    s->des_key0_low_register = 0x0;
    s->des_key0_high_register = 0x0;
    s->des_key1_low_register = 0x0;
    s->des_key1_high_register = 0x0;
    s->des_key2_low_register = 0x0;
    s->des_key2_high_register = 0x0;
    s->des_command_register = 0x0;
    s->sha_1_or_md5_data_in_register = 0x0;
    s->sha_1_or_md5_bit_count_low_register = 0x0;
    s->sha_1_or_md5_bit_count_high_register = 0x0;
    s->sha_1_or_md5_initial_value_or_digest_a_register = 0x0;
    s->sha_1_or_md5_initial_value_or_digest_b_register = 0x0;
    s->sha_1_or_md5_initial_value_or_digest_c_register = 0x0;
    s->sha_1_or_md5_initial_value_or_digest_d_register = 0x0;
    s->sha_1_initial_value_or_digest_e_register = 0x0;
    s->sha_1_or_md5_authentication_command_register = 0x0;
    s->aes_encryption_data_in_or_out_column_3_register = 0x0;
    s->aes_encryption_data_in_or_out_column_2_register = 0x0;
    s->aes_encryption_data_in_or_out_column_1_register = 0x0;
    s->aes_encryption_data_in_or_out_column_0_register = 0x0;
    s->aes_encryption_key_column_3_register = 0x0;
    s->aes_encryption_key_column_2_register = 0x0;
    s->aes_encryption_key_column_1_register = 0x0;
    s->aes_encryption_key_column_0_register = 0x0;
    s->aes_encryption_key_column_7_register = 0x0;
    s->aes_encryption_key_column_6_register = 0x0;
    s->aes_encryption_key_column_5_register = 0x0;
    s->aes_encryption_key_column_4_register = 0x0;
    s->aes_encryption_command_register = 0x0;
    s->aes_decryption_data_in_or_out_column_3_register = 0x0;
    s->aes_decryption_data_in_or_out_column_2_register = 0x0;
    s->aes_decryption_data_in_or_out_column_1_register = 0x0;
    s->aes_decryption_data_in_or_out_column_0_register = 0x0;
    s->aes_decryption_key_column_3_register = 0x0;
    s->aes_decryption_key_column_2_register = 0x0;
    s->aes_decryption_key_column_1_register = 0x0;
    s->aes_decryption_key_column_0_register = 0x0;
    s->aes_decryption_key_column_7_register = 0x0;
    s->aes_decryption_key_column_6_register = 0x0;
    s->aes_decryption_key_column_5_register = 0x0;
    s->aes_decryption_key_column_4_register = 0x0;
    s->aes_decryption_command_register = 0x0;
    s->security_accelerator_command_register = 0x0;
    s->security_accelerator_descriptor_pointer_session_0_register = 0x0;
    s->security_accelerator_descriptor_pointer_session_1_register = 0x0;
    s->security_accelerator_configuration_register = 0x0;
    s->security_accelerator_status_register = 0x0;
    s->cryptographic_engines_and_security_accelerator_interrupt_cause_register = 0x0;
    s->cryptographic_engines_and_security_accelerator_interrupt_mask_register = 0x0;
}

static void mv88f5181l_init(Object *obj) {
    MV88F5181LState *s = MV88F5181L(obj);

    /* initialize cpus and add the cpu as soc's child */
    s->cpu_type = ARM_CPU_TYPE_NAME("arm926");
    s->cpu = ARM_CPU(object_new(s->cpu_type));

    /* initialize bamboo device registers */
    /* initialize mv88f5181l_gpio registers */
    memory_region_init_io(&s->mv88f5181l_gpio_mmio, obj,
        &mv88f5181l_gpio_ops, s, TYPE_MV88F5181L, MV88F5181L_GPIO_MMIO_SIZE);
    sysbus_init_mmio(SYS_BUS_DEVICE(s), &s->mv88f5181l_gpio_mmio);
    
    /* initialize mv88f5181l_cpu_address_map registers */
    memory_region_init_io(&s->mv88f5181l_cpu_address_map_mmio, obj,
        &mv88f5181l_cpu_address_map_ops, s, TYPE_MV88F5181L, MV88F5181L_CPU_ADDRESS_MAP_MMIO_SIZE);
    sysbus_init_mmio(SYS_BUS_DEVICE(s), &s->mv88f5181l_cpu_address_map_mmio);
    
    /* initialize mv88f5181l_ddr_sdram_controller registers */
    memory_region_init_io(&s->mv88f5181l_ddr_sdram_controller_mmio, obj,
        &mv88f5181l_ddr_sdram_controller_ops, s, TYPE_MV88F5181L, MV88F5181L_DDR_SDRAM_CONTROLLER_MMIO_SIZE);
    sysbus_init_mmio(SYS_BUS_DEVICE(s), &s->mv88f5181l_ddr_sdram_controller_mmio);
    
    /* initialize mv88f5181l_pins_multiplexing_interface registers */
    memory_region_init_io(&s->mv88f5181l_pins_multiplexing_interface_mmio, obj,
        &mv88f5181l_pins_multiplexing_interface_ops, s, TYPE_MV88F5181L, MV88F5181L_PINS_MULTIPLEXING_INTERFACE_MMIO_SIZE);
    sysbus_init_mmio(SYS_BUS_DEVICE(s), &s->mv88f5181l_pins_multiplexing_interface_mmio);
    
    /* initialize mv88f5181l_pci_interface registers */
    memory_region_init_io(&s->mv88f5181l_pci_interface_mmio, obj,
        &mv88f5181l_pci_interface_ops, s, TYPE_MV88F5181L, MV88F5181L_PCI_INTERFACE_MMIO_SIZE);
    sysbus_init_mmio(SYS_BUS_DEVICE(s), &s->mv88f5181l_pci_interface_mmio);
    
    /* initialize mv88f5181l_pcie_interface registers */
    memory_region_init_io(&s->mv88f5181l_pcie_interface_mmio, obj,
        &mv88f5181l_pcie_interface_ops, s, TYPE_MV88F5181L, MV88F5181L_PCIE_INTERFACE_MMIO_SIZE);
    sysbus_init_mmio(SYS_BUS_DEVICE(s), &s->mv88f5181l_pcie_interface_mmio);
    
    /* initialize mv88f5181l_usb_2_0_controller registers */
    memory_region_init_io(&s->mv88f5181l_usb_2_0_controller_mmio, obj,
        &mv88f5181l_usb_2_0_controller_ops, s, TYPE_MV88F5181L, MV88F5181L_USB_2_0_CONTROLLER_MMIO_SIZE);
    sysbus_init_mmio(SYS_BUS_DEVICE(s), &s->mv88f5181l_usb_2_0_controller_mmio);
    
    /* initialize mv88f5181l_gigabit_ethernet_controller registers */
    memory_region_init_io(&s->mv88f5181l_gigabit_ethernet_controller_mmio, obj,
        &mv88f5181l_gigabit_ethernet_controller_ops, s, TYPE_MV88F5181L, MV88F5181L_GIGABIT_ETHERNET_CONTROLLER_MMIO_SIZE);
    sysbus_init_mmio(SYS_BUS_DEVICE(s), &s->mv88f5181l_gigabit_ethernet_controller_mmio);
    
    /* initialize mv88f5181l_cesa registers */
    memory_region_init_io(&s->mv88f5181l_cesa_mmio, obj,
        &mv88f5181l_cesa_ops, s, TYPE_MV88F5181L, MV88F5181L_CESA_MMIO_SIZE);
    sysbus_init_mmio(SYS_BUS_DEVICE(s), &s->mv88f5181l_cesa_mmio);
    

    /* initialize the interrupt controller */
    sysbus_init_child_obj(
        obj, "ic", &s->ic, sizeof(s->ic), TYPE_MV88F5181L_IC);

    /* initialize the bridge */
    sysbus_init_child_obj(
        obj, "bridge", &s->bridge, sizeof(s->bridge), TYPE_MV88F5181L_BRIDGE);

    /* initialize the timer */
    sysbus_init_child_obj(
        obj, "timer", &s->timer, sizeof(s->timer), TYPE_MV88F5181L_TIMER);

    object_property_add_const_link(OBJECT(&s->bridge), "timer", OBJECT(&s->timer), &error_abort);

    /* register reset for mv88f5181l */
    qemu_register_reset(mv88f5181l_reset, s);
}

static void mv88f5181l_realize(DeviceState *dev, Error **errp) {
    MV88F5181LState *s = MV88F5181L(dev);
    Error *err = NULL;

    /* realize the timer */
    object_property_set_bool(OBJECT(&s->timer), true, "realized", &err);
    if (err != NULL) {
        error_propagate(errp, err);
        return;
    }
    sysbus_mmio_map(SYS_BUS_DEVICE(&s->timer), 0, MV88F5181L_TIMER_MMIO_BASE);

    /* realize the bridge  */
    object_property_set_bool(OBJECT(&s->bridge), true, "realized", &err);
    if (err) {
        error_propagate(errp, err);
        return;
    }
    sysbus_mmio_map(SYS_BUS_DEVICE(&s->bridge), 0, MV88F5181L_BRIDGE_MMIO_BASE);

    /* realize the interrupt controller */
    object_property_set_bool(OBJECT(&s->ic), true, "realized", &err);
    if (err) {
        error_propagate(errp, err);
        return;
    }
    sysbus_mmio_map(SYS_BUS_DEVICE(&s->ic), 0, MV88F5181L_IC_MMIO_BASE);

    /* realize the cpu */
    object_property_set_bool(OBJECT(s->cpu), true, "realized", &err);
    if (err) {
        error_propagate(errp, err);
        return;
    }

    /* connect irq from the bridge to the interrupt controller */
    sysbus_connect_irq(SYS_BUS_DEVICE(&s->bridge), 0,
        qdev_get_gpio_in_named(DEVICE(&s->ic), MV88F5181L_IC_IRQ, 0));

    /* attach the uart to 16550A(8250) */
    if (serial_hd(0)) {
        serial_mm_init(get_system_memory(), MV88F5181L_UART_MMIO_BASE, 2,
                       qdev_get_gpio_in_named(DEVICE(&s->ic), MV88F5181L_IC_IRQ, 3),
                       115200, serial_hd(0), DEVICE_LITTLE_ENDIAN);
    }

    /* connect irq/fiq outputs from the interrupt controller to the cpu */
    qdev_connect_gpio_out_named(DEVICE(&s->ic), "irq", 0,
            qdev_get_gpio_in(DEVICE(s->cpu), ARM_CPU_IRQ));
}


static void mv88f5181l_class_init(ObjectClass *oc, void *data) {
    DeviceClass *dc = DEVICE_CLASS(oc);

    /* dc->fw_name = ; */
    /* dc->desc = ; */
    /* dc->props = ; */
    /* dc->user_creatable = ; */
    /* dc->hotpluggable = ; */
    /* dc->reset = ; */
    dc->realize = mv88f5181l_realize;
    /* dc->unrealize = ; */
    /* dc->vmsd = ; */
    /* dc->bus_type = ; */

    /* SysBusDeviceClass sbc = SYS_BUS_DEVICE_CLASS(klass); */

    /* sbc->explicit_ofw_unit_address = ; */
    /* sbc->connect_irq_notifier = ; */
}

static const TypeInfo mv88f5181l_type_info = {
    .name = TYPE_MV88F5181L,
    .parent = TYPE_SYS_BUS_DEVICE,
    .instance_size = sizeof(MV88F5181LState),
    .instance_init = mv88f5181l_init,
    /* .class_size = sizeof(SysBusDeviceClass), */
    .class_init = mv88f5181l_class_init,
};

static void mv88f5181l_register_types(void) {
    type_register_static(&mv88f5181l_type_info);
}

type_init(mv88f5181l_register_types);