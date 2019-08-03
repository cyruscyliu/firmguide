{{license}}

#include "qemu/osdep.h"
#include "qemu/log.h"
#include "qapi/error.h"
#include "hw/arm/{{machine_name}}.h"
#include "hw/arm/{{peripheral_name}}.h"

static void {{peripheral_name}}_realize(DeviceState *dev, Error **errp);

static void {{peripheral_name}}_init(Object *obj);
static void {{peripheral_name}}_class_init(ObjectClass *oc, void *data);
static void {{peripheral_name}}_register_types(void);

static void {{bridge_name}}_update(void *opaque) {
    {{peripheral_name|upper|concat}}State *s = opaque;
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
    {{peripheral_name|upper|concat}}State *s = opaque;
    s->bridge_interrupt_cause_register &= 0x1;
    s->bridge_interrupt_cause_register = deposit32(s->bridge_interrupt_cause_register, irq, 1, level);
    {{bridge_name}}_update(s);
}

static uint64_t {{bridge_name}}_read(void *opaque, hwaddr offset, unsigned size) {
    {{peripheral_name|upper|concat}}State *s = opaque;
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
    {{peripheral_name|upper|concat}}State *s = opaque;

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

static void {{peripheral_name}}_init(Object *obj) {
    {{peripheral_name|upper|concat}}State *s = {{peripheral_name|upper}}(obj);

    /* initialize the bridge mmio */
    memory_region_init_io(&s->bridge_mmio, obj, &{{bridge_name}}_ops, s, TYPE_{{peripheral_name|upper}}, {{bridge_name|upper}}_RAM_SIZE);
    sysbus_init_mmio(SYS_BUS_DEVICE(s), &s->bridge_mmio);

    /* initialize the bridge irq */
    sysbus_init_irq(SYS_BUS_DEVICE(s), &s->irq);

    /* initialize GPIO in */
    qdev_init_gpio_in_named(DEVICE(s), {{bridge_name}}_set_irq, {{bridge_name|upper}}_IRQ, 32);

    /* initialize the timer */
    sysbus_init_child_obj(obj, "timer", &s->timer, sizeof(s->timer), TYPE_{{timer_name|upper}});

    /* initialize the uart */
    sysbus_init_child_obj(obj, "uart", &s->uart, sizeof(s->uart), TYPE_{{uart_name|upper}});

    /* initialize the gpio */
    sysbus_init_child_obj(obj, "gpio", &s->gpio, sizeof(s->gpio), TYPE_{{gpio_name|upper}});

    /* initialize the pcie */
    sysbus_init_child_obj(obj, "pcie", &s->pcie, sizeof(s->pcie), TYPE_{{pcie_name|upper}});
}

static void {{peripheral_name}}_realize(DeviceState *dev, Error **errp) {
    {{peripheral_name|upper|concat}}State *s = {{peripheral_name|upper}}(dev);
    Error *err = NULL;

    /* realize the timer */
    object_property_set_bool(OBJECT(&s->timer), true, "realized", &err);
    if (err != NULL) {
        error_propagate(errp, err);
        return;
    }
    sysbus_mmio_map(SYS_BUS_DEVICE(&s->timer), 0, {{timer_name|upper}}_RAM_BASE);

    /* connect the timer to the bridge */
    sysbus_connect_irq(SYS_BUS_DEVICE(&s->timer), 0,
        qdev_get_gpio_in_named(DEVICE(s), {{bridge_name|upper}}_IRQ, 1));
    sysbus_connect_irq(SYS_BUS_DEVICE(&s->timer), 1,
        qdev_get_gpio_in_named(DEVICE(s), {{bridge_name|upper}}_IRQ, 2));

    /* realize the uart */
    object_property_set_bool(OBJECT(&s->uart), true, "realized", &err);
    if (err != NULL) {
        error_propagate(errp, err);
        return;
    }
    sysbus_mmio_map(SYS_BUS_DEVICE(&s->uart), 0, {{uart_name|upper}}_RAM_BASE);

    /* realize the uart */
    object_property_set_bool(OBJECT(&s->gpio), true, "realized", &err);
    if (err != NULL) {
        error_propagate(errp, err);
        return;
    }
    sysbus_mmio_map(SYS_BUS_DEVICE(&s->gpio), 0, {{gpio_name|upper}}_RAM_BASE);

    /* realize the pcie */
    object_property_set_bool(OBJECT(&s->pcie), true, "realized", &err);
    if (err != NULL) {
        error_propagate(errp, err);
        return;
    }
    sysbus_mmio_map(SYS_BUS_DEVICE(&s->pcie), 0, {{pcie_name|upper}}_RAM_BASE);
}

static void {{bridge_name}}_reset(DeviceState *d) {
    {{peripheral_name|upper|concat}}State *s = {{peripheral_name|upper}}(d);
    {% for register in bridge_registers %}
    s->{{register.name}} = 0;{% endfor %}
}

static void {{peripheral_name}}_class_init(ObjectClass *oc, void *data) {
    DeviceClass *dc = DEVICE_CLASS(oc);

    /* dc->fw_name = ; */
    /* dc->desc = ; */
    /* dc->props = ; */
    /* dc->user_creatable = ; */
    /* dc->hotpluggable = ; */
    dc->reset = {{bridge_name}}_reset;
    dc->realize = {{peripheral_name}}_realize;
    /* dc->unrealize = ; */
    /* dc->vmsd = ; */
    /* dc->bus_type = ; */

    /* SysBusDeviceClass sbc = SYS_BUS_DEVICE_CLASS(klass); */

    /* sbc->explicit_ofw_unit_address = ; */
    /* sbc->connect_irq_notifier = ; */
}

static const TypeInfo {{peripheral_name}}_type_info = {
    .name = TYPE_{{peripheral_name|upper}},
    .parent = TYPE_SYS_BUS_DEVICE,
    .instance_size = sizeof({{peripheral_name|upper|concat}}State),
    .instance_init = {{peripheral_name}}_init,
    /* .class_size = sizeof(SysBusDeviceClass), */
    .class_init = {{peripheral_name}}_class_init,
};

static void {{peripheral_name}}_register_types(void) {
    type_register_static(&{{peripheral_name}}_type_info);
}

type_init({{peripheral_name}}_register_types)