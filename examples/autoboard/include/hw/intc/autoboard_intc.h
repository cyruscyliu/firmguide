/*
 * autoboard intc header file
 */

#ifndef TYPE_AUTOBOARD_INTC_H
#define TYPE_AUTOBOARD_INTC_H

#include "hw/sysbus.h"

#define TYPE_AUTOBOARD_INTC "autoboard_intc"
#define AUTOBOARD_INTC(obj) \
    OBJECT_CHECK(AUTOBOARD_INTCState, (obj), TYPE_AUTOBOARD_INTC)

typedef struct irq_bundle {
    uint8_t type;
    void    *stat_mach;
} irq_bundle;

#define STAT_MACH_LEVEL_IRQ   0

typedef struct autoboard_mmio {
    uint32_t mmio_len;
    unsigned char *caches;
    uint32_t (* read)(struct autoboard_mmio *mmio, hwaddr off);
    uint32_t (* write)(struct autoboard_mmio *mmio, hwaddr off, uint64_t val);
} autoboard_mmio;

typedef struct AUTOBOARD_INTCState {
    /*< private >*/
    SysBusDevice sys_bus;

    /*< public >*/

    /*
     * mmio is the memory layout of the ic
     */
    MemoryRegion mmio;

    /*
     * cache of the mmio, internal read & write should use this
     */
    autoboard_mmio *aummio;

    /* 
     * Output to the parent device, usually cpu 
     * 
     * Currently we only use 1 irq connected to the outside
     * however, we could have more than 1 irq line connected with cpu
     * 
     * For out irq:
     * - each out irq has a list of in irqs
     * - each out irq has an index number as its position in the list and
     *     which cpu irq it will connect to
     * 
     * We also prepared several list of in irqs connected to devices:
     * - each list of in irqs has name CPU_X which X is the index of the out irq
     * 
     */
    qemu_irq irq;

    uint32_t in_irq_num;

    /* internal state for every interrupt source */
    irq_bundle *in_irqs;

} AUTOBOARD_INTCState;

#endif /* TYPE_AUTOBOARD_INTC_H */