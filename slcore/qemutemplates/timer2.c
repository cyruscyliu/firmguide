{{ license }}

#include "qemu/osdep.h"
#include "qemu/log.h"
#include "qapi/error.h"
#include "qemu/timer.h"
#include "hw/timer/{{ name }}.h"
{% for i in timer_n_irq|to_range %}
static void {{ name }}_tick_callback{{ i }}(void *opaque)
{
    {{ name|to_upper}}State *s = opaque;

    /* stupid timer */
    int64_t now = qemu_clock_get_ns(QEMU_CLOCK_VIRTUAL);
    timer_mod(s->timer[{{i}}], 0x10000 + now); /* 0.1MHZ */
    /* 100,000HZ -> 100HZ */
    if (s->counter[{{i}}] % 1000 == 0)
        qemu_set_irq(s->irq[{{i}}], 1);
    s->counter[{{i}}]++;
}
{% endfor %}

static void {{ name }}_update(void *opaque)
{
    /* {{ name|to_upper }}State *s = opaque; */
}

static uint64_t {{ name }}_read(void *opaque, hwaddr offset, unsigned size)
{
    {{ name|to_upper }}State *s = opaque;
    uint32_t res = 0;

    switch (offset) {
        default:
            return 0;{% for counter in timer_counters %}
        case {{ counter.addr }}:
            res = s->counter[{{ counter.id }}];{% endfor %}
            break;
    }
    return res;
}

static void {{ name }}_write(void *opaque, hwaddr offset, uint64_t val, unsigned size)
{
    {{ name|to_upper }}State *s = opaque;

    switch (offset) {
        default:
            return;
        case {{ reg.size|to_offset }}:
            s->reserved = val;
            break;
    }
    {{ name }}_update(s);
}

static const MemoryRegionOps {{ name }}_ops = {
    .read = {{ name }}_read,
    .write = {{ name }}_write,
    .endianness = {{ endian|to_endian }},
};

static void {{ name }}_init(Object *obj)
{
    {{ name|to_upper}}State *s = {{ name|to_upper }}(obj);

    /* initialize the mmio */
    memory_region_init_io(&s->mmio, obj, &{{ name }}_ops, s, TYPE_{{ name|to_upper }}, {{ reg.size|to_hex }});
    sysbus_init_mmio(SYS_BUS_DEVICE(s), &s->mmio);

    /* initialize an irq to the intc */
    qdev_init_gpio_out(DEVICE(s), s->irq, {{ timer_n_irq }});

    /* initialize the timer */{% for i in timer_n_irq|to_range %}
    s->timer[{{ i }}] = timer_new_ns(QEMU_CLOCK_VIRTUAL, {{ name }}_tick_callback{{ i }}, s);{% endfor %}
}

static void {{ name }}_reset(DeviceState *dev)
{
    {{ name|to_upper}}State *s = {{ name|to_upper }}(dev);
    int64_t now;
    {% for i in timer_n_irq|to_range %}
    now = qemu_clock_get_ns(QEMU_CLOCK_VIRTUAL);
    timer_mod(s->timer[{{i}}], 0x10000000 + now); /* 100HZ */
    s->counter[{{i}}] = 0;{% endfor %}
    s->reserved = 0;
}

static void {{ name }}_class_init(ObjectClass *klass, void *data)
{
    DeviceClass *dc = DEVICE_CLASS(klass);

    dc->reset = {{ name }}_reset;
}

static TypeInfo {{ name }}_type_info = {
    .name = TYPE_{{ name|to_upper }},
    .parent = TYPE_SYS_BUS_DEVICE,
    .instance_size = sizeof({{ name|to_upper}}State),
    .instance_init = {{ name }}_init,
    /* .class_size = sizeof(SysBusDeviceClass), */
    .class_init = {{ name }}_class_init,
};

static void {{ name }}_register_types(void)
{
    type_register_static(&{{ name }}_type_info);
}

type_init({{ name }}_register_types)
