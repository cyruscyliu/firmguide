{{license}}

#include "qemu/osdep.h"
#include "qemu/log.h"
#include "hw/gpio/{{gpio_name}}.h"

static void {{gpio_name}}_update(void *opaque);
static void {{gpio_name}}_set_irq(void *opaque, int irq, int level);
static uint64_t {{gpio_name}}_read(void *opaque, hwaddr offset, unsigned size);
static void {{gpio_name}}_write(void *opaque, hwaddr offset, uint64_t val, unsigned size);

static void {{gpio_name}}_reset(DeviceState *dev);

static void {{gpio_name}}_init(Object *obj);
static void {{gpio_name}}_class_init(ObjectClass *klass, void *data);
static void {{gpio_name}}_register_types(void);

static void {{gpio_name}}_update(void *opaque) {
    {{gpio_name|upper|concat}}State *s = opaque;
    int level;

    for (int i = 0; i < {{gpio_in_out_n}}; ++i) {
        if (extract32(s->gpio_data_out_enable_control_register, irq, 0)) continue;
        /* no implementation for blinking */
        if (extract32(s->gpio_blink_enable_register, i, 1)) continue;
        level = extract32(s->gpio_data_out_register, i, 1);
        qemu_set_irq(s->out[i], level);

        if (extract32(s->gpio_interrupt_cause_register, i, 1) &&
            extract32(s->gpio_interrupt_level_mask_register, i, 1)) {
            qemu_set_irq(s->irq[i / 8], 1);
        } else if (extract32(s->gpio_interrupt_cause_register, i, 1) &&
            extract32(s->gpio_interrupt_mask_register, i, 1)) {
            qemu_set_irq(s->irq[i / 8], 0);
            qemu_set_irq(s->irq[i / 8], 1);
        } else {
            qemu_set_irq(s->irq[i / 8], 0);
        }
    }
}

static void {{gpio_name}}_set_irq(void *opaque, int irq, int level) {
    {{gpio_name|upper|concat}}State *s = opaque;
    int artificial_level;

    if (extract32(s->gpio_data_out_enable_control_register, irq, 1)) return;
    if (extract32(s->gpio_blink_enable_register, irq, 1)) return;
    if (extract32(s->gpio_data_in_polarity_register, irq, 1)) {
        artificial_level = !level;
    } else {
        artificial_level = level;
    }
    if (extract32(s->gpio_data_in_register, irq, 1) == 0 && artificial_level == 1) {
        s->gpio_interrupt_cause_register =
            deposit32(s->gpio_interrupt_cause_register, irq, 1, 1);
    }
    s->gpio_data_in_register =
        deposit32(s->gpio_data_in_register, irq, 1, artificial_level);
    {{gpio_name}}_update(s);
}

static uint64_t {{gpio_name}}_read(void *opaque, hwaddr offset, unsigned size) {
    {{gpio_name|upper|concat}}State *s = ({{gpio_name|upper|concat}}State *)opaque;

    uint64_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset 0x%"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    {% for register in gpio_registers %}case {{register.name|upper}}:
        res = s->{{register.name}};
        break;
    {% endfor %}}
    return res;
}

static void {{gpio_name}}_write(void *opaque, hwaddr offset, uint64_t val, unsigned size) {
    {{gpio_name|upper|concat}}State *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset 0x%"HWADDR_PRIx"\n", __func__, offset);
        return;
    {% for register in gpio_registers %}case {{register.name|upper}}:
        s->{{register.name}} = val;
        break;
    {% endfor %}}
    {{gpio_name}}_update(s);
    return;
}

static const MemoryRegionOps {{gpio_name}}_ops = {
    .read = {{gpio_name}}_read,
    .write = {{gpio_name}}_write,
    .endianness = DEVICE_NATIVE_ENDIAN,
};

static void {{gpio_name}}_init(Object *obj) {
    {{gpio_name|upper|concat}}State *s = {{gpio_name|upper}}(obj);

    /* initialize the mmio */
    memory_region_init_io(&s->gpio_mmio, obj, &{{gpio_name}}_ops, s, "{{gpio_name}}", {{gpio_name|upper}}_MMIO_SIZE);
    sysbus_init_mmio(SYS_BUS_DEVICE(s), &s->gpio_mmio);

    /* initialize the irq */
    for (int i; i < {{gpio_irq_n}}; ++i) {
        sysbus_init_irq(SYS_BUS_DEVICE(s), &s->irq[i]);
    }

    /* initialize the input/output */
    qdev_init_gpio_in(DEVICE(s), {{gpio_name}}_set_irq, {{gpio_in_out_n}});
    qdev_init_gpio_out(DEVICE(s), s->out, {{gpio_in_out_n}});
}

static void {{gpio_name}}_reset(DeviceState *dev) {
    {{gpio_name|upper|concat}}State *s = {{gpio_name|upper}}(dev);
    {% for register in gpio_registers %}
    s->{{register.name}} = {{register.value}};{% endfor %}
}

static void {{gpio_name}}_class_init(ObjectClass *klass, void *data) {
    DeviceClass *dc = DEVICE_CLASS(klass);

    /* dc->fw_name = ; */
    /* dc->desc = ; */
    /* dc->props = ; */
    /* dc->user_creatable = ; */
    /* dc->hotpluggable = ; */
    dc->reset = {{gpio_name}}_reset;
    /* dc->realize = ; */
    /* dc->unrealize = ; */
    /* dc->vmsd = ; */
    /* dc->bus_type = ; */

    /* SysBusDeviceClass sbc = SYS_BUS_DEVICE_CLASS(klass); */

    /* sbc->explicit_ofw_unit_address = ; */
    /* sbc->connect_irq_notifier = ; */
}

static const TypeInfo {{gpio_name}}_info = {
    .name = TYPE_{{gpio_name|upper}},
    .parent = TYPE_SYS_BUS_DEVICE,
    .instance_size = sizeof({{gpio_name|upper|concat}}State),
    .instance_init = {{gpio_name}}_init,
    /* .class_zie = sizeof(SysBusDeviceClass), */
    .class_init = {{gpio_name}}_class_init,
};

static void {{gpio_name}}_register_types(void) {
    type_register_static(&{{gpio_name}}_info);
}

type_init({{gpio_name}}_register_types)