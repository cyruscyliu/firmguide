/*
 * autoboard intc header file
 */

#ifndef TYPE_AUTOBOARD_INTC_H
#define TYPE_AUTOBOARD_INTC_H

#include "hw/sysbus.h"
#include "hw/intc/autoboard_intc_utils.h"
#include "hw/misc/autoboard_utils.h"

#define TYPE_AUTOBOARD_INTC "autoboard_intc"
#define AUTOBOARD_INTC(obj) \
    OBJECT_CHECK(AUTOBOARD_INTCState, (obj), TYPE_AUTOBOARD_INTC)

typedef enum {
    STAT_MACH_IRQ_EMPTY = 0,
    STAT_MACH_IRQ_LEVEL,
    STAT_MACH_IRQ_EDGE,
    STAT_MACH_IRQ_EOI_LVL,
} autoboard_irq_stat_mach_type;

typedef struct irq_bundle {
    autoboard_irq_stat_mach_type    type;
    void                            *stat_mach;
} irq_bundle;

typedef enum {
    AUTOBOARD_INTC_INVALID = -1,
    AUTOBOARD_INTC_RAMIPS_RT3883,
    AUTOBOARD_INTC_ATH79_GENERIC,
    AUTOBOARD_INTC_KIRKWOOD_GENERIC_ORION,
    AUTOBOARD_INTC_KIRKWOOD_GENERIC_BRIDGE,
    AUTOBOARD_INTC_OXNAS_GENERIC_GIC,
    AUTOBOARD_INTC_NUM,
} autoboard_intc_cfg_id;

typedef struct auto_config_one_irq {
    // this chooses the state machine that irq belongs to
    uint8_t irq_type;
    void *irq_stat_mach_cfg;
} auto_config_one_irq;

typedef struct auto_one_intc_cfg {
    auto_config_one_irq *irq_cfgs;
    uint32_t *mm_lens;
    uint32_t mm_amount;
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
     * amount of memory region
     */
    int32_t mm_amount;

    /*
     * mmio is the memory layout of the ic
     */
    MemoryRegion *mmios;

    /*
     * cache of the mmio, internal read & write should use this
     */
    autoboard_mmio *aummios;

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

    /* 
     * internal state for every interrupt source 
     */
    uint32_t in_irq_num;
    irq_bundle *in_irqs;

} AUTOBOARD_INTCState;

// this needs to be called before real initialization of an autoboard intc instance
void set_autoboard_intc_cfg(autoboard_intc_cfg_id id, const char *name);

#endif /* TYPE_AUTOBOARD_INTC_H */