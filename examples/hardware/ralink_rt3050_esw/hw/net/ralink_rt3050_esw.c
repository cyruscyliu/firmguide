/*
 * simple dual state machine
 * state=0
 *    read       then state=0
 *    write pcr0 then state=1
 * state=1
 *    read pcr0  then state=0
 *    write      then state=1
 */

#include "qemu/osdep.h"
#include "qemu/log.h"
#include "qapi/error.h"
#include "hw/net/ralink_rt3050_esw.h"


static uint64_t ralink_rt3050_esw_read(void *opaque, hwaddr offset, unsigned size)
{
    RALINK_RT3050_ESWState *s = opaque;
    uint32_t res = 0;

    switch (offset) {
        default:
            return 0;
        case 0xc4:
            if (s->pcr0 == 1) {
                res = 1;
                s->pcr0 = 0;
            } else {
                res = 0;
            }
    }
    return res;
}

static void ralink_rt3050_esw_write(void *opaque, hwaddr offset, uint64_t val, unsigned size)
{
    RALINK_RT3050_ESWState *s = opaque;

    switch (offset) {
        default:
            return;
        case 0xc0:
            s->pcr0 = 1;
    }
}

static const MemoryRegionOps ralink_rt3050_esw_ops = {
    .read = ralink_rt3050_esw_read,
    .write = ralink_rt3050_esw_write,
    .endianness = {{ endian|to_endian }},
};

static void ralink_rt3050_esw_init(Object *obj)
{
    RALINK_RT3050_ESWState *s = RALINK_RT3050_ESW(obj);

    /* initialize the mmio */
    memory_region_init_io(&s->mmio, obj, &ralink_rt3050_esw_ops, s, TYPE_RALINK_RT3050_ESW, {{ reg.size|to_hex }});
    sysbus_init_mmio(SYS_BUS_DEVICE(s), &s->mmio);
}

static void ralink_rt3050_esw_reset(DeviceState *dev)
{
    RALINK_RT3050_ESWState *s = RALINK_RT3050_ESW(dev);

    s->pcr0 = 0;
}

static void ralink_rt3050_esw_class_init(ObjectClass *klass, void *data)
{
    DeviceClass *dc = DEVICE_CLASS(klass);

    dc->reset = ralink_rt3050_esw_reset;
}

static TypeInfo ralink_rt3050_esw_type_info = {
    .name = TYPE_RALINK_RT3050_ESW,
    .parent = TYPE_SYS_BUS_DEVICE,
    .instance_size = sizeof(RALINK_RT3050_ESWState),
    .instance_init = ralink_rt3050_esw_init,
    /* .class_size = sizeof(SysBusDeviceClass), */
    .class_init = ralink_rt3050_esw_class_init,
};

static void ralink_rt3050_esw_register_types(void)
{
    type_register_static(&ralink_rt3050_esw_type_info);
}

type_init(ralink_rt3050_esw_register_types)
