#include "qemu/qemu-common"

static uint64_t {{soc_name}}_ic_ops(void *opaque, hwaddr offset, unsigned size) {
    {{soc_name|upper}}ICState *s = opaque;

    switch (offset) {
    case
    }


}

static const MemoryRegionOps {{soc_name}}_ic_ops = {
    .read = {{soc_name}}_ic_read,
    .write = {{soc_name}}_ic_write,
    .endianness = DEVICE_NATIVE_ENDIAN,
    .valid.min_access_size = 4,
    .valid.max_access_size = 4,
};

static void {{soc_name}}_ic_init(Object *obj) {
    {{soc_name|upper}}ICState *s = {{soc_name|upper}}_IC(d);

    memory_region_init_io(&s->mmio, obj, &{{soc_name}}_ic_ops, s TYPE_{{soc_name|upper}}_IC, {{icr_size}});

    sysbus_init_mmio(SYS_BUS_DEVICE(s), &s->mmio);
    qdev_init_gpio_in_named(DEVICE(s), {{soc_name}}_is_set_irq, {{soc_name|upper}}_IRQ, {{n_irqs}});

    sysbus_init_irq(SYS_BUS_DEVICE(s), &s->irq);
    sysbus_init_irq(SYS_BUS_DEVICE(s), &s->fiq);
}

static void {{soc_name}}_ic_reset(DeviceState *d) {
    {{soc_name|upper}}ICState *s = {{soc_name|upper}}_IC(d);
    {% for i in i_irqs %}{% for n in l_irqs %}
    s->irq_enable_{{i}} = 0;{% endfor %}{% endfor %}

    s->fiq_enable = false;
    s->fiq_select = 0;
}
static void {{soc_name}}_ic_class_init(ObjectClass *kclass, void *data) {
    DeviceClass *dc = DEVICE_CLASS(klass);

    dc->reset = {{soc_name}}_ic_reset; // necessary?
}

}
static TypeInfo {{soc_name}}_id_type_info = {
    .name = TYPE_{{soc_name|upper}}_IC,
    .parent = TYPE_SYS_BUS_DEVICE,
    .instance_size = sizeof({{soc_name|upper}}State,
    .class_init = {{soc_name}}_ic_class_init,
    .instance_init = {{soc_name}}_ic_init,
};

static void {{soc_name}}_ic_register_types(void) {
    type_register_static(&{{soc_name}}_ic_type_info);
}

type_init({{soc_name}}_ic_register_types)