/*
 * autoboard maybe auto-generated header file
 */

#ifndef TYPE_AUTOBOARD_GEN_H
#define TYPE_AUTOBOARD_GEN_H

#include "hw/intc/autoboard_intc.h"
#include "hw/intc/autoboard_utils.h"

#define MMIO_LEN 0x100
#define AUTOBOARD_IRQ_NUM  1

// type for acu
// acu is for auto config unit
#define ACU_DO_INVALID      0
#define ACU_DO_WATCH_READ   (1 << 0)
#define ACU_DO_WATCH_WRITE  (1 << 1)
#define ACU_DO_WATCH_HWEVT (1 << 2)
#define ACU_DO_REACT        (1 << 3)

#define ACU_IS_DO_WATCH(d)  ((d) & (ACU_DO_WATCH_READ | ACU_DO_WATCH_WRITE | ACU_DO_WATCH_HWEVT))
#define ACU_IS_DO_KER_WATCH(d)  ((d) & (ACU_DO_WATCH_READ | ACU_DO_WATCH_WRITE))
#define ACU_IS_DO_HW_WATCH(d)  ((d) & (ACU_DO_WATCH_HWEVT))
#define ACU_IS_DO_REACT(d)  ((d) & (ACU_DO_REACT))

// status for acu func result
// done with right reaction or match an event
#define ACU_ST_DONE      0
// not match
#define ACU_ST_MISMATCH  1
// in progress
#define ACU_ST_NEXT      2

struct auto_config_unit;

typedef uint8_t (* acu_func) (AUTOBOARD_INTCState *s, struct auto_config_unit *, auto_trifle *);

typedef struct auto_config_unit {
    uint8_t type;

    uint32_t midx;
    uint32_t moff;

    uint32_t irq;

    uint32_t hw_evt;

    // this function actually returns true/false
    acu_func match_write_cnt;
    // this function actually returns nothing
    acu_func do_react;

    uint32_t next;
} auto_config_unit;

typedef struct auto_config_action {
    // progress
    uint32_t prog;

    auto_config_unit acus[];
} auto_config_action;

uint8_t try_process_at_on_acu(AUTOBOARD_INTCState *s, auto_config_unit *acu, auto_trifle *at);

// This init func should be called at the very beginning as it will init the above global variables
auto_one_intc_cfg *get_autoboard_intc_config(autoboard_intc_cfg_id id);

#endif /* TYPE_AUTOBOARD_GEN_H */