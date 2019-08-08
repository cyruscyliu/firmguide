{{license}}

#ifndef {{pcie_name|upper}}_H
#define {{pcie_name|upper}}_H

#include "hw/sysbus.h"

#define TYPE_{{pcie_name|upper}} "{{pcie_name}}"
#define {{pcie_name|upper}}(obj) \
    OBJECT_CHECK({{pcie_name|upper|concat}}State, (obj), TYPE_{{pcie_name|upper}})

#define PCIE_DEVICE_AND_VENDOR_ID_REGISTER       0x00
#define PCIE_CLASS_CODE_AND_REVISION_ID_REGISTER 0x08

#define {{pcie_name|upper}}_RAM_SIZE {{pcie_mmio_size}}
#define {{pcie_name|upper}}_RAM_BASE {{pcie_mmio_base}}

typedef struct {{pcie_name|upper|concat}}State {
    /*< private >*/
    SysBusDevice sys_bus;
    /*< public >*/

    MemoryRegion mmio;
    uint32_t device_id;
    uint32_t revision_id;
} {{pcie_name|upper|concat}}State;

#endif /* {{pcie_name|upper}}_H */