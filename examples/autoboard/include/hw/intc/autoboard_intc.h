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

typedef enum {
    STAT_MACH_EMPTY = 0,
    STAT_MACH_LEVEL_IRQ,
    STAT_MACH_EDGE_IRQ,
} autoboard_stat_mach_type;

typedef struct autoboard_mmio {
    uint32_t mmio_len;
    unsigned char *caches;
    uint32_t (* read)(struct autoboard_mmio *mmio, hwaddr off);
    uint32_t (* write)(struct autoboard_mmio *mmio, hwaddr off, uint64_t val);
} autoboard_mmio;

typedef enum {
    AUTOBOARD_INTC_INVALID = -1,
    AUTOBOARD_INTC_RAMIPS_RT3883,
    AUTOBOARD_INTC_ATH79_GENERIC,
    AUTOBOARD_INTC_KIRKWOOD_GENERIC_ORION,
    AUTOBOARD_INTC_KIRKWOOD_GENERIC_BRIDGE,
    AUTOBOARD_INTC_NUM,
} autoboard_intc_cfg_id;

typedef struct auto_config_one_irq {
    // this chooses the state machine that irq belongs to
    uint8_t irq_type;
    void *irq_stat_mach_cfg;
} auto_config_one_irq;

typedef struct auto_one_intc_cfg {
    auto_config_one_irq *irq_cfgs;
    uint32_t mmio_len;
    uint32_t irq_num;
} auto_one_intc_cfg;

typedef struct AUTOBOARD_INTCState {
    /*< private >*/
    SysBusDevice sys_bus;

    /*< public >*/

    /*
     * currently act irq idx
     */ 
    int32_t act_irq;

    /*
     * string tag used for labeling intc in log
     */
    const char *name;

    /*
     * cfg pointer for autoboard intc
     */
    struct auto_one_intc_cfg *cfg;

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

// this needs to be called before real initialization of an autoboard intc instance
void set_autoboard_intc_cfg(autoboard_intc_cfg_id id, const char *name);

#endif /* TYPE_AUTOBOARD_INTC_H */