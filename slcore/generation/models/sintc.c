{{license}}

#include "qemu/osdep.h"
#include "qemu/log.h"
#include "qapi/error.h"
#include "hw/intc/sintc.h"
#include "qemu/timer.h"

static void sintc_update(void *opaque)
{
    SIntCState *s = opaque;
    int64_t now = qemu_clock_get_ns(QEMU_CLOCK_VIRTUAL);
    timer_mod(s->timer, 0x10000000 + now); /* 100HZ */
    if (s->clear) {
        qemu_set_irq(s->irq, 0);
        s->interrupt_cause_register = deposit32(s->interrupt_cause_register, {{timer_irq}}, 1, 0);
        s->clear = false;
    } else {
        if (s->interrupt_cause_register & s->interrupt_mask_register) {
            qemu_set_irq(s->irq, 1);
        }
    }
}

static void tick_callback(void *opaque)
{
    SIntCState *s = opaque;
    s->interrupt_cause_register = deposit32(s->interrupt_cause_register, {{timer_irq}}, 1, 1);
    sintc_update(s);
}

static uint64_t sintc_read(void *opaque, hwaddr offset, unsigned size)
{
    SIntCState *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        return 0;
    case INTERRUPT_CAUSE_REGISTER:
        res = s->interrupt_cause_register;
        break;
    case INTERRUPT_MASK_REGISTER:
        res = s->interrupt_mask_register;
        break;
    }
    return res;
}

static void sintc_write(void *opaque, hwaddr offset, uint64_t val, unsigned size)
{
    SIntCState *s = opaque;

    switch (offset) {
    default:
        return;
    case INTERRUPT_CAUSE_REGISTER:
        s->interrupt_cause_register = val;
        break;
    case INTERRUPT_MASK_REGISTER:
        s->interrupt_mask_register = val;
        break;
    case INTERRUPT_CLEAR_REGISTER:
        s->clear = true;
        break;
    }
    sintc_update(s);
}

static const MemoryRegionOps sintc_ops = {
    .read = sintc_read,
    .write = sintc_write,
    .endianness = DEVICE_NATIVE_ENDIAN,
};

static void sintc_init(Object *obj)
{
    SIntCState *s = SINTC(obj);

    /* initialize the mmio */
    memory_region_init_io(&s->mmio, obj, &sintc_ops, s, TYPE_SINTC, SINTC_MMIO_SIZE);
    sysbus_init_mmio(SYS_BUS_DEVICE(s), &s->mmio);

    /* initialize the irq/fip to cpu */
    qdev_init_gpio_out_named(DEVICE(s), &s->irq, "irq", 1);

    /* initialize the timer */
    s->timer = timer_new_ns(QEMU_CLOCK_VIRTUAL, tick_callback, s);
}

static void sintc_reset(DeviceState *dev)
{
    SIntCState *s = SINTC(dev);
    
    s->interrupt_cause_register = 0;
    s->interrupt_mask_register = 0;
    s->clear = false;
}

static void sintc_class_init(ObjectClass *klass, void *data)
{
    DeviceClass *dc = DEVICE_CLASS(klass);

    /* dc->fw_name = ; */
    /* dc->desc = ; */
    /* dc->props = ; */
    /* dc->user_creatable = ; */
    /* dc->hotpluggable = ; */
    dc->reset = sintc_reset;
    /* dc->realize = ; */
    /* dc->unrealize = ; */
    /* dc->vmsd = ; */
    /* dc->bus_type = ; */

    /* SysBusDeviceClass sbc = SYS_BUS_DEVICE_CLASS(klass); */

    /* sbc->explicit_ofw_unit_address = ; */
    /* sbc->connect_irq_notifier = ; */
}

static TypeInfo sintc_type_info = {
    .name = TYPE_SINTC,
    .parent = TYPE_SYS_BUS_DEVICE,
    .instance_size = sizeof(SIntCState),
    .instance_init = sintc_init,
    /* .class_size = sizeof(SysBusDeviceClass), */
    .class_init = sintc_class_init,
};

static void sintc_register_types(void)
{
    type_register_static(&sintc_type_info);
}

type_init(sintc_register_types)
