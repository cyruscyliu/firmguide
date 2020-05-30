/*
 * autoboard timer clock source device stat machine header file
 */

#ifndef TYPE_AUTOBOARD_CLKSRC_H
#define TYPE_AUTOBOARD_CLKSRC_H

#include "hw/sysbus.h"
#include "hw/timer/autoboard_timer.h"
#include "hw/timer/autoboard_timer_gen.h"
#include "hw/timer/autoboard_timer_utils.h"
#include "hw/misc/autoboard_utils.h"

/*
 * CLKSRC STAT MACHINE
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
    CLKSRC_STAT_OFF = 0,
    CLKSRC_STAT_RUN,
    CLKSRC_STAT_NUM,
    CLKSRC_STAT_INVALID = -1,
} clksrc_stat;

/*
 * 
 */
typedef enum {
    CLKSRC_EVT_OFF = 0,
    CLKSRC_EVT_ON,
    CLKSRC_EVT_INIT,
    CLKSRC_EVT_RESET,
    CLKSRC_HW_EVT_ONE_CYCLE,
    // The following are not valid events
    CLKSRC_ALL_EVT_NUM,
    CLKSRC_EVT_INVALID = -1,
} clksrc_event;

typedef struct clksrc_cfg {
    bool increment;
    auto_config_action *is_off;
    auto_config_action *is_on;
    auto_config_action *is_init;
    auto_config_action *is_reset;
    auto_config_action *do_convert;
} clksrc_cfg;

typedef struct clksrc_stat_mach {
    const char *name;

    clksrc_cfg *cfg;

    clksrc_stat stat;

    AUTOBOARD_TIMERState *s;

    bool on;
    bool increment;
    uint64_t cycles;

    uint32_t progs[CLKSRC_ALL_EVT_NUM];

    uint8_t (* is_evt_off) (struct clksrc_stat_mach *, auto_trifle *);
    uint8_t (* is_evt_on) (struct clksrc_stat_mach *, auto_trifle *);
    uint8_t (* is_evt_init) (struct clksrc_stat_mach *, auto_trifle *);
    uint8_t (* is_evt_reset) (struct clksrc_stat_mach *, auto_trifle *);

    uint8_t (* do_convert) (struct clksrc_stat_mach *, auto_trifle *);

    void (* handle_event)(struct clksrc_stat_mach *, clksrc_event);
    int (* dispatch)(struct clksrc_stat_mach *, auto_trifle *);

    void (* pass_one_cycle)(struct clksrc_stat_mach *);
} clksrc_stat_mach;

clksrc_stat_mach *init_clksrc_stat_mach(AUTOBOARD_TIMERState *s);

#endif /* TYPE_AUTOBOARD_CLKSRC_H */