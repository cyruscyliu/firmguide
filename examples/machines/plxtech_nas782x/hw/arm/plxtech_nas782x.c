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
#include "hw/cpu/arm11mpcore.h"
#include "hw/timer/plxtech_nas782x_rps_timer.h"
#include "hw/char/serial.h"

#define TYPE_PLXTECH_NAS782X "plxtech_nas782x"
#define PLXTECH_NAS782X(obj) \
    OBJECT_CHECK(PLXTECH_NAS782XState, (obj), TYPE_PLXTECH_NAS782X)

typedef struct PLXTECH_NAS782XState {
    ARMCPU *cpu;
    ARM11MPCorePriveState arm_arm11mp_gic;
    PLXTECH_NAS782X_RPS_TIMERState timer0;
    MemoryRegion ram0;
    MemoryRegion plxtech_nand_nas782x0_mmio;
    MemoryRegion plxtech_nand_nas782x1_mmio;
    MemoryRegion plxtech_nas782x_ehci0_mmio;
    MemoryRegion snps_dwmac0_mmio;
    MemoryRegion plxtech_nas782x_sata0_mmio;
    MemoryRegion plxtech_nas782x_sata1_mmio;
    MemoryRegion plxtech_nas782x_sata2_mmio;
    MemoryRegion plxtech_nas782x_sata3_mmio;
    MemoryRegion plxtech_nas782x_sata4_mmio;
    MemoryRegion plxtech_nas782x_sata5_mmio;
    MemoryRegion plxtech_nas782x_pcie0_mmio;
    MemoryRegion plxtech_nas782x_pcie1_mmio;
    MemoryRegion plxtech_nas782x_pcie2_mmio;
    MemoryRegion plxtech_nas782x_pcie3_mmio;
    MemoryRegion plxtech_nas782x_pcie4_mmio;
    MemoryRegion plxtech_nas782x_gpio0_mmio;
    MemoryRegion plxtech_nas782x_gpio1_mmio;
    MemoryRegion plxtech_nas782x_gpio2_mmio;
    MemoryRegion plxtech_nas782x_gpio3_mmio;
    MemoryRegion plxtech_nas782x_pllb0_mmio;
    MemoryRegion plxtech_nas782x_plla0_mmio;
    MemoryRegion plxtech_nas782x_reset0_mmio;
    uint32_t plxtech_nand_nas782x0_reserved[0x100000 >> 2];
    uint32_t plxtech_nand_nas782x1_reserved[0x20 >> 2];
    uint32_t plxtech_nas782x_ehci0_reserved[0xf00 >> 2];
    uint32_t snps_dwmac0_reserved[0x2000 >> 2];
    uint32_t plxtech_nas782x_sata0_reserved[0x20000 >> 2];
    uint32_t plxtech_nas782x_sata1_reserved[0x40 >> 2];
    uint32_t plxtech_nas782x_sata2_reserved[0x20 >> 2];
    uint32_t plxtech_nas782x_sata3_reserved[0x2000 >> 2];
    uint32_t plxtech_nas782x_sata4_reserved[0xc >> 2];
    uint32_t plxtech_nas782x_sata5_reserved[0x1000 >> 2];
    uint32_t plxtech_nas782x_pcie0_reserved[0x10 >> 2];
    uint32_t plxtech_nas782x_pcie1_reserved[0x1000 >> 2];
    uint32_t plxtech_nas782x_pcie2_reserved[0x100 >> 2];
    uint32_t plxtech_nas782x_pcie3_reserved[0x1000 >> 2];
    uint32_t plxtech_nas782x_pcie4_reserved[0x100 >> 2];
    uint32_t plxtech_nas782x_gpio0_reserved[0x100 >> 2];
    uint32_t plxtech_nas782x_gpio1_reserved[0x100 >> 2];
    uint32_t plxtech_nas782x_gpio2_reserved[0x200 >> 2];
    uint32_t plxtech_nas782x_gpio3_reserved[0x200 >> 2];
    uint32_t plxtech_nas782x_pllb0_reserved[0x10 >> 2];
    uint32_t plxtech_nas782x_plla0_reserved[0x10 >> 2];
    uint32_t plxtech_nas782x_reset0_reserved[0x8 >> 2];
} PLXTECH_NAS782XState;

static void plxtech_nand_nas782x0_update(void *opaque)
{
    /* PLXTECH_NAS782XState *s = opaque; */
}

static uint64_t plxtech_nand_nas782x0_read(void *opaque, hwaddr offset, unsigned size)
{
    PLXTECH_NAS782XState *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case 0x0 ... 0xffffc:
        res = s->plxtech_nand_nas782x0_reserved[offset >> 2];
        break;
    }
    return res;
}

static void plxtech_nand_nas782x0_write(void *opaque, hwaddr offset, uint64_t val, unsigned size)
{
    PLXTECH_NAS782XState *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case 0x0 ... 0xffffc:
        s->plxtech_nand_nas782x0_reserved[offset >> 2] = val;
        break;
    }
    plxtech_nand_nas782x0_update(s);
}

static const MemoryRegionOps plxtech_nand_nas782x_ops0 = {
    .read = plxtech_nand_nas782x0_read,
    .write = plxtech_nand_nas782x0_write,
    .endianness = DEVICE_LITTLE_ENDIAN,
};
    static void plxtech_nand_nas782x1_update(void *opaque)
{
    /* PLXTECH_NAS782XState *s = opaque; */
}

static uint64_t plxtech_nand_nas782x1_read(void *opaque, hwaddr offset, unsigned size)
{
    PLXTECH_NAS782XState *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case 0x0 ... 0x1c:
        res = s->plxtech_nand_nas782x1_reserved[offset >> 2];
        break;
    }
    return res;
}

static void plxtech_nand_nas782x1_write(void *opaque, hwaddr offset, uint64_t val, unsigned size)
{
    PLXTECH_NAS782XState *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case 0x0 ... 0x1c:
        s->plxtech_nand_nas782x1_reserved[offset >> 2] = val;
        break;
    }
    plxtech_nand_nas782x1_update(s);
}

static const MemoryRegionOps plxtech_nand_nas782x_ops1 = {
    .read = plxtech_nand_nas782x1_read,
    .write = plxtech_nand_nas782x1_write,
    .endianness = DEVICE_LITTLE_ENDIAN,
};

static void plxtech_nas782x_ehci0_update(void *opaque)
{
    /* PLXTECH_NAS782XState *s = opaque; */
}

static uint64_t plxtech_nas782x_ehci0_read(void *opaque, hwaddr offset, unsigned size)
{
    PLXTECH_NAS782XState *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case 0x0 ... 0xefc:
        res = s->plxtech_nas782x_ehci0_reserved[offset >> 2];
        break;
    }
    return res;
}

static void plxtech_nas782x_ehci0_write(void *opaque, hwaddr offset, uint64_t val, unsigned size)
{
    PLXTECH_NAS782XState *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case 0x0 ... 0xefc:
        s->plxtech_nas782x_ehci0_reserved[offset >> 2] = val;
        break;
    }
    plxtech_nas782x_ehci0_update(s);
}

static const MemoryRegionOps plxtech_nas782x_ehci_ops0 = {
    .read = plxtech_nas782x_ehci0_read,
    .write = plxtech_nas782x_ehci0_write,
    .endianness = DEVICE_LITTLE_ENDIAN,
};

static void snps_dwmac0_update(void *opaque)
{
    /* PLXTECH_NAS782XState *s = opaque; */
}

static uint64_t snps_dwmac0_read(void *opaque, hwaddr offset, unsigned size)
{
    PLXTECH_NAS782XState *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case 0x0 ... 0x1ffc:
        res = s->snps_dwmac0_reserved[offset >> 2];
        break;
    }
    return res;
}

static void snps_dwmac0_write(void *opaque, hwaddr offset, uint64_t val, unsigned size)
{
    PLXTECH_NAS782XState *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case 0x0 ... 0x1ffc:
        s->snps_dwmac0_reserved[offset >> 2] = val;
        break;
    }
    snps_dwmac0_update(s);
}

static const MemoryRegionOps snps_dwmac_ops0 = {
    .read = snps_dwmac0_read,
    .write = snps_dwmac0_write,
    .endianness = DEVICE_LITTLE_ENDIAN,
};

static void plxtech_nas782x_sata0_update(void *opaque)
{
    /* PLXTECH_NAS782XState *s = opaque; */
}

static uint64_t plxtech_nas782x_sata0_read(void *opaque, hwaddr offset, unsigned size)
{
    PLXTECH_NAS782XState *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case 0x0 ... 0x1fffc:
        res = s->plxtech_nas782x_sata0_reserved[offset >> 2];
        break;
    }
    return res;
}

static void plxtech_nas782x_sata0_write(void *opaque, hwaddr offset, uint64_t val, unsigned size)
{
    PLXTECH_NAS782XState *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case 0x0 ... 0x1fffc:
        s->plxtech_nas782x_sata0_reserved[offset >> 2] = val;
        break;
    }
    plxtech_nas782x_sata0_update(s);
}

static const MemoryRegionOps plxtech_nas782x_sata_ops0 = {
    .read = plxtech_nas782x_sata0_read,
    .write = plxtech_nas782x_sata0_write,
    .endianness = DEVICE_LITTLE_ENDIAN,
};
    static void plxtech_nas782x_sata1_update(void *opaque)
{
    /* PLXTECH_NAS782XState *s = opaque; */
}

static uint64_t plxtech_nas782x_sata1_read(void *opaque, hwaddr offset, unsigned size)
{
    PLXTECH_NAS782XState *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case 0x0 ... 0x3c:
        res = s->plxtech_nas782x_sata1_reserved[offset >> 2];
        break;
    }
    return res;
}

static void plxtech_nas782x_sata1_write(void *opaque, hwaddr offset, uint64_t val, unsigned size)
{
    PLXTECH_NAS782XState *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case 0x0 ... 0x3c:
        s->plxtech_nas782x_sata1_reserved[offset >> 2] = val;
        break;
    }
    plxtech_nas782x_sata1_update(s);
}

static const MemoryRegionOps plxtech_nas782x_sata_ops1 = {
    .read = plxtech_nas782x_sata1_read,
    .write = plxtech_nas782x_sata1_write,
    .endianness = DEVICE_LITTLE_ENDIAN,
};
    static void plxtech_nas782x_sata2_update(void *opaque)
{
    /* PLXTECH_NAS782XState *s = opaque; */
}

static uint64_t plxtech_nas782x_sata2_read(void *opaque, hwaddr offset, unsigned size)
{
    PLXTECH_NAS782XState *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case 0x0 ... 0x1c:
        res = s->plxtech_nas782x_sata2_reserved[offset >> 2];
        break;
    }
    return res;
}

static void plxtech_nas782x_sata2_write(void *opaque, hwaddr offset, uint64_t val, unsigned size)
{
    PLXTECH_NAS782XState *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case 0x0 ... 0x1c:
        s->plxtech_nas782x_sata2_reserved[offset >> 2] = val;
        break;
    }
    plxtech_nas782x_sata2_update(s);
}

static const MemoryRegionOps plxtech_nas782x_sata_ops2 = {
    .read = plxtech_nas782x_sata2_read,
    .write = plxtech_nas782x_sata2_write,
    .endianness = DEVICE_LITTLE_ENDIAN,
};
    static void plxtech_nas782x_sata3_update(void *opaque)
{
    /* PLXTECH_NAS782XState *s = opaque; */
}

static uint64_t plxtech_nas782x_sata3_read(void *opaque, hwaddr offset, unsigned size)
{
    PLXTECH_NAS782XState *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case 0x0 ... 0x1ffc:
        res = s->plxtech_nas782x_sata3_reserved[offset >> 2];
        break;
    }
    return res;
}

static void plxtech_nas782x_sata3_write(void *opaque, hwaddr offset, uint64_t val, unsigned size)
{
    PLXTECH_NAS782XState *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case 0x0 ... 0x1ffc:
        s->plxtech_nas782x_sata3_reserved[offset >> 2] = val;
        break;
    }
    plxtech_nas782x_sata3_update(s);
}

static const MemoryRegionOps plxtech_nas782x_sata_ops3 = {
    .read = plxtech_nas782x_sata3_read,
    .write = plxtech_nas782x_sata3_write,
    .endianness = DEVICE_LITTLE_ENDIAN,
};
    static void plxtech_nas782x_sata4_update(void *opaque)
{
    /* PLXTECH_NAS782XState *s = opaque; */
}

static uint64_t plxtech_nas782x_sata4_read(void *opaque, hwaddr offset, unsigned size)
{
    PLXTECH_NAS782XState *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case 0x0 ... 0x8:
        res = s->plxtech_nas782x_sata4_reserved[offset >> 2];
        break;
    }
    return res;
}

static void plxtech_nas782x_sata4_write(void *opaque, hwaddr offset, uint64_t val, unsigned size)
{
    PLXTECH_NAS782XState *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case 0x0 ... 0x8:
        s->plxtech_nas782x_sata4_reserved[offset >> 2] = val;
        break;
    }
    plxtech_nas782x_sata4_update(s);
}

static const MemoryRegionOps plxtech_nas782x_sata_ops4 = {
    .read = plxtech_nas782x_sata4_read,
    .write = plxtech_nas782x_sata4_write,
    .endianness = DEVICE_LITTLE_ENDIAN,
};
    static void plxtech_nas782x_sata5_update(void *opaque)
{
    /* PLXTECH_NAS782XState *s = opaque; */
}

static uint64_t plxtech_nas782x_sata5_read(void *opaque, hwaddr offset, unsigned size)
{
    PLXTECH_NAS782XState *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case 0x0 ... 0xffc:
        res = s->plxtech_nas782x_sata5_reserved[offset >> 2];
        break;
    }
    return res;
}

static void plxtech_nas782x_sata5_write(void *opaque, hwaddr offset, uint64_t val, unsigned size)
{
    PLXTECH_NAS782XState *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case 0x0 ... 0xffc:
        s->plxtech_nas782x_sata5_reserved[offset >> 2] = val;
        break;
    }
    plxtech_nas782x_sata5_update(s);
}

static const MemoryRegionOps plxtech_nas782x_sata_ops5 = {
    .read = plxtech_nas782x_sata5_read,
    .write = plxtech_nas782x_sata5_write,
    .endianness = DEVICE_LITTLE_ENDIAN,
};

static void plxtech_nas782x_pcie0_update(void *opaque)
{
    /* PLXTECH_NAS782XState *s = opaque; */
}

static uint64_t plxtech_nas782x_pcie0_read(void *opaque, hwaddr offset, unsigned size)
{
    PLXTECH_NAS782XState *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case 0x0 ... 0xc:
        res = s->plxtech_nas782x_pcie0_reserved[offset >> 2];
        break;
    }
    return res;
}

static void plxtech_nas782x_pcie0_write(void *opaque, hwaddr offset, uint64_t val, unsigned size)
{
    PLXTECH_NAS782XState *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case 0x0 ... 0xc:
        s->plxtech_nas782x_pcie0_reserved[offset >> 2] = val;
        break;
    }
    plxtech_nas782x_pcie0_update(s);
}

static const MemoryRegionOps plxtech_nas782x_pcie_ops0 = {
    .read = plxtech_nas782x_pcie0_read,
    .write = plxtech_nas782x_pcie0_write,
    .endianness = DEVICE_LITTLE_ENDIAN,
};
    static void plxtech_nas782x_pcie1_update(void *opaque)
{
    /* PLXTECH_NAS782XState *s = opaque; */
}

static uint64_t plxtech_nas782x_pcie1_read(void *opaque, hwaddr offset, unsigned size)
{
    PLXTECH_NAS782XState *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case 0x0 ... 0xffc:
        res = s->plxtech_nas782x_pcie1_reserved[offset >> 2];
        break;
    }
    return res;
}

static void plxtech_nas782x_pcie1_write(void *opaque, hwaddr offset, uint64_t val, unsigned size)
{
    PLXTECH_NAS782XState *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case 0x0 ... 0xffc:
        s->plxtech_nas782x_pcie1_reserved[offset >> 2] = val;
        break;
    }
    plxtech_nas782x_pcie1_update(s);
}

static const MemoryRegionOps plxtech_nas782x_pcie_ops1 = {
    .read = plxtech_nas782x_pcie1_read,
    .write = plxtech_nas782x_pcie1_write,
    .endianness = DEVICE_LITTLE_ENDIAN,
};
    static void plxtech_nas782x_pcie2_update(void *opaque)
{
    /* PLXTECH_NAS782XState *s = opaque; */
}

static uint64_t plxtech_nas782x_pcie2_read(void *opaque, hwaddr offset, unsigned size)
{
    PLXTECH_NAS782XState *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case 0x0 ... 0xfc:
        res = s->plxtech_nas782x_pcie2_reserved[offset >> 2];
        break;
    }
    return res;
}

static void plxtech_nas782x_pcie2_write(void *opaque, hwaddr offset, uint64_t val, unsigned size)
{
    PLXTECH_NAS782XState *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case 0x0 ... 0xfc:
        s->plxtech_nas782x_pcie2_reserved[offset >> 2] = val;
        break;
    }
    plxtech_nas782x_pcie2_update(s);
}

static const MemoryRegionOps plxtech_nas782x_pcie_ops2 = {
    .read = plxtech_nas782x_pcie2_read,
    .write = plxtech_nas782x_pcie2_write,
    .endianness = DEVICE_LITTLE_ENDIAN,
};
    static void plxtech_nas782x_pcie3_update(void *opaque)
{
    /* PLXTECH_NAS782XState *s = opaque; */
}

static uint64_t plxtech_nas782x_pcie3_read(void *opaque, hwaddr offset, unsigned size)
{
    PLXTECH_NAS782XState *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case 0x0 ... 0xffc:
        res = s->plxtech_nas782x_pcie3_reserved[offset >> 2];
        break;
    }
    return res;
}

static void plxtech_nas782x_pcie3_write(void *opaque, hwaddr offset, uint64_t val, unsigned size)
{
    PLXTECH_NAS782XState *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case 0x0 ... 0xffc:
        s->plxtech_nas782x_pcie3_reserved[offset >> 2] = val;
        break;
    }
    plxtech_nas782x_pcie3_update(s);
}

static const MemoryRegionOps plxtech_nas782x_pcie_ops3 = {
    .read = plxtech_nas782x_pcie3_read,
    .write = plxtech_nas782x_pcie3_write,
    .endianness = DEVICE_LITTLE_ENDIAN,
};
    static void plxtech_nas782x_pcie4_update(void *opaque)
{
    /* PLXTECH_NAS782XState *s = opaque; */
}

static uint64_t plxtech_nas782x_pcie4_read(void *opaque, hwaddr offset, unsigned size)
{
    PLXTECH_NAS782XState *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case 0x0 ... 0xfc:
        res = s->plxtech_nas782x_pcie4_reserved[offset >> 2];
        break;
    }
    return res;
}

static void plxtech_nas782x_pcie4_write(void *opaque, hwaddr offset, uint64_t val, unsigned size)
{
    PLXTECH_NAS782XState *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case 0x0 ... 0xfc:
        s->plxtech_nas782x_pcie4_reserved[offset >> 2] = val;
        break;
    }
    plxtech_nas782x_pcie4_update(s);
}

static const MemoryRegionOps plxtech_nas782x_pcie_ops4 = {
    .read = plxtech_nas782x_pcie4_read,
    .write = plxtech_nas782x_pcie4_write,
    .endianness = DEVICE_LITTLE_ENDIAN,
};

static void plxtech_nas782x_gpio0_update(void *opaque)
{
    /* PLXTECH_NAS782XState *s = opaque; */
}

static uint64_t plxtech_nas782x_gpio0_read(void *opaque, hwaddr offset, unsigned size)
{
    PLXTECH_NAS782XState *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case 0x0 ... 0xfc:
        res = s->plxtech_nas782x_gpio0_reserved[offset >> 2];
        break;
    }
    return res;
}

static void plxtech_nas782x_gpio0_write(void *opaque, hwaddr offset, uint64_t val, unsigned size)
{
    PLXTECH_NAS782XState *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case 0x0 ... 0xfc:
        s->plxtech_nas782x_gpio0_reserved[offset >> 2] = val;
        break;
    }
    plxtech_nas782x_gpio0_update(s);
}

static const MemoryRegionOps plxtech_nas782x_gpio_ops0 = {
    .read = plxtech_nas782x_gpio0_read,
    .write = plxtech_nas782x_gpio0_write,
    .endianness = DEVICE_LITTLE_ENDIAN,
};
    static void plxtech_nas782x_gpio1_update(void *opaque)
{
    /* PLXTECH_NAS782XState *s = opaque; */
}

static uint64_t plxtech_nas782x_gpio1_read(void *opaque, hwaddr offset, unsigned size)
{
    PLXTECH_NAS782XState *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case 0x0 ... 0xfc:
        res = s->plxtech_nas782x_gpio1_reserved[offset >> 2];
        break;
    }
    return res;
}

static void plxtech_nas782x_gpio1_write(void *opaque, hwaddr offset, uint64_t val, unsigned size)
{
    PLXTECH_NAS782XState *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case 0x0 ... 0xfc:
        s->plxtech_nas782x_gpio1_reserved[offset >> 2] = val;
        break;
    }
    plxtech_nas782x_gpio1_update(s);
}

static const MemoryRegionOps plxtech_nas782x_gpio_ops1 = {
    .read = plxtech_nas782x_gpio1_read,
    .write = plxtech_nas782x_gpio1_write,
    .endianness = DEVICE_LITTLE_ENDIAN,
};
    static void plxtech_nas782x_gpio2_update(void *opaque)
{
    /* PLXTECH_NAS782XState *s = opaque; */
}

static uint64_t plxtech_nas782x_gpio2_read(void *opaque, hwaddr offset, unsigned size)
{
    PLXTECH_NAS782XState *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case 0x0 ... 0x1fc:
        res = s->plxtech_nas782x_gpio2_reserved[offset >> 2];
        break;
    }
    return res;
}

static void plxtech_nas782x_gpio2_write(void *opaque, hwaddr offset, uint64_t val, unsigned size)
{
    PLXTECH_NAS782XState *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case 0x0 ... 0x1fc:
        s->plxtech_nas782x_gpio2_reserved[offset >> 2] = val;
        break;
    }
    plxtech_nas782x_gpio2_update(s);
}

static const MemoryRegionOps plxtech_nas782x_gpio_ops2 = {
    .read = plxtech_nas782x_gpio2_read,
    .write = plxtech_nas782x_gpio2_write,
    .endianness = DEVICE_LITTLE_ENDIAN,
};
    static void plxtech_nas782x_gpio3_update(void *opaque)
{
    /* PLXTECH_NAS782XState *s = opaque; */
}

static uint64_t plxtech_nas782x_gpio3_read(void *opaque, hwaddr offset, unsigned size)
{
    PLXTECH_NAS782XState *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case 0x0 ... 0x1fc:
        res = s->plxtech_nas782x_gpio3_reserved[offset >> 2];
        break;
    }
    return res;
}

static void plxtech_nas782x_gpio3_write(void *opaque, hwaddr offset, uint64_t val, unsigned size)
{
    PLXTECH_NAS782XState *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case 0x0 ... 0x1fc:
        s->plxtech_nas782x_gpio3_reserved[offset >> 2] = val;
        break;
    }
    plxtech_nas782x_gpio3_update(s);
}

static const MemoryRegionOps plxtech_nas782x_gpio_ops3 = {
    .read = plxtech_nas782x_gpio3_read,
    .write = plxtech_nas782x_gpio3_write,
    .endianness = DEVICE_LITTLE_ENDIAN,
};

static void plxtech_nas782x_pllb0_update(void *opaque)
{
    /* PLXTECH_NAS782XState *s = opaque; */
}

static uint64_t plxtech_nas782x_pllb0_read(void *opaque, hwaddr offset, unsigned size)
{
    PLXTECH_NAS782XState *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case 0x0 ... 0xc:
        res = s->plxtech_nas782x_pllb0_reserved[offset >> 2];
        break;
    }
    return res;
}

static void plxtech_nas782x_pllb0_write(void *opaque, hwaddr offset, uint64_t val, unsigned size)
{
    PLXTECH_NAS782XState *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case 0x0 ... 0xc:
        s->plxtech_nas782x_pllb0_reserved[offset >> 2] = val;
        break;
    }
    plxtech_nas782x_pllb0_update(s);
}

static const MemoryRegionOps plxtech_nas782x_pllb_ops0 = {
    .read = plxtech_nas782x_pllb0_read,
    .write = plxtech_nas782x_pllb0_write,
    .endianness = DEVICE_LITTLE_ENDIAN,
};

static void plxtech_nas782x_plla0_update(void *opaque)
{
    /* PLXTECH_NAS782XState *s = opaque; */
}

static uint64_t plxtech_nas782x_plla0_read(void *opaque, hwaddr offset, unsigned size)
{
    PLXTECH_NAS782XState *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case 0x0 ... 0xc:
        res = s->plxtech_nas782x_plla0_reserved[offset >> 2];
        break;
    }
    return res;
}

static void plxtech_nas782x_plla0_write(void *opaque, hwaddr offset, uint64_t val, unsigned size)
{
    PLXTECH_NAS782XState *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case 0x0 ... 0xc:
        s->plxtech_nas782x_plla0_reserved[offset >> 2] = val;
        break;
    }
    plxtech_nas782x_plla0_update(s);
}

static const MemoryRegionOps plxtech_nas782x_plla_ops0 = {
    .read = plxtech_nas782x_plla0_read,
    .write = plxtech_nas782x_plla0_write,
    .endianness = DEVICE_LITTLE_ENDIAN,
};

static void plxtech_nas782x_reset0_update(void *opaque)
{
    /* PLXTECH_NAS782XState *s = opaque; */
}

static uint64_t plxtech_nas782x_reset0_read(void *opaque, hwaddr offset, unsigned size)
{
    PLXTECH_NAS782XState *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case 0x0 ... 0x4:
        res = s->plxtech_nas782x_reset0_reserved[offset >> 2];
        break;
    }
    return res;
}

static void plxtech_nas782x_reset0_write(void *opaque, hwaddr offset, uint64_t val, unsigned size)
{
    PLXTECH_NAS782XState *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case 0x0 ... 0x4:
        s->plxtech_nas782x_reset0_reserved[offset >> 2] = val;
        break;
    }
    plxtech_nas782x_reset0_update(s);
}

static const MemoryRegionOps plxtech_nas782x_reset_ops0 = {
    .read = plxtech_nas782x_reset0_read,
    .write = plxtech_nas782x_reset0_write,
    .endianness = DEVICE_LITTLE_ENDIAN,
};


static void plxtech_nas782x_reset(void *opaque)
{
    PLXTECH_NAS782XState *s = opaque;
    
    s->plxtech_nand_nas782x0_reserved[0x0 >> 2] = 0x40;
    s->plxtech_nas782x_plla0_reserved[0x0 >> 2] = 0x8000;
    s->plxtech_nas782x_plla0_reserved[0x4 >> 2] = 0x8000;
}

static void plxtech_nas782x_init(MachineState *machine)
{
    PLXTECH_NAS782XState *s = g_new0(PLXTECH_NAS782XState, 1);
    Error *err = NULL;
    static struct arm_boot_info binfo;
    
    s->cpu = ARM_CPU(object_new(machine->cpu_type));
    object_property_set_bool(OBJECT(s->cpu), true, "realized", &err);
    
    memory_region_allocate_system_memory(&s->ram0, OBJECT(machine), "ram0", 0x10000000);
    memory_region_add_subregion_overlap(get_system_memory(), 0x0, &s->ram0, 0);
    
    object_initialize(&s->arm_arm11mp_gic, sizeof(s->arm_arm11mp_gic), TYPE_ARM11MPCORE_PRIV);
    object_property_set_bool(OBJECT(&s->arm_arm11mp_gic), true, "realized", &err);
    sysbus_mmio_map(SYS_BUS_DEVICE(&s->arm_arm11mp_gic), 0, 0x47001000 & 0xffff0000);
    
    sysbus_connect_irq(SYS_BUS_DEVICE(&s->arm_arm11mp_gic), 0, qdev_get_gpio_in(DEVICE(s->cpu), ARM_CPU_IRQ));
    
    object_initialize(&s->timer0, sizeof(s->timer0), TYPE_PLXTECH_NAS782X_RPS_TIMER);
    qdev_set_parent_bus(DEVICE(&s->timer0), sysbus_get_default());
    object_property_set_bool(OBJECT(&s->timer0), true, "realized", &err);
    sysbus_mmio_map(SYS_BUS_DEVICE(&s->timer0), 0, 0x44400200);
    
    
    serial_mm_init(get_system_memory(), 0x44200000, 0, qdev_get_gpio_in(DEVICE(&s->arm_arm11mp_gic), 23), 115200, serial_hd(0), DEVICE_LITTLE_ENDIAN);
    
    
    
    memory_region_init_io(&s->plxtech_nand_nas782x0_mmio, NULL, &plxtech_nand_nas782x_ops0, s, TYPE_PLXTECH_NAS782X, 0x100000);
    memory_region_add_subregion_overlap(get_system_memory(), 0x41000000, &s->plxtech_nand_nas782x0_mmio, 0);
    memory_region_init_io(&s->plxtech_nand_nas782x1_mmio, NULL, &plxtech_nand_nas782x_ops1, s, TYPE_PLXTECH_NAS782X, 0x20);
    memory_region_add_subregion_overlap(get_system_memory(), 0x41c00000, &s->plxtech_nand_nas782x1_mmio, 0);
    memory_region_init_io(&s->plxtech_nas782x_ehci0_mmio, NULL, &plxtech_nas782x_ehci_ops0, s, TYPE_PLXTECH_NAS782X, 0xf00);
    memory_region_add_subregion_overlap(get_system_memory(), 0x40200100, &s->plxtech_nas782x_ehci0_mmio, 0);
    memory_region_init_io(&s->snps_dwmac0_mmio, NULL, &snps_dwmac_ops0, s, TYPE_PLXTECH_NAS782X, 0x2000);
    memory_region_add_subregion_overlap(get_system_memory(), 0x40400000, &s->snps_dwmac0_mmio, 0);
    memory_region_init_io(&s->plxtech_nas782x_sata0_mmio, NULL, &plxtech_nas782x_sata_ops0, s, TYPE_PLXTECH_NAS782X, 0x20000);
    memory_region_add_subregion_overlap(get_system_memory(), 0x45900000, &s->plxtech_nas782x_sata0_mmio, 0);
    memory_region_init_io(&s->plxtech_nas782x_sata1_mmio, NULL, &plxtech_nas782x_sata_ops1, s, TYPE_PLXTECH_NAS782X, 0x40);
    memory_region_add_subregion_overlap(get_system_memory(), 0x459a0000, &s->plxtech_nas782x_sata1_mmio, 0);
    memory_region_init_io(&s->plxtech_nas782x_sata2_mmio, NULL, &plxtech_nas782x_sata_ops2, s, TYPE_PLXTECH_NAS782X, 0x20);
    memory_region_add_subregion_overlap(get_system_memory(), 0x459b0000, &s->plxtech_nas782x_sata2_mmio, 0);
    memory_region_init_io(&s->plxtech_nas782x_sata3_mmio, NULL, &plxtech_nas782x_sata_ops3, s, TYPE_PLXTECH_NAS782X, 0x2000);
    memory_region_add_subregion_overlap(get_system_memory(), 0x459e0000, &s->plxtech_nas782x_sata3_mmio, 0);
    memory_region_init_io(&s->plxtech_nas782x_sata4_mmio, NULL, &plxtech_nas782x_sata_ops4, s, TYPE_PLXTECH_NAS782X, 0xc);
    memory_region_add_subregion_overlap(get_system_memory(), 0x44900000, &s->plxtech_nas782x_sata4_mmio, 0);
    memory_region_init_io(&s->plxtech_nas782x_sata5_mmio, NULL, &plxtech_nas782x_sata_ops5, s, TYPE_PLXTECH_NAS782X, 0x1000);
    memory_region_add_subregion_overlap(get_system_memory(), 0x50000000, &s->plxtech_nas782x_sata5_mmio, 0);
    memory_region_init_io(&s->plxtech_nas782x_pcie0_mmio, NULL, &plxtech_nas782x_pcie_ops0, s, TYPE_PLXTECH_NAS782X, 0x10);
    memory_region_add_subregion_overlap(get_system_memory(), 0x44a00000, &s->plxtech_nas782x_pcie0_mmio, 0);
    memory_region_init_io(&s->plxtech_nas782x_pcie1_mmio, NULL, &plxtech_nas782x_pcie_ops1, s, TYPE_PLXTECH_NAS782X, 0x1000);
    memory_region_add_subregion_overlap(get_system_memory(), 0x47c00000, &s->plxtech_nas782x_pcie1_mmio, 0);
    memory_region_init_io(&s->plxtech_nas782x_pcie2_mmio, NULL, &plxtech_nas782x_pcie_ops2, s, TYPE_PLXTECH_NAS782X, 0x100);
    memory_region_add_subregion_overlap(get_system_memory(), 0x47d00000, &s->plxtech_nas782x_pcie2_mmio, 0);
    memory_region_init_io(&s->plxtech_nas782x_pcie3_mmio, NULL, &plxtech_nas782x_pcie_ops3, s, TYPE_PLXTECH_NAS782X, 0x1000);
    memory_region_add_subregion_overlap(get_system_memory(), 0x47e00000, &s->plxtech_nas782x_pcie3_mmio, 0);
    memory_region_init_io(&s->plxtech_nas782x_pcie4_mmio, NULL, &plxtech_nas782x_pcie_ops4, s, TYPE_PLXTECH_NAS782X, 0x100);
    memory_region_add_subregion_overlap(get_system_memory(), 0x47f00000, &s->plxtech_nas782x_pcie4_mmio, 0);
    memory_region_init_io(&s->plxtech_nas782x_gpio0_mmio, NULL, &plxtech_nas782x_gpio_ops0, s, TYPE_PLXTECH_NAS782X, 0x100);
    memory_region_add_subregion_overlap(get_system_memory(), 0x44000000, &s->plxtech_nas782x_gpio0_mmio, 0);
    memory_region_init_io(&s->plxtech_nas782x_gpio1_mmio, NULL, &plxtech_nas782x_gpio_ops1, s, TYPE_PLXTECH_NAS782X, 0x100);
    memory_region_add_subregion_overlap(get_system_memory(), 0x44100000, &s->plxtech_nas782x_gpio1_mmio, 0);
    memory_region_init_io(&s->plxtech_nas782x_gpio2_mmio, NULL, &plxtech_nas782x_gpio_ops2, s, TYPE_PLXTECH_NAS782X, 0x200);
    memory_region_add_subregion_overlap(get_system_memory(), 0x44e00000, &s->plxtech_nas782x_gpio2_mmio, 0);
    memory_region_init_io(&s->plxtech_nas782x_gpio3_mmio, NULL, &plxtech_nas782x_gpio_ops3, s, TYPE_PLXTECH_NAS782X, 0x200);
    memory_region_add_subregion_overlap(get_system_memory(), 0x44f00000, &s->plxtech_nas782x_gpio3_mmio, 0);
    memory_region_init_io(&s->plxtech_nas782x_pllb0_mmio, NULL, &plxtech_nas782x_pllb_ops0, s, TYPE_PLXTECH_NAS782X, 0x10);
    memory_region_add_subregion_overlap(get_system_memory(), 0x44f001f0, &s->plxtech_nas782x_pllb0_mmio, 0);
    memory_region_init_io(&s->plxtech_nas782x_plla0_mmio, NULL, &plxtech_nas782x_plla_ops0, s, TYPE_PLXTECH_NAS782X, 0x10);
    memory_region_add_subregion_overlap(get_system_memory(), 0x44e001f0, &s->plxtech_nas782x_plla0_mmio, 0);
    memory_region_init_io(&s->plxtech_nas782x_reset0_mmio, NULL, &plxtech_nas782x_reset_ops0, s, TYPE_PLXTECH_NAS782X, 0x8);
    memory_region_add_subregion_overlap(get_system_memory(), 0x44e00034, &s->plxtech_nas782x_reset0_mmio, 0);
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
