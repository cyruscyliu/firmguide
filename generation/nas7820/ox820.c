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

static void oxmas782x_gpio_update(void *opaque);
static uint64_t oxmas782x_gpio_read(void *opaque, hwaddr offset, unsigned size);
static void oxmas782x_gpio_write(void *opaque, hwaddr offset, uint64_t val, unsigned size);
static void nas782x_pcie_update(void *opaque);
static uint64_t nas782x_pcie_read(void *opaque, hwaddr offset, unsigned size);
static void nas782x_pcie_write(void *opaque, hwaddr offset, uint64_t val, unsigned size);
static void nas782x_sata_update(void *opaque);
static uint64_t nas782x_sata_read(void *opaque, hwaddr offset, unsigned size);
static void nas782x_sata_write(void *opaque, hwaddr offset, uint64_t val, unsigned size);
static void nas782x_gmac_update(void *opaque);
static uint64_t nas782x_gmac_read(void *opaque, hwaddr offset, unsigned size);
static void nas782x_gmac_write(void *opaque, hwaddr offset, uint64_t val, unsigned size);
static void nas782x_ehci_update(void *opaque);
static uint64_t nas782x_ehci_read(void *opaque, hwaddr offset, unsigned size);
static void nas782x_ehci_write(void *opaque, hwaddr offset, uint64_t val, unsigned size);
static void nas782x_pll_update(void *opaque);
static uint64_t nas782x_pll_read(void *opaque, hwaddr offset, unsigned size);
static void nas782x_pll_write(void *opaque, hwaddr offset, uint64_t val, unsigned size);
static void nas782x_reset_update(void *opaque);
static uint64_t nas782x_reset_read(void *opaque, hwaddr offset, unsigned size);
static void nas782x_reset_write(void *opaque, hwaddr offset, uint64_t val, unsigned size);
static void nas782x_rps_timer_update(void *opaque);
static uint64_t nas782x_rps_timer_read(void *opaque, hwaddr offset, unsigned size);
static void nas782x_rps_timer_write(void *opaque, hwaddr offset, uint64_t val, unsigned size);
static void nas782x_rps_update(void *opaque);
static uint64_t nas782x_rps_read(void *opaque, hwaddr offset, unsigned size);
static void nas782x_rps_write(void *opaque, hwaddr offset, uint64_t val, unsigned size);

static void ox820_init(Object *obj);
static void ox820_realize(DeviceState *dev, Error **errp);
static void ox820_reset(void *opaque);

static void ox820_class_init(ObjectClass *oc, void *data);
static void ox820_register_types(void);

static void oxmas782x_gpio_update(void *opaque) 
{
    /* OX820State *s = opaque; */
}

static uint64_t oxmas782x_gpio_read(void *opaque, hwaddr offset, unsigned size) 
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

static void oxmas782x_gpio_write(void *opaque, hwaddr offset, uint64_t val, unsigned size) 
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
    oxmas782x_gpio_update(s);
}

static const MemoryRegionOps oxmas782x_gpio_ops = {
    .read = oxmas782x_gpio_read,
    .write = oxmas782x_gpio_write,
    .endianness = DEVICE_NATIVE_ENDIAN,
};

static void nas782x_pcie_update(void *opaque) 
{
    /* OX820State *s = opaque; */
}

static uint64_t nas782x_pcie_read(void *opaque, hwaddr offset, unsigned size) 
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

static void nas782x_pcie_write(void *opaque, hwaddr offset, uint64_t val, unsigned size) 
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
    nas782x_pcie_update(s);
}

static const MemoryRegionOps nas782x_pcie_ops = {
    .read = nas782x_pcie_read,
    .write = nas782x_pcie_write,
    .endianness = DEVICE_NATIVE_ENDIAN,
};

static void nas782x_sata_update(void *opaque) 
{
    /* OX820State *s = opaque; */
}

static uint64_t nas782x_sata_read(void *opaque, hwaddr offset, unsigned size) 
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

static void nas782x_sata_write(void *opaque, hwaddr offset, uint64_t val, unsigned size) 
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
    nas782x_sata_update(s);
}

static const MemoryRegionOps nas782x_sata_ops = {
    .read = nas782x_sata_read,
    .write = nas782x_sata_write,
    .endianness = DEVICE_NATIVE_ENDIAN,
};

static void nas782x_gmac_update(void *opaque) 
{
    /* OX820State *s = opaque; */
}

static uint64_t nas782x_gmac_read(void *opaque, hwaddr offset, unsigned size) 
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

static void nas782x_gmac_write(void *opaque, hwaddr offset, uint64_t val, unsigned size) 
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
    nas782x_gmac_update(s);
}

static const MemoryRegionOps nas782x_gmac_ops = {
    .read = nas782x_gmac_read,
    .write = nas782x_gmac_write,
    .endianness = DEVICE_NATIVE_ENDIAN,
};

static void nas782x_ehci_update(void *opaque) 
{
    /* OX820State *s = opaque; */
}

static uint64_t nas782x_ehci_read(void *opaque, hwaddr offset, unsigned size) 
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

static void nas782x_ehci_write(void *opaque, hwaddr offset, uint64_t val, unsigned size) 
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
    nas782x_ehci_update(s);
}

static const MemoryRegionOps nas782x_ehci_ops = {
    .read = nas782x_ehci_read,
    .write = nas782x_ehci_write,
    .endianness = DEVICE_NATIVE_ENDIAN,
};

static void nas782x_pll_update(void *opaque) 
{
    /* OX820State *s = opaque; */
}

static uint64_t nas782x_pll_read(void *opaque, hwaddr offset, unsigned size) 
{
    OX820State *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case PLL_CTRL_0:
        res = s->pll_ctrl_0;
        break;
    case PLL_CTRL_1:
        res = s->pll_ctrl_1;
        break;
    case PLL_RESERVED:
        res = s->pll_reserved;
        break;
    }
    return res;
}

static void nas782x_pll_write(void *opaque, hwaddr offset, uint64_t val, unsigned size) 
{
    OX820State *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case PLL_CTRL_0:
        s->pll_ctrl_0 = val;
        break;
    case PLL_CTRL_1:
        s->pll_ctrl_1 = val;
        break;
    case PLL_RESERVED:
        s->pll_reserved = val;
        break;
    }
    nas782x_pll_update(s);
}

static const MemoryRegionOps nas782x_pll_ops = {
    .read = nas782x_pll_read,
    .write = nas782x_pll_write,
    .endianness = DEVICE_NATIVE_ENDIAN,
};

static void nas782x_reset_update(void *opaque) 
{
    /* OX820State *s = opaque; */
}

static uint64_t nas782x_reset_read(void *opaque, hwaddr offset, unsigned size) 
{
    OX820State *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case RESET_RESERVED:
        res = s->reset_reserved;
        break;
    }
    return res;
}

static void nas782x_reset_write(void *opaque, hwaddr offset, uint64_t val, unsigned size) 
{
    OX820State *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case RESET_RESERVED:
        s->reset_reserved = val;
        break;
    }
    nas782x_reset_update(s);
}

static const MemoryRegionOps nas782x_reset_ops = {
    .read = nas782x_reset_read,
    .write = nas782x_reset_write,
    .endianness = DEVICE_NATIVE_ENDIAN,
};

static void nas782x_rps_timer_update(void *opaque) 
{
    /* OX820State *s = opaque; */
}

static uint64_t nas782x_rps_timer_read(void *opaque, hwaddr offset, unsigned size) 
{
    OX820State *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case RPS_TIMER_RESERVED:
        res = s->rps_timer_reserved;
        break;
    }
    return res;
}

static void nas782x_rps_timer_write(void *opaque, hwaddr offset, uint64_t val, unsigned size) 
{
    OX820State *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case RPS_TIMER_RESERVED:
        s->rps_timer_reserved = val;
        break;
    }
    nas782x_rps_timer_update(s);
}

static const MemoryRegionOps nas782x_rps_timer_ops = {
    .read = nas782x_rps_timer_read,
    .write = nas782x_rps_timer_write,
    .endianness = DEVICE_NATIVE_ENDIAN,
};

static void nas782x_rps_update(void *opaque) 
{
    /* OX820State *s = opaque; */
}

static uint64_t nas782x_rps_read(void *opaque, hwaddr offset, unsigned size) 
{
    OX820State *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case RPS_RESERVED:
        res = s->rps_reserved;
        break;
    }
    return res;
}

static void nas782x_rps_write(void *opaque, hwaddr offset, uint64_t val, unsigned size) 
{
    OX820State *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case RPS_RESERVED:
        s->rps_reserved = val;
        break;
    }
    nas782x_rps_update(s);
}

static const MemoryRegionOps nas782x_rps_ops = {
    .read = nas782x_rps_read,
    .write = nas782x_rps_write,
    .endianness = DEVICE_NATIVE_ENDIAN,
};

static void ox820_reset(void *opaque)
{
    OX820State *s = opaque;
    
    s->gpio_reserved = 0x0;
    s->pcie_reserved = 0x0;
    s->sata_reserved = 0x0;
    s->gmac_reserved = 0x0;
    s->ehci_reserved = 0x0;
    s->pll_ctrl_0 = 3 << 8 | 3 << 4;
    s->pll_ctrl_1 = 32768;
    s->pll_reserved = 0x0;
    s->reset_reserved = 0x0;
    s->rps_timer_reserved = 0x0;
    s->rps_reserved = 0x0;
}

static void ox820_init(Object *obj) 
{
    OX820State *s = OX820(obj);

    /* initialize cpus and add the cpu as soc's child */
    s->cpu_type = ARM_CPU_TYPE_NAME("arm11mpcore");
    s->cpu = ARM_CPU(object_new(s->cpu_type));

    /* initialize the cpus' private peripherals */
    sysbus_init_child_obj(obj, "cpu_pp", &s->cpu_pp, sizeof(s->cpu_pp), TYPE_ARM11MPCORE_PRIV);

    /* initialize bamboo device registers */
    /* initialize oxmas782x_gpio registers */
    memory_region_init_io(&s->oxmas782x_gpio_mmio, obj,
        &oxmas782x_gpio_ops, s, TYPE_OX820, OXMAS782X_GPIO_MMIO_SIZE);
    sysbus_init_mmio(SYS_BUS_DEVICE(s), &s->oxmas782x_gpio_mmio);
    /* initialize nas782x_pcie registers */
    memory_region_init_io(&s->nas782x_pcie_mmio, obj,
        &nas782x_pcie_ops, s, TYPE_OX820, NAS782X_PCIE_MMIO_SIZE);
    sysbus_init_mmio(SYS_BUS_DEVICE(s), &s->nas782x_pcie_mmio);
    /* initialize nas782x_sata registers */
    memory_region_init_io(&s->nas782x_sata_mmio, obj,
        &nas782x_sata_ops, s, TYPE_OX820, NAS782X_SATA_MMIO_SIZE);
    sysbus_init_mmio(SYS_BUS_DEVICE(s), &s->nas782x_sata_mmio);
    /* initialize nas782x_gmac registers */
    memory_region_init_io(&s->nas782x_gmac_mmio, obj,
        &nas782x_gmac_ops, s, TYPE_OX820, NAS782X_GMAC_MMIO_SIZE);
    sysbus_init_mmio(SYS_BUS_DEVICE(s), &s->nas782x_gmac_mmio);
    /* initialize nas782x_ehci registers */
    memory_region_init_io(&s->nas782x_ehci_mmio, obj,
        &nas782x_ehci_ops, s, TYPE_OX820, NAS782X_EHCI_MMIO_SIZE);
    sysbus_init_mmio(SYS_BUS_DEVICE(s), &s->nas782x_ehci_mmio);
    /* initialize nas782x_pll registers */
    memory_region_init_io(&s->nas782x_pll_mmio, obj,
        &nas782x_pll_ops, s, TYPE_OX820, NAS782X_PLL_MMIO_SIZE);
    sysbus_init_mmio(SYS_BUS_DEVICE(s), &s->nas782x_pll_mmio);
    /* initialize nas782x_reset registers */
    memory_region_init_io(&s->nas782x_reset_mmio, obj,
        &nas782x_reset_ops, s, TYPE_OX820, NAS782X_RESET_MMIO_SIZE);
    sysbus_init_mmio(SYS_BUS_DEVICE(s), &s->nas782x_reset_mmio);
    /* initialize nas782x_rps_timer registers */
    memory_region_init_io(&s->nas782x_rps_timer_mmio, obj,
        &nas782x_rps_timer_ops, s, TYPE_OX820, NAS782X_RPS_TIMER_MMIO_SIZE);
    sysbus_init_mmio(SYS_BUS_DEVICE(s), &s->nas782x_rps_timer_mmio);
    /* initialize nas782x_rps registers */
    memory_region_init_io(&s->nas782x_rps_mmio, obj,
        &nas782x_rps_ops, s, TYPE_OX820, NAS782X_RPS_MMIO_SIZE);
    sysbus_init_mmio(SYS_BUS_DEVICE(s), &s->nas782x_rps_mmio);

    /* reset */
    ox820_reset(s);
}

static void ox820_realize(DeviceState *dev, Error **errp) 
{
    OX820State *s = OX820(dev);
    Error *err = NULL;

    /*realize the cpu private peripherals */
    object_property_set_bool(OBJECT(&s->cpu_pp), true, "realized", &err);
    if (err != NULL) {
        error_propagate(errp, err);
        return;
    }
    sysbus_mmio_map(SYS_BUS_DEVICE(&s->cpu_pp), 0, 0x47000000);
    if (serial_hd(0)) {
        serial_mm_init(get_system_memory(), 0x44200000, 0,
                       qdev_get_gpio_in(DEVICE(&s->cpu_pp), 23),
                       115200, serial_hd(0), DEVICE_LITTLE_ENDIAN);
    }

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
