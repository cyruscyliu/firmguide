/* 
 * automatically generated, don't change
 */

#include "qemu/osdep.h"
#include "qemu/log.h"
#include "qapi/error.h"
#include "target/arm/cpu.h"
#include "hw/arm/ox820.h"
#include "hw/char/serial.h"
#include "exec/address-spaces.h"

static void ox820_gpio_update(void *opaque);
static uint64_t ox820_gpio_read(void *opaque, hwaddr offset, unsigned size);
static void ox820_gpio_write(void *opaque, hwaddr offset, uint64_t val, unsigned size);
static void ox820_pcie_interface_update(void *opaque);
static uint64_t ox820_pcie_interface_read(void *opaque, hwaddr offset, unsigned size);
static void ox820_pcie_interface_write(void *opaque, hwaddr offset, uint64_t val, unsigned size);
static void ox820_sata_update(void *opaque);
static uint64_t ox820_sata_read(void *opaque, hwaddr offset, unsigned size);
static void ox820_sata_write(void *opaque, hwaddr offset, uint64_t val, unsigned size);
static void ox820_ehci_update(void *opaque);
static uint64_t ox820_ehci_read(void *opaque, hwaddr offset, unsigned size);
static void ox820_ehci_write(void *opaque, hwaddr offset, uint64_t val, unsigned size);
static void ox820_gmac_update(void *opaque);
static uint64_t ox820_gmac_read(void *opaque, hwaddr offset, unsigned size);
static void ox820_gmac_write(void *opaque, hwaddr offset, uint64_t val, unsigned size);

static void ox820_init(Object *obj);
static void ox820_realize(DeviceState *dev, Error **errp);
static void ox820_reset(void *opaque);

static void ox820_class_init(ObjectClass *oc, void *data);
static void ox820_register_types(void);

static void ox820_gpio_update(void *opaque) 
{
    /* OX820State *s = opaque; */
}

static uint64_t ox820_gpio_read(void *opaque, hwaddr offset, unsigned size) 
{
    OX820State *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case GPIO_RESERVED:
        res = s->gpio_reserved;
        break;
    }
    return res;
}

static void ox820_gpio_write(void *opaque, hwaddr offset, uint64_t val, unsigned size) 
{
    OX820State *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case GPIO_RESERVED:
        s->gpio_reserved = val;
        break;
    }
    ox820_gpio_update(s);
}

static const MemoryRegionOps ox820_gpio_ops = {
    .read = ox820_gpio_read,
    .write = ox820_gpio_write,
    .endianness = DEVICE_NATIVE_ENDIAN,
};

static void ox820_pcie_interface_update(void *opaque) 
{
    /* OX820State *s = opaque; */
}

static uint64_t ox820_pcie_interface_read(void *opaque, hwaddr offset, unsigned size) 
{
    OX820State *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case PCIE_RESERVED:
        res = s->pcie_reserved;
        break;
    }
    return res;
}

static void ox820_pcie_interface_write(void *opaque, hwaddr offset, uint64_t val, unsigned size) 
{
    OX820State *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case PCIE_RESERVED:
        s->pcie_reserved = val;
        break;
    }
    ox820_pcie_interface_update(s);
}

static const MemoryRegionOps ox820_pcie_interface_ops = {
    .read = ox820_pcie_interface_read,
    .write = ox820_pcie_interface_write,
    .endianness = DEVICE_NATIVE_ENDIAN,
};

static void ox820_sata_update(void *opaque) 
{
    /* OX820State *s = opaque; */
}

static uint64_t ox820_sata_read(void *opaque, hwaddr offset, unsigned size) 
{
    OX820State *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case SATA_RESERVED:
        res = s->sata_reserved;
        break;
    }
    return res;
}

static void ox820_sata_write(void *opaque, hwaddr offset, uint64_t val, unsigned size) 
{
    OX820State *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case SATA_RESERVED:
        s->sata_reserved = val;
        break;
    }
    ox820_sata_update(s);
}

static const MemoryRegionOps ox820_sata_ops = {
    .read = ox820_sata_read,
    .write = ox820_sata_write,
    .endianness = DEVICE_NATIVE_ENDIAN,
};

static void ox820_ehci_update(void *opaque) 
{
    /* OX820State *s = opaque; */
}

static uint64_t ox820_ehci_read(void *opaque, hwaddr offset, unsigned size) 
{
    OX820State *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case EHCI_RESERVED:
        res = s->ehci_reserved;
        break;
    }
    return res;
}

static void ox820_ehci_write(void *opaque, hwaddr offset, uint64_t val, unsigned size) 
{
    OX820State *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case EHCI_RESERVED:
        s->ehci_reserved = val;
        break;
    }
    ox820_ehci_update(s);
}

static const MemoryRegionOps ox820_ehci_ops = {
    .read = ox820_ehci_read,
    .write = ox820_ehci_write,
    .endianness = DEVICE_NATIVE_ENDIAN,
};

static void ox820_gmac_update(void *opaque) 
{
    /* OX820State *s = opaque; */
}

static uint64_t ox820_gmac_read(void *opaque, hwaddr offset, unsigned size) 
{
    OX820State *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case GMAC_RESERVED:
        res = s->gmac_reserved;
        break;
    }
    return res;
}

static void ox820_gmac_write(void *opaque, hwaddr offset, uint64_t val, unsigned size) 
{
    OX820State *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case GMAC_RESERVED:
        s->gmac_reserved = val;
        break;
    }
    ox820_gmac_update(s);
}

static const MemoryRegionOps ox820_gmac_ops = {
    .read = ox820_gmac_read,
    .write = ox820_gmac_write,
    .endianness = DEVICE_NATIVE_ENDIAN,
};

static void ox820_reset(void *opaque)
{
    OX820State *s = opaque;
    
    s->gpio_reserved = 0x0;
    s->pcie_reserved = 0x0;
    s->sata_reserved = 0x0;
    s->ehci_reserved = 0x0;
    s->gmac_reserved = 0x0;
}

static void ox820_init(Object *obj) 
{
    OX820State *s = OX820(obj);

    /* initialize cpus and add the cpu as soc's child */
    s->cpu_type = ARM_CPU_TYPE_NAME("arm11mpcore");
    s->cpu = ARM_CPU(object_new(s->cpu_type));

    /* initialize the cpus' private peripherals */
    sysbus_init_child_obj(obj, "cpu_pp", &s->cpu_pp, sizeof(s->cpu_pp), TYPE_ARM11MPCORE_PRIV);
    sysbus_init_mmio(SYS_BUS_DEVICE(s), sysbus_mmio_get_region(SYS_BUS_DEVICE(&s->cpu_pp), 0));

    /* initialize bamboo device registers */
    /* initialize ox820_gpio registers */
    memory_region_init_io(&s->ox820_gpio_mmio, obj,
        &ox820_gpio_ops, s, TYPE_OX820, OX820_GPIO_MMIO_SIZE);
    sysbus_init_mmio(SYS_BUS_DEVICE(s), &s->ox820_gpio_mmio);
    /* initialize ox820_pcie_interface registers */
    memory_region_init_io(&s->ox820_pcie_interface_mmio, obj,
        &ox820_pcie_interface_ops, s, TYPE_OX820, OX820_PCIE_INTERFACE_MMIO_SIZE);
    sysbus_init_mmio(SYS_BUS_DEVICE(s), &s->ox820_pcie_interface_mmio);
    /* initialize ox820_sata registers */
    memory_region_init_io(&s->ox820_sata_mmio, obj,
        &ox820_sata_ops, s, TYPE_OX820, OX820_SATA_MMIO_SIZE);
    sysbus_init_mmio(SYS_BUS_DEVICE(s), &s->ox820_sata_mmio);
    /* initialize ox820_ehci registers */
    memory_region_init_io(&s->ox820_ehci_mmio, obj,
        &ox820_ehci_ops, s, TYPE_OX820, OX820_EHCI_MMIO_SIZE);
    sysbus_init_mmio(SYS_BUS_DEVICE(s), &s->ox820_ehci_mmio);
    /* initialize ox820_gmac registers */
    memory_region_init_io(&s->ox820_gmac_mmio, obj,
        &ox820_gmac_ops, s, TYPE_OX820, OX820_GMAC_MMIO_SIZE);
    sysbus_init_mmio(SYS_BUS_DEVICE(s), &s->ox820_gmac_mmio);

    /* register reset for ox820 */
    // qemu_register_reset(ox820_reset, s);
}

static void ox820_realize(DeviceState *dev, Error **errp) 
{
    OX820State *s = OX820(dev);
    Error *err = NULL;

    /*realize the cpu private peripherals */
    object_realize_set_bool(OBJECT(&s->cpu_pp), true, "realize", &err);
    if (err != NULL) {
        error_propagate(errp, err);
        return;
    }
    sysbus_mmio_map(SYS_BUS_DEVICE(&s->cpu_pp), 0, 0x47000000);

    /* realize the cpu */
    object_property_set_bool(OBJECT(s->cpu), true, "realized", &err);
    if (err) {
        error_propagate(errp, err);
        return;
    }

    /* connect irq/fiq outputs from the gic to cpu */
    sysbus_connect_irq(SYS_BUS_DEVICE(&s->cpu_pp), 0,
        qdev_get_gpio_in(DEVICE(s->cpu), ARM_CPU_IRQ));
    sysbus_connect_irq(SYS_BUS_DEVICE(&s->cpu_pp), 1,
        qdev_get_gpio_in(DEVICE(s->cpu), ARM_CPU_FIQ));
    sysbus_connect_irq(SYS_BUS_DEVICE(&s->cpu_pp), 2,
        qdev_get_gpio_in(DEVICE(s->cpu), ARM_CPU_VIRQ));
    sysbus_connect_irq(SYS_BUS_DEVICE(&s->cpu_pp), 3,
        qdev_get_gpio_in(DEVICE(s->cpu), ARM_CPU_VFIQ));
}

static void ox820_class_init(ObjectClass *oc, void *data) 
{
    DeviceClass *dc = DEVICE_CLASS(oc);

    /* dc->fw_name = ; */
    /* dc->desc = ; */
    /* dc->props = ; */
    /* dc->user_creatable = ; */
    /* dc->hotpluggable = ; */
    /* dc->reset = ; */
    dc->realize = ox820_realize;
    /* dc->unrealize = ; */
    /* dc->vmsd = ; */
    /* dc->bus_type = ; */

    /* SysBusDeviceClass sbc = SYS_BUS_DEVICE_CLASS(klass); */

    /* sbc->explicit_ofw_unit_address = ; */
    /* sbc->connect_irq_notifier = ; */
}

static const TypeInfo ox820_type_info = {
    .name = TYPE_OX820,
    .parent = TYPE_SYS_BUS_DEVICE,
    .instance_size = sizeof(OX820State),
    .instance_init = ox820_init,
    /* .class_size = sizeof(SysBusDeviceClass), */
    .class_init = ox820_class_init,
};

static void ox820_register_types(void) 
{
    type_register_static(&ox820_type_info);
}

type_init(ox820_register_types);
