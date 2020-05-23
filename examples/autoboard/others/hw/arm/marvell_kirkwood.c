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
//#include "hw/intc/marvell_orion_intc.h"
//#include "hw/intc/marvell_orion_bridge_intc.h"
#include "hw/intc/autoboard_intc.h"
#include "hw/timer/marvell_orion_timer.h"
#include "hw/char/serial.h"
#include "hw/char/serial.h"

#define TYPE_MARVELL_KIRKWOOD "marvell_kirkwood"
#define MARVELL_KIRKWOOD(obj) \
    OBJECT_CHECK(MARVELL_KIRKWOODState, (obj), TYPE_MARVELL_KIRKWOOD)

typedef struct MARVELL_KIRKWOODState {
    ARMCPU *cpu;
    //MARVELL_ORION_INTCState marvell_orion_intc0;
    //MARVELL_ORION_INTCState marvell_orion_intc1;
    //MARVELL_ORION_BRIDGE_INTCState marvell_orion_bridge_intc0;
    AUTOBOARD_INTCState autoboard_intc0;
    AUTOBOARD_INTCState autoboard_bridge_intc0;
    MARVELL_ORION_TIMERState timer0;
    MemoryRegion stub0_mmio;
    uint32_t stub_reserved0[0x20 >> 2];
    MemoryRegion stub1_mmio;
    uint32_t stub_reserved1[0x20 >> 2];
    MemoryRegion stub2_mmio;
    uint32_t stub_reserved2[0x4 >> 2];
    MemoryRegion stub3_mmio;
    uint32_t stub_reserved3[0x4 >> 2];
    MemoryRegion stub4_mmio;
    uint32_t stub_reserved4[0x40 >> 2];
    MemoryRegion stub5_mmio;
    uint32_t stub_reserved5[0x40 >> 2];
    MemoryRegion stub6_mmio;
    uint32_t stub_reserved6[0x20 >> 2];
    MemoryRegion stub7_mmio;
    uint32_t stub_reserved7[0x28 >> 2];
    MemoryRegion stub8_mmio;
    uint32_t stub_reserved8[0x20 >> 2];
    MemoryRegion stub9_mmio;
    uint32_t stub_reserved9[0x20 >> 2];
    MemoryRegion stub13_mmio;
    uint32_t stub_reserved13[0x80 >> 2];
    MemoryRegion stub12_mmio;
    uint32_t stub_reserved12[0x88 >> 2];
    MemoryRegion stub14_mmio;
    uint32_t stub_reserved14[0x4 >> 2];
    MemoryRegion stub15_mmio;
    uint32_t stub_reserved15[0x4 >> 2];
    MemoryRegion stub17_mmio;
    uint32_t stub_reserved17[0x4 >> 2];
    MemoryRegion stub18_mmio;
    uint32_t stub_reserved18[0x4 >> 2];
    MemoryRegion stub19_mmio;
    uint32_t stub_reserved19[0x4 >> 2];
    MemoryRegion stub22_mmio;
    uint32_t stub_reserved22[0x8 >> 2];
    MemoryRegion stub24_mmio;
    uint32_t stub_reserved24[0x10000 >> 2];
    MemoryRegion stub25_mmio;
    uint32_t stub_reserved25[0x2000 >> 2];
    MemoryRegion stub26_mmio;
    uint32_t stub_reserved26[0x2000 >> 2];
    MemoryRegion stub27_mmio;
    uint32_t stub_reserved27[0x1000 >> 2];
    MemoryRegion stub28_mmio;
    uint32_t stub_reserved28[0x100 >> 2];
    MemoryRegion stub29_mmio;
    uint32_t stub_reserved29[0x100 >> 2];
    MemoryRegion stub30_mmio;
    uint32_t stub_reserved30[0x100 >> 2];
    MemoryRegion stub31_mmio;
    uint32_t stub_reserved31[0x100 >> 2];
    MemoryRegion stub32_mmio;
    uint32_t stub_reserved32[0x4000 >> 2];
    MemoryRegion stub33_mmio;
    uint32_t stub_reserved33[0x4000 >> 2];
    MemoryRegion stub34_mmio;
    uint32_t stub_reserved34[0x2000 >> 2];
    MemoryRegion stub35_mmio;
    uint32_t stub_reserved35[0x334 >> 2];
    MemoryRegion stub36_mmio;
    uint32_t stub_reserved36[0x1ccc >> 2];
    MemoryRegion stub37_mmio;
    uint32_t stub_reserved37[0x334 >> 2];
    MemoryRegion stub38_mmio;
    uint32_t stub_reserved38[0xccc >> 2];
    MemoryRegion stub39_mmio;
    uint32_t stub_reserved39[0x200 >> 2];
    MemoryRegion stub40_mmio;
    uint32_t stub_reserved40[0x2210 >> 2];
    MemoryRegion stub41_mmio;
    uint32_t stub_reserved41[0x100000 >> 2];
    MemoryRegion stub42_mmio;
    uint32_t stub_reserved42[0x400 >> 2];
    MemoryRegion stub43_mmio;
    uint32_t stub_reserved43[0x800 >> 2];
    MemoryRegion ram;
} MARVELL_KIRKWOODState;

static void stub0_update(void *opaque)
{
    /* MARVELL_KIRKWOODState *s = opaque; */
}

static uint64_t stub0_read(void *opaque, hwaddr offset, unsigned size)
{
    MARVELL_KIRKWOODState *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case 0x0 ... 0x1c:
        res = s->stub_reserved0[offset >> 2];
        break;
    }
    return res;
}

static void stub0_write(void *opaque, hwaddr offset, uint64_t val, unsigned size)
{
    MARVELL_KIRKWOODState *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case 0x0 ... 0x1c:
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

static void stub1_update(void *opaque)
{
    /* MARVELL_KIRKWOODState *s = opaque; */
}

static uint64_t stub1_read(void *opaque, hwaddr offset, unsigned size)
{
    MARVELL_KIRKWOODState *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case 0x0 ... 0x1c:
        res = s->stub_reserved1[offset >> 2];
        break;
    }
    return res;
}

static void stub1_write(void *opaque, hwaddr offset, uint64_t val, unsigned size)
{
    MARVELL_KIRKWOODState *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case 0x0 ... 0x1c:
        s->stub_reserved1[offset >> 2] = val;
        break;
    }
    stub1_update(s);
}

static const MemoryRegionOps stub1_ops = {
    .read = stub1_read,
    .write = stub1_write,
    .endianness = DEVICE_LITTLE_ENDIAN,
};

static void stub2_update(void *opaque)
{
    /* MARVELL_KIRKWOODState *s = opaque; */
}

static uint64_t stub2_read(void *opaque, hwaddr offset, unsigned size)
{
    MARVELL_KIRKWOODState *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case 0x0:
        res = s->stub_reserved2[offset >> 2];
        break;
    }
    return res;
}

static void stub2_write(void *opaque, hwaddr offset, uint64_t val, unsigned size)
{
    MARVELL_KIRKWOODState *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case 0x0:
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

static void stub3_update(void *opaque)
{
    /* MARVELL_KIRKWOODState *s = opaque; */
}

static uint64_t stub3_read(void *opaque, hwaddr offset, unsigned size)
{
    MARVELL_KIRKWOODState *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case 0x0:
        res = s->stub_reserved3[offset >> 2];
        break;
    }
    return res;
}

static void stub3_write(void *opaque, hwaddr offset, uint64_t val, unsigned size)
{
    MARVELL_KIRKWOODState *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case 0x0:
        s->stub_reserved3[offset >> 2] = val;
        break;
    }
    stub3_update(s);
}

static const MemoryRegionOps stub3_ops = {
    .read = stub3_read,
    .write = stub3_write,
    .endianness = DEVICE_LITTLE_ENDIAN,
};

static void stub4_update(void *opaque)
{
    /* MARVELL_KIRKWOODState *s = opaque; */
}

static uint64_t stub4_read(void *opaque, hwaddr offset, unsigned size)
{
    MARVELL_KIRKWOODState *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case 0x0 ... 0x3c:
        res = s->stub_reserved4[offset >> 2];
        break;
    }
    return res;
}

static void stub4_write(void *opaque, hwaddr offset, uint64_t val, unsigned size)
{
    MARVELL_KIRKWOODState *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case 0x0 ... 0x3c:
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
    /* MARVELL_KIRKWOODState *s = opaque; */
}

static uint64_t stub5_read(void *opaque, hwaddr offset, unsigned size)
{
    MARVELL_KIRKWOODState *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case 0x0 ... 0x3c:
        res = s->stub_reserved5[offset >> 2];
        break;
    }
    return res;
}

static void stub5_write(void *opaque, hwaddr offset, uint64_t val, unsigned size)
{
    MARVELL_KIRKWOODState *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case 0x0 ... 0x3c:
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
    /* MARVELL_KIRKWOODState *s = opaque; */
}

static uint64_t stub6_read(void *opaque, hwaddr offset, unsigned size)
{
    MARVELL_KIRKWOODState *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case 0x0 ... 0x1c:
        res = s->stub_reserved6[offset >> 2];
        break;
    }
    return res;
}

static void stub6_write(void *opaque, hwaddr offset, uint64_t val, unsigned size)
{
    MARVELL_KIRKWOODState *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case 0x0 ... 0x1c:
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

static void stub7_update(void *opaque)
{
    /* MARVELL_KIRKWOODState *s = opaque; */
}

static uint64_t stub7_read(void *opaque, hwaddr offset, unsigned size)
{
    MARVELL_KIRKWOODState *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case 0x0 ... 0x24:
        res = s->stub_reserved7[offset >> 2];
        break;
    }
    return res;
}

static void stub7_write(void *opaque, hwaddr offset, uint64_t val, unsigned size)
{
    MARVELL_KIRKWOODState *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case 0x0 ... 0x24:
        s->stub_reserved7[offset >> 2] = val;
        break;
    }
    stub7_update(s);
}

static const MemoryRegionOps stub7_ops = {
    .read = stub7_read,
    .write = stub7_write,
    .endianness = DEVICE_LITTLE_ENDIAN,
};

static void stub8_update(void *opaque)
{
    /* MARVELL_KIRKWOODState *s = opaque; */
}

static uint64_t stub8_read(void *opaque, hwaddr offset, unsigned size)
{
    MARVELL_KIRKWOODState *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case 0x0 ... 0x1c:
        res = s->stub_reserved8[offset >> 2];
        break;
    }
    return res;
}

static void stub8_write(void *opaque, hwaddr offset, uint64_t val, unsigned size)
{
    MARVELL_KIRKWOODState *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case 0x0 ... 0x1c:
        s->stub_reserved8[offset >> 2] = val;
        break;
    }
    stub8_update(s);
}

static const MemoryRegionOps stub8_ops = {
    .read = stub8_read,
    .write = stub8_write,
    .endianness = DEVICE_LITTLE_ENDIAN,
};

static void stub9_update(void *opaque)
{
    /* MARVELL_KIRKWOODState *s = opaque; */
}

static uint64_t stub9_read(void *opaque, hwaddr offset, unsigned size)
{
    MARVELL_KIRKWOODState *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case 0x0 ... 0x1c:
        res = s->stub_reserved9[offset >> 2];
        break;
    }
    return res;
}

static void stub9_write(void *opaque, hwaddr offset, uint64_t val, unsigned size)
{
    MARVELL_KIRKWOODState *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case 0x0 ... 0x1c:
        s->stub_reserved9[offset >> 2] = val;
        break;
    }
    stub9_update(s);
}

static const MemoryRegionOps stub9_ops = {
    .read = stub9_read,
    .write = stub9_write,
    .endianness = DEVICE_LITTLE_ENDIAN,
};

static void stub13_update(void *opaque)
{
    /* MARVELL_KIRKWOODState *s = opaque; */
}

static uint64_t stub13_read(void *opaque, hwaddr offset, unsigned size)
{
    MARVELL_KIRKWOODState *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case 0x0 ... 0x7c:
        res = s->stub_reserved13[offset >> 2];
        break;
    }
    return res;
}

static void stub13_write(void *opaque, hwaddr offset, uint64_t val, unsigned size)
{
    MARVELL_KIRKWOODState *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case 0x0 ... 0x7c:
        s->stub_reserved13[offset >> 2] = val;
        break;
    }
    stub13_update(s);
}

static const MemoryRegionOps stub13_ops = {
    .read = stub13_read,
    .write = stub13_write,
    .endianness = DEVICE_LITTLE_ENDIAN,
};

static void stub12_update(void *opaque)
{
    /* MARVELL_KIRKWOODState *s = opaque; */
}

static uint64_t stub12_read(void *opaque, hwaddr offset, unsigned size)
{
    MARVELL_KIRKWOODState *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case 0x0 ... 0x84:
        res = s->stub_reserved12[offset >> 2];
        break;
    }
    return res;
}

static void stub12_write(void *opaque, hwaddr offset, uint64_t val, unsigned size)
{
    MARVELL_KIRKWOODState *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case 0x0 ... 0x84:
        s->stub_reserved12[offset >> 2] = val;
        break;
    }
    stub12_update(s);
}

static const MemoryRegionOps stub12_ops = {
    .read = stub12_read,
    .write = stub12_write,
    .endianness = DEVICE_LITTLE_ENDIAN,
};

static void stub14_update(void *opaque)
{
    /* MARVELL_KIRKWOODState *s = opaque; */
}

static uint64_t stub14_read(void *opaque, hwaddr offset, unsigned size)
{
    MARVELL_KIRKWOODState *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case 0x0:
        res = s->stub_reserved14[offset >> 2];
        break;
    }
    return res;
}

static void stub14_write(void *opaque, hwaddr offset, uint64_t val, unsigned size)
{
    MARVELL_KIRKWOODState *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case 0x0:
        s->stub_reserved14[offset >> 2] = val;
        break;
    }
    stub14_update(s);
}

static const MemoryRegionOps stub14_ops = {
    .read = stub14_read,
    .write = stub14_write,
    .endianness = DEVICE_LITTLE_ENDIAN,
};

static void stub15_update(void *opaque)
{
    /* MARVELL_KIRKWOODState *s = opaque; */
}

static uint64_t stub15_read(void *opaque, hwaddr offset, unsigned size)
{
    MARVELL_KIRKWOODState *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case 0x0:
        res = s->stub_reserved15[offset >> 2];
        break;
    }
    return res;
}

static void stub15_write(void *opaque, hwaddr offset, uint64_t val, unsigned size)
{
    MARVELL_KIRKWOODState *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case 0x0:
        s->stub_reserved15[offset >> 2] = val;
        break;
    }
    stub15_update(s);
}

static const MemoryRegionOps stub15_ops = {
    .read = stub15_read,
    .write = stub15_write,
    .endianness = DEVICE_LITTLE_ENDIAN,
};

static void stub17_update(void *opaque)
{
    /* MARVELL_KIRKWOODState *s = opaque; */
}

static uint64_t stub17_read(void *opaque, hwaddr offset, unsigned size)
{
    MARVELL_KIRKWOODState *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case 0x0:
        res = s->stub_reserved17[offset >> 2];
        break;
    }
    return res;
}

static void stub17_write(void *opaque, hwaddr offset, uint64_t val, unsigned size)
{
    MARVELL_KIRKWOODState *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case 0x0:
        s->stub_reserved17[offset >> 2] = val;
        break;
    }
    stub17_update(s);
}

static const MemoryRegionOps stub17_ops = {
    .read = stub17_read,
    .write = stub17_write,
    .endianness = DEVICE_LITTLE_ENDIAN,
};

static void stub18_update(void *opaque)
{
    /* MARVELL_KIRKWOODState *s = opaque; */
}

static uint64_t stub18_read(void *opaque, hwaddr offset, unsigned size)
{
    MARVELL_KIRKWOODState *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case 0x0:
        res = s->stub_reserved18[offset >> 2];
        break;
    }
    return res;
}

static void stub18_write(void *opaque, hwaddr offset, uint64_t val, unsigned size)
{
    MARVELL_KIRKWOODState *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case 0x0:
        s->stub_reserved18[offset >> 2] = val;
        break;
    }
    stub18_update(s);
}

static const MemoryRegionOps stub18_ops = {
    .read = stub18_read,
    .write = stub18_write,
    .endianness = DEVICE_LITTLE_ENDIAN,
};

static void stub19_update(void *opaque)
{
    /* MARVELL_KIRKWOODState *s = opaque; */
}

static uint64_t stub19_read(void *opaque, hwaddr offset, unsigned size)
{
    MARVELL_KIRKWOODState *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case 0x0:
        res = s->stub_reserved19[offset >> 2];
        break;
    }
    return res;
}

static void stub19_write(void *opaque, hwaddr offset, uint64_t val, unsigned size)
{
    MARVELL_KIRKWOODState *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case 0x0:
        s->stub_reserved19[offset >> 2] = val;
        break;
    }
    stub19_update(s);
}

static const MemoryRegionOps stub19_ops = {
    .read = stub19_read,
    .write = stub19_write,
    .endianness = DEVICE_LITTLE_ENDIAN,
};

static void stub22_update(void *opaque)
{
    /* MARVELL_KIRKWOODState *s = opaque; */
}

static uint64_t stub22_read(void *opaque, hwaddr offset, unsigned size)
{
    MARVELL_KIRKWOODState *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case 0x0 ... 0x4:
        res = s->stub_reserved22[offset >> 2];
        break;
    }
    return res;
}

static void stub22_write(void *opaque, hwaddr offset, uint64_t val, unsigned size)
{
    MARVELL_KIRKWOODState *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case 0x0 ... 0x4:
        s->stub_reserved22[offset >> 2] = val;
        break;
    }
    stub22_update(s);
}

static const MemoryRegionOps stub22_ops = {
    .read = stub22_read,
    .write = stub22_write,
    .endianness = DEVICE_LITTLE_ENDIAN,
};

static void stub24_update(void *opaque)
{
    /* MARVELL_KIRKWOODState *s = opaque; */
}

static uint64_t stub24_read(void *opaque, hwaddr offset, unsigned size)
{
    MARVELL_KIRKWOODState *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case 0x0 ... 0xfffc:
        res = s->stub_reserved24[offset >> 2];
        break;
    }
    return res;
}

static void stub24_write(void *opaque, hwaddr offset, uint64_t val, unsigned size)
{
    MARVELL_KIRKWOODState *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case 0x0 ... 0xfffc:
        s->stub_reserved24[offset >> 2] = val;
        break;
    }
    stub24_update(s);
}

static const MemoryRegionOps stub24_ops = {
    .read = stub24_read,
    .write = stub24_write,
    .endianness = DEVICE_LITTLE_ENDIAN,
};

static void stub25_update(void *opaque)
{
    /* MARVELL_KIRKWOODState *s = opaque; */
}

static uint64_t stub25_read(void *opaque, hwaddr offset, unsigned size)
{
    MARVELL_KIRKWOODState *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case 0x0 ... 0x1ffc:
        res = s->stub_reserved25[offset >> 2];
        break;
    }
    return res;
}

static void stub25_write(void *opaque, hwaddr offset, uint64_t val, unsigned size)
{
    MARVELL_KIRKWOODState *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case 0x0 ... 0x1ffc:
        s->stub_reserved25[offset >> 2] = val;
        break;
    }
    stub25_update(s);
}

static const MemoryRegionOps stub25_ops = {
    .read = stub25_read,
    .write = stub25_write,
    .endianness = DEVICE_LITTLE_ENDIAN,
};

static void stub26_update(void *opaque)
{
    /* MARVELL_KIRKWOODState *s = opaque; */
}

static uint64_t stub26_read(void *opaque, hwaddr offset, unsigned size)
{
    MARVELL_KIRKWOODState *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case 0x0 ... 0x1ffc:
        res = s->stub_reserved26[offset >> 2];
        break;
    }
    return res;
}

static void stub26_write(void *opaque, hwaddr offset, uint64_t val, unsigned size)
{
    MARVELL_KIRKWOODState *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case 0x0 ... 0x1ffc:
        s->stub_reserved26[offset >> 2] = val;
        break;
    }
    stub26_update(s);
}

static const MemoryRegionOps stub26_ops = {
    .read = stub26_read,
    .write = stub26_write,
    .endianness = DEVICE_LITTLE_ENDIAN,
};

static void stub27_update(void *opaque)
{
    /* MARVELL_KIRKWOODState *s = opaque; */
}

static uint64_t stub27_read(void *opaque, hwaddr offset, unsigned size)
{
    MARVELL_KIRKWOODState *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case 0x0 ... 0xffc:
        res = s->stub_reserved27[offset >> 2];
        break;
    }
    return res;
}

static void stub27_write(void *opaque, hwaddr offset, uint64_t val, unsigned size)
{
    MARVELL_KIRKWOODState *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case 0x0 ... 0xffc:
        s->stub_reserved27[offset >> 2] = val;
        break;
    }
    stub27_update(s);
}

static const MemoryRegionOps stub27_ops = {
    .read = stub27_read,
    .write = stub27_write,
    .endianness = DEVICE_LITTLE_ENDIAN,
};

static void stub28_update(void *opaque)
{
    /* MARVELL_KIRKWOODState *s = opaque; */
}

static uint64_t stub28_read(void *opaque, hwaddr offset, unsigned size)
{
    MARVELL_KIRKWOODState *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case 0x0 ... 0xfc:
        res = s->stub_reserved28[offset >> 2];
        break;
    }
    return res;
}

static void stub28_write(void *opaque, hwaddr offset, uint64_t val, unsigned size)
{
    MARVELL_KIRKWOODState *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case 0x0 ... 0xfc:
        s->stub_reserved28[offset >> 2] = val;
        break;
    }
    stub28_update(s);
}

static const MemoryRegionOps stub28_ops = {
    .read = stub28_read,
    .write = stub28_write,
    .endianness = DEVICE_LITTLE_ENDIAN,
};

static void stub29_update(void *opaque)
{
    /* MARVELL_KIRKWOODState *s = opaque; */
}

static uint64_t stub29_read(void *opaque, hwaddr offset, unsigned size)
{
    MARVELL_KIRKWOODState *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case 0x0 ... 0xfc:
        res = s->stub_reserved29[offset >> 2];
        break;
    }
    return res;
}

static void stub29_write(void *opaque, hwaddr offset, uint64_t val, unsigned size)
{
    MARVELL_KIRKWOODState *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case 0x0 ... 0xfc:
        s->stub_reserved29[offset >> 2] = val;
        break;
    }
    stub29_update(s);
}

static const MemoryRegionOps stub29_ops = {
    .read = stub29_read,
    .write = stub29_write,
    .endianness = DEVICE_LITTLE_ENDIAN,
};

static void stub30_update(void *opaque)
{
    /* MARVELL_KIRKWOODState *s = opaque; */
}

static uint64_t stub30_read(void *opaque, hwaddr offset, unsigned size)
{
    MARVELL_KIRKWOODState *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case 0x0 ... 0xfc:
        res = s->stub_reserved30[offset >> 2];
        break;
    }
    return res;
}

static void stub30_write(void *opaque, hwaddr offset, uint64_t val, unsigned size)
{
    MARVELL_KIRKWOODState *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case 0x0 ... 0xfc:
        s->stub_reserved30[offset >> 2] = val;
        break;
    }
    stub30_update(s);
}

static const MemoryRegionOps stub30_ops = {
    .read = stub30_read,
    .write = stub30_write,
    .endianness = DEVICE_LITTLE_ENDIAN,
};

static void stub31_update(void *opaque)
{
    /* MARVELL_KIRKWOODState *s = opaque; */
}

static uint64_t stub31_read(void *opaque, hwaddr offset, unsigned size)
{
    MARVELL_KIRKWOODState *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case 0x0 ... 0xfc:
        res = s->stub_reserved31[offset >> 2];
        break;
    }
    return res;
}

static void stub31_write(void *opaque, hwaddr offset, uint64_t val, unsigned size)
{
    MARVELL_KIRKWOODState *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case 0x0 ... 0xfc:
        s->stub_reserved31[offset >> 2] = val;
        break;
    }
    stub31_update(s);
}

static const MemoryRegionOps stub31_ops = {
    .read = stub31_read,
    .write = stub31_write,
    .endianness = DEVICE_LITTLE_ENDIAN,
};

static void stub32_update(void *opaque)
{
    /* MARVELL_KIRKWOODState *s = opaque; */
}

static uint64_t stub32_read(void *opaque, hwaddr offset, unsigned size)
{
    MARVELL_KIRKWOODState *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case 0x0 ... 0x3ffc:
        res = s->stub_reserved32[offset >> 2];
        break;
    }
    return res;
}

static void stub32_write(void *opaque, hwaddr offset, uint64_t val, unsigned size)
{
    MARVELL_KIRKWOODState *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case 0x0 ... 0x3ffc:
        s->stub_reserved32[offset >> 2] = val;
        break;
    }
    stub32_update(s);
}

static const MemoryRegionOps stub32_ops = {
    .read = stub32_read,
    .write = stub32_write,
    .endianness = DEVICE_LITTLE_ENDIAN,
};

static void stub33_update(void *opaque)
{
    /* MARVELL_KIRKWOODState *s = opaque; */
}

static uint64_t stub33_read(void *opaque, hwaddr offset, unsigned size)
{
    MARVELL_KIRKWOODState *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case 0x0 ... 0x3ffc:
        res = s->stub_reserved33[offset >> 2];
        break;
    }
    return res;
}

static void stub33_write(void *opaque, hwaddr offset, uint64_t val, unsigned size)
{
    MARVELL_KIRKWOODState *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case 0x0 ... 0x3ffc:
        s->stub_reserved33[offset >> 2] = val;
        break;
    }
    stub33_update(s);
}

static const MemoryRegionOps stub33_ops = {
    .read = stub33_read,
    .write = stub33_write,
    .endianness = DEVICE_LITTLE_ENDIAN,
};

static void stub34_update(void *opaque)
{
    /* MARVELL_KIRKWOODState *s = opaque; */
}

static uint64_t stub34_read(void *opaque, hwaddr offset, unsigned size)
{
    MARVELL_KIRKWOODState *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case 0x0 ... 0x1ffc:
        res = s->stub_reserved34[offset >> 2];
        break;
    }
    return res;
}

static void stub34_write(void *opaque, hwaddr offset, uint64_t val, unsigned size)
{
    MARVELL_KIRKWOODState *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case 0x0 ... 0x1ffc:
        s->stub_reserved34[offset >> 2] = val;
        break;
    }
    stub34_update(s);
}

static const MemoryRegionOps stub34_ops = {
    .read = stub34_read,
    .write = stub34_write,
    .endianness = DEVICE_LITTLE_ENDIAN,
};

static void stub35_update(void *opaque)
{
    /* MARVELL_KIRKWOODState *s = opaque; */
}

static uint64_t stub35_read(void *opaque, hwaddr offset, unsigned size)
{
    MARVELL_KIRKWOODState *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case 0x0 ... 0x330:
        res = s->stub_reserved35[offset >> 2];
        break;
    }
    return res;
}

static void stub35_write(void *opaque, hwaddr offset, uint64_t val, unsigned size)
{
    MARVELL_KIRKWOODState *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case 0x0 ... 0x330:
        s->stub_reserved35[offset >> 2] = val;
        break;
    }
    stub35_update(s);
}

static const MemoryRegionOps stub35_ops = {
    .read = stub35_read,
    .write = stub35_write,
    .endianness = DEVICE_LITTLE_ENDIAN,
};

static void stub36_update(void *opaque)
{
    /* MARVELL_KIRKWOODState *s = opaque; */
}

static uint64_t stub36_read(void *opaque, hwaddr offset, unsigned size)
{
    MARVELL_KIRKWOODState *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case 0x0 ... 0x1cc8:
        res = s->stub_reserved36[offset >> 2];
        break;
    }
    return res;
}

static void stub36_write(void *opaque, hwaddr offset, uint64_t val, unsigned size)
{
    MARVELL_KIRKWOODState *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case 0x0 ... 0x1cc8:
        s->stub_reserved36[offset >> 2] = val;
        break;
    }
    stub36_update(s);
}

static const MemoryRegionOps stub36_ops = {
    .read = stub36_read,
    .write = stub36_write,
    .endianness = DEVICE_LITTLE_ENDIAN,
};

static void stub37_update(void *opaque)
{
    /* MARVELL_KIRKWOODState *s = opaque; */
}

static uint64_t stub37_read(void *opaque, hwaddr offset, unsigned size)
{
    MARVELL_KIRKWOODState *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case 0x0 ... 0x330:
        res = s->stub_reserved37[offset >> 2];
        break;
    }
    return res;
}

static void stub37_write(void *opaque, hwaddr offset, uint64_t val, unsigned size)
{
    MARVELL_KIRKWOODState *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case 0x0 ... 0x330:
        s->stub_reserved37[offset >> 2] = val;
        break;
    }
    stub37_update(s);
}

static const MemoryRegionOps stub37_ops = {
    .read = stub37_read,
    .write = stub37_write,
    .endianness = DEVICE_LITTLE_ENDIAN,
};

static void stub38_update(void *opaque)
{
    /* MARVELL_KIRKWOODState *s = opaque; */
}

static uint64_t stub38_read(void *opaque, hwaddr offset, unsigned size)
{
    MARVELL_KIRKWOODState *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case 0x0 ... 0xcc8:
        res = s->stub_reserved38[offset >> 2];
        break;
    }
    return res;
}

static void stub38_write(void *opaque, hwaddr offset, uint64_t val, unsigned size)
{
    MARVELL_KIRKWOODState *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case 0x0 ... 0xcc8:
        s->stub_reserved38[offset >> 2] = val;
        break;
    }
    stub38_update(s);
}

static const MemoryRegionOps stub38_ops = {
    .read = stub38_read,
    .write = stub38_write,
    .endianness = DEVICE_LITTLE_ENDIAN,
};

static void stub39_update(void *opaque)
{
    /* MARVELL_KIRKWOODState *s = opaque; */
}

static uint64_t stub39_read(void *opaque, hwaddr offset, unsigned size)
{
    MARVELL_KIRKWOODState *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case 0x0 ... 0x1fc:
        res = s->stub_reserved39[offset >> 2];
        break;
    }
    return res;
}

static void stub39_write(void *opaque, hwaddr offset, uint64_t val, unsigned size)
{
    MARVELL_KIRKWOODState *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case 0x0 ... 0x1fc:
        s->stub_reserved39[offset >> 2] = val;
        break;
    }
    stub39_update(s);
}

static const MemoryRegionOps stub39_ops = {
    .read = stub39_read,
    .write = stub39_write,
    .endianness = DEVICE_LITTLE_ENDIAN,
};

static void stub40_update(void *opaque)
{
    /* MARVELL_KIRKWOODState *s = opaque; */
}

static uint64_t stub40_read(void *opaque, hwaddr offset, unsigned size)
{
    MARVELL_KIRKWOODState *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case 0x0 ... 0x220c:
        res = s->stub_reserved40[offset >> 2];
        break;
    }
    return res;
}

static void stub40_write(void *opaque, hwaddr offset, uint64_t val, unsigned size)
{
    MARVELL_KIRKWOODState *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case 0x0 ... 0x220c:
        s->stub_reserved40[offset >> 2] = val;
        break;
    }
    stub40_update(s);
}

static const MemoryRegionOps stub40_ops = {
    .read = stub40_read,
    .write = stub40_write,
    .endianness = DEVICE_LITTLE_ENDIAN,
};

static void stub41_update(void *opaque)
{
    /* MARVELL_KIRKWOODState *s = opaque; */
}

static uint64_t stub41_read(void *opaque, hwaddr offset, unsigned size)
{
    MARVELL_KIRKWOODState *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case 0x0 ... 0xffffc:
        res = s->stub_reserved41[offset >> 2];
        break;
    }
    return res;
}

static void stub41_write(void *opaque, hwaddr offset, uint64_t val, unsigned size)
{
    MARVELL_KIRKWOODState *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case 0x0 ... 0xffffc:
        s->stub_reserved41[offset >> 2] = val;
        break;
    }
    stub41_update(s);
}

static const MemoryRegionOps stub41_ops = {
    .read = stub41_read,
    .write = stub41_write,
    .endianness = DEVICE_LITTLE_ENDIAN,
};

static void stub42_update(void *opaque)
{
    /* MARVELL_KIRKWOODState *s = opaque; */
}

static uint64_t stub42_read(void *opaque, hwaddr offset, unsigned size)
{
    MARVELL_KIRKWOODState *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case 0x0 ... 0x3fc:
        res = s->stub_reserved42[offset >> 2];
        break;
    }
    return res;
}

static void stub42_write(void *opaque, hwaddr offset, uint64_t val, unsigned size)
{
    MARVELL_KIRKWOODState *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case 0x0 ... 0x3fc:
        s->stub_reserved42[offset >> 2] = val;
        break;
    }
    stub42_update(s);
}

static const MemoryRegionOps stub42_ops = {
    .read = stub42_read,
    .write = stub42_write,
    .endianness = DEVICE_LITTLE_ENDIAN,
};

static void stub43_update(void *opaque)
{
    /* MARVELL_KIRKWOODState *s = opaque; */
}

static uint64_t stub43_read(void *opaque, hwaddr offset, unsigned size)
{
    MARVELL_KIRKWOODState *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case 0x0 ... 0x7fc:
        res = s->stub_reserved43[offset >> 2];
        break;
    }
    return res;
}

static void stub43_write(void *opaque, hwaddr offset, uint64_t val, unsigned size)
{
    MARVELL_KIRKWOODState *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case 0x0 ... 0x7fc:
        s->stub_reserved43[offset >> 2] = val;
        break;
    }
    stub43_update(s);
}

static const MemoryRegionOps stub43_ops = {
    .read = stub43_read,
    .write = stub43_write,
    .endianness = DEVICE_LITTLE_ENDIAN,
};

static void marvell_kirkwood_reset(void *opaque)
{
    MARVELL_KIRKWOODState *s = opaque;
    
    s->stub_reserved0[0] = 0x0;
    s->stub_reserved1[0] = 0x0;
    s->stub_reserved2[0] = 0x0;
    s->stub_reserved3[0] = 0x0;
    s->stub_reserved4[0] = 0x0;
    s->stub_reserved5[0] = 0x0;
    s->stub_reserved6[0] = 0x0;
    s->stub_reserved7[0] = 0x0;
    s->stub_reserved8[0] = 0x0;
    s->stub_reserved9[0] = 0x0;
    s->stub_reserved13[0] = 0x0;
    s->stub_reserved12[0] = 0x0;
    s->stub_reserved14[0] = 0x0;
    s->stub_reserved15[0] = 0x0;
    s->stub_reserved17[0] = 0x0;
    s->stub_reserved18[0] = 0x0;
    s->stub_reserved19[0] = 0x0;
    s->stub_reserved22[0] = 0x0;
    s->stub_reserved24[0] = 0x0;
    s->stub_reserved25[0] = 0x0;
    s->stub_reserved26[0] = 0x0;
    s->stub_reserved27[0] = 0x0;
    s->stub_reserved28[0] = 0x0;
    s->stub_reserved29[0] = 0x0;
    s->stub_reserved30[0] = 0x0;
    s->stub_reserved31[0] = 0x0;
    s->stub_reserved32[0] = 0x0;
    s->stub_reserved33[0] = 0x0;
    s->stub_reserved34[0] = 0x0;
    s->stub_reserved35[0] = 0x0;
    s->stub_reserved36[0] = 0x0;
    s->stub_reserved37[0] = 0x0;
    s->stub_reserved38[0] = 0x0;
    s->stub_reserved39[0] = 0x0;
    s->stub_reserved40[0] = 0x0;
    s->stub_reserved41[0] = 0x0;
    s->stub_reserved42[0] = 0x0;
    s->stub_reserved43[0] = 0x0;
}

static void marvell_kirkwood_init(MachineState *machine)
{
    MARVELL_KIRKWOODState *s = g_new0(MARVELL_KIRKWOODState, 1);
    Error *err = NULL;
    static struct arm_boot_info binfo;
    
    s->cpu = ARM_CPU(object_new(machine->cpu_type));
    object_property_set_bool(OBJECT(s->cpu), true, "realized", &err);

    memory_region_allocate_system_memory(&s->ram, OBJECT(machine), "ram", machine->ram_size);
    memory_region_add_subregion_overlap(get_system_memory(), 0, &s->ram, 0);
    
    //object_initialize(&s->marvell_orion_intc0, sizeof(s->marvell_orion_intc0), TYPE_MARVELL_ORION_INTC);
    //qdev_set_parent_bus(DEVICE(&s->marvell_orion_intc0), sysbus_get_default());
    //object_property_set_bool(OBJECT(&s->marvell_orion_intc0), true, "realized", &err);
    //sysbus_mmio_map(SYS_BUS_DEVICE(&s->marvell_orion_intc0), 0, 0xf1020200);
    //object_initialize(&s->marvell_orion_intc1, sizeof(s->marvell_orion_intc1), TYPE_MARVELL_ORION_INTC);
    //qdev_set_parent_bus(DEVICE(&s->marvell_orion_intc1), sysbus_get_default());
    //object_property_set_bool(OBJECT(&s->marvell_orion_intc1), true, "realized", &err);
    //sysbus_mmio_map(SYS_BUS_DEVICE(&s->marvell_orion_intc1), 0, 0xf1020210);
    //object_initialize(&s->marvell_orion_bridge_intc0, sizeof(s->marvell_orion_bridge_intc0), TYPE_MARVELL_ORION_BRIDGE_INTC);
    //qdev_set_parent_bus(DEVICE(&s->marvell_orion_bridge_intc0), sysbus_get_default());
    //object_property_set_bool(OBJECT(&s->marvell_orion_bridge_intc0), true, "realized", &err);
    //sysbus_mmio_map(SYS_BUS_DEVICE(&s->marvell_orion_bridge_intc0), 0, 0xf1020110);
    
    //qdev_connect_gpio_out(DEVICE(&s->marvell_orion_intc0), 0, qdev_get_gpio_in(DEVICE(s->cpu), ARM_CPU_IRQ));
    //qdev_connect_gpio_out(DEVICE(&s->marvell_orion_intc1), 0, qdev_get_gpio_in(DEVICE(s->cpu), ARM_CPU_IRQ));
    //qdev_connect_gpio_out(DEVICE(&s->marvell_orion_bridge_intc0), 0, qdev_get_gpio_in(DEVICE(&s->marvell_orion_intc0), 1));
    
    set_autoboard_intc_cfg(AUTOBOARD_INTC_KIRKWOOD_GENERIC_ORION, "orion-intc");
    object_initialize(&s->autoboard_intc0, sizeof(s->autoboard_intc0), TYPE_AUTOBOARD_INTC);
    qdev_set_parent_bus(DEVICE(&s->autoboard_intc0), sysbus_get_default());
    object_property_set_bool(OBJECT(&s->autoboard_intc0), true, "realized", &err);
    sysbus_mmio_map(SYS_BUS_DEVICE(&s->autoboard_intc0), 0, 0xf1020200);

    set_autoboard_intc_cfg(AUTOBOARD_INTC_KIRKWOOD_GENERIC_BRIDGE, "bridge-intc");
    object_initialize(&s->autoboard_bridge_intc0, sizeof(s->autoboard_bridge_intc0), TYPE_AUTOBOARD_INTC);
    qdev_set_parent_bus(DEVICE(&s->autoboard_bridge_intc0), sysbus_get_default());
    object_property_set_bool(OBJECT(&s->autoboard_bridge_intc0), true, "realized", &err);
    sysbus_mmio_map(SYS_BUS_DEVICE(&s->autoboard_bridge_intc0), 0, 0xf1020110);

    qdev_connect_gpio_out(DEVICE(&s->autoboard_intc0), 0, qdev_get_gpio_in(DEVICE(s->cpu), ARM_CPU_IRQ));
    qdev_connect_gpio_out(DEVICE(&s->autoboard_bridge_intc0), 0, qdev_get_gpio_in(DEVICE(&s->autoboard_intc0), 1));
    
    object_initialize(&s->timer0, sizeof(s->timer0), TYPE_MARVELL_ORION_TIMER);
    qdev_set_parent_bus(DEVICE(&s->timer0), sysbus_get_default());
    object_property_set_bool(OBJECT(&s->timer0), true, "realized", &err);
    sysbus_mmio_map(SYS_BUS_DEVICE(&s->timer0), 0, 0xf1020300);
    
    //qdev_connect_gpio_out(DEVICE(&s->timer0), 0, qdev_get_gpio_in(DEVICE(&s->marvell_orion_bridge_intc0), 1));
    //qdev_connect_gpio_out(DEVICE(&s->timer0), 1, qdev_get_gpio_in(DEVICE(&s->marvell_orion_bridge_intc0), 2));
    qdev_connect_gpio_out(DEVICE(&s->timer0), 0, qdev_get_gpio_in(DEVICE(&s->autoboard_bridge_intc0), 1));
    qdev_connect_gpio_out(DEVICE(&s->timer0), 1, qdev_get_gpio_in(DEVICE(&s->autoboard_bridge_intc0), 2));
    
    //serial_mm_init(get_system_memory(), 0xf1012100, 2, qdev_get_gpio_in(DEVICE(&s->marvell_orion_intc1), 2), 115200, serial_hd(0), DEVICE_LITTLE_ENDIAN);
    //serial_mm_init(get_system_memory(), 0xf1012000, 2, qdev_get_gpio_in(DEVICE(&s->marvell_orion_intc1), 1), 115200, serial_hd(1), DEVICE_LITTLE_ENDIAN);
    serial_mm_init(get_system_memory(), 0xf1012100, 2, qdev_get_gpio_in(DEVICE(&s->autoboard_intc0), 34), 115200, serial_hd(0), DEVICE_LITTLE_ENDIAN);
    serial_mm_init(get_system_memory(), 0xf1012000, 2, qdev_get_gpio_in(DEVICE(&s->autoboard_intc0), 33), 115200, serial_hd(1), DEVICE_LITTLE_ENDIAN);
    
    
    memory_region_init_io(&s->stub0_mmio, NULL, &stub0_ops, s, TYPE_MARVELL_KIRKWOOD, 0x20);
    memory_region_add_subregion_overlap(get_system_memory(), 0xf1001500, &s->stub0_mmio, 0);
    memory_region_init_io(&s->stub1_mmio, NULL, &stub1_ops, s, TYPE_MARVELL_KIRKWOOD, 0x20);
    memory_region_add_subregion_overlap(get_system_memory(), 0xf1010000, &s->stub1_mmio, 0);
    memory_region_init_io(&s->stub2_mmio, NULL, &stub2_ops, s, TYPE_MARVELL_KIRKWOOD, 0x4);
    memory_region_add_subregion_overlap(get_system_memory(), 0xf1010030, &s->stub2_mmio, 0);
    memory_region_init_io(&s->stub3_mmio, NULL, &stub3_ops, s, TYPE_MARVELL_KIRKWOOD, 0x4);
    memory_region_add_subregion_overlap(get_system_memory(), 0xf1010078, &s->stub3_mmio, 0);
    memory_region_init_io(&s->stub4_mmio, NULL, &stub4_ops, s, TYPE_MARVELL_KIRKWOOD, 0x40);
    memory_region_add_subregion_overlap(get_system_memory(), 0xf1010100, &s->stub4_mmio, 0);
    memory_region_init_io(&s->stub5_mmio, NULL, &stub5_ops, s, TYPE_MARVELL_KIRKWOOD, 0x40);
    memory_region_add_subregion_overlap(get_system_memory(), 0xf1010140, &s->stub5_mmio, 0);
    memory_region_init_io(&s->stub6_mmio, NULL, &stub6_ops, s, TYPE_MARVELL_KIRKWOOD, 0x20);
    memory_region_add_subregion_overlap(get_system_memory(), 0xf1010300, &s->stub6_mmio, 0);
    memory_region_init_io(&s->stub7_mmio, NULL, &stub7_ops, s, TYPE_MARVELL_KIRKWOOD, 0x28);
    memory_region_add_subregion_overlap(get_system_memory(), 0xf1010600, &s->stub7_mmio, 0);
    memory_region_init_io(&s->stub8_mmio, NULL, &stub8_ops, s, TYPE_MARVELL_KIRKWOOD, 0x20);
    memory_region_add_subregion_overlap(get_system_memory(), 0xf1011000, &s->stub8_mmio, 0);
    memory_region_init_io(&s->stub9_mmio, NULL, &stub9_ops, s, TYPE_MARVELL_KIRKWOOD, 0x20);
    memory_region_add_subregion_overlap(get_system_memory(), 0xf1011100, &s->stub9_mmio, 0);
    memory_region_init_io(&s->stub13_mmio, NULL, &stub13_ops, s, TYPE_MARVELL_KIRKWOOD, 0x80);
    memory_region_add_subregion_overlap(get_system_memory(), 0xf1020000, &s->stub13_mmio, 0);
    memory_region_init_io(&s->stub12_mmio, NULL, &stub12_ops, s, TYPE_MARVELL_KIRKWOOD, 0x88);
    memory_region_add_subregion_overlap(get_system_memory(), 0xf1020080, &s->stub12_mmio, 0);
    memory_region_init_io(&s->stub14_mmio, NULL, &stub14_ops, s, TYPE_MARVELL_KIRKWOOD, 0x4);
    memory_region_add_subregion_overlap(get_system_memory(), 0xf1020108, &s->stub14_mmio, 0);
    memory_region_init_io(&s->stub15_mmio, NULL, &stub15_ops, s, TYPE_MARVELL_KIRKWOOD, 0x4);
    memory_region_add_subregion_overlap(get_system_memory(), 0xf102010c, &s->stub15_mmio, 0);
    memory_region_init_io(&s->stub17_mmio, NULL, &stub17_ops, s, TYPE_MARVELL_KIRKWOOD, 0x4);
    memory_region_add_subregion_overlap(get_system_memory(), 0xf1020118, &s->stub17_mmio, 0);
    memory_region_init_io(&s->stub18_mmio, NULL, &stub18_ops, s, TYPE_MARVELL_KIRKWOOD, 0x4);
    memory_region_add_subregion_overlap(get_system_memory(), 0xf102011c, &s->stub18_mmio, 0);
    memory_region_init_io(&s->stub19_mmio, NULL, &stub19_ops, s, TYPE_MARVELL_KIRKWOOD, 0x4);
    memory_region_add_subregion_overlap(get_system_memory(), 0xf1020128, &s->stub19_mmio, 0);
    memory_region_init_io(&s->stub22_mmio, NULL, &stub22_ops, s, TYPE_MARVELL_KIRKWOOD, 0x8);
    memory_region_add_subregion_overlap(get_system_memory(), 0xf1020320, &s->stub22_mmio, 0);
    memory_region_init_io(&s->stub24_mmio, NULL, &stub24_ops, s, TYPE_MARVELL_KIRKWOOD, 0x10000);
    memory_region_add_subregion_overlap(get_system_memory(), 0xf1030000, &s->stub24_mmio, 0);
    memory_region_init_io(&s->stub25_mmio, NULL, &stub25_ops, s, TYPE_MARVELL_KIRKWOOD, 0x2000);
    memory_region_add_subregion_overlap(get_system_memory(), 0xf1040000, &s->stub25_mmio, 0);
    memory_region_init_io(&s->stub26_mmio, NULL, &stub26_ops, s, TYPE_MARVELL_KIRKWOOD, 0x2000);
    memory_region_add_subregion_overlap(get_system_memory(), 0xf1044000, &s->stub26_mmio, 0);
    memory_region_init_io(&s->stub27_mmio, NULL, &stub27_ops, s, TYPE_MARVELL_KIRKWOOD, 0x1000);
    memory_region_add_subregion_overlap(get_system_memory(), 0xf1050000, &s->stub27_mmio, 0);
    memory_region_init_io(&s->stub28_mmio, NULL, &stub28_ops, s, TYPE_MARVELL_KIRKWOOD, 0x100);
    memory_region_add_subregion_overlap(get_system_memory(), 0xf1060800, &s->stub28_mmio, 0);
    memory_region_init_io(&s->stub29_mmio, NULL, &stub29_ops, s, TYPE_MARVELL_KIRKWOOD, 0x100);
    memory_region_add_subregion_overlap(get_system_memory(), 0xf1060900, &s->stub29_mmio, 0);
    memory_region_init_io(&s->stub30_mmio, NULL, &stub30_ops, s, TYPE_MARVELL_KIRKWOOD, 0x100);
    memory_region_add_subregion_overlap(get_system_memory(), 0xf1060a00, &s->stub30_mmio, 0);
    memory_region_init_io(&s->stub31_mmio, NULL, &stub31_ops, s, TYPE_MARVELL_KIRKWOOD, 0x100);
    memory_region_add_subregion_overlap(get_system_memory(), 0xf1060b00, &s->stub31_mmio, 0);
    memory_region_init_io(&s->stub32_mmio, NULL, &stub32_ops, s, TYPE_MARVELL_KIRKWOOD, 0x4000);
    memory_region_add_subregion_overlap(get_system_memory(), 0xf1072000, &s->stub32_mmio, 0);
    memory_region_init_io(&s->stub33_mmio, NULL, &stub33_ops, s, TYPE_MARVELL_KIRKWOOD, 0x4000);
    memory_region_add_subregion_overlap(get_system_memory(), 0xf1076000, &s->stub33_mmio, 0);
    memory_region_init_io(&s->stub34_mmio, NULL, &stub34_ops, s, TYPE_MARVELL_KIRKWOOD, 0x2000);
    memory_region_add_subregion_overlap(get_system_memory(), 0xf1080000, &s->stub34_mmio, 0);
    memory_region_init_io(&s->stub35_mmio, NULL, &stub35_ops, s, TYPE_MARVELL_KIRKWOOD, 0x334);
    memory_region_add_subregion_overlap(get_system_memory(), 0xf1082000, &s->stub35_mmio, 0);
    memory_region_init_io(&s->stub36_mmio, NULL, &stub36_ops, s, TYPE_MARVELL_KIRKWOOD, 0x1ccc);
    memory_region_add_subregion_overlap(get_system_memory(), 0xf1082334, &s->stub36_mmio, 0);
    memory_region_init_io(&s->stub37_mmio, NULL, &stub37_ops, s, TYPE_MARVELL_KIRKWOOD, 0x334);
    memory_region_add_subregion_overlap(get_system_memory(), 0xf1084000, &s->stub37_mmio, 0);
    memory_region_init_io(&s->stub38_mmio, NULL, &stub38_ops, s, TYPE_MARVELL_KIRKWOOD, 0xccc);
    memory_region_add_subregion_overlap(get_system_memory(), 0xf1084334, &s->stub38_mmio, 0);
    memory_region_init_io(&s->stub39_mmio, NULL, &stub39_ops, s, TYPE_MARVELL_KIRKWOOD, 0x200);
    memory_region_add_subregion_overlap(get_system_memory(), 0xf1090000, &s->stub39_mmio, 0);
    memory_region_init_io(&s->stub40_mmio, NULL, &stub40_ops, s, TYPE_MARVELL_KIRKWOOD, 0x2210);
    memory_region_add_subregion_overlap(get_system_memory(), 0xf10a0000, &s->stub40_mmio, 0);
    memory_region_init_io(&s->stub41_mmio, NULL, &stub41_ops, s, TYPE_MARVELL_KIRKWOOD, 0x100000);
    memory_region_add_subregion_overlap(get_system_memory(), 0xf2000000, &s->stub41_mmio, 0);
    memory_region_init_io(&s->stub42_mmio, NULL, &stub42_ops, s, TYPE_MARVELL_KIRKWOOD, 0x400);
    memory_region_add_subregion_overlap(get_system_memory(), 0xf4000000, &s->stub42_mmio, 0);
    memory_region_init_io(&s->stub43_mmio, NULL, &stub43_ops, s, TYPE_MARVELL_KIRKWOOD, 0x800);
    memory_region_add_subregion_overlap(get_system_memory(), 0xf5000000, &s->stub43_mmio, 0);
    
    marvell_kirkwood_reset(s);

    binfo.board_id = 0xFFFFFFFF;
    binfo.ram_size = machine->ram_size;
    binfo.kernel_filename = machine->kernel_filename;
    binfo.kernel_cmdline = machine->kernel_cmdline;
    binfo.initrd_filename = machine->initrd_filename;
    arm_load_kernel(ARM_CPU(first_cpu), &binfo);
}

static void marvell_kirkwood_machine_init(MachineClass *mc)
{
    mc->desc = "marvell_kirkwood";
    mc->init = marvell_kirkwood_init;
    mc->default_ram_size = 0x8000000;
    mc->default_cpu_type = ARM_CPU_TYPE_NAME("feroceon");
    mc->ignore_memory_transaction_failures = false;
}

DEFINE_MACHINE("marvell_kirkwood", marvell_kirkwood_machine_init)

