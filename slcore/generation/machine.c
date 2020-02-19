{{ license }} 
#include "qemu/osdep.h"
#include "qemu/log.h"
#include "hw/sysbus.h"
#include "hw/boards.h"
#include "qemu/units.h"
#include "hw/{{ arch }}/{{ arch }}.h"
#include "exec/address-spaces.h"
{% for header in cpu_get_header %}#include "{{ header }}"
{% endfor %}{% for header in intc_get_header %}#include "{{ header }}"
{% endfor %}{% for header in serial_get_header %}#include "{{ header }}"
{% endfor %}
#define TYPE_{{ machine_name|upper }} "{{  machine_name }}"
#define {{ machine_name|upper }}(obj) \
    OBJECT_CHECK({{ machine_name|upper }}State, (obj), TYPE_{{ machine_name|upper }})

typedef struct {{ machine_name|upper }}State {
    {% for cpu_field in cpu_get_field %}{{ cpu_field }}
    {% endfor %}{% for intc_field in intc_get_field %}{{ intc_field }}
    {% endfor %}MemoryRegion ram;
} {{ machine_name|upper }}State;

static void {{ machine_name }}_init(MachineState *machine)
{
    {{ machine_name|upper }}State *s = g_new0({{ machine_name|upper }}State, 1);
    Error *err = NULL;
    static struct {{ arch }}_boot_info binfo;

    {% for line in cpu_get_body %}{{ line }}
    {% endfor %}
    memory_region_allocate_system_memory(&s->ram, OBJECT(machine), "ram", machine->ram_size);
    memory_region_add_subregion_overlap(get_system_memory(), 0, &s->ram, {{ ram_get_priority }});

    {% for line in intc_get_body %}{{ line }}
    {% endfor %}
    {% for line in serial_get_body %}{{ line }}
    {% endfor %}
    binfo.board_id = {{ board_id }};
    binfo.ram_size = machine->ram_size;
    binfo.kernel_filename = machine->kernel_filename;
    binfo.kernel_cmdline = machine->kernel_cmdline;
    binfo.initrd_filename = machine->initrd_filename;
    {{ arch }}_load_kernel({{ arch|upper }}_CPU(first_cpu), &binfo);
}

static void {{ machine_name }}_machine_init(MachineClass *mc)
{
    /* mc->family = ; */
    /* mc->name = "{{ machine_name }}"; */
    /* mc->alias = ; */
    mc->desc = "{{ machine_description }}";
    /* mc->deprecation_reason = ; */
    mc->init = {{ machine_name }}_init;
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
    mc->default_ram_size = {{ ram_get_size }};
    mc->default_cpu_type = {{ cpu_get_type}};
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

DEFINE_MACHINE("{{ machine_name }}", {{ machine_name }}_machine_init)

