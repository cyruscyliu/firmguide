/* 
 * automatically generated, don't change
 */

#include "qemu/osdep.h"
#include "qapi/error.h"
#include "target/arm/cpu.h"
#include "hw/arm/mv88f5181L.h"

static void mv88f5181_cpu_address_map_update(void *opaque);
static uint64_t mv88f5181_cpu_address_map_read(void *opaque, hwaddr offset, unsigned size);
static void mv88f5181_cpu_address_map_write(void *opaque, hwaddr offset, uint64_t val, unsigned size);

static void mv88f5181L_init(Object *obj);
static void mv88f5181L_realize(DeviceState *dev, Error **errp);
static void mv88f5181_cpu_address_map_reset(DeviceState *d);

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

static void mv88f5181_cpu_address_map_reset(DeviceState *d) {
    MV88F5181LState *s = MV88F5181L(d);
    
    s->window0_control_register = 0;
    s->window0_base_register = 0;
    s->window0_remap_low_register = 0;
    s->window0_remap_high_register = 0;
    s->window1_control_register = 0;
    s->window1_base_register = 0;
    s->window1_remap_low_register = 0;
    s->window1_remap_high_register = 0;
    s->window2_control_register = 0;
    s->window2_base_register = 0;
    s->window2_remap_low_register = 0;
    s->window2_remap_high_register = 0;
    s->window3_control_register = 0;
    s->window3_base_register = 0;
    s->window4_control_register = 0;
    s->window4_base_register = 0;
    s->window5_control_register = 0;
    s->window5_base_register = 0;
    s->window6_control_register = 0;
    s->window6_base_register = 0;
    s->window7_control_register = 0;
    s->window7_base_register = 0;
    s->_88f5181_internal_registers_base_address_register = 0;
}

static void mv88f5181L_init(Object *obj) {
    MV88F5181LState *s = MV88F5181L(obj);

    /* initialize cpus and add the cpu as soc's child */
    s->cpu_type = ARM_CPU_TYPE_NAME("arm926");
    s->cpu = ARM_CPU(object_new(s->cpu_type));

    /* initialize cpu address map registers */
    memory_region_init_io(&s->cpu_address_map_mmio, obj,
        &mv88f5181_cpu_address_map_ops, s, TYPE_MV88F5181L, MV88F5181_CPU_ADDRESS_MAP_RAM_SIZE);
    sysbus_init_mmio(SYS_BUS_DEVICE(s), &s->cpu_address_map_mmio);

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
    dc->reset = mv88f5181_cpu_address_map_reset; */
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