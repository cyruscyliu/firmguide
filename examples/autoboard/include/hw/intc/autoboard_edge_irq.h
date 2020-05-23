/*
 * autoboard edge irq stat machine header file
 */

#ifndef TYPE_AUTOBOARD_EDGE_IRQ_H
#define TYPE_AUTOBOARD_EDGE_IRQ_H

#include "hw/sysbus.h"
#include "hw/intc/autoboard_intc.h"
#include "hw/intc/autoboard_gen.h"
#include "hw/intc/autoboard_utils.h"

/*
 * EDGE IRQ STAT MACHINE
 * 
 * "-" means all the other events
 * 
 *       OFF  IDLE   ACT  MSK 
 * OFF    -    on    on   on
 * IDLE  off    -   pulse msk
 * ACT   off   ack    -   msk
 * MSK   off  unmsk unmsk   -
 * 
 * on reset, set this irq to idle 
 * on init, set this irq to idle if it is in off, otherwise no change?
 * 
 */
typedef enum {
    EDGE_STAT_OFF = 0,
    EDGE_STAT_IDLE,
    EDGE_STAT_ACT,
    EDGE_STAT_MSK,
    EDGE_STAT_NUM,
    EDGE_STAT_INVALID = -1,
} edge_irq_stat;

/*
 * currently, we only found the case that msk/unmsk/init is watchable
 * for evt on/off/reset, they are raised by the hardware
 */
typedef enum {
    EDGE_EVT_OFF = 0,
    EDGE_EVT_ON,
    EDGE_EVT_PULSE,
    EDGE_HW_EVT_PULSE_UP,
    EDGE_HW_EVT_PULSE_DOWN,
    EDGE_EVT_ACK,
    EDGE_EVT_MSK,
    EDGE_EVT_UNMSK,
    EDGE_EVT_RESET,
    EDGE_EVT_INIT,
    // The following are not valid events
    EDGE_EVT_NUM,
    EDGE_EVT_INVALID = -1,
} edge_irq_event;

typedef struct edge_irq_cfg {
    auto_config_action *is_off;
    auto_config_action *is_on;
    auto_config_action *is_pulse;
    auto_config_action *is_ack;
    auto_config_action *is_msk;
    auto_config_action *is_unmsk;
    auto_config_action *is_reset;
    auto_config_action *is_init;
    auto_config_action *do_act;
    auto_config_action *do_deact;
} edge_irq_cfg;

typedef struct edge_irq_stat_mach {
    uint32_t irq_idx;

    edge_irq_cfg *cfg;

    edge_irq_stat stat;

    AUTOBOARD_INTCState *s;

    uint8_t on;
    uint8_t act;
    uint8_t msk;

    uint8_t (* is_evt_off) (struct edge_irq_stat_mach *, auto_trifle *);
    uint8_t (* is_evt_on) (struct edge_irq_stat_mach *, auto_trifle *);
    uint8_t (* is_evt_pulse) (struct edge_irq_stat_mach *, auto_trifle *);
    uint8_t (* is_evt_ack) (struct edge_irq_stat_mach *, auto_trifle *);
    uint8_t (* is_evt_msk) (struct edge_irq_stat_mach *, auto_trifle *);
    uint8_t (* is_evt_unmsk) (struct edge_irq_stat_mach *, auto_trifle *);
    uint8_t (* is_evt_reset) (struct edge_irq_stat_mach *, auto_trifle *);
    uint8_t (* is_evt_init) (struct edge_irq_stat_mach *, auto_trifle *);

    bool (* is_acted) (struct edge_irq_stat_mach *);
    uint8_t (* do_act) (struct edge_irq_stat_mach *);
    uint8_t (* do_deact) (struct edge_irq_stat_mach *);

    void (* handle_event)(struct edge_irq_stat_mach *, edge_irq_event);
    int (* dispatch)(struct edge_irq_stat_mach *, auto_trifle *);

} edge_irq_stat_mach;

edge_irq_stat_mach *init_edge_irq_stat_mach(AUTOBOARD_INTCState *s, uint32_t cfg_idx);

#endif /* TYPE_AUTOBOARD_EDGE_IRQ_H */