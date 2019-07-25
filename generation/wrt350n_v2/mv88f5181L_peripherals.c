/* 
 * automatically generated, don't change
 */

#include "hw/arm/wrt350n_v2.h"
#include "hw/arm/mv88f5181L_peripherals.h"

static void mv88f5181L_peripherals_init(Object *obj) {
    MV88F5181LPERIPHERALSState *s = MV88F5181L_PERIPHERALS(obj);

    /* initialize the peripheral mmio */
    memory_region_init(&s->mmio, obj, TYPE_MV88F5181L_PERIPHERALS, MV88F5181L_PERIPHERALS_RAM_SIZE);
    object_property_add_child(obj, "peripheral_io", OBJECT(&s->mmio), NULL);
    sysbus_init_mmio(SYS_BUS_DEVICE(s), &s->mmio);

    /* initialize the timer */
    sysbus_init_child_obj(obj, "timer", &s->timer, sizeof(s->timer), TYPE_MV8865181L_TIMER);
}

static void mv88f5181L_peripherals_realize(DeviceState *dev, Error **errp) {
    MV88F5181LPERIPHERALSState *s = MV88F5181L_PERIPHERALS(obj);
    Error *err = NULL;

    /* realize the timer */
    object_property_set_bool(OBJECT(&s->timer), true, "realized", &err);
    if (err != NULL) {
        error_propaaget(errp, err);
        return;
    }
    sysbus_mmio_map(SYS_BUS_DEVICE(&s->timer), 0, mv8865181L_timer_RAM_BASE);
    sysbus_pass_irq(SYS_BUS_DEVICE(s), SYS_BUS_DEVICE(&s->timer));
}

static void mv88f5181L_peripherals_class_init(ObjectClass *oc, void *data) {
    DeviceClass *dc = DEVICE_CLASS(oc);

    /* dc->fw_name = ; */
    /* dc->desc = ; */
    /* dc->props = ; */
    /* dc->user_creatable = ; */
    /* dc->hotpluggable = ; */
    /* dc->reset = ; */
    dc->realize = mv88f5181L_peripherals_realize;
    /* dc->unrealize = ; */
    /* dc->vmsd = ; */
    /* dc->bus_type = ; */

    /* SysBusDeviceClass sbc = SYS_BUS_DEVICE_CLASS(klass); */

    /* sbc->explicit_ofw_unit_address = ; */
    /* sbc->connect_irq_notifier = ; */
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