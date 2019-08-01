/* 
 * automatically generated, don't change
 */

#ifndef MV88F5181L_PCIE_H
#define MV88F5181L_PCIE_H

#include "hw/sysbus.h"

#define TYPE_MV88F5181L_PCIE "mv88f5181L_pcie"
#define MV88F5181L_PCIE(obj) \
    OBJECT_CHECK(MV88F5181LPCIEState, (obj), TYPE_MV88F5181L_PCIE)

#define PCIE_DEVICE_AND_VENDOR_ID_REGISTER       0x00
#define PCIE_CLASS_CODE_AND_REVISION_ID_REGISTER 0x08

#define MV88F5181L_PCIE_RAM_SIZE 0x2000
#define MV88F5181L_PCIE_RAM_BASE 0xf1040000

typedef struct MV88F5181LPCIEState {
    /*< private >*/
    SysBusDevice sys_bus;
    /*< public >*/

    MemoryRegion mmio;
    uint32_t device_id;
    uint32_t revision_id;
} MV88F5181LPCIEState;

#endif /* MV88F5181L_PCIE_H */