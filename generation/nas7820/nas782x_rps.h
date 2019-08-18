/* 
 * automatically generated, don't change
 */

#ifndef NAS782X_RPS_H
#define NAS782X_RPS_H

#include "hw/sysbus.h"

#define TYPE_NAS782X_RPS "nas782x_rps"
#define NAS782X_RPS(obj) \
    OBJECT_CHECK(NAS782XRPSState, (obj),  TYPE_NAS782X_RPS)


#define RPS_STATUS 0x0
#define RPS_RAM_STATUS 0x4
#define RPS_UNMASK 0x8
#define RPS_MASK 0xC

#define NAS782X_RPS_MMIO_SIZE 0x14
#define NAS782X_RPS_MMIO_BASE 0x44400000
#define NAS782X_RPS_IRQ "nas782x_rps_irq"

typedef struct NAS782XRPSState {
    /*< private >*/
    SysBusDevice sys_bus;
    /*< public >*/

    MemoryRegion bridge_mmio;
    qemu_irq irq;

    uint32_t rps_status;
    uint32_t rps_ram_status;
    uint32_t rps_unmask;
    uint32_t rps_mask;
    
} NAS782XRPSState;

#endif /* NAS782X_RPS_H */