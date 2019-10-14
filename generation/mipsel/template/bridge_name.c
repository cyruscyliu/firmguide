{{license}}

#include "qemu/osdep.h"
#include "qemu/log.h"
#include "qapi/error.h"
#include "hw/mips/{{bridge_name}}.h"

static void {{bridge_name}}_realize(DeviceState *dev, Error **errp);

static void {{bridge_name}}_init(Object *obj);
static void {{bridge_name}}_class_init(ObjectClass *oc, void *data);
static void {{bridge_name}}_register_types(void);

static void {{bridge_name}}_update(void *opaque)
{
    {{bridge_name|upper|concat}}State *s = opaque;
}

static uint64_t {{bridge_name}}_read(void *opaque, hwaddr offset, unsigned size)
{
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

static void {{bridge_name}}_write(void *opaque, hwaddr offset, uint64_t val, unsigned size)
{
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

static void {{bridge_name}}_init(Object *obj) 
{
    {{bridge_name|upper|concat}}State *s = {{bridge_name|upper}}(obj);

    /* initialize the bridge mmio */
    memory_region_init_io(
        &s->bridge_mmio, obj, &{{bridge_name}}_ops, s, TYPE_{{bridge_name|upper}}, {{bridge_name|upper}}_MMIO_SIZE);
    sysbus_init_mmio(SYS_BUS_DEVICE(s), &s->bridge_mmio);
}

static void {{bridge_name}}_realize(DeviceState *dev, Error **errp)
{
    {{bridge_name|upper|concat}}State *s = {{bridge_name|upper}}(dev);
    {% for register in bridge_registers %}
    s->{{register.name}} = {{register.value}};{% endfor %}
}

static void {{bridge_name}}_reset(DeviceState *d)
{
    {{bridge_name|upper|concat}}State *s = {{bridge_name|upper}}(d);
    {% for register in bridge_registers %}
    s->{{register.name}} = {{register.value}};{% endfor %}
}

static void {{bridge_name}}_class_init(ObjectClass *oc, void *data)
{
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

static void {{bridge_name}}_register_types(void)
{
    type_register_static(&{{bridge_name}}_type_info);
}

type_init({{bridge_name}}_register_types)
