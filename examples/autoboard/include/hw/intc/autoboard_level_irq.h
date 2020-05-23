/*
 * autoboard level irq stat machine header file
 */

#ifndef TYPE_AUTOBOARD_LVL_IRQ_H
#define TYPE_AUTOBOARD_LVL_IRQ_H

#include "hw/sysbus.h"
#include "hw/intc/autoboard_intc.h"
#include "hw/intc/autoboard_gen.h"
#include "hw/intc/autoboard_utils.h"

/*
 * LEVEL IRQ STAT MACHINE
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
    LVL_STAT_OFF = 0,
    LVL_STAT_IDLE,
    LVL_STAT_ACT,
    LVL_STAT_MSK,
    //LVL_STAT_ACK,
    LVL_STAT_NUM,
    LVL_STAT_INVALID = -1,
} level_irq_stat;

/*
 * currently, we only found the case that msk/unmsk/init is watchable
 * for evt on/off/reset, they are raised by the hardware
 */
typedef enum {
    LVL_EVT_OFF = 0,
    LVL_EVT_ON,
    LVL_EVT_ACT,
    LVL_EVT_DEACT,
    LVL_EVT_MSK,
    // Seems we don't need ack step in hardware as we didn't find any kernel code call ack solely
    //LVL_EVT_ACK,
    LVL_EVT_UNMSK,
    LVL_EVT_RESET,
    LVL_EVT_INIT,
    // The following are not valid events
    LVL_EVT_NUM,
    LVL_EVT_INVALID = -1,
} level_irq_event;

typedef struct level_irq_cfg {
    auto_config_action *is_off;
    auto_config_action *is_on;
    auto_config_action *is_act;
    auto_config_action *is_deact;
    auto_config_action *is_msk;
    auto_config_action *is_unmsk;
    auto_config_action *is_reset;
    auto_config_action *is_init;
    auto_config_action *do_act;
    auto_config_action *do_deact;
} level_irq_cfg;

typedef struct level_irq_stat_mach {
    uint32_t irq_idx;

    level_irq_cfg *cfg;

    level_irq_stat stat;

    AUTOBOARD_INTCState *s;

    uint8_t on;
    uint8_t act;
    uint8_t msk;

    uint8_t (* is_evt_off) (struct level_irq_stat_mach *, auto_trifle *);
    uint8_t (* is_evt_on) (struct level_irq_stat_mach *, auto_trifle *);
    uint8_t (* is_evt_act) (struct level_irq_stat_mach *, auto_trifle *);
    uint8_t (* is_evt_deact) (struct level_irq_stat_mach *, auto_trifle *);
    uint8_t (* is_evt_msk) (struct level_irq_stat_mach *, auto_trifle *);
    uint8_t (* is_evt_unmsk) (struct level_irq_stat_mach *, auto_trifle *);
    uint8_t (* is_evt_reset) (struct level_irq_stat_mach *, auto_trifle *);
    uint8_t (* is_evt_init) (struct level_irq_stat_mach *, auto_trifle *);

    bool (* is_acted) (struct level_irq_stat_mach *);
    uint8_t (* do_act) (struct level_irq_stat_mach *);
    uint8_t (* do_deact) (struct level_irq_stat_mach *);

    void (* handle_event)(struct level_irq_stat_mach *, level_irq_event);
    int (* dispatch)(struct level_irq_stat_mach *, auto_trifle *);

} level_irq_stat_mach;

level_irq_stat_mach *init_level_irq_stat_mach(AUTOBOARD_INTCState *s, uint32_t cfg_idx);

#endif /* TYPE_AUTOBOARD_LVL_IRQ_H */