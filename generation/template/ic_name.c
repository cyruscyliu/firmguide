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

static void {{ic_name}}_update({{ic_name|upper|concat}}State *s) {
    {{ic_name|upper|concat}}State *s = opaque;
    if (extract32(s->main_interrupt_cause_register, 0, 1)) {
        if (s->main_interrupt_cause_register & s->main_irq_interrupt_mask_register) {
            qemu_set_irq(s->irq, 1);
        }
    }
}

static void {{ic_name}}_set_irq(void *opaque, int irq, int level) {
    {{ic_name|upper|concat}}State *s = opaque;
    if (level) {
        deposit32(s->main_interrupt_cause_register, irq, 1, level);
        {{ic_name}}_update(s);
    }
}

static uint64_t {{ic_name}}_read(void *opaque, hwaddr offset, unsigned size) {
    {{ic_name|upper|concat}}State *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    {% for register in ic_registers %}case {{register.name|upper}}:
        res = s->{{register.name}};
        break;
    {% endfor %}}
    return res;
}

static void {{ic_name}}_write(void *opaque, hwaddr offset, uint64_t val, unsigned size) {
    {{ic_name|upper|concat}}State *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    {% for register in ic_registers %}case {{register.name|upper}}:
        s->{{register.name}} = val;
        break;
    }
    {% endfor %}
    {{ic_name}}_update(s);
}

static const MemoryRegionOps {{ic_name}}_ops = {
    .read = {{ic_name}}_read,
    .write = {{ic_name}}_write,
    .endianness = DEVICE_NATIVE_ENDIAN,
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
}

static void {{ic_name}}_reset(DeviceState *dev) {
    {{ic_name|upper|concat}}State *s = {{ic_name|upper}}(dev);
    {% for register in ic_registers %}
    s->{{register.name}} = 0;{% endfor %}
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