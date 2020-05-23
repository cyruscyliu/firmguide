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
#include "hw/intc/ralink_rt2880_intc.h"
#include "hw/char/serial.h"
#include "hw/char/serial.h"
#include "hw/char/serial.h"

#define TYPE_MEDIATEK_MT7628AN_SOC "mediatek_mt7628an_soc"
#define MEDIATEK_MT7628AN_SOC(obj) \
    OBJECT_CHECK(MEDIATEK_MT7628AN_SOCState, (obj), TYPE_MEDIATEK_MT7628AN_SOC)

typedef struct MEDIATEK_MT7628AN_SOCState {
    MIPSCPU *cpu;
    RALINK_RT2880_INTCState ralink_rt2880_intc0;
    MemoryRegion flash;
    MemoryRegion ram0;
    MemoryRegion mediatek_mt7628_wmac0_mmio;
    MemoryRegion mediatek_mt7620_pci0_mmio;
    MemoryRegion mediatek_mt7620_pci1_mmio;
    MemoryRegion ralink_rt3050_esw0_mmio;
    MemoryRegion ralink_rt5350_eth0_mmio;
    MemoryRegion generic_ohci0_mmio;
    MemoryRegion generic_ehci0_mmio;
    MemoryRegion ralink_mt7620_sdhci0_mmio;
    MemoryRegion mediatek_mt7620_usbphy0_mmio;
    MemoryRegion ralink_rt3883_gdma0_mmio;
    MemoryRegion ralink_mt7620a_pcm0_mmio;
    MemoryRegion mediatek_mt7628_pwm0_mmio;
    MemoryRegion ralink_mt7621_spi0_mmio;
    MemoryRegion mediatek_mt7628_i2s0_mmio;
    MemoryRegion mediatek_mt7621_i2c0_mmio;
    MemoryRegion mtk_mt7621_gpio0_mmio;
    MemoryRegion ralink_rt3050_memc0_mmio;
    MemoryRegion mediatek_mt7621_wdt0_mmio;
    MemoryRegion ralink_mt7620a_sysc0_mmio;
    uint32_t mediatek_mt7628_wmac0_reserved[0x100000 >> 2];
    uint32_t mediatek_mt7620_pci0_reserved[0x100 >> 2];
    uint32_t mediatek_mt7620_pci1_reserved[0x100 >> 2];
    uint32_t ralink_rt3050_esw0_reserved[0x8000 >> 2];
    uint32_t ralink_rt5350_eth0_reserved[0x10000 >> 2];
    uint32_t generic_ohci0_reserved[0x1000 >> 2];
    uint32_t generic_ehci0_reserved[0x1000 >> 2];
    uint32_t ralink_mt7620_sdhci0_reserved[0x4000 >> 2];
    uint32_t mediatek_mt7620_usbphy0_reserved[0x1000 >> 2];
    uint32_t ralink_rt3883_gdma0_reserved[0x800 >> 2];
    uint32_t ralink_mt7620a_pcm0_reserved[0x800 >> 2];
    uint32_t mediatek_mt7628_pwm0_reserved[0x1000 >> 2];
    uint32_t ralink_mt7621_spi0_reserved[0x100 >> 2];
    uint32_t mediatek_mt7628_i2s0_reserved[0x100 >> 2];
    uint32_t mediatek_mt7621_i2c0_reserved[0x100 >> 2];
    uint32_t mtk_mt7621_gpio0_reserved[0x100 >> 2];
    uint32_t ralink_rt3050_memc0_reserved[0x100 >> 2];
    uint32_t mediatek_mt7621_wdt0_reserved[0x30 >> 2];
    uint32_t ralink_mt7620a_sysc0_reserved[0x100 >> 2];
} MEDIATEK_MT7628AN_SOCState;

static void mediatek_mt7628_wmac0_update(void *opaque)
{
    /* MEDIATEK_MT7628AN_SOCState *s = opaque; */
}

static uint64_t mediatek_mt7628_wmac0_read(void *opaque, hwaddr offset, unsigned size)
{
    MEDIATEK_MT7628AN_SOCState *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case 0x0 ... 0xffffc:
        res = s->mediatek_mt7628_wmac0_reserved[offset >> 2];
        break;
    }
    return res;
}

static void mediatek_mt7628_wmac0_write(void *opaque, hwaddr offset, uint64_t val, unsigned size)
{
    MEDIATEK_MT7628AN_SOCState *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case 0x0 ... 0xffffc:
        s->mediatek_mt7628_wmac0_reserved[offset >> 2] = val;
        break;
    }
    mediatek_mt7628_wmac0_update(s);
}

static const MemoryRegionOps mediatek_mt7628_wmac_ops0 = {
    .read = mediatek_mt7628_wmac0_read,
    .write = mediatek_mt7628_wmac0_write,
    .endianness = DEVICE_LITTLE_ENDIAN,
};

static void mediatek_mt7620_pci0_update(void *opaque)
{
    /* MEDIATEK_MT7628AN_SOCState *s = opaque; */
}

static uint64_t mediatek_mt7620_pci0_read(void *opaque, hwaddr offset, unsigned size)
{
    MEDIATEK_MT7628AN_SOCState *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case 0x0 ... 0xfc:
        res = s->mediatek_mt7620_pci0_reserved[offset >> 2];
        break;
    }
    return res;
}

static void mediatek_mt7620_pci0_write(void *opaque, hwaddr offset, uint64_t val, unsigned size)
{
    MEDIATEK_MT7628AN_SOCState *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case 0x0 ... 0xfc:
        s->mediatek_mt7620_pci0_reserved[offset >> 2] = val;
        break;
    }
    mediatek_mt7620_pci0_update(s);
}

static const MemoryRegionOps mediatek_mt7620_pci_ops0 = {
    .read = mediatek_mt7620_pci0_read,
    .write = mediatek_mt7620_pci0_write,
    .endianness = DEVICE_LITTLE_ENDIAN,
};
    static void mediatek_mt7620_pci1_update(void *opaque)
{
    /* MEDIATEK_MT7628AN_SOCState *s = opaque; */
}

static uint64_t mediatek_mt7620_pci1_read(void *opaque, hwaddr offset, unsigned size)
{
    MEDIATEK_MT7628AN_SOCState *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case 0x0 ... 0xfc:
        res = s->mediatek_mt7620_pci1_reserved[offset >> 2];
        break;
    }
    return res;
}

static void mediatek_mt7620_pci1_write(void *opaque, hwaddr offset, uint64_t val, unsigned size)
{
    MEDIATEK_MT7628AN_SOCState *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case 0x0 ... 0xfc:
        s->mediatek_mt7620_pci1_reserved[offset >> 2] = val;
        break;
    }
    mediatek_mt7620_pci1_update(s);
}

static const MemoryRegionOps mediatek_mt7620_pci_ops1 = {
    .read = mediatek_mt7620_pci1_read,
    .write = mediatek_mt7620_pci1_write,
    .endianness = DEVICE_LITTLE_ENDIAN,
};

static void ralink_rt3050_esw0_update(void *opaque)
{
    /* MEDIATEK_MT7628AN_SOCState *s = opaque; */
}

static uint64_t ralink_rt3050_esw0_read(void *opaque, hwaddr offset, unsigned size)
{
    MEDIATEK_MT7628AN_SOCState *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case 0x0 ... 0x7ffc:
        res = s->ralink_rt3050_esw0_reserved[offset >> 2];
        break;
    }
    return res;
}

static void ralink_rt3050_esw0_write(void *opaque, hwaddr offset, uint64_t val, unsigned size)
{
    MEDIATEK_MT7628AN_SOCState *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case 0x0 ... 0x7ffc:
        s->ralink_rt3050_esw0_reserved[offset >> 2] = val;
        break;
    }
    ralink_rt3050_esw0_update(s);
}

static const MemoryRegionOps ralink_rt3050_esw_ops0 = {
    .read = ralink_rt3050_esw0_read,
    .write = ralink_rt3050_esw0_write,
    .endianness = DEVICE_LITTLE_ENDIAN,
};

static void ralink_rt5350_eth0_update(void *opaque)
{
    /* MEDIATEK_MT7628AN_SOCState *s = opaque; */
}

static uint64_t ralink_rt5350_eth0_read(void *opaque, hwaddr offset, unsigned size)
{
    MEDIATEK_MT7628AN_SOCState *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case 0x0 ... 0xfffc:
        res = s->ralink_rt5350_eth0_reserved[offset >> 2];
        break;
    }
    return res;
}

static void ralink_rt5350_eth0_write(void *opaque, hwaddr offset, uint64_t val, unsigned size)
{
    MEDIATEK_MT7628AN_SOCState *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case 0x0 ... 0xfffc:
        s->ralink_rt5350_eth0_reserved[offset >> 2] = val;
        break;
    }
    ralink_rt5350_eth0_update(s);
}

static const MemoryRegionOps ralink_rt5350_eth_ops0 = {
    .read = ralink_rt5350_eth0_read,
    .write = ralink_rt5350_eth0_write,
    .endianness = DEVICE_LITTLE_ENDIAN,
};

static void generic_ohci0_update(void *opaque)
{
    /* MEDIATEK_MT7628AN_SOCState *s = opaque; */
}

static uint64_t generic_ohci0_read(void *opaque, hwaddr offset, unsigned size)
{
    MEDIATEK_MT7628AN_SOCState *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case 0x0 ... 0xffc:
        res = s->generic_ohci0_reserved[offset >> 2];
        break;
    }
    return res;
}

static void generic_ohci0_write(void *opaque, hwaddr offset, uint64_t val, unsigned size)
{
    MEDIATEK_MT7628AN_SOCState *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case 0x0 ... 0xffc:
        s->generic_ohci0_reserved[offset >> 2] = val;
        break;
    }
    generic_ohci0_update(s);
}

static const MemoryRegionOps generic_ohci_ops0 = {
    .read = generic_ohci0_read,
    .write = generic_ohci0_write,
    .endianness = DEVICE_LITTLE_ENDIAN,
};

static void generic_ehci0_update(void *opaque)
{
    /* MEDIATEK_MT7628AN_SOCState *s = opaque; */
}

static uint64_t generic_ehci0_read(void *opaque, hwaddr offset, unsigned size)
{
    MEDIATEK_MT7628AN_SOCState *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case 0x0 ... 0xffc:
        res = s->generic_ehci0_reserved[offset >> 2];
        break;
    }
    return res;
}

static void generic_ehci0_write(void *opaque, hwaddr offset, uint64_t val, unsigned size)
{
    MEDIATEK_MT7628AN_SOCState *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case 0x0 ... 0xffc:
        s->generic_ehci0_reserved[offset >> 2] = val;
        break;
    }
    generic_ehci0_update(s);
}

static const MemoryRegionOps generic_ehci_ops0 = {
    .read = generic_ehci0_read,
    .write = generic_ehci0_write,
    .endianness = DEVICE_LITTLE_ENDIAN,
};

static void ralink_mt7620_sdhci0_update(void *opaque)
{
    /* MEDIATEK_MT7628AN_SOCState *s = opaque; */
}

static uint64_t ralink_mt7620_sdhci0_read(void *opaque, hwaddr offset, unsigned size)
{
    MEDIATEK_MT7628AN_SOCState *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case 0x0 ... 0x3ffc:
        res = s->ralink_mt7620_sdhci0_reserved[offset >> 2];
        break;
    }
    return res;
}

static void ralink_mt7620_sdhci0_write(void *opaque, hwaddr offset, uint64_t val, unsigned size)
{
    MEDIATEK_MT7628AN_SOCState *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case 0x0 ... 0x3ffc:
        s->ralink_mt7620_sdhci0_reserved[offset >> 2] = val;
        break;
    }
    ralink_mt7620_sdhci0_update(s);
}

static const MemoryRegionOps ralink_mt7620_sdhci_ops0 = {
    .read = ralink_mt7620_sdhci0_read,
    .write = ralink_mt7620_sdhci0_write,
    .endianness = DEVICE_LITTLE_ENDIAN,
};

static void mediatek_mt7620_usbphy0_update(void *opaque)
{
    /* MEDIATEK_MT7628AN_SOCState *s = opaque; */
}

static uint64_t mediatek_mt7620_usbphy0_read(void *opaque, hwaddr offset, unsigned size)
{
    MEDIATEK_MT7628AN_SOCState *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case 0x0 ... 0xffc:
        res = s->mediatek_mt7620_usbphy0_reserved[offset >> 2];
        break;
    }
    return res;
}

static void mediatek_mt7620_usbphy0_write(void *opaque, hwaddr offset, uint64_t val, unsigned size)
{
    MEDIATEK_MT7628AN_SOCState *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case 0x0 ... 0xffc:
        s->mediatek_mt7620_usbphy0_reserved[offset >> 2] = val;
        break;
    }
    mediatek_mt7620_usbphy0_update(s);
}

static const MemoryRegionOps mediatek_mt7620_usbphy_ops0 = {
    .read = mediatek_mt7620_usbphy0_read,
    .write = mediatek_mt7620_usbphy0_write,
    .endianness = DEVICE_LITTLE_ENDIAN,
};

static void ralink_rt3883_gdma0_update(void *opaque)
{
    /* MEDIATEK_MT7628AN_SOCState *s = opaque; */
}

static uint64_t ralink_rt3883_gdma0_read(void *opaque, hwaddr offset, unsigned size)
{
    MEDIATEK_MT7628AN_SOCState *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case 0x0 ... 0x7fc:
        res = s->ralink_rt3883_gdma0_reserved[offset >> 2];
        break;
    }
    return res;
}

static void ralink_rt3883_gdma0_write(void *opaque, hwaddr offset, uint64_t val, unsigned size)
{
    MEDIATEK_MT7628AN_SOCState *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case 0x0 ... 0x7fc:
        s->ralink_rt3883_gdma0_reserved[offset >> 2] = val;
        break;
    }
    ralink_rt3883_gdma0_update(s);
}

static const MemoryRegionOps ralink_rt3883_gdma_ops0 = {
    .read = ralink_rt3883_gdma0_read,
    .write = ralink_rt3883_gdma0_write,
    .endianness = DEVICE_LITTLE_ENDIAN,
};

static void ralink_mt7620a_pcm0_update(void *opaque)
{
    /* MEDIATEK_MT7628AN_SOCState *s = opaque; */
}

static uint64_t ralink_mt7620a_pcm0_read(void *opaque, hwaddr offset, unsigned size)
{
    MEDIATEK_MT7628AN_SOCState *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case 0x0 ... 0x7fc:
        res = s->ralink_mt7620a_pcm0_reserved[offset >> 2];
        break;
    }
    return res;
}

static void ralink_mt7620a_pcm0_write(void *opaque, hwaddr offset, uint64_t val, unsigned size)
{
    MEDIATEK_MT7628AN_SOCState *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case 0x0 ... 0x7fc:
        s->ralink_mt7620a_pcm0_reserved[offset >> 2] = val;
        break;
    }
    ralink_mt7620a_pcm0_update(s);
}

static const MemoryRegionOps ralink_mt7620a_pcm_ops0 = {
    .read = ralink_mt7620a_pcm0_read,
    .write = ralink_mt7620a_pcm0_write,
    .endianness = DEVICE_LITTLE_ENDIAN,
};

static void mediatek_mt7628_pwm0_update(void *opaque)
{
    /* MEDIATEK_MT7628AN_SOCState *s = opaque; */
}

static uint64_t mediatek_mt7628_pwm0_read(void *opaque, hwaddr offset, unsigned size)
{
    MEDIATEK_MT7628AN_SOCState *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case 0x0 ... 0xffc:
        res = s->mediatek_mt7628_pwm0_reserved[offset >> 2];
        break;
    }
    return res;
}

static void mediatek_mt7628_pwm0_write(void *opaque, hwaddr offset, uint64_t val, unsigned size)
{
    MEDIATEK_MT7628AN_SOCState *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case 0x0 ... 0xffc:
        s->mediatek_mt7628_pwm0_reserved[offset >> 2] = val;
        break;
    }
    mediatek_mt7628_pwm0_update(s);
}

static const MemoryRegionOps mediatek_mt7628_pwm_ops0 = {
    .read = mediatek_mt7628_pwm0_read,
    .write = mediatek_mt7628_pwm0_write,
    .endianness = DEVICE_LITTLE_ENDIAN,
};

static void ralink_mt7621_spi0_update(void *opaque)
{
    /* MEDIATEK_MT7628AN_SOCState *s = opaque; */
}

static uint64_t ralink_mt7621_spi0_read(void *opaque, hwaddr offset, unsigned size)
{
    MEDIATEK_MT7628AN_SOCState *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case 0x0 ... 0xfc:
        res = s->ralink_mt7621_spi0_reserved[offset >> 2];
        break;
    }
    return res;
}

static void ralink_mt7621_spi0_write(void *opaque, hwaddr offset, uint64_t val, unsigned size)
{
    MEDIATEK_MT7628AN_SOCState *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case 0x0 ... 0xfc:
        s->ralink_mt7621_spi0_reserved[offset >> 2] = val;
        break;
    }
    ralink_mt7621_spi0_update(s);
}

static const MemoryRegionOps ralink_mt7621_spi_ops0 = {
    .read = ralink_mt7621_spi0_read,
    .write = ralink_mt7621_spi0_write,
    .endianness = DEVICE_LITTLE_ENDIAN,
};

static void mediatek_mt7628_i2s0_update(void *opaque)
{
    /* MEDIATEK_MT7628AN_SOCState *s = opaque; */
}

static uint64_t mediatek_mt7628_i2s0_read(void *opaque, hwaddr offset, unsigned size)
{
    MEDIATEK_MT7628AN_SOCState *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case 0x0 ... 0xfc:
        res = s->mediatek_mt7628_i2s0_reserved[offset >> 2];
        break;
    }
    return res;
}

static void mediatek_mt7628_i2s0_write(void *opaque, hwaddr offset, uint64_t val, unsigned size)
{
    MEDIATEK_MT7628AN_SOCState *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case 0x0 ... 0xfc:
        s->mediatek_mt7628_i2s0_reserved[offset >> 2] = val;
        break;
    }
    mediatek_mt7628_i2s0_update(s);
}

static const MemoryRegionOps mediatek_mt7628_i2s_ops0 = {
    .read = mediatek_mt7628_i2s0_read,
    .write = mediatek_mt7628_i2s0_write,
    .endianness = DEVICE_LITTLE_ENDIAN,
};

static void mediatek_mt7621_i2c0_update(void *opaque)
{
    /* MEDIATEK_MT7628AN_SOCState *s = opaque; */
}

static uint64_t mediatek_mt7621_i2c0_read(void *opaque, hwaddr offset, unsigned size)
{
    MEDIATEK_MT7628AN_SOCState *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case 0x0 ... 0xfc:
        res = s->mediatek_mt7621_i2c0_reserved[offset >> 2];
        break;
    }
    return res;
}

static void mediatek_mt7621_i2c0_write(void *opaque, hwaddr offset, uint64_t val, unsigned size)
{
    MEDIATEK_MT7628AN_SOCState *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case 0x0 ... 0xfc:
        s->mediatek_mt7621_i2c0_reserved[offset >> 2] = val;
        break;
    }
    mediatek_mt7621_i2c0_update(s);
}

static const MemoryRegionOps mediatek_mt7621_i2c_ops0 = {
    .read = mediatek_mt7621_i2c0_read,
    .write = mediatek_mt7621_i2c0_write,
    .endianness = DEVICE_LITTLE_ENDIAN,
};

static void mtk_mt7621_gpio0_update(void *opaque)
{
    /* MEDIATEK_MT7628AN_SOCState *s = opaque; */
}

static uint64_t mtk_mt7621_gpio0_read(void *opaque, hwaddr offset, unsigned size)
{
    MEDIATEK_MT7628AN_SOCState *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case 0x0 ... 0xfc:
        res = s->mtk_mt7621_gpio0_reserved[offset >> 2];
        break;
    }
    return res;
}

static void mtk_mt7621_gpio0_write(void *opaque, hwaddr offset, uint64_t val, unsigned size)
{
    MEDIATEK_MT7628AN_SOCState *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case 0x0 ... 0xfc:
        s->mtk_mt7621_gpio0_reserved[offset >> 2] = val;
        break;
    }
    mtk_mt7621_gpio0_update(s);
}

static const MemoryRegionOps mtk_mt7621_gpio_ops0 = {
    .read = mtk_mt7621_gpio0_read,
    .write = mtk_mt7621_gpio0_write,
    .endianness = DEVICE_LITTLE_ENDIAN,
};

static void ralink_rt3050_memc0_update(void *opaque)
{
    /* MEDIATEK_MT7628AN_SOCState *s = opaque; */
}

static uint64_t ralink_rt3050_memc0_read(void *opaque, hwaddr offset, unsigned size)
{
    MEDIATEK_MT7628AN_SOCState *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case 0x0 ... 0xfc:
        res = s->ralink_rt3050_memc0_reserved[offset >> 2];
        break;
    }
    return res;
}

static void ralink_rt3050_memc0_write(void *opaque, hwaddr offset, uint64_t val, unsigned size)
{
    MEDIATEK_MT7628AN_SOCState *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case 0x0 ... 0xfc:
        s->ralink_rt3050_memc0_reserved[offset >> 2] = val;
        break;
    }
    ralink_rt3050_memc0_update(s);
}

static const MemoryRegionOps ralink_rt3050_memc_ops0 = {
    .read = ralink_rt3050_memc0_read,
    .write = ralink_rt3050_memc0_write,
    .endianness = DEVICE_LITTLE_ENDIAN,
};

static void mediatek_mt7621_wdt0_update(void *opaque)
{
    /* MEDIATEK_MT7628AN_SOCState *s = opaque; */
}

static uint64_t mediatek_mt7621_wdt0_read(void *opaque, hwaddr offset, unsigned size)
{
    MEDIATEK_MT7628AN_SOCState *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case 0x0 ... 0x2c:
        res = s->mediatek_mt7621_wdt0_reserved[offset >> 2];
        break;
    }
    return res;
}

static void mediatek_mt7621_wdt0_write(void *opaque, hwaddr offset, uint64_t val, unsigned size)
{
    MEDIATEK_MT7628AN_SOCState *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case 0x0 ... 0x2c:
        s->mediatek_mt7621_wdt0_reserved[offset >> 2] = val;
        break;
    }
    mediatek_mt7621_wdt0_update(s);
}

static const MemoryRegionOps mediatek_mt7621_wdt_ops0 = {
    .read = mediatek_mt7621_wdt0_read,
    .write = mediatek_mt7621_wdt0_write,
    .endianness = DEVICE_LITTLE_ENDIAN,
};

static void ralink_mt7620a_sysc0_update(void *opaque)
{
    /* MEDIATEK_MT7628AN_SOCState *s = opaque; */
}

static uint64_t ralink_mt7620a_sysc0_read(void *opaque, hwaddr offset, unsigned size)
{
    MEDIATEK_MT7628AN_SOCState *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case 0x0 ... 0xfc:
        res = s->ralink_mt7620a_sysc0_reserved[offset >> 2];
        break;
    }
    return res;
}

static void ralink_mt7620a_sysc0_write(void *opaque, hwaddr offset, uint64_t val, unsigned size)
{
    MEDIATEK_MT7628AN_SOCState *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case 0x0 ... 0xfc:
        s->ralink_mt7620a_sysc0_reserved[offset >> 2] = val;
        break;
    }
    ralink_mt7620a_sysc0_update(s);
}

static const MemoryRegionOps ralink_mt7620a_sysc_ops0 = {
    .read = ralink_mt7620a_sysc0_read,
    .write = ralink_mt7620a_sysc0_write,
    .endianness = DEVICE_LITTLE_ENDIAN,
};


static void mediatek_mt7628an_soc_reset(void *opaque)
{
    MEDIATEK_MT7628AN_SOCState *s = opaque;
    
    s->ralink_rt3050_esw0_reserved[0xc4 >> 2] = 0x1;
    s->ralink_mt7620a_sysc0_reserved[0x0 >> 2] = 0x3637544d;
    s->ralink_mt7620a_sysc0_reserved[0x4 >> 2] = 0x20203832;
    s->ralink_mt7620a_sysc0_reserved[0x8 >> 2] = 0x100000;
}

static void mediatek_mt7628an_soc_init(MachineState *machine)
{
    MEDIATEK_MT7628AN_SOCState *s = g_new0(MEDIATEK_MT7628AN_SOCState, 1);
    Error *err = NULL;
    static struct mips_boot_info binfo;
    
    s->cpu = MIPS_CPU(object_new(machine->cpu_type));
    object_property_set_bool(OBJECT(s->cpu), true, "realized", &err);
    
    memory_region_allocate_system_memory(&s->ram0, OBJECT(machine), "ram0", 0x8000000);
    memory_region_add_subregion_overlap(get_system_memory(), 0x0, &s->ram0, 0);
    
    cpu_mips_irq_init_cpu(s->cpu);
    cpu_mips_clock_init(s->cpu);
    object_initialize(&s->ralink_rt2880_intc0, sizeof(s->ralink_rt2880_intc0), TYPE_RALINK_RT2880_INTC);
    qdev_set_parent_bus(DEVICE(&s->ralink_rt2880_intc0), sysbus_get_default());
    object_property_set_bool(OBJECT(&s->ralink_rt2880_intc0), true, "realized", &err);
    sysbus_mmio_map(SYS_BUS_DEVICE(&s->ralink_rt2880_intc0), 0, 0x10000200);
    
    qdev_connect_gpio_out(DEVICE(&s->ralink_rt2880_intc0), 0, s->cpu->env.irq[2]);
    
    
    
    serial_mm_init(get_system_memory(), 0x10000e00, 2, qdev_get_gpio_in(DEVICE(&s->ralink_rt2880_intc0), 22), 115200, serial_hd(0), DEVICE_LITTLE_ENDIAN);
    serial_mm_init(get_system_memory(), 0x10000d00, 2, qdev_get_gpio_in(DEVICE(&s->ralink_rt2880_intc0), 21), 115200, serial_hd(1), DEVICE_LITTLE_ENDIAN);
    serial_mm_init(get_system_memory(), 0x10000c00, 2, qdev_get_gpio_in(DEVICE(&s->ralink_rt2880_intc0), 20), 115200, serial_hd(2), DEVICE_LITTLE_ENDIAN);
    
    
    memory_region_init_rom(&s->flash, NULL, "boot.flash", 0x400000, &err);
    memory_region_add_subregion_overlap(get_system_memory(), 0x1fc00000, &s->flash, 0);
    
    memory_region_init_io(&s->mediatek_mt7628_wmac0_mmio, NULL, &mediatek_mt7628_wmac_ops0, s, TYPE_MEDIATEK_MT7628AN_SOC, 0x100000);
    memory_region_add_subregion_overlap(get_system_memory(), 0x10300000, &s->mediatek_mt7628_wmac0_mmio, 0);
    memory_region_init_io(&s->mediatek_mt7620_pci0_mmio, NULL, &mediatek_mt7620_pci_ops0, s, TYPE_MEDIATEK_MT7628AN_SOC, 0x100);
    memory_region_add_subregion_overlap(get_system_memory(), 0x10140000, &s->mediatek_mt7620_pci0_mmio, 0);
    memory_region_init_io(&s->mediatek_mt7620_pci1_mmio, NULL, &mediatek_mt7620_pci_ops1, s, TYPE_MEDIATEK_MT7628AN_SOC, 0x100);
    memory_region_add_subregion_overlap(get_system_memory(), 0x10142000, &s->mediatek_mt7620_pci1_mmio, 0);
    memory_region_init_io(&s->ralink_rt3050_esw0_mmio, NULL, &ralink_rt3050_esw_ops0, s, TYPE_MEDIATEK_MT7628AN_SOC, 0x8000);
    memory_region_add_subregion_overlap(get_system_memory(), 0x10110000, &s->ralink_rt3050_esw0_mmio, 0);
    memory_region_init_io(&s->ralink_rt5350_eth0_mmio, NULL, &ralink_rt5350_eth_ops0, s, TYPE_MEDIATEK_MT7628AN_SOC, 0x10000);
    memory_region_add_subregion_overlap(get_system_memory(), 0x10100000, &s->ralink_rt5350_eth0_mmio, 0);
    memory_region_init_io(&s->generic_ohci0_mmio, NULL, &generic_ohci_ops0, s, TYPE_MEDIATEK_MT7628AN_SOC, 0x1000);
    memory_region_add_subregion_overlap(get_system_memory(), 0x101c1000, &s->generic_ohci0_mmio, 0);
    memory_region_init_io(&s->generic_ehci0_mmio, NULL, &generic_ehci_ops0, s, TYPE_MEDIATEK_MT7628AN_SOC, 0x1000);
    memory_region_add_subregion_overlap(get_system_memory(), 0x101c0000, &s->generic_ehci0_mmio, 0);
    memory_region_init_io(&s->ralink_mt7620_sdhci0_mmio, NULL, &ralink_mt7620_sdhci_ops0, s, TYPE_MEDIATEK_MT7628AN_SOC, 0x4000);
    memory_region_add_subregion_overlap(get_system_memory(), 0x10130000, &s->ralink_mt7620_sdhci0_mmio, 0);
    memory_region_init_io(&s->mediatek_mt7620_usbphy0_mmio, NULL, &mediatek_mt7620_usbphy_ops0, s, TYPE_MEDIATEK_MT7628AN_SOC, 0x1000);
    memory_region_add_subregion_overlap(get_system_memory(), 0x10120000, &s->mediatek_mt7620_usbphy0_mmio, 0);
    memory_region_init_io(&s->ralink_rt3883_gdma0_mmio, NULL, &ralink_rt3883_gdma_ops0, s, TYPE_MEDIATEK_MT7628AN_SOC, 0x800);
    memory_region_add_subregion_overlap(get_system_memory(), 0x10002800, &s->ralink_rt3883_gdma0_mmio, 0);
    memory_region_init_io(&s->ralink_mt7620a_pcm0_mmio, NULL, &ralink_mt7620a_pcm_ops0, s, TYPE_MEDIATEK_MT7628AN_SOC, 0x800);
    memory_region_add_subregion_overlap(get_system_memory(), 0x10002000, &s->ralink_mt7620a_pcm0_mmio, 0);
    memory_region_init_io(&s->mediatek_mt7628_pwm0_mmio, NULL, &mediatek_mt7628_pwm_ops0, s, TYPE_MEDIATEK_MT7628AN_SOC, 0x1000);
    memory_region_add_subregion_overlap(get_system_memory(), 0x10005000, &s->mediatek_mt7628_pwm0_mmio, 0);
    memory_region_init_io(&s->ralink_mt7621_spi0_mmio, NULL, &ralink_mt7621_spi_ops0, s, TYPE_MEDIATEK_MT7628AN_SOC, 0x100);
    memory_region_add_subregion_overlap(get_system_memory(), 0x10000b00, &s->ralink_mt7621_spi0_mmio, 0);
    memory_region_init_io(&s->mediatek_mt7628_i2s0_mmio, NULL, &mediatek_mt7628_i2s_ops0, s, TYPE_MEDIATEK_MT7628AN_SOC, 0x100);
    memory_region_add_subregion_overlap(get_system_memory(), 0x10000a00, &s->mediatek_mt7628_i2s0_mmio, 0);
    memory_region_init_io(&s->mediatek_mt7621_i2c0_mmio, NULL, &mediatek_mt7621_i2c_ops0, s, TYPE_MEDIATEK_MT7628AN_SOC, 0x100);
    memory_region_add_subregion_overlap(get_system_memory(), 0x10000900, &s->mediatek_mt7621_i2c0_mmio, 0);
    memory_region_init_io(&s->mtk_mt7621_gpio0_mmio, NULL, &mtk_mt7621_gpio_ops0, s, TYPE_MEDIATEK_MT7628AN_SOC, 0x100);
    memory_region_add_subregion_overlap(get_system_memory(), 0x10000600, &s->mtk_mt7621_gpio0_mmio, 0);
    memory_region_init_io(&s->ralink_rt3050_memc0_mmio, NULL, &ralink_rt3050_memc_ops0, s, TYPE_MEDIATEK_MT7628AN_SOC, 0x100);
    memory_region_add_subregion_overlap(get_system_memory(), 0x10000300, &s->ralink_rt3050_memc0_mmio, 0);
    memory_region_init_io(&s->mediatek_mt7621_wdt0_mmio, NULL, &mediatek_mt7621_wdt_ops0, s, TYPE_MEDIATEK_MT7628AN_SOC, 0x30);
    memory_region_add_subregion_overlap(get_system_memory(), 0x10000100, &s->mediatek_mt7621_wdt0_mmio, 0);
    memory_region_init_io(&s->ralink_mt7620a_sysc0_mmio, NULL, &ralink_mt7620a_sysc_ops0, s, TYPE_MEDIATEK_MT7628AN_SOC, 0x100);
    memory_region_add_subregion_overlap(get_system_memory(), 0x10000000, &s->ralink_mt7620a_sysc0_mmio, 0);
    mediatek_mt7628an_soc_reset(s);

    binfo.board_id = 0xFFFFFFFF;
    binfo.ram_size = machine->ram_size;
    binfo.kernel_filename = machine->kernel_filename;
    binfo.kernel_cmdline = machine->kernel_cmdline;
    binfo.initrd_filename = machine->initrd_filename;
    mips_load_kernel(MIPS_CPU(first_cpu), &binfo);
}

static void mediatek_mt7628an_soc_machine_init(MachineClass *mc)
{
    mc->desc = "mediatek_mt7628an_soc";
    mc->init = mediatek_mt7628an_soc_init;
    mc->default_ram_size = 256 * MiB;
    mc->default_cpu_type = MIPS_CPU_TYPE_NAME("24KEc");
    mc->ignore_memory_transaction_failures = false;
}

DEFINE_MACHINE("mediatek_mt7628an_soc", mediatek_mt7628an_soc_machine_init)
