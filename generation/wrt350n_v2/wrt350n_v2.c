#include "qemu/osdep.h"
#include "hw/arm/mv88f5181L.h"

static void wrt350n_v2_init(MachineState *machine) {

}

static void wrt350n_v2_machine_init(MachineClass *mc) {
    /* mc->family = ; */
    mc->name = "wrt350n_v2"; */
    /* mc->alias = ; */
    mc->desc = "Linksys WRT350N v2 (MV88F5181L)";
    /* mc->deprecation_reason = ; */
    mc->init = wrt350n_v2_init;
    /* mc->reset = ; */
    /* mc->hot_add_cpu = ; */
    /* mc->kvm_type = ; */
    mc->block_default_type = IF_NONE;
    /* mc->units_per_default_bus = ; */
    mc->max_cpus = MV88F5181L_NCPUS;
    /* mc->min_cpus =  */;
    mc->default_cpus = MV88F5181L_NCPUS;
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
    mc->default_ram_size = 1024 * 1024 * 1024;
    mc->default_cpu_type = ARM_CPU_TYPE_NAME("arm926");;
    /* mc->default_kernel_irqchip_split = ; */
    /* mc->option_rom_has_mr = ; */
    /* mc->minimum_page_bits = ; */
    /* mc->has_hotpluggable_cpus = ; */
    mc->ignore_memory_transaction_failures = true;
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
DEFINE_MACHINE("wrt350n_v2", wrt350n_v2_machine_init)