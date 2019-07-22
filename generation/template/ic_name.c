{{license}}

#include "hw/intc/{{ic_name}}.h"
#include "qemu/log.h"

static void {{ic_name}}_update({{soc_name}}ICState *s) {
    bool set = false;

    set = (s->irq_level_0 & s->fiq_enable_0);
    qemu_set_irq(s->fiq, set);
    set = (s->irq_level_0 & s->irq_enable_0);
    qemu_set_irq(s->irq, set);
}

static void {{ic_name}}_set_irq(void *opaque, int irq, int level) {
    {{soc_name|upper}}ICState *s = {{ic_name|upper}}(obj);
    s->irq_level_0 = deposit32(s->irq_level_0, irq, 1, level != 0);
    {{ic_name}}_update(s);
}

static void {{ic_name}}_read(void *opaque, hwaddr offset, unsigned size) {
    {{soc_name|upper}}ICState *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    case MAIN_INTERRUPT_CAUSE_REGISTER:
        res = s->irq_level_0;
        break;
    case MAIN_IRQ_INTERRUPT_MASK_REGISTER:
        res = s->irq_enable_0;
        break;
    case MAIN_FIQ_INTERRUPT_MASK_REGISTER:
        res = s->fiq_enable_0;
        break;
    case MAIN_ENDPOINT_INTERRUPT_MASK_REGISTER:
        /* do nothing */
        break;
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    }
    return res;
}

static void {{ic_name}}_write(void *opaque, hwaddr offset, uint64_t val, unsigned size) {
    {{soc_name|upper}}ICState *s = opaque;

    switch (offset) {
    case MAIN_INTERRUPT_CAUSE_REGISTER:
        s->irq_level_0 = extract64(val, 0, 32);
        break;
    case MAIN_IRQ_INTERRUPT_MASK_REGISTER:
        s->irq_enable_0 |= extract64(val, 0, 32);
        break;
    case MAIN_FIQ_INTERRUPT_MASK_REGISTER:
        s->fiq_enable_0 |= extract64(val, 0, 32);
        break;
    case MAIN_ENDPOINT_INTERRUPT_MASK_REGISTER:
        /* do nothing */
        break;
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    }
    {{ic_name}}_update(s);
}

static const MemoryRegionOps {{soc_name}}_ic_ops = {
    .read = {{ic_name}}_read,
    .write = {{ic_name}}_write,
    .endianness = DEVICE_NATIVE_ENDIAN,
    .valid.min_access_size = 4,
    .valid.max_access_size = 4,
};

static void {{soc_name}}_ic_init(Object *obj) {
    {{soc_name|upper}}ICState *s = {{ic_name|upper}}(obj);

    /* initialize the mmio */
    memory_region_init_io(&s->mmio, obj, &{{ic_name}}_ops, s, TYPE_{{ic_name|upper}}, {{ic_ram_size}});
    sysbus_init_mmio(SYS_BUS_DEVICE(s), &s->mmio);

    /* initialize the irq */
    qdev_init_gpio_in_named(DEVICE(s), {{ic_name}}_set_irq, {{ic_name|upper}}_IRQ, {{n_irqs}});
    sysbus_init_irq(SYS_BUS_DEVICE(s), &s->irq);
    sysbus_init_irq(SYS_BUS_DEVICE(s), &s->fiq);
}

static void {{soc_name}}_ic_reset(DeviceState *d) {
    {{soc_name|upper}}ICState *s = {{soc_name|upper}}_IC(d);
    {% for i in i_irqs %}{% for n in l_irqs %}
    s->irq_enable_{{i}} = 0;{% endfor %}{% endfor %}

    s->fiq_enable = false;
    s->fiq_select = 0;
}

static void {{ic_name}}_class_init(ObjectClass *kclass, void *data) {
    DeviceClass *dc = DEVICE_CLASS(klass);

    /* dc->fw_name = ; */
    /* dc->desc = ; */
    /* dc->props = ; */
    /* dc->user_creatable = ; */
    /* dc->hotpluggable = ; */
    dc->reset = {{soc_name}}_ic_reset;
    /* dc->realize = ; */
    /* dc->unrealize = ; */
    /* dc->vmsd = ; */
    /* dc->bus_type = ; */

    /* SysBusDeviceClass sbc = SYS_BUS_DEVICE_CLASS(klass); */

    /* sbc->explicit_ofw_unit_address = ; */
    /* sbc->connect_irq_notifier = ; */
}

static TypeInfo {{ic_name}}_type_info = {
    .name = TYPE_{{ic_name|upper}},
    .parent = TYPE_SYS_BUS_DEVICE,
    .instance_size = sizeof({{soc_name|upper}}ICState,
    .instance_init = {{ic_name}}_init,
    /* .class_size = sizeof(SysBusDeviceClass), */
    .class_init = {{ic_name}}_class_init,
};

static void {{ic_name}}_register_types(void) {
    type_register_static(&{{ic_name}}_type_info);
}

type_init({{ic_name}}_register_types)