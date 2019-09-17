/* 
 * automatically generated, don't change
 */

#ifndef BCMA_H
#define BCMA_H

#include "hw/sysbus.h"

#define TYPE_BCMA "bcma"
#define BCMA(obj) \
    OBJECT_CHECK(BCMAState, (obj),  TYPE_BCMA)


#define BCMA_CC_ID_REGISTER 0x0
#define BCMA_CC_EROM_REGISTER 0xfc
#define BCMA_SCAN_STOP_FLAG 0x1000

#define BCMA_MMIO_SIZE 0x2000
#define BCMA_MMIO_BASE 0x18000000
#define BCMA_IRQ "bcma_irq"

typedef struct BCMAState {
    /*< private >*/
    SysBusDevice sys_bus;
    /*< public >*/

    MemoryRegion bridge_mmio;
    qemu_irq irq;

    uint32_t bcma_cc_id_register;
    uint32_t bcma_cc_erom_register;
    uint32_t bcma_scan_stop_flag;
    
} BCMAState;

#endif /* BCMA_H */
