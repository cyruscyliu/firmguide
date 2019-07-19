#ifndef {{soc_name|upper}}_H
#define {{soc_name|upper}}_H

#include "hw/arm/arm.h"
#include "hw/sysbus.h"

#define TYPE_{{soc_name|upper}} "{{soc_name}}"
#define {{soc_name|upper}}(obj) \
    OBJECT_CHECK({{soc_name|upper}}State, (obj), TYPE_{{soc_name|upper}})
#define TYPE_{{soc_name|upper}}_CONTROL "{{soc_name}}-control"
#define {{soc_name|upper}}_CONTROL(obj) \
    OBJECT_CHECK({{soc_name|upper}}ControlState, (obj), TYPE_{{soc_name|upper}}_CONTROL)
#define TYPE_{{soc_name|upper}}_PERIPHERALS "{{soc_name}}-peripherals"
#define {{soc_name|upper}}_PERIPHERALS(obj) \
    OBJECT_CHECK({{soc_name|upper}}PeripheralState, (obj),  TYPE_{{soc_name|upper}}_PERIPHERALS)

#define {{soc_name|upper}}_NCPUS {{n_cpus}}

typedef struct {{soc_name|upper}}ControlState {
    /*< private >*/
    SysBusDevice sysbus;
    /*< public >*/

    MemoryRegion mmio;

    /* outputs to CPU cores */
    qemu_irq[{{soc_name|upper}}_NCPUS];
    qemu_fiq[{{soc_name|upper}}_NCPUS];
} {{soc_name|upper}}ControlState;

typedef struct {{soc_name|upper}}PeripheralState {
    /*< private >*/
    SysBusDevice parent_obj;
    /*< public >*/

    MemoryRegion ram_alias[4];
    qemu_irq irq, fiq;
} {{soc_name|upper}}PeripheralState;

typedef struct {{soc_name|upper}}State {
    /*< private >*/
    DeviceState parent_obj;
    /*< public >*/

    char *cpu_type;
    uint32_t enabled_cpus;

    ARMCPU cpus[{{soc_name|upper}}_NCPUS];
    {{soc_name|upper}}ControlState control;
    {{soc_name|upper}}PeripheralState peripherals;
} {{soc_name|upper}}State;

typedef struct {{soc_name|upper}}Class {
    /*< private >*/
    DeviceClass parent_class;
    /*< public >*/

    const char *name;
    const char *cpu_type;
    int clusterid;
} {{soc_name|upper}}Class;

#define {{soc_name|upper}}_CLASS(klass) \
    OBJECT_CLASS_CHECK({{soc_name|upper}}Class, (klass), TYPE_{{soc_name|upper}})
#define {{soc_name|upper}}L_GET_CLASS(obj) \
    OBJECT_GET_CLASS({{soc_name|upper}}Class, (obj), TYPE_{{soc_name|upper}})

#define ERROR_PROPAGATE(errp, err) \
    if (err) { \
        error_propagate(errp, err); \
        return; \
    }

#endif /* {{soc_name|upper}}_H */