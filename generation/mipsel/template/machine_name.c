{{license}}

#include "qemu/osdep.h"
#include "qemu/units.h"
#include "qapi/error.h"
#include "exec/address-spaces.h"
#include "sysemu/blockdev.h"
#include "sysemu/numa.h"
#include "hw/mips/mips.h"
#include "hw/mips/cpudevs.h"
#include "target/mips/cpu.h"
#include "hw/block/flash.h"
#include "hw/mips/{{machine_name}}.h"
#include "hw/mips/{{soc_name}}.h"

#include "qemu/log.h"
#include "hw/mips/bios.h"
#include "hw/ide.h"
#include "hw/loader.h"
#include "elf.h"
#include "hw/timer/mc146818rtc.h"
#include "hw/input/i8042.h"
#include "hw/timer/i8254.h"
#include "exec/address-spaces.h"
#include "sysemu/qtest.h"
#include "qemu/error-report.h"


static void {{machine_name}}_init(MachineState *machine);
static void {{machine_name}}_machine_init(MachineClass *mc);

static struct _loaderparams {
    int ram_size;
    const char *kernel_filename;
    const char *kernel_cmdline;
    const char *initrd_filename;
} loaderparams;

/*
static void mips_qemu_write (void *opaque, hwaddr addr,
                             uint64_t val, unsigned size)
{
    if ((addr & 0xffff) == 0 && val == 42)
        qemu_system_reset_request(SHUTDOWN_CAUSE_GUEST_RESET);
    else if ((addr & 0xffff) == 4 && val == 42)
        qemu_system_shutdown_request(SHUTDOWN_CAUSE_GUEST_SHUTDOWN);
}

static uint64_t mips_qemu_read (void *opaque, hwaddr addr,
                                unsigned size)
{
    return 0;
}

static const MemoryRegionOps mips_qemu_ops = {
    .read = mips_qemu_read,
    .write = mips_qemu_write,
    .endianness = DEVICE_NATIVE_ENDIAN,
};
*/

typedef struct ResetData {
    MIPSCPU *cpu;
    uint64_t vector;
} ResetData;

static int64_t load_kernel(void)
{
    const size_t params_size = 264;
    int64_t entry, kernel_high, initrd_size;
    long kernel_size;
    ram_addr_t initrd_offset;
    uint32_t *params_buf;
    int big_endian;

#ifdef TARGET_WORDS_BIGENDIAN
    big_endian = 1;
#else
    big_endian = 0;
#endif
    kernel_size = load_elf(loaderparams.kernel_filename, NULL,
                           cpu_mips_kseg0_to_phys, NULL,
                           (uint64_t *)&entry, NULL,
                           (uint64_t *)&kernel_high, big_endian,
                           EM_MIPS, 1, 0);
    if (kernel_size >= 0) {
        if ((entry & ~0x7fffffffULL) == 0x80000000)
            entry = (int32_t)entry;
    } else {
        error_report("could not load kernel '%s': %s",
                     loaderparams.kernel_filename,
                     load_elf_strerror(kernel_size));
        exit(1);
    }

    /* load initrd */
    initrd_size = 0;
    initrd_offset = 0;
    if (loaderparams.initrd_filename) {
        initrd_size = get_image_size (loaderparams.initrd_filename);
        if (initrd_size > 0) {
            initrd_offset = (kernel_high + ~INITRD_PAGE_MASK) & INITRD_PAGE_MASK;
            if (initrd_offset + initrd_size > ram_size) {
                error_report("memory too small for initial ram disk '%s'",
                             loaderparams.initrd_filename);
                exit(1);
            }
            initrd_size = load_image_targphys(loaderparams.initrd_filename,
                                              initrd_offset,
                                              ram_size - initrd_offset);
        }
        if (initrd_size == (target_ulong) -1) {
            error_report("could not load initial ram disk '%s'",
                         loaderparams.initrd_filename);
            exit(1);
        }
    }

    /* Store command line.  */
    params_buf = g_malloc(params_size);

    params_buf[0] = tswap32(ram_size);
    params_buf[1] = tswap32(0x12345678);


    if (initrd_size > 0) {
        snprintf((char *)params_buf + 8, 256, "rd_start=0x%" PRIx64 " rd_size=%" PRId64 " %s",
                 cpu_mips_phys_to_kseg0(NULL, initrd_offset),
                 initrd_size, loaderparams.kernel_cmdline);
    } else {
        snprintf((char *)params_buf + 8, 256, "%s", loaderparams.kernel_cmdline);
    }

    rom_add_blob_fixed("params", params_buf, params_size,
                       16 * MiB - params_size);

    g_free(params_buf);
    return entry;
}

static void main_cpu_reset(void *opaque)
{
    ResetData *s = (ResetData *)opaque;
    CPUMIPSState *env = &(s->cpu->env);

    cpu_reset(CPU(s->cpu));
    env->active_tc.PC = s->vector;
}

static void {{machine_name}}_init(MachineState *machine) 
{
    //ram_addr_t ram_size;
    //MemoryRegion *iomem;
    ResetData *reset_info;

    // get machine info
    //iomem = g_new(MemoryRegion, 1);

    /* allocate our machine  */
    {{machine_name|upper}}State *s = g_new0({{machine_name|upper}}State, 1);

    /* initialize the soc */
    object_initialize(&s->soc, sizeof(s->soc), TYPE_{{soc_name|upper}});
    object_property_add_child(OBJECT(machine), "soc", OBJECT(&s->soc), &error_abort);

    /* realize the soc */
    object_property_set_bool(OBJECT(&s->soc), true, "realized", &error_abort);

    /* allocate the ram */
    memory_region_allocate_system_memory(&s->ram, OBJECT(machine), "ram", machine->ram_size);
    memory_region_add_subregion_overlap(get_system_memory(), 0, &s->ram, -1);
    /* memory_region_allocate_system_memory do the same things as below */
    /* object_property_add_child(OBJECT(machine), "ram", OBJECT(&s->ram), &error_abort); */
    /* so, comment the line above */

    //memory_region_init_io(iomem, NULL, &mips_qemu_ops, NULL, "mips-qemu", 0x10000);
    //memory_region_add_subregion(address_space_mem, 0x1fbf0000, iomem);

    reset_info = g_malloc0(sizeof(ResetData));
    reset_info->cpu = s->soc.cpu;
    reset_info->vector = s->soc.cpu->env.active_tc.PC;
    qemu_register_reset(main_cpu_reset, reset_info);

    if (machine->kernel_filename) {
        loaderparams.ram_size = machine->ram_size;
        loaderparams.kernel_filename = machine->kernel_filename;
        loaderparams.kernel_cmdline = machine->kernel_cmdline;
        loaderparams.initrd_filename = machine->initrd_filename;
        reset_info->vector = load_kernel();
    }

    /* Init CPU internal devices */
    cpu_mips_irq_init_cpu(s->soc.cpu);
    cpu_mips_clock_init(s->soc.cpu);
}

static void {{machine_name}}_machine_init(MachineClass *mc) 
{
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
    /* mc->max_cpus = ;*/
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
    mc->default_ram_size = {{ram_size}}; /* 1 * GiB[MiB], 1024 * 1024 [* 1024] */
    mc->default_cpu_type = MIPS_CPU_TYPE_NAME("{{cpu_type}}");
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
