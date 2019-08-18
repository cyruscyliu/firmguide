/* 
 * automatically generated, don't change
 */

#include "qemu/osdep.h"
#include "qemu/units.h"
#include "qapi/error.h"
#include "exec/address-spaces.h"
#include "sysemu/blockdev.h"
#include "sysemu/numa.h"
#include "hw/arm/arm.h"
#include "target/arm/cpu.h"
#include "hw/block/flash.h"
#include "hw/arm/nas7820.h"
#include "hw/arm/ox820.h"

static const int nas7820_board_id = 0x480;

static void nas7820_init(MachineState *machine);
static void nas7820_machine_init(MachineClass *mc);

static void nas7820_init(MachineState *machine) 
{
    static struct arm_boot_info binfo;
    DriveInfo *dinfo;

    /* allocate our machine  */
    NAS7820State *s = g_new0(NAS7820State, 1);

    /* initialize the soc */
    object_initialize(&s->soc, sizeof(s->soc), TYPE_OX820);
    object_property_add_child(OBJECT(machine), "soc", OBJECT(&s->soc), &error_abort);

    /* realize the soc */
    object_property_set_bool(OBJECT(&s->soc), true, "realized", &error_abort);

    /* allocate the ram */
    memory_region_allocate_system_memory(&s->ram, OBJECT(machine), "ram", machine->ram_size);
    memory_region_add_subregion_overlap(get_system_memory(), 0, &s->ram, 0);
    /* memory_region_allocate_system_memory do the same things as below */
    /* object_property_add_child(OBJECT(machine), "ram", OBJECT(&s->ram), &error_abort); */
    /* so, comment the line above */

    /* map bamboo devices mmio */
    /* map oxmas782x_gpio mmio */
    sysbus_mmio_map(SYS_BUS_DEVICE(&s->soc), 0, OXMAS782X_GPIO_MMIO_BASE);
    /* map nas782x_pcie mmio */
    sysbus_mmio_map(SYS_BUS_DEVICE(&s->soc), 1, NAS782X_PCIE_MMIO_BASE);
    /* map nas782x_sata mmio */
    sysbus_mmio_map(SYS_BUS_DEVICE(&s->soc), 2, NAS782X_SATA_MMIO_BASE);
    /* map nas782x_gmac mmio */
    sysbus_mmio_map(SYS_BUS_DEVICE(&s->soc), , NAS782X_GMAC_MMIO_BASE);
    /* map nas782x_ehci mmio */
    sysbus_mmio_map(SYS_BUS_DEVICE(&s->soc), 3, NAS782X_EHCI_MMIO_BASE);
    /* map nas782x_pll mmio */
    sysbus_mmio_map(SYS_BUS_DEVICE(&s->soc), , NAS782X_PLL_MMIO_BASE);
    /* map nas782x_reset mmio */
    sysbus_mmio_map(SYS_BUS_DEVICE(&s->soc), , NAS782X_RESET_MMIO_BASE);
    /* map nas782x_rps_timer mmio */
    sysbus_mmio_map(SYS_BUS_DEVICE(&s->soc), , NAS782X_RPS_TIMER_MMIO_BASE);
    /* map nas782x_rps mmio */
    sysbus_mmio_map(SYS_BUS_DEVICE(&s->soc), , NAS782X_RPS_MMIO_BASE);

    /* set up the nand flash */
    dinfo = drive_get(IF_MTD, 0, 0);
    nand_init(dinfo ? blk_by_legacy_dinfo(dinfo): NULL, 0xec, 0x73);

    if (!flash) {
        fprintf(stderr, "qemu: Error registering flash memory.\n");
    }

    /* boot */
    binfo.board_id = nas7820_board_id;
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
    mc->default_ram_size = 32 * MiB; /* 1 * GiB[MiB], 1024 * 1024 [* 1024] */
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
