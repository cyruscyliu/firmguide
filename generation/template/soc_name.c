{{license}}

#include "qemu/osdep.h"
#include "qapi/error.h"
#include "hw/arm/{{soc_name}}.h"


static void {{soc_name}}_init(Object *obj) {
    {{soc_name|upper}}State *s = {{soc_name|upper}}(obj);
    {{soc_name|upper}}Class *c = {{soc_name|upper}}_GET_CLASS(obj);

    /* initialize cpus and add the cpu as soc's child */
    object_initialize_child(obj, "cpu", &s->cpu,  sizeof(s->cpu), s->cpu_type, &error_abort, NULL);

    /* initialize peripherals and the peripherals as soc and sysbus's child */
    sysbus_init_child_obj(
        obj, "peripherals", &s->peripherals, sizeof(s->peripherals),
        TYPE_{{soc_name|upper}}_PERIPHERALS);
}

static void {{soc_name}}_realize(DeviceState *dev, Error **errp) {
    {{soc_name|upper}}State *s = {{soc_name|upper}}(obj);
    {{soc_name|upper}}Class *c = {{soc_name|upper}}_GET_CLASS(obj);
    Error *err = NULL;

    /* common peripherals */
    obj = object_property_get_link(OBJECT(dev), "ram", &err);
    if (obj == NULL) {
        error_setg(errp, "%s: required ram link not found : %s", __func__, error_get_pretty(err));
        return;
    }
    object_property_add_const_link(OBJECT(&s->peripherals), "ram", obj, &err);
     if (err) {
        error_propagate(errp, err);
        return;
    }

    /* realize the peripherals  */
    object_property_set_bool(OBJECT(&s->peripherals), true, "realized", &err);
    if (err) {
        error_propagate(errp, err);
        return;
    }

    /* register peripherals' mr */
    sysbus_mmio_map_overlap(SYS_BUS_DEVICE(&s->peripherals), 0, {{peripheral_name|upper}}_BASE, 1);

    /* realize the cpu */
    object_property_set_bool(OBJECT(&s->cpu), true, "realized", &err);
    if (err) {
        error_propagate(errp, err);
        return;
    }

    /* connect irq/fiq outputs from the interrupt controller to the cpu */
    qdev_connect_gpio_out_named(DEVICE(&s->ic), "irq", 0,
            qdev_get_gpio_in(DEVICE(&s->cpu), ARM_CPU_IRQ));
    qdev_connect_gpio_out_named(DEVICE(&s->ic), "fiq", 0,
            qdev_get_gpio_in(DEVICE(&s->cpu), ARM_CPU_FIQ));
}


static void {{soc_name}}_class_init(ObjectClass *oc, void *data) {
DeviceClass *dc = DEVICE_CLASS(oc);

/* dc->fw_name = ; */
/* dc->desc = ; */
/* dc->props = ; */
/* dc->user_creatable = ; */
/* dc->hotpluggable = ; */
/* dc->reset = ; */
dc->realize = {{soc_name}}_realize;
/* dc->unrealize = ; */
/* dc->vmsd = ; */
/* dc->bus_type = ; */
}

static const TypeInfo {{soc_name}}_type_info = {
.name = TYPE_{{soc_name|upper}},
.parent = TYPE_DEVICE,
.instance_size = sizeof({{soc_name|upper}}State),
.instance_init = {{soc_name}}_init,
/* .class_size = sizeof(DeviceClass), */
.class_init = {{soc_name}}_class_init,
};

static void {{soc_name}}_register_types= {
type_register_static(&{{soc_name}}_type_info);
}

type_init({{soc_name}}_register_types);