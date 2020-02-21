{{ license }}

#include "qemu/osdep.h"
#include "qemu/log.h"
#include "qapi/error.h"
#include "hw/intc/{{ name }}.h"

{% for irqn_to_reg in intc_irqn_to_regs %}
static const {{ name }}_to_reg {{ name }}_irq{{ irqn_to_reg.irqn }}_to_regs[] = {
    {% for to_reg in irqn_to_reg.to_regs %}{
        .offset = {{ to_reg.offset }},
        .value  = {{ to_reg.value }},
        .size   = {{ to_reg.size }},
    },{% endfor %}{
        .offset = -1
    }
}
{% endfor %}
static const {{ name }}_irqn_table_entry {{ name }}_irqn_table[] = {
    {% for irqn_to_reg in intc_irqn_to_regs %}{
         .irqn = {{ irqn_to_reg.irqn }},
         .to_regs = &{{ name }}_irq{{ irqn_to_reg.irqn }}_to_regs,
    },{% endfor %}{
        .irqn = -1;
    }
}

static void {{ name }}_update(void *opaque)
{
    {{ name|upper }}State *s = opaque;
    int i;

    /* This is the meeting place for all interrupt source.
     * STATE_IDLE means this interrupt source is sound.
     * STATE_SET_ALARM is set when the interrupt source is
     * in STATE_IDLE and the source pull up the signal. At
     * this time, we should update MMIOs according to SET_
     * ALARM_TABLE. See {{ name }}_set_irq for details.
     * STATE_MASK_ACK/STATE_ACK is set when the r/w pattern
     * is captured. The pattern is from the source code.
     * STATE_CLEAR is set when the interrupt source is in
     * STATE_MASK_ACK/STATE_ACK and the source pull down the
     * signal. We will pull down the signal as well.
     * STATE_UNMASK is set when the r/w pattern is captured.
     * The pattern is from the srouce code. A interrupt
     * going into STATE_UNMAKS will go to STATE_IDLE immediately.
     */
    for (i = 0; i < 32; i++) {
        switch(s->state[i]) {
            case STATE_IDLE:
                break;
            case STATE_MASK_ACK:
            case STATE_MASK:
                break;
            case STATE_CLEAR:
                qemu_set_irq(s->irq, 0);
                break;
            case STATE_SET_ALARM:
                qemu_set_irq(s->irq, 1);
                break;
            case STATE_UNMASK:
                s->state[i] = STATE_IDLE;
                break;
        }
    }
}

static void {{ name }}_set_irq(void *opaque, int irq, int level)
{
    {{ name|upper }}State *s = opaque;
    struct {{ name }}_irq_table_entry entry;
    struct {{ name }}_to_regs *to_regs;
    int i, j;

    /* One and only one interrupt source will call me when
     * it pull up or pull down the level of the signal.
     * This behavior will make STATE_IDLE -> STATE_SET_ALARM,
     * of STATE_MASK_ACK/STATE_MASK -> STATE_CLEAR.
     * State is guaranteed for every interrupt source.
     */
    switch(s->state[irq]) {
        case STATE_IDLE:
            if (level) {
                for (i = 0, entry = {{ name }}_irqn_table[i].irqn; entry.irqn != -1; i++) {
                    if (entry.irqn != irqn) continue;
                    to_regs = entry.to_regs;
                    for (j = 0; to_regs[j].offset != -1; i++) {
                        {{ name }}_write(s, to_regs[j].offset, to_regs[j].value, to_regs[j].size);
                    }
                }
                s->state[irq] = STATE_SET_ALARM;
            }
            break;
        case STATE_MASK_ACK:
            if (!level) s->state[irq] = STATE_CLEAR;
            break;
        case STATE_UNMASK:
            if (!level) {
                s->state[irq] = STATE_CLEAR;
                s->clear = deposit32(s->cause, irq, 1, level);
            }
            break;
        case STATE_CLEAR:
        case STATE_SET_ALARM:
        case STATE_MASK:
            break;
    }
    {{ name }}_update(s);
}

static uint64_t {{ name }}_read(void *opaque, hwaddr offset, unsigned size)
{
    {{ name|upper }}State *s = opaque;
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
    {{ name|upper }}State *s = opaque;
    int i;

    switch (offset) {
        default:
            return;{% for register in intc_get_registers %}
        case {{ register.offset }}:
            s->{{ register.rname }}= val;
            for (i = 0; i < 32; i++) {
                if({{ register.action }} == val)
                    break
            }
            switch (s->state[i]) {
                case STATE_SET_ALARM:{% if register.mask_ack %}
                    s->state[i] = STATE_MASK_ACK;{% endif %}{% if register.mask %}
                    s->state[i] = STATE_MASK;{% endif %}
                    break;
                case STATE_MASK:
                case STATE_MASK_ACK:{% if register.clean %}
                    s->state[i] = STATE_CLEAR;{% endif %}
                    break;
                case STATE_UNMASK:
                case STATE_CLEAR:
                case STATE_IDLE:
                    break;
            }
            break;{% endfor %}
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
    {{ name|upper }}State *s = {{ name|upper }}(obj);

    /* initialize the mmio */
    memory_region_init_io(&s->mmio, obj, &{{ name }}_ops, s, TYPE_{{ name|upper }}, {{ reg.size }});
    sysbus_init_mmio(SYS_BUS_DEVICE(s), &s->mmio);

    /* initialize the irq/fip to cpu */
    qdev_init_gpio_out(DEVICE(s), &s->irq, 1);
    qdev_init_gpio_in(DEVICE(s), {{ name }}_set_irq, 32);
}

static void {{ name }}_reset(DeviceState *dev)
{
    {{ name|upper }}State *s = {{ name|upper }}(dev);{% for register in intc_get_registers %}
    s->{{ register.rname }} = 0;{% endfor %}
    s->cause = 0;
}

static void {{ name }}_class_init(ObjectClass *klass, void *data)
{
    DeviceClass *dc = DEVICE_CLASS(klass);

    dc->reset = {{ name }}_reset;
}

static TypeInfo {{ name }}_type_info = {
    .name = TYPE_{{ name|upper }},
    .parent = TYPE_SYS_BUS_DEVICE,
    .instance_size = sizeof({{ name|upper }}State),
    .instance_init = {{ name }}_init,
    .class_init = {{ name }}_class_init,
};

static void {{ name }}_register_types(void)
{
    type_register_static(&{{ name }}_type_info);
}

type_init({{ name }}_register_types)

