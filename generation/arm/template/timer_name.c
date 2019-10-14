{{license}}

#include "qemu/osdep.h"
#include "qemu/log.h"
#include "qemu/timer.h"
#include "hw/timer/{{timer_name}}.h"

static void {{timer_name}}_callback(void *opaque);
static void {{timer_name}}_update(void *opaque);
static void {{timer_name}}_reset(DeviceState *dev);

static uint64_t {{timer_name}}_read(void *opaque, hwaddr offset, unsigned size);
static void {{timer_name}}_write(void *opaque, hwaddr offset, uint64_t val, unsigned size);

static void {{timer_name}}_init(Object *obj);
static void {{timer_name}}_class_init(ObjectClass *klass, void *data);
static void {{timer_name}}_register_types(void);

static void {{timer_name}}_update(void *opaque) 
{
    {{timer_name|upper|concat}}State *s = opaque;

    int64_t now = qemu_clock_get_ns(QEMU_CLOCK_VIRTUAL);
    timer_mod(s->timer, 0x5 + now); /* 200MHZ */
    if (extract32(s->cpu_timers_control_register, 0, 1)) {
        if (s->cpu_timer0_register == 0) {
            qemu_set_irq(s->irq_0, 1);
            if (s->reserved_0 == 0) {
                s->reserved_0 = 1;
                s->cpu_timer0_register = 0xffffffff;
            }
            if (extract32(s->cpu_timers_control_register, 1, 1) == 1) {
                 s->cpu_timer0_register = s->cpu_timer0_reload_register / 0x5ff;
            }
        }
        if (extract32(s->cpu_timers_control_register, 1, 1) == 1 ||
            (extract32(s->cpu_timers_control_register, 1, 1) == 0 && !s->reserved_0)) {
            s->cpu_timer0_register--;
        }
    }

    if (extract32(s->cpu_timers_control_register, 2, 1)) {
        if (s->cpu_timer1_register == 0) {
            qemu_set_irq(s->irq_1, 1);
            if (s->reserved_1 == 0) {
                s->reserved_1 = 1;
                s->cpu_timer1_register = 0xffffffff;
            }
            if (extract32(s->cpu_timers_control_register, 3, 1) == 1) {
                 s->cpu_timer1_register = s->cpu_timer1_reload_register / 0x5ff;
            }
        }
        if (extract32(s->cpu_timers_control_register, 3, 1) == 1 ||
            (extract32(s->cpu_timers_control_register, 3, 1) == 0 && !s->reserved_1)) {
            s->cpu_timer1_register--;
        }
    }
}

static void {{timer_name}}_callback(void *opaque) 
{
    {{timer_name|upper|concat}}State *s = opaque;

    {{timer_name}}_update(s);
}

static uint64_t {{timer_name}}_read(void *opaque, hwaddr offset, unsigned size) 
{
    {{timer_name|upper|concat}}State *s = opaque;

    uint64_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset 0x%"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    {% for register in timer_registers %}case {{register.name|upper}}:
        res = s->{{register.name}};
        break;
    {% endfor %}}
    return res;
}

static void {{timer_name}}_write(void *opaque, hwaddr offset, uint64_t val, unsigned size) 
{
    {{timer_name|upper|concat}}State *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset 0x%"HWADDR_PRIx"\n", __func__, offset);
        return;
    {% for register in timer_registers %}case {{register.name|upper}}:
        s->{{register.name}} = val;
        break;
    {% endfor %}}
    {{timer_name}}_update(s);
}

static const MemoryRegionOps {{timer_name}}_ops = {
    .read = {{timer_name}}_read,
    .write = {{timer_name}}_write,
    .endianness = DEVICE_NATIVE_ENDIAN,
};

static void {{timer_name}}_init(Object *obj) 
{
    {{timer_name|upper|concat}}State *s = {{timer_name|upper}}(obj);

    /* initialize the mmio */
    memory_region_init_io(&s->mmio, obj, &{{timer_name}}_ops, s, "{{timer_name}}", {{timer_name|upper}}_MMIO_SIZE);
    sysbus_init_mmio(SYS_BUS_DEVICE(s), &s->mmio);

    /* initialize the irqs */
    sysbus_init_irq(SYS_BUS_DEVICE(s), &s->irq_0);
    sysbus_init_irq(SYS_BUS_DEVICE(s), &s->irq_1);

    /* initialize the timer */
    s->timer = timer_new_ns(QEMU_CLOCK_VIRTUAL, {{timer_name}}_callback, s);
}

static void {{timer_name}}_reset(DeviceState *dev) 
{
    {{timer_name|upper|concat}}State *s = {{timer_name|upper}}(dev);
    {% for register in timer_registers %}
    s->{{register.name}} = 0;{% endfor %}
    s->reserved_0 = 0;
    s->reserved_1 = 0;
    s->reserved_2 = 0;
}

static void {{timer_name}}_class_init(ObjectClass *klass, void *data) 
{
    DeviceClass *dc = DEVICE_CLASS(klass);

    /* dc->fw_name = ; */
    /* dc->desc = ; */
    /* dc->props = ; */
    /* dc->user_creatable = ; */
    /* dc->hotpluggable = ; */
    /* dc->reset = ; */
    dc->reset = {{timer_name}}_reset;
    /* dc->realize = ; */
    /* dc->unrealize = ; */
    /* dc->vmsd = ; */
    /* dc->bus_type = ; */

    /* SysBusDeviceClass sbc = SYS_BUS_DEVICE_CLASS(klass); */

    /* sbc->explicit_ofw_unit_address = ; */
    /* sbc->connect_irq_notifier = ; */
}

static const TypeInfo {{timer_name}}_info = {
    .name = TYPE_{{timer_name|upper}},
    .parent = TYPE_SYS_BUS_DEVICE,
    .instance_size = sizeof({{timer_name|upper|concat}}State),
    .instance_init = {{timer_name}}_init,
    /* .class_zie = sizeof(SysBusDeviceClass), */
    .class_init = {{timer_name}}_class_init,
};

static void {{timer_name}}_register_types(void) 
{
    type_register_static(&{{timer_name}}_info);
}

type_init({{timer_name}}_register_types)
