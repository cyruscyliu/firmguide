{{license}}

#include "qemu/osdep.h"
#include "qemu/log.h"
#include "qapi/error.h"
#include "target/arm/cpu.h"
#include "hw/arm/{{soc_name}}.h"
#include "hw/char/serial.h"
#include "exec/address-spaces.h"

{% for device in bamboo %}static void {{device.name}}_update(void *opaque);
static uint64_t {{device.name}}_read(void *opaque, hwaddr offset, unsigned size);
static void {{device.name}}_write(void *opaque, hwaddr offset, uint64_t val, unsigned size);
{% endfor %}
static void {{soc_name}}_init(Object *obj);
static void {{soc_name}}_realize(DeviceState *dev, Error **errp);
static void {{soc_name}}_reset(void *opaque);

static void {{soc_name}}_class_init(ObjectClass *oc, void *data);
static void {{soc_name}}_register_types(void);

{% for device in bamboo %}static void {{device.name}}_update(void *opaque) 
{
    /* {{soc_name|upper|concat}}State *s = opaque; */
}

static uint64_t {{device.name}}_read(void *opaque, hwaddr offset, unsigned size) 
{
    {{soc_name|upper|concat}}State *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    {% for register in device.registers %}case {{register.name|upper}}:
        res = s->{{register.name}};
        break;
    {% endfor %}}
    return res;
}

static void {{device.name}}_write(void *opaque, hwaddr offset, uint64_t val, unsigned size) 
{
    {{soc_name|upper|concat}}State *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    {% for register in device.registers %}case {{register.name|upper}}:
        s->{{register.name}} = val;
        break;
    {% endfor %}}
    {{device.name}}_update(s);
}

static const MemoryRegionOps {{device.name}}_ops = {
    .read = {{device.name}}_read,
    .write = {{device.name}}_write,
    .endianness = DEVICE_NATIVE_ENDIAN,
};

{% endfor %}static void {{soc_name}}_reset(void *opaque)
{
    {{soc_name|upper|concat}}State *s = opaque;
    {% for device in bamboo %}{% for register in device.registers %}
    s->{{register.name}} = {{register.value}};{% endfor %}{% endfor %}
}

static void {{soc_name}}_init(Object *obj) 
{
    {{soc_name|upper}}State *s = {{soc_name|upper}}(obj);

    /* initialize cpus and add the cpu as soc's child */
    s->cpu_type = ARM_CPU_TYPE_NAME("{{cpu_type}}");
    s->cpu = ARM_CPU(object_new(s->cpu_type));

    /* initialize bamboo device registers */{% for device in bamboo %}
    /* initialize {{device.name}} registers */
    memory_region_init_io(&s->{{device.name}}_mmio, obj,
        &{{device.name}}_ops, s, TYPE_{{soc_name|upper}}, {{device.name|upper}}_MMIO_SIZE);
    sysbus_init_mmio(SYS_BUS_DEVICE(s), &s->{{device.name}}_mmio);
    {% endfor %}{% if timer %}

    /* initialize the timer */
    sysbus_init_child_obj(
        obj, "timer", &s->timer, sizeof(s->timer), TYPE_{{timer_name|upper}});
    {% endif %}
    /* initialize the bridge */
    sysbus_init_child_obj(
        obj, "bridge", &s->bridge, sizeof(s->bridge), TYPE_{{bridge_name|upper}});{% if timer %}

    object_property_add_const_link(OBJECT(&s->bridge), "timer", OBJECT(&s->timer), &error_abort);
    {% endif %}{% if ic %}
    /* initialize the interrupt controller */
    sysbus_init_child_obj(
        obj, "ic", &s->ic, sizeof(s->ic), TYPE_{{ic_name|upper}});
    {% endif %}{% if ic %}
    object_property_add_const_link(OBJECT(&s->ic), "bridge", OBJECT(&s->bridge), &error_abort);{% endif %}

    /* register reset for {{soc_name}} */
    // qemu_register_reset({{soc_name}}_reset, s);
}

static void {{soc_name}}_realize(DeviceState *dev, Error **errp) 
{
    {{soc_name|upper}}State *s = {{soc_name|upper}}(dev);
    Error *err = NULL;{% if timer %}

    /* realize the timer */
    object_property_set_bool(OBJECT(&s->timer), true, "realized", &err);
    if (err != NULL) {
        error_propagate(errp, err);
        return;
    }
    sysbus_mmio_map(SYS_BUS_DEVICE(&s->timer), 0, {{timer_name|upper}}_MMIO_BASE);
    {% endif %}
    /* realize the bridge  */
    object_property_set_bool(OBJECT(&s->bridge), true, "realized", &err);
    if (err) {
        error_propagate(errp, err);
        return;
    }
    sysbus_mmio_map(SYS_BUS_DEVICE(&s->bridge), 0, {{bridge_name|upper}}_MMIO_BASE);{% if ic %}

    /* realize the interrupt controller */
    object_property_set_bool(OBJECT(&s->ic), true, "realized", &err);
    if (err) {
        error_propagate(errp, err);
        return;
    }
    sysbus_mmio_map(SYS_BUS_DEVICE(&s->ic), 0, {{ic_name|upper}}_MMIO_BASE);
    {% endif %}{% if ic %}
    /* attach the uart to 16550A(8250) */
    if (serial_hd(0)) {
        serial_mm_init(get_system_memory(), {{uart_name|upper}}_MMIO_BASE, 2,
                       qdev_get_gpio_in_named(DEVICE(&s->ic), {{ic_name|upper}}_IRQ, 3),
                       115200, serial_hd(0), DEVICE_LITTLE_ENDIAN);
    }{% endif %}

    /* realize the cpu */
    object_property_set_bool(OBJECT(s->cpu), true, "realized", &err);
    if (err) {
        error_propagate(errp, err);
        return;
    }
    /* connect irq/fiq outputs from the interrupt controller to the cpu */
    qdev_connect_gpio_out_named(DEVICE(&s->ic), "irq", 0,
            qdev_get_gpio_in(DEVICE(s->cpu), ARM_CPU_IRQ));
}

static void {{soc_name}}_class_init(ObjectClass *oc, void *data) 
{
    DeviceClass *dc = DEVICE_CLASS(oc);

    /* dc->fw_name = ; */
    /* dc->desc = ; */
    /* dc->props = ; */
    /* dc->user_creatable = ; */
    /* dc->hotpluggable = ; */
    /* dc->reset = ; */
    dc->realize = {{soc_name}}_realize;
    /* dc->unrealize = ; */
    /* dc->vmsd = ; */
    /* dc->bus_type = ; */

    /* SysBusDeviceClass sbc = SYS_BUS_DEVICE_CLASS(klass); */

    /* sbc->explicit_ofw_unit_address = ; */
    /* sbc->connect_irq_notifier = ; */
}

static const TypeInfo {{soc_name}}_type_info = {
    .name = TYPE_{{soc_name|upper}},
    .parent = TYPE_SYS_BUS_DEVICE,
    .instance_size = sizeof({{soc_name|upper}}State),
    .instance_init = {{soc_name}}_init,
    /* .class_size = sizeof(SysBusDeviceClass), */
    .class_init = {{soc_name}}_class_init,
};

static void {{soc_name}}_register_types(void) 
{
    type_register_static(&{{soc_name}}_type_info);
}

type_init({{soc_name}}_register_types);
