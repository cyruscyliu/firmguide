/*
 * autoboard timer clock event device stat machine header file
 */

#ifndef TYPE_AUTOBOARD_CLKDEV_H
#define TYPE_AUTOBOARD_CLKDEV_H

#include "hw/sysbus.h"
#include "hw/timer/autoboard_timer.h"
#include "hw/timer/autoboard_timer_gen.h"
#include "hw/timer/autoboard_timer_utils.h"
#include "hw/misc/autoboard_utils.h"

/*
 * CLKEVT STAT MACHINE
 * 
 * "-" means all the other events
 * 
 *             OFF   UNUSED  PERIO  ONESHOT 
 * OFF                                     
 * UNUSED                                  
 * PERIO                                  
 * ONESHOT                                
 * 
 */
typedef enum {
    CLKEVT_STAT_OFF = 0,
    CLKEVT_STAT_UNUSED,
    CLKEVT_STAT_PERIODIC,
    CLKEVT_STAT_ONESHOT,
    // TODO: for ACK EVT, actually the behaviors are different when 
    //       clkevt device works on different stats (oneshot/perio/...)
    //       we should consider introduce more detail stats to supp this when free
    //       now there only has timer running on periodic mode as far as I know
    CLKEVT_STAT_NUM,
    CLKEVT_STAT_INVALID = -1,
} clkevt_stat;

/*
 * 
 */
typedef enum {
    CLKEVT_EVT_OFF = 0,
    CLKEVT_EVT_ON,
    CLKEVT_EVT_INIT,
    CLKEVT_EVT_RESET,
    CLKEVT_EVT_SET_UNUSED,
    CLKEVT_EVT_SET_PERIO,
    CLKEVT_EVT_SET_ONESHOT,
    CLKEVT_EVT_ACK,
    CLKEVT_EVT_ONESHOT_SET_NEXT,
    CLKEVT_HW_EVT_ONE_CYCLE,
    // The following are not valid events
    CLKEVT_ALL_EVT_NUM,
    CLKEVT_EVT_INVALID = -1,
} clkevt_event;

typedef struct clkevt_cfg {
    auto_config_action *is_off;
    auto_config_action *is_on;
    auto_config_action *is_init;
    auto_config_action *is_reset;
    auto_config_action *is_set_unused;
    auto_config_action *is_set_perio;
    auto_config_action *is_set_oneshot;
    auto_config_action *is_ack;
    auto_config_action *is_oneshot_set_next;
} clkevt_cfg;

typedef struct clkevt_stat_mach {
    uint32_t clk_idx;

    const char *name;

    clkevt_cfg *cfg;

    clkevt_stat stat;

    AUTOBOARD_TIMERState *s;

    bool on;
    bool enable;
    bool repeat;

    uint32_t delta;
    uint32_t load;
    uint32_t countdown;

    uint32_t step;

    uint32_t progs[CLKEVT_ALL_EVT_NUM];

    uint8_t (* is_evt_off) (struct clkevt_stat_mach *, auto_trifle *);
    uint8_t (* is_evt_on) (struct clkevt_stat_mach *, auto_trifle *);
    uint8_t (* is_evt_init) (struct clkevt_stat_mach *, auto_trifle *);
    uint8_t (* is_evt_reset) (struct clkevt_stat_mach *, auto_trifle *);
    uint8_t (* is_evt_set_unused) (struct clkevt_stat_mach *, auto_trifle *);
    uint8_t (* is_evt_set_perio) (struct clkevt_stat_mach *, auto_trifle *);
    uint8_t (* is_evt_set_oneshot) (struct clkevt_stat_mach *, auto_trifle *);
    uint8_t (* is_evt_ack) (struct clkevt_stat_mach *, auto_trifle *);
    uint8_t (* is_evt_oneshot_set_next) (struct clkevt_stat_mach *, auto_trifle *);

    void (* act_irq) (AUTOBOARD_TIMERState *s);
    void (* deact_irq) (AUTOBOARD_TIMERState *s);

    void (* handle_event)(struct clkevt_stat_mach *, clkevt_event);
    int (* dispatch)(struct clkevt_stat_mach *, auto_trifle *);

    void (* pass_one_cycle)(struct clkevt_stat_mach *);
} clkevt_stat_mach;

clkevt_stat_mach *init_clkevt_stat_mach(AUTOBOARD_TIMERState *s, uint32_t cfg_idx);

#endif /* TYPE_AUTOBOARD_CLKDEV_H */