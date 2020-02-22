/*
 * Salamander Generic Timer
 */
#include "qemu/osdep.h"
#include "qemu/log.h"
#include "qapi/error.h"
#include "qemu/timer.h"
#include "hw/timer/slgtimer.h"

static void slgtick_callback(void *opaque)
{
    SLGTimerState *s = opaque;
    int64_t now = qemu_clock_get_ns(QEMU_CLOCK_VIRTUAL);
    timer_mod(s->timer, 0x10000000 + now); /* 100HZ */
    /* stupid timer */
    qemu_set_irq(s->irq, 1);
}

static void slgtimer_init(Object *obj)
{
    SLGTimerState *s = SLGTimer(obj);

    /* initialize an irq to the intc */
    qdev_init_gpio_out(DEVICE(s), &s->irq, 1);

    /* initialize the timer */
    s->timer = timer_new_ns(QEMU_CLOCK_VIRTUAL, slgtick_callback, s);
}

static void slgtimer_reset(DeviceState *dev)
{
    /* SLGTimerState *s = SLGTimer(dev); */
}

static void slgtimer_class_init(ObjectClass *klass, void *data)
{
    DeviceClass *dc = DEVICE_CLASS(klass);

    dc->reset = slgtimer_reset;
}

static TypeInfo slgtimer_type_info = {
    .name = TYPE_SLGTIMER,
    .parent = TYPE_SYS_BUS_DEVICE,
    .instance_size = sizeof(SLGTimerState),
    .instance_init = slgtimer_init,
    /* .class_size = sizeof(SysBusDeviceClass), */
    .class_init = slgtimer_class_init,
};

static void slgtimer_register_types(void)
{
    type_register_static(&slgtimer_type_info);
}

type_init(slgtimer_register_types)
