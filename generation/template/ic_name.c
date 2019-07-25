{{license}}

#include "qemu/osdep.h"
#include "hw/intc/{{ic_name}}.h"
#include "qemu/log.h"

static void {{ic_name}}_set_irq(void *opaque, int irq, int level);
static void {{ic_name}}_update({{ic_name|upper|concat}}State *s);
static void {{ic_name}}_reset(DeviceState *d);

static uint64_t {{ic_name}}_read(void *opaque, hwaddr offset, unsigned size);
static void {{ic_name}}_write(void *opaque, hwaddr offset, uint64_t val, unsigned size);

static void {{ic_name}}_init(Object *obj);
static void {{ic_name}}_class_init(ObjectClass *kclass, void *data);
static void {{ic_name}}_register_types(void);

static void {{ic_name}}_set_irq(void *opaque, int irq, int level) {
    {{ic_name|upper|concat}}State *s = {{ic_name|upper}}(opaque);
    s->irq_level_0 = deposit32(s->irq_level_0, irq, 1, level != 0);
    {{ic_name}}_update(s);
}

static uint64_t {{ic_name}}_read(void *opaque, hwaddr offset, unsigned size) {
    {{ic_name|upper|concat}}State *s = opaque;
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
        return 0;
    }
    return res;
}

static void {{ic_name}}_write(void *opaque, hwaddr offset, uint64_t val, unsigned size) {
    {{ic_name|upper|concat}}State *s = opaque;

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

static void {{ic_name}}_update({{ic_name|upper|concat}}State *s) {
    bool set = false;

    set = (s->irq_level_0 & s->fiq_enable_0);
    qemu_set_irq(s->fiq, set);
    set = (s->irq_level_0 & s->irq_enable_0);
    qemu_set_irq(s->irq, set);
}

static const MemoryRegionOps {{ic_name}}_ops = {
    .read = {{ic_name}}_read,
    .write = {{ic_name}}_write,
    .endianness = DEVICE_NATIVE_ENDIAN,
    .valid.min_access_size = 4,
    .valid.max_access_size = 4,
};

static void {{ic_name}}_init(Object *obj) {
    {{ic_name|upper|concat}}State *s = {{ic_name|upper}}(obj);

    /* initialize the mmio */
    memory_region_init_io(&s->mmio, obj, &{{ic_name}}_ops, s, TYPE_{{ic_name|upper}}, {{ic_name|upper}}_RAM_SIZE);
    sysbus_init_mmio(SYS_BUS_DEVICE(s), &s->mmio);

    /* initialize the interrupt input */
    qdev_init_gpio_in_named(DEVICE(s), {{ic_name}}_set_irq, {{ic_name|upper}}_IRQ, {{ic_name|upper}}_N_IRQS);

    /* initialize the irq/fip to cpu */
    qdev_init_gpio_out_named(DEVICE(s), &s->irq, "irq", 1);
    qdev_init_gpio_out_named(DEVICE(s), &s->fiq, "fiq", 1);
}

static void {{ic_name}}_reset(DeviceState *d) {
    {{ic_name|upper|concat}}State *s = {{ic_name|upper}}(d);
    {% for i in i_irqs %}{% for n in l_irqs %}
    s->irq_level_{{i}} = 0;
    s->irq_enable_{{i}} = 0;
    s->fiq_enable_{{i}} = 0;{% endfor %}{% endfor %}
}

static void {{ic_name}}_class_init(ObjectClass *klass, void *data) {
    DeviceClass *dc = DEVICE_CLASS(klass);

    /* dc->fw_name = ; */
    /* dc->desc = ; */
    /* dc->props = ; */
    /* dc->user_creatable = ; */
    /* dc->hotpluggable = ; */
    dc->reset = {{ic_name}}_reset;
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
    .instance_size = sizeof({{ic_name|upper|concat}}State),
    .instance_init = {{ic_name}}_init,
    /* .class_size = sizeof(SysBusDeviceClass), */
    .class_init = {{ic_name}}_class_init,
};

static void {{ic_name}}_register_types(void) {
    type_register_static(&{{ic_name}}_type_info);
}

type_init({{ic_name}}_register_types)