/* 
 * automatically generated, don't change
 */

#include "qemu/osdep.h"
#include "qemu/log.h"
#include "qapi/error.h"
#include "target/arm/cpu.h"
#include "hw/arm/ox820.h"
#include "hw/char/serial.h"
#include "exec/address-spaces.h"

static void oxmas782x_gpioa_0_update(void *opaque);
static uint64_t oxmas782x_gpioa_0_read(void *opaque, hwaddr offset, unsigned size);
static void oxmas782x_gpioa_0_write(void *opaque, hwaddr offset, uint64_t val, unsigned size);
static void oxmas782x_gpioa_1_update(void *opaque);
static uint64_t oxmas782x_gpioa_1_read(void *opaque, hwaddr offset, unsigned size);
static void oxmas782x_gpioa_1_write(void *opaque, hwaddr offset, uint64_t val, unsigned size);
static void oxmas782x_gpiob_0_update(void *opaque);
static uint64_t oxmas782x_gpiob_0_read(void *opaque, hwaddr offset, unsigned size);
static void oxmas782x_gpiob_0_write(void *opaque, hwaddr offset, uint64_t val, unsigned size);
static void oxmas782x_gpiob_1_update(void *opaque);
static uint64_t oxmas782x_gpiob_1_read(void *opaque, hwaddr offset, unsigned size);
static void oxmas782x_gpiob_1_write(void *opaque, hwaddr offset, uint64_t val, unsigned size);
static void nas782x_pcie0_cfg_update(void *opaque);
static uint64_t nas782x_pcie0_cfg_read(void *opaque, hwaddr offset, unsigned size);
static void nas782x_pcie0_cfg_write(void *opaque, hwaddr offset, uint64_t val, unsigned size);
static void nas782x_pcie0_it_update(void *opaque);
static uint64_t nas782x_pcie0_it_read(void *opaque, hwaddr offset, unsigned size);
static void nas782x_pcie0_it_write(void *opaque, hwaddr offset, uint64_t val, unsigned size);
static void nas782x_pcie0_phy_update(void *opaque);
static uint64_t nas782x_pcie0_phy_read(void *opaque, hwaddr offset, unsigned size);
static void nas782x_pcie0_phy_write(void *opaque, hwaddr offset, uint64_t val, unsigned size);
static void nas782x_pcie1_cfg_update(void *opaque);
static uint64_t nas782x_pcie1_cfg_read(void *opaque, hwaddr offset, unsigned size);
static void nas782x_pcie1_cfg_write(void *opaque, hwaddr offset, uint64_t val, unsigned size);
static void nas782x_pcie1_it_update(void *opaque);
static uint64_t nas782x_pcie1_it_read(void *opaque, hwaddr offset, unsigned size);
static void nas782x_pcie1_it_write(void *opaque, hwaddr offset, uint64_t val, unsigned size);
static void nas782x_pcie1_phy_update(void *opaque);
static uint64_t nas782x_pcie1_phy_read(void *opaque, hwaddr offset, unsigned size);
static void nas782x_pcie1_phy_write(void *opaque, hwaddr offset, uint64_t val, unsigned size);
static void nas782x_sata_ports_update(void *opaque);
static uint64_t nas782x_sata_ports_read(void *opaque, hwaddr offset, unsigned size);
static void nas782x_sata_ports_write(void *opaque, hwaddr offset, uint64_t val, unsigned size);
static void nas782x_sata_dmactl_update(void *opaque);
static uint64_t nas782x_sata_dmactl_read(void *opaque, hwaddr offset, unsigned size);
static void nas782x_sata_dmactl_write(void *opaque, hwaddr offset, uint64_t val, unsigned size);
static void nas782x_sata_sgdma_update(void *opaque);
static uint64_t nas782x_sata_sgdma_read(void *opaque, hwaddr offset, unsigned size);
static void nas782x_sata_sgdma_write(void *opaque, hwaddr offset, uint64_t val, unsigned size);
static void nas782x_sata_core_update(void *opaque);
static uint64_t nas782x_sata_core_read(void *opaque, hwaddr offset, unsigned size);
static void nas782x_sata_core_write(void *opaque, hwaddr offset, uint64_t val, unsigned size);
static void nas782x_sata_pyh_update(void *opaque);
static uint64_t nas782x_sata_pyh_read(void *opaque, hwaddr offset, unsigned size);
static void nas782x_sata_pyh_write(void *opaque, hwaddr offset, uint64_t val, unsigned size);
static void nas782x_sata_descriptors_update(void *opaque);
static uint64_t nas782x_sata_descriptors_read(void *opaque, hwaddr offset, unsigned size);
static void nas782x_sata_descriptors_write(void *opaque, hwaddr offset, uint64_t val, unsigned size);
static void nas782x_gmac_update(void *opaque);
static uint64_t nas782x_gmac_read(void *opaque, hwaddr offset, unsigned size);
static void nas782x_gmac_write(void *opaque, hwaddr offset, uint64_t val, unsigned size);
static void nas782x_ehci_update(void *opaque);
static uint64_t nas782x_ehci_read(void *opaque, hwaddr offset, unsigned size);
static void nas782x_ehci_write(void *opaque, hwaddr offset, uint64_t val, unsigned size);
static void nas782x_plla_update(void *opaque);
static uint64_t nas782x_plla_read(void *opaque, hwaddr offset, unsigned size);
static void nas782x_plla_write(void *opaque, hwaddr offset, uint64_t val, unsigned size);
static void nas782x_pllb_update(void *opaque);
static uint64_t nas782x_pllb_read(void *opaque, hwaddr offset, unsigned size);
static void nas782x_pllb_write(void *opaque, hwaddr offset, uint64_t val, unsigned size);
static void nas782x_reset_update(void *opaque);
static uint64_t nas782x_reset_read(void *opaque, hwaddr offset, unsigned size);
static void nas782x_reset_write(void *opaque, hwaddr offset, uint64_t val, unsigned size);
static void nas782x_rps_timer_update(void *opaque);
static uint64_t nas782x_rps_timer_read(void *opaque, hwaddr offset, unsigned size);
static void nas782x_rps_timer_write(void *opaque, hwaddr offset, uint64_t val, unsigned size);
static void nas782x_rps_update(void *opaque);
static uint64_t nas782x_rps_read(void *opaque, hwaddr offset, unsigned size);
static void nas782x_rps_write(void *opaque, hwaddr offset, uint64_t val, unsigned size);
static void nas782x_nand_0_update(void *opaque);
static uint64_t nas782x_nand_0_read(void *opaque, hwaddr offset, unsigned size);
static void nas782x_nand_0_write(void *opaque, hwaddr offset, uint64_t val, unsigned size);
static void nas782x_nand_1_update(void *opaque);
static uint64_t nas782x_nand_1_read(void *opaque, hwaddr offset, unsigned size);
static void nas782x_nand_1_write(void *opaque, hwaddr offset, uint64_t val, unsigned size);

static void ox820_init(Object *obj);
static void ox820_realize(DeviceState *dev, Error **errp);
static void ox820_reset(void *opaque);

static void ox820_class_init(ObjectClass *oc, void *data);
static void ox820_register_types(void);

static void oxmas782x_gpioa_0_update(void *opaque) 
{
    /* OX820State *s = opaque; */
}

static uint64_t oxmas782x_gpioa_0_read(void *opaque, hwaddr offset, unsigned size) 
{
    OX820State *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case GPIOA_0_RESERVED:
        res = s->gpioa_0_reserved;
        break;
    }
    return res;
}

static void oxmas782x_gpioa_0_write(void *opaque, hwaddr offset, uint64_t val, unsigned size) 
{
    OX820State *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case GPIOA_0_RESERVED:
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
    /* OX820State *s = opaque; */
}

static uint64_t oxmas782x_gpioa_1_read(void *opaque, hwaddr offset, unsigned size) 
{
    OX820State *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case GPIOA_1_RESERVED:
        res = s->gpioa_1_reserved;
        break;
    }
    return res;
}

static void oxmas782x_gpioa_1_write(void *opaque, hwaddr offset, uint64_t val, unsigned size) 
{
    OX820State *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case GPIOA_1_RESERVED:
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
    /* OX820State *s = opaque; */
}

static uint64_t oxmas782x_gpiob_0_read(void *opaque, hwaddr offset, unsigned size) 
{
    OX820State *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case GPIOB_0_RESERVED:
        res = s->gpiob_0_reserved;
        break;
    }
    return res;
}

static void oxmas782x_gpiob_0_write(void *opaque, hwaddr offset, uint64_t val, unsigned size) 
{
    OX820State *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case GPIOB_0_RESERVED:
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
    /* OX820State *s = opaque; */
}

static uint64_t oxmas782x_gpiob_1_read(void *opaque, hwaddr offset, unsigned size) 
{
    OX820State *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case GPIOB_1_RESERVED:
        res = s->gpiob_1_reserved;
        break;
    }
    return res;
}

static void oxmas782x_gpiob_1_write(void *opaque, hwaddr offset, uint64_t val, unsigned size) 
{
    OX820State *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case GPIOB_1_RESERVED:
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
    /* OX820State *s = opaque; */
}

static uint64_t nas782x_pcie0_cfg_read(void *opaque, hwaddr offset, unsigned size) 
{
    OX820State *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case PCIE0_CFG_RESERVED:
        res = s->pcie0_cfg_reserved;
        break;
    }
    return res;
}

static void nas782x_pcie0_cfg_write(void *opaque, hwaddr offset, uint64_t val, unsigned size) 
{
    OX820State *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case PCIE0_CFG_RESERVED:
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
    /* OX820State *s = opaque; */
}

static uint64_t nas782x_pcie0_it_read(void *opaque, hwaddr offset, unsigned size) 
{
    OX820State *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case PCIE0_IT_RESERVED:
        res = s->pcie0_it_reserved;
        break;
    }
    return res;
}

static void nas782x_pcie0_it_write(void *opaque, hwaddr offset, uint64_t val, unsigned size) 
{
    OX820State *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case PCIE0_IT_RESERVED:
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
    /* OX820State *s = opaque; */
}

static uint64_t nas782x_pcie0_phy_read(void *opaque, hwaddr offset, unsigned size) 
{
    OX820State *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case PCIE0_PHY_RESERVED:
        res = s->pcie0_phy_reserved;
        break;
    }
    return res;
}

static void nas782x_pcie0_phy_write(void *opaque, hwaddr offset, uint64_t val, unsigned size) 
{
    OX820State *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case PCIE0_PHY_RESERVED:
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
    /* OX820State *s = opaque; */
}

static uint64_t nas782x_pcie1_cfg_read(void *opaque, hwaddr offset, unsigned size) 
{
    OX820State *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case PCIE1_CFG_RESERVED:
        res = s->pcie1_cfg_reserved;
        break;
    }
    return res;
}

static void nas782x_pcie1_cfg_write(void *opaque, hwaddr offset, uint64_t val, unsigned size) 
{
    OX820State *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case PCIE1_CFG_RESERVED:
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
    /* OX820State *s = opaque; */
}

static uint64_t nas782x_pcie1_it_read(void *opaque, hwaddr offset, unsigned size) 
{
    OX820State *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case PCIE1_IT_RESERVED:
        res = s->pcie1_it_reserved;
        break;
    }
    return res;
}

static void nas782x_pcie1_it_write(void *opaque, hwaddr offset, uint64_t val, unsigned size) 
{
    OX820State *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case PCIE1_IT_RESERVED:
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
    /* OX820State *s = opaque; */
}

static uint64_t nas782x_pcie1_phy_read(void *opaque, hwaddr offset, unsigned size) 
{
    OX820State *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case PCIE1_PHY_RESERVED:
        res = s->pcie1_phy_reserved;
        break;
    }
    return res;
}

static void nas782x_pcie1_phy_write(void *opaque, hwaddr offset, uint64_t val, unsigned size) 
{
    OX820State *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case PCIE1_PHY_RESERVED:
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
    /* OX820State *s = opaque; */
}

static uint64_t nas782x_sata_ports_read(void *opaque, hwaddr offset, unsigned size) 
{
    OX820State *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case SATA_PORTS_RESERVED:
        res = s->sata_ports_reserved;
        break;
    }
    return res;
}

static void nas782x_sata_ports_write(void *opaque, hwaddr offset, uint64_t val, unsigned size) 
{
    OX820State *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case SATA_PORTS_RESERVED:
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
    /* OX820State *s = opaque; */
}

static uint64_t nas782x_sata_dmactl_read(void *opaque, hwaddr offset, unsigned size) 
{
    OX820State *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case SATA_DMACTL_RESERVED:
        res = s->sata_dmactl_reserved;
        break;
    }
    return res;
}

static void nas782x_sata_dmactl_write(void *opaque, hwaddr offset, uint64_t val, unsigned size) 
{
    OX820State *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case SATA_DMACTL_RESERVED:
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
    /* OX820State *s = opaque; */
}

static uint64_t nas782x_sata_sgdma_read(void *opaque, hwaddr offset, unsigned size) 
{
    OX820State *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case SATA_SGDMA_RESERVED:
        res = s->sata_sgdma_reserved;
        break;
    }
    return res;
}

static void nas782x_sata_sgdma_write(void *opaque, hwaddr offset, uint64_t val, unsigned size) 
{
    OX820State *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case SATA_SGDMA_RESERVED:
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
    /* OX820State *s = opaque; */
}

static uint64_t nas782x_sata_core_read(void *opaque, hwaddr offset, unsigned size) 
{
    OX820State *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case SATA_CORE_RESERVED:
        res = s->sata_core_reserved;
        break;
    }
    return res;
}

static void nas782x_sata_core_write(void *opaque, hwaddr offset, uint64_t val, unsigned size) 
{
    OX820State *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case SATA_CORE_RESERVED:
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
    /* OX820State *s = opaque; */
}

static uint64_t nas782x_sata_pyh_read(void *opaque, hwaddr offset, unsigned size) 
{
    OX820State *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case SATA_PYH_RESERVED:
        res = s->sata_pyh_reserved;
        break;
    }
    return res;
}

static void nas782x_sata_pyh_write(void *opaque, hwaddr offset, uint64_t val, unsigned size) 
{
    OX820State *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case SATA_PYH_RESERVED:
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
    /* OX820State *s = opaque; */
}

static uint64_t nas782x_sata_descriptors_read(void *opaque, hwaddr offset, unsigned size) 
{
    OX820State *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case SATA_DESCRIPTORS_RESERVED:
        res = s->sata_descriptors_reserved;
        break;
    }
    return res;
}

static void nas782x_sata_descriptors_write(void *opaque, hwaddr offset, uint64_t val, unsigned size) 
{
    OX820State *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case SATA_DESCRIPTORS_RESERVED:
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
    /* OX820State *s = opaque; */
}

static uint64_t nas782x_gmac_read(void *opaque, hwaddr offset, unsigned size) 
{
    OX820State *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case GMAC_RESERVED:
        res = s->gmac_reserved;
        break;
    }
    return res;
}

static void nas782x_gmac_write(void *opaque, hwaddr offset, uint64_t val, unsigned size) 
{
    OX820State *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case GMAC_RESERVED:
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
    /* OX820State *s = opaque; */
}

static uint64_t nas782x_ehci_read(void *opaque, hwaddr offset, unsigned size) 
{
    OX820State *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case EHCI_RESERVED:
        res = s->ehci_reserved;
        break;
    }
    return res;
}

static void nas782x_ehci_write(void *opaque, hwaddr offset, uint64_t val, unsigned size) 
{
    OX820State *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case EHCI_RESERVED:
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
    /* OX820State *s = opaque; */
}

static uint64_t nas782x_plla_read(void *opaque, hwaddr offset, unsigned size) 
{
    OX820State *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case PLLA_CTRL_0:
        res = s->plla_ctrl_0;
        break;
    case PLLA_CTRL_1:
        res = s->plla_ctrl_1;
        break;
    case PLLA_RESERVED:
        res = s->plla_reserved;
        break;
    }
    return res;
}

static void nas782x_plla_write(void *opaque, hwaddr offset, uint64_t val, unsigned size) 
{
    OX820State *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case PLLA_CTRL_0:
        s->plla_ctrl_0 = val;
        break;
    case PLLA_CTRL_1:
        s->plla_ctrl_1 = val;
        break;
    case PLLA_RESERVED:
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
    /* OX820State *s = opaque; */
}

static uint64_t nas782x_pllb_read(void *opaque, hwaddr offset, unsigned size) 
{
    OX820State *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case PLLB_RESERVED:
        res = s->pllb_reserved;
        break;
    }
    return res;
}

static void nas782x_pllb_write(void *opaque, hwaddr offset, uint64_t val, unsigned size) 
{
    OX820State *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case PLLB_RESERVED:
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
    /* OX820State *s = opaque; */
}

static uint64_t nas782x_reset_read(void *opaque, hwaddr offset, unsigned size) 
{
    OX820State *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case RESET_RESERVED:
        res = s->reset_reserved;
        break;
    }
    return res;
}

static void nas782x_reset_write(void *opaque, hwaddr offset, uint64_t val, unsigned size) 
{
    OX820State *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case RESET_RESERVED:
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
    /* OX820State *s = opaque; */
}

static uint64_t nas782x_rps_timer_read(void *opaque, hwaddr offset, unsigned size) 
{
    OX820State *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case RPS_TIMER_RESERVED:
        res = s->rps_timer_reserved;
        break;
    }
    return res;
}

static void nas782x_rps_timer_write(void *opaque, hwaddr offset, uint64_t val, unsigned size) 
{
    OX820State *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case RPS_TIMER_RESERVED:
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
    /* OX820State *s = opaque; */
}

static uint64_t nas782x_rps_read(void *opaque, hwaddr offset, unsigned size) 
{
    OX820State *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case RPS_RESERVED:
        res = s->rps_reserved;
        break;
    }
    return res;
}

static void nas782x_rps_write(void *opaque, hwaddr offset, uint64_t val, unsigned size) 
{
    OX820State *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case RPS_RESERVED:
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
    /* OX820State *s = opaque; */
}

static uint64_t nas782x_nand_0_read(void *opaque, hwaddr offset, unsigned size) 
{
    OX820State *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case IO_ADDR_R:
        res = s->io_addr_r;
        break;
    case NAND_0_RESERVED:
        res = s->nand_0_reserved;
        break;
    }
    return res;
}

static void nas782x_nand_0_write(void *opaque, hwaddr offset, uint64_t val, unsigned size) 
{
    OX820State *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case IO_ADDR_R:
        s->io_addr_r = val;
        break;
    case NAND_0_RESERVED:
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
    /* OX820State *s = opaque; */
}

static uint64_t nas782x_nand_1_read(void *opaque, hwaddr offset, unsigned size) 
{
    OX820State *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case NAND_1_RESERVED:
        res = s->nand_1_reserved;
        break;
    }
    return res;
}

static void nas782x_nand_1_write(void *opaque, hwaddr offset, uint64_t val, unsigned size) 
{
    OX820State *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case NAND_1_RESERVED:
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

static void ox820_reset(void *opaque)
{
    OX820State *s = opaque;
    
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

static void ox820_init(Object *obj) 
{
    OX820State *s = OX820(obj);

    /* initialize cpus and add the cpu as soc's child */
    s->cpu_type = ARM_CPU_TYPE_NAME("arm11mpcore");
    s->cpu = ARM_CPU(object_new(s->cpu_type));

    /* initialize the cpus' private peripherals */
    sysbus_init_child_obj(obj, "cpu_pp", &s->cpu_pp, sizeof(s->cpu_pp), TYPE_ARM11MPCORE_PRIV);

    /* initialize bamboo device registers */
    /* initialize oxmas782x_gpioa_0 registers */
    memory_region_init_io(&s->oxmas782x_gpioa_0_mmio, obj,
        &oxmas782x_gpioa_0_ops, s, TYPE_OX820, OXMAS782X_GPIOA_0_MMIO_SIZE);
    sysbus_init_mmio(SYS_BUS_DEVICE(s), &s->oxmas782x_gpioa_0_mmio);
    /* initialize oxmas782x_gpioa_1 registers */
    memory_region_init_io(&s->oxmas782x_gpioa_1_mmio, obj,
        &oxmas782x_gpioa_1_ops, s, TYPE_OX820, OXMAS782X_GPIOA_1_MMIO_SIZE);
    sysbus_init_mmio(SYS_BUS_DEVICE(s), &s->oxmas782x_gpioa_1_mmio);
    /* initialize oxmas782x_gpiob_0 registers */
    memory_region_init_io(&s->oxmas782x_gpiob_0_mmio, obj,
        &oxmas782x_gpiob_0_ops, s, TYPE_OX820, OXMAS782X_GPIOB_0_MMIO_SIZE);
    sysbus_init_mmio(SYS_BUS_DEVICE(s), &s->oxmas782x_gpiob_0_mmio);
    /* initialize oxmas782x_gpiob_1 registers */
    memory_region_init_io(&s->oxmas782x_gpiob_1_mmio, obj,
        &oxmas782x_gpiob_1_ops, s, TYPE_OX820, OXMAS782X_GPIOB_1_MMIO_SIZE);
    sysbus_init_mmio(SYS_BUS_DEVICE(s), &s->oxmas782x_gpiob_1_mmio);
    /* initialize nas782x_pcie0_cfg registers */
    memory_region_init_io(&s->nas782x_pcie0_cfg_mmio, obj,
        &nas782x_pcie0_cfg_ops, s, TYPE_OX820, NAS782X_PCIE0_CFG_MMIO_SIZE);
    sysbus_init_mmio(SYS_BUS_DEVICE(s), &s->nas782x_pcie0_cfg_mmio);
    /* initialize nas782x_pcie0_it registers */
    memory_region_init_io(&s->nas782x_pcie0_it_mmio, obj,
        &nas782x_pcie0_it_ops, s, TYPE_OX820, NAS782X_PCIE0_IT_MMIO_SIZE);
    sysbus_init_mmio(SYS_BUS_DEVICE(s), &s->nas782x_pcie0_it_mmio);
    /* initialize nas782x_pcie0_phy registers */
    memory_region_init_io(&s->nas782x_pcie0_phy_mmio, obj,
        &nas782x_pcie0_phy_ops, s, TYPE_OX820, NAS782X_PCIE0_PHY_MMIO_SIZE);
    sysbus_init_mmio(SYS_BUS_DEVICE(s), &s->nas782x_pcie0_phy_mmio);
    /* initialize nas782x_pcie1_cfg registers */
    memory_region_init_io(&s->nas782x_pcie1_cfg_mmio, obj,
        &nas782x_pcie1_cfg_ops, s, TYPE_OX820, NAS782X_PCIE1_CFG_MMIO_SIZE);
    sysbus_init_mmio(SYS_BUS_DEVICE(s), &s->nas782x_pcie1_cfg_mmio);
    /* initialize nas782x_pcie1_it registers */
    memory_region_init_io(&s->nas782x_pcie1_it_mmio, obj,
        &nas782x_pcie1_it_ops, s, TYPE_OX820, NAS782X_PCIE1_IT_MMIO_SIZE);
    sysbus_init_mmio(SYS_BUS_DEVICE(s), &s->nas782x_pcie1_it_mmio);
    /* initialize nas782x_pcie1_phy registers */
    memory_region_init_io(&s->nas782x_pcie1_phy_mmio, obj,
        &nas782x_pcie1_phy_ops, s, TYPE_OX820, NAS782X_PCIE1_PHY_MMIO_SIZE);
    sysbus_init_mmio(SYS_BUS_DEVICE(s), &s->nas782x_pcie1_phy_mmio);
    /* initialize nas782x_sata_ports registers */
    memory_region_init_io(&s->nas782x_sata_ports_mmio, obj,
        &nas782x_sata_ports_ops, s, TYPE_OX820, NAS782X_SATA_PORTS_MMIO_SIZE);
    sysbus_init_mmio(SYS_BUS_DEVICE(s), &s->nas782x_sata_ports_mmio);
    /* initialize nas782x_sata_dmactl registers */
    memory_region_init_io(&s->nas782x_sata_dmactl_mmio, obj,
        &nas782x_sata_dmactl_ops, s, TYPE_OX820, NAS782X_SATA_DMACTL_MMIO_SIZE);
    sysbus_init_mmio(SYS_BUS_DEVICE(s), &s->nas782x_sata_dmactl_mmio);
    /* initialize nas782x_sata_sgdma registers */
    memory_region_init_io(&s->nas782x_sata_sgdma_mmio, obj,
        &nas782x_sata_sgdma_ops, s, TYPE_OX820, NAS782X_SATA_SGDMA_MMIO_SIZE);
    sysbus_init_mmio(SYS_BUS_DEVICE(s), &s->nas782x_sata_sgdma_mmio);
    /* initialize nas782x_sata_core registers */
    memory_region_init_io(&s->nas782x_sata_core_mmio, obj,
        &nas782x_sata_core_ops, s, TYPE_OX820, NAS782X_SATA_CORE_MMIO_SIZE);
    sysbus_init_mmio(SYS_BUS_DEVICE(s), &s->nas782x_sata_core_mmio);
    /* initialize nas782x_sata_pyh registers */
    memory_region_init_io(&s->nas782x_sata_pyh_mmio, obj,
        &nas782x_sata_pyh_ops, s, TYPE_OX820, NAS782X_SATA_PYH_MMIO_SIZE);
    sysbus_init_mmio(SYS_BUS_DEVICE(s), &s->nas782x_sata_pyh_mmio);
    /* initialize nas782x_sata_descriptors registers */
    memory_region_init_io(&s->nas782x_sata_descriptors_mmio, obj,
        &nas782x_sata_descriptors_ops, s, TYPE_OX820, NAS782X_SATA_DESCRIPTORS_MMIO_SIZE);
    sysbus_init_mmio(SYS_BUS_DEVICE(s), &s->nas782x_sata_descriptors_mmio);
    /* initialize nas782x_gmac registers */
    memory_region_init_io(&s->nas782x_gmac_mmio, obj,
        &nas782x_gmac_ops, s, TYPE_OX820, NAS782X_GMAC_MMIO_SIZE);
    sysbus_init_mmio(SYS_BUS_DEVICE(s), &s->nas782x_gmac_mmio);
    /* initialize nas782x_ehci registers */
    memory_region_init_io(&s->nas782x_ehci_mmio, obj,
        &nas782x_ehci_ops, s, TYPE_OX820, NAS782X_EHCI_MMIO_SIZE);
    sysbus_init_mmio(SYS_BUS_DEVICE(s), &s->nas782x_ehci_mmio);
    /* initialize nas782x_plla registers */
    memory_region_init_io(&s->nas782x_plla_mmio, obj,
        &nas782x_plla_ops, s, TYPE_OX820, NAS782X_PLLA_MMIO_SIZE);
    sysbus_init_mmio(SYS_BUS_DEVICE(s), &s->nas782x_plla_mmio);
    /* initialize nas782x_pllb registers */
    memory_region_init_io(&s->nas782x_pllb_mmio, obj,
        &nas782x_pllb_ops, s, TYPE_OX820, NAS782X_PLLB_MMIO_SIZE);
    sysbus_init_mmio(SYS_BUS_DEVICE(s), &s->nas782x_pllb_mmio);
    /* initialize nas782x_reset registers */
    memory_region_init_io(&s->nas782x_reset_mmio, obj,
        &nas782x_reset_ops, s, TYPE_OX820, NAS782X_RESET_MMIO_SIZE);
    sysbus_init_mmio(SYS_BUS_DEVICE(s), &s->nas782x_reset_mmio);
    /* initialize nas782x_rps_timer registers */
    memory_region_init_io(&s->nas782x_rps_timer_mmio, obj,
        &nas782x_rps_timer_ops, s, TYPE_OX820, NAS782X_RPS_TIMER_MMIO_SIZE);
    sysbus_init_mmio(SYS_BUS_DEVICE(s), &s->nas782x_rps_timer_mmio);
    /* initialize nas782x_rps registers */
    memory_region_init_io(&s->nas782x_rps_mmio, obj,
        &nas782x_rps_ops, s, TYPE_OX820, NAS782X_RPS_MMIO_SIZE);
    sysbus_init_mmio(SYS_BUS_DEVICE(s), &s->nas782x_rps_mmio);
    /* initialize nas782x_nand_0 registers */
    memory_region_init_io(&s->nas782x_nand_0_mmio, obj,
        &nas782x_nand_0_ops, s, TYPE_OX820, NAS782X_NAND_0_MMIO_SIZE);
    sysbus_init_mmio(SYS_BUS_DEVICE(s), &s->nas782x_nand_0_mmio);
    /* initialize nas782x_nand_1 registers */
    memory_region_init_io(&s->nas782x_nand_1_mmio, obj,
        &nas782x_nand_1_ops, s, TYPE_OX820, NAS782X_NAND_1_MMIO_SIZE);
    sysbus_init_mmio(SYS_BUS_DEVICE(s), &s->nas782x_nand_1_mmio);

    /* reset */
    ox820_reset(s);
}

static void ox820_realize(DeviceState *dev, Error **errp) 
{
    OX820State *s = OX820(dev);
    Error *err = NULL;

    /*realize the cpu private peripherals */
    object_property_set_bool(OBJECT(&s->cpu_pp), true, "realized", &err);
    if (err != NULL) {
        error_propagate(errp, err);
        return;
    }
    sysbus_mmio_map(SYS_BUS_DEVICE(&s->cpu_pp), 0, 0x47000000);
    if (serial_hd(0)) {
        serial_mm_init(get_system_memory(), 0x44200000, 0,
                       qdev_get_gpio_in(DEVICE(&s->cpu_pp), 23),
                       115200, serial_hd(0), DEVICE_LITTLE_ENDIAN);
    }

    /* realize the cpu */
    object_property_set_bool(OBJECT(s->cpu), true, "realized", &err);
    if (err) {
        error_propagate(errp, err);
        return;
    }

    /* connect irq/fiq outputs from the gic to cpu */
    sysbus_connect_irq(SYS_BUS_DEVICE(&s->cpu_pp), 0,
        qdev_get_gpio_in(DEVICE(s->cpu), ARM_CPU_IRQ));
    sysbus_connect_irq(SYS_BUS_DEVICE(&s->cpu_pp), 1,
        qdev_get_gpio_in(DEVICE(s->cpu), ARM_CPU_FIQ));
    sysbus_connect_irq(SYS_BUS_DEVICE(&s->cpu_pp), 2,
        qdev_get_gpio_in(DEVICE(s->cpu), ARM_CPU_VIRQ));
    sysbus_connect_irq(SYS_BUS_DEVICE(&s->cpu_pp), 3,
        qdev_get_gpio_in(DEVICE(s->cpu), ARM_CPU_VFIQ));
}

static void ox820_class_init(ObjectClass *oc, void *data) 
{
    DeviceClass *dc = DEVICE_CLASS(oc);

    /* dc->fw_name = ; */
    /* dc->desc = ; */
    /* dc->props = ; */
    /* dc->user_creatable = ; */
    /* dc->hotpluggable = ; */
    /* dc->reset = ; */
    dc->realize = ox820_realize;
    /* dc->unrealize = ; */
    /* dc->vmsd = ; */
    /* dc->bus_type = ; */

    /* SysBusDeviceClass sbc = SYS_BUS_DEVICE_CLASS(klass); */

    /* sbc->explicit_ofw_unit_address = ; */
    /* sbc->connect_irq_notifier = ; */
}

static const TypeInfo ox820_type_info = {
    .name = TYPE_OX820,
    .parent = TYPE_SYS_BUS_DEVICE,
    .instance_size = sizeof(OX820State),
    .instance_init = ox820_init,
    /* .class_size = sizeof(SysBusDeviceClass), */
    .class_init = ox820_class_init,
};

static void ox820_register_types(void) 
{
    type_register_static(&ox820_type_info);
}

type_init(ox820_register_types);
