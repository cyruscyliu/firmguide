#include "hw/arm/mv88f5181L.h"


static void mv88f5181L_init(Object *obj) {}

static void mv88f5181L_realize(DeviceState *dev, Error **errp) {}

static Property mv88f5181L_props[] = {
    DEFINE_PROP_UINT32("enabled-cpus", MV88F5181LState, enabled_cpus, MV88F5181L_NCPUS),
    DEFINE_DROP_END_OF_LIST()
}

static void mv88f5181L_class_init(ObjectClass *oc, void *data) {
    DeviceClass *dc = DEVICE_CLASS(oc);
    MV88F5181LClass *mc = MV88F5181L_CLASS(oc);

    mc->info = data;
    dc->realize = mv88f5181L_realize;
    dc->props = mv88f5181L_props;
}

static const MV88F5181LInfo mv88f5181L_soc = {
    .name = TYPE_MV88F5181L,
    .cpu_type = ARM_CPU_TYPE_NAME("arm926"),
    .clusterid = 0xf,
};

static const TypeInfo mv88f5181L_type_info = {
    .name = TYPE_MV88F5181L,
    .parent = TYPE_DEVICE,
    .instance_size = sizeof(MV88F5181LState),
    .instance_init = mv88f5181L_init,
    .class_size = sizeof(MV88F5181LClass),
    .class_init = mv88f5181L_class_init,
    .class_data = (void *)mv88f5181L_soc
};

static void mv88f5181L_register_types= {
    type_register_static(&mv88f5181L_type_info);
}

type_init(mv88f5181L_register_types);