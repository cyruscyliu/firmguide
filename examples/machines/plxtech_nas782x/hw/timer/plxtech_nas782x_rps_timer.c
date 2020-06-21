/*
 * automatically generated, don't change
 */

#include "qemu/osdep.h"
#include "qemu/log.h"
#include "qapi/error.h"
#include "qemu/timer.h"
#include "hw/timer/plxtech_nas782x_rps_timer.h"

static void plxtech_nas782x_rps_timer_tick_callback0(void *opaque)
{
    PLXTECH_NAS782X_RPS_TIMERState *s = opaque;

    /* stupid timer */
    int64_t now = qemu_clock_get_ns(QEMU_CLOCK_VIRTUAL);
    timer_mod(s->timer[0], 1000000000 / 390625 + now); /* 390625HZ */
    /* 390625HZ -> 100HZ */
    if (s->counter[0] % (390625 / 100) == 0)
        qemu_set_irq(s->irq[0], 1);
    s->counter[0] &= ((1 << 24) - 1);
    s->counter[0]++;
}


static void plxtech_nas782x_rps_timer_update(void *opaque)
{
    /* PLXTECH_NAS782X_RPS_TIMERState *s = opaque; */
}

static uint64_t plxtech_nas782x_rps_timer_read(void *opaque, hwaddr offset, unsigned size)
{
    PLXTECH_NAS782X_RPS_TIMERState *s = opaque;
    uint32_t res = 0;

    switch (offset) {
        default:
            return 0;
        case 0x24:
            res = s->counter[0];
            res = ~res;
            break;
    }
    return res;
}

static void plxtech_nas782x_rps_timer_write(void *opaque, hwaddr offset, uint64_t val, unsigned size)
{
    PLXTECH_NAS782X_RPS_TIMERState *s = opaque;

    switch (offset) {
        default:
            return;
        case 0x0 ... 0x3c:
            s->reserved = val;
            break;
    }
    plxtech_nas782x_rps_timer_update(s);
}

static const MemoryRegionOps plxtech_nas782x_rps_timer_ops = {
    .read = plxtech_nas782x_rps_timer_read,
    .write = plxtech_nas782x_rps_timer_write,
    .endianness = DEVICE_LITTLE_ENDIAN,
};

static void plxtech_nas782x_rps_timer_init(Object *obj)
{
    PLXTECH_NAS782X_RPS_TIMERState *s = PLXTECH_NAS782X_RPS_TIMER(obj);

    /* initialize the mmio */
    memory_region_init_io(&s->mmio, obj, &plxtech_nas782x_rps_timer_ops, s, TYPE_PLXTECH_NAS782X_RPS_TIMER, 0x40);
    sysbus_init_mmio(SYS_BUS_DEVICE(s), &s->mmio);

    /* initialize an irq to the intc */
    qdev_init_gpio_out(DEVICE(s), s->irq, 1);

    /* initialize the timer */
    s->timer[0] = timer_new_ns(QEMU_CLOCK_VIRTUAL, plxtech_nas782x_rps_timer_tick_callback0, s);
}

static void plxtech_nas782x_rps_timer_reset(DeviceState *dev)
{
    PLXTECH_NAS782X_RPS_TIMERState *s = PLXTECH_NAS782X_RPS_TIMER(dev);
    int64_t now;
    
    now = qemu_clock_get_ns(QEMU_CLOCK_VIRTUAL);
    timer_mod(s->timer[0], 0x10000000 + now); /* 100HZ */
    s->counter[0] = 0;
    s->reserved = 0;
}

static void plxtech_nas782x_rps_timer_class_init(ObjectClass *klass, void *data)
{
    DeviceClass *dc = DEVICE_CLASS(klass);

    dc->reset = plxtech_nas782x_rps_timer_reset;
}

static TypeInfo plxtech_nas782x_rps_timer_type_info = {
    .name = TYPE_PLXTECH_NAS782X_RPS_TIMER,
    .parent = TYPE_SYS_BUS_DEVICE,
    .instance_size = sizeof(PLXTECH_NAS782X_RPS_TIMERState),
    .instance_init = plxtech_nas782x_rps_timer_init,
    /* .class_size = sizeof(SysBusDeviceClass), */
    .class_init = plxtech_nas782x_rps_timer_class_init,
};

static void plxtech_nas782x_rps_timer_register_types(void)
{
    type_register_static(&plxtech_nas782x_rps_timer_type_info);
}

type_init(plxtech_nas782x_rps_timer_register_types)
