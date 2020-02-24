{{ license }}

#include "qemu/osdep.h"
#include "qemu/log.h"
#include "qapi/error.h"
#include "qemu/timer.h"
#include "hw/timer/{{ name }}.h"
{% for i in irqc|range %}
static void {{ name }}_tick_callback{{ i }}(void *opaque)
{
    {{ name|upper}}State *s = opaque;

    /* stupid timer */
    int64_t now = qemu_clock_get_ns(QEMU_CLOCK_VIRTUAL);
    timer_mod(s->timer[{{i}}], 0x10000000 + now); /* 100HZ */
    qemu_set_irq(s->irq[{{i}}], 1);
}
{% endfor %}

static void {{ name }}_update(void *opaque)
{
    /* {{ name|upper }}State *s = opaque; */
}

static uint64_t {{ name }}_read(void *opaque, hwaddr offset, unsigned size)
{
    {{ name|upper }}State *s = opaque;
    uint32_t res = 0;

    switch (offset) {
        default:
            return 0;
        case 0x0 ... {{ reg.size }} - 0x4:
            res = s->reserved;
            break;
    }
    return res;
}

static void {{ name }}_write(void *opaque, hwaddr offset, uint64_t val, unsigned size)
{
    {{ name|upper }}State *s = opaque;

    switch (offset) {
        default:
            return;
        case 0x0 ... {{ reg.size }} - 0x4:
            s->reserved = val;
            break;
    }
    {{ name }}_update(s);
}

static const MemoryRegionOps {{ name }}_ops = {
    .read = {{ name }}_read,
    .write = {{ name }}_write,
    .endianness = {{ endian }},
};

static void {{ name }}_init(Object *obj)
{
    {{ name|upper}}State *s = {{ name|upper }}(obj);

    /* initialize the mmio */
    memory_region_init_io(&s->mmio, obj, &{{ name }}_ops, s, TYPE_{{ name|upper }}, {{ reg.size }});
    sysbus_init_mmio(SYS_BUS_DEVICE(s), &s->mmio);

    /* initialize an irq to the intc */
    qdev_init_gpio_out(DEVICE(s), s->irq, {{ irqc }});

    /* initialize the timer */{% for i in irqc|range %}
    s->timer[{{ i }}] = timer_new_ns(QEMU_CLOCK_VIRTUAL, {{ name }}_tick_callback{{ i }}, s);{% endfor %}
}

static void {{ name }}_reset(DeviceState *dev)
{
    {{ name|upper}}State *s = {{ name|upper }}(dev);
    s->reserved = 0;
}

static void {{ name }}_class_init(ObjectClass *klass, void *data)
{
    DeviceClass *dc = DEVICE_CLASS(klass);

    dc->reset = {{ name }}_reset;
}

static TypeInfo {{ name }}_type_info = {
    .name = TYPE_{{ name|upper }},
    .parent = TYPE_SYS_BUS_DEVICE,
    .instance_size = sizeof({{ name|upper}}State),
    .instance_init = {{ name }}_init,
    /* .class_size = sizeof(SysBusDeviceClass), */
    .class_init = {{ name }}_class_init,
};

static void {{ name }}_register_types(void)
{
    type_register_static(&{{ name }}_type_info);
}

type_init({{ name }}_register_types)

