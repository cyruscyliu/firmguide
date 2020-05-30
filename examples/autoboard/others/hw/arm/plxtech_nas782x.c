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
//#include "hw/cpu/arm11mpcore.h"
#include "hw/cpu/autoboard_arm11mpcore.h"
//#include "hw/timer/plxtech_nas782x_rps_timer.h"
#include "hw/timer/autoboard_timer.h"
#include "hw/char/serial.h"

#define TYPE_PLXTECH_NAS782X "plxtech_nas782x"
#define PLXTECH_NAS782X(obj) \
    OBJECT_CHECK(PLXTECH_NAS782XState, (obj), TYPE_PLXTECH_NAS782X)

typedef struct PLXTECH_NAS782XState {
    ARMCPU *cpu;
    //ARM11MPCorePriveState arm_arm11mp_gic;
    AUTOBOARDARM11MPCorePriveState autoboard_intc;
    //PLXTECH_NAS782X_RPS_TIMERState timer0;
    AUTOBOARD_TIMERState timer0;
    MemoryRegion stub0_mmio;
    uint32_t stub_reserved0[0xf00 >> 2];
    MemoryRegion stub1_mmio;
    uint32_t stub_reserved1[0x2000 >> 2];
    MemoryRegion stub30_mmio;
    uint32_t stub_reserved30[0x4 >> 2];
    MemoryRegion stub2_mmio;
    uint32_t stub_reserved2[0xffffc >> 2];
    MemoryRegion stub31_mmio;
    uint32_t stub_reserved31[0x4 >> 2];
    MemoryRegion stub3_mmio;
    uint32_t stub_reserved3[0x1c >> 2];
    MemoryRegion stub4_mmio;
    uint32_t stub_reserved4[0x100 >> 2];
    MemoryRegion stub5_mmio;
    uint32_t stub_reserved5[0x100 >> 2];
    MemoryRegion stub7_mmio;
    uint32_t stub_reserved7[0x14 >> 2];
    MemoryRegion stub9_mmio;
    uint32_t stub_reserved9[0xc >> 2];
    MemoryRegion stub10_mmio;
    uint32_t stub_reserved10[0x10 >> 2];
    MemoryRegion stub11_mmio;
    uint32_t stub_reserved11[0x34 >> 2];
    MemoryRegion stub12_mmio;
    uint32_t stub_reserved12[0x8 >> 2];
    MemoryRegion stub13_mmio;
    uint32_t stub_reserved13[0x1b4 >> 2];
    MemoryRegion stub32_mmio;
    uint32_t stub_reserved32[0x4 >> 2];
    MemoryRegion stub15_mmio;
    uint32_t stub_reserved15[0x1f0 >> 2];
    MemoryRegion stub16_mmio;
    uint32_t stub_reserved16[0x10 >> 2];
    MemoryRegion stub17_mmio;
    uint32_t stub_reserved17[0x20000 >> 2];
    MemoryRegion stub18_mmio;
    uint32_t stub_reserved18[0x40 >> 2];
    MemoryRegion stub19_mmio;
    uint32_t stub_reserved19[0x20 >> 2];
    MemoryRegion stub20_mmio;
    uint32_t stub_reserved20[0x2000 >> 2];
    MemoryRegion stub25_mmio;
    uint32_t stub_reserved25[0x1000 >> 2];
    MemoryRegion stub26_mmio;
    uint32_t stub_reserved26[0x100 >> 2];
    MemoryRegion stub27_mmio;
    uint32_t stub_reserved27[0x1000 >> 2];
    MemoryRegion stub28_mmio;
    uint32_t stub_reserved28[0x100 >> 2];
    MemoryRegion stub29_mmio;
    uint32_t stub_reserved29[0x1000 >> 2];
    MemoryRegion stub14_mmio;
    uint32_t stub_reserved14[0x8 >> 2];
    MemoryRegion stub33_mmio;
    uint32_t stub_reserved33[0x4 >> 2];
    MemoryRegion ram;
} PLXTECH_NAS782XState;

static void stub0_update(void *opaque)
{
    /* PLXTECH_NAS782XState *s = opaque; */
}

static uint64_t stub0_read(void *opaque, hwaddr offset, unsigned size)
{
    PLXTECH_NAS782XState *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case 0x0 ... 0xefc:
        res = s->stub_reserved0[offset >> 2];
        break;
    }
    return res;
}

static void stub0_write(void *opaque, hwaddr offset, uint64_t val, unsigned size)
{
    PLXTECH_NAS782XState *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case 0x0 ... 0xefc:
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
    /* PLXTECH_NAS782XState *s = opaque; */
}

static uint64_t stub1_read(void *opaque, hwaddr offset, unsigned size)
{
    PLXTECH_NAS782XState *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case 0x0 ... 0x1ffc:
        res = s->stub_reserved1[offset >> 2];
        break;
    }
    return res;
}

static void stub1_write(void *opaque, hwaddr offset, uint64_t val, unsigned size)
{
    PLXTECH_NAS782XState *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case 0x0 ... 0x1ffc:
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

static void stub30_update(void *opaque)
{
    /* PLXTECH_NAS782XState *s = opaque; */
}

static uint64_t stub30_read(void *opaque, hwaddr offset, unsigned size)
{
    PLXTECH_NAS782XState *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case 0x0:
        res = s->stub_reserved30[offset >> 2];
        break;
    }
    return res;
}

static void stub30_write(void *opaque, hwaddr offset, uint64_t val, unsigned size)
{
    PLXTECH_NAS782XState *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case 0x0:
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

static void stub2_update(void *opaque)
{
    /* PLXTECH_NAS782XState *s = opaque; */
}

static uint64_t stub2_read(void *opaque, hwaddr offset, unsigned size)
{
    PLXTECH_NAS782XState *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case 0x0 ... 0xffff8:
        res = s->stub_reserved2[offset >> 2];
        break;
    }
    return res;
}

static void stub2_write(void *opaque, hwaddr offset, uint64_t val, unsigned size)
{
    PLXTECH_NAS782XState *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case 0x0 ... 0xffff8:
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

static void stub31_update(void *opaque)
{
    /* PLXTECH_NAS782XState *s = opaque; */
}

static uint64_t stub31_read(void *opaque, hwaddr offset, unsigned size)
{
    PLXTECH_NAS782XState *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case 0x0:
        res = s->stub_reserved31[offset >> 2];
        break;
    }
    return res;
}

static void stub31_write(void *opaque, hwaddr offset, uint64_t val, unsigned size)
{
    PLXTECH_NAS782XState *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case 0x0:
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

static void stub3_update(void *opaque)
{
    /* PLXTECH_NAS782XState *s = opaque; */
}

static uint64_t stub3_read(void *opaque, hwaddr offset, unsigned size)
{
    PLXTECH_NAS782XState *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case 0x0 ... 0x18:
        res = s->stub_reserved3[offset >> 2];
        break;
    }
    return res;
}

static void stub3_write(void *opaque, hwaddr offset, uint64_t val, unsigned size)
{
    PLXTECH_NAS782XState *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case 0x0 ... 0x18:
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
    /* PLXTECH_NAS782XState *s = opaque; */
}

static uint64_t stub4_read(void *opaque, hwaddr offset, unsigned size)
{
    PLXTECH_NAS782XState *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case 0x0 ... 0xfc:
        res = s->stub_reserved4[offset >> 2];
        break;
    }
    return res;
}

static void stub4_write(void *opaque, hwaddr offset, uint64_t val, unsigned size)
{
    PLXTECH_NAS782XState *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case 0x0 ... 0xfc:
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
    /* PLXTECH_NAS782XState *s = opaque; */
}

static uint64_t stub5_read(void *opaque, hwaddr offset, unsigned size)
{
    PLXTECH_NAS782XState *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case 0x0 ... 0xfc:
        res = s->stub_reserved5[offset >> 2];
        break;
    }
    return res;
}

static void stub5_write(void *opaque, hwaddr offset, uint64_t val, unsigned size)
{
    PLXTECH_NAS782XState *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case 0x0 ... 0xfc:
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

static void stub7_update(void *opaque)
{
    /* PLXTECH_NAS782XState *s = opaque; */
}

static uint64_t stub7_read(void *opaque, hwaddr offset, unsigned size)
{
    PLXTECH_NAS782XState *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case 0x0 ... 0x10:
        res = s->stub_reserved7[offset >> 2];
        break;
    }
    return res;
}

static void stub7_write(void *opaque, hwaddr offset, uint64_t val, unsigned size)
{
    PLXTECH_NAS782XState *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case 0x0 ... 0x10:
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

static void stub9_update(void *opaque)
{
    /* PLXTECH_NAS782XState *s = opaque; */
}

static uint64_t stub9_read(void *opaque, hwaddr offset, unsigned size)
{
    PLXTECH_NAS782XState *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case 0x0 ... 0x8:
        res = s->stub_reserved9[offset >> 2];
        break;
    }
    return res;
}

static void stub9_write(void *opaque, hwaddr offset, uint64_t val, unsigned size)
{
    PLXTECH_NAS782XState *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case 0x0 ... 0x8:
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

static void stub10_update(void *opaque)
{
    /* PLXTECH_NAS782XState *s = opaque; */
}

static uint64_t stub10_read(void *opaque, hwaddr offset, unsigned size)
{
    PLXTECH_NAS782XState *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case 0x0 ... 0xc:
        res = s->stub_reserved10[offset >> 2];
        break;
    }
    return res;
}

static void stub10_write(void *opaque, hwaddr offset, uint64_t val, unsigned size)
{
    PLXTECH_NAS782XState *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case 0x0 ... 0xc:
        s->stub_reserved10[offset >> 2] = val;
        break;
    }
    stub10_update(s);
}

static const MemoryRegionOps stub10_ops = {
    .read = stub10_read,
    .write = stub10_write,
    .endianness = DEVICE_LITTLE_ENDIAN,
};

static void stub11_update(void *opaque)
{
    /* PLXTECH_NAS782XState *s = opaque; */
}

static uint64_t stub11_read(void *opaque, hwaddr offset, unsigned size)
{
    PLXTECH_NAS782XState *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case 0x0 ... 0x30:
        res = s->stub_reserved11[offset >> 2];
        break;
    }
    return res;
}

static void stub11_write(void *opaque, hwaddr offset, uint64_t val, unsigned size)
{
    PLXTECH_NAS782XState *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case 0x0 ... 0x30:
        s->stub_reserved11[offset >> 2] = val;
        break;
    }
    stub11_update(s);
}

static const MemoryRegionOps stub11_ops = {
    .read = stub11_read,
    .write = stub11_write,
    .endianness = DEVICE_LITTLE_ENDIAN,
};

static void stub12_update(void *opaque)
{
    /* PLXTECH_NAS782XState *s = opaque; */
}

static uint64_t stub12_read(void *opaque, hwaddr offset, unsigned size)
{
    PLXTECH_NAS782XState *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case 0x0 ... 0x4:
        res = s->stub_reserved12[offset >> 2];
        break;
    }
    return res;
}

static void stub12_write(void *opaque, hwaddr offset, uint64_t val, unsigned size)
{
    PLXTECH_NAS782XState *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case 0x0 ... 0x4:
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

static void stub13_update(void *opaque)
{
    /* PLXTECH_NAS782XState *s = opaque; */
}

static uint64_t stub13_read(void *opaque, hwaddr offset, unsigned size)
{
    PLXTECH_NAS782XState *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case 0x0 ... 0x1b0:
        res = s->stub_reserved13[offset >> 2];
        break;
    }
    return res;
}

static void stub13_write(void *opaque, hwaddr offset, uint64_t val, unsigned size)
{
    PLXTECH_NAS782XState *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case 0x0 ... 0x1b0:
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

static void stub32_update(void *opaque)
{
    /* PLXTECH_NAS782XState *s = opaque; */
}

static uint64_t stub32_read(void *opaque, hwaddr offset, unsigned size)
{
    PLXTECH_NAS782XState *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case 0x0:
        res = s->stub_reserved32[offset >> 2];
        break;
    }
    return res;
}

static void stub32_write(void *opaque, hwaddr offset, uint64_t val, unsigned size)
{
    PLXTECH_NAS782XState *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case 0x0:
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

static void stub15_update(void *opaque)
{
    /* PLXTECH_NAS782XState *s = opaque; */
}

static uint64_t stub15_read(void *opaque, hwaddr offset, unsigned size)
{
    PLXTECH_NAS782XState *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case 0x0 ... 0x1ec:
        res = s->stub_reserved15[offset >> 2];
        break;
    }
    return res;
}

static void stub15_write(void *opaque, hwaddr offset, uint64_t val, unsigned size)
{
    PLXTECH_NAS782XState *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case 0x0 ... 0x1ec:
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

static void stub16_update(void *opaque)
{
    /* PLXTECH_NAS782XState *s = opaque; */
}

static uint64_t stub16_read(void *opaque, hwaddr offset, unsigned size)
{
    PLXTECH_NAS782XState *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case 0x0 ... 0xc:
        res = s->stub_reserved16[offset >> 2];
        break;
    }
    return res;
}

static void stub16_write(void *opaque, hwaddr offset, uint64_t val, unsigned size)
{
    PLXTECH_NAS782XState *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case 0x0 ... 0xc:
        s->stub_reserved16[offset >> 2] = val;
        break;
    }
    stub16_update(s);
}

static const MemoryRegionOps stub16_ops = {
    .read = stub16_read,
    .write = stub16_write,
    .endianness = DEVICE_LITTLE_ENDIAN,
};

static void stub17_update(void *opaque)
{
    /* PLXTECH_NAS782XState *s = opaque; */
}

static uint64_t stub17_read(void *opaque, hwaddr offset, unsigned size)
{
    PLXTECH_NAS782XState *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case 0x0 ... 0x1fffc:
        res = s->stub_reserved17[offset >> 2];
        break;
    }
    return res;
}

static void stub17_write(void *opaque, hwaddr offset, uint64_t val, unsigned size)
{
    PLXTECH_NAS782XState *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case 0x0 ... 0x1fffc:
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
    /* PLXTECH_NAS782XState *s = opaque; */
}

static uint64_t stub18_read(void *opaque, hwaddr offset, unsigned size)
{
    PLXTECH_NAS782XState *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case 0x0 ... 0x3c:
        res = s->stub_reserved18[offset >> 2];
        break;
    }
    return res;
}

static void stub18_write(void *opaque, hwaddr offset, uint64_t val, unsigned size)
{
    PLXTECH_NAS782XState *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case 0x0 ... 0x3c:
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
    /* PLXTECH_NAS782XState *s = opaque; */
}

static uint64_t stub19_read(void *opaque, hwaddr offset, unsigned size)
{
    PLXTECH_NAS782XState *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case 0x0 ... 0x1c:
        res = s->stub_reserved19[offset >> 2];
        break;
    }
    return res;
}

static void stub19_write(void *opaque, hwaddr offset, uint64_t val, unsigned size)
{
    PLXTECH_NAS782XState *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case 0x0 ... 0x1c:
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

static void stub20_update(void *opaque)
{
    /* PLXTECH_NAS782XState *s = opaque; */
}

static uint64_t stub20_read(void *opaque, hwaddr offset, unsigned size)
{
    PLXTECH_NAS782XState *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case 0x0 ... 0x1ffc:
        res = s->stub_reserved20[offset >> 2];
        break;
    }
    return res;
}

static void stub20_write(void *opaque, hwaddr offset, uint64_t val, unsigned size)
{
    PLXTECH_NAS782XState *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case 0x0 ... 0x1ffc:
        s->stub_reserved20[offset >> 2] = val;
        break;
    }
    stub20_update(s);
}

static const MemoryRegionOps stub20_ops = {
    .read = stub20_read,
    .write = stub20_write,
    .endianness = DEVICE_LITTLE_ENDIAN,
};

static void stub25_update(void *opaque)
{
    /* PLXTECH_NAS782XState *s = opaque; */
}

static uint64_t stub25_read(void *opaque, hwaddr offset, unsigned size)
{
    PLXTECH_NAS782XState *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case 0x0 ... 0xffc:
        res = s->stub_reserved25[offset >> 2];
        break;
    }
    return res;
}

static void stub25_write(void *opaque, hwaddr offset, uint64_t val, unsigned size)
{
    PLXTECH_NAS782XState *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case 0x0 ... 0xffc:
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
    /* PLXTECH_NAS782XState *s = opaque; */
}

static uint64_t stub26_read(void *opaque, hwaddr offset, unsigned size)
{
    PLXTECH_NAS782XState *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case 0x0 ... 0xfc:
        res = s->stub_reserved26[offset >> 2];
        break;
    }
    return res;
}

static void stub26_write(void *opaque, hwaddr offset, uint64_t val, unsigned size)
{
    PLXTECH_NAS782XState *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case 0x0 ... 0xfc:
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
    /* PLXTECH_NAS782XState *s = opaque; */
}

static uint64_t stub27_read(void *opaque, hwaddr offset, unsigned size)
{
    PLXTECH_NAS782XState *s = opaque;
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
    PLXTECH_NAS782XState *s = opaque;

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
    /* PLXTECH_NAS782XState *s = opaque; */
}

static uint64_t stub28_read(void *opaque, hwaddr offset, unsigned size)
{
    PLXTECH_NAS782XState *s = opaque;
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
    PLXTECH_NAS782XState *s = opaque;

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
    /* PLXTECH_NAS782XState *s = opaque; */
}

static uint64_t stub29_read(void *opaque, hwaddr offset, unsigned size)
{
    PLXTECH_NAS782XState *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case 0x0 ... 0xffc:
        res = s->stub_reserved29[offset >> 2];
        break;
    }
    return res;
}

static void stub29_write(void *opaque, hwaddr offset, uint64_t val, unsigned size)
{
    PLXTECH_NAS782XState *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case 0x0 ... 0xffc:
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

static void stub14_update(void *opaque)
{
    /* PLXTECH_NAS782XState *s = opaque; */
}

static uint64_t stub14_read(void *opaque, hwaddr offset, unsigned size)
{
    PLXTECH_NAS782XState *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case 0x0 ... 0x4:
        res = s->stub_reserved14[offset >> 2];
        break;
    }
    return res;
}

static void stub14_write(void *opaque, hwaddr offset, uint64_t val, unsigned size)
{
    PLXTECH_NAS782XState *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case 0x0 ... 0x4:
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

static void stub33_update(void *opaque)
{
    /* PLXTECH_NAS782XState *s = opaque; */
}

static uint64_t stub33_read(void *opaque, hwaddr offset, unsigned size)
{
    PLXTECH_NAS782XState *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case 0x0:
        res = s->stub_reserved33[offset >> 2];
        break;
    }
    return res;
}

static void stub33_write(void *opaque, hwaddr offset, uint64_t val, unsigned size)
{
    PLXTECH_NAS782XState *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case 0x0:
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

static void plxtech_nas782x_reset(void *opaque)
{
    PLXTECH_NAS782XState *s = opaque;
    
    s->stub_reserved0[0] = 0x0;
    s->stub_reserved1[0] = 0x0;
    s->stub_reserved30[0] = 0x40;
    s->stub_reserved2[0] = 0x0;
    s->stub_reserved31[0] = 0x40;
    s->stub_reserved3[0] = 0x0;
    s->stub_reserved4[0] = 0x0;
    s->stub_reserved5[0] = 0x0;
    s->stub_reserved7[0] = 0x0;
    s->stub_reserved9[0] = 0x0;
    s->stub_reserved10[0] = 0x0;
    s->stub_reserved11[0] = 0x0;
    s->stub_reserved12[0] = 0x0;
    s->stub_reserved13[0] = 0x0;
    s->stub_reserved32[0] = 0x00000200;
    //s->stub_reserved32[0] = 0x0;
    //s->stub_reserved32[0] = 0x8000;
    s->stub_reserved15[0] = 0x0;
    s->stub_reserved16[0] = 0x0;
    s->stub_reserved17[0] = 0x0;
    s->stub_reserved18[0] = 0x0;
    s->stub_reserved19[0] = 0x0;
    s->stub_reserved20[0] = 0x0;
    s->stub_reserved25[0] = 0x0;
    s->stub_reserved26[0] = 0x0;
    s->stub_reserved27[0] = 0x0;
    s->stub_reserved28[0] = 0x0;
    s->stub_reserved29[0] = 0x0;
    s->stub_reserved14[0] = 0x0;
    s->stub_reserved33[0] = 0x2ccb8000;
    //s->stub_reserved33[0] = 0x0;
    //s->stub_reserved33[0] = 0x8000;
}

static void plxtech_nas782x_init(MachineState *machine)
{
    PLXTECH_NAS782XState *s = g_new0(PLXTECH_NAS782XState, 1);
    Error *err = NULL;
    static struct arm_boot_info binfo;
    
    s->cpu = ARM_CPU(object_new(machine->cpu_type));
    object_property_set_bool(OBJECT(s->cpu), true, "realized", &err);

    memory_region_allocate_system_memory(&s->ram, OBJECT(machine), "ram", machine->ram_size);
    memory_region_add_subregion_overlap(get_system_memory(), 0, &s->ram, 0);
    
    
    //object_initialize(&s->arm_arm11mp_gic, sizeof(s->arm_arm11mp_gic), TYPE_ARM11MPCORE_PRIV);
    //object_property_set_bool(OBJECT(&s->arm_arm11mp_gic), true, "realized", &err);
    //sysbus_mmio_map(SYS_BUS_DEVICE(&s->arm_arm11mp_gic), 0, 0x47001000 & 0xffff0000);
    
    //sysbus_connect_irq(SYS_BUS_DEVICE(&s->arm_arm11mp_gic), 0, qdev_get_gpio_in(DEVICE(s->cpu), ARM_CPU_IRQ));

    object_initialize(&s->autoboard_intc, sizeof(s->autoboard_intc), TYPE_AUTOBOARDARM11MPCORE_PRIV);
    object_property_set_bool(OBJECT(&s->autoboard_intc), true, "realized", &err);
    sysbus_mmio_map(SYS_BUS_DEVICE(&s->autoboard_intc), 0, 0x47001000 & 0xffff0000);
    
    sysbus_connect_irq(SYS_BUS_DEVICE(&s->autoboard_intc), 0, qdev_get_gpio_in(DEVICE(s->cpu), ARM_CPU_IRQ));
    
    set_autoboard_timer_cfg(AUTOBOARD_TIMER_OXNAS_GENERIC_RPS, "clksrc-rps");
    object_initialize(&s->timer0, sizeof(s->timer0), TYPE_AUTOBOARD_TIMER);
    qdev_set_parent_bus(DEVICE(&s->timer0), sysbus_get_default());
    object_property_set_bool(OBJECT(&s->timer0), true, "realized", &err);
    sysbus_mmio_map(SYS_BUS_DEVICE(&s->timer0), 0, 0x44400200);
    
    //serial_mm_init(get_system_memory(), 0x44200000, 0, qdev_get_gpio_in(DEVICE(&s->arm_arm11mp_gic), 23), 115200, serial_hd(0), DEVICE_LITTLE_ENDIAN);

    serial_mm_init(get_system_memory(), 0x44200000, 0, qdev_get_gpio_in(DEVICE(&s->autoboard_intc), 55), 115200, serial_hd(0), DEVICE_LITTLE_ENDIAN);
    
    
    memory_region_init_io(&s->stub0_mmio, NULL, &stub0_ops, s, TYPE_PLXTECH_NAS782X, 0xf00);
    memory_region_add_subregion_overlap(get_system_memory(), 0x40200100, &s->stub0_mmio, 0);
    memory_region_init_io(&s->stub1_mmio, NULL, &stub1_ops, s, TYPE_PLXTECH_NAS782X, 0x2000);
    memory_region_add_subregion_overlap(get_system_memory(), 0x40400000, &s->stub1_mmio, 0);
    memory_region_init_io(&s->stub30_mmio, NULL, &stub30_ops, s, TYPE_PLXTECH_NAS782X, 0x4);
    memory_region_add_subregion_overlap(get_system_memory(), 0x41000000, &s->stub30_mmio, 0);
    memory_region_init_io(&s->stub2_mmio, NULL, &stub2_ops, s, TYPE_PLXTECH_NAS782X, 0xffffc);
    memory_region_add_subregion_overlap(get_system_memory(), 0x41000004, &s->stub2_mmio, 0);
    memory_region_init_io(&s->stub31_mmio, NULL, &stub31_ops, s, TYPE_PLXTECH_NAS782X, 0x4);
    memory_region_add_subregion_overlap(get_system_memory(), 0x41c00000, &s->stub31_mmio, 0);
    memory_region_init_io(&s->stub3_mmio, NULL, &stub3_ops, s, TYPE_PLXTECH_NAS782X, 0x1c);
    memory_region_add_subregion_overlap(get_system_memory(), 0x41c00004, &s->stub3_mmio, 0);
    memory_region_init_io(&s->stub4_mmio, NULL, &stub4_ops, s, TYPE_PLXTECH_NAS782X, 0x100);
    memory_region_add_subregion_overlap(get_system_memory(), 0x44000000, &s->stub4_mmio, 0);
    memory_region_init_io(&s->stub5_mmio, NULL, &stub5_ops, s, TYPE_PLXTECH_NAS782X, 0x100);
    memory_region_add_subregion_overlap(get_system_memory(), 0x44100000, &s->stub5_mmio, 0);
    memory_region_init_io(&s->stub7_mmio, NULL, &stub7_ops, s, TYPE_PLXTECH_NAS782X, 0x14);
    memory_region_add_subregion_overlap(get_system_memory(), 0x44400000, &s->stub7_mmio, 0);
    memory_region_init_io(&s->stub9_mmio, NULL, &stub9_ops, s, TYPE_PLXTECH_NAS782X, 0xc);
    memory_region_add_subregion_overlap(get_system_memory(), 0x44900000, &s->stub9_mmio, 0);
    memory_region_init_io(&s->stub10_mmio, NULL, &stub10_ops, s, TYPE_PLXTECH_NAS782X, 0x10);
    memory_region_add_subregion_overlap(get_system_memory(), 0x44a00000, &s->stub10_mmio, 0);
    memory_region_init_io(&s->stub11_mmio, NULL, &stub11_ops, s, TYPE_PLXTECH_NAS782X, 0x34);
    memory_region_add_subregion_overlap(get_system_memory(), 0x44e00000, &s->stub11_mmio, 0);
    memory_region_init_io(&s->stub12_mmio, NULL, &stub12_ops, s, TYPE_PLXTECH_NAS782X, 0x8);
    memory_region_add_subregion_overlap(get_system_memory(), 0x44e00034, &s->stub12_mmio, 0);
    memory_region_init_io(&s->stub13_mmio, NULL, &stub13_ops, s, TYPE_PLXTECH_NAS782X, 0x1b4);
    memory_region_add_subregion_overlap(get_system_memory(), 0x44e0003c, &s->stub13_mmio, 0);
    memory_region_init_io(&s->stub32_mmio, NULL, &stub32_ops, s, TYPE_PLXTECH_NAS782X, 0x4);
    memory_region_add_subregion_overlap(get_system_memory(), 0x44e001f0, &s->stub32_mmio, 0);
    memory_region_init_io(&s->stub15_mmio, NULL, &stub15_ops, s, TYPE_PLXTECH_NAS782X, 0x1f0);
    memory_region_add_subregion_overlap(get_system_memory(), 0x44f00000, &s->stub15_mmio, 0);
    memory_region_init_io(&s->stub16_mmio, NULL, &stub16_ops, s, TYPE_PLXTECH_NAS782X, 0x10);
    memory_region_add_subregion_overlap(get_system_memory(), 0x44f001f0, &s->stub16_mmio, 0);
    memory_region_init_io(&s->stub17_mmio, NULL, &stub17_ops, s, TYPE_PLXTECH_NAS782X, 0x20000);
    memory_region_add_subregion_overlap(get_system_memory(), 0x45900000, &s->stub17_mmio, 0);
    memory_region_init_io(&s->stub18_mmio, NULL, &stub18_ops, s, TYPE_PLXTECH_NAS782X, 0x40);
    memory_region_add_subregion_overlap(get_system_memory(), 0x459a0000, &s->stub18_mmio, 0);
    memory_region_init_io(&s->stub19_mmio, NULL, &stub19_ops, s, TYPE_PLXTECH_NAS782X, 0x20);
    memory_region_add_subregion_overlap(get_system_memory(), 0x459b0000, &s->stub19_mmio, 0);
    memory_region_init_io(&s->stub20_mmio, NULL, &stub20_ops, s, TYPE_PLXTECH_NAS782X, 0x2000);
    memory_region_add_subregion_overlap(get_system_memory(), 0x459e0000, &s->stub20_mmio, 0);
    memory_region_init_io(&s->stub25_mmio, NULL, &stub25_ops, s, TYPE_PLXTECH_NAS782X, 0x1000);
    memory_region_add_subregion_overlap(get_system_memory(), 0x47c00000, &s->stub25_mmio, 0);
    memory_region_init_io(&s->stub26_mmio, NULL, &stub26_ops, s, TYPE_PLXTECH_NAS782X, 0x100);
    memory_region_add_subregion_overlap(get_system_memory(), 0x47d00000, &s->stub26_mmio, 0);
    memory_region_init_io(&s->stub27_mmio, NULL, &stub27_ops, s, TYPE_PLXTECH_NAS782X, 0x1000);
    memory_region_add_subregion_overlap(get_system_memory(), 0x47e00000, &s->stub27_mmio, 0);
    memory_region_init_io(&s->stub28_mmio, NULL, &stub28_ops, s, TYPE_PLXTECH_NAS782X, 0x100);
    memory_region_add_subregion_overlap(get_system_memory(), 0x47f00000, &s->stub28_mmio, 0);
    memory_region_init_io(&s->stub29_mmio, NULL, &stub29_ops, s, TYPE_PLXTECH_NAS782X, 0x1000);
    memory_region_add_subregion_overlap(get_system_memory(), 0x50000000, &s->stub29_mmio, 0);
    memory_region_init_io(&s->stub14_mmio, NULL, &stub14_ops, s, TYPE_PLXTECH_NAS782X, 0x8);
    memory_region_add_subregion_overlap(get_system_memory(), 0x44e001f8, &s->stub14_mmio, 0);
    memory_region_init_io(&s->stub33_mmio, NULL, &stub33_ops, s, TYPE_PLXTECH_NAS782X, 0x4);
    memory_region_add_subregion_overlap(get_system_memory(), 0x44e001f4, &s->stub33_mmio, 0);
    
    plxtech_nas782x_reset(s);

    binfo.board_id = 0xFFFFFFFF;
    binfo.ram_size = machine->ram_size;
    binfo.kernel_filename = machine->kernel_filename;
    binfo.kernel_cmdline = machine->kernel_cmdline;
    binfo.initrd_filename = machine->initrd_filename;
    arm_load_kernel(ARM_CPU(first_cpu), &binfo);
}

static void plxtech_nas782x_machine_init(MachineClass *mc)
{
    mc->desc = "plxtech_nas782x";
    mc->init = plxtech_nas782x_init;
    mc->default_ram_size = 256 * MiB;
    mc->default_cpu_type = ARM_CPU_TYPE_NAME("arm11mpcore");
    mc->ignore_memory_transaction_failures = false;
}

DEFINE_MACHINE("plxtech_nas782x", plxtech_nas782x_machine_init)

