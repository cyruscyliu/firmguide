{{ license }}

#include "qemu/osdep.h"
#include "qemu/log.h"
#include "hw/sysbus.h"
#include "hw/boards.h"
#include "qemu/units.h"
#include "hw/{{ arch }}/{{ arch }}.h"{% for header in ram_get_header %}
#include "{{ header }}"{% endfor %}{% for header in cpu_get_header %}
#include "{{ header }}"{% endfor %}{% for header in intc_get_header %}
#include "{{ header }}"{% endfor %}{% for header in timer_get_header %}
#include "{{ header }}"{% endfor %}{% for header in serial_get_header %}
#include "{{ header }}"{% endfor %}{% for header in flash_get_header %}
#include "{{ header }}"{% endfor %}{% for header in mmio_get_header %}
#include "{{ header }}"{% endfor %}

#define TYPE_{{ machine_name|to_upper }} "{{  machine_name }}"
#define {{ machine_name|to_upper }}(obj) \
    OBJECT_CHECK({{ machine_name|to_upper }}State, (obj), TYPE_{{ machine_name|to_upper }})

typedef struct {{ machine_name|to_upper }}State {
    {% for line in cpu_get_field %}{{ line }}{% endfor %}{% for line in intc_get_field %}
    {{ line }}{% endfor %}{% for line in timer_get_field %}
    {{ line }}{% endfor %}{% for line in bamboo_get_field %}
    {{ line }}{% endfor %}{% for line in flash_get_field %}
    {{ line }}{% endfor %}{% for line in ram_get_field %}
    {{ line }}{% endfor %}{% for line in mmio_get_registers %}
    {{ line }}{% endfor %}
} {{ machine_name|to_upper }}State;{% for suite in mmio_get_suite %}
{{ suite }}{% endfor %}

static void {{ machine_name }}_reset(void *opaque)
{
    {{ machine_name|to_upper }}State *s = opaque;
    {% for line in mmio_get_reset %}
    {{ line }}{% endfor %}
}

static void {{ machine_name }}_init(MachineState *machine)
{
    {{ machine_name|to_upper }}State *s = g_new0({{ machine_name|to_upper }}State, 1);
    Error *err = NULL;
    static struct {{ arch }}_boot_info binfo;
    {% for line in cpu_get_body %}
    {{ line }}{% endfor %}
    {% for line in ram_get_body  %}
    {{ line }}{% endfor %}
    {% for line in intc_get_body %}
    {{ line }}{% endfor %}
    {% for line in intc_get_connection %}
    {{ line }}{% endfor %}
    {% for line in timer_get_body %}
    {{ line }}{% endfor %}
    {% for line in timer_get_connection %}
    {{ line }}{% endfor %}
    {% for line in serial_get_body %}
    {{ line }}{% endfor %}
    {% for line in misc_get_body %}
    {{ line }}{% endfor %}
    {% for line in bamboo_get_body %}
    {{ line }}{% endfor %}
    {% for line in flash_get_body %}
    {{ line }}{% endfor %}
    {% for line in mmio_get_body %}
    {{ line }}{% endfor %}
    {{ machine_name }}_reset(s);

    binfo.board_id = {{ board_id }};
    binfo.ram_size = machine->ram_size;
    binfo.kernel_filename = machine->kernel_filename;
    binfo.kernel_cmdline = machine->kernel_cmdline;
    binfo.initrd_filename = machine->initrd_filename;
    {{ arch }}_load_kernel({{ arch|to_upper }}_CPU(first_cpu), &binfo);
}

static void {{ machine_name }}_machine_init(MachineClass *mc)
{
    mc->desc = "{{ machine_description }}";
    mc->init = {{ machine_name }}_init;
    mc->default_ram_size =  256 MiB;
    mc->default_cpu_type = {{ arch|to_upper }}_CPU_TYPE_NAME("{{ cpu_get_type }}");
    mc->ignore_memory_transaction_failures = false;
}

DEFINE_MACHINE("{{ machine_name }}", {{ machine_name }}_machine_init)
