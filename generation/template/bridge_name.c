{{license}}

#include "qemu/osdep.h"
#include "qemu/log.h"
#include "qapi/error.h"
#include "hw/arm/{{bridge_name}}.h"
#include "hw/timer/{{timer_name}}.h"

static void {{bridge_name}}_realize(DeviceState *dev, Error **errp);

static void {{bridge_name}}_init(Object *obj);
static void {{bridge_name}}_class_init(ObjectClass *oc, void *data);
static void {{bridge_name}}_register_types(void);

static void {{bridge_name}}_update(void *opaque) {
    {{bridge_name|upper|concat}}State *s = opaque;
    if (extract32(s->bridge_interrupt_cause_register, 1, 1)) {
        if (s->bridge_interrupt_cause_register & s->bridge_interrupt_mask_register) {
            qemu_set_irq(s->irq, 1);
        }
    } else {
        /* clear the interrupt */
        qemu_set_irq(s->irq, 0);
    }
    if (extract32(s->bridge_interrupt_cause_register, 2, 1)) {
        if (s->bridge_interrupt_cause_register & s->bridge_interrupt_mask_register) {
            qemu_set_irq(s->irq, 1);
        }
    } else {
        /* clear the interrupt */
        qemu_set_irq(s->irq, 0);
    }
}

static void {{bridge_name}}_set_irq(void *opaque, int irq, int level) {
    {{bridge_name|upper|concat}}State *s = opaque;
    s->bridge_interrupt_cause_register &= 0x1;
    s->bridge_interrupt_cause_register = deposit32(s->bridge_interrupt_cause_register, irq, 1, level);
    {{bridge_name}}_update(s);
}

static uint64_t {{bridge_name}}_read(void *opaque, hwaddr offset, unsigned size) {
    {{bridge_name|upper|concat}}State *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    {% for register in bridge_registers %}case {{register.name|upper}}:
        res = s->{{register.name}};
        break;
    {% endfor %}}
    return res;
}

static void {{bridge_name}}_write(void *opaque, hwaddr offset, uint64_t val, unsigned size) {
    {{bridge_name|upper|concat}}State *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    {% for register in bridge_registers %}case {{register.name|upper}}:
        s->{{register.name}} = val;
        break;
    {% endfor %}}
    {{bridge_name}}_update(s);
}

static const MemoryRegionOps {{bridge_name}}_ops = {
    .read = {{bridge_name}}_read,
    .write = {{bridge_name}}_write,
    .endianness = DEVICE_NATIVE_ENDIAN,
};

static void {{bridge_name}}_init(Object *obj) {
    {{bridge_name|upper|concat}}State *s = {{bridge_name|upper}}(obj);

    /* initialize the bridge mmio */
    memory_region_init_io(
        &s->bridge_mmio, obj, &{{bridge_name}}_ops, s, TYPE_{{bridge_name|upper}}, {{bridge_name|upper}}_MMIO_SIZE);
    sysbus_init_mmio(SYS_BUS_DEVICE(s), &s->bridge_mmio);

    /* initialize the bridge irq */
    sysbus_init_irq(SYS_BUS_DEVICE(s), &s->irq);

    /* initialize GPIO in */
    qdev_init_gpio_in_named(DEVICE(s), {{bridge_name}}_set_irq, {{bridge_name|upper}}_IRQ, 32);
}

static void {{bridge_name}}_realize(DeviceState *dev, Error **errp) {
    {{bridge_name|upper|concat}}State *s = {{bridge_name|upper}}(dev);
    Object *obj;
    {{timer_name|upper|concat}}State *timer;
    Error *err = NULL;

    /* connect the timer to the bridge */
    obj = object_property_get_link(OBJECT(dev), "timer", &err) ;
    timer = {{timer_name|upper}}(obj);
    if (timer == NULL) {
        error_setg(errp, "%s: required ram link not found: %s",
                   __func__, error_get_pretty(err));
        return;
    }
    sysbus_connect_irq(SYS_BUS_DEVICE(timer), 0,
        qdev_get_gpio_in_named(DEVICE(s), {{bridge_name|upper}}_IRQ, 1));
    sysbus_connect_irq(SYS_BUS_DEVICE(timer), 1,
        qdev_get_gpio_in_named(DEVICE(s), {{bridge_name|upper}}_IRQ, 2));
}

static void {{bridge_name}}_reset(DeviceState *d) {
    {{bridge_name|upper|concat}}State *s = {{bridge_name|upper}}(d);
    {% for register in bridge_registers %}
    s->{{register.name}} = 0;{% endfor %}
}

static void {{bridge_name}}_class_init(ObjectClass *oc, void *data) {
    DeviceClass *dc = DEVICE_CLASS(oc);

    /* dc->fw_name = ; */
    /* dc->desc = ; */
    /* dc->props = ; */
    /* dc->user_creatable = ; */
    /* dc->hotpluggable = ; */
    dc->reset = {{bridge_name}}_reset;
    dc->realize = {{bridge_name}}_realize;
    /* dc->unrealize = ; */
    /* dc->vmsd = ; */
    /* dc->bus_type = ; */

    /* SysBusDeviceClass sbc = SYS_BUS_DEVICE_CLASS(klass); */

    /* sbc->explicit_ofw_unit_address = ; */
    /* sbc->connect_irq_notifier = ; */
}

static const TypeInfo {{bridge_name}}_type_info = {
    .name = TYPE_{{bridge_name|upper}},
    .parent = TYPE_SYS_BUS_DEVICE,
    .instance_size = sizeof({{bridge_name|upper|concat}}State),
    .instance_init = {{bridge_name}}_init,
    /* .class_size = sizeof(SysBusDeviceClass), */
    .class_init = {{bridge_name}}_class_init,
};

static void {{bridge_name}}_register_types(void) {
    type_register_static(&{{bridge_name}}_type_info);
}

type_init({{bridge_name}}_register_types)