/* 
 * automatically generated, don't change
 */

#include "qemu/osdep.h"
#include "qemu/log.h"
#include "hw/sysbus.h"
#include "target/arm/cpu-qom.h"
#include "hw/mips/cpudevs.h"
#include "exec/address-spaces.h"
#include "hw/char/serial.h"
#include "sysemu/blockdev.h"
#include "hw/block/flash.h"
#include "hw/mips/mips.h"
#include "qemu/units.h"
#include "target/mips/cpu.h"
#include "hw/boards.h"

#define TYPE_WRT320N_V1 "wrt320n_v1"
#define WRT320N_V1(obj) \
    OBJECT_CHECK(WRT320N_V1State, (obj), TYPE_WRT320N_V1)

typedef struct WRT320N_V1State {
    MIPSCPU *cpu;
    MemoryRegion ram;
    MemoryRegion bcma_mmio;
    uint32_t bcma_cc_id_register;
    uint32_t bcma_cc_CAP;
    uint32_t bcma_cc_CORECTL;
    uint32_t bcma_cc_CLKDIV;
    uint32_t bcma_cc_erom_register;
    uint32_t bcma_cc_FLASH_CFG;
    uint32_t bcma_cc_uart0_DATA;
    uint32_t bcma_cc_uart0_IMR;
    uint32_t bcma_cc_uart0_FCR;
    uint32_t bcma_cc_uart0_LCR;
    uint32_t bcma_cc_uart0_MCR;
    uint32_t bcma_cc_uart0_LSR;
    uint32_t bcma_cc_uart0_MSR;
    uint32_t bcma_cc_uart0_SCRATCH;
    uint32_t bcma_cc_uart1_DATA;
    uint32_t bcma_cc_uart1_IMR;
    uint32_t bcma_cc_uart1_FCR;
    uint32_t bcma_cc_uart1_LCR;
    uint32_t bcma_cc_uart1_MCR;
    uint32_t bcma_cc_uart1_LSR;
    uint32_t bcma_cc_uart1_MSR;
    uint32_t bcma_cc_uart1_SCRATCH;
    uint32_t bcma_cc_OOBSELOUTA30;
    uint32_t bcma_scan_commoncore_CIA;
    uint32_t bcma_scan_commoncore_CIB;
    uint32_t bcma_scan_commoncore_MP;
    uint32_t bcma_scan_commoncore_SP1;
    uint32_t bcma_scan_commoncore_MW1;
    uint32_t bcma_scan_mipscore_CIA;
    uint32_t bcma_scan_mipscore_CIB;
    uint32_t bcma_scan_mipscore_MP;
    uint32_t bcma_scan_mipscore_SP1;
    uint32_t bcma_scan_mipscore_MW1;
    uint32_t bcma_scan_END;
    uint32_t bcma_mips_core_mips74k_CORECTL;
    uint32_t bcma_mips_core_mips74k_EXCEPTBASE;
    uint32_t bcma_mips_core_mips74k_BIST;
    uint32_t bcma_mips_core_mips74k_INTMASK_INT0;
    uint32_t bcma_mips_core_mips74k_INTMASK_INT1;
    uint32_t bcma_mips_core_mips74k_INTMASK_INT2;
    uint32_t bcma_mips_core_mips74k_INTMASK_INT3;
    uint32_t bcma_mips_core_mips74k_INTMASK_INT4;
    uint32_t bcma_mips_core_mips74k_INTMASK_XXXX;
    uint32_t bcma_mips_core_mips74k_NMIMASK;
    uint32_t bcma_mips_core_mips74k_GPIOSEL;
    uint32_t bcma_mips_core_mips74k_GPIOOUT;
    uint32_t bcma_mips_core_mips74k_GPIOEN;
} WRT320N_V1State;

static void bcma_update(void *opaque)
{
    /* WRT320N_V1State *s = opaque; */
}

static uint64_t bcma_read(void *opaque, hwaddr offset, unsigned size)
{
    WRT320N_V1State *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case 0x0:
        res = s->bcma_cc_id_register;
        break;
    case 0x4:
        res = s->bcma_cc_CAP;
        break;
    case 0x8:
        res = s->bcma_cc_CORECTL;
        break;
    case 0xa4:
        res = s->bcma_cc_CLKDIV;
        break;
    case 0xfc:
        res = s->bcma_cc_erom_register;
        break;
    case 0x128:
        res = s->bcma_cc_FLASH_CFG;
        break;
    case 0x300:
        res = s->bcma_cc_uart0_DATA;
        break;
    case 0x304:
        res = s->bcma_cc_uart0_IMR;
        break;
    case 0x308:
        res = s->bcma_cc_uart0_FCR;
        break;
    case 0x30c:
        res = s->bcma_cc_uart0_LCR;
        break;
    case 0x310:
        res = s->bcma_cc_uart0_MCR;
        break;
    case 0x314:
        res = s->bcma_cc_uart0_LSR;
        break;
    case 0x318:
        res = s->bcma_cc_uart0_MSR;
        break;
    case 0x31c:
        res = s->bcma_cc_uart0_SCRATCH;
        break;
    case 0x400:
        res = s->bcma_cc_uart1_DATA;
        break;
    case 0x404:
        res = s->bcma_cc_uart1_IMR;
        break;
    case 0x408:
        res = s->bcma_cc_uart1_FCR;
        break;
    case 0x40c:
        res = s->bcma_cc_uart1_LCR;
        break;
    case 0x410:
        res = s->bcma_cc_uart1_MCR;
        break;
    case 0x414:
        res = s->bcma_cc_uart1_LSR;
        break;
    case 0x418:
        res = s->bcma_cc_uart1_MSR;
        break;
    case 0x41c:
        res = s->bcma_cc_uart1_SCRATCH;
        break;
    case 0x1100:
        res = s->bcma_cc_OOBSELOUTA30;
        break;
    case 0x2000:
        res = s->bcma_scan_commoncore_CIA;
        break;
    case 0x2004:
        res = s->bcma_scan_commoncore_CIB;
        break;
    case 0x2008:
        res = s->bcma_scan_commoncore_MP;
        break;
    case 0x200c:
        res = s->bcma_scan_commoncore_SP1;
        break;
    case 0x2010:
        res = s->bcma_scan_commoncore_MW1;
        break;
    case 0x2014:
        res = s->bcma_scan_mipscore_CIA;
        break;
    case 0x2018:
        res = s->bcma_scan_mipscore_CIB;
        break;
    case 0x201c:
        res = s->bcma_scan_mipscore_MP;
        break;
    case 0x2020:
        res = s->bcma_scan_mipscore_SP1;
        break;
    case 0x2024:
        res = s->bcma_scan_mipscore_MW1;
        break;
    case 0x2028:
        res = s->bcma_scan_END;
        break;
    case 0x3000:
        res = s->bcma_mips_core_mips74k_CORECTL;
        break;
    case 0x3004:
        res = s->bcma_mips_core_mips74k_EXCEPTBASE;
        break;
    case 0x300c:
        res = s->bcma_mips_core_mips74k_BIST;
        break;
    case 0x3014:
        res = s->bcma_mips_core_mips74k_INTMASK_INT0;
        break;
    case 0x3018:
        res = s->bcma_mips_core_mips74k_INTMASK_INT1;
        break;
    case 0x301c:
        res = s->bcma_mips_core_mips74k_INTMASK_INT2;
        break;
    case 0x3020:
        res = s->bcma_mips_core_mips74k_INTMASK_INT3;
        break;
    case 0x3024:
        res = s->bcma_mips_core_mips74k_INTMASK_INT4;
        break;
    case 0x3028:
        res = s->bcma_mips_core_mips74k_INTMASK_XXXX;
        break;
    case 0x302c:
        res = s->bcma_mips_core_mips74k_NMIMASK;
        break;
    case 0x3040:
        res = s->bcma_mips_core_mips74k_GPIOSEL;
        break;
    case 0x3044:
        res = s->bcma_mips_core_mips74k_GPIOOUT;
        break;
    case 0x3048:
        res = s->bcma_mips_core_mips74k_GPIOEN;
        break;
    }
    return res;
}

static void bcma_write(void *opaque, hwaddr offset, uint64_t val, unsigned size)
{
    WRT320N_V1State *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case 0x0:
        s->bcma_cc_id_register = val;
        break;
    case 0x4:
        s->bcma_cc_CAP = val;
        break;
    case 0x8:
        s->bcma_cc_CORECTL = val;
        break;
    case 0xa4:
        s->bcma_cc_CLKDIV = val;
        break;
    case 0xfc:
        s->bcma_cc_erom_register = val;
        break;
    case 0x128:
        s->bcma_cc_FLASH_CFG = val;
        break;
    case 0x300:
        s->bcma_cc_uart0_DATA = val;
        break;
    case 0x304:
        s->bcma_cc_uart0_IMR = val;
        break;
    case 0x308:
        s->bcma_cc_uart0_FCR = val;
        break;
    case 0x30c:
        s->bcma_cc_uart0_LCR = val;
        break;
    case 0x310:
        s->bcma_cc_uart0_MCR = val;
        break;
    case 0x314:
        s->bcma_cc_uart0_LSR = val;
        break;
    case 0x318:
        s->bcma_cc_uart0_MSR = val;
        break;
    case 0x31c:
        s->bcma_cc_uart0_SCRATCH = val;
        break;
    case 0x400:
        s->bcma_cc_uart1_DATA = val;
        break;
    case 0x404:
        s->bcma_cc_uart1_IMR = val;
        break;
    case 0x408:
        s->bcma_cc_uart1_FCR = val;
        break;
    case 0x40c:
        s->bcma_cc_uart1_LCR = val;
        break;
    case 0x410:
        s->bcma_cc_uart1_MCR = val;
        break;
    case 0x414:
        s->bcma_cc_uart1_LSR = val;
        break;
    case 0x418:
        s->bcma_cc_uart1_MSR = val;
        break;
    case 0x41c:
        s->bcma_cc_uart1_SCRATCH = val;
        break;
    case 0x1100:
        s->bcma_cc_OOBSELOUTA30 = val;
        break;
    case 0x2000:
        s->bcma_scan_commoncore_CIA = val;
        break;
    case 0x2004:
        s->bcma_scan_commoncore_CIB = val;
        break;
    case 0x2008:
        s->bcma_scan_commoncore_MP = val;
        break;
    case 0x200c:
        s->bcma_scan_commoncore_SP1 = val;
        break;
    case 0x2010:
        s->bcma_scan_commoncore_MW1 = val;
        break;
    case 0x2014:
        s->bcma_scan_mipscore_CIA = val;
        break;
    case 0x2018:
        s->bcma_scan_mipscore_CIB = val;
        break;
    case 0x201c:
        s->bcma_scan_mipscore_MP = val;
        break;
    case 0x2020:
        s->bcma_scan_mipscore_SP1 = val;
        break;
    case 0x2024:
        s->bcma_scan_mipscore_MW1 = val;
        break;
    case 0x2028:
        s->bcma_scan_END = val;
        break;
    case 0x3000:
        s->bcma_mips_core_mips74k_CORECTL = val;
        break;
    case 0x3004:
        s->bcma_mips_core_mips74k_EXCEPTBASE = val;
        break;
    case 0x300c:
        s->bcma_mips_core_mips74k_BIST = val;
        break;
    case 0x3014:
        s->bcma_mips_core_mips74k_INTMASK_INT0 = val;
        break;
    case 0x3018:
        s->bcma_mips_core_mips74k_INTMASK_INT1 = val;
        break;
    case 0x301c:
        s->bcma_mips_core_mips74k_INTMASK_INT2 = val;
        break;
    case 0x3020:
        s->bcma_mips_core_mips74k_INTMASK_INT3 = val;
        break;
    case 0x3024:
        s->bcma_mips_core_mips74k_INTMASK_INT4 = val;
        break;
    case 0x3028:
        s->bcma_mips_core_mips74k_INTMASK_XXXX = val;
        break;
    case 0x302c:
        s->bcma_mips_core_mips74k_NMIMASK = val;
        break;
    case 0x3040:
        s->bcma_mips_core_mips74k_GPIOSEL = val;
        break;
    case 0x3044:
        s->bcma_mips_core_mips74k_GPIOOUT = val;
        break;
    case 0x3048:
        s->bcma_mips_core_mips74k_GPIOEN = val;
        break;
    }
    bcma_update(s);
}

static const MemoryRegionOps bcma_ops = {
    .read = bcma_read,
    .write = bcma_write,
    .endianness = DEVICE_NATIVE_ENDIAN,
};

static void wrt320n_v1_reset(void *opaque)
{
    WRT320N_V1State *s = opaque;

    s->bcma_cc_id_register = 0x4716 | 0x10000 | 0x900000 | 0x0000000 | 0x00000000;
    s->bcma_cc_CAP = 0x1 | 0x8 | 0x700 | 0x10000000;
    s->bcma_cc_CORECTL = 0x1 | 0x2 | 0x8;
    s->bcma_cc_CLKDIV = 0xff;
    s->bcma_cc_erom_register = 0x18002000;
    s->bcma_cc_FLASH_CFG = 0x10;
    s->bcma_cc_uart0_DATA = 0x0;
    s->bcma_cc_uart0_IMR = 0x0;
    s->bcma_cc_uart0_FCR = 0x0;
    s->bcma_cc_uart0_LCR = 0x0;
    s->bcma_cc_uart0_MCR = 0x0;
    s->bcma_cc_uart0_LSR = 0x1 << 5 | 0x1 << 6 | 0x1 << 7;
    s->bcma_cc_uart0_MSR = 0x0;
    s->bcma_cc_uart0_SCRATCH = 0x0;
    s->bcma_cc_uart1_DATA = 0x0;
    s->bcma_cc_uart1_IMR = 0x0;
    s->bcma_cc_uart1_FCR = 0x0;
    s->bcma_cc_uart1_LCR = 0x0;
    s->bcma_cc_uart1_MCR = 0x0;
    s->bcma_cc_uart1_LSR = 0x0;
    s->bcma_cc_uart1_MSR = 0x0;
    s->bcma_cc_uart1_SCRATCH = 0x0;
    s->bcma_cc_OOBSELOUTA30 = 0x3;
    s->bcma_scan_commoncore_CIA = 0x1 | 0x0 | 0x0 << 4 | 0x800 << 8 | 0x4BF << 20;
    s->bcma_scan_commoncore_CIB = 0x1 | 0x0 | 0x1 << 4 | 0x1 << 9 | 0x1 << 14 | 0x0 << 19 | 0x23 << 24;
    s->bcma_scan_commoncore_MP = 0x1 | 0x2 | 0x0 << 4;
    s->bcma_scan_commoncore_SP1 = 0x1 | 0x4 | 0x0 << 4 | 0x0 << 6 | 0x0 << 8 | 0x18000 << 12;
    s->bcma_scan_commoncore_MW1 = 0x1 | 0x4 | 0x0 << 4 | 0xC0 | 0x0 << 8 | 0x18001 << 12;
    s->bcma_scan_mipscore_CIA = 0x1 | 0x0 | 0x0 << 4 | 0x82c << 8 | 0x4A7 << 20;
    s->bcma_scan_mipscore_CIB = 0x1 | 0x0 | 0x1 << 4 | 0x1 << 9 | 0x1 << 14 | 0x0 << 19 | 0x23 << 24;
    s->bcma_scan_mipscore_MP = 0x1 | 0x2 | 0x0 << 4;
    s->bcma_scan_mipscore_SP1 = 0x1 | 0x4 | 0x0 << 4 | 0x0 << 6 | 0x0 << 8 | 0x18003 << 12;
    s->bcma_scan_mipscore_MW1 = 0x1 | 0x4 | 0x0 << 4 | 0xC0 | 0x0 << 8 | 0x18004 << 12;
    s->bcma_scan_END = 0x1 | 0xe;
    s->bcma_mips_core_mips74k_CORECTL = 0x0;
    s->bcma_mips_core_mips74k_EXCEPTBASE = 0x0;
    s->bcma_mips_core_mips74k_BIST = 0x0;
    s->bcma_mips_core_mips74k_INTMASK_INT0 = 0x8;
    s->bcma_mips_core_mips74k_INTMASK_INT1 = 0x0;
    s->bcma_mips_core_mips74k_INTMASK_INT2 = 0x0;
    s->bcma_mips_core_mips74k_INTMASK_INT3 = 0x0;
    s->bcma_mips_core_mips74k_INTMASK_INT4 = 0x0;
    s->bcma_mips_core_mips74k_INTMASK_XXXX = 0x0;
    s->bcma_mips_core_mips74k_NMIMASK = 0x0;
    s->bcma_mips_core_mips74k_GPIOSEL = 0x0;
    s->bcma_mips_core_mips74k_GPIOOUT = 0x0;
    s->bcma_mips_core_mips74k_GPIOEN = 0x0;
}

static void wrt320n_v1_init(MachineState *machine)
{
    WRT320N_V1State *s = g_new0(WRT320N_V1State, 1);
    Error *err = NULL;
    DriveInfo *dinfo;
    static struct mips_boot_info binfo;

    s->cpu = MIPS_CPU(object_new(machine->cpu_type));
    object_property_set_bool(OBJECT(s->cpu), true, "realized", &err);
    cpu_mips_irq_init_cpu(s->cpu);
    cpu_mips_clock_init(s->cpu);
    memory_region_allocate_system_memory(&s->ram, OBJECT(machine), "ram", machine->ram_size);
    memory_region_add_subregion_overlap(get_system_memory(), 0, &s->ram, -2);
    serial_mm_init(get_system_memory(), 0x18000300, 0, s->cpu->env.irq[2], 115200, serial_hd(0), DEVICE_LITTLE_ENDIAN);
    dinfo = drive_get(IF_PFLASH, 0, 0);
    pflash_cfi01_register(0x1c000000, "flash", 32 * MiB, dinfo ? blk_by_legacy_dinfo(dinfo): NULL, 32 * KiB, 4, 0, 0, 0, 0, 0);

    memory_region_init_io(&s->bcma_mmio, NULL, &bcma_ops, s, TYPE_WRT320N_V1, 0x5000);
    memory_region_add_subregion_overlap(get_system_memory(), 0x18000000, &s->bcma_mmio, -1);

    wrt320n_v1_reset(s);

    binfo.ram_size = machine->ram_size;
    binfo.kernel_filename = machine->kernel_filename;
    binfo.kernel_cmdline = machine->kernel_cmdline;
    binfo.initrd_filename = machine->initrd_filename;
    mips_load_kernel(MIPS_CPU(first_cpu), &binfo);
}

static void wrt320n_v1_machine_init(MachineClass *mc)
{
    /* mc->family = ; */
    /* mc->name = "wrt320n_v1"; */
    /* mc->alias = ; */
    mc->desc = "Linksys WRT320N v1 (BCM4717A1)";
    /* mc->deprecation_reason = ; */
    mc->init = wrt320n_v1_init;
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
    mc->default_ram_size = 1024 * MiB;
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

DEFINE_MACHINE("wrt320n_v1", wrt320n_v1_machine_init)