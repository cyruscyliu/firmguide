/*
 * automatically generated, don't change
 */

#include "qemu/osdep.h"
#include "qemu/log.h"
#include "qapi/error.h"
#include "hw/timer/plxtech_nas782x_rps_timer.h"

static void plxtech_nas782x_rps_timer_clksrc_callback0(void *opaque)
{
    /* PLXTECH_NAS782X_RPS_TIMERState *s = opaque; */
}

static void plxtech_nas782x_rps_timer_clkevt_callback0(void *opaque)
{
    PLXTECH_NAS782X_RPS_TIMERState *s = opaque;

    int64_t now = qemu_clock_get_ns(QEMU_CLOCK_VIRTUAL);
    timer_mod(s->timer[0], 10000000 + now); /* 100HZ */
    qemu_set_irq(s->irq[0], 1);
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
            res = ptimer_get_count(s->ptimer[0]);
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
    QEMUBH *bh[1];

    /* initialize the mmio */
    memory_region_init_io(&s->mmio, obj, &plxtech_nas782x_rps_timer_ops, s, TYPE_PLXTECH_NAS782X_RPS_TIMER, 0x40);
    sysbus_init_mmio(SYS_BUS_DEVICE(s), &s->mmio);

    /* initialize an irq to the intc */
    qdev_init_gpio_out(DEVICE(s), s->irq, 1);

    /* initialize the timer */
    bh[0] = qemu_bh_new(plxtech_nas782x_rps_timer_clksrc_callback0, s);
    s->ptimer[0] = ptimer_init(bh[0], PTIMER_POLICY_DEFAULT);
    s->timer[0] = timer_new_ns(QEMU_CLOCK_VIRTUAL, plxtech_nas782x_rps_timer_clkevt_callback0, s);
}

static void plxtech_nas782x_rps_timer_reset(DeviceState *dev)
{
    PLXTECH_NAS782X_RPS_TIMERState *s = PLXTECH_NAS782X_RPS_TIMER(dev);
    
    ptimer_set_freq(s->ptimer[0], 390625);
    ptimer_set_limit(s->ptimer[0], (uint32_t)((1 << 24) - 1), 1);
    ptimer_run(s->ptimer[0], 0);
    int64_t now0 = qemu_clock_get_ns(QEMU_CLOCK_VIRTUAL);
    timer_mod(s->timer[0], 10000000 + now0);/* 100HZ */
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
