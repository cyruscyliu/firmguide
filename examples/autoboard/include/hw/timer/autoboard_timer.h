/*
 * autoboard timer header file
 */

#ifndef TYPE_AUTOBOARD_TIMER_H
#define TYPE_AUTOBOARD_TIMER_H

#include "hw/sysbus.h"
#include "qemu/timer.h"
#include "hw/timer/autoboard_timer_utils.h"
#include "hw/misc/autoboard_utils.h"

#define TYPE_AUTOBOARD_TIMER "autoboard_timer"
#define AUTOBOARD_TIMER(obj) \
    OBJECT_CHECK(AUTOBOARD_TIMERState, (obj), TYPE_AUTOBOARD_TIMER)

typedef enum {
    STAT_MACH_CLKDEV_EMPTY = 0,
    STAT_MACH_CLKDEV_EVENT,
    STAT_MACH_CLKDEV_SOURCE,
} autoboard_clkdev_stat_mach_type;

typedef struct timer_bundle {
    autoboard_clkdev_stat_mach_type     type;
    void                                *stat_mach;
} timer_bundle;

typedef enum {
    AUTOBOARD_TIMER_INVALID = -1,
    //AUTOBOARD_TIMER_RAMIPS_RT3883,
    //AUTOBOARD_TIMER_ATH79_GENERIC,
    //AUTOBOARD_TIMER_KIRKWOOD_GENERIC_ORION,
    //AUTOBOARD_TIMER_KIRKWOOD_GENERIC_BRIDGE,
    AUTOBOARD_TIMER_OXNAS_GENERIC_RPS,
    AUTOBOARD_TIMER_OXNAS_GENERIC_MPTIMER,
    AUTOBOARD_TIMER_NUM,
} autoboard_timer_cfg_id;

typedef struct auto_config_one_timer {
    // this chooses the state machine that timer belongs to
    uint8_t timer_type;
    void *timer_stat_mach_cfg;
} auto_config_one_timer;

typedef struct auto_one_timer_cfg {
    auto_config_one_timer *timer_cfgs;
    uint32_t *mm_lens;
    uint32_t mm_amount;
    bool is_level_irq;
    uint32_t ns_per_cycle;
} auto_one_timer_cfg;

typedef struct AUTOBOARD_TIMERState {
    /*< private >*/
    SysBusDevice sys_bus;
    /*< public >*/

    /*
     * string tag used for labeling intc in log
     */
    const char *name;

    /*
     * cfg pointer for autoboard timer
     */
    struct auto_one_timer_cfg *cfg;

    /*
     * amount of memory region
     */
    int32_t mm_amount;

    /*
     * mmio is the memory layout of the timer
     */
    MemoryRegion *mmios;

    /*
     * cache of the mmio, internal read & write should use this
     */
    autoboard_mmio *aummios;

    /* output of the timer */
    qemu_irq irq;
    bool is_level_irq;

    QEMUTimer *timer;

    uint32_t ns_per_cycle;

    timer_bundle *clkdev;

    void (* act_irq) (struct AUTOBOARD_TIMERState *s);
    void (* deact_irq) (struct AUTOBOARD_TIMERState *s);

} AUTOBOARD_TIMERState;

// this needs to be called before real initialization of an autoboard timer instance
void set_autoboard_timer_cfg(autoboard_timer_cfg_id id, const char *name);

#endif /* TYPE_AUTOBOARD_TIMER_H */