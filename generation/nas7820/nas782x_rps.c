/* 
 * automatically generated, don't change
 */

#include "qemu/osdep.h"
#include "qemu/log.h"
#include "qapi/error.h"
#include "hw/arm/nas782x_rps.h"

static void nas782x_rps_realize(DeviceState *dev, Error **errp);

static void nas782x_rps_init(Object *obj);
static void nas782x_rps_class_init(ObjectClass *oc, void *data);
static void nas782x_rps_register_types(void);

static void nas782x_rps_update(void *opaque)
{
    NAS782XRPSState *s = opaque;
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

static void nas782x_rps_set_irq(void *opaque, int irq, int level)
{
    NAS782XRPSState *s = opaque;
    s->bridge_interrupt_cause_register &= 0x1;
    s->bridge_interrupt_cause_register = deposit32(s->bridge_interrupt_cause_register, irq, 1, level);
    nas782x_rps_update(s);
}

static uint64_t nas782x_rps_read(void *opaque, hwaddr offset, unsigned size)
{
    NAS782XRPSState *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case RPS_STATUS:
        res = s->rps_status;
        break;
    case RPS_RAM_STATUS:
        res = s->rps_ram_status;
        break;
    case RPS_UNMASK:
        res = s->rps_unmask;
        break;
    case RPS_MASK:
        res = s->rps_mask;
        break;
    }
    return res;
}

static void nas782x_rps_write(void *opaque, hwaddr offset, uint64_t val, unsigned size)
{
    NAS782XRPSState *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case RPS_STATUS:
        s->rps_status = val;
        break;
    case RPS_RAM_STATUS:
        s->rps_ram_status = val;
        break;
    case RPS_UNMASK:
        s->rps_unmask = val;
        break;
    case RPS_MASK:
        s->rps_mask = val;
        break;
    }
    nas782x_rps_update(s);
}

static const MemoryRegionOps nas782x_rps_ops = {
    .read = nas782x_rps_read,
    .write = nas782x_rps_write,
    .endianness = DEVICE_NATIVE_ENDIAN,
};

static void nas782x_rps_init(Object *obj) 
{
    NAS782XRPSState *s = NAS782X_RPS(obj);

    /* initialize the bridge mmio */
    memory_region_init_io(
        &s->bridge_mmio, obj, &nas782x_rps_ops, s, TYPE_NAS782X_RPS, NAS782X_RPS_MMIO_SIZE);
    sysbus_init_mmio(SYS_BUS_DEVICE(s), &s->bridge_mmio);

    /* initialize the bridge irq */
    sysbus_init_irq(SYS_BUS_DEVICE(s), &s->irq);

    /* initialize GPIO in */
    qdev_init_gpio_in_named(DEVICE(s), nas782x_rps_set_irq, NAS782X_RPS_IRQ, 32);
}

static void nas782x_rps_realize(DeviceState *dev, Error **errp)
{
    NAS782XRPSState *s = NAS782X_RPS(dev);
}

static void nas782x_rps_reset(DeviceState *d)
{
    NAS782XRPSState *s = NAS782X_RPS(d);
    
    s->rps_status = 0;
    s->rps_ram_status = 0;
    s->rps_unmask = 0;
    s->rps_mask = 0;
}

static void nas782x_rps_class_init(ObjectClass *oc, void *data)
{
    DeviceClass *dc = DEVICE_CLASS(oc);

    /* dc->fw_name = ; */
    /* dc->desc = ; */
    /* dc->props = ; */
    /* dc->user_creatable = ; */
    /* dc->hotpluggable = ; */
    dc->reset = nas782x_rps_reset;
    dc->realize = nas782x_rps_realize;
    /* dc->unrealize = ; */
    /* dc->vmsd = ; */
    /* dc->bus_type = ; */

    /* SysBusDeviceClass sbc = SYS_BUS_DEVICE_CLASS(klass); */

    /* sbc->explicit_ofw_unit_address = ; */
    /* sbc->connect_irq_notifier = ; */
}

static const TypeInfo nas782x_rps_type_info = {
    .name = TYPE_NAS782X_RPS,
    .parent = TYPE_SYS_BUS_DEVICE,
    .instance_size = sizeof(NAS782XRPSState),
    .instance_init = nas782x_rps_init,
    /* .class_size = sizeof(SysBusDeviceClass), */
    .class_init = nas782x_rps_class_init,
};

static void nas782x_rps_register_types(void)
{
    type_register_static(&nas782x_rps_type_info);
}

type_init(nas782x_rps_register_types)
