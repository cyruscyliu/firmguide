/*
 * autoboard eoi level irq stat machine header file
 */

#ifndef TYPE_AUTOBOARD_EOI_LVL_IRQ_H
#define TYPE_AUTOBOARD_EOI_LVL_IRQ_H

#include "hw/sysbus.h"
#include "hw/intc/autoboard_intc.h"
#include "hw/intc/autoboard_intc_gen.h"
#include "hw/intc/autoboard_intc_utils.h"
#include "hw/misc/autoboard_utils.h"

/*
 * LEVEL EOI IRQ STAT MACHINE
 * 
 * "-" means all the other events
 * 
 *       OFF  IDLE   ACT  MSK 
 * OFF    -    on    on   on
 * IDLE  off    -   act   msk
 * ACT   off  deact   -   msk
 * MSK   off  unmsk unmsk   -
 * 
 * on reset, set this irq to idle 
 * on init, set this irq to idle if it is in off, otherwise no change?
 * 
 */
typedef enum {
    EOI_LVL_STAT_OFF = 0,
    EOI_LVL_STAT_IDLE,
    EOI_LVL_STAT_ACT,
    EOI_LVL_STAT_MSK,
    //EOI_LVL_STAT_ACK,
    EOI_LVL_STAT_NUM,
    EOI_LVL_STAT_INVALID = -1,
} eoi_lvl_irq_stat;

/*
 * currently, we only found the case that msk/unmsk/init is watchable
 * for evt on/off/reset, they are raised by the hardware
 */
typedef enum {
    EOI_LVL_EVT_OFF = 0,
    EOI_LVL_EVT_ON,
    EOI_LVL_EVT_ACT,
    EOI_LVL_EVT_DEACT,
    EOI_LVL_EVT_EOI,
    EOI_LVL_EVT_MSK,
    // Seems we don't need ack step in hardware as we didn't find any kernel code call ack solely
    //EOI_LVL_EVT_ACK,
    EOI_LVL_EVT_UNMSK,
    EOI_LVL_EVT_RESET,
    EOI_LVL_EVT_INIT,
    EOI_LVL_HW_EVT_DOACT,
    EOI_LVL_HW_EVT_DODEACT,
    // The following are not valid events
    EOI_LVL_ALL_EVT_NUM,
    EOI_LVL_EVT_INVALID = -1,
} eoi_lvl_irq_event;

typedef struct eoi_lvl_irq_cfg {
    auto_config_action *is_off;
    auto_config_action *is_on;
    auto_config_action *is_act;
    auto_config_action *is_deact;
    auto_config_action *is_eoi;
    auto_config_action *is_msk;
    auto_config_action *is_unmsk;
    auto_config_action *is_reset;
    auto_config_action *is_init;
    auto_config_action *do_act;
    auto_config_action *do_deact;
} eoi_lvl_irq_cfg;

typedef struct eoi_lvl_irq_stat_mach {
    uint32_t irq_idx;

    eoi_lvl_irq_cfg *cfg;

    eoi_lvl_irq_stat stat;

    AUTOBOARD_INTCState *s;

    uint8_t on;
    uint8_t act;
    uint8_t msk;

    uint32_t progs[EOI_LVL_ALL_EVT_NUM];

    uint8_t (* is_evt_off) (struct eoi_lvl_irq_stat_mach *, auto_trifle *);
    uint8_t (* is_evt_on) (struct eoi_lvl_irq_stat_mach *, auto_trifle *);
    uint8_t (* is_evt_act) (struct eoi_lvl_irq_stat_mach *, auto_trifle *);
    uint8_t (* is_evt_deact) (struct eoi_lvl_irq_stat_mach *, auto_trifle *);
    uint8_t (* is_evt_eoi) (struct eoi_lvl_irq_stat_mach *, auto_trifle *);
    uint8_t (* is_evt_msk) (struct eoi_lvl_irq_stat_mach *, auto_trifle *);
    uint8_t (* is_evt_unmsk) (struct eoi_lvl_irq_stat_mach *, auto_trifle *);
    uint8_t (* is_evt_reset) (struct eoi_lvl_irq_stat_mach *, auto_trifle *);
    uint8_t (* is_evt_init) (struct eoi_lvl_irq_stat_mach *, auto_trifle *);

    bool (* is_acted) (struct eoi_lvl_irq_stat_mach *);
    uint8_t (* do_act) (struct eoi_lvl_irq_stat_mach *, auto_trifle *);
    uint8_t (* do_deact) (struct eoi_lvl_irq_stat_mach *, auto_trifle *);

    void (* handle_event)(struct eoi_lvl_irq_stat_mach *, eoi_lvl_irq_event);
    int (* dispatch)(struct eoi_lvl_irq_stat_mach *, auto_trifle *);

} eoi_lvl_irq_stat_mach;

eoi_lvl_irq_stat_mach *init_eoi_lvl_irq_stat_mach(AUTOBOARD_INTCState *s, uint32_t cfg_idx);

#endif /* TYPE_AUTOBOARD_EOI_LVL_IRQ_H */