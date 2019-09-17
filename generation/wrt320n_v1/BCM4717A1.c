/* 
 * automatically generated, don't change
 */

#include "qemu/osdep.h"
#include "qemu/log.h"
#include "qapi/error.h"
#include "target/mips/cpu.h"
#include "hw/mips/BCM4717A1.h"
#include "hw/char/serial.h"
#include "exec/address-spaces.h"

static void BCM4717A1_init(Object *obj);
static void BCM4717A1_realize(DeviceState *dev, Error **errp);
static void BCM4717A1_reset(void *opaque);

static void BCM4717A1_class_init(ObjectClass *oc, void *data);
static void BCM4717A1_register_types(void);

static void BCM4717A1_reset(void *opaque)
{
    BCM4717A1State *s = opaque;
}

static void BCM4717A1_init(Object *obj) 
{
    BCM4717A1State *s = BCM4717A1(obj);

    /* initialize cpus and add the cpu as soc's child */
    s->cpu_type = MIPS_CPU_TYPE_NAME("74Kf");
    s->cpu = MIPS_CPU(object_new(s->cpu_type));

    
    /* initialize the bridge */
    sysbus_init_child_obj(obj, "bridge", &s->bridge, sizeof(s->bridge), TYPE_BCMA);
    
    /* reset */
    BCM4717A1_reset(s);
}

static void BCM4717A1_realize(DeviceState *dev, Error **errp) 
{
    BCM4717A1State *s = BCM4717A1(dev);

    Error *err = NULL;
    /* realize the cpu */
    object_property_set_bool(OBJECT(s->cpu), true, "realized", &err);
    if (err) {
        error_propagate(errp, err);
        return;
    }

    
    /* realize the bridge  */
    object_property_set_bool(OBJECT(&s->bridge), true, "realized", &err);
    if (err) {
        error_propagate(errp, err);
        return;
    }
    sysbus_mmio_map_overlap(SYS_BUS_DEVICE(&s->bridge), 0, BCMA_MMIO_BASE, 1);
}

static void BCM4717A1_class_init(ObjectClass *oc, void *data) 
{
    DeviceClass *dc = DEVICE_CLASS(oc);

    /* dc->fw_name = ; */
    /* dc->desc = ; */
    /* dc->props = ; */
    /* dc->user_creatable = ; */
    /* dc->hotpluggable = ; */
    /* dc->reset = ; */
    dc->realize = BCM4717A1_realize;
    /* dc->unrealize = ; */
    /* dc->vmsd = ; */
    /* dc->bus_type = ; */

    /* SysBusDeviceClass sbc = SYS_BUS_DEVICE_CLASS(klass); */

    /* sbc->explicit_ofw_unit_address = ; */
    /* sbc->connect_irq_notifier = ; */
}

static const TypeInfo BCM4717A1_type_info = {
    .name = TYPE_BCM4717A1,
    .parent = TYPE_SYS_BUS_DEVICE,
    .instance_size = sizeof(BCM4717A1State),
    .instance_init = BCM4717A1_init,
    /* .class_size = sizeof(SysBusDeviceClass), */
    .class_init = BCM4717A1_class_init,
};

static void BCM4717A1_register_types(void) 
{
    type_register_static(&BCM4717A1_type_info);
}

type_init(BCM4717A1_register_types);
