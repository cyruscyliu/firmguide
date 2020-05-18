{{ license }}

#include "qemu/osdep.h"
#include "qemu/log.h"
#include "qapi/error.h"
#include "hw/intc/{{ name }}.h"

static bool set_{{ name }}_irqn_to_regs(void *opaque, int irqn)
{
    {{ name|to_upper }}State *s = opaque;
    switch(irqn) { {% for irqn_to_reg in intc_irqn_to_regs %}
        case {{ irqn_to_reg.irqn }}:{% for line in irqn_to_reg.set_body %}
            {{ line }}{% endfor %}
            break;{% endfor %}
    }
    return true;
}

static bool clear_{{ name }}_irqn_to_regs(void *opaque, int irqn)
{
    {{ name|to_upper }}State *s = opaque;
    switch(irqn) { {% for irqn_to_reg in intc_irqn_to_regs %}
        case {{ irqn_to_reg.irqn }}:{% for line in irqn_to_reg.clear_body %}
            {{ line }}{% endfor %}
            break;{% endfor %}
    }
    return true;
}

static void {{ name }}_update(void *opaque)
{
    {{ name|to_upper }}State *s = opaque;
    int i;

    // state transition table
    // state_from pending masked state_to
    //    REST       0      0     REST
    //    REST       0      1     REST
    //    REST       1      0     NOISE
    //    REST       1      1     NOISE
    //    NOISE      0      0     REST
    //    NOISE      0      1     REST
    //    NOISE      1      0     ALARM(*)
    //    NOISE      1      1     NOISE
    //    ALARM      0      0     REST(*)
    //    ALARM      0      1     REST(*)
    //    ALARM      1      0     ALARM(*)
    //    ALARM      1      1     NOISE(*)
    for (i = 0; i < N_IRQ; i++) {
        switch(s->state[i]) {
            case STATE_REST:
                if (s->pending[i]) {
                    s->state[i] = STATE_NOISE;
                    if (!s->masked[i]) {
                        s->state[i] = STATE_ALARM;
                        set_{{ name }}_irqn_to_regs(s, i);
                        qemu_set_irq(s->irq, 1);
                    }
                }
                break;
            case STATE_NOISE:
                if (s->pending[i]) {
                    if (!s->masked[i]) {
                        s->state[i] = STATE_ALARM;
                        set_{{ name }}_irqn_to_regs(s, i);
                        qemu_set_irq(s->irq, 1);
                    }
                } else {
                    s->state[i] = STATE_REST;
                    clear_{{ name }}_irqn_to_regs(s, i);
                    qemu_set_irq(s->irq, 0);
                }
                break;
            case STATE_ALARM:
                if (s->pending[i]) {
                    if (s->masked[i]) {
                        clear_{{ name }}_irqn_to_regs(s, i);
                        qemu_set_irq(s->irq, 0);
                        s->state[i] = STATE_NOISE;
                    }
                } else {
                    s->state[i] = STATE_REST;
                    clear_{{ name }}_irqn_to_regs(s, i);
                    qemu_set_irq(s->irq, 0);
                }
                break;
        }
    }
}

static uint64_t {{ name }}_read(void *opaque, hwaddr offset, unsigned size)
{
    {{ name|to_upper }}State *s = opaque;
    uint32_t res = 0;

    switch (offset) {
        default:
            return 0;{% for register in intc_get_registers %}
        case {{ register.offset }}:
            res = s->{{ register.rname }};
            break;{% endfor %}
    }
    return res;
}

static void {{ name }}_write(void *opaque, hwaddr offset, uint64_t val, unsigned size)
{
    {{ name|to_upper }}State *s = opaque;
    uint64_t irqn;
    uint32_t old;

    switch (offset) {
        default:
            return;{% for register in intc_get_registers %}
        case {{ register.offset }}:
            old = (uint32_t)s->{{ register.rname }};{% if register.mask_ack %}
            for (irqn = 0; irqn < N_IRQ; irqn++)
                if ({{ register.mask_ack_action }} == (uint32_t)val) {
                    s->masked[irqn] = true;
                    s->pending[irqn] = false;
                }{% endif %}{% if register.mask %}
            for (irqn = 0; irqn < N_IRQ; irqn++)
                if ({{ register.mask_action }} == (uint32_t)val) {
                    s->masked[irqn] = true;
                }{% endif %}{% if register.ack %}
            for (irqn = 0; irqn < N_IRQ; irqn++)
                if ({{ register.ack_action }} == (uint32_t)val) {
                    s->pending[irqn] = false;
                }{% endif %}{% if register.unmask %}
            for (irqn = 0; irqn < N_IRQ; irqn++)
                if ({{ register.unmask_action }} == (uint32_t)val) {
                    s->masked[irqn] = false;
                }{% endif %}{% if register.override %}
            s->{{ register.rname }}= val;{% endif %}
            break;{% endfor %}
    }
    {{ name }}_update(s);
}

static const MemoryRegionOps {{ name }}_ops = {
    .read = {{ name }}_read,
    .write = {{ name }}_write,
    .endianness = {{ endian }},
};

static void {{ name }}_set_irq(void *opaque, int irq, int level)
{
    {{ name|to_upper }}State *s = opaque;

    if (level)
        s->pending[irq] = true;
    else
        s->pending[irq] = false;

    {{ name }}_update(s);
}

static void {{ name }}_init(Object *obj)
{
    {{ name|to_upper }}State *s = {{ name|to_upper }}(obj);

    /* initialize the mmio */
    memory_region_init_io(&s->mmio, obj, &{{ name }}_ops, s, TYPE_{{ name|to_upper }}, {{ reg.size }});
    sysbus_init_mmio(SYS_BUS_DEVICE(s), &s->mmio);

    /* initialize the irq/fip to cpu */
    qdev_init_gpio_out(DEVICE(s), &s->irq, 1);
    qdev_init_gpio_in(DEVICE(s), {{ name }}_set_irq, N_IRQ);
}

static void {{ name }}_reset(DeviceState *dev)
{
    int irqn;
    {{ name|to_upper }}State *s = {{ name|to_upper }}(dev);{% for register in intc_get_registers %}
    s->{{ register.rname }} = {{ register.value }};{% endfor %}

    for (irqn = 0; irqn < N_IRQ; irqn++)
        s->masked[irqn] = true;
}

static void {{ name }}_class_init(ObjectClass *klass, void *data)
{
    DeviceClass *dc = DEVICE_CLASS(klass);

    dc->reset = {{ name }}_reset;
}

static TypeInfo {{ name }}_type_info = {
    .name = TYPE_{{ name|to_upper }},
    .parent = TYPE_SYS_BUS_DEVICE,
    .instance_size = sizeof({{ name|to_upper }}State),
    .instance_init = {{ name }}_init,
    .class_init = {{ name }}_class_init,
};

static void {{ name }}_register_types(void)
{
    type_register_static(&{{ name }}_type_info);
}

type_init({{ name }}_register_types)
