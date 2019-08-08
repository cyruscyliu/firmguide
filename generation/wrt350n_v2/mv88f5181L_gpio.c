/* 
 * automatically generated, don't change
 */

#include "qemu/osdep.h"
#include "qemu/log.h"
#include "hw/gpio/mv88f5181L_gpio.h"

static void mv88f5181L_gpio_update(void *opaque);
static void mv88f5181L_gpio_set_irq(void *opaque, int irq, int level);
static uint64_t mv88f5181L_gpio_read(void *opaque, hwaddr offset, unsigned size);
static void mv88f5181L_gpio_write(void *opaque, hwaddr offset, uint64_t val, unsigned size);

static void mv88f5181L_gpio_reset(DeviceState *dev);

static void mv88f5181L_gpio_init(Object *obj);
static void mv88f5181L_gpio_class_init(ObjectClass *klass, void *data);
static void mv88f5181L_gpio_register_types(void);

static void mv88f5181L_gpio_update(void *opaque) {
    /* MV88F5181LGPIOState *s = opaque; */
}

static void mv88f5181L_gpio_set_irq(void *opaque, int irq, int level) {
    /* MV88F5181LGPIOState *s = opaque; */
}

static uint64_t mv88f5181L_gpio_read(void *opaque, hwaddr offset, unsigned size) {
    MV88F5181LGPIOState *s = (MV88F5181LGPIOState *)opaque;

    uint64_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset 0x%"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case GPIO_DATA_OUT_REGISTER:
        res = s->gpio_data_out_register;
        break;
    case GPIO_DATA_OUT_ENABLE_CONTROL_REGISTER:
        res = s->gpio_data_out_enable_control_register;
        break;
    case GPIO_BLINK_ENABLE_REGISTER:
        res = s->gpio_blink_enable_register;
        break;
    case GPIO_DATA_IN_POLARITY_REGISTER:
        res = s->gpio_data_in_polarity_register;
        break;
    case GPIO_DATA_IN_REGISTER:
        res = s->gpio_data_in_register;
        break;
    case GPIO_INTERRUPT_CAUSE_REGISTER:
        res = s->gpio_interrupt_cause_register;
        break;
    case GPIO_INTERRUPT_MASK_REGISTER:
        res = s->gpio_interrupt_mask_register;
        break;
    case GPIO_INTERRUPT_LEVEL_MASK_REGISTER:
        res = s->gpio_interrupt_level_mask_register;
        break;
    }
    return res;
}

static void mv88f5181L_gpio_write(void *opaque, hwaddr offset, uint64_t val, unsigned size) {
    MV88F5181LGPIOState *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset 0x%"HWADDR_PRIx"\n", __func__, offset);
        return;
    case GPIO_DATA_OUT_REGISTER:
        s->gpio_data_out_register = val;
        break;
    case GPIO_DATA_OUT_ENABLE_CONTROL_REGISTER:
        s->gpio_data_out_enable_control_register = val;
        break;
    case GPIO_BLINK_ENABLE_REGISTER:
        s->gpio_blink_enable_register = val;
        break;
    case GPIO_DATA_IN_POLARITY_REGISTER:
        s->gpio_data_in_polarity_register = val;
        break;
    case GPIO_DATA_IN_REGISTER:
        s->gpio_data_in_register = val;
        break;
    case GPIO_INTERRUPT_CAUSE_REGISTER:
        s->gpio_interrupt_cause_register = val;
        break;
    case GPIO_INTERRUPT_MASK_REGISTER:
        s->gpio_interrupt_mask_register = val;
        break;
    case GPIO_INTERRUPT_LEVEL_MASK_REGISTER:
        s->gpio_interrupt_level_mask_register = val;
        break;
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
    memory_region_init_io(&s->gpio_mmio, obj, &mv88f5181L_gpio_ops, s, "mv88f5181L_gpio", MV88F5181L_GPIO_MMIO_SIZE);
    sysbus_init_mmio(SYS_BUS_DEVICE(s), &s->gpio_mmio);

    /* initialize the irq */
    for (int i; i < 4; ++i) {
        sysbus_init_irq(SYS_BUS_DEVICE(s), &s->irq[i]);
    }

    /* initialize the input/output */
    qdev_init_gpio_in(DEVICE(s), mv88f5181L_gpio_set_irq, 26);
    qdev_init_gpio_out(DEVICE(s), s->out, 26);
}

static void mv88f5181L_gpio_reset(DeviceState *dev) {
    MV88F5181LGPIOState *s = MV88F5181L_GPIO(dev);
    
    s->gpio_data_out_register = 0x0 << 0 | 0x0 << 26;
    s->gpio_data_out_enable_control_register = 0xFFFF << 0 | 0x0 << 26;
    s->gpio_blink_enable_register = 0x0 << 0 | 0x0 << 26;
    s->gpio_data_in_polarity_register = 0x0 << 0 | 0x0 << 26;
    s->gpio_data_in_register = 0x0 << 0 | 0x0 << 26;
    s->gpio_interrupt_cause_register = 0x0 << 0 | 0x0 << 26;
    s->gpio_interrupt_mask_register = 0x0 << 0 | 0x0 << 26;
    s->gpio_interrupt_level_mask_register = 0x0 << 0 | 0x0 << 26;
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