{{license}}

#include "qemu/osdep.h"
#include "qemu/log.h"
#include "hw/pci-host/{{pice_name}}.h"

static void {{pice_name}}_update(void *opaque);
static void {{pice_name}}_reset(DeviceState *dev);

static uint64_t {{pice_name}}_read(void *opaque, hwaddr offset, unsigned size);
static void {{pice_name}}_write(void *opaque, hwaddr offset, uint64_t val, unsigned size);

static void {{pice_name}}_init(Object *obj);
static void {{pice_name}}_class_init(ObjectClass *klass, void *data);
static void {{pice_name}}_register_types(void);

static void {{pice_name}}_update(void *opaque) {
    /* {{pice_name|upper|concat}}State *s = opaque; */
}

static uint64_t {{pice_name}}_read(void *opaque, hwaddr offset, unsigned size) {
    {{pice_name|upper|concat}}State *s = ({{pice_name|upper|concat}}State *)opaque;

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

static void {{pice_name}}_write(void *opaque, hwaddr offset, uint64_t val, unsigned size) {
    {{pice_name|upper|concat}}State *s = opaque;

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
    {{pice_name}}_update(s);
    return;
}

static const MemoryRegionOps {{pice_name}}_ops = {
    .read = {{pice_name}}_read,
    .write = {{pice_name}}_write,
    .endianness = DEVICE_NATIVE_ENDIAN,
};

static void {{pice_name}}_init(Object *obj) {
    {{pice_name|upper|concat}}State *s = {{pice_name|upper}}(obj);

    /* initialize the mmio */
    memory_region_init_io(&s->mmio, obj, &{{pice_name}}_ops, s, "{{pice_name}}", {{pice_name|upper}}_RAM_SIZE);
    sysbus_init_mmio(SYS_BUS_DEVICE(s), &s->mmio);
}

static void {{pice_name}}_reset(DeviceState *dev) {
    {{pice_name|upper|concat}}State *s = {{pice_name|upper}}(dev);

    s->device_id = 0x5181;
    s->revision_id = 3;
}

static void {{pice_name}}_class_init(ObjectClass *klass, void *data) {
    DeviceClass *dc = DEVICE_CLASS(klass);

    /* dc->fw_name = ; */
    /* dc->desc = ; */
    /* dc->props = ; */
    /* dc->user_creatable = ; */
    /* dc->hotpluggable = ; */
    dc->reset = {{pice_name}}_reset;
    /* dc->realize = ; */
    /* dc->unrealize = ; */
    /* dc->vmsd = ; */
    /* dc->bus_type = ; */

    /* SysBusDeviceClass sbc = SYS_BUS_DEVICE_CLASS(klass); */

    /* sbc->explicit_ofw_unit_address = ; */
    /* sbc->connect_irq_notifier = ; */
}

static const TypeInfo {{pice_name}}_info = {
    .name = TYPE_{{pice_name|upper}},
    .parent = TYPE_SYS_BUS_DEVICE,
    .instance_size = sizeof({{pice_name|upper|concat}}State),
    .instance_init = {{pice_name}}_init,
    /* .class_zie = sizeof(SysBusDeviceClass), */
    .class_init = {{pice_name}}_class_init,
};

static void {{pice_name}}_register_types(void) {
    type_register_static(&{{pice_name}}_info);
}

type_init({{pice_name}}_register_types)