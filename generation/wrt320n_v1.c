/* 
 * automatically generated, don't change
 */

#include "qemu/osdep.h"
#include "qemu/log.h"
#include "hw/sysbus.h"
#include "hw/mips/cpudevs.h"
#include "exec/address-spaces.h"
#include "hw/char/serial.h"
#include "sysemu/blockdev.h"
#include "hw/block/flash.h"
#include "hw/mips/mips.h"
#include "qemu/units.h"
#include "target/arm/cpu.h"
#include "hw/boards.h"

#define TYPE_WRT320N_V1 "wrt320n_v1"
#define WRT320N_V1(obj) \
    OBJECT_CHECK(WRT320N_V1State, (obj), TYPE_WRT320N_V1)

typedef struct WRT320N_V1State {
    MIPSCPU *cpu;
    MemoryRegion ram;
} WRT320N_V1State;

static void wrt320n_v1_reset(void *opaque)
{
    WRT320N_V1State *s = opaque;
}

static void wrt320n_v1_init(MachineState *machine)
{
    WRT320N_V1State *s = g_new0(WRT320N_V1State, 1);
    Error *err = NULL;
    DriveInfo *dinfo;
    struct mips_boot_info binfo;

    s->cpu = MIPS_CPU(object_new(machine->cpu_type));
    object_property_set_bool(OBJECT(s->cpu), true, "realized", &err);
    cpu_mips_irq_init_cpu(s->cpu);
    cpu_mips_clock_init(s->cpu);
    memory_region_allocate_system_memory(&s->ram, OBJECT(machine), "ram", machine->ram_size);
    memory_region_add_subregion_overlap(get_system_memory(), 0, &s->ram, -1);
    serial_mm_init(get_system_memory(), 0x18000300, 0, s->cpu->env.irq[2], 115200, serial_hd(0), DEVICE_LITTLE_ENDIAN);
    dinfo = drive_get(IF_PFLASH, 0, 0);
    pflash_cfi01_register(0x1c000000, "flash", 32 * MiB, dinfo ? blk_by_legacy_dinfo(dinfo): NULL, 32 * KiB, 4, 0, 0, 0, 0, 0);


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
    /* mc->is_dault = ; */
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