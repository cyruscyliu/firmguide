{{license}}

#include "qemu/osdep.h"
#include "qemu/log.h"
#include "qapi/error.h"
#include "target/mips/cpu.h"
#include "hw/mips/{{soc_name}}.h"
#include "hw/char/serial.h"
#include "exec/address-spaces.h"

static void {{soc_name}}_init(Object *obj);
static void {{soc_name}}_realize(DeviceState *dev, Error **errp);
static void {{soc_name}}_reset(void *opaque);

static void {{soc_name}}_class_init(ObjectClass *oc, void *data);
static void {{soc_name}}_register_types(void);

static void {{soc_name}}_reset(void *opaque)
{
    {{soc_name|upper|concat}}State *s = opaque;
}

static void {{soc_name}}_init(Object *obj) 
{
    {{soc_name|upper}}State *s = {{soc_name|upper}}(obj);

    /* initialize cpus and add the cpu as soc's child */
    s->cpu_type = MIPS_CPU_TYPE_NAME("{{cpu_type}}");
    s->cpu = MIPS_CPU(object_new(s->cpu_type));

    {% if bridge %}
    /* initialize the bridge */
    sysbus_init_child_obj(obj, "bridge", &s->bridge, sizeof(s->bridge), TYPE_{{bridge_name|upper}});{% endif %}
    
    /* reset */
    {{soc_name}}_reset(s);
}

static void {{soc_name}}_realize(DeviceState *dev, Error **errp) 
{
    {{soc_name|upper}}State *s = {{soc_name|upper}}(dev);

    Error *err = NULL;
    /* realize the cpu */
    object_property_set_bool(OBJECT(s->cpu), true, "realized", &err);
    if (err) {
        error_propagate(errp, err);
        return;
    }

    {% if bridge %}
    /* realize the bridge  */
    object_property_set_bool(OBJECT(&s->bridge), true, "realized", &err);
    if (err) {
	    error_propagate(errp, err);
	    return;
    }
    sysbus_mmio_map_overlap(SYS_BUS_DEVICE(&s->bridge), 0, {{bridge_name|upper}}_MMIO_BASE, -1);

    /* attach the uart to 16550A(8250) */
    if (serial_hd(0)) {
	    serial_mm_init(get_system_memory(), {{uart_mmio_base}}, {{uart_reg_shift}},
			    s->cpu->env.irq[{{uart_irq}}],
			    {{uart_baud_rate}}, serial_hd(0), DEVICE_NATIVE_ENDIAN);
    }
    {% endif %}
}

static void {{soc_name}}_class_init(ObjectClass *oc, void *data) 
{
    DeviceClass *dc = DEVICE_CLASS(oc);

    /* dc->fw_name = ; */
    /* dc->desc = ; */
    /* dc->props = ; */
    /* dc->user_creatable = ; */
    /* dc->hotpluggable = ; */
    /* dc->reset = ; */
    dc->realize = {{soc_name}}_realize;
    /* dc->unrealize = ; */
    /* dc->vmsd = ; */
    /* dc->bus_type = ; */

    /* SysBusDeviceClass sbc = SYS_BUS_DEVICE_CLASS(klass); */

    /* sbc->explicit_ofw_unit_address = ; */
    /* sbc->connect_irq_notifier = ; */
}

static const TypeInfo {{soc_name}}_type_info = {
    .name = TYPE_{{soc_name|upper}},
    .parent = TYPE_SYS_BUS_DEVICE,
    .instance_size = sizeof({{soc_name|upper}}State),
    .instance_init = {{soc_name}}_init,
    /* .class_size = sizeof(SysBusDeviceClass), */
    .class_init = {{soc_name}}_class_init,
};

static void {{soc_name}}_register_types(void) 
{
    type_register_static(&{{soc_name}}_type_info);
}

type_init({{soc_name}}_register_types);
