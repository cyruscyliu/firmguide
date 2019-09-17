{{license}}

#ifndef {{machine_name|upper}}_H
#define {{machine_name|upper}}_H

#include "qemu/osdep.h"
#include "hw/mips/{{soc_name}}.h"
#include "hw/block/flash.h"

#define TYPE_{{machine_name|upper}} "{{machine_name}}"

typedef struct {{machine_name|upper}}State {
    {{soc_name|upper}}State soc;
    MemoryRegion ram;
} {{machine_name|upper}}State;

#endif /* {{machine_name|upper}}_H */
