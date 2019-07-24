{{license}}

#include "hw/arm/{{peripheral_name}}.h"

static void {{peripheral_name}}_init(Object *obj) {
    {{peripheral_name|upper}}State *s = {{peripheral_name|upper}}(obj);

    /* initialize the ram for peripheral devices */
    memory_region_init(&s->peri_mr, obj, TYPE_{{peripheral_name|upper}}, {{peripheral_ram_size}});
    object_property_add_child(obj, "peripheral-io", OBJECT(&s->peri_mr), NULL);
    sysbus_init_mmio(SYS_BUS_DEVICE(s), &s->peri_mr);

    /* initialize the interrupt controller */
    object_initialize(&s->ic, sizeof(s->ic), TYPE_{{ic_name}});
    object_property_add_child(obj, "ic", OBJECT(&s->ic), NULL);
    qdev_set_parent_bus(DEVICE(&s->ic), sysbus_get_default());
}

static void {{peripheral_name}}_realize(DeviceState *dev, Error **errp) {
    {{peripheral_name|upper}}State *s = {{peripheral_name|upper}}(obj);

    /* realize the interrupt controller */
    object_property_set_bool(OBJECT(&s->ic), true, "realized", &err);
    if (err) {
        error_propagate(errp, err);
        return;
    }
    memory_region_add_subregion(&s->peri_mr, {{ic_name|upper}}_OFFSET,
        sysbus_mmio_get_region(SYS_BUS_DEVICE(&s->ic), 0));
    sysbus_pass_irq(SYS_BUS_DEVICE(s), SYS_BUS_DEVICE(&s->ic));
}

static void {{peripheral_name}}_class_init(ObjectClass *oc, void *data) {
    DeviceClass *dc = DEVICE_CLASS(oc);

    /* dc->fw_name = ; */
    /* dc->desc = ; */
    /* dc->props = ; */
    /* dc->user_creatable = ; */
    /* dc->hotpluggable = ; */
    /* dc->reset = ; */
    dc->realize = {{peripheral_name}}_realize;
    /* dc->unrealize = ; */
    /* dc->vmsd = ; */
    /* dc->bus_type = ; */

    /* SysBusDeviceClass sbc = SYS_BUS_DEVICE_CLASS(klass); */

    /* sbc->explicit_ofw_unit_address = ; */
    /* sbc->connect_irq_notifier = ; */
}

static const TypeInfo {{peripheral_name}}_type_info = {
    .name = TYPE_{{peripheral_name|upper}},
    .parent = TYPE_SYS_BUS_DEVICE,
    .instance_size = sizeof({{peripheral_name|upper}}State),
    .instance_init = {{peripheral_name}}_init,
    /* .class_size = sizeof(SysBusDeviceClass), */
    .class_init = {{peripheral_name}}_class_init,
}

static void {{peripheral_name}}_register_types(void) {
    type_register_static(&{{peripheral_name}}_type_info);
}

type_init({{peripheral_name}}_register_types)