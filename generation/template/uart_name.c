{{license}}

#include "qemu/osdep.h"
#include "qemu/log.h"
#include "hw/char/{{uart_name}}.h"
#include "chardev/char-fe.h"

static int {{uart_name}}_can_receive(void *opaque);
static void {{uart_name}}_receive(void *opaque, const uint8_t *buf, int size);
static void {{uart_name}}_event(void *opaque, int event);

static void {{uart_name}}_update(void *opaque);
static void {{uart_name}}_reset(DeviceState *dev);

static uint64_t {{uart_name}}_read(void *opaque, hwaddr offset, unsigned size);
static void {{uart_name}}_write(void *opaque, hwaddr offset, uint64_t val, unsigned size);

static void {{uart_name}}_init(Object *obj);
static void {{uart_name}}_class_init(ObjectClass *klass, void *data);
static void {{uart_name}}_register_types(void);

static void {{uart_name}}_update(void *opaque) {
    /* {{uart_name|upper|concat}}State *s = opaque; */
}

static int {{uart_name}}_can_receive(void *opaque) {
    /* {{uart_name|upper|concat}}State *s = opaque; */

    return 0;
}

static void {{uart_name}}_receive(void *opaque, const uint8_t *buf, int size) {
    {{uart_name|upper|concat}}State *s = opaque;
    {{uart_name}}_update(s);
}

static void {{uart_name}}_event(void *opaque, int event) {
}

static uint64_t {{uart_name}}_read(void *opaque, hwaddr offset, unsigned size) {
    {{uart_name|upper|concat}}State *s = ({{uart_name|upper|concat}}State *)opaque;

    uint64_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset 0x%"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    {% for register in uart_registers %}case {{register.name|upper}}:
        res = s->{{register.name}};
        break;
    {% endfor %}}
    return res;
}

static void {{uart_name}}_write(void *opaque, hwaddr offset, uint64_t val, unsigned size) {
    {{uart_name|upper|concat}}State *s = ({{uart_name|upper|concat}}State *)opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset 0x%"HWADDR_PRIx"\n", __func__, offset);
        return;
    {% for register in uart_registers %}case {{register.name|upper}}:
        s->{{register.name}} = val;
        break;
    {% endfor %}}
    {{uart_name}}_update(s);
}

static const MemoryRegionOps {{uart_name}}_ops = {
    .read = {{uart_name}}_read,
    .write = {{uart_name}}_write,
    .endianness = DEVICE_NATIVE_ENDIAN,
};

static void {{uart_name}}_init(Object *obj) {
    {{uart_name|upper|concat}}State *s = {{uart_name|upper}}(obj);

    /* initialize the mmio */
    memory_region_init_io(&s->mmio, obj, &{{uart_name}}_ops, s, "{{uart_name}}", {{uart_name|upper}}_MMIO_SIZE);
    sysbus_init_mmio(SYS_BUS_DEVICE(s), &s->mmio);

    /* initialize the irq */
    sysbus_init_irq(SYS_BUS_DEVICE(s), &s->irq);

    /* initialize the chardev */
    qemu_chr_fe_set_handlers(&s->chr, {{uart_name}}_can_receive,
        {{uart_name}}_receive, {{uart_name}}_event, NULL, s, NULL, true);
}

static void {{uart_name}}_reset(DeviceState *dev) {
    {{uart_name|upper|concat}}State *s = {{uart_name|upper}}(dev);
    {% for register in uart_registers %}
    s->{{register.name}} = 0;{% endfor %}
}

static void {{uart_name}}_class_init(ObjectClass *klass, void *data) {
    DeviceClass *dc = DEVICE_CLASS(klass);

    /* dc->fw_name = ; */
    /* dc->desc = ; */
    /* dc->props = ; */
    /* dc->user_creatable = ; */
    /* dc->hotpluggable = ; */
    dc->reset = {{uart_name}}_reset;
    /* dc->realize = ; */
    /* dc->unrealize = ; */
    /* dc->vmsd = ; */
    /* dc->bus_type = ; */

    /* SysBusDeviceClass sbc = SYS_BUS_DEVICE_CLASS(klass); */

    /* sbc->explicit_ofw_unit_address = ; */
    /* sbc->connect_irq_notifier = ; */
}

static const TypeInfo {{uart_name}}_info = {
    .name = TYPE_{{uart_name|upper}},
    .parent = TYPE_SYS_BUS_DEVICE,
    .instance_size = sizeof({{uart_name|upper|concat}}State),
    .instance_init = {{uart_name}}_init,
    /* .class_zie = sizeof(SysBusDeviceClass), */
    .class_init = {{uart_name}}_class_init,
};

static void {{uart_name}}_register_types(void) {
    type_register_static(&{{uart_name}}_info);
}

type_init({{uart_name}}_register_types)