/*
 * automatically generated, don't change
 */

#include "qemu/osdep.h"
#include "qemu/log.h"
#include "qapi/error.h"
#include "qemu/timer.h"
#include "hw/timer/marvell_orion_timer.h"

static void marvell_orion_timer_tick_callback0(void *opaque)
{
    MARVELL_ORION_TIMERState *s = opaque;

    /* stupid timer */
    int64_t now = qemu_clock_get_ns(QEMU_CLOCK_VIRTUAL);
    timer_mod(s->timer[0], 1000000000 / 1000000 + now); /* 1000000HZ */
    /* 1000000HZ -> 100HZ */
    if (s->counter[0] % (1000000 / 100) == 0)
        qemu_set_irq(s->irq[0], 1);
    s->counter[0] &= ((1 << 32) - 1);
    s->counter[0]++;
}

static void marvell_orion_timer_tick_callback1(void *opaque)
{
    MARVELL_ORION_TIMERState *s = opaque;

    /* stupid timer */
    int64_t now = qemu_clock_get_ns(QEMU_CLOCK_VIRTUAL);
    timer_mod(s->timer[1], 1000000000 / 1000000 + now); /* 1000000HZ */
    /* 1000000HZ -> 100HZ */
    if (s->counter[1] % (1000000 / 100) == 0)
        qemu_set_irq(s->irq[1], 1);
    s->counter[1] &= ((1 << 32) - 1);
    s->counter[1]++;
}


static void marvell_orion_timer_update(void *opaque)
{
    /* MARVELL_ORION_TIMERState *s = opaque; */
}

static uint64_t marvell_orion_timer_read(void *opaque, hwaddr offset, unsigned size)
{
    MARVELL_ORION_TIMERState *s = opaque;
    uint32_t res = 0;

    switch (offset) {
        default:
            return 0;
        case 0x14:
            res = s->counter[1];
            break;
    }
    return res;
}

static void marvell_orion_timer_write(void *opaque, hwaddr offset, uint64_t val, unsigned size)
{
    MARVELL_ORION_TIMERState *s = opaque;

    switch (offset) {
        default:
            return;
        case 0x0 ... 0x1c:
            s->reserved = val;
            break;
    }
    marvell_orion_timer_update(s);
}

static const MemoryRegionOps marvell_orion_timer_ops = {
    .read = marvell_orion_timer_read,
    .write = marvell_orion_timer_write,
    .endianness = DEVICE_LITTLE_ENDIAN,
};

static void marvell_orion_timer_init(Object *obj)
{
    MARVELL_ORION_TIMERState *s = MARVELL_ORION_TIMER(obj);

    /* initialize the mmio */
    memory_region_init_io(&s->mmio, obj, &marvell_orion_timer_ops, s, TYPE_MARVELL_ORION_TIMER, 0x20);
    sysbus_init_mmio(SYS_BUS_DEVICE(s), &s->mmio);

    /* initialize an irq to the intc */
    qdev_init_gpio_out(DEVICE(s), s->irq, 2);

    /* initialize the timer */
    s->timer[0] = timer_new_ns(QEMU_CLOCK_VIRTUAL, marvell_orion_timer_tick_callback0, s);
    s->timer[1] = timer_new_ns(QEMU_CLOCK_VIRTUAL, marvell_orion_timer_tick_callback1, s);
}

static void marvell_orion_timer_reset(DeviceState *dev)
{
    MARVELL_ORION_TIMERState *s = MARVELL_ORION_TIMER(dev);
    int64_t now;
    
    now = qemu_clock_get_ns(QEMU_CLOCK_VIRTUAL);
    timer_mod(s->timer[0], 0x10000000 + now); /* 100HZ */
    s->counter[0] = 0;
    now = qemu_clock_get_ns(QEMU_CLOCK_VIRTUAL);
    timer_mod(s->timer[1], 0x10000000 + now); /* 100HZ */
    s->counter[1] = 0;
    s->reserved = 0;
}

static void marvell_orion_timer_class_init(ObjectClass *klass, void *data)
{
    DeviceClass *dc = DEVICE_CLASS(klass);

    dc->reset = marvell_orion_timer_reset;
}

static TypeInfo marvell_orion_timer_type_info = {
    .name = TYPE_MARVELL_ORION_TIMER,
    .parent = TYPE_SYS_BUS_DEVICE,
    .instance_size = sizeof(MARVELL_ORION_TIMERState),
    .instance_init = marvell_orion_timer_init,
    /* .class_size = sizeof(SysBusDeviceClass), */
    .class_init = marvell_orion_timer_class_init,
};

static void marvell_orion_timer_register_types(void)
{
    type_register_static(&marvell_orion_timer_type_info);
}

type_init(marvell_orion_timer_register_types)
