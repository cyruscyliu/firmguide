#include "qemu/osdep.h"
#include "qemu/log.h"
#include "qapi/error.h"
#include "hw/net/brcm_bus_axi.h"

#define SCAN_ER_VALID       0x00000001
#define SCAN_ER_TAGX        0x00000006
#define SCAN_ER_TAG         0x0000000E
#define SCAN_ER_TAG_CI      0x00000000
#define SCAN_ER_TAG_MP      0x00000002
#define SCAN_ER_TAG_ADDR    0x00000004
#define SCAN_ER_TAG_END     0x0000000E
#define SCAN_ER_BAD         0xFFFFFFFF

#define CIA(manuf, id, class) \
    (manuf << 20 | id << 8 | class << 0 | SCAN_ER_TAG_CI | SCAN_ER_VALID)
#define CIB(rev, wrapper1, wrapper0, port1, port0) \
    (rev << 24 | wrapper1 << 19 | wrapper0 << 14 | port1 << 9 | port0 << 4 | SCAN_ER_VALID)
#define ADDR(addr, port, type) \
    (addr << 12 | port << 8 | type << 6 | SCAN_ER_TAG_ADDR | SCAN_ER_VALID)
#define END (SCAN_ER_TAG_END | SCAN_ER_VALID)

/*
 * 0x18000000 0x1000
 * 0x18001000 0x1000 EROM
 * 0x18002000 0x1000 COMMON
 * 0x18003000 0x1000 IEEE80211
 * 0x18004000 0x1000 PCIE2
 */
#define EROM_ADDR       (({{ reg.base|to_hex }} + 0x1000) >> 12)
#define COMMON_ADDR     (({{ reg.base|to_hex }} + 0x2000) >> 12)
#define IEEE80211_ADDR  (({{ reg.base|to_hex }} + 0x3000) >> 12)
#define PCIE2_ADDR      (({{ reg.base|to_hex }} + 0x4000) >> 12)

/*
 * EROM
 */
#define common_chip     (0x1000)
#define ieee80211_chip  (common_chip + 0x8 + 0x4)
#define pcie2           (ieee80211_chip + 0x8 + 0x4)
#define end             (pcie2 + 0x8 + 0x4)
/*
 * COMMON
 */
#define BCMA_CC_CHIPSTATE (0x2000 + 0x002C)
#define BCMA_CC_CAP       (0x2000 + 0x0004)
#define BCMA_CC_CAP_EXT   (0x2000 + 0x00AC)
#define BCMA_CLKCTLST     (0x2000 + 0x01E0)
/*
 * PCIE2
 */
#define BCMA_CORE_PCI_MDIO_CONTROL 0x4128

static uint64_t brcm_bus_axi_read(void *opaque, hwaddr offset, unsigned size)
{
    // qemu_log("[R] brcm_bus_axi 0x%lx, 0x%x\n", offset, size);
    BRCM_BUS_AXIState *s = opaque;
    uint32_t res = 0;

    switch (offset) {
        default:
            return 0;
        case 0x0:
            return 0x8 << 20 | 0x1 << 16 | 0x4313;
        case 0xFC:
            return {{ reg.base|to_hex }} + common_chip;
        // common chip
        case common_chip + 0x0:
            return CIA(0x4BF, 0x800, 0x0);
        case common_chip + 0x4:
            return CIB(0x24, 1, 0, 1, 0);
        case common_chip + 0x8:
            return ADDR(COMMON_ADDR, 0, 0);
        // 80211 chip
        case ieee80211_chip + 0x0:
            return CIA(0x4BF, 0x812, 0x0);
        case ieee80211_chip + 0x4:
            return CIB(0x18, 1, 0, 1, 0);
        case ieee80211_chip + 0x8:
            return ADDR(IEEE80211_ADDR, 0, 0);
        // pcie chip
        case pcie2:
            return CIA(0x4BF, 0x820, 0x0);
        case pcie2 + 0x4:
            return CIB(0x11, 1, 0, 1, 0);
        case pcie2 + 0x8:
            return ADDR(PCIE2_ADDR, 0, 0);
        // end
        case end:
            return END;
        case BCMA_CLKCTLST:
            if (s->bcma_clkctlst_forceht) {
                return 0x00020000;
            } else {
                return 0;
            }
        case BCMA_CORE_PCI_MDIO_CONTROL:
            return 0x100;

    }
    return res;
}

#define BCMA_CLKCTLST_FORCEHT 2

static void brcm_bus_axi_write(void *opaque, hwaddr offset, uint64_t val, unsigned size)
{
    // qemu_log("[W] brcm_bus_axi 0x%lx, 0x%lx, 0x%x\n", offset, val, size);
    BRCM_BUS_AXIState *s = opaque;

    switch (offset) {
        default:
            return;
        case BCMA_CLKCTLST:
            if (val == BCMA_CLKCTLST_FORCEHT) {
                s->bcma_clkctlst_forceht = true;
            }
    }
    return;
}

static const MemoryRegionOps brcm_bus_axi_ops = {
    .read = brcm_bus_axi_read,
    .write = brcm_bus_axi_write,
    .endianness = {{ endian|to_endian }},
};

static void brcm_bus_axi_init(Object *obj)
{
    BRCM_BUS_AXIState *s = BRCM_BUS_AXI(obj);

    /* initialize the mmio */
    memory_region_init_io(&s->mmio, obj, &brcm_bus_axi_ops, s, TYPE_BRCM_BUS_AXI, {{ reg.size|to_hex }} * 5);
    sysbus_init_mmio(SYS_BUS_DEVICE(s), &s->mmio);
}

static void brcm_bus_axi_reset(DeviceState *dev)
{
    BRCM_BUS_AXIState *s = BRCM_BUS_AXI(dev);
}

static void brcm_bus_axi_class_init(ObjectClass *klass, void *data)
{
    DeviceClass *dc = DEVICE_CLASS(klass);

    dc->reset = brcm_bus_axi_reset;
}

static TypeInfo brcm_bus_axi_type_info = {
    .name = TYPE_BRCM_BUS_AXI,
    .parent = TYPE_SYS_BUS_DEVICE,
    .instance_size = sizeof(BRCM_BUS_AXIState),
    .instance_init = brcm_bus_axi_init,
    /* .class_size = sizeof(SysBusDeviceClass), */
    .class_init = brcm_bus_axi_class_init,
};

static void brcm_bus_axi_register_types(void)
{
    type_register_static(&brcm_bus_axi_type_info);
}

type_init(brcm_bus_axi_register_types)
