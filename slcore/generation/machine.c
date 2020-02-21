{{ license }}

#include "qemu/osdep.h"
#include "qemu/log.h"
#include "hw/sysbus.h"
#include "hw/boards.h"
#include "qemu/units.h"
#include "hw/{{ arch }}/{{ arch }}.h"
#include "exec/address-spaces.h"{% for header in cpu_get_header %}
#include "{{ header }}"{% endfor %}{% for header in intc_get_header %}
#include "{{ header }}"{% endfor %}{% for header in serial_get_header %}
#include "{{ header }}"{% endfor %}

#define TYPE_{{ machine_name|upper }} "{{  machine_name }}"
#define {{ machine_name|upper }}(obj) \
    OBJECT_CHECK({{ machine_name|upper }}State, (obj), TYPE_{{ machine_name|upper }})

typedef struct {{ machine_name|upper }}State {
    {% for cpu_field in cpu_get_field %}{{ cpu_field }}{% endfor %}{% for intc_field in intc_get_field %}
    {{ intc_field }}{% endfor %}{% for bamboo_field in bamboo_get_field %}
    {{ bamboo_field }}{% endfor %}
    MemoryRegion ram;
} {{ machine_name|upper }}State;{% for suite in bamboo_get_suite %}
{{ suite }}{% endfor %}

static void {{ machine_name }}_reset(void *opaque)
{
    {{ machine_name|upper }}State *s = opaque;
    {% for line in reset_get_field %}
    {{ line }}{% endfor %}
}

static void {{ machine_name }}_init(MachineState *machine)
{
    {{ machine_name|upper }}State *s = g_new0({{ machine_name|upper }}State, 1);
    Error *err = NULL;
    static struct {{ arch }}_boot_info binfo;
    {% for line in cpu_get_body %}
    {{ line }}{% endfor %}

    memory_region_allocate_system_memory(&s->ram, OBJECT(machine), "ram", machine->ram_size);
    memory_region_add_subregion_overlap(get_system_memory(), 0, &s->ram, {{ ram_get_priority }});
    {% for line in intc_get_body %}
    {{ line }}{% endfor %}
    {% for line in serial_get_body %}
    {{ line }}{% endfor %}
    {% for line in bamboo_get_body %}
    {{ line }}{% endfor %}
    {{ machine_name }}_reset(s);

    binfo.board_id = {{ board_id }};
    binfo.ram_size = machine->ram_size;
    binfo.kernel_filename = machine->kernel_filename;
    binfo.kernel_cmdline = machine->kernel_cmdline;
    binfo.initrd_filename = machine->initrd_filename;
    {{ arch }}_load_kernel({{ arch|upper }}_CPU(first_cpu), &binfo);
}

static void {{ machine_name }}_machine_init(MachineClass *mc)
{
    mc->desc = "{{ machine_description }}";
    mc->init = {{ machine_name }}_init;
    mc->default_ram_size = {{ ram_get_size }};
    mc->default_cpu_type = "{{ cpu_get_type}}";
    mc->ignore_memory_transaction_failures = false;
}

DEFINE_MACHINE("{{ machine_name }}", {{ machine_name }}_machine_init)

