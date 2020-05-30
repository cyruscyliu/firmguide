/*
 * autoboard timer auto generated implementation
 */

#include "qemu/osdep.h"

#include "hw/timer/autoboard_timer.h"
#include "hw/timer/autoboard_clkevt.h"
#include "hw/timer/autoboard_clksrc.h"
#include "hw/timer/autoboard_timer_gen.h"
#include "hw/timer/autoboard_timer_utils.h"
#include "hw/misc/autoboard_utils.h"


uint8_t timer_try_process_at_on_acu(AUTOBOARD_TIMERState *s, auto_config_unit *acu, auto_trifle *at)
{
    switch (acu->type) {
        case ACU_DO_WATCH_READ:
        {
            if ((at->type != TRIFLE_KER_READ) || (at->mmio_idx != acu->midx) || (at->off != acu->moff))
                return ACU_ST_MISMATCH;
        }
            break;
        case ACU_DO_WATCH_WRITE:
        {
            if ((at->type != TRIFLE_KER_WRITE) || (at->mmio_idx != acu->midx) || (at->off != acu->moff))
                return ACU_ST_MISMATCH;

            if (!acu->match_write_cnt(s, acu, at))
                return ACU_ST_MISMATCH;
        }
            break;
        case ACU_DO_WATCH_HWEVT:
        {
            if ((at->type != TRIFLE_HW_EVT) || (at->hw_evt != acu->hw_evt))
                return ACU_ST_MISMATCH;
        }
            break;
        case ACU_DO_REACT:
        {
            acu->do_react(s, acu, at);
        }
            break;
        default:
            assert(false && "this should not be executed");
            break;
    }

    return (acu->next) ? (ACU_ST_NEXT) : (ACU_ST_DONE);
}

static auto_config_action wait_hw_evt_clkevt_reset_cfg = {
    .prog = 0,
    .acus = {
        {
            .type = ACU_DO_WATCH_HWEVT,
            .hw_evt = CLKEVT_EVT_RESET,
            .next = 0,
        }
    }
};

static auto_config_action wait_hw_evt_clksrc_reset_cfg = {
    .prog = 0,
    .acus = {
        {
            .type = ACU_DO_WATCH_HWEVT,
            .hw_evt = CLKSRC_EVT_RESET,
            .next = 0,
        }
    }
};

/*
 * for oxnas.generic
 * 
 * we have 2 timers, 1 for clvevt in giv, 1 for clksrc
 * 
 */

#define OXNAS_GENERIC_RPS_LEVEL_IRQ true
#define OXNAS_GENERIC_RPS_INCREMENT false
#define OXNAS_GENERIC_RPS_NS_PER_CYCLE 2560
#define OXNAS_GENERIC_RPS_MMIO_AMOUNT 1
#define OXNAS_GENERIC_RPS_MMIO1 0x40
static uint32_t oxnas_generic_rps_mmio_lens[OXNAS_GENERIC_RPS_MMIO_AMOUNT] = {
   OXNAS_GENERIC_RPS_MMIO1, 
};

static uint8_t oxnas_generic_rps_is_init_func0(AUTOBOARD_TIMERState *s, auto_config_unit *acu, auto_trifle *at)
{
    //printf("[+] match init func0 at->new_val:0x%x %d \n", at->new_val, (at->new_val == (uint32_t)(uint32_t)((1 << 24) - 1)));
    return (at->new_val == (uint32_t)((1 << 24) - 1));
}

static uint8_t oxnas_generic_rps_is_init_func1(AUTOBOARD_TIMERState *s, auto_config_unit *acu, auto_trifle *at)
{
    //printf("[+] match init func1 at->new_val:0x%x result: %d \n", at->new_val, (at->new_val == (uint32_t)(__bit(2) | __bit(6) | __bit(7)));
    return (at->new_val == (uint32_t)(__bit(2) | __bit(6) | __bit(7)));
}

static auto_config_action oxnas_generic_rps_is_init_cfg = {
    .prog = 0,
    .acus = {
        {
            .type = ACU_DO_WATCH_WRITE,
            .midx = 0,
            .moff = 0x20,
            .match_write_cnt = oxnas_generic_rps_is_init_func0,
            .next = 1,
        },
        {
            .type = ACU_DO_WATCH_WRITE,
            .midx = 0,
            .moff = 0x28,
            .match_write_cnt = oxnas_generic_rps_is_init_func1,
            .next = 0,
        },
    }
};

// TODO: this logic can be more clear by only doing necessary conversion when kernel reads
//       should add one more event & partly re-design the stat machine
static uint8_t oxnas_generic_rps_do_convert_func(AUTOBOARD_TIMERState *s, auto_config_unit *acu, auto_trifle *at)
{
    uint32_t midx = 0, moff = 0x24;
    uint32_t cycles = ((clksrc_stat_mach *)(((timer_bundle *)s->clkdev)->stat_mach))->cycles;
    //uint32_t val = s->aummios[acu->midx].read(&s->aummios[acu->midx], acu->moff);
    //printf("[+] uart act write before 0x%x, size %d, value 0x%x\n", acu->moff, 4, val);
    s->aummios[midx].write(s->aummios, moff, (uint32_t)(cycles));
    //printf("[+] uart act write after 0x%x, size %d, value 0x%x\n", acu->moff, 4, val | (uint32_t)(1 << acu->irq));
    return 0;
}

static auto_config_action oxnas_generic_rps_do_convert_cfg = {
    .prog = 0,
    .acus = {
        {
            .type = ACU_DO_REACT,
            .do_react = oxnas_generic_rps_do_convert_func,
            .next = 0,
        }
    }
};

static clksrc_cfg oxnas_generic_rps_timer_cfg = {
    .increment = OXNAS_GENERIC_RPS_INCREMENT,
    .is_off = NULL,
    .is_on = NULL,
    .is_init = &oxnas_generic_rps_is_init_cfg,
    .is_reset = &wait_hw_evt_clksrc_reset_cfg,
    .do_convert = &oxnas_generic_rps_do_convert_cfg,
};

static auto_config_one_timer oxnas_generic_rps_timer_cfgs = {
    .timer_type = STAT_MACH_CLKDEV_SOURCE,
    .timer_stat_mach_cfg = &oxnas_generic_rps_timer_cfg,
};

/*
 * Config Panel
 */

static auto_one_timer_cfg all_timer_cfgs[AUTOBOARD_TIMER_NUM] = {
    [AUTOBOARD_TIMER_OXNAS_GENERIC_RPS] = {
        .timer_cfgs = &oxnas_generic_rps_timer_cfgs,
        .mm_lens = oxnas_generic_rps_mmio_lens,
        .mm_amount = OXNAS_GENERIC_RPS_MMIO_AMOUNT,
        .is_level_irq = OXNAS_GENERIC_RPS_LEVEL_IRQ,
        .ns_per_cycle = OXNAS_GENERIC_RPS_NS_PER_CYCLE,
    },
};

// This init func should be called at the very beginning as it will init the above global variables
auto_one_timer_cfg *get_autoboard_timer_config(autoboard_timer_cfg_id id)
{
    assert(id > AUTOBOARD_TIMER_INVALID && id < AUTOBOARD_TIMER_NUM && "invalid autoboard timer cfg id");
    return &all_timer_cfgs[id];
}