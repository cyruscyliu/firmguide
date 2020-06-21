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
#include "hw/intc/ralink_rt2880_intc.h"
#include "hw/timer/ralink_rt2880_timer.h"
#include "hw/char/serial.h"
#include "hw/char/serial.h"

#define TYPE_RALINK_RT3883_SOC "ralink_rt3883_soc"
#define RALINK_RT3883_SOC(obj) \
    OBJECT_CHECK(RALINK_RT3883_SOCState, (obj), TYPE_RALINK_RT3883_SOC)

typedef struct RALINK_RT3883_SOCState {
    MIPSCPU *cpu;
    RALINK_RT2880_INTCState ralink_rt2880_intc0;
    RALINK_RT2880_TIMERState timer0;
    MemoryRegion flash0;
    MemoryRegion ram0;
    MemoryRegion ohci_platform0_mmio;
    MemoryRegion ehci_platform0_mmio;
    MemoryRegion ralink_rt2880_wmac0_mmio;
    MemoryRegion ralink_rt3883_pci0_mmio;
    MemoryRegion ralink_rt3883_eth0_mmio;
    MemoryRegion ralink_rt2880_spi0_mmio;
    MemoryRegion ralink_rt2880_gpio0_mmio;
    MemoryRegion ralink_rt2880_gpio1_mmio;
    MemoryRegion ralink_rt2880_gpio2_mmio;
    MemoryRegion ralink_rt2880_gpio3_mmio;
    MemoryRegion ralink_rt3050_memc0_mmio;
    MemoryRegion ralink_rt2880_wdt0_mmio;
    MemoryRegion ralink_rt3050_sysc0_mmio;
    uint32_t ohci_platform0_reserved[0x1000 >> 2];
    uint32_t ehci_platform0_reserved[0x1000 >> 2];
    uint32_t ralink_rt2880_wmac0_reserved[0x9c40 >> 2];
    uint32_t ralink_rt3883_pci0_reserved[0x20000 >> 2];
    uint32_t ralink_rt3883_eth0_reserved[0x2710 >> 2];
    uint32_t ralink_rt2880_spi0_reserved[0x100 >> 2];
    uint32_t ralink_rt2880_gpio0_reserved[0x34 >> 2];
    uint32_t ralink_rt2880_gpio1_reserved[0x24 >> 2];
    uint32_t ralink_rt2880_gpio2_reserved[0x24 >> 2];
    uint32_t ralink_rt2880_gpio3_reserved[0x24 >> 2];
    uint32_t ralink_rt3050_memc0_reserved[0x100 >> 2];
    uint32_t ralink_rt2880_wdt0_reserved[0x10 >> 2];
    uint32_t ralink_rt3050_sysc0_reserved[0x100 >> 2];
} RALINK_RT3883_SOCState;

static void ohci_platform0_update(void *opaque)
{
    /* RALINK_RT3883_SOCState *s = opaque; */
}

static uint64_t ohci_platform0_read(void *opaque, hwaddr offset, unsigned size)
{
    RALINK_RT3883_SOCState *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case 0x0 ... 0xffc:
        res = s->ohci_platform0_reserved[offset >> 2];
        break;
    }
    return res;
}

static void ohci_platform0_write(void *opaque, hwaddr offset, uint64_t val, unsigned size)
{
    RALINK_RT3883_SOCState *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case 0x0 ... 0xffc:
        s->ohci_platform0_reserved[offset >> 2] = val;
        break;
    }
    ohci_platform0_update(s);
}

static const MemoryRegionOps ohci_platform_ops0 = {
    .read = ohci_platform0_read,
    .write = ohci_platform0_write,
    .endianness = DEVICE_LITTLE_ENDIAN,
};

static void ehci_platform0_update(void *opaque)
{
    /* RALINK_RT3883_SOCState *s = opaque; */
}

static uint64_t ehci_platform0_read(void *opaque, hwaddr offset, unsigned size)
{
    RALINK_RT3883_SOCState *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case 0x0 ... 0xffc:
        res = s->ehci_platform0_reserved[offset >> 2];
        break;
    }
    return res;
}

static void ehci_platform0_write(void *opaque, hwaddr offset, uint64_t val, unsigned size)
{
    RALINK_RT3883_SOCState *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case 0x0 ... 0xffc:
        s->ehci_platform0_reserved[offset >> 2] = val;
        break;
    }
    ehci_platform0_update(s);
}

static const MemoryRegionOps ehci_platform_ops0 = {
    .read = ehci_platform0_read,
    .write = ehci_platform0_write,
    .endianness = DEVICE_LITTLE_ENDIAN,
};

static void ralink_rt2880_wmac0_update(void *opaque)
{
    /* RALINK_RT3883_SOCState *s = opaque; */
}

static uint64_t ralink_rt2880_wmac0_read(void *opaque, hwaddr offset, unsigned size)
{
    RALINK_RT3883_SOCState *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case 0x0 ... 0x9c3c:
        res = s->ralink_rt2880_wmac0_reserved[offset >> 2];
        break;
    }
    return res;
}

static void ralink_rt2880_wmac0_write(void *opaque, hwaddr offset, uint64_t val, unsigned size)
{
    RALINK_RT3883_SOCState *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case 0x0 ... 0x9c3c:
        s->ralink_rt2880_wmac0_reserved[offset >> 2] = val;
        break;
    }
    ralink_rt2880_wmac0_update(s);
}

static const MemoryRegionOps ralink_rt2880_wmac_ops0 = {
    .read = ralink_rt2880_wmac0_read,
    .write = ralink_rt2880_wmac0_write,
    .endianness = DEVICE_LITTLE_ENDIAN,
};

static void ralink_rt3883_pci0_update(void *opaque)
{
    /* RALINK_RT3883_SOCState *s = opaque; */
}

static uint64_t ralink_rt3883_pci0_read(void *opaque, hwaddr offset, unsigned size)
{
    RALINK_RT3883_SOCState *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case 0x0 ... 0x1fffc:
        res = s->ralink_rt3883_pci0_reserved[offset >> 2];
        break;
    }
    return res;
}

static void ralink_rt3883_pci0_write(void *opaque, hwaddr offset, uint64_t val, unsigned size)
{
    RALINK_RT3883_SOCState *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case 0x0 ... 0x1fffc:
        s->ralink_rt3883_pci0_reserved[offset >> 2] = val;
        break;
    }
    ralink_rt3883_pci0_update(s);
}

static const MemoryRegionOps ralink_rt3883_pci_ops0 = {
    .read = ralink_rt3883_pci0_read,
    .write = ralink_rt3883_pci0_write,
    .endianness = DEVICE_LITTLE_ENDIAN,
};

static void ralink_rt3883_eth0_update(void *opaque)
{
    /* RALINK_RT3883_SOCState *s = opaque; */
}

static uint64_t ralink_rt3883_eth0_read(void *opaque, hwaddr offset, unsigned size)
{
    RALINK_RT3883_SOCState *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case 0x0 ... 0x270c:
        res = s->ralink_rt3883_eth0_reserved[offset >> 2];
        break;
    }
    return res;
}

static void ralink_rt3883_eth0_write(void *opaque, hwaddr offset, uint64_t val, unsigned size)
{
    RALINK_RT3883_SOCState *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case 0x0 ... 0x270c:
        s->ralink_rt3883_eth0_reserved[offset >> 2] = val;
        break;
    }
    ralink_rt3883_eth0_update(s);
}

static const MemoryRegionOps ralink_rt3883_eth_ops0 = {
    .read = ralink_rt3883_eth0_read,
    .write = ralink_rt3883_eth0_write,
    .endianness = DEVICE_LITTLE_ENDIAN,
};

static void ralink_rt2880_spi0_update(void *opaque)
{
    /* RALINK_RT3883_SOCState *s = opaque; */
}

static uint64_t ralink_rt2880_spi0_read(void *opaque, hwaddr offset, unsigned size)
{
    RALINK_RT3883_SOCState *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case 0x0 ... 0xfc:
        res = s->ralink_rt2880_spi0_reserved[offset >> 2];
        break;
    }
    return res;
}

static void ralink_rt2880_spi0_write(void *opaque, hwaddr offset, uint64_t val, unsigned size)
{
    RALINK_RT3883_SOCState *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case 0x0 ... 0xfc:
        s->ralink_rt2880_spi0_reserved[offset >> 2] = val;
        break;
    }
    ralink_rt2880_spi0_update(s);
}

static const MemoryRegionOps ralink_rt2880_spi_ops0 = {
    .read = ralink_rt2880_spi0_read,
    .write = ralink_rt2880_spi0_write,
    .endianness = DEVICE_LITTLE_ENDIAN,
};

static void ralink_rt2880_gpio0_update(void *opaque)
{
    /* RALINK_RT3883_SOCState *s = opaque; */
}

static uint64_t ralink_rt2880_gpio0_read(void *opaque, hwaddr offset, unsigned size)
{
    RALINK_RT3883_SOCState *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case 0x0 ... 0x30:
        res = s->ralink_rt2880_gpio0_reserved[offset >> 2];
        break;
    }
    return res;
}

static void ralink_rt2880_gpio0_write(void *opaque, hwaddr offset, uint64_t val, unsigned size)
{
    RALINK_RT3883_SOCState *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case 0x0 ... 0x30:
        s->ralink_rt2880_gpio0_reserved[offset >> 2] = val;
        break;
    }
    ralink_rt2880_gpio0_update(s);
}

static const MemoryRegionOps ralink_rt2880_gpio_ops0 = {
    .read = ralink_rt2880_gpio0_read,
    .write = ralink_rt2880_gpio0_write,
    .endianness = DEVICE_LITTLE_ENDIAN,
};
    static void ralink_rt2880_gpio1_update(void *opaque)
{
    /* RALINK_RT3883_SOCState *s = opaque; */
}

static uint64_t ralink_rt2880_gpio1_read(void *opaque, hwaddr offset, unsigned size)
{
    RALINK_RT3883_SOCState *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case 0x0 ... 0x20:
        res = s->ralink_rt2880_gpio1_reserved[offset >> 2];
        break;
    }
    return res;
}

static void ralink_rt2880_gpio1_write(void *opaque, hwaddr offset, uint64_t val, unsigned size)
{
    RALINK_RT3883_SOCState *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case 0x0 ... 0x20:
        s->ralink_rt2880_gpio1_reserved[offset >> 2] = val;
        break;
    }
    ralink_rt2880_gpio1_update(s);
}

static const MemoryRegionOps ralink_rt2880_gpio_ops1 = {
    .read = ralink_rt2880_gpio1_read,
    .write = ralink_rt2880_gpio1_write,
    .endianness = DEVICE_LITTLE_ENDIAN,
};
    static void ralink_rt2880_gpio2_update(void *opaque)
{
    /* RALINK_RT3883_SOCState *s = opaque; */
}

static uint64_t ralink_rt2880_gpio2_read(void *opaque, hwaddr offset, unsigned size)
{
    RALINK_RT3883_SOCState *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case 0x0 ... 0x20:
        res = s->ralink_rt2880_gpio2_reserved[offset >> 2];
        break;
    }
    return res;
}

static void ralink_rt2880_gpio2_write(void *opaque, hwaddr offset, uint64_t val, unsigned size)
{
    RALINK_RT3883_SOCState *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case 0x0 ... 0x20:
        s->ralink_rt2880_gpio2_reserved[offset >> 2] = val;
        break;
    }
    ralink_rt2880_gpio2_update(s);
}

static const MemoryRegionOps ralink_rt2880_gpio_ops2 = {
    .read = ralink_rt2880_gpio2_read,
    .write = ralink_rt2880_gpio2_write,
    .endianness = DEVICE_LITTLE_ENDIAN,
};
    static void ralink_rt2880_gpio3_update(void *opaque)
{
    /* RALINK_RT3883_SOCState *s = opaque; */
}

static uint64_t ralink_rt2880_gpio3_read(void *opaque, hwaddr offset, unsigned size)
{
    RALINK_RT3883_SOCState *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case 0x0 ... 0x20:
        res = s->ralink_rt2880_gpio3_reserved[offset >> 2];
        break;
    }
    return res;
}

static void ralink_rt2880_gpio3_write(void *opaque, hwaddr offset, uint64_t val, unsigned size)
{
    RALINK_RT3883_SOCState *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case 0x0 ... 0x20:
        s->ralink_rt2880_gpio3_reserved[offset >> 2] = val;
        break;
    }
    ralink_rt2880_gpio3_update(s);
}

static const MemoryRegionOps ralink_rt2880_gpio_ops3 = {
    .read = ralink_rt2880_gpio3_read,
    .write = ralink_rt2880_gpio3_write,
    .endianness = DEVICE_LITTLE_ENDIAN,
};

static void ralink_rt3050_memc0_update(void *opaque)
{
    /* RALINK_RT3883_SOCState *s = opaque; */
}

static uint64_t ralink_rt3050_memc0_read(void *opaque, hwaddr offset, unsigned size)
{
    RALINK_RT3883_SOCState *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case 0x0 ... 0xfc:
        res = s->ralink_rt3050_memc0_reserved[offset >> 2];
        break;
    }
    return res;
}

static void ralink_rt3050_memc0_write(void *opaque, hwaddr offset, uint64_t val, unsigned size)
{
    RALINK_RT3883_SOCState *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case 0x0 ... 0xfc:
        s->ralink_rt3050_memc0_reserved[offset >> 2] = val;
        break;
    }
    ralink_rt3050_memc0_update(s);
}

static const MemoryRegionOps ralink_rt3050_memc_ops0 = {
    .read = ralink_rt3050_memc0_read,
    .write = ralink_rt3050_memc0_write,
    .endianness = DEVICE_LITTLE_ENDIAN,
};

static void ralink_rt2880_wdt0_update(void *opaque)
{
    /* RALINK_RT3883_SOCState *s = opaque; */
}

static uint64_t ralink_rt2880_wdt0_read(void *opaque, hwaddr offset, unsigned size)
{
    RALINK_RT3883_SOCState *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case 0x0 ... 0xc:
        res = s->ralink_rt2880_wdt0_reserved[offset >> 2];
        break;
    }
    return res;
}

static void ralink_rt2880_wdt0_write(void *opaque, hwaddr offset, uint64_t val, unsigned size)
{
    RALINK_RT3883_SOCState *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case 0x0 ... 0xc:
        s->ralink_rt2880_wdt0_reserved[offset >> 2] = val;
        break;
    }
    ralink_rt2880_wdt0_update(s);
}

static const MemoryRegionOps ralink_rt2880_wdt_ops0 = {
    .read = ralink_rt2880_wdt0_read,
    .write = ralink_rt2880_wdt0_write,
    .endianness = DEVICE_LITTLE_ENDIAN,
};

static void ralink_rt3050_sysc0_update(void *opaque)
{
    /* RALINK_RT3883_SOCState *s = opaque; */
}

static uint64_t ralink_rt3050_sysc0_read(void *opaque, hwaddr offset, unsigned size)
{
    RALINK_RT3883_SOCState *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case 0x0 ... 0xfc:
        res = s->ralink_rt3050_sysc0_reserved[offset >> 2];
        break;
    }
    return res;
}

static void ralink_rt3050_sysc0_write(void *opaque, hwaddr offset, uint64_t val, unsigned size)
{
    RALINK_RT3883_SOCState *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case 0x0 ... 0xfc:
        s->ralink_rt3050_sysc0_reserved[offset >> 2] = val;
        break;
    }
    ralink_rt3050_sysc0_update(s);
}

static const MemoryRegionOps ralink_rt3050_sysc_ops0 = {
    .read = ralink_rt3050_sysc0_read,
    .write = ralink_rt3050_sysc0_write,
    .endianness = DEVICE_LITTLE_ENDIAN,
};


static void ralink_rt3883_soc_reset(void *opaque)
{
    RALINK_RT3883_SOCState *s = opaque;
    
    s->ralink_rt3050_sysc0_reserved[0x0 >> 2] = 0x38335452;
    s->ralink_rt3050_sysc0_reserved[0x4 >> 2] = 0x20203338;
}

static void ralink_rt3883_soc_init(MachineState *machine)
{
    RALINK_RT3883_SOCState *s = g_new0(RALINK_RT3883_SOCState, 1);
    Error *err = NULL;
    static struct mips_boot_info binfo;
    
    s->cpu = MIPS_CPU(object_new(machine->cpu_type));
    object_property_set_bool(OBJECT(s->cpu), true, "realized", &err);
    
    memory_region_allocate_system_memory(&s->ram0, OBJECT(machine), "ram0", 0x10000000);
    memory_region_add_subregion_overlap(get_system_memory(), 0x0, &s->ram0, 0);
    
    cpu_mips_irq_init_cpu(s->cpu);
    cpu_mips_clock_init(s->cpu);
    object_initialize(&s->ralink_rt2880_intc0, sizeof(s->ralink_rt2880_intc0), TYPE_RALINK_RT2880_INTC);
    qdev_set_parent_bus(DEVICE(&s->ralink_rt2880_intc0), sysbus_get_default());
    object_property_set_bool(OBJECT(&s->ralink_rt2880_intc0), true, "realized", &err);
    sysbus_mmio_map(SYS_BUS_DEVICE(&s->ralink_rt2880_intc0), 0, 0x10000200);
    
    qdev_connect_gpio_out(DEVICE(&s->ralink_rt2880_intc0), 0, s->cpu->env.irq[2]);
    
    object_initialize(&s->timer0, sizeof(s->timer0), TYPE_RALINK_RT2880_TIMER);
    qdev_set_parent_bus(DEVICE(&s->timer0), sysbus_get_default());
    object_property_set_bool(OBJECT(&s->timer0), true, "realized", &err);
    sysbus_mmio_map(SYS_BUS_DEVICE(&s->timer0), 0, 0x10000100);
    
    
    serial_mm_init_au(get_system_memory(), 0x10000c00, 2, qdev_get_gpio_in(DEVICE(&s->ralink_rt2880_intc0), 12), 115200, serial_hd(0), DEVICE_LITTLE_ENDIAN);
    serial_mm_init_au(get_system_memory(), 0x10000500, 2, qdev_get_gpio_in(DEVICE(&s->ralink_rt2880_intc0), 5), 115200, serial_hd(1), DEVICE_LITTLE_ENDIAN);
    
    
    memory_region_init_rom(&s->flash0, NULL, "boot.flash.0", 0x4000000, &err);
    memory_region_add_subregion_overlap(get_system_memory(), 0x1c000000, &s->flash0, 0);
    
    memory_region_init_io(&s->ohci_platform0_mmio, NULL, &ohci_platform_ops0, s, TYPE_RALINK_RT3883_SOC, 0x1000);
    memory_region_add_subregion_overlap(get_system_memory(), 0x101c1000, &s->ohci_platform0_mmio, 0);
    memory_region_init_io(&s->ehci_platform0_mmio, NULL, &ehci_platform_ops0, s, TYPE_RALINK_RT3883_SOC, 0x1000);
    memory_region_add_subregion_overlap(get_system_memory(), 0x101c0000, &s->ehci_platform0_mmio, 0);
    memory_region_init_io(&s->ralink_rt2880_wmac0_mmio, NULL, &ralink_rt2880_wmac_ops0, s, TYPE_RALINK_RT3883_SOC, 0x9c40);
    memory_region_add_subregion_overlap(get_system_memory(), 0x10180000, &s->ralink_rt2880_wmac0_mmio, 0);
    memory_region_init_io(&s->ralink_rt3883_pci0_mmio, NULL, &ralink_rt3883_pci_ops0, s, TYPE_RALINK_RT3883_SOC, 0x20000);
    memory_region_add_subregion_overlap(get_system_memory(), 0x10140000, &s->ralink_rt3883_pci0_mmio, 0);
    memory_region_init_io(&s->ralink_rt3883_eth0_mmio, NULL, &ralink_rt3883_eth_ops0, s, TYPE_RALINK_RT3883_SOC, 0x2710);
    memory_region_add_subregion_overlap(get_system_memory(), 0x10100000, &s->ralink_rt3883_eth0_mmio, 0);
    memory_region_init_io(&s->ralink_rt2880_spi0_mmio, NULL, &ralink_rt2880_spi_ops0, s, TYPE_RALINK_RT3883_SOC, 0x100);
    memory_region_add_subregion_overlap(get_system_memory(), 0x10000b00, &s->ralink_rt2880_spi0_mmio, 0);
    memory_region_init_io(&s->ralink_rt2880_gpio0_mmio, NULL, &ralink_rt2880_gpio_ops0, s, TYPE_RALINK_RT3883_SOC, 0x34);
    memory_region_add_subregion_overlap(get_system_memory(), 0x10000600, &s->ralink_rt2880_gpio0_mmio, 0);
    memory_region_init_io(&s->ralink_rt2880_gpio1_mmio, NULL, &ralink_rt2880_gpio_ops1, s, TYPE_RALINK_RT3883_SOC, 0x24);
    memory_region_add_subregion_overlap(get_system_memory(), 0x10000638, &s->ralink_rt2880_gpio1_mmio, 0);
    memory_region_init_io(&s->ralink_rt2880_gpio2_mmio, NULL, &ralink_rt2880_gpio_ops2, s, TYPE_RALINK_RT3883_SOC, 0x24);
    memory_region_add_subregion_overlap(get_system_memory(), 0x10000660, &s->ralink_rt2880_gpio2_mmio, 0);
    memory_region_init_io(&s->ralink_rt2880_gpio3_mmio, NULL, &ralink_rt2880_gpio_ops3, s, TYPE_RALINK_RT3883_SOC, 0x24);
    memory_region_add_subregion_overlap(get_system_memory(), 0x10000688, &s->ralink_rt2880_gpio3_mmio, 0);
    memory_region_init_io(&s->ralink_rt3050_memc0_mmio, NULL, &ralink_rt3050_memc_ops0, s, TYPE_RALINK_RT3883_SOC, 0x100);
    memory_region_add_subregion_overlap(get_system_memory(), 0x10000300, &s->ralink_rt3050_memc0_mmio, 0);
    memory_region_init_io(&s->ralink_rt2880_wdt0_mmio, NULL, &ralink_rt2880_wdt_ops0, s, TYPE_RALINK_RT3883_SOC, 0x10);
    memory_region_add_subregion_overlap(get_system_memory(), 0x10000120, &s->ralink_rt2880_wdt0_mmio, 0);
    memory_region_init_io(&s->ralink_rt3050_sysc0_mmio, NULL, &ralink_rt3050_sysc_ops0, s, TYPE_RALINK_RT3883_SOC, 0x100);
    memory_region_add_subregion_overlap(get_system_memory(), 0x10000000, &s->ralink_rt3050_sysc0_mmio, 0);
    ralink_rt3883_soc_reset(s);

    binfo.board_id = 0xFFFFFFFF;
    binfo.ram_size = machine->ram_size;
    binfo.kernel_filename = machine->kernel_filename;
    binfo.kernel_cmdline = machine->kernel_cmdline;
    binfo.initrd_filename = machine->initrd_filename;
    mips_load_kernel(MIPS_CPU(first_cpu), &binfo);
}

static void ralink_rt3883_soc_machine_init(MachineClass *mc)
{
    mc->desc = "ralink_rt3883_soc";
    mc->init = ralink_rt3883_soc_init;
    mc->default_ram_size = 256 * MiB;
    mc->default_cpu_type = MIPS_CPU_TYPE_NAME("74Kf");
    mc->ignore_memory_transaction_failures = false;
}

DEFINE_MACHINE("ralink_rt3883_soc", ralink_rt3883_soc_machine_init)
