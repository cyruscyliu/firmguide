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

#define TYPE_QCA_AR7242 "qca_ar7242"
#define QCA_AR7242(obj) \
    OBJECT_CHECK(QCA_AR7242State, (obj), TYPE_QCA_AR7242)

typedef struct QCA_AR7242State {
    MIPSCPU *cpu;
    QCA_AR7240_MISC_INTCState qca_ar7240_misc_intc0;
    MemoryRegion stub0_mmio;
    uint32_t stub_reserved0[0x1000 >> 2];
    MemoryRegion stub1_mmio;
    uint32_t stub_reserved1[0x100 >> 2];
    MemoryRegion stub3_mmio;
    uint32_t stub_reserved3[0x28 >> 2];
    MemoryRegion stub4_mmio;
    uint32_t stub_reserved4[0x8 >> 2];
    MemoryRegion stub5_mmio;
    uint32_t stub_reserved5[0x3c >> 2];
    MemoryRegion stub6_mmio;
    uint32_t stub_reserved6[0x8 >> 2];
    MemoryRegion stub8_mmio;
    uint32_t stub_reserved8[0x4 >> 2];
    MemoryRegion stub9_mmio;
    uint32_t stub_reserved9[0x1000 >> 2];
    MemoryRegion stub10_mmio;
    uint32_t stub_reserved10[0x100 >> 2];
    MemoryRegion stub11_mmio;
    uint32_t stub_reserved11[0x200 >> 2];
    MemoryRegion stub12_mmio;
    uint32_t stub_reserved12[0x200 >> 2];
    MemoryRegion stub13_mmio;
    uint32_t stub_reserved13[0x1000 >> 2];
    MemoryRegion stub14_mmio;
    uint32_t stub_reserved14[0x10 >> 2];
    MemoryRegion flash;
    MemoryRegion ram;
} QCA_AR7242State;

static void stub0_update(void *opaque)
{
    /* QCA_AR7242State *s = opaque; */
}

static uint64_t stub0_read(void *opaque, hwaddr offset, unsigned size)
{
    QCA_AR7242State *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case 0x0 ... 0xffc:
        res = s->stub_reserved0[offset >> 2];
        break;
    }
    return res;
}

static void stub0_write(void *opaque, hwaddr offset, uint64_t val, unsigned size)
{
    QCA_AR7242State *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case 0x0 ... 0xffc:
        s->stub_reserved0[offset >> 2] = val;
        break;
    }
    stub0_update(s);
}

static const MemoryRegionOps stub0_ops = {
    .read = stub0_read,
    .write = stub0_write,
    .endianness = DEVICE_BIG_ENDIAN,
};

static void stub1_update(void *opaque)
{
    /* QCA_AR7242State *s = opaque; */
}

static uint64_t stub1_read(void *opaque, hwaddr offset, unsigned size)
{
    QCA_AR7242State *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case 0x0 ... 0xfc:
        res = s->stub_reserved1[offset >> 2];
        break;
    }
    return res;
}

static void stub1_write(void *opaque, hwaddr offset, uint64_t val, unsigned size)
{
    QCA_AR7242State *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case 0x0 ... 0xfc:
        s->stub_reserved1[offset >> 2] = val;
        break;
    }
    stub1_update(s);
}

static const MemoryRegionOps stub1_ops = {
    .read = stub1_read,
    .write = stub1_write,
    .endianness = DEVICE_BIG_ENDIAN,
};

static void stub3_update(void *opaque)
{
    /* QCA_AR7242State *s = opaque; */
}

static uint64_t stub3_read(void *opaque, hwaddr offset, unsigned size)
{
    QCA_AR7242State *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case 0x0 ... 0x24:
        res = s->stub_reserved3[offset >> 2];
        break;
    }
    return res;
}

static void stub3_write(void *opaque, hwaddr offset, uint64_t val, unsigned size)
{
    QCA_AR7242State *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case 0x0 ... 0x24:
        s->stub_reserved3[offset >> 2] = val;
        break;
    }
    stub3_update(s);
}

static const MemoryRegionOps stub3_ops = {
    .read = stub3_read,
    .write = stub3_write,
    .endianness = DEVICE_BIG_ENDIAN,
};

static void stub4_update(void *opaque)
{
    /* QCA_AR7242State *s = opaque; */
}

static uint64_t stub4_read(void *opaque, hwaddr offset, unsigned size)
{
    QCA_AR7242State *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case 0x0 ... 0x4:
        res = s->stub_reserved4[offset >> 2];
        break;
    }
    return res;
}

static void stub4_write(void *opaque, hwaddr offset, uint64_t val, unsigned size)
{
    QCA_AR7242State *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case 0x0 ... 0x4:
        s->stub_reserved4[offset >> 2] = val;
        break;
    }
    stub4_update(s);
}

static const MemoryRegionOps stub4_ops = {
    .read = stub4_read,
    .write = stub4_write,
    .endianness = DEVICE_BIG_ENDIAN,
};

static void stub5_update(void *opaque)
{
    /* QCA_AR7242State *s = opaque; */
}

static uint64_t stub5_read(void *opaque, hwaddr offset, unsigned size)
{
    QCA_AR7242State *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case 0x0 ... 0x38:
        res = s->stub_reserved5[offset >> 2];
        break;
    }
    return res;
}

static void stub5_write(void *opaque, hwaddr offset, uint64_t val, unsigned size)
{
    QCA_AR7242State *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case 0x0 ... 0x38:
        s->stub_reserved5[offset >> 2] = val;
        break;
    }
    stub5_update(s);
}

static const MemoryRegionOps stub5_ops = {
    .read = stub5_read,
    .write = stub5_write,
    .endianness = DEVICE_BIG_ENDIAN,
};

static void stub6_update(void *opaque)
{
    /* QCA_AR7242State *s = opaque; */
}

static uint64_t stub6_read(void *opaque, hwaddr offset, unsigned size)
{
    QCA_AR7242State *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case 0x0 ... 0x4:
        res = s->stub_reserved6[offset >> 2];
        break;
    }
    return res;
}

static void stub6_write(void *opaque, hwaddr offset, uint64_t val, unsigned size)
{
    QCA_AR7242State *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case 0x0 ... 0x4:
        s->stub_reserved6[offset >> 2] = val;
        break;
    }
    stub6_update(s);
}

static const MemoryRegionOps stub6_ops = {
    .read = stub6_read,
    .write = stub6_write,
    .endianness = DEVICE_BIG_ENDIAN,
};

static void stub8_update(void *opaque)
{
    /* QCA_AR7242State *s = opaque; */
}

static uint64_t stub8_read(void *opaque, hwaddr offset, unsigned size)
{
    QCA_AR7242State *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case 0x0:
        res = s->stub_reserved8[offset >> 2];
        break;
    }
    return res;
}

static void stub8_write(void *opaque, hwaddr offset, uint64_t val, unsigned size)
{
    QCA_AR7242State *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case 0x0:
        s->stub_reserved8[offset >> 2] = val;
        break;
    }
    stub8_update(s);
}

static const MemoryRegionOps stub8_ops = {
    .read = stub8_read,
    .write = stub8_write,
    .endianness = DEVICE_BIG_ENDIAN,
};

static void stub9_update(void *opaque)
{
    /* QCA_AR7242State *s = opaque; */
}

static uint64_t stub9_read(void *opaque, hwaddr offset, unsigned size)
{
    QCA_AR7242State *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case 0x0 ... 0xffc:
        res = s->stub_reserved9[offset >> 2];
        break;
    }
    return res;
}

static void stub9_write(void *opaque, hwaddr offset, uint64_t val, unsigned size)
{
    QCA_AR7242State *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case 0x0 ... 0xffc:
        s->stub_reserved9[offset >> 2] = val;
        break;
    }
    stub9_update(s);
}

static const MemoryRegionOps stub9_ops = {
    .read = stub9_read,
    .write = stub9_write,
    .endianness = DEVICE_BIG_ENDIAN,
};

static void stub10_update(void *opaque)
{
    /* QCA_AR7242State *s = opaque; */
}

static uint64_t stub10_read(void *opaque, hwaddr offset, unsigned size)
{
    QCA_AR7242State *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case 0x0 ... 0xfc:
        res = s->stub_reserved10[offset >> 2];
        break;
    }
    return res;
}

static void stub10_write(void *opaque, hwaddr offset, uint64_t val, unsigned size)
{
    QCA_AR7242State *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case 0x0 ... 0xfc:
        s->stub_reserved10[offset >> 2] = val;
        break;
    }
    stub10_update(s);
}

static const MemoryRegionOps stub10_ops = {
    .read = stub10_read,
    .write = stub10_write,
    .endianness = DEVICE_BIG_ENDIAN,
};

static void stub11_update(void *opaque)
{
    /* QCA_AR7242State *s = opaque; */
}

static uint64_t stub11_read(void *opaque, hwaddr offset, unsigned size)
{
    QCA_AR7242State *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case 0x0 ... 0x1fc:
        res = s->stub_reserved11[offset >> 2];
        break;
    }
    return res;
}

static void stub11_write(void *opaque, hwaddr offset, uint64_t val, unsigned size)
{
    QCA_AR7242State *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case 0x0 ... 0x1fc:
        s->stub_reserved11[offset >> 2] = val;
        break;
    }
    stub11_update(s);
}

static const MemoryRegionOps stub11_ops = {
    .read = stub11_read,
    .write = stub11_write,
    .endianness = DEVICE_BIG_ENDIAN,
};

static void stub12_update(void *opaque)
{
    /* QCA_AR7242State *s = opaque; */
}

static uint64_t stub12_read(void *opaque, hwaddr offset, unsigned size)
{
    QCA_AR7242State *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case 0x0 ... 0x1fc:
        res = s->stub_reserved12[offset >> 2];
        break;
    }
    return res;
}

static void stub12_write(void *opaque, hwaddr offset, uint64_t val, unsigned size)
{
    QCA_AR7242State *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case 0x0 ... 0x1fc:
        s->stub_reserved12[offset >> 2] = val;
        break;
    }
    stub12_update(s);
}

static const MemoryRegionOps stub12_ops = {
    .read = stub12_read,
    .write = stub12_write,
    .endianness = DEVICE_BIG_ENDIAN,
};

static void stub13_update(void *opaque)
{
    /* QCA_AR7242State *s = opaque; */
}

static uint64_t stub13_read(void *opaque, hwaddr offset, unsigned size)
{
    QCA_AR7242State *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case 0x0 ... 0xffc:
        res = s->stub_reserved13[offset >> 2];
        break;
    }
    return res;
}

static void stub13_write(void *opaque, hwaddr offset, uint64_t val, unsigned size)
{
    QCA_AR7242State *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case 0x0 ... 0xffc:
        s->stub_reserved13[offset >> 2] = val;
        break;
    }
    stub13_update(s);
}

static const MemoryRegionOps stub13_ops = {
    .read = stub13_read,
    .write = stub13_write,
    .endianness = DEVICE_BIG_ENDIAN,
};

static void stub14_update(void *opaque)
{
    /* QCA_AR7242State *s = opaque; */
}

static uint64_t stub14_read(void *opaque, hwaddr offset, unsigned size)
{
    QCA_AR7242State *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case 0x0 ... 0xc:
        res = s->stub_reserved14[offset >> 2];
        break;
    }
    return res;
}

static void stub14_write(void *opaque, hwaddr offset, uint64_t val, unsigned size)
{
    QCA_AR7242State *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case 0x0 ... 0xc:
        s->stub_reserved14[offset >> 2] = val;
        break;
    }
    stub14_update(s);
}

static const MemoryRegionOps stub14_ops = {
    .read = stub14_read,
    .write = stub14_write,
    .endianness = DEVICE_BIG_ENDIAN,
};

static void qca_ar7242_reset(void *opaque)
{
    QCA_AR7242State *s = opaque;
    
    s->stub_reserved0[0] = 0x0;
    s->stub_reserved1[0] = 0x0;
    s->stub_reserved3[0] = 0x0;
    s->stub_reserved4[0] = 0x0;
    s->stub_reserved5[0] = 0x0;
    s->stub_reserved6[0] = 0x0;
    s->stub_reserved8[0] = 0x0;
    s->stub_reserved9[0] = 0x0;
    s->stub_reserved10[0] = 0x0;
    s->stub_reserved11[0] = 0x0;
    s->stub_reserved12[0] = 0x0;
    s->stub_reserved13[0] = 0x0;
    s->stub_reserved14[0] = 0x0;
}

static void qca_ar7242_init(MachineState *machine)
{
    QCA_AR7242State *s = g_new0(QCA_AR7242State, 1);
    Error *err = NULL;
    static struct mips_boot_info binfo;
    
    s->cpu = MIPS_CPU(object_new(machine->cpu_type));
    object_property_set_bool(OBJECT(s->cpu), true, "realized", &err);

    memory_region_allocate_system_memory(&s->ram, OBJECT(machine), "ram", machine->ram_size);
    memory_region_add_subregion_overlap(get_system_memory(), 0, &s->ram, 0);
    
    
    cpu_mips_irq_init_cpu(s->cpu);
    cpu_mips_clock_init(s->cpu);
    object_initialize(&s->qca_ar7240_misc_intc0, sizeof(s->qca_ar7240_misc_intc0), TYPE_QCA_AR7240_MISC_INTC);
    qdev_set_parent_bus(DEVICE(&s->qca_ar7240_misc_intc0), sysbus_get_default());
    object_property_set_bool(OBJECT(&s->qca_ar7240_misc_intc0), true, "realized", &err);
    sysbus_mmio_map(SYS_BUS_DEVICE(&s->qca_ar7240_misc_intc0), 0, 0x18060010);
    
    qdev_connect_gpio_out(DEVICE(&s->qca_ar7240_misc_intc0), 0, s->cpu->env.irq[6]);
    
    
    serial_mm_init(get_system_memory(), 0x18020000, 2, qdev_get_gpio_in(DEVICE(&s->qca_ar7240_misc_intc0), 3), 115200, serial_hd(0), DEVICE_BIG_ENDIAN);
    
    
    memory_region_init_io(&s->stub0_mmio, NULL, &stub0_ops, s, TYPE_QCA_AR7242, 0x1000);
    memory_region_add_subregion_overlap(get_system_memory(), 0x14000000, &s->stub0_mmio, 0);
    memory_region_init_io(&s->stub1_mmio, NULL, &stub1_ops, s, TYPE_QCA_AR7242, 0x100);
    memory_region_add_subregion_overlap(get_system_memory(), 0x18000000, &s->stub1_mmio, 0);
    memory_region_init_io(&s->stub3_mmio, NULL, &stub3_ops, s, TYPE_QCA_AR7242, 0x28);
    memory_region_add_subregion_overlap(get_system_memory(), 0x18040000, &s->stub3_mmio, 0);
    memory_region_init_io(&s->stub4_mmio, NULL, &stub4_ops, s, TYPE_QCA_AR7242, 0x8);
    memory_region_add_subregion_overlap(get_system_memory(), 0x18040028, &s->stub4_mmio, 0);
    memory_region_init_io(&s->stub5_mmio, NULL, &stub5_ops, s, TYPE_QCA_AR7242, 0x3c);
    memory_region_add_subregion_overlap(get_system_memory(), 0x18050000, &s->stub5_mmio, 0);
    memory_region_init_io(&s->stub6_mmio, NULL, &stub6_ops, s, TYPE_QCA_AR7242, 0x8);
    memory_region_add_subregion_overlap(get_system_memory(), 0x18060008, &s->stub6_mmio, 0);
    memory_region_init_io(&s->stub8_mmio, NULL, &stub8_ops, s, TYPE_QCA_AR7242, 0x4);
    memory_region_add_subregion_overlap(get_system_memory(), 0x1806001c, &s->stub8_mmio, 0);
    memory_region_init_io(&s->stub9_mmio, NULL, &stub9_ops, s, TYPE_QCA_AR7242, 0x1000);
    memory_region_add_subregion_overlap(get_system_memory(), 0x180c0000, &s->stub9_mmio, 0);
    memory_region_init_io(&s->stub10_mmio, NULL, &stub10_ops, s, TYPE_QCA_AR7242, 0x100);
    memory_region_add_subregion_overlap(get_system_memory(), 0x180f0000, &s->stub10_mmio, 0);
    memory_region_init_io(&s->stub11_mmio, NULL, &stub11_ops, s, TYPE_QCA_AR7242, 0x200);
    memory_region_add_subregion_overlap(get_system_memory(), 0x19000000, &s->stub11_mmio, 0);
    memory_region_init_io(&s->stub12_mmio, NULL, &stub12_ops, s, TYPE_QCA_AR7242, 0x200);
    memory_region_add_subregion_overlap(get_system_memory(), 0x1a000000, &s->stub12_mmio, 0);
    memory_region_init_io(&s->stub13_mmio, NULL, &stub13_ops, s, TYPE_QCA_AR7242, 0x1000);
    memory_region_add_subregion_overlap(get_system_memory(), 0x1b000000, &s->stub13_mmio, 0);
    memory_region_init_io(&s->stub14_mmio, NULL, &stub14_ops, s, TYPE_QCA_AR7242, 0x10);
    memory_region_add_subregion_overlap(get_system_memory(), 0x1f000000, &s->stub14_mmio, 0);
    
    memory_region_init_rom(&s->flash, NULL, "boot.flash", 0x400000, &err);
    memory_region_add_subregion_overlap(get_system_memory(), 0x1fc00000, &s->flash, 0);
    qca_ar7242_reset(s);

    binfo.board_id = 0xFFFFFFFF;
    binfo.ram_size = machine->ram_size;
    binfo.kernel_filename = machine->kernel_filename;
    binfo.kernel_cmdline = machine->kernel_cmdline;
    binfo.initrd_filename = machine->initrd_filename;
    mips_load_kernel(MIPS_CPU(first_cpu), &binfo);
}

static void qca_ar7242_machine_init(MachineClass *mc)
{
    mc->desc = "qca_ar7242";
    mc->init = qca_ar7242_init;
    mc->default_ram_size = 256 * MiB;
    mc->default_cpu_type = MIPS_CPU_TYPE_NAME("24Kc");
    mc->ignore_memory_transaction_failures = false;
}

DEFINE_MACHINE("qca_ar7242", qca_ar7242_machine_init)

