/* 
 * automatically generated, don't change
 */

#include "qemu/osdep.h"
#include "qemu/log.h"
#include "hw/pci-host/mv88f5181L_pcie.h"

static void mv88f5181L_pcie_update(void *opaque);
static void mv88f5181L_pcie_reset(DeviceState *dev);

static uint64_t mv88f5181L_pcie_read(void *opaque, hwaddr offset, unsigned size);
static void mv88f5181L_pcie_write(void *opaque, hwaddr offset, uint64_t val, unsigned size);

static void mv88f5181L_pcie_init(Object *obj);
static void mv88f5181L_pcie_class_init(ObjectClass *klass, void *data);
static void mv88f5181L_pcie_register_types(void);

static void mv88f5181L_pcie_update(void *opaque) {
    /* MV88F5181LPCIEState *s = opaque; */
}

static uint64_t mv88f5181L_pcie_read(void *opaque, hwaddr offset, unsigned size) {
    MV88F5181LPCIEState *s = (MV88F5181LPCIEState *)opaque;

    uint64_t res = 0;

    switch (offset) {
    case PCIE_DEVICE_AND_VENDOR_ID_REGISTER:
        res = s->device_id << 16;
        break;
    case PCIE_CLASS_CODE_AND_REVISION_ID_REGISTER:
        res = s->revision_id;
        break;
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset 0x%"HWADDR_PRIx"\n", __func__, offset);
        res = 0;
    }
    return res;
}

static void mv88f5181L_pcie_write(void *opaque, hwaddr offset, uint64_t val, unsigned size) {
    MV88F5181LPCIEState *s = opaque;

    switch (offset) {
    case PCIE_DEVICE_AND_VENDOR_ID_REGISTER:
        s->device_id = val;
        break;
    case PCIE_CLASS_CODE_AND_REVISION_ID_REGISTER:
        s->revision_id = val;
        break;
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset 0x%"HWADDR_PRIx"\n", __func__, offset);
    }
    mv88f5181L_pcie_update(s);
    return;
}

static const MemoryRegionOps mv88f5181L_pcie_ops = {
    .read = mv88f5181L_pcie_read,
    .write = mv88f5181L_pcie_write,
    .endianness = DEVICE_NATIVE_ENDIAN,
};

static void mv88f5181L_pcie_init(Object *obj) {
    MV88F5181LPCIEState *s = MV88F5181L_PCIE(obj);

    /* initialize the mmio */
    memory_region_init_io(&s->mmio, obj, &mv88f5181L_pcie_ops, s, "mv88f5181L_pcie", MV88F5181L_PCIE_RAM_SIZE);
    sysbus_init_mmio(SYS_BUS_DEVICE(s), &s->mmio);
}

static void mv88f5181L_pcie_reset(DeviceState *dev) {
    MV88F5181LPCIEState *s = MV88F5181L_PCIE(dev);

    s->device_id = 0x5181;
    s->revision_id = 3;
}

static void mv88f5181L_pcie_class_init(ObjectClass *klass, void *data) {
    DeviceClass *dc = DEVICE_CLASS(klass);

    /* dc->fw_name = ; */
    /* dc->desc = ; */
    /* dc->props = ; */
    /* dc->user_creatable = ; */
    /* dc->hotpluggable = ; */
    dc->reset = mv88f5181L_pcie_reset;
    /* dc->realize = ; */
    /* dc->unrealize = ; */
    /* dc->vmsd = ; */
    /* dc->bus_type = ; */

    /* SysBusDeviceClass sbc = SYS_BUS_DEVICE_CLASS(klass); */

    /* sbc->explicit_ofw_unit_address = ; */
    /* sbc->connect_irq_notifier = ; */
}

static const TypeInfo mv88f5181L_pcie_info = {
    .name = TYPE_MV88F5181L_PCIE,
    .parent = TYPE_SYS_BUS_DEVICE,
    .instance_size = sizeof(MV88F5181LPCIEState),
    .instance_init = mv88f5181L_pcie_init,
    /* .class_zie = sizeof(SysBusDeviceClass), */
    .class_init = mv88f5181L_pcie_class_init,
};

static void mv88f5181L_pcie_register_types(void) {
    type_register_static(&mv88f5181L_pcie_info);
}

type_init(mv88f5181L_pcie_register_types)