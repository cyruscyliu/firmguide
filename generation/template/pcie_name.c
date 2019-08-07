{{license}}

#include "qemu/osdep.h"
#include "qemu/log.h"
#include "hw/pci-host/{{pcie_name}}.h"

static void {{pcie_name}}_update(void *opaque);
static void {{pcie_name}}_reset(DeviceState *dev);

static uint64_t {{pcie_name}}_read(void *opaque, hwaddr offset, unsigned size);
static void {{pcie_name}}_write(void *opaque, hwaddr offset, uint64_t val, unsigned size);

static void {{pcie_name}}_init(Object *obj);
static void {{pcie_name}}_class_init(ObjectClass *klass, void *data);
static void {{pcie_name}}_register_types(void);

static void {{pcie_name}}_update(void *opaque) {
    /* {{pcie_name|upper|concat}}State *s = opaque; */
}

static uint64_t {{pcie_name}}_read(void *opaque, hwaddr offset, unsigned size) {
    {{pcie_name|upper|concat}}State *s = ({{pcie_name|upper|concat}}State *)opaque;

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

static void {{pcie_name}}_write(void *opaque, hwaddr offset, uint64_t val, unsigned size) {
    {{pcie_name|upper|concat}}State *s = opaque;

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
    {{pcie_name}}_update(s);
    return;
}

static const MemoryRegionOps {{pcie_name}}_ops = {
    .read = {{pcie_name}}_read,
    .write = {{pcie_name}}_write,
    .endianness = DEVICE_NATIVE_ENDIAN,
};

static void {{pcie_name}}_init(Object *obj) {
    {{pcie_name|upper|concat}}State *s = {{pcie_name|upper}}(obj);

    /* initialize the mmio */
    memory_region_init_io(&s->mmio, obj, &{{pcie_name}}_ops, s, "{{pcie_name}}", {{pcie_name|upper}}_RAM_SIZE);
    sysbus_init_mmio(SYS_BUS_DEVICE(s), &s->mmio);
}

static void {{pcie_name}}_reset(DeviceState *dev) {
    {{pcie_name|upper|concat}}State *s = {{pcie_name|upper}}(dev);

    s->device_id = 0x5181;
    s->revision_id = 3;
}

static void {{pcie_name}}_class_init(ObjectClass *klass, void *data) {
    DeviceClass *dc = DEVICE_CLASS(klass);

    /* dc->fw_name = ; */
    /* dc->desc = ; */
    /* dc->props = ; */
    /* dc->user_creatable = ; */
    /* dc->hotpluggable = ; */
    dc->reset = {{pcie_name}}_reset;
    /* dc->realize = ; */
    /* dc->unrealize = ; */
    /* dc->vmsd = ; */
    /* dc->bus_type = ; */

    /* SysBusDeviceClass sbc = SYS_BUS_DEVICE_CLASS(klass); */

    /* sbc->explicit_ofw_unit_address = ; */
    /* sbc->connect_irq_notifier = ; */
}

static const TypeInfo {{pcie_name}}_info = {
    .name = TYPE_{{pcie_name|upper}},
    .parent = TYPE_SYS_BUS_DEVICE,
    .instance_size = sizeof({{pcie_name|upper|concat}}State),
    .instance_init = {{pcie_name}}_init,
    /* .class_zie = sizeof(SysBusDeviceClass), */
    .class_init = {{pcie_name}}_class_init,
};

static void {{pcie_name}}_register_types(void) {
    type_register_static(&{{pcie_name}}_info);
}

type_init({{pcie_name}}_register_types)