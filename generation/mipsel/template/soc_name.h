{{license}}

#ifndef {{soc_name|upper}}_H
#define {{soc_name|upper}}_H

#include "hw/mips/mips.h"
#include "hw/sysbus.h"
#include "hw/mips/{{bridge_name}}.h"

#define TYPE_{{soc_name|upper}} "{{soc_name}}"
#define {{soc_name|upper}}(obj) \
    OBJECT_CHECK({{soc_name|upper}}State, (obj), TYPE_{{soc_name|upper}})

typedef struct {{soc_name|upper}}State {
    /*< private >*/
    SysBusDevice sys_bus;
    /*< public >*/

    const char *cpu_type;
    MIPSCPU *cpu;

    {{bridge_name|upper|concat}}State bridge;

} {{soc_name|upper}}State;

#endif /* {{soc_name|upper}}_H */
