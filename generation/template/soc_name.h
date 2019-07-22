{{license}}

#ifndef {{soc_name|upper}}_H
#define {{soc_name|upper}}_H

#include "hw/sysbus.h"
#include "hw/initc/{{soc_name}}_ic.h"
#include "hw/gpio/{{soc_name}}_gpio"

#define TYPE_{{soc_name|upper}} "{{soc_name}}"
#define {{soc_name|upper}}(obj) \
    OBJECT_CHECK({{soc_name|upper}}State, (obj), TYPE_{{soc_name|upper}})

#define {{soc_name|upper}}_NCPUS {{n_cpus}}

typedef struct {{soc_name|upper}}State {
    /*< private >*/
    DeviceState parent_obj;
    /*< public >*/

    char *cpu_type;
    uint32_t enabled_cpus;

    ARMCPU cpus[{{soc_name|upper}}_NCPUS];
    {{soc_name|upper}}PeripheralState peripherals;
} {{soc_name|upper}}State;

#endif /* {{soc_name|upper}}_H */