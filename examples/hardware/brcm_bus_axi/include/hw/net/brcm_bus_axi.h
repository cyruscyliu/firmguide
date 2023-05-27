/*
 * simple dual state machine
 */

#ifndef BRCM_BUS_AXI_H
#define BRCM_BUS_AXI_H

#include "hw/sysbus.h"

#define TYPE_BRCM_BUS_AXI "brcm_bus_axi"
#define BRCM_BUS_AXI(obj) \
    OBJECT_CHECK(BRCM_BUS_AXIState, (obj), TYPE_BRCM_BUS_AXI)

typedef struct BRCM_BUS_AXIState {
    /*< private >*/
    SysBusDevice sys_bus;
    /*< public >*/

    MemoryRegion mmio;
    bool bcma_clkctlst_forceht;
} BRCM_BUS_AXIState;

#endif /* BRCM_BUS_AXI_H */
