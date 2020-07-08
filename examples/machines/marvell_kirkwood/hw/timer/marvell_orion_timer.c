/*
 * automatically generated, don't change
 */

#include "qemu/osdep.h"
#include "qemu/log.h"
#include "qapi/error.h"
#include "hw/timer/marvell_orion_timer.h"

static void marvell_orion_timer_clksrc_callback0(void *opaque)
{
    /* MARVELL_ORION_TIMERState *s = opaque; */
}

static void marvell_orion_timer_clkevt_callback0(void *opaque)
{
    MARVELL_ORION_TIMERState *s = opaque;

    int64_t now = qemu_clock_get_ns(QEMU_CLOCK_VIRTUAL);
    timer_mod(s->timer[0], 10000000 + now); /* 100HZ */
    qemu_set_irq(s->irq[0], 1);
}

static void marvell_orion_timer_clksrc_callback1(void *opaque)
{
    /* MARVELL_ORION_TIMERState *s = opaque; */
}

static void marvell_orion_timer_clkevt_callback1(void *opaque)
{
    MARVELL_ORION_TIMERState *s = opaque;

    int64_t now = qemu_clock_get_ns(QEMU_CLOCK_VIRTUAL);
    timer_mod(s->timer[1], 10000000 + now); /* 100HZ */
    qemu_set_irq(s->irq[1], 1);
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
            res = ptimer_get_count(s->ptimer[1]);
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
    QEMUBH *bh[2];

    /* initialize the mmio */
    memory_region_init_io(&s->mmio, obj, &marvell_orion_timer_ops, s, TYPE_MARVELL_ORION_TIMER, 0x20);
    sysbus_init_mmio(SYS_BUS_DEVICE(s), &s->mmio);

    /* initialize an irq to the intc */
    qdev_init_gpio_out(DEVICE(s), s->irq, 2);

    /* initialize the timer */
    bh[0] = qemu_bh_new(marvell_orion_timer_clksrc_callback0, s);
    s->ptimer[0] = ptimer_init(bh[0], PTIMER_POLICY_DEFAULT);
    s->timer[0] = timer_new_ns(QEMU_CLOCK_VIRTUAL, marvell_orion_timer_clkevt_callback0, s);
    bh[1] = qemu_bh_new(marvell_orion_timer_clksrc_callback1, s);
    s->ptimer[1] = ptimer_init(bh[1], PTIMER_POLICY_DEFAULT);
    s->timer[1] = timer_new_ns(QEMU_CLOCK_VIRTUAL, marvell_orion_timer_clkevt_callback1, s);
}

static void marvell_orion_timer_reset(DeviceState *dev)
{
    MARVELL_ORION_TIMERState *s = MARVELL_ORION_TIMER(dev);
    
    ptimer_set_freq(s->ptimer[0], 200000000);
    ptimer_set_limit(s->ptimer[0], (uint32_t)((1 << 32) - 1), 1);
    ptimer_run(s->ptimer[0], 0);
    int64_t now0 = qemu_clock_get_ns(QEMU_CLOCK_VIRTUAL);
    timer_mod(s->timer[0], 10000000 + now0);/* 100HZ */
    ptimer_set_freq(s->ptimer[1], 200000000);
    ptimer_set_limit(s->ptimer[1], (uint32_t)((1 << 32) - 1), 1);
    ptimer_run(s->ptimer[1], 0);
    int64_t now1 = qemu_clock_get_ns(QEMU_CLOCK_VIRTUAL);
    timer_mod(s->timer[1], 10000000 + now1);/* 100HZ */
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
