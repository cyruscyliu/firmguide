/* 
 * automatically generated, don't change
 */

#include "qemu/osdep.h"
#include "qemu/log.h"
#include "hw/sysbus.h"
#include "qemu/units.h"
#include "target/mips/cpu.h"
#include "target/arm/cpu-qom.h"
#include "hw/mips/cpudevs.h"
#include "exec/address-spaces.h"
#include "hw/char/serial.h"
#include "hw/mips/mips.h"
#include "hw/boards.h"

#define TYPE_AR71XX_GENERIC "ar71xx_generic"
#define AR71XX_GENERIC(obj) \
    OBJECT_CHECK(AR71XXGENERICState, (obj), TYPE_AR71XX_GENERIC)

typedef struct AR71XXGENERICState {
    MIPSCPU *cpu;
    MemoryRegion ram;
    MemoryRegion stub0_mmio;
    uint32_t stub_reserved0;
    MemoryRegion stub1_mmio;
    uint32_t stub_reserved1;
    MemoryRegion stub10_mmio;
    uint32_t stub_reserved10;
    MemoryRegion stub11_mmio;
    uint32_t stub_reserved11;
    MemoryRegion stub12_mmio;
    uint32_t stub_reserved12;
    MemoryRegion stub13_mmio;
    uint32_t stub_reserved13;
    MemoryRegion stub14_mmio;
    uint32_t stub_reserved14;
    MemoryRegion stub15_mmio;
    uint32_t stub_reserved15;
    MemoryRegion stub16_mmio;
    uint32_t stub_reserved16;
    MemoryRegion stub2_mmio;
    uint32_t stub_reserved2;
    MemoryRegion stub3_mmio;
    uint32_t stub_reserved3;
    MemoryRegion stub4_mmio;
    uint32_t stub_reserved4;
    MemoryRegion stub5_mmio;
    uint32_t stub_reserved5;
    MemoryRegion stub6_mmio;
    uint32_t stub_reserved6;
    MemoryRegion stub7_mmio;
    uint32_t stub_reserved7;
    MemoryRegion stub8_mmio;
    uint32_t stub_reserved8;
    MemoryRegion stub9_mmio;
    uint32_t stub_reserved9;
} AR71XXGENERICState;

static void stub0_update(void *opaque)
{
    /* AR71XXGENERICState *s = opaque; */
}

static uint64_t stub0_read(void *opaque, hwaddr offset, unsigned size)
{
    AR71XXGENERICState *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case 0x0 ... 0x4:
        res = s->stub_reserved0;
        break;
    }
    return res;
}

static void stub0_write(void *opaque, hwaddr offset, uint64_t val, unsigned size)
{
    AR71XXGENERICState *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case 0x0 ... 0x4:
        s->stub_reserved0 = val;
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
    /* AR71XXGENERICState *s = opaque; */
}

static uint64_t stub1_read(void *opaque, hwaddr offset, unsigned size)
{
    AR71XXGENERICState *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case 0x0:
        res = s->stub_reserved1;
        break;
    }
    return res;
}

static void stub1_write(void *opaque, hwaddr offset, uint64_t val, unsigned size)
{
    AR71XXGENERICState *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case 0x0:
        s->stub_reserved1 = val;
        break;
    }
    stub1_update(s);
}

static const MemoryRegionOps stub1_ops = {
    .read = stub1_read,
    .write = stub1_write,
    .endianness = DEVICE_BIG_ENDIAN,
};

static void stub10_update(void *opaque)
{
    /* AR71XXGENERICState *s = opaque; */
}

static uint64_t stub10_read(void *opaque, hwaddr offset, unsigned size)
{
    AR71XXGENERICState *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case 0x0 ... 0x1fc:
        res = s->stub_reserved10;
        break;
    }
    return res;
}

static void stub10_write(void *opaque, hwaddr offset, uint64_t val, unsigned size)
{
    AR71XXGENERICState *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case 0x0 ... 0x1fc:
        s->stub_reserved10 = val;
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
    /* AR71XXGENERICState *s = opaque; */
}

static uint64_t stub11_read(void *opaque, hwaddr offset, unsigned size)
{
    AR71XXGENERICState *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case 0x0 ... 0xfffffc:
        res = s->stub_reserved11;
        break;
    }
    return res;
}

static void stub11_write(void *opaque, hwaddr offset, uint64_t val, unsigned size)
{
    AR71XXGENERICState *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case 0x0 ... 0xfffffc:
        s->stub_reserved11 = val;
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
    /* AR71XXGENERICState *s = opaque; */
}

static uint64_t stub12_read(void *opaque, hwaddr offset, unsigned size)
{
    AR71XXGENERICState *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case 0x0 ... 0xfc:
        res = s->stub_reserved12;
        break;
    }
    return res;
}

static void stub12_write(void *opaque, hwaddr offset, uint64_t val, unsigned size)
{
    AR71XXGENERICState *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case 0x0 ... 0xfc:
        s->stub_reserved12 = val;
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
    /* AR71XXGENERICState *s = opaque; */
}

static uint64_t stub13_read(void *opaque, hwaddr offset, unsigned size)
{
    AR71XXGENERICState *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case 0x0 ... 0x2fffc:
        res = s->stub_reserved13;
        break;
    }
    return res;
}

static void stub13_write(void *opaque, hwaddr offset, uint64_t val, unsigned size)
{
    AR71XXGENERICState *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case 0x0 ... 0x2fffc:
        s->stub_reserved13 = val;
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
    /* AR71XXGENERICState *s = opaque; */
}

static uint64_t stub14_read(void *opaque, hwaddr offset, unsigned size)
{
    AR71XXGENERICState *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case 0x0 ... 0x1fffc:
        res = s->stub_reserved14;
        break;
    }
    return res;
}

static void stub14_write(void *opaque, hwaddr offset, uint64_t val, unsigned size)
{
    AR71XXGENERICState *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case 0x0 ... 0x1fffc:
        s->stub_reserved14 = val;
        break;
    }
    stub14_update(s);
}

static const MemoryRegionOps stub14_ops = {
    .read = stub14_read,
    .write = stub14_write,
    .endianness = DEVICE_BIG_ENDIAN,
};

static void stub15_update(void *opaque)
{
    /* AR71XXGENERICState *s = opaque; */
}

static uint64_t stub15_read(void *opaque, hwaddr offset, unsigned size)
{
    AR71XXGENERICState *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case 0x0:
        res = s->stub_reserved15;
        break;
    }
    return res;
}

static void stub15_write(void *opaque, hwaddr offset, uint64_t val, unsigned size)
{
    AR71XXGENERICState *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case 0x0:
        s->stub_reserved15 = val;
        break;
    }
    stub15_update(s);
}

static const MemoryRegionOps stub15_ops = {
    .read = stub15_read,
    .write = stub15_write,
    .endianness = DEVICE_BIG_ENDIAN,
};

static void stub16_update(void *opaque)
{
    /* AR71XXGENERICState *s = opaque; */
}

static uint64_t stub16_read(void *opaque, hwaddr offset, unsigned size)
{
    AR71XXGENERICState *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case 0x0 ... 0x68:
        res = s->stub_reserved16;
        break;
    }
    return res;
}

static void stub16_write(void *opaque, hwaddr offset, uint64_t val, unsigned size)
{
    AR71XXGENERICState *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case 0x0 ... 0x68:
        s->stub_reserved16 = val;
        break;
    }
    stub16_update(s);
}

static const MemoryRegionOps stub16_ops = {
    .read = stub16_read,
    .write = stub16_write,
    .endianness = DEVICE_BIG_ENDIAN,
};

static void stub2_update(void *opaque)
{
    /* AR71XXGENERICState *s = opaque; */
}

static uint64_t stub2_read(void *opaque, hwaddr offset, unsigned size)
{
    AR71XXGENERICState *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case 0x0 ... 0x74:
        res = s->stub_reserved2;
        break;
    }
    return res;
}

static void stub2_write(void *opaque, hwaddr offset, uint64_t val, unsigned size)
{
    AR71XXGENERICState *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case 0x0 ... 0x74:
        s->stub_reserved2 = val;
        break;
    }
    stub2_update(s);
}

static const MemoryRegionOps stub2_ops = {
    .read = stub2_read,
    .write = stub2_write,
    .endianness = DEVICE_BIG_ENDIAN,
};

static void stub3_update(void *opaque)
{
    /* AR71XXGENERICState *s = opaque; */
}

static uint64_t stub3_read(void *opaque, hwaddr offset, unsigned size)
{
    AR71XXGENERICState *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case 0x0:
        res = s->stub_reserved3;
        break;
    }
    return res;
}

static void stub3_write(void *opaque, hwaddr offset, uint64_t val, unsigned size)
{
    AR71XXGENERICState *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case 0x0:
        s->stub_reserved3 = val;
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
    /* AR71XXGENERICState *s = opaque; */
}

static uint64_t stub4_read(void *opaque, hwaddr offset, unsigned size)
{
    AR71XXGENERICState *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case 0x0 ... 0xf8:
        res = s->stub_reserved4;
        break;
    }
    return res;
}

static void stub4_write(void *opaque, hwaddr offset, uint64_t val, unsigned size)
{
    AR71XXGENERICState *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case 0x0 ... 0xf8:
        s->stub_reserved4 = val;
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
    /* AR71XXGENERICState *s = opaque; */
}

static uint64_t stub5_read(void *opaque, hwaddr offset, unsigned size)
{
    AR71XXGENERICState *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case 0x0:
        res = s->stub_reserved5;
        break;
    }
    return res;
}

static void stub5_write(void *opaque, hwaddr offset, uint64_t val, unsigned size)
{
    AR71XXGENERICState *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case 0x0:
        s->stub_reserved5 = val;
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
    /* AR71XXGENERICState *s = opaque; */
}

static uint64_t stub6_read(void *opaque, hwaddr offset, unsigned size)
{
    AR71XXGENERICState *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case 0x0 ... 0xfc:
        res = s->stub_reserved6;
        break;
    }
    return res;
}

static void stub6_write(void *opaque, hwaddr offset, uint64_t val, unsigned size)
{
    AR71XXGENERICState *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case 0x0 ... 0xfc:
        s->stub_reserved6 = val;
        break;
    }
    stub6_update(s);
}

static const MemoryRegionOps stub6_ops = {
    .read = stub6_read,
    .write = stub6_write,
    .endianness = DEVICE_BIG_ENDIAN,
};

static void stub7_update(void *opaque)
{
    /* AR71XXGENERICState *s = opaque; */
}

static uint64_t stub7_read(void *opaque, hwaddr offset, unsigned size)
{
    AR71XXGENERICState *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case 0x0 ... 0x4:
        res = s->stub_reserved7;
        break;
    }
    return res;
}

static void stub7_write(void *opaque, hwaddr offset, uint64_t val, unsigned size)
{
    AR71XXGENERICState *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case 0x0 ... 0x4:
        s->stub_reserved7 = val;
        break;
    }
    stub7_update(s);
}

static const MemoryRegionOps stub7_ops = {
    .read = stub7_read,
    .write = stub7_write,
    .endianness = DEVICE_BIG_ENDIAN,
};

static void stub8_update(void *opaque)
{
    /* AR71XXGENERICState *s = opaque; */
}

static uint64_t stub8_read(void *opaque, hwaddr offset, unsigned size)
{
    AR71XXGENERICState *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case 0x0 ... 0xfc:
        res = s->stub_reserved8;
        break;
    }
    return res;
}

static void stub8_write(void *opaque, hwaddr offset, uint64_t val, unsigned size)
{
    AR71XXGENERICState *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case 0x0 ... 0xfc:
        s->stub_reserved8 = val;
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
    /* AR71XXGENERICState *s = opaque; */
}

static uint64_t stub9_read(void *opaque, hwaddr offset, unsigned size)
{
    AR71XXGENERICState *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case 0x0 ... 0x1fc:
        res = s->stub_reserved9;
        break;
    }
    return res;
}

static void stub9_write(void *opaque, hwaddr offset, uint64_t val, unsigned size)
{
    AR71XXGENERICState *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case 0x0 ... 0x1fc:
        s->stub_reserved9 = val;
        break;
    }
    stub9_update(s);
}

static const MemoryRegionOps stub9_ops = {
    .read = stub9_read,
    .write = stub9_write,
    .endianness = DEVICE_BIG_ENDIAN,
};

static void ar71xx_generic_reset(void *opaque)
{
    AR71XXGENERICState *s = opaque;

    s->stub_reserved0 = 0x0;
    s->stub_reserved1 = 0x10000000;
    s->stub_reserved10 = 0x0;
    s->stub_reserved11 = 0x0;
    s->stub_reserved12 = 0x0;
    s->stub_reserved13 = 0x0;
    s->stub_reserved14 = 0x0;
    s->stub_reserved15 = 0xb0;
    s->stub_reserved16 = 0x0;
    s->stub_reserved2 = 0x0;
    s->stub_reserved3 = 0x10000000;
    s->stub_reserved4 = 0x0;
    s->stub_reserved5 = 0x10;
    s->stub_reserved6 = 0x0;
    s->stub_reserved7 = 0x0;
    s->stub_reserved8 = 0x0;
    s->stub_reserved9 = 0x0;
}

static void ar71xx_generic_init(MachineState *machine)
{
    AR71XXGENERICState *s = g_new0(AR71XXGENERICState, 1);
    Error *err = NULL;
    static struct mips_boot_info binfo;

    s->cpu = MIPS_CPU(object_new(machine->cpu_type));
    object_property_set_bool(OBJECT(s->cpu), true, "realized", &err);
    cpu_mips_irq_init_cpu(s->cpu);
    cpu_mips_clock_init(s->cpu);
    memory_region_allocate_system_memory(&s->ram, OBJECT(machine), "ram", machine->ram_size);
    memory_region_add_subregion_overlap(get_system_memory(), 0, &s->ram, 0);
    serial_mm_init(get_system_memory(), 0x18020000, 0x2, s->cpu->env.irq[0x6], 115200, serial_hd(0), DEVICE_BIG_ENDIAN);

    memory_region_init_io(&s->stub0_mmio, NULL, &stub0_ops, s, TYPE_AR71XX_GENERIC, 0x8);
    memory_region_add_subregion_overlap(get_system_memory(), 0x18060000, &s->stub0_mmio, 0);
    memory_region_init_io(&s->stub1_mmio, NULL, &stub1_ops, s, TYPE_AR71XX_GENERIC, 0x4);
    memory_region_add_subregion_overlap(get_system_memory(), 0x18060010, &s->stub1_mmio, 0);
    memory_region_init_io(&s->stub10_mmio, NULL, &stub10_ops, s, TYPE_AR71XX_GENERIC, 0x200);
    memory_region_add_subregion_overlap(get_system_memory(), 0x19000000, &s->stub10_mmio, 0);
    memory_region_init_io(&s->stub11_mmio, NULL, &stub11_ops, s, TYPE_AR71XX_GENERIC, 0x1000000);
    memory_region_add_subregion_overlap(get_system_memory(), 0x1f000000, &s->stub11_mmio, 0);
    memory_region_init_io(&s->stub12_mmio, NULL, &stub12_ops, s, TYPE_AR71XX_GENERIC, 0x100);
    memory_region_add_subregion_overlap(get_system_memory(), 0x18070000, &s->stub12_mmio, 0);
    memory_region_init_io(&s->stub13_mmio, NULL, &stub13_ops, s, TYPE_AR71XX_GENERIC, 0x30000);
    memory_region_add_subregion_overlap(get_system_memory(), 0x180c0000, &s->stub13_mmio, 0);
    memory_region_init_io(&s->stub14_mmio, NULL, &stub14_ops, s, TYPE_AR71XX_GENERIC, 0x20000);
    memory_region_add_subregion_overlap(get_system_memory(), 0x18100000, &s->stub14_mmio, 0);
    memory_region_init_io(&s->stub15_mmio, NULL, &stub15_ops, s, TYPE_AR71XX_GENERIC, 0x4);
    memory_region_add_subregion_overlap(get_system_memory(), 0x18060090, &s->stub15_mmio, 0);
    memory_region_init_io(&s->stub16_mmio, NULL, &stub16_ops, s, TYPE_AR71XX_GENERIC, 0x6c);
    memory_region_add_subregion_overlap(get_system_memory(), 0x18060094, &s->stub16_mmio, 0);
    memory_region_init_io(&s->stub2_mmio, NULL, &stub2_ops, s, TYPE_AR71XX_GENERIC, 0x78);
    memory_region_add_subregion_overlap(get_system_memory(), 0x18060018, &s->stub2_mmio, 0);
    memory_region_init_io(&s->stub3_mmio, NULL, &stub3_ops, s, TYPE_AR71XX_GENERIC, 0x4);
    memory_region_add_subregion_overlap(get_system_memory(), 0x18060014, &s->stub3_mmio, 0);
    memory_region_init_io(&s->stub4_mmio, NULL, &stub4_ops, s, TYPE_AR71XX_GENERIC, 0xfc);
    memory_region_add_subregion_overlap(get_system_memory(), 0x18050004, &s->stub4_mmio, 0);
    memory_region_init_io(&s->stub5_mmio, NULL, &stub5_ops, s, TYPE_AR71XX_GENERIC, 0x4);
    memory_region_add_subregion_overlap(get_system_memory(), 0x18050000, &s->stub5_mmio, 0);
    memory_region_init_io(&s->stub6_mmio, NULL, &stub6_ops, s, TYPE_AR71XX_GENERIC, 0x100);
    memory_region_add_subregion_overlap(get_system_memory(), 0x18000000, &s->stub6_mmio, 0);
    memory_region_init_io(&s->stub7_mmio, NULL, &stub7_ops, s, TYPE_AR71XX_GENERIC, 0x8);
    memory_region_add_subregion_overlap(get_system_memory(), 0x18060008, &s->stub7_mmio, 0);
    memory_region_init_io(&s->stub8_mmio, NULL, &stub8_ops, s, TYPE_AR71XX_GENERIC, 0x100);
    memory_region_add_subregion_overlap(get_system_memory(), 0x18040000, &s->stub8_mmio, 0);
    memory_region_init_io(&s->stub9_mmio, NULL, &stub9_ops, s, TYPE_AR71XX_GENERIC, 0x200);
    memory_region_add_subregion_overlap(get_system_memory(), 0x1a000000, &s->stub9_mmio, 0);

    ar71xx_generic_reset(s);

    binfo.ram_size = machine->ram_size;
    binfo.kernel_filename = machine->kernel_filename;
    binfo.kernel_cmdline = machine->kernel_cmdline;
    binfo.initrd_filename = machine->initrd_filename;
    mips_load_kernel(MIPS_CPU(first_cpu), &binfo);
}

static void ar71xx_generic_machine_init(MachineClass *mc)
{
    /* mc->family = ; */
    /* mc->name = "ar71xx_generic"; */
    /* mc->alias = ; */
    mc->desc = "ar71xx_generic";
    /* mc->deprecation_reason = ; */
    mc->init = ar71xx_generic_init;
    /* mc->reset = ; */
    /* mc->hot_add_cpu = ; */
    /* mc->kvm_type = ; */
    /* mc->block_default_type = ; */
    /* mc->units_per_default_bus = ; */
    /* mc->max_cpus = ; */
    /* mc->min_cpus = ; */
    /* mc->default_cpus = ; */
    /* mc->no_serial = 1; */
    /* mc->no_paralled = 1; */
    /* mc->no_floppy = 1; */
    /* mc->no_cdrom = 1; */
    /* mc->no_sdcard = 1; */
    /* mc->pci_allow_0_address = 1; */
    /* mc->legacy_fw_cfg_order = 1; */
    /* mc->is_default = ; */
    /* mc->default_machine_opts = ; */
    /* mc->default_boot_order = ; */
    /* mc->default_display = ; */
    /* mc->compat_props = ; */
    /* mc->hw_version = ; */
    mc->default_ram_size = 128 * MiB;
    mc->default_cpu_type = MIPS_CPU_TYPE_NAME("74Kf");
    /* mc->default_kernel_irqchip_split = ; */
    /* mc->option_rom_has_mr = ; */
    /* mc->minimum_page_bits = ; */
    /* mc->has_hotpluggable_cpus = ; */
    mc->ignore_memory_transaction_failures = false;
    /* mc->numa_mem_align_shift = ; */
    /* mc->valid_cpu_types = ; */
    /* mc->allowed_dynamic_sysbus_devices = ; */
    /* mc->auto_enable_numa_with_memhp = ; */
    /* mc->numa_auto_assign_ram = ; */
    /* mc->ignore_boot_device_suffixes = ; */
    /* mc->smbus_no_migration_support = ; */
    /* mc->nvdimm_supported = ; */
    /* mc->get_hotplug_handler = ; */
    /* mc->cpu_index_to_instance_props = ; */
    /* mc->CPuArchIdList = ; */
    /* mc->get_default_cpu_node_id = ; */
}

DEFINE_MACHINE("ar71xx_generic", ar71xx_generic_machine_init)