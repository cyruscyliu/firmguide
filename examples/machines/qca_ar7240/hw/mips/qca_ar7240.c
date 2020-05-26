/*
 * automatically generated, don't change
 */

#include "qemu/osdep.h"
#include "qemu/log.h"
#include "hw/sysbus.h"
#include "hw/boards.h"
#include "qemu/units.h"
#include "hw/mips/mips.h"
#include "exec/address-spaces.h"
#include "target/mips/cpu.h"
#include "hw/mips/cpudevs.h"
#include "hw/intc/qca_ar7240_misc_intc.h"
#include "hw/char/serial.h"

#define TYPE_QCA_AR7240 "qca_ar7240"
#define QCA_AR7240(obj) \
    OBJECT_CHECK(QCA_AR7240State, (obj), TYPE_QCA_AR7240)

typedef struct QCA_AR7240State {
    MIPSCPU *cpu;
    QCA_AR7240_MISC_INTCState qca_ar7240_misc_intc0;
    MemoryRegion flash0;
    MemoryRegion ram0;
    MemoryRegion generic_ohci0_mmio;
    MemoryRegion qca_ar7100_spi0_mmio;
    MemoryRegion qca_ar7240_eth0_mmio;
    MemoryRegion qca_ar7240_eth1_mmio;
    MemoryRegion qcom_ar7240_pci0_mmio;
    MemoryRegion qcom_ar7240_pci1_mmio;
    MemoryRegion qcom_ar7240_pci2_mmio;
    MemoryRegion qca_ar7100_reset0_mmio;
    MemoryRegion qca_ar7130_wdt0_mmio;
    MemoryRegion qca_ar7240_pll0_mmio;
    MemoryRegion pinctrl_single0_mmio;
    MemoryRegion qca_ar7100_gpio0_mmio;
    MemoryRegion qca_ar7240_ddr_controller0_mmio;
    uint32_t generic_ohci0_reserved[0x1000 >> 2];
    uint32_t qca_ar7100_spi0_reserved[0x10 >> 2];
    uint32_t qca_ar7240_eth0_reserved[0x200 >> 2];
    uint32_t qca_ar7240_eth1_reserved[0x200 >> 2];
    uint32_t qcom_ar7240_pci0_reserved[0x1000 >> 2];
    uint32_t qcom_ar7240_pci1_reserved[0x100 >> 2];
    uint32_t qcom_ar7240_pci2_reserved[0x1000 >> 2];
    uint32_t qca_ar7100_reset0_reserved[0x98 >> 2];
    uint32_t qca_ar7130_wdt0_reserved[0x8 >> 2];
    uint32_t qca_ar7240_pll0_reserved[0x3c >> 2];
    uint32_t pinctrl_single0_reserved[0x8 >> 2];
    uint32_t qca_ar7100_gpio0_reserved[0x30 >> 2];
    uint32_t qca_ar7240_ddr_controller0_reserved[0x100 >> 2];
} QCA_AR7240State;

static void generic_ohci0_update(void *opaque)
{
    /* QCA_AR7240State *s = opaque; */
}

static uint64_t generic_ohci0_read(void *opaque, hwaddr offset, unsigned size)
{
    QCA_AR7240State *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case 0x0 ... 0xffc:
        res = s->generic_ohci0_reserved[offset >> 2];
        break;
    }
    return res;
}

static void generic_ohci0_write(void *opaque, hwaddr offset, uint64_t val, unsigned size)
{
    QCA_AR7240State *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case 0x0 ... 0xffc:
        s->generic_ohci0_reserved[offset >> 2] = val;
        break;
    }
    generic_ohci0_update(s);
}

static const MemoryRegionOps generic_ohci_ops0 = {
    .read = generic_ohci0_read,
    .write = generic_ohci0_write,
    .endianness = DEVICE_BIG_ENDIAN,
};

static void qca_ar7100_spi0_update(void *opaque)
{
    /* QCA_AR7240State *s = opaque; */
}

static uint64_t qca_ar7100_spi0_read(void *opaque, hwaddr offset, unsigned size)
{
    QCA_AR7240State *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case 0x0 ... 0xc:
        res = s->qca_ar7100_spi0_reserved[offset >> 2];
        break;
    }
    return res;
}

static void qca_ar7100_spi0_write(void *opaque, hwaddr offset, uint64_t val, unsigned size)
{
    QCA_AR7240State *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case 0x0 ... 0xc:
        s->qca_ar7100_spi0_reserved[offset >> 2] = val;
        break;
    }
    qca_ar7100_spi0_update(s);
}

static const MemoryRegionOps qca_ar7100_spi_ops0 = {
    .read = qca_ar7100_spi0_read,
    .write = qca_ar7100_spi0_write,
    .endianness = DEVICE_BIG_ENDIAN,
};

static void qca_ar7240_eth0_update(void *opaque)
{
    /* QCA_AR7240State *s = opaque; */
}

static uint64_t qca_ar7240_eth0_read(void *opaque, hwaddr offset, unsigned size)
{
    QCA_AR7240State *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case 0x0 ... 0x1fc:
        res = s->qca_ar7240_eth0_reserved[offset >> 2];
        break;
    }
    return res;
}

static void qca_ar7240_eth0_write(void *opaque, hwaddr offset, uint64_t val, unsigned size)
{
    QCA_AR7240State *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case 0x0 ... 0x1fc:
        s->qca_ar7240_eth0_reserved[offset >> 2] = val;
        break;
    }
    qca_ar7240_eth0_update(s);
}

static const MemoryRegionOps qca_ar7240_eth_ops0 = {
    .read = qca_ar7240_eth0_read,
    .write = qca_ar7240_eth0_write,
    .endianness = DEVICE_BIG_ENDIAN,
};
    static void qca_ar7240_eth1_update(void *opaque)
{
    /* QCA_AR7240State *s = opaque; */
}

static uint64_t qca_ar7240_eth1_read(void *opaque, hwaddr offset, unsigned size)
{
    QCA_AR7240State *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case 0x0 ... 0x1fc:
        res = s->qca_ar7240_eth1_reserved[offset >> 2];
        break;
    }
    return res;
}

static void qca_ar7240_eth1_write(void *opaque, hwaddr offset, uint64_t val, unsigned size)
{
    QCA_AR7240State *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case 0x0 ... 0x1fc:
        s->qca_ar7240_eth1_reserved[offset >> 2] = val;
        break;
    }
    qca_ar7240_eth1_update(s);
}

static const MemoryRegionOps qca_ar7240_eth_ops1 = {
    .read = qca_ar7240_eth1_read,
    .write = qca_ar7240_eth1_write,
    .endianness = DEVICE_BIG_ENDIAN,
};

static void qcom_ar7240_pci0_update(void *opaque)
{
    /* QCA_AR7240State *s = opaque; */
}

static uint64_t qcom_ar7240_pci0_read(void *opaque, hwaddr offset, unsigned size)
{
    QCA_AR7240State *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case 0x0 ... 0xffc:
        res = s->qcom_ar7240_pci0_reserved[offset >> 2];
        break;
    }
    return res;
}

static void qcom_ar7240_pci0_write(void *opaque, hwaddr offset, uint64_t val, unsigned size)
{
    QCA_AR7240State *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case 0x0 ... 0xffc:
        s->qcom_ar7240_pci0_reserved[offset >> 2] = val;
        break;
    }
    qcom_ar7240_pci0_update(s);
}

static const MemoryRegionOps qcom_ar7240_pci_ops0 = {
    .read = qcom_ar7240_pci0_read,
    .write = qcom_ar7240_pci0_write,
    .endianness = DEVICE_BIG_ENDIAN,
};
    static void qcom_ar7240_pci1_update(void *opaque)
{
    /* QCA_AR7240State *s = opaque; */
}

static uint64_t qcom_ar7240_pci1_read(void *opaque, hwaddr offset, unsigned size)
{
    QCA_AR7240State *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case 0x0 ... 0xfc:
        res = s->qcom_ar7240_pci1_reserved[offset >> 2];
        break;
    }
    return res;
}

static void qcom_ar7240_pci1_write(void *opaque, hwaddr offset, uint64_t val, unsigned size)
{
    QCA_AR7240State *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case 0x0 ... 0xfc:
        s->qcom_ar7240_pci1_reserved[offset >> 2] = val;
        break;
    }
    qcom_ar7240_pci1_update(s);
}

static const MemoryRegionOps qcom_ar7240_pci_ops1 = {
    .read = qcom_ar7240_pci1_read,
    .write = qcom_ar7240_pci1_write,
    .endianness = DEVICE_BIG_ENDIAN,
};
    static void qcom_ar7240_pci2_update(void *opaque)
{
    /* QCA_AR7240State *s = opaque; */
}

static uint64_t qcom_ar7240_pci2_read(void *opaque, hwaddr offset, unsigned size)
{
    QCA_AR7240State *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case 0x0 ... 0xffc:
        res = s->qcom_ar7240_pci2_reserved[offset >> 2];
        break;
    }
    return res;
}

static void qcom_ar7240_pci2_write(void *opaque, hwaddr offset, uint64_t val, unsigned size)
{
    QCA_AR7240State *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case 0x0 ... 0xffc:
        s->qcom_ar7240_pci2_reserved[offset >> 2] = val;
        break;
    }
    qcom_ar7240_pci2_update(s);
}

static const MemoryRegionOps qcom_ar7240_pci_ops2 = {
    .read = qcom_ar7240_pci2_read,
    .write = qcom_ar7240_pci2_write,
    .endianness = DEVICE_BIG_ENDIAN,
};

static void qca_ar7100_reset0_update(void *opaque)
{
    /* QCA_AR7240State *s = opaque; */
}

static uint64_t qca_ar7100_reset0_read(void *opaque, hwaddr offset, unsigned size)
{
    QCA_AR7240State *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case 0x0 ... 0x94:
        res = s->qca_ar7100_reset0_reserved[offset >> 2];
        break;
    }
    return res;
}

static void qca_ar7100_reset0_write(void *opaque, hwaddr offset, uint64_t val, unsigned size)
{
    QCA_AR7240State *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case 0x0 ... 0x94:
        s->qca_ar7100_reset0_reserved[offset >> 2] = val;
        break;
    }
    qca_ar7100_reset0_update(s);
}

static const MemoryRegionOps qca_ar7100_reset_ops0 = {
    .read = qca_ar7100_reset0_read,
    .write = qca_ar7100_reset0_write,
    .endianness = DEVICE_BIG_ENDIAN,
};

static void qca_ar7130_wdt0_update(void *opaque)
{
    /* QCA_AR7240State *s = opaque; */
}

static uint64_t qca_ar7130_wdt0_read(void *opaque, hwaddr offset, unsigned size)
{
    QCA_AR7240State *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case 0x0 ... 0x4:
        res = s->qca_ar7130_wdt0_reserved[offset >> 2];
        break;
    }
    return res;
}

static void qca_ar7130_wdt0_write(void *opaque, hwaddr offset, uint64_t val, unsigned size)
{
    QCA_AR7240State *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case 0x0 ... 0x4:
        s->qca_ar7130_wdt0_reserved[offset >> 2] = val;
        break;
    }
    qca_ar7130_wdt0_update(s);
}

static const MemoryRegionOps qca_ar7130_wdt_ops0 = {
    .read = qca_ar7130_wdt0_read,
    .write = qca_ar7130_wdt0_write,
    .endianness = DEVICE_BIG_ENDIAN,
};

static void qca_ar7240_pll0_update(void *opaque)
{
    /* QCA_AR7240State *s = opaque; */
}

static uint64_t qca_ar7240_pll0_read(void *opaque, hwaddr offset, unsigned size)
{
    QCA_AR7240State *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case 0x0 ... 0x38:
        res = s->qca_ar7240_pll0_reserved[offset >> 2];
        break;
    }
    return res;
}

static void qca_ar7240_pll0_write(void *opaque, hwaddr offset, uint64_t val, unsigned size)
{
    QCA_AR7240State *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case 0x0 ... 0x38:
        s->qca_ar7240_pll0_reserved[offset >> 2] = val;
        break;
    }
    qca_ar7240_pll0_update(s);
}

static const MemoryRegionOps qca_ar7240_pll_ops0 = {
    .read = qca_ar7240_pll0_read,
    .write = qca_ar7240_pll0_write,
    .endianness = DEVICE_BIG_ENDIAN,
};

static void pinctrl_single0_update(void *opaque)
{
    /* QCA_AR7240State *s = opaque; */
}

static uint64_t pinctrl_single0_read(void *opaque, hwaddr offset, unsigned size)
{
    QCA_AR7240State *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case 0x0 ... 0x4:
        res = s->pinctrl_single0_reserved[offset >> 2];
        break;
    }
    return res;
}

static void pinctrl_single0_write(void *opaque, hwaddr offset, uint64_t val, unsigned size)
{
    QCA_AR7240State *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case 0x0 ... 0x4:
        s->pinctrl_single0_reserved[offset >> 2] = val;
        break;
    }
    pinctrl_single0_update(s);
}

static const MemoryRegionOps pinctrl_single_ops0 = {
    .read = pinctrl_single0_read,
    .write = pinctrl_single0_write,
    .endianness = DEVICE_BIG_ENDIAN,
};

static void qca_ar7100_gpio0_update(void *opaque)
{
    /* QCA_AR7240State *s = opaque; */
}

static uint64_t qca_ar7100_gpio0_read(void *opaque, hwaddr offset, unsigned size)
{
    QCA_AR7240State *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case 0x0 ... 0x2c:
        res = s->qca_ar7100_gpio0_reserved[offset >> 2];
        break;
    }
    return res;
}

static void qca_ar7100_gpio0_write(void *opaque, hwaddr offset, uint64_t val, unsigned size)
{
    QCA_AR7240State *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case 0x0 ... 0x2c:
        s->qca_ar7100_gpio0_reserved[offset >> 2] = val;
        break;
    }
    qca_ar7100_gpio0_update(s);
}

static const MemoryRegionOps qca_ar7100_gpio_ops0 = {
    .read = qca_ar7100_gpio0_read,
    .write = qca_ar7100_gpio0_write,
    .endianness = DEVICE_BIG_ENDIAN,
};

static void qca_ar7240_ddr_controller0_update(void *opaque)
{
    /* QCA_AR7240State *s = opaque; */
}

static uint64_t qca_ar7240_ddr_controller0_read(void *opaque, hwaddr offset, unsigned size)
{
    QCA_AR7240State *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case 0x0 ... 0xfc:
        res = s->qca_ar7240_ddr_controller0_reserved[offset >> 2];
        break;
    }
    return res;
}

static void qca_ar7240_ddr_controller0_write(void *opaque, hwaddr offset, uint64_t val, unsigned size)
{
    QCA_AR7240State *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case 0x0 ... 0xfc:
        s->qca_ar7240_ddr_controller0_reserved[offset >> 2] = val;
        break;
    }
    qca_ar7240_ddr_controller0_update(s);
}

static const MemoryRegionOps qca_ar7240_ddr_controller_ops0 = {
    .read = qca_ar7240_ddr_controller0_read,
    .write = qca_ar7240_ddr_controller0_write,
    .endianness = DEVICE_BIG_ENDIAN,
};


static void qca_ar7240_reset(void *opaque)
{
    QCA_AR7240State *s = opaque;
    
    s->qca_ar7100_reset0_reserved[0x74 >> 2] = 0xb0;
    s->qca_ar7100_reset0_reserved[0x94 >> 2] = 0x10;
    s->qca_ar7240_pll0_reserved[0x0 >> 2] = 0x810;
}

static void qca_ar7240_init(MachineState *machine)
{
    QCA_AR7240State *s = g_new0(QCA_AR7240State, 1);
    Error *err = NULL;
    static struct mips_boot_info binfo;
    
    s->cpu = MIPS_CPU(object_new(machine->cpu_type));
    object_property_set_bool(OBJECT(s->cpu), true, "realized", &err);
    
    memory_region_allocate_system_memory(&s->ram0, OBJECT(machine), "ram0", 0x10000000);
    memory_region_add_subregion_overlap(get_system_memory(), 0x0, &s->ram0, 0);
    
    cpu_mips_irq_init_cpu(s->cpu);
    cpu_mips_clock_init(s->cpu);
    object_initialize(&s->qca_ar7240_misc_intc0, sizeof(s->qca_ar7240_misc_intc0), TYPE_QCA_AR7240_MISC_INTC);
    qdev_set_parent_bus(DEVICE(&s->qca_ar7240_misc_intc0), sysbus_get_default());
    object_property_set_bool(OBJECT(&s->qca_ar7240_misc_intc0), true, "realized", &err);
    sysbus_mmio_map(SYS_BUS_DEVICE(&s->qca_ar7240_misc_intc0), 0, 0x18060010);
    
    qdev_connect_gpio_out(DEVICE(&s->qca_ar7240_misc_intc0), 0, s->cpu->env.irq[6]);
    
    
    
    serial_mm_init(get_system_memory(), 0x18020000, 2, qdev_get_gpio_in(DEVICE(&s->qca_ar7240_misc_intc0), 3), 115200, serial_hd(0), DEVICE_BIG_ENDIAN);
    
    
    memory_region_init_rom(&s->flash0, NULL, "boot.flash.0", 0x400000, &err);
    memory_region_add_subregion_overlap(get_system_memory(), 0x1fc00000, &s->flash0, 0);
    
    memory_region_init_io(&s->generic_ohci0_mmio, NULL, &generic_ohci_ops0, s, TYPE_QCA_AR7240, 0x1000);
    memory_region_add_subregion_overlap(get_system_memory(), 0x1b000000, &s->generic_ohci0_mmio, 0);
    memory_region_init_io(&s->qca_ar7100_spi0_mmio, NULL, &qca_ar7100_spi_ops0, s, TYPE_QCA_AR7240, 0x10);
    memory_region_add_subregion_overlap(get_system_memory(), 0x1f000000, &s->qca_ar7100_spi0_mmio, 0);
    memory_region_init_io(&s->qca_ar7240_eth0_mmio, NULL, &qca_ar7240_eth_ops0, s, TYPE_QCA_AR7240, 0x200);
    memory_region_add_subregion_overlap(get_system_memory(), 0x19000000, &s->qca_ar7240_eth0_mmio, 0);
    memory_region_init_io(&s->qca_ar7240_eth1_mmio, NULL, &qca_ar7240_eth_ops1, s, TYPE_QCA_AR7240, 0x200);
    memory_region_add_subregion_overlap(get_system_memory(), 0x1a000000, &s->qca_ar7240_eth1_mmio, 0);
    memory_region_init_io(&s->qcom_ar7240_pci0_mmio, NULL, &qcom_ar7240_pci_ops0, s, TYPE_QCA_AR7240, 0x1000);
    memory_region_add_subregion_overlap(get_system_memory(), 0x180c0000, &s->qcom_ar7240_pci0_mmio, 0);
    memory_region_init_io(&s->qcom_ar7240_pci1_mmio, NULL, &qcom_ar7240_pci_ops1, s, TYPE_QCA_AR7240, 0x100);
    memory_region_add_subregion_overlap(get_system_memory(), 0x180f0000, &s->qcom_ar7240_pci1_mmio, 0);
    memory_region_init_io(&s->qcom_ar7240_pci2_mmio, NULL, &qcom_ar7240_pci_ops2, s, TYPE_QCA_AR7240, 0x1000);
    memory_region_add_subregion_overlap(get_system_memory(), 0x14000000, &s->qcom_ar7240_pci2_mmio, 0);
    memory_region_init_io(&s->qca_ar7100_reset0_mmio, NULL, &qca_ar7100_reset_ops0, s, TYPE_QCA_AR7240, 0x98);
    memory_region_add_subregion_overlap(get_system_memory(), 0x1806001c, &s->qca_ar7100_reset0_mmio, 0);
    memory_region_init_io(&s->qca_ar7130_wdt0_mmio, NULL, &qca_ar7130_wdt_ops0, s, TYPE_QCA_AR7240, 0x8);
    memory_region_add_subregion_overlap(get_system_memory(), 0x18060008, &s->qca_ar7130_wdt0_mmio, 0);
    memory_region_init_io(&s->qca_ar7240_pll0_mmio, NULL, &qca_ar7240_pll_ops0, s, TYPE_QCA_AR7240, 0x3c);
    memory_region_add_subregion_overlap(get_system_memory(), 0x18050000, &s->qca_ar7240_pll0_mmio, 0);
    memory_region_init_io(&s->pinctrl_single0_mmio, NULL, &pinctrl_single_ops0, s, TYPE_QCA_AR7240, 0x8);
    memory_region_add_subregion_overlap(get_system_memory(), 0x18040028, &s->pinctrl_single0_mmio, 0);
    memory_region_init_io(&s->qca_ar7100_gpio0_mmio, NULL, &qca_ar7100_gpio_ops0, s, TYPE_QCA_AR7240, 0x30);
    memory_region_add_subregion_overlap(get_system_memory(), 0x18040000, &s->qca_ar7100_gpio0_mmio, 0);
    memory_region_init_io(&s->qca_ar7240_ddr_controller0_mmio, NULL, &qca_ar7240_ddr_controller_ops0, s, TYPE_QCA_AR7240, 0x100);
    memory_region_add_subregion_overlap(get_system_memory(), 0x18000000, &s->qca_ar7240_ddr_controller0_mmio, 0);
    qca_ar7240_reset(s);

    binfo.board_id = 0xFFFFFFFF;
    binfo.ram_size = machine->ram_size;
    binfo.kernel_filename = machine->kernel_filename;
    binfo.kernel_cmdline = machine->kernel_cmdline;
    binfo.initrd_filename = machine->initrd_filename;
    mips_load_kernel(MIPS_CPU(first_cpu), &binfo);
}

static void qca_ar7240_machine_init(MachineClass *mc)
{
    mc->desc = "qca_ar7240";
    mc->init = qca_ar7240_init;
    mc->default_ram_size = 256 * MiB;
    mc->default_cpu_type = MIPS_CPU_TYPE_NAME("24Kc");
    mc->ignore_memory_transaction_failures = false;
}

DEFINE_MACHINE("qca_ar7240", qca_ar7240_machine_init)
