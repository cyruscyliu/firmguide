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
#define ACU_INVALID 0
#define ACU_WATCH   1
#define ACU_REACT   2

// status for acu func result
// done with right reaction or match an event
#define ACU_DONE      0
// not match
#define ACU_MISMATCH  1
// in progress
#define ACU_NEXT      2

struct auto_config_unit;

typedef uint8_t (* acu_func) (AUTOBOARD_INTCState *s, struct auto_config_unit *, write_once *);

typedef struct auto_config_unit {
    acu_func func;

    uint8_t type;
    uint32_t off;
    uint32_t irq;
    uint32_t next;
} auto_config_unit;

typedef struct auto_config_action {
    // progress
    uint32_t prog;

    auto_config_unit acus[];
} auto_config_action;

typedef struct auto_config_one_irq {
    // this chooses the state machine that irq belongs to
    uint8_t irq_type;
    void *irq_stat_mach_cfg;
} auto_config_one_irq;

extern auto_config_one_irq *autoboard_irq_cfgs;
extern uint32_t mmio_len;
extern uint32_t autoboard_irq_num;

// This init func should be called at the very beginning as it will init the above global variables
void init_autoboard_intc_config(void);

#endif /* TYPE_AUTOBOARD_GEN_H */