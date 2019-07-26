{{license}}

#include "qemu/osdep.h"
#include "qemu/units.h"
#include "qapi/error.h"
#include "exec/address-spaces.h"
#include "sysemu/blockdev.h"
#include "sysemu/numa.h"
#include "hw/arm/arm.h"
#include "target/arm/cpu.h"
#include "hw/arm/{{machine_name}}.h"
#include "hw/arm/{{soc_name}}.h"

static const int {{machine_name}}_board_id = {{board_id}};

static void {{machine_name}}_init(MachineState *machine);
static void {{machine_name}}_machine_init(MachineClass *mc);

static void {{machine_name}}_init(MachineState *machine) {
    static struct arm_boot_info binfo;
    DriveInfo *dinfo;
    PFlashCFI01 *flash;

    /* allocate our machine  */
    {{machine_name|upper}}State *s = g_new0({{machine_name|upper}}State, 1);

    /* initialize the soc */
    object_initialize(&s->soc, sizeof(s->soc), TYPE_{{soc_name|upper}});
    object_property_add_child(OBJECT(machine), "soc", OBJECT(&s->soc), &error_abort);

    /* allocate the ram */
    memory_region_allocate_system_memory(&s->ram, OBJECT(machine), "ram", machine->ram_size);
    memory_region_add_subregion_overlap(get_system_memory(), 0, &s->ram, 0);
    /* memory_region_allocate_system_memory do the same things as below */
    /* object_property_add_child(OBJECT(machine), "ram", OBJECT(&s->ram), &error_abort); */
    /* so, comment the last line */
    object_property_add_const_link(OBJECT(&s->soc), "ram", OBJECT(&s->ram), &error_abort);

    /* realize the soc */
    object_property_set_bool(OBJECT(&s->soc), true, "realized", &error_abort);

    /* set up the flash */{% if flash_enable %}
    dinfo = drive_get(IF_PFLASH, 0, 0);
    flash = pflash_cfi01_register(
            {{machine_name|upper}}_FLASH_ADDR, "flash", {{machine_name|upper}}_FLASH_SIZE,
            dinfo ? blk_by_legacy_dinfo(dinfo): NULL, {{machine_name|upper}}_FLASH_SECT_SIZE,
            4, 0, 0, 0, 0, 0);
    if (!flash) {
        fprintf(stderr, "qemu: Error registering flash memory.\n");
    } else {
        s->flash = flash;
        object_property_add_child(OBJECT(machine), "flash", OBJECT(&s->flash), &error_abort);
        object_property_add_const_link(OBJECT(&s->soc), "flash", OBJECT(&s->flash), &error_abort);
    }{% endif %}{% if sd_enable %}/* plugin in sd not implemented yet */ {% endif %}

    /* boot */
    binfo.board_id = {{machine_name}}_board_id;
    binfo.ram_size = machine->ram_size;
    binfo.kernel_filename = machine->kernel_filename;
    binfo.kernel_cmdline = machine->kernel_cmdline;
    binfo.initrd_filename = machine->initrd_filename;
    arm_load_kernel(ARM_CPU(first_cpu), &binfo);
}

static void {{machine_name}}_machine_init(MachineClass *mc) {
    /* mc->family = ; */
    /* mc->name = "{{machine_name}}"; */
    /* mc->alias = ; */
    mc->desc = "{{machine_desc}}";
    /* mc->deprecation_reason = ; */
    mc->init = {{machine_name}}_init;
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
    mc->default_ram_size = {{ram_size}}; /* 1 * GiB[MiB], 1024 * 1024 [* 1024] */
    mc->default_cpu_type = ARM_CPU_TYPE_NAME("{{cpu_type}}");
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
DEFINE_MACHINE("{{machine_name}}", {{machine_name}}_machine_init)