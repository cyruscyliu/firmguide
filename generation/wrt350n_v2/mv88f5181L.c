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
}

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
    s->ddr_sdram_configuration_register = 0x400 << 0 | 0x2 << 14 | 0x0 << 17 | 0x1 << 18 | 0x0 << 19 | 0x2 << 20 | 0x0 << 22 | 0x1 << 24 | 0x1 << 25 | 0x0 << 26;
    s->ddr_sdram_control_register = 0x0 << 0 | 0x1 << 6 | 0x0 << 7 | 0x1 << 12 | 0x0 << 13 | 0x0 << 14 | 0x1 << 18 | 0x0 << 19 | 0x3 << 24 | 0x0 << 28;
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
    Object *obj;

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
}

static const TypeInfo mv88f5181L_type_info = {
    .name = TYPE_MV88F5181L,
    .parent = TYPE_DEVICE,
    .instance_size = sizeof(MV88F5181LState),
    .instance_init = mv88f5181L_init,
    /* .class_size = sizeof(DeviceClass), */
    .class_init = mv88f5181L_class_init,
};

static void mv88f5181L_register_types(void) {
    type_register_static(&mv88f5181L_type_info);
}

type_init(mv88f5181L_register_types);