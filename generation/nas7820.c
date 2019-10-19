/* 
 * automatically generated, don't change
 */

#include "qemu/osdep.h"
#include "qemu/log.h"
#include "hw/sysbus.h"
#include "target/arm/cpu-qom.h"
#include "hw/cpu/arm11mpcore.h"
#include "exec/address-spaces.h"
#include "hw/char/serial.h"
#include "sysemu/blockdev.h"
#include "hw/block/flash.h"
#include "hw/arm/arm.h"
#include "qemu/units.h"
#include "target/arm/cpu.h"
#include "hw/boards.h"

#define TYPE_NAS7820 "nas7820"
#define NAS7820(obj) \
    OBJECT_CHECK(NAS7820State, (obj), TYPE_NAS7820)

typedef struct NAS7820State {
    ARMCPU *cpu;
    ARM11MPCorePriveState cpu_pp;
    MemoryRegion ram;
    MemoryRegion oxmas782x_gpioa_0_mmio;
    uint32_t gpioa_0_reserved;
    MemoryRegion oxmas782x_gpioa_1_mmio;
    uint32_t gpioa_1_reserved;
    MemoryRegion oxmas782x_gpiob_0_mmio;
    uint32_t gpiob_0_reserved;
    MemoryRegion oxmas782x_gpiob_1_mmio;
    uint32_t gpiob_1_reserved;
    MemoryRegion nas782x_pcie0_cfg_mmio;
    uint32_t pcie0_cfg_reserved;
    MemoryRegion nas782x_pcie0_it_mmio;
    uint32_t pcie0_it_reserved;
    MemoryRegion nas782x_pcie0_phy_mmio;
    uint32_t pcie0_phy_reserved;
    MemoryRegion nas782x_pcie1_cfg_mmio;
    uint32_t pcie1_cfg_reserved;
    MemoryRegion nas782x_pcie1_it_mmio;
    uint32_t pcie1_it_reserved;
    MemoryRegion nas782x_pcie1_phy_mmio;
    uint32_t pcie1_phy_reserved;
    MemoryRegion nas782x_sata_ports_mmio;
    uint32_t sata_ports_reserved;
    MemoryRegion nas782x_sata_dmactl_mmio;
    uint32_t sata_dmactl_reserved;
    MemoryRegion nas782x_sata_sgdma_mmio;
    uint32_t sata_sgdma_reserved;
    MemoryRegion nas782x_sata_core_mmio;
    uint32_t sata_core_reserved;
    MemoryRegion nas782x_sata_pyh_mmio;
    uint32_t sata_pyh_reserved;
    MemoryRegion nas782x_sata_descriptors_mmio;
    uint32_t sata_descriptors_reserved;
    MemoryRegion nas782x_gmac_mmio;
    uint32_t gmac_reserved;
    MemoryRegion nas782x_ehci_mmio;
    uint32_t ehci_reserved;
    MemoryRegion nas782x_plla_mmio;
    uint32_t plla_ctrl_0;
    uint32_t plla_ctrl_1;
    uint32_t plla_reserved;
    MemoryRegion nas782x_pllb_mmio;
    uint32_t pllb_reserved;
    MemoryRegion nas782x_reset_mmio;
    uint32_t reset_reserved;
    MemoryRegion nas782x_rps_timer_mmio;
    uint32_t rps_timer_reserved;
    MemoryRegion nas782x_rps_mmio;
    uint32_t rps_reserved;
    MemoryRegion nas782x_nand_0_mmio;
    uint32_t io_addr_r;
    uint32_t nand_0_reserved;
    MemoryRegion nas782x_nand_1_mmio;
    uint32_t nand_1_reserved;
} NAS7820State;

static void oxmas782x_gpioa_0_update(void *opaque)
{
    /* NAS7820State *s = opaque; */
}

static uint64_t oxmas782x_gpioa_0_read(void *opaque, hwaddr offset, unsigned size)
{
    NAS7820State *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case 0x0 ... 0x100:
        res = s->gpioa_0_reserved;
        break;
    }
    return res;
}

static void oxmas782x_gpioa_0_write(void *opaque, hwaddr offset, uint64_t val, unsigned size)
{
    NAS7820State *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case 0x0 ... 0x100:
        s->gpioa_0_reserved = val;
        break;
    }
    oxmas782x_gpioa_0_update(s);
}

static const MemoryRegionOps oxmas782x_gpioa_0_ops = {
    .read = oxmas782x_gpioa_0_read,
    .write = oxmas782x_gpioa_0_write,
    .endianness = DEVICE_NATIVE_ENDIAN,
};

static void oxmas782x_gpioa_1_update(void *opaque)
{
    /* NAS7820State *s = opaque; */
}

static uint64_t oxmas782x_gpioa_1_read(void *opaque, hwaddr offset, unsigned size)
{
    NAS7820State *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case 0x0 ... 0x200:
        res = s->gpioa_1_reserved;
        break;
    }
    return res;
}

static void oxmas782x_gpioa_1_write(void *opaque, hwaddr offset, uint64_t val, unsigned size)
{
    NAS7820State *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case 0x0 ... 0x200:
        s->gpioa_1_reserved = val;
        break;
    }
    oxmas782x_gpioa_1_update(s);
}

static const MemoryRegionOps oxmas782x_gpioa_1_ops = {
    .read = oxmas782x_gpioa_1_read,
    .write = oxmas782x_gpioa_1_write,
    .endianness = DEVICE_NATIVE_ENDIAN,
};

static void oxmas782x_gpiob_0_update(void *opaque)
{
    /* NAS7820State *s = opaque; */
}

static uint64_t oxmas782x_gpiob_0_read(void *opaque, hwaddr offset, unsigned size)
{
    NAS7820State *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case 0x0 ... 0x100:
        res = s->gpiob_0_reserved;
        break;
    }
    return res;
}

static void oxmas782x_gpiob_0_write(void *opaque, hwaddr offset, uint64_t val, unsigned size)
{
    NAS7820State *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case 0x0 ... 0x100:
        s->gpiob_0_reserved = val;
        break;
    }
    oxmas782x_gpiob_0_update(s);
}

static const MemoryRegionOps oxmas782x_gpiob_0_ops = {
    .read = oxmas782x_gpiob_0_read,
    .write = oxmas782x_gpiob_0_write,
    .endianness = DEVICE_NATIVE_ENDIAN,
};

static void oxmas782x_gpiob_1_update(void *opaque)
{
    /* NAS7820State *s = opaque; */
}

static uint64_t oxmas782x_gpiob_1_read(void *opaque, hwaddr offset, unsigned size)
{
    NAS7820State *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case 0x0 ... 0x200:
        res = s->gpiob_1_reserved;
        break;
    }
    return res;
}

static void oxmas782x_gpiob_1_write(void *opaque, hwaddr offset, uint64_t val, unsigned size)
{
    NAS7820State *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case 0x0 ... 0x200:
        s->gpiob_1_reserved = val;
        break;
    }
    oxmas782x_gpiob_1_update(s);
}

static const MemoryRegionOps oxmas782x_gpiob_1_ops = {
    .read = oxmas782x_gpiob_1_read,
    .write = oxmas782x_gpiob_1_write,
    .endianness = DEVICE_NATIVE_ENDIAN,
};

static void nas782x_pcie0_cfg_update(void *opaque)
{
    /* NAS7820State *s = opaque; */
}

static uint64_t nas782x_pcie0_cfg_read(void *opaque, hwaddr offset, unsigned size)
{
    NAS7820State *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case 0x0 ... 0x1000:
        res = s->pcie0_cfg_reserved;
        break;
    }
    return res;
}

static void nas782x_pcie0_cfg_write(void *opaque, hwaddr offset, uint64_t val, unsigned size)
{
    NAS7820State *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case 0x0 ... 0x1000:
        s->pcie0_cfg_reserved = val;
        break;
    }
    nas782x_pcie0_cfg_update(s);
}

static const MemoryRegionOps nas782x_pcie0_cfg_ops = {
    .read = nas782x_pcie0_cfg_read,
    .write = nas782x_pcie0_cfg_write,
    .endianness = DEVICE_NATIVE_ENDIAN,
};

static void nas782x_pcie0_it_update(void *opaque)
{
    /* NAS7820State *s = opaque; */
}

static uint64_t nas782x_pcie0_it_read(void *opaque, hwaddr offset, unsigned size)
{
    NAS7820State *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case 0x0 ... 0x100:
        res = s->pcie0_it_reserved;
        break;
    }
    return res;
}

static void nas782x_pcie0_it_write(void *opaque, hwaddr offset, uint64_t val, unsigned size)
{
    NAS7820State *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case 0x0 ... 0x100:
        s->pcie0_it_reserved = val;
        break;
    }
    nas782x_pcie0_it_update(s);
}

static const MemoryRegionOps nas782x_pcie0_it_ops = {
    .read = nas782x_pcie0_it_read,
    .write = nas782x_pcie0_it_write,
    .endianness = DEVICE_NATIVE_ENDIAN,
};

static void nas782x_pcie0_phy_update(void *opaque)
{
    /* NAS7820State *s = opaque; */
}

static uint64_t nas782x_pcie0_phy_read(void *opaque, hwaddr offset, unsigned size)
{
    NAS7820State *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case 0x0 ... 0x10:
        res = s->pcie0_phy_reserved;
        break;
    }
    return res;
}

static void nas782x_pcie0_phy_write(void *opaque, hwaddr offset, uint64_t val, unsigned size)
{
    NAS7820State *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case 0x0 ... 0x10:
        s->pcie0_phy_reserved = val;
        break;
    }
    nas782x_pcie0_phy_update(s);
}

static const MemoryRegionOps nas782x_pcie0_phy_ops = {
    .read = nas782x_pcie0_phy_read,
    .write = nas782x_pcie0_phy_write,
    .endianness = DEVICE_NATIVE_ENDIAN,
};

static void nas782x_pcie1_cfg_update(void *opaque)
{
    /* NAS7820State *s = opaque; */
}

static uint64_t nas782x_pcie1_cfg_read(void *opaque, hwaddr offset, unsigned size)
{
    NAS7820State *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case 0x0 ... 0x1000:
        res = s->pcie1_cfg_reserved;
        break;
    }
    return res;
}

static void nas782x_pcie1_cfg_write(void *opaque, hwaddr offset, uint64_t val, unsigned size)
{
    NAS7820State *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case 0x0 ... 0x1000:
        s->pcie1_cfg_reserved = val;
        break;
    }
    nas782x_pcie1_cfg_update(s);
}

static const MemoryRegionOps nas782x_pcie1_cfg_ops = {
    .read = nas782x_pcie1_cfg_read,
    .write = nas782x_pcie1_cfg_write,
    .endianness = DEVICE_NATIVE_ENDIAN,
};

static void nas782x_pcie1_it_update(void *opaque)
{
    /* NAS7820State *s = opaque; */
}

static uint64_t nas782x_pcie1_it_read(void *opaque, hwaddr offset, unsigned size)
{
    NAS7820State *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case 0x0 ... 0x100:
        res = s->pcie1_it_reserved;
        break;
    }
    return res;
}

static void nas782x_pcie1_it_write(void *opaque, hwaddr offset, uint64_t val, unsigned size)
{
    NAS7820State *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case 0x0 ... 0x100:
        s->pcie1_it_reserved = val;
        break;
    }
    nas782x_pcie1_it_update(s);
}

static const MemoryRegionOps nas782x_pcie1_it_ops = {
    .read = nas782x_pcie1_it_read,
    .write = nas782x_pcie1_it_write,
    .endianness = DEVICE_NATIVE_ENDIAN,
};

static void nas782x_pcie1_phy_update(void *opaque)
{
    /* NAS7820State *s = opaque; */
}

static uint64_t nas782x_pcie1_phy_read(void *opaque, hwaddr offset, unsigned size)
{
    NAS7820State *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case 0x0 ... 0x10:
        res = s->pcie1_phy_reserved;
        break;
    }
    return res;
}

static void nas782x_pcie1_phy_write(void *opaque, hwaddr offset, uint64_t val, unsigned size)
{
    NAS7820State *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case 0x0 ... 0x10:
        s->pcie1_phy_reserved = val;
        break;
    }
    nas782x_pcie1_phy_update(s);
}

static const MemoryRegionOps nas782x_pcie1_phy_ops = {
    .read = nas782x_pcie1_phy_read,
    .write = nas782x_pcie1_phy_write,
    .endianness = DEVICE_NATIVE_ENDIAN,
};

static void nas782x_sata_ports_update(void *opaque)
{
    /* NAS7820State *s = opaque; */
}

static uint64_t nas782x_sata_ports_read(void *opaque, hwaddr offset, unsigned size)
{
    NAS7820State *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case 0x0 ... 0x20000:
        res = s->sata_ports_reserved;
        break;
    }
    return res;
}

static void nas782x_sata_ports_write(void *opaque, hwaddr offset, uint64_t val, unsigned size)
{
    NAS7820State *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case 0x0 ... 0x20000:
        s->sata_ports_reserved = val;
        break;
    }
    nas782x_sata_ports_update(s);
}

static const MemoryRegionOps nas782x_sata_ports_ops = {
    .read = nas782x_sata_ports_read,
    .write = nas782x_sata_ports_write,
    .endianness = DEVICE_NATIVE_ENDIAN,
};

static void nas782x_sata_dmactl_update(void *opaque)
{
    /* NAS7820State *s = opaque; */
}

static uint64_t nas782x_sata_dmactl_read(void *opaque, hwaddr offset, unsigned size)
{
    NAS7820State *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case 0x0 ... 0x40:
        res = s->sata_dmactl_reserved;
        break;
    }
    return res;
}

static void nas782x_sata_dmactl_write(void *opaque, hwaddr offset, uint64_t val, unsigned size)
{
    NAS7820State *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case 0x0 ... 0x40:
        s->sata_dmactl_reserved = val;
        break;
    }
    nas782x_sata_dmactl_update(s);
}

static const MemoryRegionOps nas782x_sata_dmactl_ops = {
    .read = nas782x_sata_dmactl_read,
    .write = nas782x_sata_dmactl_write,
    .endianness = DEVICE_NATIVE_ENDIAN,
};

static void nas782x_sata_sgdma_update(void *opaque)
{
    /* NAS7820State *s = opaque; */
}

static uint64_t nas782x_sata_sgdma_read(void *opaque, hwaddr offset, unsigned size)
{
    NAS7820State *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case 0x0 ... 0x20:
        res = s->sata_sgdma_reserved;
        break;
    }
    return res;
}

static void nas782x_sata_sgdma_write(void *opaque, hwaddr offset, uint64_t val, unsigned size)
{
    NAS7820State *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case 0x0 ... 0x20:
        s->sata_sgdma_reserved = val;
        break;
    }
    nas782x_sata_sgdma_update(s);
}

static const MemoryRegionOps nas782x_sata_sgdma_ops = {
    .read = nas782x_sata_sgdma_read,
    .write = nas782x_sata_sgdma_write,
    .endianness = DEVICE_NATIVE_ENDIAN,
};

static void nas782x_sata_core_update(void *opaque)
{
    /* NAS7820State *s = opaque; */
}

static uint64_t nas782x_sata_core_read(void *opaque, hwaddr offset, unsigned size)
{
    NAS7820State *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case 0x0 ... 0x2000:
        res = s->sata_core_reserved;
        break;
    }
    return res;
}

static void nas782x_sata_core_write(void *opaque, hwaddr offset, uint64_t val, unsigned size)
{
    NAS7820State *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case 0x0 ... 0x2000:
        s->sata_core_reserved = val;
        break;
    }
    nas782x_sata_core_update(s);
}

static const MemoryRegionOps nas782x_sata_core_ops = {
    .read = nas782x_sata_core_read,
    .write = nas782x_sata_core_write,
    .endianness = DEVICE_NATIVE_ENDIAN,
};

static void nas782x_sata_pyh_update(void *opaque)
{
    /* NAS7820State *s = opaque; */
}

static uint64_t nas782x_sata_pyh_read(void *opaque, hwaddr offset, unsigned size)
{
    NAS7820State *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case 0x0 ... 0xC:
        res = s->sata_pyh_reserved;
        break;
    }
    return res;
}

static void nas782x_sata_pyh_write(void *opaque, hwaddr offset, uint64_t val, unsigned size)
{
    NAS7820State *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case 0x0 ... 0xC:
        s->sata_pyh_reserved = val;
        break;
    }
    nas782x_sata_pyh_update(s);
}

static const MemoryRegionOps nas782x_sata_pyh_ops = {
    .read = nas782x_sata_pyh_read,
    .write = nas782x_sata_pyh_write,
    .endianness = DEVICE_NATIVE_ENDIAN,
};

static void nas782x_sata_descriptors_update(void *opaque)
{
    /* NAS7820State *s = opaque; */
}

static uint64_t nas782x_sata_descriptors_read(void *opaque, hwaddr offset, unsigned size)
{
    NAS7820State *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case 0x0 ... 0x1000:
        res = s->sata_descriptors_reserved;
        break;
    }
    return res;
}

static void nas782x_sata_descriptors_write(void *opaque, hwaddr offset, uint64_t val, unsigned size)
{
    NAS7820State *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case 0x0 ... 0x1000:
        s->sata_descriptors_reserved = val;
        break;
    }
    nas782x_sata_descriptors_update(s);
}

static const MemoryRegionOps nas782x_sata_descriptors_ops = {
    .read = nas782x_sata_descriptors_read,
    .write = nas782x_sata_descriptors_write,
    .endianness = DEVICE_NATIVE_ENDIAN,
};

static void nas782x_gmac_update(void *opaque)
{
    /* NAS7820State *s = opaque; */
}

static uint64_t nas782x_gmac_read(void *opaque, hwaddr offset, unsigned size)
{
    NAS7820State *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case 0x0 ... 0x2000:
        res = s->gmac_reserved;
        break;
    }
    return res;
}

static void nas782x_gmac_write(void *opaque, hwaddr offset, uint64_t val, unsigned size)
{
    NAS7820State *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case 0x0 ... 0x2000:
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
    /* NAS7820State *s = opaque; */
}

static uint64_t nas782x_ehci_read(void *opaque, hwaddr offset, unsigned size)
{
    NAS7820State *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case 0x0 ... 0xf00:
        res = s->ehci_reserved;
        break;
    }
    return res;
}

static void nas782x_ehci_write(void *opaque, hwaddr offset, uint64_t val, unsigned size)
{
    NAS7820State *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case 0x0 ... 0xf00:
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

static void nas782x_plla_update(void *opaque)
{
    /* NAS7820State *s = opaque; */
}

static uint64_t nas782x_plla_read(void *opaque, hwaddr offset, unsigned size)
{
    NAS7820State *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case 0x0:
        res = s->plla_ctrl_0;
        break;
    case 0x4:
        res = s->plla_ctrl_1;
        break;
    case 0x8 ... 0x10:
        res = s->plla_reserved;
        break;
    }
    return res;
}

static void nas782x_plla_write(void *opaque, hwaddr offset, uint64_t val, unsigned size)
{
    NAS7820State *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case 0x0:
        s->plla_ctrl_0 = val;
        break;
    case 0x4:
        s->plla_ctrl_1 = val;
        break;
    case 0x8 ... 0x10:
        s->plla_reserved = val;
        break;
    }
    nas782x_plla_update(s);
}

static const MemoryRegionOps nas782x_plla_ops = {
    .read = nas782x_plla_read,
    .write = nas782x_plla_write,
    .endianness = DEVICE_NATIVE_ENDIAN,
};

static void nas782x_pllb_update(void *opaque)
{
    /* NAS7820State *s = opaque; */
}

static uint64_t nas782x_pllb_read(void *opaque, hwaddr offset, unsigned size)
{
    NAS7820State *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case 0x0 ... 0x10:
        res = s->pllb_reserved;
        break;
    }
    return res;
}

static void nas782x_pllb_write(void *opaque, hwaddr offset, uint64_t val, unsigned size)
{
    NAS7820State *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case 0x0 ... 0x10:
        s->pllb_reserved = val;
        break;
    }
    nas782x_pllb_update(s);
}

static const MemoryRegionOps nas782x_pllb_ops = {
    .read = nas782x_pllb_read,
    .write = nas782x_pllb_write,
    .endianness = DEVICE_NATIVE_ENDIAN,
};

static void nas782x_reset_update(void *opaque)
{
    /* NAS7820State *s = opaque; */
}

static uint64_t nas782x_reset_read(void *opaque, hwaddr offset, unsigned size)
{
    NAS7820State *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case 0x0 ... 0x8:
        res = s->reset_reserved;
        break;
    }
    return res;
}

static void nas782x_reset_write(void *opaque, hwaddr offset, uint64_t val, unsigned size)
{
    NAS7820State *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case 0x0 ... 0x8:
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
    /* NAS7820State *s = opaque; */
}

static uint64_t nas782x_rps_timer_read(void *opaque, hwaddr offset, unsigned size)
{
    NAS7820State *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case 0x0 ... 0x40:
        res = s->rps_timer_reserved;
        break;
    }
    return res;
}

static void nas782x_rps_timer_write(void *opaque, hwaddr offset, uint64_t val, unsigned size)
{
    NAS7820State *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case 0x0 ... 0x40:
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
    /* NAS7820State *s = opaque; */
}

static uint64_t nas782x_rps_read(void *opaque, hwaddr offset, unsigned size)
{
    NAS7820State *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case 0x0 ... 0x14:
        res = s->rps_reserved;
        break;
    }
    return res;
}

static void nas782x_rps_write(void *opaque, hwaddr offset, uint64_t val, unsigned size)
{
    NAS7820State *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case 0x0 ... 0x14:
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

static void nas782x_nand_0_update(void *opaque)
{
    /* NAS7820State *s = opaque; */
}

static uint64_t nas782x_nand_0_read(void *opaque, hwaddr offset, unsigned size)
{
    NAS7820State *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case 0x0:
        res = s->io_addr_r;
        break;
    case 0x4 ... 0x100000:
        res = s->nand_0_reserved;
        break;
    }
    return res;
}

static void nas782x_nand_0_write(void *opaque, hwaddr offset, uint64_t val, unsigned size)
{
    NAS7820State *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case 0x0:
        s->io_addr_r = val;
        break;
    case 0x4 ... 0x100000:
        s->nand_0_reserved = val;
        break;
    }
    nas782x_nand_0_update(s);
}

static const MemoryRegionOps nas782x_nand_0_ops = {
    .read = nas782x_nand_0_read,
    .write = nas782x_nand_0_write,
    .endianness = DEVICE_NATIVE_ENDIAN,
};

static void nas782x_nand_1_update(void *opaque)
{
    /* NAS7820State *s = opaque; */
}

static uint64_t nas782x_nand_1_read(void *opaque, hwaddr offset, unsigned size)
{
    NAS7820State *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case 0x0 ... 0x20:
        res = s->nand_1_reserved;
        break;
    }
    return res;
}

static void nas782x_nand_1_write(void *opaque, hwaddr offset, uint64_t val, unsigned size)
{
    NAS7820State *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case 0x0 ... 0x20:
        s->nand_1_reserved = val;
        break;
    }
    nas782x_nand_1_update(s);
}

static const MemoryRegionOps nas782x_nand_1_ops = {
    .read = nas782x_nand_1_read,
    .write = nas782x_nand_1_write,
    .endianness = DEVICE_NATIVE_ENDIAN,
};

static void nas7820_reset(void *opaque)
{
    NAS7820State *s = opaque;

    s->gpioa_0_reserved = 0x0;
    s->gpioa_1_reserved = 0x0;
    s->gpiob_0_reserved = 0x0;
    s->gpiob_1_reserved = 0x0;
    s->pcie0_cfg_reserved = 0x0;
    s->pcie0_it_reserved = 0x0;
    s->pcie0_phy_reserved = 0x0;
    s->pcie1_cfg_reserved = 0x0;
    s->pcie1_it_reserved = 0x0;
    s->pcie1_phy_reserved = 0x0;
    s->sata_ports_reserved = 0x0;
    s->sata_dmactl_reserved = 0x0;
    s->sata_sgdma_reserved = 0x0;
    s->sata_core_reserved = 0x0;
    s->sata_pyh_reserved = 0x0;
    s->sata_descriptors_reserved = 0x0;
    s->gmac_reserved = 0x0;
    s->ehci_reserved = 0x0;
    s->plla_ctrl_0 = 3 << 8 | 3 << 4;
    s->plla_ctrl_1 = 32768;
    s->plla_reserved = 0x0;
    s->pllb_reserved = 0x0;
    s->reset_reserved = 0x0;
    s->rps_timer_reserved = 0x0;
    s->rps_reserved = 0x0;
    s->io_addr_r = 0x40;
    s->nand_0_reserved = 0x0;
    s->nand_1_reserved = 0x0;
}

static void nas7820_init(MachineState *machine)
{
    NAS7820State *s = g_new0(NAS7820State, 1);
    Error *err = NULL;
    DriveInfo *dinfo;
    struct arm_boot_info binfo;

    s->cpu = ARM_CPU(object_new(machine->cpu_type));
    object_property_set_bool(OBJECT(s->cpu), true, "realized", &err);
    object_initialize(&s->cpu_pp, sizeof(s->cpu_pp), TYPE_ARM11MPCORE_PRIV);
    object_property_set_bool(OBJECT(&s->cpu_pp), true, "realized", &err);
    sysbus_mmio_map(SYS_BUS_DEVICE(&s->cpu_pp), 0, 0x47000000);
    memory_region_allocate_system_memory(&s->ram, OBJECT(machine), "ram", machine->ram_size);
    memory_region_add_subregion_overlap(get_system_memory(), 0, &s->ram, -1);
    serial_mm_init(get_system_memory(), 0x44200000, 0, qdev_get_gpio_in(DEVICE(&s->cpu_pp), 23, 115200, serial_hd(0), DEVICE_LITTLE_ENDIAN);
    dinfo = drive_get(IF_MTD, 0, 0);
    nand_init(dinfo ? blk_by_legacy_dinfo(dinfo): NULL, 0xec, 0x73);

    memory_region_init_io(&s->oxmas782x_gpioa_0_mmio, NULL, &oxmas782x_gpioa_0_ops, s, TYPE_NAS7820, 0x100);
    memory_region_add_subregion_overlap(get_system_memory(), 0x44000000, &s->oxmas782x_gpioa_0_mmio, 0);
    memory_region_init_io(&s->oxmas782x_gpioa_1_mmio, NULL, &oxmas782x_gpioa_1_ops, s, TYPE_NAS7820, 0x200);
    memory_region_add_subregion_overlap(get_system_memory(), 0x44E00000, &s->oxmas782x_gpioa_1_mmio, 0);
    memory_region_init_io(&s->oxmas782x_gpiob_0_mmio, NULL, &oxmas782x_gpiob_0_ops, s, TYPE_NAS7820, 0x100);
    memory_region_add_subregion_overlap(get_system_memory(), 0x44100000, &s->oxmas782x_gpiob_0_mmio, 0);
    memory_region_init_io(&s->oxmas782x_gpiob_1_mmio, NULL, &oxmas782x_gpiob_1_ops, s, TYPE_NAS7820, 0x200);
    memory_region_add_subregion_overlap(get_system_memory(), 0x44F00000, &s->oxmas782x_gpiob_1_mmio, 0);
    memory_region_init_io(&s->nas782x_pcie0_cfg_mmio, NULL, &nas782x_pcie0_cfg_ops, s, TYPE_NAS7820, 0x1000);
    memory_region_add_subregion_overlap(get_system_memory(), 0x47C00000, &s->nas782x_pcie0_cfg_mmio, 0);
    memory_region_init_io(&s->nas782x_pcie0_it_mmio, NULL, &nas782x_pcie0_it_ops, s, TYPE_NAS7820, 0x100);
    memory_region_add_subregion_overlap(get_system_memory(), 0x47D00000, &s->nas782x_pcie0_it_mmio, 0);
    memory_region_init_io(&s->nas782x_pcie0_phy_mmio, NULL, &nas782x_pcie0_phy_ops, s, TYPE_NAS7820, 0x10);
    memory_region_add_subregion_overlap(get_system_memory(), 0x47A00000, &s->nas782x_pcie0_phy_mmio, 0);
    memory_region_init_io(&s->nas782x_pcie1_cfg_mmio, NULL, &nas782x_pcie1_cfg_ops, s, TYPE_NAS7820, 0x1000);
    memory_region_add_subregion_overlap(get_system_memory(), 0x47E00000, &s->nas782x_pcie1_cfg_mmio, 0);
    memory_region_init_io(&s->nas782x_pcie1_it_mmio, NULL, &nas782x_pcie1_it_ops, s, TYPE_NAS7820, 0x100);
    memory_region_add_subregion_overlap(get_system_memory(), 0x47F00000, &s->nas782x_pcie1_it_mmio, 0);
    memory_region_init_io(&s->nas782x_pcie1_phy_mmio, NULL, &nas782x_pcie1_phy_ops, s, TYPE_NAS7820, 0x10);
    memory_region_add_subregion_overlap(get_system_memory(), 0x44A00000, &s->nas782x_pcie1_phy_mmio, 0);
    memory_region_init_io(&s->nas782x_sata_ports_mmio, NULL, &nas782x_sata_ports_ops, s, TYPE_NAS7820, 0x20000);
    memory_region_add_subregion_overlap(get_system_memory(), 0x45900000, &s->nas782x_sata_ports_mmio, 0);
    memory_region_init_io(&s->nas782x_sata_dmactl_mmio, NULL, &nas782x_sata_dmactl_ops, s, TYPE_NAS7820, 0x40);
    memory_region_add_subregion_overlap(get_system_memory(), 0x459A0000, &s->nas782x_sata_dmactl_mmio, 0);
    memory_region_init_io(&s->nas782x_sata_sgdma_mmio, NULL, &nas782x_sata_sgdma_ops, s, TYPE_NAS7820, 0x20);
    memory_region_add_subregion_overlap(get_system_memory(), 0x459B0000, &s->nas782x_sata_sgdma_mmio, 0);
    memory_region_init_io(&s->nas782x_sata_core_mmio, NULL, &nas782x_sata_core_ops, s, TYPE_NAS7820, 0x2000);
    memory_region_add_subregion_overlap(get_system_memory(), 0x459E0000, &s->nas782x_sata_core_mmio, 0);
    memory_region_init_io(&s->nas782x_sata_pyh_mmio, NULL, &nas782x_sata_pyh_ops, s, TYPE_NAS7820, 0xC);
    memory_region_add_subregion_overlap(get_system_memory(), 0x44900000, &s->nas782x_sata_pyh_mmio, 0);
    memory_region_init_io(&s->nas782x_sata_descriptors_mmio, NULL, &nas782x_sata_descriptors_ops, s, TYPE_NAS7820, 0x1000);
    memory_region_add_subregion_overlap(get_system_memory(), 0x50000000, &s->nas782x_sata_descriptors_mmio, 0);
    memory_region_init_io(&s->nas782x_gmac_mmio, NULL, &nas782x_gmac_ops, s, TYPE_NAS7820, 0x2000);
    memory_region_add_subregion_overlap(get_system_memory(), 0x40400000, &s->nas782x_gmac_mmio, 0);
    memory_region_init_io(&s->nas782x_ehci_mmio, NULL, &nas782x_ehci_ops, s, TYPE_NAS7820, 0xf00);
    memory_region_add_subregion_overlap(get_system_memory(), 0x40200100, &s->nas782x_ehci_mmio, 0);
    memory_region_init_io(&s->nas782x_plla_mmio, NULL, &nas782x_plla_ops, s, TYPE_NAS7820, 0x10);
    memory_region_add_subregion_overlap(get_system_memory(), 0x44e001f0, &s->nas782x_plla_mmio, 0);
    memory_region_init_io(&s->nas782x_pllb_mmio, NULL, &nas782x_pllb_ops, s, TYPE_NAS7820, 0x10);
    memory_region_add_subregion_overlap(get_system_memory(), 0x44f001f0, &s->nas782x_pllb_mmio, 0);
    memory_region_init_io(&s->nas782x_reset_mmio, NULL, &nas782x_reset_ops, s, TYPE_NAS7820, 0x8);
    memory_region_add_subregion_overlap(get_system_memory(), 0x44e00034, &s->nas782x_reset_mmio, 0);
    memory_region_init_io(&s->nas782x_rps_timer_mmio, NULL, &nas782x_rps_timer_ops, s, TYPE_NAS7820, 0x40);
    memory_region_add_subregion_overlap(get_system_memory(), 0x44400200, &s->nas782x_rps_timer_mmio, 0);
    memory_region_init_io(&s->nas782x_rps_mmio, NULL, &nas782x_rps_ops, s, TYPE_NAS7820, 0x14);
    memory_region_add_subregion_overlap(get_system_memory(), 0x44400000, &s->nas782x_rps_mmio, 0);
    memory_region_init_io(&s->nas782x_nand_0_mmio, NULL, &nas782x_nand_0_ops, s, TYPE_NAS7820, 0x100000);
    memory_region_add_subregion_overlap(get_system_memory(), 0x41000000, &s->nas782x_nand_0_mmio, 0);
    memory_region_init_io(&s->nas782x_nand_1_mmio, NULL, &nas782x_nand_1_ops, s, TYPE_NAS7820, 0x20);
    memory_region_add_subregion_overlap(get_system_memory(), 0x41C00000, &s->nas782x_nand_1_mmio, 0);

    nas7820_reset(s);

    sysbus_connect_irq(SYS_BUS_DEVICE(&s->cpu_pp), 0, qdev_get_gpio_in(DEVICE(s->cpu), ARM_CPU_IRQ));
    sysbus_connect_irq(SYS_BUS_DEVICE(&s->cpu_pp), 1, qdev_get_gpio_in(DEVICE(s->cpu), ARM_CPU_FIQ));
    sysbus_connect_irq(SYS_BUS_DEVICE(&s->cpu_pp), 2, qdev_get_gpio_in(DEVICE(s->cpu), ARM_CPU_VIRQ));
    sysbus_connect_irq(SYS_BUS_DEVICE(&s->cpu_pp), 3, qdev_get_gpio_in(DEVICE(s->cpu), ARM_CPU_VFIQ));
    binfo.board_id = 0x480;
    binfo.ram_size = machine->ram_size;
    binfo.kernel_filename = machine->kernel_filename;
    binfo.kernel_cmdline = machine->kernel_cmdline;
    binfo.initrd_filename = machine->initrd_filename;
    arm_load_kernel(ARM_CPU(first_cpu), &binfo);
}

static void nas7820_machine_init(MachineClass *mc)
{
    /* mc->family = ; */
    /* mc->name = "nas7820"; */
    /* mc->alias = ; */
    mc->desc = "PLX NAS7820";
    /* mc->deprecation_reason = ; */
    mc->init = nas7820_init;
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
    /* mc->is_dault = ; */
    /* mc->default_machine_opts = ; */
    /* mc->default_boot_order = ; */
    /* mc->default_display = ; */
    /* mc->compat_props = ; */
    /* mc->hw_version = ; */
    mc->default_ram_size = 2 * GiB;
    mc->default_cpu_type = ARM_CPU_TYPE_NAME("arm11mpcore");
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

DEFINE_MACHINE("nas7820", nas7820_machine_init)