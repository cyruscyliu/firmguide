#include "qemu/osdep.h"
#include "qapi/error.h"
#include "hw/arm/{{soc_name}}.h"


static void {{soc_name}}_init(Object *obj) {
    {{soc_name|upper}}State *s = {{soc_name|upper}}(obj);
    {{soc_name|upper}}Class *c = {{soc_name|upper}}_GET_CLASS(obj);

    /* initialize cpus */
    int n;
    for (n = 0; n < {{soc_name|upper}}_NCPUS; n++) {
        object_initialize_child(
            obj, "cpu[*]", &s->cpus[n],  sizeof(s->cpus[n]),
            s->cpu_type, &error_abort, NULL);
    }
    /* initialize sysbus */
    sysbus_init_child_obj(
        obj, "control", &s->control, sizeof(s->control),
        TYPE_{{soc_name|upper}}_CONTROL);

    /* initialize peripherals */
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
        error_setg(
            errp, "%s: required ram link not found : %s",
            __func__, error_get_pretty(err));
        return;
    }
    object_property_add_const_link(OBJECT(&s->peripherals), "ram", obj, &err);
    ERROR_PROPAGET(errp, err);

    /* realize {{peripheral_name|upper}}State */
    object_property_set_bool(OBJECT(&s->peripherals), true, "realized", &err);
    ERROR_PROPAGET(errp, err);

}


static void {{soc_name}}_class_init(ObjectClass *oc, void *data) {
    DeviceClass *dc = DEVICE_CLASS(oc);
    {{soc_name|upper}}Class *mc = {{soc_name|upper}}_CLASS(oc);

    dc->realize = {{soc_name}}_realize;
    mc->name= "{{soc_name}}";
    mc->cpu_type = ARM_CPU_TYPE_NAME("{{cpu_type}}");
}

static const TypeInfo {{soc_name}}_type_info = {
    .name = TYPE_{{soc_name|upper}},
    .parent = TYPE_DEVICE,
    .instance_size = sizeof({{soc_name|upper}}State),
    .instance_init = {{soc_name}}_init,
    .class_size = sizeof({{soc_name|upper}}Class),
    .class_init = {{soc_name}}_class_init,
};

static void {{soc_name}}_register_types= {
    type_register_static(&{{soc_name}}_type_info);
}

type_init({{soc_name}}_register_types);