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
#include "hw/intc/marvell_orion_intc.h"
#include "hw/intc/marvell_orion_bridge_intc.h"
#include "hw/timer/marvell_orion_timer.h"
#include "hw/char/serial.h"
#include "hw/char/serial.h"

#define TYPE_MARVELL_KIRKWOOD "marvell_kirkwood"
#define MARVELL_KIRKWOOD(obj) \
    OBJECT_CHECK(MARVELL_KIRKWOODState, (obj), TYPE_MARVELL_KIRKWOOD)

typedef struct MARVELL_KIRKWOODState {
    ARMCPU *cpu;
    MARVELL_ORION_INTCState marvell_orion_intc0;
    MARVELL_ORION_INTCState marvell_orion_intc1;
    MARVELL_ORION_BRIDGE_INTCState marvell_orion_bridge_intc0;
    MARVELL_ORION_TIMERState timer0;
    MemoryRegion ram0;
    MemoryRegion plxtech_nand_nas782x0_mmio;
    MemoryRegion marvell_orion_sdio0_mmio;
    MemoryRegion marvell_orion_sata0_mmio;
    MemoryRegion marvell_mv64xxx_i2c0_mmio;
    MemoryRegion marvell_mv64xxx_i2c1_mmio;
    MemoryRegion marvell_orion_rtc0_mmio;
    MemoryRegion marvell_kirkwood_thermal0_mmio;
    MemoryRegion marvell_kirkwood_audio0_mmio;
    MemoryRegion marvell_mvebu_sata_phy0_mmio;
    MemoryRegion marvell_mvebu_sata_phy1_mmio;
    MemoryRegion marvell_kirkwood_eth0_mmio;
    MemoryRegion marvell_kirkwood_eth1_mmio;
    MemoryRegion marvell_orion_mdio0_mmio;
    MemoryRegion marvell_orion_xor0_mmio;
    MemoryRegion marvell_orion_xor1_mmio;
    MemoryRegion marvell_orion_xor2_mmio;
    MemoryRegion marvell_orion_xor3_mmio;
    MemoryRegion marvell_orion_ehci0_mmio;
    MemoryRegion marvell_kirkwood_crypto0_mmio;
    MemoryRegion marvell_orion_wdt0_mmio;
    MemoryRegion marvell_orion_wdt1_mmio;
    MemoryRegion marvell_kirkwood_cache0_mmio;
    MemoryRegion marvell_kirkwood_gating_clock0_mmio;
    MemoryRegion marvell_orion_system_controller0_mmio;
    MemoryRegion marvell_mbus_controller0_mmio;
    MemoryRegion marvell_mbus_controller1_mmio;
    MemoryRegion marvell_orion_gpio0_mmio;
    MemoryRegion marvell_orion_gpio1_mmio;
    MemoryRegion marvell_orion_spi0_mmio;
    MemoryRegion marvell_kirkwood_core_clock0_mmio;
    MemoryRegion marvell_88f6282_pinctrl0_mmio;
    MemoryRegion marvell_kirkwood_mbus0_mmio;
    MemoryRegion marvell_kirkwood_pcie0_mmio;
    MemoryRegion marvell_kirkwood_pcie1_mmio;
    MemoryRegion mmio_sram0_mmio;
    uint32_t plxtech_nand_nas782x0_reserved[0x400 >> 2];
    uint32_t marvell_orion_sdio0_reserved[0x200 >> 2];
    uint32_t marvell_orion_sata0_reserved[0x5000 >> 2];
    uint32_t marvell_mv64xxx_i2c0_reserved[0x20 >> 2];
    uint32_t marvell_mv64xxx_i2c1_reserved[0x20 >> 2];
    uint32_t marvell_orion_rtc0_reserved[0x20 >> 2];
    uint32_t marvell_kirkwood_thermal0_reserved[0x4 >> 2];
    uint32_t marvell_kirkwood_audio0_reserved[0x2210 >> 2];
    uint32_t marvell_mvebu_sata_phy0_reserved[0x334 >> 2];
    uint32_t marvell_mvebu_sata_phy1_reserved[0x334 >> 2];
    uint32_t marvell_kirkwood_eth0_reserved[0x4000 >> 2];
    uint32_t marvell_kirkwood_eth1_reserved[0x4000 >> 2];
    uint32_t marvell_orion_mdio0_reserved[0x84 >> 2];
    uint32_t marvell_orion_xor0_reserved[0x100 >> 2];
    uint32_t marvell_orion_xor1_reserved[0x100 >> 2];
    uint32_t marvell_orion_xor2_reserved[0x100 >> 2];
    uint32_t marvell_orion_xor3_reserved[0x100 >> 2];
    uint32_t marvell_orion_ehci0_reserved[0x1000 >> 2];
    uint32_t marvell_kirkwood_crypto0_reserved[0x10000 >> 2];
    uint32_t marvell_orion_wdt0_reserved[0x28 >> 2];
    uint32_t marvell_orion_wdt1_reserved[0x4 >> 2];
    uint32_t marvell_kirkwood_cache0_reserved[0x4 >> 2];
    uint32_t marvell_kirkwood_gating_clock0_reserved[0x4 >> 2];
    uint32_t marvell_orion_system_controller0_reserved[0x120 >> 2];
    uint32_t marvell_mbus_controller0_reserved[0x80 >> 2];
    uint32_t marvell_mbus_controller1_reserved[0x20 >> 2];
    uint32_t marvell_orion_gpio0_reserved[0x40 >> 2];
    uint32_t marvell_orion_gpio1_reserved[0x40 >> 2];
    uint32_t marvell_orion_spi0_reserved[0x28 >> 2];
    uint32_t marvell_kirkwood_core_clock0_reserved[0x4 >> 2];
    uint32_t marvell_88f6282_pinctrl0_reserved[0x20 >> 2];
    uint32_t marvell_kirkwood_mbus0_reserved[0x100000 >> 2];
    uint32_t marvell_kirkwood_pcie0_reserved[0x2000 >> 2];
    uint32_t marvell_kirkwood_pcie1_reserved[0x2000 >> 2];
    uint32_t mmio_sram0_reserved[0x800 >> 2];
} MARVELL_KIRKWOODState;

static void plxtech_nand_nas782x0_update(void *opaque)
{
    /* MARVELL_KIRKWOODState *s = opaque; */
}

static uint64_t plxtech_nand_nas782x0_read(void *opaque, hwaddr offset, unsigned size)
{
    MARVELL_KIRKWOODState *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case 0x0 ... 0x3fc:
        res = s->plxtech_nand_nas782x0_reserved[offset >> 2];
        break;
    }
    return res;
}

static void plxtech_nand_nas782x0_write(void *opaque, hwaddr offset, uint64_t val, unsigned size)
{
    MARVELL_KIRKWOODState *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case 0x0 ... 0x3fc:
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

static void marvell_orion_sdio0_update(void *opaque)
{
    /* MARVELL_KIRKWOODState *s = opaque; */
}

static uint64_t marvell_orion_sdio0_read(void *opaque, hwaddr offset, unsigned size)
{
    MARVELL_KIRKWOODState *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case 0x0 ... 0x1fc:
        res = s->marvell_orion_sdio0_reserved[offset >> 2];
        break;
    }
    return res;
}

static void marvell_orion_sdio0_write(void *opaque, hwaddr offset, uint64_t val, unsigned size)
{
    MARVELL_KIRKWOODState *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case 0x0 ... 0x1fc:
        s->marvell_orion_sdio0_reserved[offset >> 2] = val;
        break;
    }
    marvell_orion_sdio0_update(s);
}

static const MemoryRegionOps marvell_orion_sdio_ops0 = {
    .read = marvell_orion_sdio0_read,
    .write = marvell_orion_sdio0_write,
    .endianness = DEVICE_LITTLE_ENDIAN,
};

static void marvell_orion_sata0_update(void *opaque)
{
    /* MARVELL_KIRKWOODState *s = opaque; */
}

static uint64_t marvell_orion_sata0_read(void *opaque, hwaddr offset, unsigned size)
{
    MARVELL_KIRKWOODState *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case 0x0 ... 0x4ffc:
        res = s->marvell_orion_sata0_reserved[offset >> 2];
        break;
    }
    return res;
}

static void marvell_orion_sata0_write(void *opaque, hwaddr offset, uint64_t val, unsigned size)
{
    MARVELL_KIRKWOODState *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case 0x0 ... 0x4ffc:
        s->marvell_orion_sata0_reserved[offset >> 2] = val;
        break;
    }
    marvell_orion_sata0_update(s);
}

static const MemoryRegionOps marvell_orion_sata_ops0 = {
    .read = marvell_orion_sata0_read,
    .write = marvell_orion_sata0_write,
    .endianness = DEVICE_LITTLE_ENDIAN,
};

static void marvell_mv64xxx_i2c0_update(void *opaque)
{
    /* MARVELL_KIRKWOODState *s = opaque; */
}

static uint64_t marvell_mv64xxx_i2c0_read(void *opaque, hwaddr offset, unsigned size)
{
    MARVELL_KIRKWOODState *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case 0x0 ... 0x1c:
        res = s->marvell_mv64xxx_i2c0_reserved[offset >> 2];
        break;
    }
    return res;
}

static void marvell_mv64xxx_i2c0_write(void *opaque, hwaddr offset, uint64_t val, unsigned size)
{
    MARVELL_KIRKWOODState *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case 0x0 ... 0x1c:
        s->marvell_mv64xxx_i2c0_reserved[offset >> 2] = val;
        break;
    }
    marvell_mv64xxx_i2c0_update(s);
}

static const MemoryRegionOps marvell_mv64xxx_i2c_ops0 = {
    .read = marvell_mv64xxx_i2c0_read,
    .write = marvell_mv64xxx_i2c0_write,
    .endianness = DEVICE_LITTLE_ENDIAN,
};
    static void marvell_mv64xxx_i2c1_update(void *opaque)
{
    /* MARVELL_KIRKWOODState *s = opaque; */
}

static uint64_t marvell_mv64xxx_i2c1_read(void *opaque, hwaddr offset, unsigned size)
{
    MARVELL_KIRKWOODState *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case 0x0 ... 0x1c:
        res = s->marvell_mv64xxx_i2c1_reserved[offset >> 2];
        break;
    }
    return res;
}

static void marvell_mv64xxx_i2c1_write(void *opaque, hwaddr offset, uint64_t val, unsigned size)
{
    MARVELL_KIRKWOODState *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case 0x0 ... 0x1c:
        s->marvell_mv64xxx_i2c1_reserved[offset >> 2] = val;
        break;
    }
    marvell_mv64xxx_i2c1_update(s);
}

static const MemoryRegionOps marvell_mv64xxx_i2c_ops1 = {
    .read = marvell_mv64xxx_i2c1_read,
    .write = marvell_mv64xxx_i2c1_write,
    .endianness = DEVICE_LITTLE_ENDIAN,
};

static void marvell_orion_rtc0_update(void *opaque)
{
    /* MARVELL_KIRKWOODState *s = opaque; */
}

static uint64_t marvell_orion_rtc0_read(void *opaque, hwaddr offset, unsigned size)
{
    MARVELL_KIRKWOODState *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case 0x0 ... 0x1c:
        res = s->marvell_orion_rtc0_reserved[offset >> 2];
        break;
    }
    return res;
}

static void marvell_orion_rtc0_write(void *opaque, hwaddr offset, uint64_t val, unsigned size)
{
    MARVELL_KIRKWOODState *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case 0x0 ... 0x1c:
        s->marvell_orion_rtc0_reserved[offset >> 2] = val;
        break;
    }
    marvell_orion_rtc0_update(s);
}

static const MemoryRegionOps marvell_orion_rtc_ops0 = {
    .read = marvell_orion_rtc0_read,
    .write = marvell_orion_rtc0_write,
    .endianness = DEVICE_LITTLE_ENDIAN,
};

static void marvell_kirkwood_thermal0_update(void *opaque)
{
    /* MARVELL_KIRKWOODState *s = opaque; */
}

static uint64_t marvell_kirkwood_thermal0_read(void *opaque, hwaddr offset, unsigned size)
{
    MARVELL_KIRKWOODState *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case 0x0:
        res = s->marvell_kirkwood_thermal0_reserved[offset >> 2];
        break;
    }
    return res;
}

static void marvell_kirkwood_thermal0_write(void *opaque, hwaddr offset, uint64_t val, unsigned size)
{
    MARVELL_KIRKWOODState *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case 0x0:
        s->marvell_kirkwood_thermal0_reserved[offset >> 2] = val;
        break;
    }
    marvell_kirkwood_thermal0_update(s);
}

static const MemoryRegionOps marvell_kirkwood_thermal_ops0 = {
    .read = marvell_kirkwood_thermal0_read,
    .write = marvell_kirkwood_thermal0_write,
    .endianness = DEVICE_LITTLE_ENDIAN,
};

static void marvell_kirkwood_audio0_update(void *opaque)
{
    /* MARVELL_KIRKWOODState *s = opaque; */
}

static uint64_t marvell_kirkwood_audio0_read(void *opaque, hwaddr offset, unsigned size)
{
    MARVELL_KIRKWOODState *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case 0x0 ... 0x220c:
        res = s->marvell_kirkwood_audio0_reserved[offset >> 2];
        break;
    }
    return res;
}

static void marvell_kirkwood_audio0_write(void *opaque, hwaddr offset, uint64_t val, unsigned size)
{
    MARVELL_KIRKWOODState *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case 0x0 ... 0x220c:
        s->marvell_kirkwood_audio0_reserved[offset >> 2] = val;
        break;
    }
    marvell_kirkwood_audio0_update(s);
}

static const MemoryRegionOps marvell_kirkwood_audio_ops0 = {
    .read = marvell_kirkwood_audio0_read,
    .write = marvell_kirkwood_audio0_write,
    .endianness = DEVICE_LITTLE_ENDIAN,
};

static void marvell_mvebu_sata_phy0_update(void *opaque)
{
    /* MARVELL_KIRKWOODState *s = opaque; */
}

static uint64_t marvell_mvebu_sata_phy0_read(void *opaque, hwaddr offset, unsigned size)
{
    MARVELL_KIRKWOODState *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case 0x0 ... 0x330:
        res = s->marvell_mvebu_sata_phy0_reserved[offset >> 2];
        break;
    }
    return res;
}

static void marvell_mvebu_sata_phy0_write(void *opaque, hwaddr offset, uint64_t val, unsigned size)
{
    MARVELL_KIRKWOODState *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case 0x0 ... 0x330:
        s->marvell_mvebu_sata_phy0_reserved[offset >> 2] = val;
        break;
    }
    marvell_mvebu_sata_phy0_update(s);
}

static const MemoryRegionOps marvell_mvebu_sata_phy_ops0 = {
    .read = marvell_mvebu_sata_phy0_read,
    .write = marvell_mvebu_sata_phy0_write,
    .endianness = DEVICE_LITTLE_ENDIAN,
};
    static void marvell_mvebu_sata_phy1_update(void *opaque)
{
    /* MARVELL_KIRKWOODState *s = opaque; */
}

static uint64_t marvell_mvebu_sata_phy1_read(void *opaque, hwaddr offset, unsigned size)
{
    MARVELL_KIRKWOODState *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case 0x0 ... 0x330:
        res = s->marvell_mvebu_sata_phy1_reserved[offset >> 2];
        break;
    }
    return res;
}

static void marvell_mvebu_sata_phy1_write(void *opaque, hwaddr offset, uint64_t val, unsigned size)
{
    MARVELL_KIRKWOODState *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case 0x0 ... 0x330:
        s->marvell_mvebu_sata_phy1_reserved[offset >> 2] = val;
        break;
    }
    marvell_mvebu_sata_phy1_update(s);
}

static const MemoryRegionOps marvell_mvebu_sata_phy_ops1 = {
    .read = marvell_mvebu_sata_phy1_read,
    .write = marvell_mvebu_sata_phy1_write,
    .endianness = DEVICE_LITTLE_ENDIAN,
};

static void marvell_kirkwood_eth0_update(void *opaque)
{
    /* MARVELL_KIRKWOODState *s = opaque; */
}

static uint64_t marvell_kirkwood_eth0_read(void *opaque, hwaddr offset, unsigned size)
{
    MARVELL_KIRKWOODState *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case 0x0 ... 0x3ffc:
        res = s->marvell_kirkwood_eth0_reserved[offset >> 2];
        break;
    }
    return res;
}

static void marvell_kirkwood_eth0_write(void *opaque, hwaddr offset, uint64_t val, unsigned size)
{
    MARVELL_KIRKWOODState *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case 0x0 ... 0x3ffc:
        s->marvell_kirkwood_eth0_reserved[offset >> 2] = val;
        break;
    }
    marvell_kirkwood_eth0_update(s);
}

static const MemoryRegionOps marvell_kirkwood_eth_ops0 = {
    .read = marvell_kirkwood_eth0_read,
    .write = marvell_kirkwood_eth0_write,
    .endianness = DEVICE_LITTLE_ENDIAN,
};
    static void marvell_kirkwood_eth1_update(void *opaque)
{
    /* MARVELL_KIRKWOODState *s = opaque; */
}

static uint64_t marvell_kirkwood_eth1_read(void *opaque, hwaddr offset, unsigned size)
{
    MARVELL_KIRKWOODState *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case 0x0 ... 0x3ffc:
        res = s->marvell_kirkwood_eth1_reserved[offset >> 2];
        break;
    }
    return res;
}

static void marvell_kirkwood_eth1_write(void *opaque, hwaddr offset, uint64_t val, unsigned size)
{
    MARVELL_KIRKWOODState *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case 0x0 ... 0x3ffc:
        s->marvell_kirkwood_eth1_reserved[offset >> 2] = val;
        break;
    }
    marvell_kirkwood_eth1_update(s);
}

static const MemoryRegionOps marvell_kirkwood_eth_ops1 = {
    .read = marvell_kirkwood_eth1_read,
    .write = marvell_kirkwood_eth1_write,
    .endianness = DEVICE_LITTLE_ENDIAN,
};

static void marvell_orion_mdio0_update(void *opaque)
{
    /* MARVELL_KIRKWOODState *s = opaque; */
}

static uint64_t marvell_orion_mdio0_read(void *opaque, hwaddr offset, unsigned size)
{
    MARVELL_KIRKWOODState *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case 0x0 ... 0x80:
        res = s->marvell_orion_mdio0_reserved[offset >> 2];
        break;
    }
    return res;
}

static void marvell_orion_mdio0_write(void *opaque, hwaddr offset, uint64_t val, unsigned size)
{
    MARVELL_KIRKWOODState *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case 0x0 ... 0x80:
        s->marvell_orion_mdio0_reserved[offset >> 2] = val;
        break;
    }
    marvell_orion_mdio0_update(s);
}

static const MemoryRegionOps marvell_orion_mdio_ops0 = {
    .read = marvell_orion_mdio0_read,
    .write = marvell_orion_mdio0_write,
    .endianness = DEVICE_LITTLE_ENDIAN,
};

static void marvell_orion_xor0_update(void *opaque)
{
    /* MARVELL_KIRKWOODState *s = opaque; */
}

static uint64_t marvell_orion_xor0_read(void *opaque, hwaddr offset, unsigned size)
{
    MARVELL_KIRKWOODState *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case 0x0 ... 0xfc:
        res = s->marvell_orion_xor0_reserved[offset >> 2];
        break;
    }
    return res;
}

static void marvell_orion_xor0_write(void *opaque, hwaddr offset, uint64_t val, unsigned size)
{
    MARVELL_KIRKWOODState *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case 0x0 ... 0xfc:
        s->marvell_orion_xor0_reserved[offset >> 2] = val;
        break;
    }
    marvell_orion_xor0_update(s);
}

static const MemoryRegionOps marvell_orion_xor_ops0 = {
    .read = marvell_orion_xor0_read,
    .write = marvell_orion_xor0_write,
    .endianness = DEVICE_LITTLE_ENDIAN,
};
    static void marvell_orion_xor1_update(void *opaque)
{
    /* MARVELL_KIRKWOODState *s = opaque; */
}

static uint64_t marvell_orion_xor1_read(void *opaque, hwaddr offset, unsigned size)
{
    MARVELL_KIRKWOODState *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case 0x0 ... 0xfc:
        res = s->marvell_orion_xor1_reserved[offset >> 2];
        break;
    }
    return res;
}

static void marvell_orion_xor1_write(void *opaque, hwaddr offset, uint64_t val, unsigned size)
{
    MARVELL_KIRKWOODState *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case 0x0 ... 0xfc:
        s->marvell_orion_xor1_reserved[offset >> 2] = val;
        break;
    }
    marvell_orion_xor1_update(s);
}

static const MemoryRegionOps marvell_orion_xor_ops1 = {
    .read = marvell_orion_xor1_read,
    .write = marvell_orion_xor1_write,
    .endianness = DEVICE_LITTLE_ENDIAN,
};
    static void marvell_orion_xor2_update(void *opaque)
{
    /* MARVELL_KIRKWOODState *s = opaque; */
}

static uint64_t marvell_orion_xor2_read(void *opaque, hwaddr offset, unsigned size)
{
    MARVELL_KIRKWOODState *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case 0x0 ... 0xfc:
        res = s->marvell_orion_xor2_reserved[offset >> 2];
        break;
    }
    return res;
}

static void marvell_orion_xor2_write(void *opaque, hwaddr offset, uint64_t val, unsigned size)
{
    MARVELL_KIRKWOODState *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case 0x0 ... 0xfc:
        s->marvell_orion_xor2_reserved[offset >> 2] = val;
        break;
    }
    marvell_orion_xor2_update(s);
}

static const MemoryRegionOps marvell_orion_xor_ops2 = {
    .read = marvell_orion_xor2_read,
    .write = marvell_orion_xor2_write,
    .endianness = DEVICE_LITTLE_ENDIAN,
};
    static void marvell_orion_xor3_update(void *opaque)
{
    /* MARVELL_KIRKWOODState *s = opaque; */
}

static uint64_t marvell_orion_xor3_read(void *opaque, hwaddr offset, unsigned size)
{
    MARVELL_KIRKWOODState *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case 0x0 ... 0xfc:
        res = s->marvell_orion_xor3_reserved[offset >> 2];
        break;
    }
    return res;
}

static void marvell_orion_xor3_write(void *opaque, hwaddr offset, uint64_t val, unsigned size)
{
    MARVELL_KIRKWOODState *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case 0x0 ... 0xfc:
        s->marvell_orion_xor3_reserved[offset >> 2] = val;
        break;
    }
    marvell_orion_xor3_update(s);
}

static const MemoryRegionOps marvell_orion_xor_ops3 = {
    .read = marvell_orion_xor3_read,
    .write = marvell_orion_xor3_write,
    .endianness = DEVICE_LITTLE_ENDIAN,
};

static void marvell_orion_ehci0_update(void *opaque)
{
    /* MARVELL_KIRKWOODState *s = opaque; */
}

static uint64_t marvell_orion_ehci0_read(void *opaque, hwaddr offset, unsigned size)
{
    MARVELL_KIRKWOODState *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case 0x0 ... 0xffc:
        res = s->marvell_orion_ehci0_reserved[offset >> 2];
        break;
    }
    return res;
}

static void marvell_orion_ehci0_write(void *opaque, hwaddr offset, uint64_t val, unsigned size)
{
    MARVELL_KIRKWOODState *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case 0x0 ... 0xffc:
        s->marvell_orion_ehci0_reserved[offset >> 2] = val;
        break;
    }
    marvell_orion_ehci0_update(s);
}

static const MemoryRegionOps marvell_orion_ehci_ops0 = {
    .read = marvell_orion_ehci0_read,
    .write = marvell_orion_ehci0_write,
    .endianness = DEVICE_LITTLE_ENDIAN,
};

static void marvell_kirkwood_crypto0_update(void *opaque)
{
    /* MARVELL_KIRKWOODState *s = opaque; */
}

static uint64_t marvell_kirkwood_crypto0_read(void *opaque, hwaddr offset, unsigned size)
{
    MARVELL_KIRKWOODState *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case 0x0 ... 0xfffc:
        res = s->marvell_kirkwood_crypto0_reserved[offset >> 2];
        break;
    }
    return res;
}

static void marvell_kirkwood_crypto0_write(void *opaque, hwaddr offset, uint64_t val, unsigned size)
{
    MARVELL_KIRKWOODState *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case 0x0 ... 0xfffc:
        s->marvell_kirkwood_crypto0_reserved[offset >> 2] = val;
        break;
    }
    marvell_kirkwood_crypto0_update(s);
}

static const MemoryRegionOps marvell_kirkwood_crypto_ops0 = {
    .read = marvell_kirkwood_crypto0_read,
    .write = marvell_kirkwood_crypto0_write,
    .endianness = DEVICE_LITTLE_ENDIAN,
};

static void marvell_orion_wdt0_update(void *opaque)
{
    /* MARVELL_KIRKWOODState *s = opaque; */
}

static uint64_t marvell_orion_wdt0_read(void *opaque, hwaddr offset, unsigned size)
{
    MARVELL_KIRKWOODState *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case 0x0 ... 0x24:
        res = s->marvell_orion_wdt0_reserved[offset >> 2];
        break;
    }
    return res;
}

static void marvell_orion_wdt0_write(void *opaque, hwaddr offset, uint64_t val, unsigned size)
{
    MARVELL_KIRKWOODState *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case 0x0 ... 0x24:
        s->marvell_orion_wdt0_reserved[offset >> 2] = val;
        break;
    }
    marvell_orion_wdt0_update(s);
}

static const MemoryRegionOps marvell_orion_wdt_ops0 = {
    .read = marvell_orion_wdt0_read,
    .write = marvell_orion_wdt0_write,
    .endianness = DEVICE_LITTLE_ENDIAN,
};
    static void marvell_orion_wdt1_update(void *opaque)
{
    /* MARVELL_KIRKWOODState *s = opaque; */
}

static uint64_t marvell_orion_wdt1_read(void *opaque, hwaddr offset, unsigned size)
{
    MARVELL_KIRKWOODState *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case 0x0:
        res = s->marvell_orion_wdt1_reserved[offset >> 2];
        break;
    }
    return res;
}

static void marvell_orion_wdt1_write(void *opaque, hwaddr offset, uint64_t val, unsigned size)
{
    MARVELL_KIRKWOODState *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case 0x0:
        s->marvell_orion_wdt1_reserved[offset >> 2] = val;
        break;
    }
    marvell_orion_wdt1_update(s);
}

static const MemoryRegionOps marvell_orion_wdt_ops1 = {
    .read = marvell_orion_wdt1_read,
    .write = marvell_orion_wdt1_write,
    .endianness = DEVICE_LITTLE_ENDIAN,
};

static void marvell_kirkwood_cache0_update(void *opaque)
{
    /* MARVELL_KIRKWOODState *s = opaque; */
}

static uint64_t marvell_kirkwood_cache0_read(void *opaque, hwaddr offset, unsigned size)
{
    MARVELL_KIRKWOODState *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case 0x0:
        res = s->marvell_kirkwood_cache0_reserved[offset >> 2];
        break;
    }
    return res;
}

static void marvell_kirkwood_cache0_write(void *opaque, hwaddr offset, uint64_t val, unsigned size)
{
    MARVELL_KIRKWOODState *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case 0x0:
        s->marvell_kirkwood_cache0_reserved[offset >> 2] = val;
        break;
    }
    marvell_kirkwood_cache0_update(s);
}

static const MemoryRegionOps marvell_kirkwood_cache_ops0 = {
    .read = marvell_kirkwood_cache0_read,
    .write = marvell_kirkwood_cache0_write,
    .endianness = DEVICE_LITTLE_ENDIAN,
};

static void marvell_kirkwood_gating_clock0_update(void *opaque)
{
    /* MARVELL_KIRKWOODState *s = opaque; */
}

static uint64_t marvell_kirkwood_gating_clock0_read(void *opaque, hwaddr offset, unsigned size)
{
    MARVELL_KIRKWOODState *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case 0x0:
        res = s->marvell_kirkwood_gating_clock0_reserved[offset >> 2];
        break;
    }
    return res;
}

static void marvell_kirkwood_gating_clock0_write(void *opaque, hwaddr offset, uint64_t val, unsigned size)
{
    MARVELL_KIRKWOODState *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case 0x0:
        s->marvell_kirkwood_gating_clock0_reserved[offset >> 2] = val;
        break;
    }
    marvell_kirkwood_gating_clock0_update(s);
}

static const MemoryRegionOps marvell_kirkwood_gating_clock_ops0 = {
    .read = marvell_kirkwood_gating_clock0_read,
    .write = marvell_kirkwood_gating_clock0_write,
    .endianness = DEVICE_LITTLE_ENDIAN,
};

static void marvell_orion_system_controller0_update(void *opaque)
{
    /* MARVELL_KIRKWOODState *s = opaque; */
}

static uint64_t marvell_orion_system_controller0_read(void *opaque, hwaddr offset, unsigned size)
{
    MARVELL_KIRKWOODState *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case 0x0 ... 0x11c:
        res = s->marvell_orion_system_controller0_reserved[offset >> 2];
        break;
    }
    return res;
}

static void marvell_orion_system_controller0_write(void *opaque, hwaddr offset, uint64_t val, unsigned size)
{
    MARVELL_KIRKWOODState *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case 0x0 ... 0x11c:
        s->marvell_orion_system_controller0_reserved[offset >> 2] = val;
        break;
    }
    marvell_orion_system_controller0_update(s);
}

static const MemoryRegionOps marvell_orion_system_controller_ops0 = {
    .read = marvell_orion_system_controller0_read,
    .write = marvell_orion_system_controller0_write,
    .endianness = DEVICE_LITTLE_ENDIAN,
};

static void marvell_mbus_controller0_update(void *opaque)
{
    /* MARVELL_KIRKWOODState *s = opaque; */
}

static uint64_t marvell_mbus_controller0_read(void *opaque, hwaddr offset, unsigned size)
{
    MARVELL_KIRKWOODState *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case 0x0 ... 0x7c:
        res = s->marvell_mbus_controller0_reserved[offset >> 2];
        break;
    }
    return res;
}

static void marvell_mbus_controller0_write(void *opaque, hwaddr offset, uint64_t val, unsigned size)
{
    MARVELL_KIRKWOODState *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case 0x0 ... 0x7c:
        s->marvell_mbus_controller0_reserved[offset >> 2] = val;
        break;
    }
    marvell_mbus_controller0_update(s);
}

static const MemoryRegionOps marvell_mbus_controller_ops0 = {
    .read = marvell_mbus_controller0_read,
    .write = marvell_mbus_controller0_write,
    .endianness = DEVICE_LITTLE_ENDIAN,
};
    static void marvell_mbus_controller1_update(void *opaque)
{
    /* MARVELL_KIRKWOODState *s = opaque; */
}

static uint64_t marvell_mbus_controller1_read(void *opaque, hwaddr offset, unsigned size)
{
    MARVELL_KIRKWOODState *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case 0x0 ... 0x1c:
        res = s->marvell_mbus_controller1_reserved[offset >> 2];
        break;
    }
    return res;
}

static void marvell_mbus_controller1_write(void *opaque, hwaddr offset, uint64_t val, unsigned size)
{
    MARVELL_KIRKWOODState *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case 0x0 ... 0x1c:
        s->marvell_mbus_controller1_reserved[offset >> 2] = val;
        break;
    }
    marvell_mbus_controller1_update(s);
}

static const MemoryRegionOps marvell_mbus_controller_ops1 = {
    .read = marvell_mbus_controller1_read,
    .write = marvell_mbus_controller1_write,
    .endianness = DEVICE_LITTLE_ENDIAN,
};

static void marvell_orion_gpio0_update(void *opaque)
{
    /* MARVELL_KIRKWOODState *s = opaque; */
}

static uint64_t marvell_orion_gpio0_read(void *opaque, hwaddr offset, unsigned size)
{
    MARVELL_KIRKWOODState *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case 0x0 ... 0x3c:
        res = s->marvell_orion_gpio0_reserved[offset >> 2];
        break;
    }
    return res;
}

static void marvell_orion_gpio0_write(void *opaque, hwaddr offset, uint64_t val, unsigned size)
{
    MARVELL_KIRKWOODState *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case 0x0 ... 0x3c:
        s->marvell_orion_gpio0_reserved[offset >> 2] = val;
        break;
    }
    marvell_orion_gpio0_update(s);
}

static const MemoryRegionOps marvell_orion_gpio_ops0 = {
    .read = marvell_orion_gpio0_read,
    .write = marvell_orion_gpio0_write,
    .endianness = DEVICE_LITTLE_ENDIAN,
};
    static void marvell_orion_gpio1_update(void *opaque)
{
    /* MARVELL_KIRKWOODState *s = opaque; */
}

static uint64_t marvell_orion_gpio1_read(void *opaque, hwaddr offset, unsigned size)
{
    MARVELL_KIRKWOODState *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case 0x0 ... 0x3c:
        res = s->marvell_orion_gpio1_reserved[offset >> 2];
        break;
    }
    return res;
}

static void marvell_orion_gpio1_write(void *opaque, hwaddr offset, uint64_t val, unsigned size)
{
    MARVELL_KIRKWOODState *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case 0x0 ... 0x3c:
        s->marvell_orion_gpio1_reserved[offset >> 2] = val;
        break;
    }
    marvell_orion_gpio1_update(s);
}

static const MemoryRegionOps marvell_orion_gpio_ops1 = {
    .read = marvell_orion_gpio1_read,
    .write = marvell_orion_gpio1_write,
    .endianness = DEVICE_LITTLE_ENDIAN,
};

static void marvell_orion_spi0_update(void *opaque)
{
    /* MARVELL_KIRKWOODState *s = opaque; */
}

static uint64_t marvell_orion_spi0_read(void *opaque, hwaddr offset, unsigned size)
{
    MARVELL_KIRKWOODState *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case 0x0 ... 0x24:
        res = s->marvell_orion_spi0_reserved[offset >> 2];
        break;
    }
    return res;
}

static void marvell_orion_spi0_write(void *opaque, hwaddr offset, uint64_t val, unsigned size)
{
    MARVELL_KIRKWOODState *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case 0x0 ... 0x24:
        s->marvell_orion_spi0_reserved[offset >> 2] = val;
        break;
    }
    marvell_orion_spi0_update(s);
}

static const MemoryRegionOps marvell_orion_spi_ops0 = {
    .read = marvell_orion_spi0_read,
    .write = marvell_orion_spi0_write,
    .endianness = DEVICE_LITTLE_ENDIAN,
};

static void marvell_kirkwood_core_clock0_update(void *opaque)
{
    /* MARVELL_KIRKWOODState *s = opaque; */
}

static uint64_t marvell_kirkwood_core_clock0_read(void *opaque, hwaddr offset, unsigned size)
{
    MARVELL_KIRKWOODState *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case 0x0:
        res = s->marvell_kirkwood_core_clock0_reserved[offset >> 2];
        break;
    }
    return res;
}

static void marvell_kirkwood_core_clock0_write(void *opaque, hwaddr offset, uint64_t val, unsigned size)
{
    MARVELL_KIRKWOODState *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case 0x0:
        s->marvell_kirkwood_core_clock0_reserved[offset >> 2] = val;
        break;
    }
    marvell_kirkwood_core_clock0_update(s);
}

static const MemoryRegionOps marvell_kirkwood_core_clock_ops0 = {
    .read = marvell_kirkwood_core_clock0_read,
    .write = marvell_kirkwood_core_clock0_write,
    .endianness = DEVICE_LITTLE_ENDIAN,
};

static void marvell_88f6282_pinctrl0_update(void *opaque)
{
    /* MARVELL_KIRKWOODState *s = opaque; */
}

static uint64_t marvell_88f6282_pinctrl0_read(void *opaque, hwaddr offset, unsigned size)
{
    MARVELL_KIRKWOODState *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case 0x0 ... 0x1c:
        res = s->marvell_88f6282_pinctrl0_reserved[offset >> 2];
        break;
    }
    return res;
}

static void marvell_88f6282_pinctrl0_write(void *opaque, hwaddr offset, uint64_t val, unsigned size)
{
    MARVELL_KIRKWOODState *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case 0x0 ... 0x1c:
        s->marvell_88f6282_pinctrl0_reserved[offset >> 2] = val;
        break;
    }
    marvell_88f6282_pinctrl0_update(s);
}

static const MemoryRegionOps marvell_88f6282_pinctrl_ops0 = {
    .read = marvell_88f6282_pinctrl0_read,
    .write = marvell_88f6282_pinctrl0_write,
    .endianness = DEVICE_LITTLE_ENDIAN,
};

static void marvell_kirkwood_mbus0_update(void *opaque)
{
    /* MARVELL_KIRKWOODState *s = opaque; */
}

static uint64_t marvell_kirkwood_mbus0_read(void *opaque, hwaddr offset, unsigned size)
{
    MARVELL_KIRKWOODState *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case 0x0 ... 0xffffc:
        res = s->marvell_kirkwood_mbus0_reserved[offset >> 2];
        break;
    }
    return res;
}

static void marvell_kirkwood_mbus0_write(void *opaque, hwaddr offset, uint64_t val, unsigned size)
{
    MARVELL_KIRKWOODState *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case 0x0 ... 0xffffc:
        s->marvell_kirkwood_mbus0_reserved[offset >> 2] = val;
        break;
    }
    marvell_kirkwood_mbus0_update(s);
}

static const MemoryRegionOps marvell_kirkwood_mbus_ops0 = {
    .read = marvell_kirkwood_mbus0_read,
    .write = marvell_kirkwood_mbus0_write,
    .endianness = DEVICE_LITTLE_ENDIAN,
};

static void marvell_kirkwood_pcie0_update(void *opaque)
{
    /* MARVELL_KIRKWOODState *s = opaque; */
}

static uint64_t marvell_kirkwood_pcie0_read(void *opaque, hwaddr offset, unsigned size)
{
    MARVELL_KIRKWOODState *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case 0x0 ... 0x1ffc:
        res = s->marvell_kirkwood_pcie0_reserved[offset >> 2];
        break;
    }
    return res;
}

static void marvell_kirkwood_pcie0_write(void *opaque, hwaddr offset, uint64_t val, unsigned size)
{
    MARVELL_KIRKWOODState *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case 0x0 ... 0x1ffc:
        s->marvell_kirkwood_pcie0_reserved[offset >> 2] = val;
        break;
    }
    marvell_kirkwood_pcie0_update(s);
}

static const MemoryRegionOps marvell_kirkwood_pcie_ops0 = {
    .read = marvell_kirkwood_pcie0_read,
    .write = marvell_kirkwood_pcie0_write,
    .endianness = DEVICE_LITTLE_ENDIAN,
};
    static void marvell_kirkwood_pcie1_update(void *opaque)
{
    /* MARVELL_KIRKWOODState *s = opaque; */
}

static uint64_t marvell_kirkwood_pcie1_read(void *opaque, hwaddr offset, unsigned size)
{
    MARVELL_KIRKWOODState *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case 0x0 ... 0x1ffc:
        res = s->marvell_kirkwood_pcie1_reserved[offset >> 2];
        break;
    }
    return res;
}

static void marvell_kirkwood_pcie1_write(void *opaque, hwaddr offset, uint64_t val, unsigned size)
{
    MARVELL_KIRKWOODState *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case 0x0 ... 0x1ffc:
        s->marvell_kirkwood_pcie1_reserved[offset >> 2] = val;
        break;
    }
    marvell_kirkwood_pcie1_update(s);
}

static const MemoryRegionOps marvell_kirkwood_pcie_ops1 = {
    .read = marvell_kirkwood_pcie1_read,
    .write = marvell_kirkwood_pcie1_write,
    .endianness = DEVICE_LITTLE_ENDIAN,
};

static void mmio_sram0_update(void *opaque)
{
    /* MARVELL_KIRKWOODState *s = opaque; */
}

static uint64_t mmio_sram0_read(void *opaque, hwaddr offset, unsigned size)
{
    MARVELL_KIRKWOODState *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case 0x0 ... 0x7fc:
        res = s->mmio_sram0_reserved[offset >> 2];
        break;
    }
    return res;
}

static void mmio_sram0_write(void *opaque, hwaddr offset, uint64_t val, unsigned size)
{
    MARVELL_KIRKWOODState *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case 0x0 ... 0x7fc:
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


static void marvell_kirkwood_reset(void *opaque)
{
    MARVELL_KIRKWOODState *s = opaque;
    
    s->plxtech_nand_nas782x0_reserved[0x0 >> 2] = 0x40;
}

static void marvell_kirkwood_init(MachineState *machine)
{
    MARVELL_KIRKWOODState *s = g_new0(MARVELL_KIRKWOODState, 1);
    Error *err = NULL;
    static struct arm_boot_info binfo;
    
    s->cpu = ARM_CPU(object_new(machine->cpu_type));
    object_property_set_bool(OBJECT(s->cpu), true, "realized", &err);
    
    memory_region_allocate_system_memory(&s->ram0, OBJECT(machine), "ram0", 0x8000000);
    memory_region_add_subregion_overlap(get_system_memory(), 0x0, &s->ram0, 0);
    
    object_initialize(&s->marvell_orion_intc0, sizeof(s->marvell_orion_intc0), TYPE_MARVELL_ORION_INTC);
    qdev_set_parent_bus(DEVICE(&s->marvell_orion_intc0), sysbus_get_default());
    object_property_set_bool(OBJECT(&s->marvell_orion_intc0), true, "realized", &err);
    sysbus_mmio_map(SYS_BUS_DEVICE(&s->marvell_orion_intc0), 0, 0xf1020200);
    object_initialize(&s->marvell_orion_intc1, sizeof(s->marvell_orion_intc1), TYPE_MARVELL_ORION_INTC);
    qdev_set_parent_bus(DEVICE(&s->marvell_orion_intc1), sysbus_get_default());
    object_property_set_bool(OBJECT(&s->marvell_orion_intc1), true, "realized", &err);
    sysbus_mmio_map(SYS_BUS_DEVICE(&s->marvell_orion_intc1), 0, 0xf1020210);
    object_initialize(&s->marvell_orion_bridge_intc0, sizeof(s->marvell_orion_bridge_intc0), TYPE_MARVELL_ORION_BRIDGE_INTC);
    qdev_set_parent_bus(DEVICE(&s->marvell_orion_bridge_intc0), sysbus_get_default());
    object_property_set_bool(OBJECT(&s->marvell_orion_bridge_intc0), true, "realized", &err);
    sysbus_mmio_map(SYS_BUS_DEVICE(&s->marvell_orion_bridge_intc0), 0, 0xf1020110);
    
    qdev_connect_gpio_out(DEVICE(&s->marvell_orion_intc0), 0, qdev_get_gpio_in(DEVICE(s->cpu), ARM_CPU_IRQ));
    qdev_connect_gpio_out(DEVICE(&s->marvell_orion_intc1), 0, qdev_get_gpio_in(DEVICE(s->cpu), ARM_CPU_IRQ));
    qdev_connect_gpio_out(DEVICE(&s->marvell_orion_bridge_intc0), 0, qdev_get_gpio_in(DEVICE(&s->marvell_orion_intc0), 1));
    
    object_initialize(&s->timer0, sizeof(s->timer0), TYPE_MARVELL_ORION_TIMER);
    qdev_set_parent_bus(DEVICE(&s->timer0), sysbus_get_default());
    object_property_set_bool(OBJECT(&s->timer0), true, "realized", &err);
    sysbus_mmio_map(SYS_BUS_DEVICE(&s->timer0), 0, 0xf1020300);
    
    qdev_connect_gpio_out(DEVICE(&s->timer0), 0, qdev_get_gpio_in(DEVICE(&s->marvell_orion_bridge_intc0), 1));
    qdev_connect_gpio_out(DEVICE(&s->timer0), 1, qdev_get_gpio_in(DEVICE(&s->marvell_orion_bridge_intc0), 2));
    
    serial_mm_init(get_system_memory(), 0xf1012100, 2, qdev_get_gpio_in(DEVICE(&s->marvell_orion_intc1), 2), 115200, serial_hd(0), DEVICE_LITTLE_ENDIAN);
    serial_mm_init(get_system_memory(), 0xf1012000, 2, qdev_get_gpio_in(DEVICE(&s->marvell_orion_intc1), 1), 115200, serial_hd(1), DEVICE_LITTLE_ENDIAN);
    
    
    
    memory_region_init_io(&s->plxtech_nand_nas782x0_mmio, NULL, &plxtech_nand_nas782x_ops0, s, TYPE_MARVELL_KIRKWOOD, 0x400);
    memory_region_add_subregion_overlap(get_system_memory(), 0xf4000000, &s->plxtech_nand_nas782x0_mmio, 0);
    memory_region_init_io(&s->marvell_orion_sdio0_mmio, NULL, &marvell_orion_sdio_ops0, s, TYPE_MARVELL_KIRKWOOD, 0x200);
    memory_region_add_subregion_overlap(get_system_memory(), 0xf1090000, &s->marvell_orion_sdio0_mmio, 0);
    memory_region_init_io(&s->marvell_orion_sata0_mmio, NULL, &marvell_orion_sata_ops0, s, TYPE_MARVELL_KIRKWOOD, 0x5000);
    memory_region_add_subregion_overlap(get_system_memory(), 0xf1080000, &s->marvell_orion_sata0_mmio, 0);
    memory_region_init_io(&s->marvell_mv64xxx_i2c0_mmio, NULL, &marvell_mv64xxx_i2c_ops0, s, TYPE_MARVELL_KIRKWOOD, 0x20);
    memory_region_add_subregion_overlap(get_system_memory(), 0xf1011000, &s->marvell_mv64xxx_i2c0_mmio, 0);
    memory_region_init_io(&s->marvell_mv64xxx_i2c1_mmio, NULL, &marvell_mv64xxx_i2c_ops1, s, TYPE_MARVELL_KIRKWOOD, 0x20);
    memory_region_add_subregion_overlap(get_system_memory(), 0xf1011100, &s->marvell_mv64xxx_i2c1_mmio, 0);
    memory_region_init_io(&s->marvell_orion_rtc0_mmio, NULL, &marvell_orion_rtc_ops0, s, TYPE_MARVELL_KIRKWOOD, 0x20);
    memory_region_add_subregion_overlap(get_system_memory(), 0xf1010300, &s->marvell_orion_rtc0_mmio, 0);
    memory_region_init_io(&s->marvell_kirkwood_thermal0_mmio, NULL, &marvell_kirkwood_thermal_ops0, s, TYPE_MARVELL_KIRKWOOD, 0x4);
    memory_region_add_subregion_overlap(get_system_memory(), 0xf1010078, &s->marvell_kirkwood_thermal0_mmio, 0);
    memory_region_init_io(&s->marvell_kirkwood_audio0_mmio, NULL, &marvell_kirkwood_audio_ops0, s, TYPE_MARVELL_KIRKWOOD, 0x2210);
    memory_region_add_subregion_overlap(get_system_memory(), 0xf10a0000, &s->marvell_kirkwood_audio0_mmio, 0);
    memory_region_init_io(&s->marvell_mvebu_sata_phy0_mmio, NULL, &marvell_mvebu_sata_phy_ops0, s, TYPE_MARVELL_KIRKWOOD, 0x334);
    memory_region_add_subregion_overlap(get_system_memory(), 0xf1082000, &s->marvell_mvebu_sata_phy0_mmio, 0);
    memory_region_init_io(&s->marvell_mvebu_sata_phy1_mmio, NULL, &marvell_mvebu_sata_phy_ops1, s, TYPE_MARVELL_KIRKWOOD, 0x334);
    memory_region_add_subregion_overlap(get_system_memory(), 0xf1084000, &s->marvell_mvebu_sata_phy1_mmio, 0);
    memory_region_init_io(&s->marvell_kirkwood_eth0_mmio, NULL, &marvell_kirkwood_eth_ops0, s, TYPE_MARVELL_KIRKWOOD, 0x4000);
    memory_region_add_subregion_overlap(get_system_memory(), 0xf1072000, &s->marvell_kirkwood_eth0_mmio, 0);
    memory_region_init_io(&s->marvell_kirkwood_eth1_mmio, NULL, &marvell_kirkwood_eth_ops1, s, TYPE_MARVELL_KIRKWOOD, 0x4000);
    memory_region_add_subregion_overlap(get_system_memory(), 0xf1076000, &s->marvell_kirkwood_eth1_mmio, 0);
    memory_region_init_io(&s->marvell_orion_mdio0_mmio, NULL, &marvell_orion_mdio_ops0, s, TYPE_MARVELL_KIRKWOOD, 0x84);
    memory_region_add_subregion_overlap(get_system_memory(), 0xf1072004, &s->marvell_orion_mdio0_mmio, 0);
    memory_region_init_io(&s->marvell_orion_xor0_mmio, NULL, &marvell_orion_xor_ops0, s, TYPE_MARVELL_KIRKWOOD, 0x100);
    memory_region_add_subregion_overlap(get_system_memory(), 0xf1060800, &s->marvell_orion_xor0_mmio, 0);
    memory_region_init_io(&s->marvell_orion_xor1_mmio, NULL, &marvell_orion_xor_ops1, s, TYPE_MARVELL_KIRKWOOD, 0x100);
    memory_region_add_subregion_overlap(get_system_memory(), 0xf1060900, &s->marvell_orion_xor1_mmio, 0);
    memory_region_init_io(&s->marvell_orion_xor2_mmio, NULL, &marvell_orion_xor_ops2, s, TYPE_MARVELL_KIRKWOOD, 0x100);
    memory_region_add_subregion_overlap(get_system_memory(), 0xf1060a00, &s->marvell_orion_xor2_mmio, 0);
    memory_region_init_io(&s->marvell_orion_xor3_mmio, NULL, &marvell_orion_xor_ops3, s, TYPE_MARVELL_KIRKWOOD, 0x100);
    memory_region_add_subregion_overlap(get_system_memory(), 0xf1060b00, &s->marvell_orion_xor3_mmio, 0);
    memory_region_init_io(&s->marvell_orion_ehci0_mmio, NULL, &marvell_orion_ehci_ops0, s, TYPE_MARVELL_KIRKWOOD, 0x1000);
    memory_region_add_subregion_overlap(get_system_memory(), 0xf1050000, &s->marvell_orion_ehci0_mmio, 0);
    memory_region_init_io(&s->marvell_kirkwood_crypto0_mmio, NULL, &marvell_kirkwood_crypto_ops0, s, TYPE_MARVELL_KIRKWOOD, 0x10000);
    memory_region_add_subregion_overlap(get_system_memory(), 0xf1030000, &s->marvell_kirkwood_crypto0_mmio, 0);
    memory_region_init_io(&s->marvell_orion_wdt0_mmio, NULL, &marvell_orion_wdt_ops0, s, TYPE_MARVELL_KIRKWOOD, 0x28);
    memory_region_add_subregion_overlap(get_system_memory(), 0xf1020300, &s->marvell_orion_wdt0_mmio, -1);
    memory_region_init_io(&s->marvell_orion_wdt1_mmio, NULL, &marvell_orion_wdt_ops1, s, TYPE_MARVELL_KIRKWOOD, 0x4);
    memory_region_add_subregion_overlap(get_system_memory(), 0xf1020108, &s->marvell_orion_wdt1_mmio, 0);
    memory_region_init_io(&s->marvell_kirkwood_cache0_mmio, NULL, &marvell_kirkwood_cache_ops0, s, TYPE_MARVELL_KIRKWOOD, 0x4);
    memory_region_add_subregion_overlap(get_system_memory(), 0xf1020128, &s->marvell_kirkwood_cache0_mmio, 0);
    memory_region_init_io(&s->marvell_kirkwood_gating_clock0_mmio, NULL, &marvell_kirkwood_gating_clock_ops0, s, TYPE_MARVELL_KIRKWOOD, 0x4);
    memory_region_add_subregion_overlap(get_system_memory(), 0xf102011c, &s->marvell_kirkwood_gating_clock0_mmio, 0);
    memory_region_init_io(&s->marvell_orion_system_controller0_mmio, NULL, &marvell_orion_system_controller_ops0, s, TYPE_MARVELL_KIRKWOOD, 0x120);
    memory_region_add_subregion_overlap(get_system_memory(), 0xf1020000, &s->marvell_orion_system_controller0_mmio, -1);
    memory_region_init_io(&s->marvell_mbus_controller0_mmio, NULL, &marvell_mbus_controller_ops0, s, TYPE_MARVELL_KIRKWOOD, 0x80);
    memory_region_add_subregion_overlap(get_system_memory(), 0xf1020000, &s->marvell_mbus_controller0_mmio, 0);
    memory_region_init_io(&s->marvell_mbus_controller1_mmio, NULL, &marvell_mbus_controller_ops1, s, TYPE_MARVELL_KIRKWOOD, 0x20);
    memory_region_add_subregion_overlap(get_system_memory(), 0xf1001500, &s->marvell_mbus_controller1_mmio, 0);
    memory_region_init_io(&s->marvell_orion_gpio0_mmio, NULL, &marvell_orion_gpio_ops0, s, TYPE_MARVELL_KIRKWOOD, 0x40);
    memory_region_add_subregion_overlap(get_system_memory(), 0xf1010100, &s->marvell_orion_gpio0_mmio, 0);
    memory_region_init_io(&s->marvell_orion_gpio1_mmio, NULL, &marvell_orion_gpio_ops1, s, TYPE_MARVELL_KIRKWOOD, 0x40);
    memory_region_add_subregion_overlap(get_system_memory(), 0xf1010140, &s->marvell_orion_gpio1_mmio, 0);
    memory_region_init_io(&s->marvell_orion_spi0_mmio, NULL, &marvell_orion_spi_ops0, s, TYPE_MARVELL_KIRKWOOD, 0x28);
    memory_region_add_subregion_overlap(get_system_memory(), 0xf1010600, &s->marvell_orion_spi0_mmio, 0);
    memory_region_init_io(&s->marvell_kirkwood_core_clock0_mmio, NULL, &marvell_kirkwood_core_clock_ops0, s, TYPE_MARVELL_KIRKWOOD, 0x4);
    memory_region_add_subregion_overlap(get_system_memory(), 0xf1010030, &s->marvell_kirkwood_core_clock0_mmio, 0);
    memory_region_init_io(&s->marvell_88f6282_pinctrl0_mmio, NULL, &marvell_88f6282_pinctrl_ops0, s, TYPE_MARVELL_KIRKWOOD, 0x20);
    memory_region_add_subregion_overlap(get_system_memory(), 0xf1010000, &s->marvell_88f6282_pinctrl0_mmio, 0);
    memory_region_init_io(&s->marvell_kirkwood_mbus0_mmio, NULL, &marvell_kirkwood_mbus_ops0, s, TYPE_MARVELL_KIRKWOOD, 0x100000);
    memory_region_add_subregion_overlap(get_system_memory(), 0xf2000000, &s->marvell_kirkwood_mbus0_mmio, 0);
    memory_region_init_io(&s->marvell_kirkwood_pcie0_mmio, NULL, &marvell_kirkwood_pcie_ops0, s, TYPE_MARVELL_KIRKWOOD, 0x2000);
    memory_region_add_subregion_overlap(get_system_memory(), 0xf1040000, &s->marvell_kirkwood_pcie0_mmio, 0);
    memory_region_init_io(&s->marvell_kirkwood_pcie1_mmio, NULL, &marvell_kirkwood_pcie_ops1, s, TYPE_MARVELL_KIRKWOOD, 0x2000);
    memory_region_add_subregion_overlap(get_system_memory(), 0xf1044000, &s->marvell_kirkwood_pcie1_mmio, 0);
    memory_region_init_io(&s->mmio_sram0_mmio, NULL, &mmio_sram_ops0, s, TYPE_MARVELL_KIRKWOOD, 0x800);
    memory_region_add_subregion_overlap(get_system_memory(), 0xf5000000, &s->mmio_sram0_mmio, 0);
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
    mc->default_ram_size = 128 * MiB;
    mc->default_cpu_type = ARM_CPU_TYPE_NAME("feroceon");
    mc->ignore_memory_transaction_failures = false;
}

DEFINE_MACHINE("marvell_kirkwood", marvell_kirkwood_machine_init)
