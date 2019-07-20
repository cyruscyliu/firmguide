#include "hw/arm/mv88f5181L_peripherals.h"

static void mv88f5181L_peripherals_init(Object *obj) {
    MV88F5181L_PERIPHERALSState *s = MV88F5181L_PERIPHERALS(obj);

    /* initialize the ram for peripheral devices */
    memory_region_init(&s->peri_mr, obj, TYPE_MV88F5181L_PERIPHERALS, 0x10000000);
    object_property_add_child(obj, "peripheral-io", OBJECT(&s->peri_mr), NULL);
    sysbus_init_mmio(SYS_BUS_DEVICE(s), &s->peri_mr);

    /* initialize the interrupt controller */
    object_initialize(&s->ic, sizeof(s->ic), TYPE_mv88f5181L_ic);
    object_property_add_child(obj, "ic", OBJECT(&s->ic), NULL);
    qdev_set_parent_bus(DEVICE(&s->ic), sysbus_get_default());

    /* initialize the GPIO */
    object_initialize(&s->gpio, sizeof(s->gpio),  TYPE_mv88f5181L_gpio);
    object_property_add_child(obj, "gpio", OBJECT(&s->gpio), NULL);
    qdev_set_parent_bus(DEVICE(&s->gpio), sysbus_get_default());
}

static void mv88f5181L_peripherals_realize(DeviceState *dev, Error **errp) {
    MV88F5181L_PERIPHERALSState *s = MV88F5181L_PERIPHERALS(obj);

    /* realize the interrupt controller */
    object_property_set_bool(OBJECT(&s->ic), true, "realized", &err);
    if (err) {
        error_propagate(errp, err);
        return;
    }
    memory_region_add_subregion(&s->peri_mr, MV88F5181L_IC_OFFSET,
        sysbus_mmio_get_region(SYS_BUS_DEVICE(&s->ic), 0));
    sysbus_pass_irq(SYS_BUS_DEVICE(s), SYS_BUS_DEVICE(&s->ic));

    /* realize the gpio */
    object_property_set_bool(OBJECT(&s->gpio), true, "realized", &err);
    if (err) {
        error_propagate(errp, err);
        return;
    }
    memory_region_add_subregion(&s->peri_mr, "MV88F5181L_GPIO"_OFFSET,
        sysbus_mmio_get_region(SYS_BUS_DEVICE(&s->gpio), 0));
    if (err) {
        error_propagate(errp, err);
        return;
    }
}

static void mv88f5181L_peripherals_class_init(ObjectClass *oc, void *data) {
    DeviceClass *dc = DEVICE_CLASS(oc);

    dc->realize = mv88f5181L_peripherals_realize;
}

static const TypeInfo mv88f5181L_peripherals_type_info = {
    .name = TYPE_MV88F5181L_PERIPHERALS,
    .parent = TYPE_SYS_BUS_DEVICE,
    .instance_size = sizeof(MV88F5181L_PERIPHERALSState),
    .instance_init = mv88f5181L_peripherals_init,
    /* .class_size = sizeof(SysBusDeviceClass), */
    .class_init = mv88f5181L_peripherals_class_init,
}

static void mv88f5181L_peripherals_register_types(void) {
    type_register_static(&mv88f5181L_peripherals_type_info);
}

type_init(mv88f5181L_peripherals_register_types)