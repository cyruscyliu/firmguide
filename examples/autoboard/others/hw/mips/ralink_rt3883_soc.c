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
//#include "hw/intc/ralink_rt2880_intc.h"
#include "hw/intc/autoboard_intc.h"
#include "hw/timer/ralink_rt2880_timer.h"
#include "hw/char/serial.h"
#include "hw/char/serial.h"

#define TYPE_RALINK_RT3883_SOC "ralink_rt3883_soc"
#define RALINK_RT3883_SOC(obj) \
    OBJECT_CHECK(RALINK_RT3883_SOCState, (obj), TYPE_RALINK_RT3883_SOC)

typedef struct RALINK_RT3883_SOCState {
    MIPSCPU *cpu;
    //RALINK_RT2880_INTCState ralink_rt2880_intc0;
    AUTOBOARD_INTCState autoboard_intc0;
    RALINK_RT2880_TIMERState timer0;
    MemoryRegion stub17_mmio;
    uint32_t stub_reserved17[0x4 >> 2];
    MemoryRegion stub2_mmio;
    uint32_t stub_reserved2[0x10 >> 2];
    MemoryRegion stub4_mmio;
    uint32_t stub_reserved4[0x100 >> 2];
    MemoryRegion stub6_mmio;
    uint32_t stub_reserved6[0x34 >> 2];
    MemoryRegion stub7_mmio;
    uint32_t stub_reserved7[0x24 >> 2];
    MemoryRegion stub8_mmio;
    uint32_t stub_reserved8[0x24 >> 2];
    MemoryRegion stub9_mmio;
    uint32_t stub_reserved9[0x24 >> 2];
    MemoryRegion stub10_mmio;
    uint32_t stub_reserved10[0x100 >> 2];
    MemoryRegion stub12_mmio;
    uint32_t stub_reserved12[0x2710 >> 2];
    MemoryRegion stub13_mmio;
    uint32_t stub_reserved13[0x20000 >> 2];
    MemoryRegion stub14_mmio;
    uint32_t stub_reserved14[0x9c40 >> 2];
    MemoryRegion stub15_mmio;
    uint32_t stub_reserved15[0x1000 >> 2];
    MemoryRegion stub16_mmio;
    uint32_t stub_reserved16[0x1000 >> 2];
    MemoryRegion stub0_mmio;
    uint32_t stub_reserved0[0xf8 >> 2];
    MemoryRegion stub18_mmio;
    uint32_t stub_reserved18[0x4 >> 2];
    MemoryRegion flash;
    MemoryRegion ram;
} RALINK_RT3883_SOCState;

static void stub17_update(void *opaque)
{
    /* RALINK_RT3883_SOCState *s = opaque; */
}

static uint64_t stub17_read(void *opaque, hwaddr offset, unsigned size)
{
    RALINK_RT3883_SOCState *s = opaque;
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
    RALINK_RT3883_SOCState *s = opaque;

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

static void stub2_update(void *opaque)
{
    /* RALINK_RT3883_SOCState *s = opaque; */
}

static uint64_t stub2_read(void *opaque, hwaddr offset, unsigned size)
{
    RALINK_RT3883_SOCState *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case 0x0 ... 0xc:
        res = s->stub_reserved2[offset >> 2];
        break;
    }
    return res;
}

static void stub2_write(void *opaque, hwaddr offset, uint64_t val, unsigned size)
{
    RALINK_RT3883_SOCState *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case 0x0 ... 0xc:
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

static void stub4_update(void *opaque)
{
    /* RALINK_RT3883_SOCState *s = opaque; */
}

static uint64_t stub4_read(void *opaque, hwaddr offset, unsigned size)
{
    RALINK_RT3883_SOCState *s = opaque;
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
    RALINK_RT3883_SOCState *s = opaque;

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

static void stub6_update(void *opaque)
{
    /* RALINK_RT3883_SOCState *s = opaque; */
}

static uint64_t stub6_read(void *opaque, hwaddr offset, unsigned size)
{
    RALINK_RT3883_SOCState *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case 0x0 ... 0x30:
        res = s->stub_reserved6[offset >> 2];
        break;
    }
    return res;
}

static void stub6_write(void *opaque, hwaddr offset, uint64_t val, unsigned size)
{
    RALINK_RT3883_SOCState *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case 0x0 ... 0x30:
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
    /* RALINK_RT3883_SOCState *s = opaque; */
}

static uint64_t stub7_read(void *opaque, hwaddr offset, unsigned size)
{
    RALINK_RT3883_SOCState *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case 0x0 ... 0x20:
        res = s->stub_reserved7[offset >> 2];
        break;
    }
    return res;
}

static void stub7_write(void *opaque, hwaddr offset, uint64_t val, unsigned size)
{
    RALINK_RT3883_SOCState *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case 0x0 ... 0x20:
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
    /* RALINK_RT3883_SOCState *s = opaque; */
}

static uint64_t stub8_read(void *opaque, hwaddr offset, unsigned size)
{
    RALINK_RT3883_SOCState *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case 0x0 ... 0x20:
        res = s->stub_reserved8[offset >> 2];
        break;
    }
    return res;
}

static void stub8_write(void *opaque, hwaddr offset, uint64_t val, unsigned size)
{
    RALINK_RT3883_SOCState *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case 0x0 ... 0x20:
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
    /* RALINK_RT3883_SOCState *s = opaque; */
}

static uint64_t stub9_read(void *opaque, hwaddr offset, unsigned size)
{
    RALINK_RT3883_SOCState *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case 0x0 ... 0x20:
        res = s->stub_reserved9[offset >> 2];
        break;
    }
    return res;
}

static void stub9_write(void *opaque, hwaddr offset, uint64_t val, unsigned size)
{
    RALINK_RT3883_SOCState *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case 0x0 ... 0x20:
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
    /* RALINK_RT3883_SOCState *s = opaque; */
}

static uint64_t stub10_read(void *opaque, hwaddr offset, unsigned size)
{
    RALINK_RT3883_SOCState *s = opaque;
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
    RALINK_RT3883_SOCState *s = opaque;

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
    .endianness = DEVICE_LITTLE_ENDIAN,
};

static void stub12_update(void *opaque)
{
    /* RALINK_RT3883_SOCState *s = opaque; */
}

static uint64_t stub12_read(void *opaque, hwaddr offset, unsigned size)
{
    RALINK_RT3883_SOCState *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case 0x0 ... 0x270c:
        res = s->stub_reserved12[offset >> 2];
        break;
    }
    return res;
}

static void stub12_write(void *opaque, hwaddr offset, uint64_t val, unsigned size)
{
    RALINK_RT3883_SOCState *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case 0x0 ... 0x270c:
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
    /* RALINK_RT3883_SOCState *s = opaque; */
}

static uint64_t stub13_read(void *opaque, hwaddr offset, unsigned size)
{
    RALINK_RT3883_SOCState *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case 0x0 ... 0x1fffc:
        res = s->stub_reserved13[offset >> 2];
        break;
    }
    return res;
}

static void stub13_write(void *opaque, hwaddr offset, uint64_t val, unsigned size)
{
    RALINK_RT3883_SOCState *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case 0x0 ... 0x1fffc:
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

static void stub14_update(void *opaque)
{
    /* RALINK_RT3883_SOCState *s = opaque; */
}

static uint64_t stub14_read(void *opaque, hwaddr offset, unsigned size)
{
    RALINK_RT3883_SOCState *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case 0x0 ... 0x9c3c:
        res = s->stub_reserved14[offset >> 2];
        break;
    }
    return res;
}

static void stub14_write(void *opaque, hwaddr offset, uint64_t val, unsigned size)
{
    RALINK_RT3883_SOCState *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case 0x0 ... 0x9c3c:
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
    /* RALINK_RT3883_SOCState *s = opaque; */
}

static uint64_t stub15_read(void *opaque, hwaddr offset, unsigned size)
{
    RALINK_RT3883_SOCState *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case 0x0 ... 0xffc:
        res = s->stub_reserved15[offset >> 2];
        break;
    }
    return res;
}

static void stub15_write(void *opaque, hwaddr offset, uint64_t val, unsigned size)
{
    RALINK_RT3883_SOCState *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case 0x0 ... 0xffc:
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
    /* RALINK_RT3883_SOCState *s = opaque; */
}

static uint64_t stub16_read(void *opaque, hwaddr offset, unsigned size)
{
    RALINK_RT3883_SOCState *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case 0x0 ... 0xffc:
        res = s->stub_reserved16[offset >> 2];
        break;
    }
    return res;
}

static void stub16_write(void *opaque, hwaddr offset, uint64_t val, unsigned size)
{
    RALINK_RT3883_SOCState *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case 0x0 ... 0xffc:
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

static void stub0_update(void *opaque)
{
    /* RALINK_RT3883_SOCState *s = opaque; */
}

static uint64_t stub0_read(void *opaque, hwaddr offset, unsigned size)
{
    RALINK_RT3883_SOCState *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case 0x0 ... 0xf4:
        res = s->stub_reserved0[offset >> 2];
        break;
    }
    return res;
}

static void stub0_write(void *opaque, hwaddr offset, uint64_t val, unsigned size)
{
    RALINK_RT3883_SOCState *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case 0x0 ... 0xf4:
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

static void stub18_update(void *opaque)
{
    /* RALINK_RT3883_SOCState *s = opaque; */
}

static uint64_t stub18_read(void *opaque, hwaddr offset, unsigned size)
{
    RALINK_RT3883_SOCState *s = opaque;
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
    RALINK_RT3883_SOCState *s = opaque;

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

static void ralink_rt3883_soc_reset(void *opaque)
{
    RALINK_RT3883_SOCState *s = opaque;
    
    s->stub_reserved17[0] = 0x38335452;
    //s->stub_reserved17[0] = 0x0;
    s->stub_reserved2[0] = 0x0;
    s->stub_reserved4[0] = 0x0;
    s->stub_reserved6[0] = 0x0;
    s->stub_reserved7[0] = 0x0;
    s->stub_reserved8[0] = 0x0;
    s->stub_reserved9[0] = 0x0;
    s->stub_reserved10[0] = 0x0;
    s->stub_reserved12[0] = 0x0;
    s->stub_reserved13[0] = 0x0;
    s->stub_reserved14[0] = 0x0;
    s->stub_reserved15[0] = 0x0;
    s->stub_reserved16[0] = 0x0;
    s->stub_reserved0[0] = 0x0;
    s->stub_reserved18[0] = 0x20203338;
    //s->stub_reserved18[0] = 0x0;
}

static void ralink_rt3883_soc_init(MachineState *machine)
{
    RALINK_RT3883_SOCState *s = g_new0(RALINK_RT3883_SOCState, 1);
    Error *err = NULL;
    static struct mips_boot_info binfo;
    
    s->cpu = MIPS_CPU(object_new(machine->cpu_type));
    object_property_set_bool(OBJECT(s->cpu), true, "realized", &err);

    memory_region_allocate_system_memory(&s->ram, OBJECT(machine), "ram", machine->ram_size);
    memory_region_add_subregion_overlap(get_system_memory(), 0, &s->ram, 0);
    
    
    cpu_mips_irq_init_cpu(s->cpu);
    cpu_mips_clock_init(s->cpu);

    //object_initialize(&s->ralink_rt2880_intc0, sizeof(s->ralink_rt2880_intc0), TYPE_RALINK_RT2880_INTC);
    //qdev_set_parent_bus(DEVICE(&s->ralink_rt2880_intc0), sysbus_get_default());
    //object_property_set_bool(OBJECT(&s->ralink_rt2880_intc0), true, "realized", &err);
    //sysbus_mmio_map(SYS_BUS_DEVICE(&s->ralink_rt2880_intc0), 0, 0x10000200);

    //qdev_connect_gpio_out(DEVICE(&s->ralink_rt2880_intc0), 0, s->cpu->env.irq[2]);
    
    set_autoboard_intc_cfg(AUTOBOARD_INTC_RAMIPS_RT3883, "intc");
    object_initialize(&s->autoboard_intc0, sizeof(s->autoboard_intc0), TYPE_AUTOBOARD_INTC);
    qdev_set_parent_bus(DEVICE(&s->autoboard_intc0), sysbus_get_default());
    object_property_set_bool(OBJECT(&s->autoboard_intc0), true, "realized", &err);
    sysbus_mmio_map(SYS_BUS_DEVICE(&s->autoboard_intc0), 0, 0x10000200);

    qdev_connect_gpio_out(DEVICE(&s->autoboard_intc0), 0, s->cpu->env.irq[2]);
    
    object_initialize(&s->timer0, sizeof(s->timer0), TYPE_RALINK_RT2880_TIMER);
    qdev_set_parent_bus(DEVICE(&s->timer0), sysbus_get_default());
    object_property_set_bool(OBJECT(&s->timer0), true, "realized", &err);
    sysbus_mmio_map(SYS_BUS_DEVICE(&s->timer0), 0, 0x10000100);
    
    
    //serial_mm_init_au(get_system_memory(), 0x10000c00, 2, qdev_get_gpio_in(DEVICE(&s->ralink_rt2880_intc0), 12), 115200, serial_hd(0), DEVICE_LITTLE_ENDIAN);
    //serial_mm_init_au(get_system_memory(), 0x10000500, 2, qdev_get_gpio_in(DEVICE(&s->ralink_rt2880_intc0), 5), 115200, serial_hd(1), DEVICE_LITTLE_ENDIAN);
    serial_mm_init_au(get_system_memory(), 0x10000c00, 2, qdev_get_gpio_in(DEVICE(&s->autoboard_intc0), 12), 115200, serial_hd(0), DEVICE_LITTLE_ENDIAN);
    serial_mm_init_au(get_system_memory(), 0x10000500, 2, qdev_get_gpio_in(DEVICE(&s->autoboard_intc0), 5), 115200, serial_hd(1), DEVICE_LITTLE_ENDIAN);
    
    
    memory_region_init_io(&s->stub17_mmio, NULL, &stub17_ops, s, TYPE_RALINK_RT3883_SOC, 0x4);
    memory_region_add_subregion_overlap(get_system_memory(), 0x10000000, &s->stub17_mmio, 0);
    memory_region_init_io(&s->stub2_mmio, NULL, &stub2_ops, s, TYPE_RALINK_RT3883_SOC, 0x10);
    memory_region_add_subregion_overlap(get_system_memory(), 0x10000120, &s->stub2_mmio, 0);
    memory_region_init_io(&s->stub4_mmio, NULL, &stub4_ops, s, TYPE_RALINK_RT3883_SOC, 0x100);
    memory_region_add_subregion_overlap(get_system_memory(), 0x10000300, &s->stub4_mmio, 0);
    memory_region_init_io(&s->stub6_mmio, NULL, &stub6_ops, s, TYPE_RALINK_RT3883_SOC, 0x34);
    memory_region_add_subregion_overlap(get_system_memory(), 0x10000600, &s->stub6_mmio, 0);
    memory_region_init_io(&s->stub7_mmio, NULL, &stub7_ops, s, TYPE_RALINK_RT3883_SOC, 0x24);
    memory_region_add_subregion_overlap(get_system_memory(), 0x10000638, &s->stub7_mmio, 0);
    memory_region_init_io(&s->stub8_mmio, NULL, &stub8_ops, s, TYPE_RALINK_RT3883_SOC, 0x24);
    memory_region_add_subregion_overlap(get_system_memory(), 0x10000660, &s->stub8_mmio, 0);
    memory_region_init_io(&s->stub9_mmio, NULL, &stub9_ops, s, TYPE_RALINK_RT3883_SOC, 0x24);
    memory_region_add_subregion_overlap(get_system_memory(), 0x10000688, &s->stub9_mmio, 0);
    memory_region_init_io(&s->stub10_mmio, NULL, &stub10_ops, s, TYPE_RALINK_RT3883_SOC, 0x100);
    memory_region_add_subregion_overlap(get_system_memory(), 0x10000b00, &s->stub10_mmio, 0);
    memory_region_init_io(&s->stub12_mmio, NULL, &stub12_ops, s, TYPE_RALINK_RT3883_SOC, 0x2710);
    memory_region_add_subregion_overlap(get_system_memory(), 0x10100000, &s->stub12_mmio, 0);
    memory_region_init_io(&s->stub13_mmio, NULL, &stub13_ops, s, TYPE_RALINK_RT3883_SOC, 0x20000);
    memory_region_add_subregion_overlap(get_system_memory(), 0x10140000, &s->stub13_mmio, 0);
    memory_region_init_io(&s->stub14_mmio, NULL, &stub14_ops, s, TYPE_RALINK_RT3883_SOC, 0x9c40);
    memory_region_add_subregion_overlap(get_system_memory(), 0x10180000, &s->stub14_mmio, 0);
    memory_region_init_io(&s->stub15_mmio, NULL, &stub15_ops, s, TYPE_RALINK_RT3883_SOC, 0x1000);
    memory_region_add_subregion_overlap(get_system_memory(), 0x101c0000, &s->stub15_mmio, 0);
    memory_region_init_io(&s->stub16_mmio, NULL, &stub16_ops, s, TYPE_RALINK_RT3883_SOC, 0x1000);
    memory_region_add_subregion_overlap(get_system_memory(), 0x101c1000, &s->stub16_mmio, 0);
    memory_region_init_io(&s->stub0_mmio, NULL, &stub0_ops, s, TYPE_RALINK_RT3883_SOC, 0xf8);
    memory_region_add_subregion_overlap(get_system_memory(), 0x10000008, &s->stub0_mmio, 0);
    memory_region_init_io(&s->stub18_mmio, NULL, &stub18_ops, s, TYPE_RALINK_RT3883_SOC, 0x4);
    memory_region_add_subregion_overlap(get_system_memory(), 0x10000004, &s->stub18_mmio, 0);
    
    memory_region_init_rom(&s->flash, NULL, "boot.flash", 0x400000, &err);
    memory_region_add_subregion_overlap(get_system_memory(), 0x1fc00000, &s->flash, 0);
    ralink_rt3883_soc_reset(s);

    binfo.board_id = 0xFFFFFFFF;
    binfo.ram_size = machine->ram_size;
    binfo.kernel_filename = machine->kernel_filename;
    binfo.kernel_cmdline = machine->kernel_cmdline;
    binfo.initrd_filename = machine->initrd_filename;
    mips_load_kernel(MIPS_CPU(first_cpu), &binfo);
}

static void ralink_rt3883_soc_machine_init(MachineClass *mc)
{
    mc->desc = "ralink_rt3883_soc";
    mc->init = ralink_rt3883_soc_init;
    mc->default_ram_size = 256 * MiB;
    mc->default_cpu_type = MIPS_CPU_TYPE_NAME("74Kf");
    mc->ignore_memory_transaction_failures = false;
}

DEFINE_MACHINE("ralink_rt3883_soc", ralink_rt3883_soc_machine_init)

