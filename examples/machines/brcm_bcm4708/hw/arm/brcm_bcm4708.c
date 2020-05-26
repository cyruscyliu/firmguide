/*
 * automatically generated, don't change
 */

#include "qemu/osdep.h"
#include "qemu/log.h"
#include "hw/sysbus.h"
#include "hw/boards.h"
#include "qemu/units.h"
#include "hw/arm/arm.h"
#include "exec/address-spaces.h"
#include "target/arm/cpu-qom.h"
#include "target/arm/cpu.h"
#include "hw/cpu/a9mpcore.h"
#include "hw/char/serial.h"
#include "hw/char/serial.h"

#define TYPE_BRCM_BCM4708 "brcm_bcm4708"
#define BRCM_BCM4708(obj) \
    OBJECT_CHECK(BRCM_BCM4708State, (obj), TYPE_BRCM_BCM4708)

typedef struct BRCM_BCM4708State {
    ARMCPU *cpu;
    A9MPPrivState arm_cortex_a9_gic;
    MemoryRegion flash0;
    MemoryRegion flash1;
    MemoryRegion flash2;
    MemoryRegion ram0;
    MemoryRegion ram1;
    MemoryRegion mmio_sram0_mmio;
    MemoryRegion brcm_bcm4708_sysram0_mmio;
    MemoryRegion brcm_bus_axi0_mmio;
    uint32_t mmio_sram0_reserved[0x10000 >> 2];
    uint32_t brcm_bcm4708_sysram0_reserved[0x1000 >> 2];
    uint32_t brcm_bus_axi0_reserved[0x1000 >> 2];
} BRCM_BCM4708State;

static void mmio_sram0_update(void *opaque)
{
    /* BRCM_BCM4708State *s = opaque; */
}

static uint64_t mmio_sram0_read(void *opaque, hwaddr offset, unsigned size)
{
    BRCM_BCM4708State *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case 0x0 ... 0xfffc:
        res = s->mmio_sram0_reserved[offset >> 2];
        break;
    }
    return res;
}

static void mmio_sram0_write(void *opaque, hwaddr offset, uint64_t val, unsigned size)
{
    BRCM_BCM4708State *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case 0x0 ... 0xfffc:
        s->mmio_sram0_reserved[offset >> 2] = val;
        break;
    }
    mmio_sram0_update(s);
}

static const MemoryRegionOps mmio_sram_ops0 = {
    .read = mmio_sram0_read,
    .write = mmio_sram0_write,
    .endianness = DEVICE_LITTLE_ENDIAN,
};

static void brcm_bcm4708_sysram0_update(void *opaque)
{
    /* BRCM_BCM4708State *s = opaque; */
}

static uint64_t brcm_bcm4708_sysram0_read(void *opaque, hwaddr offset, unsigned size)
{
    BRCM_BCM4708State *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case 0x0 ... 0xffc:
        res = s->brcm_bcm4708_sysram0_reserved[offset >> 2];
        break;
    }
    return res;
}

static void brcm_bcm4708_sysram0_write(void *opaque, hwaddr offset, uint64_t val, unsigned size)
{
    BRCM_BCM4708State *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case 0x0 ... 0xffc:
        s->brcm_bcm4708_sysram0_reserved[offset >> 2] = val;
        break;
    }
    brcm_bcm4708_sysram0_update(s);
}

static const MemoryRegionOps brcm_bcm4708_sysram_ops0 = {
    .read = brcm_bcm4708_sysram0_read,
    .write = brcm_bcm4708_sysram0_write,
    .endianness = DEVICE_LITTLE_ENDIAN,
};

static void brcm_bus_axi0_update(void *opaque)
{
    /* BRCM_BCM4708State *s = opaque; */
}

static uint64_t brcm_bus_axi0_read(void *opaque, hwaddr offset, unsigned size)
{
    BRCM_BCM4708State *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case 0x0 ... 0xffc:
        res = s->brcm_bus_axi0_reserved[offset >> 2];
        break;
    }
    return res;
}

static void brcm_bus_axi0_write(void *opaque, hwaddr offset, uint64_t val, unsigned size)
{
    BRCM_BCM4708State *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case 0x0 ... 0xffc:
        s->brcm_bus_axi0_reserved[offset >> 2] = val;
        break;
    }
    brcm_bus_axi0_update(s);
}

static const MemoryRegionOps brcm_bus_axi_ops0 = {
    .read = brcm_bus_axi0_read,
    .write = brcm_bus_axi0_write,
    .endianness = DEVICE_LITTLE_ENDIAN,
};


static void brcm_bcm4708_reset(void *opaque)
{
    BRCM_BCM4708State *s = opaque;
    
}

static void brcm_bcm4708_init(MachineState *machine)
{
    BRCM_BCM4708State *s = g_new0(BRCM_BCM4708State, 1);
    Error *err = NULL;
    static struct arm_boot_info binfo;
    
    s->cpu = ARM_CPU(object_new(machine->cpu_type));
    object_property_set_int(OBJECT(s->cpu), 0x19020000 & 0xffff0000, "reset-cbar", &err);
    object_property_set_bool(OBJECT(s->cpu), true, "realized", &err);
    
    memory_region_allocate_system_memory(&s->ram0, OBJECT(machine), "ram0", 0x8000000);
    memory_region_add_subregion_overlap(get_system_memory(), 0x0, &s->ram0, 0);
    memory_region_allocate_system_memory(&s->ram1, OBJECT(machine), "ram1", 0x8000000);
    memory_region_add_subregion_overlap(get_system_memory(), 0x88000000, &s->ram1, 0);
    
    object_initialize(&s->arm_cortex_a9_gic, sizeof(s->arm_cortex_a9_gic), TYPE_A9MPCORE_PRIV);
    qdev_prop_set_uint32(DEVICE(&s->arm_cortex_a9_gic), "num-cpu", 2);
    object_property_set_bool(OBJECT(&s->arm_cortex_a9_gic), true, "realized", &err);
    sysbus_mmio_map(SYS_BUS_DEVICE(&s->arm_cortex_a9_gic), 0, 0x19021000 & 0xffff0000);
    
    sysbus_connect_irq(SYS_BUS_DEVICE(&s->arm_cortex_a9_gic), 0, qdev_get_gpio_in(DEVICE(s->cpu), ARM_CPU_IRQ));
    
    
    
    serial_mm_init(get_system_memory(), 0x18000400, 0, qdev_get_gpio_in(DEVICE(&s->arm_cortex_a9_gic), 85 - 32), 115200, serial_hd(0), DEVICE_LITTLE_ENDIAN);
    serial_mm_init(get_system_memory(), 0x18000300, 0, qdev_get_gpio_in(DEVICE(&s->arm_cortex_a9_gic), 85 - 32), 115200, serial_hd(1), DEVICE_LITTLE_ENDIAN);
    
    sysbus_create_varargs("l2x0", 0x19022000 , NULL);
    
    memory_region_init_rom(&s->flash0, NULL, "boot.flash.0", 0x600, &err);
    memory_region_add_subregion_overlap(get_system_memory(), 0x18028000, &s->flash0, 0);
    memory_region_init_rom(&s->flash1, NULL, "boot.flash.1", 0x600, &err);
    memory_region_add_subregion_overlap(get_system_memory(), 0x1811a408, &s->flash1, 0);
    memory_region_init_rom(&s->flash2, NULL, "boot.flash.2", 0x20, &err);
    memory_region_add_subregion_overlap(get_system_memory(), 0x18028f00, &s->flash2, 0);
    
    memory_region_init_io(&s->mmio_sram0_mmio, NULL, &mmio_sram_ops0, s, TYPE_BRCM_BCM4708, 0x10000);
    memory_region_add_subregion_overlap(get_system_memory(), 0xffff0000, &s->mmio_sram0_mmio, 0);
    memory_region_init_io(&s->brcm_bcm4708_sysram0_mmio, NULL, &brcm_bcm4708_sysram_ops0, s, TYPE_BRCM_BCM4708, 0x1000);
    memory_region_add_subregion_overlap(get_system_memory(), 0xffff0000, &s->brcm_bcm4708_sysram0_mmio, 0);
    memory_region_init_io(&s->brcm_bus_axi0_mmio, NULL, &brcm_bus_axi_ops0, s, TYPE_BRCM_BCM4708, 0x1000);
    memory_region_add_subregion_overlap(get_system_memory(), 0x18000000, &s->brcm_bus_axi0_mmio, -1);
    brcm_bcm4708_reset(s);

    binfo.board_id = 0xFFFFFFFF;
    binfo.ram_size = machine->ram_size;
    binfo.kernel_filename = machine->kernel_filename;
    binfo.kernel_cmdline = machine->kernel_cmdline;
    binfo.initrd_filename = machine->initrd_filename;
    arm_load_kernel(ARM_CPU(first_cpu), &binfo);
}

static void brcm_bcm4708_machine_init(MachineClass *mc)
{
    mc->desc = "brcm_bcm4708";
    mc->init = brcm_bcm4708_init;
    mc->default_ram_size = 128 * MiB;
    mc->default_cpu_type = ARM_CPU_TYPE_NAME("cortex-a9");
    mc->ignore_memory_transaction_failures = false;
}

DEFINE_MACHINE("brcm_bcm4708", brcm_bcm4708_machine_init)
