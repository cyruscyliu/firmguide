/*
 * automatically generated, don't change
 */

#include "qemu/osdep.h"
#include "qemu/log.h"
#include "qapi/error.h"
#include "qemu/timer.h"
#include "hw/timer/ralink_rt2880_timer.h"

static void ralink_rt2880_timer_tick_callback0(void *opaque)
{
    RALINK_RT2880_TIMERState *s = opaque;

    /* stupid timer */
    int64_t now = qemu_clock_get_ns(QEMU_CLOCK_VIRTUAL);
    timer_mod(s->timer[0], 1000000000 / 1000000 + now); /* 1000000HZ */
    /* 1000000HZ -> 100HZ */
    if (s->counter[0] % (1000000 / 100) == 0)
        qemu_set_irq(s->irq[0], 1);
    s->counter[0] &= ((1 << 32) - 1);
    s->counter[0]++;
}


static void ralink_rt2880_timer_update(void *opaque)
{
    /* RALINK_RT2880_TIMERState *s = opaque; */
}

static uint64_t ralink_rt2880_timer_read(void *opaque, hwaddr offset, unsigned size)
{
    RALINK_RT2880_TIMERState *s = opaque;
    uint32_t res = 0;

    switch (offset) {
        default:
            return 0;
            break;
    }
    return res;
}

static void ralink_rt2880_timer_write(void *opaque, hwaddr offset, uint64_t val, unsigned size)
{
    RALINK_RT2880_TIMERState *s = opaque;

    switch (offset) {
        default:
            return;
        case 0x0 ... 0x1c:
            s->reserved = val;
            break;
    }
    ralink_rt2880_timer_update(s);
}

static const MemoryRegionOps ralink_rt2880_timer_ops = {
    .read = ralink_rt2880_timer_read,
    .write = ralink_rt2880_timer_write,
    .endianness = DEVICE_LITTLE_ENDIAN,
};

static void ralink_rt2880_timer_init(Object *obj)
{
    RALINK_RT2880_TIMERState *s = RALINK_RT2880_TIMER(obj);

    /* initialize the mmio */
    memory_region_init_io(&s->mmio, obj, &ralink_rt2880_timer_ops, s, TYPE_RALINK_RT2880_TIMER, 0x20);
    sysbus_init_mmio(SYS_BUS_DEVICE(s), &s->mmio);

    /* initialize an irq to the intc */
    qdev_init_gpio_out(DEVICE(s), s->irq, 1);

    /* initialize the timer */
    s->timer[0] = timer_new_ns(QEMU_CLOCK_VIRTUAL, ralink_rt2880_timer_tick_callback0, s);
}

static void ralink_rt2880_timer_reset(DeviceState *dev)
{
    RALINK_RT2880_TIMERState *s = RALINK_RT2880_TIMER(dev);
    int64_t now;
    
    now = qemu_clock_get_ns(QEMU_CLOCK_VIRTUAL);
    timer_mod(s->timer[0], 0x10000000 + now); /* 100HZ */
    s->counter[0] = 0;
    s->reserved = 0;
}

static void ralink_rt2880_timer_class_init(ObjectClass *klass, void *data)
{
    DeviceClass *dc = DEVICE_CLASS(klass);

    dc->reset = ralink_rt2880_timer_reset;
}

static TypeInfo ralink_rt2880_timer_type_info = {
    .name = TYPE_RALINK_RT2880_TIMER,
    .parent = TYPE_SYS_BUS_DEVICE,
    .instance_size = sizeof(RALINK_RT2880_TIMERState),
    .instance_init = ralink_rt2880_timer_init,
    /* .class_size = sizeof(SysBusDeviceClass), */
    .class_init = ralink_rt2880_timer_class_init,
};

static void ralink_rt2880_timer_register_types(void)
{
    type_register_static(&ralink_rt2880_timer_type_info);
}

type_init(ralink_rt2880_timer_register_types)
