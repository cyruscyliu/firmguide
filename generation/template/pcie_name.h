{{license}}

#ifndef {{pice_name|upper}}_H
#define {{pice_name|upper}}_H

#include "hw/sysbus.h"

#define TYPE_{{pice_name|upper}} "{{pice_name}}"
#define {{pice_name|upper}}(obj) \
    OBJECT_CHECK({{pice_name|upper|concat}}State, (obj), TYPE_{{pice_name|upper}})

#define PCIE_DEVICE_AND_VENDOR_ID_REGISTER       0x00
#define PCIE_CLASS_CODE_AND_REVISION_ID_REGISTER 0x08

#define {{pice_name|upper}}_RAM_SIZE {{pice_ram_size}}
#define {{pice_name|upper}}_RAM_BASE {{pice_ram_base}}

typedef struct {{pice_name|upper|concat}}State {
    /*< private >*/
    SysBusDevice sys_bus;
    /*< public >*/

    MemoryRegion mmio;
    uint32_t device_id;
    uint32_t revision_id;
} {{pice_name|upper|concat}}State;

#endif /* {{pice_name|upper}}_H */