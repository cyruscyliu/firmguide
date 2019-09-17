/* 
 * automatically generated, don't change
 */

#include "qemu/osdep.h"
#include "qemu/log.h"
#include "qapi/error.h"
#include "hw/mips/bcma.h"

static void bcma_realize(DeviceState *dev, Error **errp);

static void bcma_init(Object *obj);
static void bcma_class_init(ObjectClass *oc, void *data);
static void bcma_register_types(void);

static void bcma_update(void *opaque)
{
    BCMAState *s = opaque;
}

static uint64_t bcma_read(void *opaque, hwaddr offset, unsigned size)
{
    BCMAState *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case BCMA_CC_ID_REGISTER:
        res = s->bcma_cc_id_register;
        break;
    case BCMA_CC_EROM_REGISTER:
        res = s->bcma_cc_erom_register;
        break;
    case BCMA_SCAN_STOP_FLAG:
        res = s->bcma_scan_stop_flag;
        break;
    }
    return res;
}

static void bcma_write(void *opaque, hwaddr offset, uint64_t val, unsigned size)
{
    BCMAState *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case BCMA_CC_ID_REGISTER:
        s->bcma_cc_id_register = val;
        break;
    case BCMA_CC_EROM_REGISTER:
        s->bcma_cc_erom_register = val;
        break;
    case BCMA_SCAN_STOP_FLAG:
        s->bcma_scan_stop_flag = val;
        break;
    }
    bcma_update(s);
}

static const MemoryRegionOps bcma_ops = {
    .read = bcma_read,
    .write = bcma_write,
    .endianness = DEVICE_NATIVE_ENDIAN,
};

static void bcma_init(Object *obj) 
{
    BCMAState *s = BCMA(obj);

    /* initialize the bridge mmio */
    memory_region_init_io(
        &s->bridge_mmio, obj, &bcma_ops, s, TYPE_BCMA, BCMA_MMIO_SIZE);
    sysbus_init_mmio(SYS_BUS_DEVICE(s), &s->bridge_mmio);
}

static void bcma_realize(DeviceState *dev, Error **errp)
{
    BCMAState *s = BCMA(dev);
    
    s->bcma_cc_id_register = 0x4716 | 0x10000 | 0x900000 | 0x0000000 | 0x00000000;
    s->bcma_cc_erom_register = 0x18001000;
    s->bcma_scan_stop_flag = 0xe | 0x1;
}

static void bcma_reset(DeviceState *d)
{
    BCMAState *s = BCMA(d);
    
    s->bcma_cc_id_register = 0x4716 | 0x10000 | 0x900000 | 0x0000000 | 0x00000000;
    s->bcma_cc_erom_register = 0x18001000;
    s->bcma_scan_stop_flag = 0xe | 0x1;
}

static void bcma_class_init(ObjectClass *oc, void *data)
{
    DeviceClass *dc = DEVICE_CLASS(oc);

    /* dc->fw_name = ; */
    /* dc->desc = ; */
    /* dc->props = ; */
    /* dc->user_creatable = ; */
    /* dc->hotpluggable = ; */
    dc->reset = bcma_reset;
    dc->realize = bcma_realize;
    /* dc->unrealize = ; */
    /* dc->vmsd = ; */
    /* dc->bus_type = ; */

    /* SysBusDeviceClass sbc = SYS_BUS_DEVICE_CLASS(klass); */

    /* sbc->explicit_ofw_unit_address = ; */
    /* sbc->connect_irq_notifier = ; */
}

static const TypeInfo bcma_type_info = {
    .name = TYPE_BCMA,
    .parent = TYPE_SYS_BUS_DEVICE,
    .instance_size = sizeof(BCMAState),
    .instance_init = bcma_init,
    /* .class_size = sizeof(SysBusDeviceClass), */
    .class_init = bcma_class_init,
};

static void bcma_register_types(void)
{
    type_register_static(&bcma_type_info);
}

type_init(bcma_register_types)
