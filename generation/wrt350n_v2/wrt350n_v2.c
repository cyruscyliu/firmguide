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
#include "hw/arm/wrt350n_v2.h"
#include "hw/arm/mv88f5181l.h"

static const int wrt350n_v2_board_id = 0x661;

static void wrt350n_v2_init(MachineState *machine);
static void wrt350n_v2_machine_init(MachineClass *mc);

static void wrt350n_v2_init(MachineState *machine) {
    static struct arm_boot_info binfo;
    DriveInfo *dinfo;
    PFlashCFI01 *flash;

    /* allocate our machine  */
    WRT350N_V2State *s = g_new0(WRT350N_V2State, 1);

    /* initialize the soc */
    object_initialize(&s->soc, sizeof(s->soc), TYPE_MV88F5181L);
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
    /* map mv88f5181l_gpio mmio */
    sysbus_mmio_map(SYS_BUS_DEVICE(&s->soc), 0, MV88F5181L_GPIO_MMIO_BASE);
    
    /* map mv88f5181l_cpu_address_map mmio */
    sysbus_mmio_map(SYS_BUS_DEVICE(&s->soc), 1, MV88F5181L_CPU_ADDRESS_MAP_MMIO_BASE);
    
    /* map mv88f5181l_ddr_sdram_controller mmio */
    sysbus_mmio_map(SYS_BUS_DEVICE(&s->soc), 2, MV88F5181L_DDR_SDRAM_CONTROLLER_MMIO_BASE);
    
    /* map mv88f5181l_pins_multiplexing_interface mmio */
    sysbus_mmio_map(SYS_BUS_DEVICE(&s->soc), 3, MV88F5181L_PINS_MULTIPLEXING_INTERFACE_MMIO_BASE);
    
    /* map mv88f5181l_pci_interface mmio */
    sysbus_mmio_map(SYS_BUS_DEVICE(&s->soc), 4, MV88F5181L_PCI_INTERFACE_MMIO_BASE);
    
    /* map mv88f5181l_pcie_interface mmio */
    sysbus_mmio_map(SYS_BUS_DEVICE(&s->soc), 5, MV88F5181L_PCIE_INTERFACE_MMIO_BASE);
    
    /* map mv88f5181l_usb_2_0_controller mmio */
    sysbus_mmio_map(SYS_BUS_DEVICE(&s->soc), 6, MV88F5181L_USB_2_0_CONTROLLER_MMIO_BASE);
    
    /* map mv88f5181l_gigabit_ethernet_controller mmio */
    sysbus_mmio_map(SYS_BUS_DEVICE(&s->soc), 7, MV88F5181L_GIGABIT_ETHERNET_CONTROLLER_MMIO_BASE);
    
    /* map mv88f5181l_cesa mmio */
    sysbus_mmio_map(SYS_BUS_DEVICE(&s->soc), 8, MV88F5181L_CESA_MMIO_BASE);
    
    /* set up the flash */
    dinfo = drive_get(IF_PFLASH, 0, 0);
    flash = pflash_cfi01_register(
            WRT350N_V2_FLASH_ADDR, "flash", WRT350N_V2_FLASH_SIZE,
            dinfo ? blk_by_legacy_dinfo(dinfo): NULL, WRT350N_V2_FLASH_SECT_SIZE,
            4, 0, 0, 0, 0, 0);
    if (!flash) {
        fprintf(stderr, "qemu: Error registering flash memory.\n");
    } else {
        s->flash = flash;
    }

    /* boot */
    binfo.board_id = wrt350n_v2_board_id;
    binfo.ram_size = machine->ram_size;
    binfo.kernel_filename = machine->kernel_filename;
    binfo.kernel_cmdline = machine->kernel_cmdline;
    binfo.initrd_filename = machine->initrd_filename;
    arm_load_kernel(ARM_CPU(first_cpu), &binfo);
}

static void wrt350n_v2_machine_init(MachineClass *mc) {
    /* mc->family = ; */
    /* mc->name = "wrt350n_v2"; */
    /* mc->alias = ; */
    mc->desc = "Linksys WRT350N v2 (MV88F5181L)";
    /* mc->deprecation_reason = ; */
    mc->init = wrt350n_v2_init;
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
    mc->default_cpu_type = ARM_CPU_TYPE_NAME("arm926");
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
DEFINE_MACHINE("wrt350n_v2", wrt350n_v2_machine_init)