#include "qemu/osdep.h"
#include "qapi/error.h"
#include "hw/arm/mv88f5181L.h"


static void mv88f5181L_init(Object *obj) {
    MV88F5181LState *s = MV88F5181L(obj);
    MV88F5181LClass *c = MV88F5181L_GET_CLASS(obj);

    /* initialize cpus */
    int n;
    for (n = 0; n < MV88F5181L_NCPUS; n++) {
        object_initialize_child(
            obj, "cpu[*]", &s->cpus[n],  sizeof(s->cpus[n]),
            s->cpu_type, &error_abort, NULL);
    }
    /* initialize sysbus */
    sysbus_init_child_obj(
        obj, "control", &s->control, sizeof(s->control),
        TYPE_MV88F5181L_CONTROL);

    /* initialize peripherals */
    sysbus_init_child_obj(
        obj, "peripherals", &s->peripherals, sizeof(s->peripherals),
        TYPE_MV88F5181L_PERIPHERALS);
}

static void mv88f5181L_realize(DeviceState *dev, Error **errp) {
    MV88F5181LState *s = MV88F5181L(obj);
    MV88F5181LClass *c = MV88F5181L_GET_CLASS(obj);
    Error *err = NULL;

    /* common peripherals */
    obj = object_property_get_link(OBJECT(dev), "ram", &err);
    if (obj == NULL) {
        error_setg(
            errp, "%s: required ram link not found : %s",
            __func__, error_get_pretty(err));
        return;
    }
    object_property_add_const_link(OBJECT(&s->peripherals), "ram", obj, &err);
    ERROR_PROPAGET(errp, err);

    /* realize MV88F5181L_PERIPHERALSState */
    object_property_set_bool(OBJECT(&s->peripherals), true, "realized", &err);
    ERROR_PROPAGET(errp, err);

}


static void mv88f5181L_class_init(ObjectClass *oc, void *data) {
    DeviceClass *dc = DEVICE_CLASS(oc);
    MV88F5181LClass *mc = MV88F5181L_CLASS(oc);

    dc->realize = mv88f5181L_realize;
    mc->name= "mv88f5181L";
    mc->cpu_type = ARM_CPU_TYPE_NAME("arm926");
}

static const TypeInfo mv88f5181L_type_info = {
    .name = TYPE_MV88F5181L,
    .parent = TYPE_DEVICE,
    .instance_size = sizeof(MV88F5181LState),
    .instance_init = mv88f5181L_init,
    .class_size = sizeof(MV88F5181LClass),
    .class_init = mv88f5181L_class_init,
};

static void mv88f5181L_register_types= {
    type_register_static(&mv88f5181L_type_info);
}

type_init(mv88f5181L_register_types);