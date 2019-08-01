/* 
 * automatically generated, don't change
 */

#include "qemu/osdep.h"
#include "qemu/log.h"
#include "hw/gpio/mv88f5181L_gpio.h"

static void mv88f5181L_gpio_update(void *opaque);
static void mv88f5181L_gpio_reset(DeviceState *dev);

static uint64_t mv88f5181L_gpio_read(void *opaque, hwaddr offset, unsigned size);
static void mv88f5181L_gpio_write(void *opaque, hwaddr offset, uint64_t val, unsigned size);

static void mv88f5181L_gpio_init(Object *obj);
static void mv88f5181L_gpio_class_init(ObjectClass *klass, void *data);
static void mv88f5181L_gpio_register_types(void);

static void mv88f5181L_gpio_update(void *opaque) {
    /* MV88F5181LGPIOState *s = opaque; */
}

static uint64_t mv88f5181L_gpio_read(void *opaque, hwaddr offset, unsigned size) {
    MV88F5181LGPIOState *s = (MV88F5181LGPIOState *)opaque;

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

static void mv88f5181L_gpio_write(void *opaque, hwaddr offset, uint64_t val, unsigned size) {
    MV88F5181LGPIOState *s = opaque;

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
    mv88f5181L_gpio_update(s);
    return;
}

static const MemoryRegionOps mv88f5181L_gpio_ops = {
    .read = mv88f5181L_gpio_read,
    .write = mv88f5181L_gpio_write,
    .endianness = DEVICE_NATIVE_ENDIAN,
};

static void mv88f5181L_gpio_init(Object *obj) {
    MV88F5181LGPIOState *s = MV88F5181L_GPIO(obj);

    /* initialize the mmio */
    memory_region_init_io(&s->mmio, obj, &mv88f5181L_gpio_ops, s, "mv88f5181L_gpio", MV88F5181L_GPIO_RAM_SIZE);
    sysbus_init_mmio(SYS_BUS_DEVICE(s), &s->mmio);

    /* initialize the output */
    qdev_init_gpio_out(DEVICE(s), s->out, 32);
}

static void mv88f5181L_gpio_reset(DeviceState *dev) {
    MV88F5181LGPIOState *s = MV88F5181LGPIO(dev);

    s->icr = 0;
    s->imr = 0;
    s->ilmr = 0;
}

static void mv88f5181L_gpio_class_init(ObjectClass *klass, void *data) {
    DeviceClass *dc = DEVICE_CLASS(klass);

    /* dc->fw_name = ; */
    /* dc->desc = ; */
    /* dc->props = ; */
    /* dc->user_creatable = ; */
    /* dc->hotpluggable = ; */
    dc->reset = mv88f5181L_gpio_reset;
    /* dc->realize = ; */
    /* dc->unrealize = ; */
    /* dc->vmsd = ; */
    /* dc->bus_type = ; */

    /* SysBusDeviceClass sbc = SYS_BUS_DEVICE_CLASS(klass); */

    /* sbc->explicit_ofw_unit_address = ; */
    /* sbc->connect_irq_notifier = ; */
}

static const TypeInfo mv88f5181L_gpio_info = {
    .name = TYPE_MV88F5181L_GPIO,
    .parent = TYPE_SYS_BUS_DEVICE,
    .instance_size = sizeof(MV88F5181LGPIOState),
    .instance_init = mv88f5181L_gpio_init,
    /* .class_zie = sizeof(SysBusDeviceClass), */
    .class_init = mv88f5181L_gpio_class_init,
};

static void mv88f5181L_gpio_register_types(void) {
    type_register_static(&mv88f5181L_gpio_info);
}

type_init(mv88f5181L_gpio_register_types)