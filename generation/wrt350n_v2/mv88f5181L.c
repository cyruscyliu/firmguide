/* 
 * automatically generated, don't change
 */

#include "qemu/osdep.h"
#include "qapi/error.h"
#include "hw/arm/mv88f5181L.h"


static void mv88f5181L_init(Object *obj) {
    MV88F5181LState *s = MV88F5181L(obj);
    MV88F5181LClass *c = MV88F5181L_GET_CLASS(obj);

    /* initialize cpus and add the cpu as soc's child */
    object_initialize_child(obj, "cpu", &s->cpu,  sizeof(s->cpu), s->cpu_type, &error_abort, NULL);

    /* initialize peripherals and the peripherals as soc and sysbus's child */
    sysbus_init_child_obj(
        obj, "peripherals", &s->peripherals, sizeof(s->peripherals),
        TYPE_MV88F5181L_PERIPHERALS);

    /* initialize the interrupt controller */
    object_initialize(&s->ic, sizeof(s->ic), TYPE_mv88f5181L_ic);
    object_property_add_child(obj, "ic", OBJECT(&s->ic), NULL);
    qdev_set_parent_bus(DEVICE(&s->ic), sysbus_get_default());
}

static void mv88f5181L_realize(DeviceState *dev, Error **errp) {
    MV88F5181LState *s = MV88F5181L(obj);
    MV88F5181LClass *c = MV88F5181L_GET_CLASS(obj);
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
    sysbus_mmio_map_overlap(SYS_BUS_DEVICE(&s->peripherals), 0, MV88F5181L_PERIPHERALS_BASE, 1);

    /* realize the cpu */
    object_property_set_bool(OBJECT(&s->cpu), true, "realized", &err);
    if (err) {
        error_propagate(errp, err);
        return;
    }

    /* realize the local interrupt controller */
    object_property_set_bool(OBJECT(&s->ic), true, "realized", &err);
    if (err) {
        error_propagate(errp, err);
        return;
    }

    memory_region_add_subregion(&s->peri_mr, MV88F5181L_IC_OFFSET,
        sysbus_mmio_get_region(SYS_BUS_DEVICE(&s->ic), 0));
    sysbus_pass_irq(SYS_BUS_DEVICE(s), SYS_BUS_DEVICE(&s->ic));
    /* connect irq/fiq outputs from the interrupt controller to the cpu */
    qdev_connect_gpio_out_named(DEVICE(&s->ic), "irq", 0,
            qdev_get_gpio_in(DEVICE(&s->cpu), ARM_CPU_IRQ));
    qdev_connect_gpio_out_named(DEVICE(&s->ic), "fiq", 0,
            qdev_get_gpio_in(DEVICE(&s->cpu), ARM_CPU_FIQ));
}


static void mv88f5181L_class_init(ObjectClass *oc, void *data) {
DeviceClass *dc = DEVICE_CLASS(oc);

/* dc->fw_name = ; */
/* dc->desc = ; */
/* dc->props = ; */
/* dc->user_creatable = ; */
/* dc->hotpluggable = ; */
/* dc->reset = ; */
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

static void mv88f5181L_register_types= {
type_register_static(&mv88f5181L_type_info);
}

type_init(mv88f5181L_register_types);