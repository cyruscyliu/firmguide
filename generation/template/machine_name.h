{{license}}

#ifndef {{machine_name|upper}}_H
#define {{machine_name|upper}}_H

#include "qemu/osdep.h"
#include "hw/arm/{{soc_name}}.h"
#include "hw/block/flash.h"

#define {{machine_name|upper}}_FLASH_ADDR      {{flash_addr}}
#define {{machine_name|upper}}_FLASH_SIZE      ({{flash_size}})
#define {{machine_name|upper}}_FLASH_SECT_SIZE ({{flash_sect_size}})

#define TYPE_{{machine_name|upper}} "{{machine_name}}"

typedef struct {{machine_name|upper}}State {
    {{soc_name|upper}}State soc;
    MemoryRegion ram;
} {{machine_name|upper}}State;

#endif /* {{machine_name|upper}}_H */