/*
 * automatically generated, don't change
 */

#include "qemu/osdep.h"
#include "qemu/log.h"
#include "qapi/error.h"
#include "hw/timer/ralink_rt2880_timer.h"

static void ralink_rt2880_timer_clksrc_callback0(void *opaque)
{
    /* RALINK_RT2880_TIMERState *s = opaque; */
}

static void ralink_rt2880_timer_clkevt_callback0(void *opaque)
{
    RALINK_RT2880_TIMERState *s = opaque;

    int64_t now = qemu_clock_get_ns(QEMU_CLOCK_VIRTUAL);
    timer_mod(s->timer[0], 10000000 + now); /* 100HZ */
    qemu_set_irq(s->irq[0], 1);
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
    QEMUBH *bh[1];

    /* initialize the mmio */
    memory_region_init_io(&s->mmio, obj, &ralink_rt2880_timer_ops, s, TYPE_RALINK_RT2880_TIMER, 0x20);
    sysbus_init_mmio(SYS_BUS_DEVICE(s), &s->mmio);

    /* initialize an irq to the intc */
    qdev_init_gpio_out(DEVICE(s), s->irq, 1);

    /* initialize the timer */
    bh[0] = qemu_bh_new(ralink_rt2880_timer_clksrc_callback0, s);
    s->ptimer[0] = ptimer_init(bh[0], PTIMER_POLICY_DEFAULT);
    s->timer[0] = timer_new_ns(QEMU_CLOCK_VIRTUAL, ralink_rt2880_timer_clkevt_callback0, s);
}

static void ralink_rt2880_timer_reset(DeviceState *dev)
{
    RALINK_RT2880_TIMERState *s = RALINK_RT2880_TIMER(dev);
    
    ptimer_set_freq(s->ptimer[0], 1000000);
    ptimer_set_limit(s->ptimer[0], (uint32_t)((1 << 32) - 1), 1);
    ptimer_run(s->ptimer[0], 0);
    int64_t now0 = qemu_clock_get_ns(QEMU_CLOCK_VIRTUAL);
    timer_mod(s->timer[0], 10000000 + now0);/* 100HZ */
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
