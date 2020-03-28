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
    MemoryRegion stub0_mmio;
    uint32_t stub_reserved0[0x300 >> 2];
    MemoryRegion stub2_mmio;
    uint32_t stub_reserved2[0xb00 >> 2];
    MemoryRegion stub4_mmio;
    uint32_t stub_reserved4[0x600 >> 2];
    MemoryRegion stub5_mmio;
    uint32_t stub_reserved5[0x20 >> 2];
    MemoryRegion stub6_mmio;
    uint32_t stub_reserved6[0x600 >> 2];
    MemoryRegion ram;
    MemoryRegion ram0;
    MemoryRegion ram1;
    MemoryRegion ram2;
    MemoryRegion ram3;
} BRCM_BCM4708State;

static void stub0_update(void *opaque)
{
    /* BRCM_BCM4708State *s = opaque; */
}

static uint64_t stub0_read(void *opaque, hwaddr offset, unsigned size)
{
    BRCM_BCM4708State *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case 0x0 ... 0x2fc:
        res = s->stub_reserved0[offset >> 2];
        break;
    }
    return res;
}

static void stub0_write(void *opaque, hwaddr offset, uint64_t val, unsigned size)
{
    BRCM_BCM4708State *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case 0x0 ... 0x2fc:
        s->stub_reserved0[offset >> 2] = val;
        break;
    }
    stub0_update(s);
}

static const MemoryRegionOps stub0_ops = {
    .read = stub0_read,
    .write = stub0_write,
    .endianness = DEVICE_LITTLE_ENDIAN,
};

static void stub2_update(void *opaque)
{
    /* BRCM_BCM4708State *s = opaque; */
}

static uint64_t stub2_read(void *opaque, hwaddr offset, unsigned size)
{
    BRCM_BCM4708State *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case 0x0 ... 0xafc:
        res = s->stub_reserved2[offset >> 2];
        break;
    }
    return res;
}

static void stub2_write(void *opaque, hwaddr offset, uint64_t val, unsigned size)
{
    BRCM_BCM4708State *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case 0x0 ... 0xafc:
        s->stub_reserved2[offset >> 2] = val;
        break;
    }
    stub2_update(s);
}

static const MemoryRegionOps stub2_ops = {
    .read = stub2_read,
    .write = stub2_write,
    .endianness = DEVICE_LITTLE_ENDIAN,
};

static void stub4_update(void *opaque)
{
    /* BRCM_BCM4708State *s = opaque; */
}

static uint64_t stub4_read(void *opaque, hwaddr offset, unsigned size)
{
    BRCM_BCM4708State *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case 0x0 ... 0x5fc:
        res = s->stub_reserved4[offset >> 2];
        break;
    }
    return res;
}

static void stub4_write(void *opaque, hwaddr offset, uint64_t val, unsigned size)
{
    BRCM_BCM4708State *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case 0x0 ... 0x5fc:
        s->stub_reserved4[offset >> 2] = val;
        break;
    }
    stub4_update(s);
}

static const MemoryRegionOps stub4_ops = {
    .read = stub4_read,
    .write = stub4_write,
    .endianness = DEVICE_LITTLE_ENDIAN,
};

static void stub5_update(void *opaque)
{
    /* BRCM_BCM4708State *s = opaque; */
}

static uint64_t stub5_read(void *opaque, hwaddr offset, unsigned size)
{
    BRCM_BCM4708State *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case 0x0 ... 0x1c:
        res = s->stub_reserved5[offset >> 2];
        break;
    }
    return res;
}

static void stub5_write(void *opaque, hwaddr offset, uint64_t val, unsigned size)
{
    BRCM_BCM4708State *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case 0x0 ... 0x1c:
        s->stub_reserved5[offset >> 2] = val;
        break;
    }
    stub5_update(s);
}

static const MemoryRegionOps stub5_ops = {
    .read = stub5_read,
    .write = stub5_write,
    .endianness = DEVICE_LITTLE_ENDIAN,
};

static void stub6_update(void *opaque)
{
    /* BRCM_BCM4708State *s = opaque; */
}

static uint64_t stub6_read(void *opaque, hwaddr offset, unsigned size)
{
    BRCM_BCM4708State *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case 0x0 ... 0x5fc:
        res = s->stub_reserved6[offset >> 2];
        break;
    }
    return res;
}

static void stub6_write(void *opaque, hwaddr offset, uint64_t val, unsigned size)
{
    BRCM_BCM4708State *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case 0x0 ... 0x5fc:
        s->stub_reserved6[offset >> 2] = val;
        break;
    }
    stub6_update(s);
}

static const MemoryRegionOps stub6_ops = {
    .read = stub6_read,
    .write = stub6_write,
    .endianness = DEVICE_LITTLE_ENDIAN,
};

static void brcm_bcm4708_reset(void *opaque)
{
    BRCM_BCM4708State *s = opaque;
    
    s->stub_reserved0[0] = 0x0;
    s->stub_reserved2[0] = 0x0;
    s->stub_reserved4[0] = 0x0;
    s->stub_reserved5[0] = 0x0;
    s->stub_reserved6[0] = 0x0;
}

static void brcm_bcm4708_init(MachineState *machine)
{
    BRCM_BCM4708State *s = g_new0(BRCM_BCM4708State, 1);
    Error *err = NULL;
    static struct arm_boot_info binfo;
    
    s->cpu = ARM_CPU(object_new(machine->cpu_type));
    object_property_set_int(OBJECT(s->cpu), 0x19020000 & 0xffff0000, "reset-cbar", &err);
    object_property_set_bool(OBJECT(s->cpu), true, "realized", &err);

    memory_region_allocate_system_memory(&s->ram, OBJECT(machine), "ram", machine->ram_size);
    memory_region_add_subregion_overlap(get_system_memory(), 0, &s->ram, 0);
    
    memory_region_allocate_system_memory(&s->ram0, OBJECT(machine), "ram0", 134217728);
    memory_region_add_subregion_overlap(get_system_memory(), 2281701376, &s->ram0, 0);
    memory_region_allocate_system_memory(&s->ram1, OBJECT(machine), "ram1", 134217728);
    memory_region_add_subregion_overlap(get_system_memory(), 2281701376, &s->ram1, 0);
    memory_region_allocate_system_memory(&s->ram2, OBJECT(machine), "ram2", 134217728);
    memory_region_add_subregion_overlap(get_system_memory(), 2281701376, &s->ram2, 0);
    memory_region_allocate_system_memory(&s->ram3, OBJECT(machine), "ram3", 134217728);
    memory_region_add_subregion_overlap(get_system_memory(), 2281701376, &s->ram3, 0);
    
    object_initialize(&s->arm_cortex_a9_gic, sizeof(s->arm_cortex_a9_gic), TYPE_A9MPCORE_PRIV);
    qdev_prop_set_uint32(DEVICE(&s->arm_cortex_a9_gic), "num-cpu", 2);
    object_property_set_bool(OBJECT(&s->arm_cortex_a9_gic), true, "realized", &err);
    sysbus_mmio_map(SYS_BUS_DEVICE(&s->arm_cortex_a9_gic), 0, 0x19021000 & 0xffff0000);
    
    sysbus_connect_irq(SYS_BUS_DEVICE(&s->arm_cortex_a9_gic), 0, qdev_get_gpio_in(DEVICE(s->cpu), ARM_CPU_IRQ));
    
    
    
    serial_mm_init(get_system_memory(), 0x18000400, 0, qdev_get_gpio_in(DEVICE(&s->arm_cortex_a9_gic), 85 - 32), 115200, serial_hd(0), DEVICE_LITTLE_ENDIAN);
    serial_mm_init(get_system_memory(), 0x18000300, 0, qdev_get_gpio_in(DEVICE(&s->arm_cortex_a9_gic), 85 - 32), 115200, serial_hd(1), DEVICE_LITTLE_ENDIAN);
    
    sysbus_create_varargs("l2x0", 0x19022000 , NULL);
    
    memory_region_init_io(&s->stub0_mmio, NULL, &stub0_ops, s, TYPE_BRCM_BCM4708, 0x300);
    memory_region_add_subregion_overlap(get_system_memory(), 0x18000000, &s->stub0_mmio, 0);
    memory_region_init_io(&s->stub2_mmio, NULL, &stub2_ops, s, TYPE_BRCM_BCM4708, 0xb00);
    memory_region_add_subregion_overlap(get_system_memory(), 0x18000500, &s->stub2_mmio, 0);
    memory_region_init_io(&s->stub4_mmio, NULL, &stub4_ops, s, TYPE_BRCM_BCM4708, 0x600);
    memory_region_add_subregion_overlap(get_system_memory(), 0x18028000, &s->stub4_mmio, 0);
    memory_region_init_io(&s->stub5_mmio, NULL, &stub5_ops, s, TYPE_BRCM_BCM4708, 0x20);
    memory_region_add_subregion_overlap(get_system_memory(), 0x18028f00, &s->stub5_mmio, 0);
    memory_region_init_io(&s->stub6_mmio, NULL, &stub6_ops, s, TYPE_BRCM_BCM4708, 0x600);
    memory_region_add_subregion_overlap(get_system_memory(), 0x1811a408, &s->stub6_mmio, 0);
    
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
    mc->default_ram_size = 0x8000000;
    mc->default_cpu_type = ARM_CPU_TYPE_NAME("cortex-a9");
    mc->ignore_memory_transaction_failures = false;
}

DEFINE_MACHINE("brcm_bcm4708", brcm_bcm4708_machine_init)

