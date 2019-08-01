{{license}}

#include "qemu/osdep.h"
#include "qemu/log.h"
#include "hw/gpio/{{gpio_name}}.h"

static void {{gpio_name}}_update(void *opaque);
static void {{gpio_name}}_reset(DeviceState *dev);

static uint64_t {{gpio_name}}_read(void *opaque, hwaddr offset, unsigned size);
static void {{gpio_name}}_write(void *opaque, hwaddr offset, uint64_t val, unsigned size);

static void {{gpio_name}}_init(Object *obj);
static void {{gpio_name}}_class_init(ObjectClass *klass, void *data);
static void {{gpio_name}}_register_types(void);

static void {{gpio_name}}_update(void *opaque) {
    /* {{gpio_name|upper|concat}}State *s = opaque; */
}

static uint64_t {{gpio_name}}_read(void *opaque, hwaddr offset, unsigned size) {
    {{gpio_name|upper|concat}}State *s = ({{gpio_name|upper|concat}}State *)opaque;

    uint64_t res = 0;

    switch (offset) {
    case GPIO_DOR: /* GPIO Data Out Register */
        /* do nothing */
        break;
    case GPIO_DOECR: /* GPIO Data Out Enable Control Register */
        /* do nothing */
        break;
    case GPIO_BER: /* GPIO Blink Enable Register */
        /* do nothing */
        break;
    case GPIO_DIPR: /* GPIO Data In Polarity Register */
        /* do nothing */
        break;
    case GPIO_DIR: /* GPIO Data In Register */
        /* do nothing */
        break;
    case GPIO_ICR: /* GPIO Interrupt Cause Register */
        res = s->icr;
        break;
    case GPIO_IMR: /* GPIO Interrupt Mask Register */
        res = s->imr;
        break;
    case GPIO_ILMR: /* GPIO Interrupt Level Mask Register */
        res = s->ilmr;
        break;
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset 0x%"HWADDR_PRIx"\n", __func__, offset);
        res = 0;
    }
    return res;
}

static void {{gpio_name}}_write(void *opaque, hwaddr offset, uint64_t val, unsigned size) {
    {{gpio_name|upper|concat}}State *s = opaque;

    switch (offset) {
    case GPIO_DOR: /* GPIO Data Out Register */
        /* do nothing */
        break;
    case GPIO_DOECR: /* GPIO Data Out Enable Control Register */
        /* do nothing */
        break;
    case GPIO_BER: /* GPIO Blink Enable Register */
        /* do nothing */
        break;
    case GPIO_DIPR: /* GPIO Data In Polarity Register */
        /* do nothing */
        break;
    case GPIO_DIR: /* GPIO Data In Register */
        /* do nothing */
        break;
    case GPIO_ICR: /* GPIO Interrupt Cause Register */
        s->icr = val;
        break;
    case GPIO_IMR: /* GPIO Interrupt Mask Register */
        s->imr = val;
        break;
    case GPIO_ILMR: /* GPIO Interrupt Level Mask Register */
        s->ilmr = val;
        break;
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset 0x%"HWADDR_PRIx"\n", __func__, offset);
    }
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
    memory_region_init_io(&s->mmio, obj, &{{gpio_name}}_ops, s, "{{gpio_name}}", {{gpio_name|upper}}_RAM_SIZE);
    sysbus_init_mmio(SYS_BUS_DEVICE(s), &s->mmio);

    /* initialize the output */
    qdev_init_gpio_out(DEVICE(s), s->out, {{gpio_n}});
}

static void {{gpio_name}}_reset(DeviceState *dev) {
    {{gpio_name|upper|concat}}State *s = {{gpio_name|upper}}(dev);

    s->icr = 0;
    s->imr = 0;
    s->ilmr = 0;
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